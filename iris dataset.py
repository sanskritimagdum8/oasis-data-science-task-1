

import pandas as pd
import csv

df=pd.read_csv(r'C:\Users\admin\Downloads\IRIS.csv')
df.head()


# In[2]:


setosa = df[df['species'] == 'Iris-setosa']
versicolor = df[df['species'] == 'Iris-versicolor']
virginica = df[df['species'] == 'Iris-virginica']


# In[5]:


print('Iris-setosa')
setosa.describe()


# In[6]:


print('\nIris-versicolor')
versicolor.describe()


# In[7]:


print('\nIris-virginica')
virginica.describe()






