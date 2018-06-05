#!/usr/bin/python3
"""DOCSTRING."""

if __name__ == '__main__':
    import datetime
    import logging
    import psycopg2
    import inbound_functions
    import inbound_config
    import sys
    import pdb
    import os

    try:
        # create path to logfile
        logfile = '/'.join([inbound_config.logpath, '%s.log' % datetime.date.today()])
        logging.basicConfig(level=logging.INFO, filename=logfile)

        logging.info('Start')

        # Connect to DWH
        conn = psycopg2.connect(dbname=inbound_config.dbname,
                                host=inbound_config.host,
                                port=inbound_config.port,
                                user=inbound_config.user,
                                password=inbound_config.password)
        cur = conn.cursor()
        logging.info('Connected to DWH.')
	    
        # Insert into control table
        cur.execute(inbound_config.insert_into_control_table)
        cur.execute(inbound_config.update_integ_fail_control_table)
        logging.info('Inserted in control table')

        # Insert into tmp table
        cur.execute(inbound_config.insert_into_tmp_table)
        logging.info('Inserted in tmp table')

        cur.execute(inbound_config.update_integ_fail)
        result_cnpjs = cur.fetchall()
        cnpjs = [line[0] for line in result_cnpjs]
	
    	if os.path.isfile('/home/dbm/production/inbound/files/DB_API_INBOUND.csv'):
    		logging.info('Delete old files.')
           	os.remove('/home/dbm/production/inbound/files/DB_API_INBOUND.csv')

        i = 0
        while i < len(cnpjs):
            for cnpj in cnpjs[i:i+15]:

                logging.info('%s - get data' % cnpj)
                # Initialize result dic for query
                result = inbound_config.fields.copy()
                result.update({'cnpj': cnpj})

                try:
                    # Get URL to request in API
                    request_url = inbound_functions.create_request_url(inbound_config.base_url, cnpj)
                    # Send URL and return JSON
                    jsonData = inbound_functions.openUrlJson(request_url)
                    # Check if JSON was submmited correctly

                    if jsonData['ExecutionError'] == True:
                        result.update({'Success': 'True'})
                        # Loga erro no arquivo de logs.
                        logging.info('Invalid CNPJ. Submit Success. Execution Error.')

                        # Create and execute update query
                        queryUnsuccess = cur.mogrify(inbound_config.query_unsuccess, result)
                        cur.execute(queryUnsuccess)
                    else:
                        basic_data = inbound_functions.getData(jsonData)
                        resultEnriched = inbound_functions.putInResult(result, basic_data)
                        logging.info('%s - received data' % cnpj)

                        # Create and execute update query
                        query = cur.mogrify(inbound_config.base_query, resultEnriched)
                        cur.execute(query)

                except Exception as e:
                    logging.error(e)
                    # put success true and Invalid CNPJ
                    query = cur.mogrify(inbound_config.query_unsuccess, result)
                    cur.execute(query)

                logging.info('%s - updated' % cnpj)
                i = i + 1

            # Commit changes
            conn.commit()
            logging.info('commited')

        # update control table submit success
        cur.execute(inbound_config.update_control_table_submit_success)

        # query to select acc to update in SF
        cur.execute(inbound_config.query_to_upload_in_sf)
        unloadAll = cur.fetchall()

        inbound_functions.addHeader()

        i = 0
        while i != len(unloadAll):
            inbound_functions.appendInCSV(unloadAll[i])
            i += 1

        # Commit changes
        conn.commit()
        logging.info('commited')

        conn.close()
        logging.info('Finished')
    except Exception as e:
        logging.exception('Program not working!')
        sys.exit()
