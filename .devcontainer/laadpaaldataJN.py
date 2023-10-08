import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('laadpaaldata.csv')
df.head()

df.info()

#datum 2018-02-29 omzetten naar NaT, 2018 geen schrikkeljaar. 
df['Started'] = pd.to_datetime(df['Started'], errors='coerce')
df['Ended'] = pd.to_datetime(df['Ended'], errors='coerce')

#'Started' en 'Ended' naar datetime omzetten
df['Started'] = pd.to_datetime(df['Started'])
df['Ended'] = pd.to_datetime(df['Ended'])
df.head()

#Extra kollom maken voor het uur van de dag
df['HourOfDay'] = df['Started'].dt.hour

#Verwijder rijen met negatieve waarden
df = df[df['ChargeTime'] >= 0]

df.head()


df['Weekday'] = df['Started'].dt.day_name()

df.head()


df['Weekday'].describe()


df['TotalEnergy (kwh)'] = df['TotalEnergy'] / 1000
df.head()

#de snelheid wordt berekend door de totale energie te delen door de oplaadtijd.
df['ChargeSpeed'] =  df['TotalEnergy (kwh)'] / df['ChargeTime'] 


#checkbox van maken in streamlit pyplot

#lineplot om de laadsnelheid te vergelijken per uur in een dag voor elk dag in de week. 
sns.relplot(kind= 'line', data= df, x= 'HourOfDay', y= 'ChargeSpeed', hue= 'Weekday', col='Weekday', ci = None) 
plt.show()

# niet opgeladen tijd kijken
df['NotChargeTime'] = df['ConnectedTime'] - df['ChargeTime']
df.head()

#streamlit checkbox/dropdown maken?

#regressielijn om de aantal niet-opgeladentijd per uur te vergelijken met de uur van de dag. 
sns.relplot(kind= 'line', data= df, x= 'HourOfDay', y= 'NotChargeTime', hue= 'Weekday', col= 'Weekday', ci = None)
plt.show()

sns.boxplot(data=df, x='ChargeTime')
plt.show()

sns.relplot( data=df,kind= 'scatter', x='MaxPower',y='TotalEnergy', hue ='HourOfDay', col= 'Weekday')

plt.show()





