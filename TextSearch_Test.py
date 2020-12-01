# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

def getdata():
    myfolder='G:\\BI\\Talend\\ML_Use_Cases'
    myfile='trade_tariff_id_text.csv'
    
    mypd=pd.read_csv(myfolder+"\\"+myfile,delimiter='|',header=0,encoding='latin-1')
    
    return mypd


def applyfilter(stringlist,mypd):
    subpd=mypd.copy(deep=True)
    for i in range(0,len(stringlist)):
        subpd=subpd[subpd.iloc[:,4].str.contains(stringlist[i])]
        
    return subpd

def create_sublist(finalpd):
    distinctlist=[]
    mylist=[]
    mydict={}
    for i in range(0,len(finalpd)):
        mylist.append(finalpd.iloc[i,4])
        
    distinctlist=set(mylist)
    distinctlist=list(distinctlist)
    
    sub_wordstring=''
    for i in range(0,len(distinctlist)):
        sub_wordstring=sub_wordstring+' '+distinctlist[i]
        
    sub_wordlist=sub_wordstring.split()
    distinct_wordlist=set(sub_wordlist)
    distinct_wordlist=list(distinct_wordlist)
    
    for i in range(0,len(distinct_wordlist)):
        mydict[distinct_wordlist[i]]=300-sub_wordlist.count(distinct_wordlist[i])
        
    return mydict

if __name__=='__main__':
    
    mypd=getdata()
    mystring='women,wool,trousers'
    stringlist=mystring.split(',')
    #stringlist=['women','trouser','silk']
    finalpd=applyfilter(stringlist,mypd)
    print(finalpd)


