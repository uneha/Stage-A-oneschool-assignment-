#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd


# In[1]:


#question 1


# In[2]:


lst = [[35,'Portugal',94],[33,'Argentina',93],[30,'Brazil',92]]


# In[3]:


col = ['Age','Nationality','Overall']


# In[9]:


pd.DataFrame(lst,columns=col,index=[i for i in range(1,4)])


# In[10]:


pd.DataFrame(lst,columns=col,index=[1,2,3])


# In[64]:


#Answers to the question based on the African food production dataset


# In[11]:


food_data=pd.read_csv(r'C:\Users\USER\Downloads\FoodBalanceSheets_E_Africa_NOFLAG.csv')


# In[12]:


subset_1 = food_data.groupby('Item')


# In[13]:


subset_1['Y2014'].sum()


# In[15]:


#Hence animal fat produced in 2014 = 209460.54


# In[17]:


subset_1['Y2017'].sum()


# In[18]:


#Hence animal fat produced in 2017 = 269617.53


# In[20]:


food_data.describe(include = 'all')


# In[21]:


#Hence mean (for 2015) = 135.236 and standard deviation(for 2015) = 1603.404


# In[22]:


food_data.isnull().sum()


# In[23]:


#Hence total number of missing value in 2016 is 1535 


# In[26]:


round(1535/len(food_data)*100,2) #percentage of missing data


# In[29]:


print(food_data['Element Code'].corr(food_data['Y2014']))


# In[35]:


print(food_data['Element Code'].corr(food_data['Y2015']))


# In[34]:


print(food_data['Element Code'].corr(food_data['Y2016']))


# In[33]:


print(food_data['Element Code'].corr(food_data['Y2017']))


# In[36]:


#Hence 2014 has highest correlation with Element Code


# In[37]:


subset_element = food_data.groupby('Element')


# In[38]:


subset_element.sum()


# In[39]:


#Hence 2017 has the highest import quantity sum


# In[40]:


#Sum of production in 2014 = 1931287.75


# In[41]:


subset_element['Y2018'].sum()


# In[44]:


# Domestic supply quantity had ighest sum in 2018


# In[45]:


# Protien supply quantity had the 3rd lowest sum in 2018


# In[58]:


subset_algeria = food_data[food_data['Area'] == 'Algeria'].groupby('Element')


# In[60]:


subset_algeria['Y2018'].sum()


# In[61]:


#Total Import Quantity in Algeria in 2018 = 36238.29


# In[62]:


food_data['Area'].nunique()


# In[63]:


#Total number of unique countries in the dataset = 49


# In[ ]:




