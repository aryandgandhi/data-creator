import pyodbc
import sys
import pandas as pd
import time
import random 

myfile = open("pw2.txt")
txt = myfile.readlines()[0:28]
ID = txt[4][14:-2]
PSWD = txt[5][14:-2]
ID_Az = txt[17][20:-2]
PSWD_Az = txt[18][20:-2]
myfile.close()

con = pyodbc.connect('DSN=Snowflake;UID=%s;PWD=%s'% (ID, PSWD))
con.setdecoding(pyodbc.SQL_CHAR, encoding='ISO-8859-1')
cursor=con.cursor()
cursor.execute('''select a.dealer_code,
         coalesce(c.inventory_store_number, a.store_number) as store_number,
         a.doc_number, 
            a.pso_line_item_number,
            a.dealer_customer_number, 
            a.SALES_METHOD as sales_channel,
             b.orig_order_ts::date as order_date,
             a.part_number, 
            a.revised_line_qty as order_qty
        from "OEM_DMD_EXT_CURR_VW" a  
        left join "CPATT_STORAGE_PART_SALES_ORDER_VW" b
            on a.dealer_code = b.dealer_code
            and a.doc_number = b.doc_number
        left join "DDSW_DEALER_HIERARCHY_VW" c
            on a.dealer_code = c.dealer_code 
            and a.store_number = c.store_number 
            and a.part_type = c.part_type
       where a.dealer_code = 'T030'
        and a.forecast_demand_ind <> 'No'   
        and a.effective_flier <> 'Yes' 
         and b.orig_order_ts >= '2022-01-01'
         and b.orig_order_ts <= '2022-06-30'
        and a.revised_line_qty > 0;
        ''')



rows= cursor.fetchall()

part_list_1 = pd.DataFrame.from_records(rows, columns=[col[0] for col in cursor.description])




con = pyodbc.connect('DSN=Snowflake;UID=%s;PWD=%s'% (ID, PSWD))
con.setdecoding(pyodbc.SQL_CHAR, encoding='ISO-8859-1')
cursor=con.cursor()
cursor.execute(''' select ID_PART, PART_TYP_ID AS price, 
PROD_MAJ_CLS_CD AS Major, 
PROD_MNR_CLS_CD AS Minor, 
PARTS_PROD_CD AS ppc  
from "LGCYDB2_V_NACD_PART_PRC_VW"
        ''')



rows= cursor.fetchall()

part_list_2 = pd.DataFrame.from_records(rows, columns=[col[0] for col in cursor.description])


