'''
TR Connect Plotting Example

Securities:
IBM: IBM
JNJ: Johnson & Johnson

Measurements:
1751: Net Income 
2001: Cash
3351: total liabilities
3051: short term debt
'''
import os, json,sys
from tr_connect import TR

creds = None

if creds == None:
    cred_path = os.path.join(os.environ['HOME'],'trkeys.json')
    with open(cred_path,'r') as f:
        creds = json.load(f)


tr = TR(creds)
jnj =  tr.query('JNJ','ws.1751','Q')

print jnj

# ibm = tr.query('IBM',1751,'Q']
ibm = tr.query('IBM',['ws.1751','ws.2001','ws.3351'],'Q')

print ibm
print ibm.data.keys()
fig = ibm.plot('ws.1751','Net Income')


