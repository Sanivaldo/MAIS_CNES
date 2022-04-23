#!/usr/bin/env python
# coding: utf-8

# In[13]:


import csv
import pandas as pd
import wget
import zipfile


# In[11]:


url = 'ftp://ftp.datasus.gov.br/cnes/BASE_DE_DADOS_CNES_202201.ZIP'
csv = wget.download(url)


# In[61]:


with zipfile.ZipFile("**diretorio**\\BASE_DE_DADOS_CNES_202201 (1).ZIP") as z:
    print(*z.namelist(),sep="\n")


# In[65]:


with zipfile.ZipFile("**diretorio**\\BASE_DE_DADOS_CNES_202201 (1).ZIP") as z:
    with z.open ('tbEstabelecimento202201.csv')as f:
         microdados_cnae = pd.read_csv(f,sep=';',encoding = 'UTF-8')


# In[66]:


microdados_cnae.head()


# In[67]:


microdados_cnae.columns.values


# In[ ]:





# In[ ]:





# In[ ]:




