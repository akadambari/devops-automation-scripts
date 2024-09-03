import pandas as pd
import sys
import json


df=pd.read_csv(sys.argv[1])

print(df)
validation_report_AggGLExtract={}
cnt_failed=0

lst_col=['AMOUNTCREDIT','AMOUNTDEBIT','NET_CREDIT','NET_DEBIT']
for h in lst_col:
 cnt_failed=0
 for i in df[h]:
   d=str(i)
   dec_count=d[::-1].find('.')
   if dec_count > 2:
       print(h)
       print(i)
       cnt_failed=cnt_failed+1

  
 validation_report_AggGLExtract[h]=cnt_failed
  
  

print(validation_report_AggGLExtract)
  
with open('validation_report_AggGLExtract_'+sys.argv[2]+'.txt','w') as fout:
     json.dump(validation_report_AggGLExtract,fout)
      
  
