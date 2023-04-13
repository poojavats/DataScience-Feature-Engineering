#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import nbconvert


# In[2]:


df=sns.load_dataset('titanic')


# In[3]:


df.head()


# In[4]:


#Check missing value in dataset
df.isnull()


# In[5]:


df.isnull().sum()


# In[6]:


# getting error here beacuse of (ValueError: could not convert string to float: 'male')
#sns.heatmap(df)


# In[7]:


sns.heatmap(df.isnull())


# In[8]:


#Handling missing values by deleting rows
df.dropna()


# In[9]:


##rowwise deletion
df.dropna().shape


# In[10]:


df.shape


# # Note-> Above practice is not good by deleting the rows, beacuse here we are missing lot of data

# In[11]:


## Handling missing values by deleting Column Wise
df.dropna(axis=1)


# In[12]:


## Imputation Technique
### 1-Mean value Imputation


# In[13]:


sns.distplot(df['age'])


# In[14]:


df.age.isnull().sum()


# In[15]:


df['Age_mean']=df['age'].fillna(df['age'].mean())


# In[16]:


df[['Age_mean','age']]


# In[17]:


## Above techniques works when our data is normally distrubted.


# # Meadian Value Imputation-When data is skewed or- when we have outliers we used this technique

# In[18]:


df['Age_median']=df['age'].fillna(df['age'].median())


# In[19]:


df[['Age_mean','age','Age_median']]


# # 3- Mode Value Imputation- Used for Categarial data

# In[20]:


df[df['embarked'].isnull()]


# In[21]:


df['embarked'].unique()


# In[22]:


df['age'].notna()


# In[23]:


df[df['age'].notna()]


# In[24]:


df[df['age'].notna()]['embarked'].mode()


# In[25]:


df[df['age'].notna()]['embarked'].mode()[0]


# In[26]:


mode= df[df['age'].notna()]['embarked'].mode()[0]


# In[27]:


mode


# In[28]:


df['embarked_mode']=df['embarked'].fillna(mode)


# In[29]:


df[['embarked_mode','embarked']]


# In[30]:


df['embarked_mode'].isnull().sum()


# In[ ]:




