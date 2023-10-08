#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


df = pd.read_csv('laadpaaldata.csv')
df.head()


# In[4]:


df.info()


# In[5]:


#datum 2018-02-29 omzetten naar NaT, 2018 geen schrikkeljaar. 
df['Started'] = pd.to_datetime(df['Started'], errors='coerce')
df['Ended'] = pd.to_datetime(df['Ended'], errors='coerce')


# In[6]:


#'Started' en 'Ended' naar datetime omzetten
df['Started'] = pd.to_datetime(df['Started'])
df['Ended'] = pd.to_datetime(df['Ended'])
df.head()


# In[7]:


#Extra kollom maken voor het uur van de dag
df['HourOfDay'] = df['Started'].dt.hour


# In[8]:


#Verwijder rijen met negatieve waarden
df = df[df['ChargeTime'] >= 0]


# In[9]:


df.head()


# In[10]:


df['Weekday'] = df['Started'].dt.day_name()


# In[11]:


df.head()


# In[12]:


df['Weekday'].describe()


# In[13]:


df['TotalEnergy (kwh)'] = df['TotalEnergy'] / 1000
df.head()


# In[14]:


#de snelheid wordt berekend door de totale energie te delen door de oplaadtijd.
df['ChargeSpeed'] =  df['TotalEnergy (kwh)'] / df['ChargeTime'] 


# In[15]:


#checkbox van maken in streamlit pyplot


#lineplot om de laadsnelheid te vergelijken per uur in een dag voor elk dag in de week. 
sns.relplot(kind= 'line', data= df, x= 'HourOfDay', y= 'ChargeSpeed', hue= 'Weekday', col='Weekday', ci = None)
plt.show()


# In[16]:


# niet opgeladen tijd kijken
df['NotChargeTime'] = df['ConnectedTime'] - df['ChargeTime']


# In[17]:


df.head()


# In[18]:


#streamlit checkbox/dropdown maken?

#regressielijn om de aantal niet-opgeladentijd per uur te vergelijken met de uur van de dag. 
sns.relplot(kind= 'line', data= df, x= 'HourOfDay', y= 'NotChargeTime', hue= 'Weekday', col= 'Weekday', ci = None)
plt.show()


# In[20]:


sns.boxplot(data=df, x='ChargeTime')
plt.show()


# In[37]:


sns.relplot( data=df,kind= 'scatter', x='MaxPower',y='TotalEnergy', hue ='HourOfDay', col= 'Weekday')

plt.show()


# In[ ]:




