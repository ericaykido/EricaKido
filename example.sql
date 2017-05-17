CREATE [ [LOCAL ] { TEMPORARY | TEMP } ] TABLE 
[ IF NOT EXISTS ] table_name
( { column_name data_type [column_attributes] [ column_constraints ] 
  | table_constraints
  | LIKE parent_table [ { INCLUDING | EXCLUDING } DEFAULTS ] } 
  [, ... ]  )
[ BACKUP { YES | NO } ]
[table_attribute]

where column_attributes are:
  [ DEFAULT default_expr ]
  [ IDENTITY ( seed, step ) ] 
  [ ENCODE encoding ] 
  [ DISTKEY ]
  [ SORTKEY ]

and column_constraints are:
  [ { NOT NULL | NULL } ]
  [ { UNIQUE  |  PRIMARY KEY } ]
  [ REFERENCES reftable [ ( refcolumn ) ] ] 

and table_constraints  are:
  [ UNIQUE ( column_name [, ... ] ) ]
  [ PRIMARY KEY ( column_name [, ... ] )  ]
  [ FOREIGN KEY (column_name [, ... ] ) REFERENCES reftable [ ( refcolumn ) ] 

and table_attributes are:
  [ DISTSTYLE { EVEN | KEY | ALL } ] 
  [ DISTKEY ( column_name ) ]
  [ [COMPOUND | INTERLEAVED ] SORTKEY ( column_name [, ...] )];


alter table venue
rename column venueseats to venuesize;

CREATE [ OR REPLACE ] FUNCTION f_function_name 
( [argument_name data_type [ , ... ] ] )
RETURNS data_type
{VOLATILE | STABLE | IMMUTABLE }   
AS $$
  python_program
$$ LANGUAGE plpythonu;

select top 10 salesid, sum(pricepaid), 
percentile_cont(0.6) within group (order by salesid),
median (salesid)
from sales group by salesid, pricepaid;

select
  userid
  , query
  , pid
  , starttime
  , left(text, 50) as text
from stv_inflight