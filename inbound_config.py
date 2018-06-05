    # !/usr/bin/python3
"""DOCSTRING."""

logpath =  '/home/dbm/production/logs/dbm_api'

base_url = """https://upgrademe.bigdatacorp.com.br/upgrademe/api/CNPJ%7CDOC=""" # noqa

fields = {
    'cnpj': None,
    'BusinessName': None,
    'OfficialName': None,
    'FoundingDate': None,
    'cnae': None,
    'irs_status': None,
    'legal_nature_code': None,
    'mei': None,
    'simples': None,
    'tax_regime': None,
    'employees_number': None,
    'income': None,
    'AddressCore': None,
    'City': None,
    'Complement': None,
    'Neighborhood': None,
    'Number': None,
    'State': None,
    'ZipCode': None
}

# DWH
# Settings to connect to Loggi DWH
dbname = 'x'
host = 'x'
port = 'x'
user = 'x'
password = 'x'

# Query to update CNPJ that is invalid
query_unsuccess = """
UPDATE dbm.cm3_tmp_api_inbound
SET business_name = 'Invalid CNPJ'
WHERE cnpj = %(cnpj)s
and official_name is not null
"""

# Query to update cnpj with retrieved results from API
base_query = """
UPDATE dbm.cm3_tmp_api_inbound
SET
    cnpj = %(cnpj)s,
    business_name = %(BusinessName)s,
    official_name = %(OfficialName)s,
    founding_date = %(FoundingDate)s,
    cnae = %(cnae)s,
    irs_status = %(irs_status)s,
    legal_nature_code = %(legal_nature_code)s,
    mei = %(mei)s,
    simples = %(simples)s,
    tax_regime = %(tax_regime)s,
    employees_number = %(employees_number)s,
    income = %(income)s,
    address_core = %(AddressCore)s,
    city = %(City)s,
    complement = %(Complement)s,
    neighborhood = %(Neighborhood)s,
    number = %(Number)s,
    state = %(State)s,
    zipcode = %(ZipCode)s
WHERE cnpj = %(cnpj)s;
"""

cnpj_query = """
SELECT cnpj
FROM dbm.cm2_dbm_send_enrichment
WHERE is_updated_dbm is false and submit_success is false and date(submit_date) = date(getdate()) and object = 'sign_up';
"""

update_integ_fail= """
SELECT a.cnpj 
FROM dbm.cm2_dbm_send_enrichment a
LEFT JOIN salesforce.accounts b on a.cnpj = b.cnpj_c  
WHERE is_updated_dbm is false 
and object = 'sign_up'
and sf_id != 'integ_fail'
and date(submit_date) >= date('2018-03-03')
and b.cnae_c is null;
"""

insert_into_control_table="""
insert into dbm.cm2_dbm_send_enrichment
select  case when (date(C.data_da_criacao_c) = date(getdate())) then C.id
            else ( case when (C.id is null) then 'integ_fail' 
                    else C.id
                    end
            ) 
        end as "sf_id",
        A.db_id as "customer_db_id",
        right(dbm.fx_str_trat('00000000000000' || rtrim(ltrim(cnpj))), 14) as "CNPJ",
        'sign_up' as "object",
        date(getdate()) as "submit_date",
        'BDC' as "partner",
        false as "submit_success",
        false as "is_updated_dbm"
from public.sign_up A
left join salesforce.accounts C on A.db_id = (C.id_loggi_c || '.1') and C.is_person_account is false and C.record_type_id = '0121a000000V9W6AAK'
    where
    cnpj in (
        SELECT cnpj
        FROM public.sign_up
        WHERE (date(created) >= date('2018-03-05')
        and account_type = 'Company')
    )
and cnpj not in (select cnpj
                    from dbm.cm2_dbm_send_enrichment)
and account_type = 'Company'
and A.db_id not in (select customer_db_id 
                    from dbm.cm2_dbm_send_enrichment
                    where customer_db_id is not null);
"""

update_integ_fail_control_table="""
UPDATE
    dbm.cm2_dbm_send_enrichment
SET
    sf_id = 
        case when (B.id is null) then 'integ_fail' 
            else B.id
        end
FROM dbm.cm2_dbm_send_enrichment AS A
    INNER JOIN salesforce.accounts AS B
        ON A.cnpj = B.cnpj_c
WHERE
    A.sf_id ='integ_fail' 
and date(A.submit_date) >= date('2018-03-03')
and A.object = 'sign_up';
"""

insert_into_tmp_table="""
insert into dbm.cm3_tmp_api_inbound 
SELECT A.cnpj as "cnpj",
       null as business_name,
       null as official_name,
       null as founding_date,
       null as cnae,
       null as irs_status,
       null as legal_nature_code ,
       null as mei,
       null as simples ,
       null as tax_regime,
       null as employees_number,
       null as income,
       null as address_core,
       null as city,
       null as complement,
       null as neighborhood,
       null as number ,
       null as state,
       null as zipcode
FROM public.sign_up A
LEFT JOIN dbm.cm2_dbm_send_enrichment B on A.cnpj = B.cnpj
WHERE (A.created >= '2018-03-03 00:00:00'
and A.account_type = 'Company'
and date(B.submit_date) >= date('2018-03-03')
and submit_success is false
and B.object = 'sign_up'
and B.sf_id != 'integ_fail'
and A.cnpj not in (select cnpj from dbm.cm3_tmp_api_inbound));
"""

update_control_table_submit_success="""
update dbm.cm2_dbm_send_enrichment
set submit_success = true
where dbm.cm2_dbm_send_enrichment.cnpj in (select cnpj
                                            from dbm.cm3_tmp_api_inbound A
                                            where A.business_name <> 'Invalid CNPJ')
    and dbm.cm2_dbm_send_enrichment.cnpj not in (select cnpj 
                                                    from dbm.cm2_bdc_api_enrichment)
    and dbm.cm2_dbm_send_enrichment.submit_success is false
    and dbm.cm2_dbm_send_enrichment.object = 'sign_up'
    and date(dbm.cm2_dbm_send_enrichment.submit_date) >= date('2018-03-03')
    and dbm.cm2_dbm_send_enrichment.sf_id != 'integ_fail';
"""

query_to_upload_in_sf="""
select  D.id as "id",
    dbm.fx_str_trat(btrim(upper(B.official_name))) as "official_name",
    case when dbm.fx_str_trat(btrim(upper(B.business_name))) is null then '' 
        else dbm.fx_str_trat(btrim(upper(B.business_name)))
    end as "business_name",
    case when left(dbm.fx_str_trat(btrim(B.cnae)),7) is null then ''
        else left(dbm.fx_str_trat(btrim(B.cnae)),7)
    end as "cnae", 
    case when dbm.fx_str_trat(rtrim(ltrim(upper(C.desc_cnae)))) is null then ''
        else dbm.fx_str_trat(rtrim(ltrim(upper(C.desc_cnae))))
    end as "cnae_descricao", 
    case when B.tax_regime is null then ''
        else B.tax_regime
    end as "tax_regime", 
    case when B.employees_number is null then ''
        else B.employees_number
    end as "employees_number", 
    case when B.income is null then ''
        else B.income
    end as "income", 
    case when B.irs_status in ('ATIVA','ATIVO') then 'ATIVA' 
    end as "irs_status",
    case when D.pr_qualifier_c is null then 'DBM-API'
        else D.pr_qualifier_c
    end as "pr_qualifier",
    case when D.origem_c is null then 'Database'
        else D.origem_c
    end as "lead_source",
    date(getdate()) as "dbm_date"
--into dbm.temp_load_api
from dbm.cm3_tmp_api_inbound B
left join dbm.cm3_dm_cnae C on left(dbm.fx_str_trat(btrim(B.cnae)),7) = C.cnae
left join salesforce.accounts D on B.cnpj = D.cnpj_c and D.is_person_account is false and D.record_type_id = '0121a000000V9W6AAK'
left join dbm.cm2_dbm_send_enrichment A on A.cnpj = B.cnpj
    where
	A.submit_success = 'True'
    	and A.is_updated_dbm is false
    	and date(A.submit_date) >= date('2018-03-03')
   	and D.id is not null
    	and B.official_name is not null
    	group by D.id,B.official_name, B.business_name, B.tax_regime, B.employees_number, B.income, B.cnae, C.desc_cnae, B.irs_status,  D.pr_qualifier_c,D.origem_c, D.status_qualifier_c, D.fase_c,B.AreaCode, B.Phone;
"""

update_control_table_is_updated_dbm="""
update dbm.cm2_dbm_send_enrichment
    set is_updated_dbm = true
    where cnpj not in (select cnpj 
                        from dbm.cm3_tmp_api_inbound 
                        where business_name != 'Invalid CNPJ')
    and submit_success is True
    and sf_id <> 'integ_fail'
    and date(submit_date) >= date('2018-03-03')
    and is_updated_dbm is false;
"""
