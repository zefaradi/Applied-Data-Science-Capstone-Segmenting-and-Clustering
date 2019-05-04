
# coding: utf-8

# In[ ]:


# @hidden_cell
# The project token is an authorization token that is used to access project resources like data sources, connections, and used by platform APIs.
from project_lib import Project
project = Project(project_id='06f49202-4489-470e-bfb5-1700da2bffa6', project_access_token='p-6b7f03e3905bc15e328e5eef8df43dac155ed8e4')
pc = project.project_context


# # Peer-graded Assignment: Segmenting and Clustering Neighborhoods in Toronto

# In[1]:


import numpy as np # library to handle data in a vectorized manner

import pandas as pd # library for data analsysis


# In[2]:


import requests
from pandas import DataFrame
from tabulate import tabulate
from bs4 import BeautifulSoup

df=pd.read_html('https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M')[0]
df.head()


# In[3]:


#Renaming columns

df.columns = ['Postcode','Borough','Neighbourhood']
df.head()


# In[4]:


#Delete the first row with index 0

df1 = df.drop(df.index[0])
df1.head()


# In[5]:


#Deleting rows that doesn't have an assignd Borough
df2 = df1[df1.Borough != 'Not assigned']
df2.head()


# In[6]:


#If a cell has a borough but a Not assigned neighborhood, then the neighborhood will be the same as the borough.
pd.options.mode.chained_assignment = None

df2.Neighbourhood[df2.Neighbourhood == "Not assigned"] = df2.Borough

df2.head(10)


# In[7]:


# Combining Neighbourhoods with the same Boroughs

df3 = df2.groupby(['Postcode','Borough'])['Neighbourhood'].agg(lambda x: tuple(x)).reset_index()
df3.head()


# In[8]:


# Combining Neighbourhoods with the same Boroughs

df3 = df2.groupby(['Postcode','Borough'])['Neighbourhood'].agg(lambda x: tuple(x)).reset_index()
df3.head()

