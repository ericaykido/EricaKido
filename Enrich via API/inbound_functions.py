# !/usr/bin/python3
"""DOCSTRING."""

import json
import requests
import logging
import smtplib
import csv
import pdb

def create_request_url(base_url, cnpj):
    """Concatenate base url and cnpj."""
    request_url = '%s%s' % (base_url, cnpj)
    return request_url

# Open URL and return json
def openUrlJson(request_url):
    try:
        response = requests.get(request_url)
        jsonData = response.json()
        return jsonData
    except Exception as e:
        # Log if there is timeout
        logging.error(e)

# Get data from JSON and put in array
def getData(jsonData):
    """DOCSTRING."""
    # Tranform String in JSON

    entities = json.loads(jsonData['OperationResult'])
    # check if results are empty
    if not entities.get('Entities')[0].get('Companies'):
        raise ValueError('CNPJ not found. Empty result. Basic Data.')
    else :
        
        data = ['']*19

        for array_data in entities.get('Entities'):
            for basic_data in array_data.get('Companies'):
                
                if basic_data.get('OfficialName'):
                    data[0] = basic_data.get("IdNumber")
                    data[1] = basic_data.get('BusinessName')
                    data[2] = basic_data.get('OfficialName')
                    data[3] = basic_data.get('FoundingDate')
                    
                    extra = basic_data.get('ExtraInformation')
                    
                    for extra_info in extra:
                        if(extra_info.get('Name') == 'cnae'):
                            data[4] = extra_info.get('Value')

                        if(extra_info.get('Name') == 'employees_number'):
                            data[10] = extra_info.get('Value')

                        if(extra_info.get('Name') == 'tax_regime' or extra_info.get('Name') == 'irs_capital'):
                            data[9] = extra_info.get('Value')

                        if(extra_info.get('Name') == 'legal_nature_code'):
                            data[6] = basic_data.get('Value')

                        if(extra_info.get('Name') == 'irs_status'):
                            data[5] = extra_info.get('Value')

                        if(extra_info.get('Name') == 'mei'):
                            data[7] = extra_info.get('Value')

                        if(extra_info.get('Name') == 'simples'):
                            data[8] = extra_info.get('Value')
                else:
                    for contact_data in array_data.get('Companies'):

                        for address_data in contact_data.get('Contacts'):

                            if address_data.get('Address').get('AddressCore'):
                                data[12] = address_data.get('Address').get('AddressCore')
                                data[13] = address_data.get('Address').get('City')
                                data[14] = address_data.get('Address').get('Complement')
                                data[15] = address_data.get('Address').get('Neighborhood')
                                data[16] = address_data.get('Address').get('Number')
                                data[17] = address_data.get('Address').get('State')
                                data[18] = address_data.get('Address').get('ZipCode')

        return data

# update list resutl
def putInResult(result, dataArray):
    result.update({'Key':dataArray[0]})
    result.update({'BusinessName':dataArray[1]})
    result.update({'OfficialName':dataArray[2]})
    result.update({'FoundingDate':dataArray[3]})
    result.update({'cnae':dataArray[4]})
    result.update({'irs_status':dataArray[5]})
    result.update({'legal_nature_code':dataArray[6]})
    result.update({'mei':dataArray[7]})
    result.update({'simples':dataArray[8]})
    result.update({'tax_regime':dataArray[9]})
    result.update({'employees_number':dataArray[10]})
    result.update({'income':dataArray[11]})
    result.update({'AddressCore':dataArray[12]})
    result.update({'City':dataArray[13]})
    result.update({'Complement':dataArray[14]})
    result.update({'Neighborhood':dataArray[15]})
    result.update({'Number':dataArray[16]})
    result.update({'State':dataArray[17]})
    result.update({'ZipCode':dataArray[18]})
    return result