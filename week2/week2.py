# coding: utf-8

# # 1. The Series Data Structure

# In[34]:


import pandas as pd
get_ipython().run_line_magic('pinfo', 'pd.Series')


# In[36]:


animals = ['Tiger', 'Bear', 'Moose']
pd.Series(animals)


# In[8]:


numbers = [1, 2, 3]
pd.Series(numbers)


# In[9]:


animals = ['Tiger', 'Bear', None]
pd.Series(animals)


# In[10]:


numbers = [1, 2, None]
pd.Series(numbers)


# None and nan are different

# In[11]:


import numpy as np
np.nan == None


# In[12]:


np.nan == np.nan


# In[13]:


np.isnan(np.nan)


# In[14]:


sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}
s = pd.Series(sports)
s


# In[15]:


s.index #to know the index value 


# In[16]:


s = pd.Series(['Tiger', 'Bear', 'Moose'], index=['India', 'America', 'Canada'])
s


# In[17]:


sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}
s = pd.Series(sports, index=['Golf', 'Sumo', 'Hockey'])
s


# # 2. Querying a Series

# In[18]:


sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}
s = pd.Series(sports)
s


# In[19]:


s.iloc[3]


# In[20]:


s.loc['Golf']


# In[21]:


s[3]


# In[22]:


s['Golf']


# In[23]:


sports = {99: 'Bhutan',
          100: 'Scotland',
          101: 'Japan',
          102: 'South Korea'}
s = pd.Series(sports)


# In[24]:


s


# In[25]:


s[0] #This won't call s.iloc[0] as one might expect, it generates an error instead


# In[ ]:


s.iloc[0]


# In[ ]:


s = pd.Series([100.00, 120.00, 101.00, 3.00])
s


# In[ ]:


total = 0
for item in s:
    print(item)


# In[ ]:


total = 0
for item in s:
    total+=item
print(total)


# In[ ]:


import numpy as np

total = np.sum(s)
print(total)


# In[ ]:


#this creates a big series of random numbers
s = pd.Series(np.random.randint(0,1000,10000))
s.head()


# In[ ]:


len(s)


# In[41]:


#this creates a big series of random numbers
s = pd.Series(np.random.randint(0,1000,1))
s.head()


# In[42]:


get_ipython().run_cell_magic('timeit', '-n 100', 'summary = 0\nfor item in s:\n    summary+=item')


# In[43]:


get_ipython().run_cell_magic('timeit', '-n 100', 'summary = np.sum(s)')


# In[44]:


s+=2 #adds two to each item in s using broadcasting
s.head()


# In[45]:


for label, value in s.iteritems():
    s.set_value(label, value+2)
s.head()


# In[46]:


get_ipython().run_cell_magic('timeit', '-n 10', 's = pd.Series(np.random.randint(0,1000,10000))\nfor label, value in s.iteritems():\n    s.loc[label]= value+2')


# In[47]:


s.head()


# In[48]:


s.head


# In[49]:


import pandas as pd
%%timeit -n 10
s = pd.Series(np.random.randint(0,1000,10000))
s+=2


# In[52]:


s = pd.Series([1, 2, 3])
s.loc['Animal'] = 'Bears'
s


# In[53]:


original_sports = pd.Series({'Archery': 'Bhutan',
                             'Golf': 'Scotland',
                             'Sumo': 'Japan',
                             'Taekwondo': 'South Korea'})
cricket_loving_countries = pd.Series(['Australia',
                                      'Barbados',
                                      'Pakistan',
                                      'England'], 
                                   index=['Cricket',
                                          'Cricket',
                                          'Cricket',
                                          'Cricket'])
all_countries = original_sports.append(cricket_loving_countries)


# In[54]:


original_sports


# In[55]:


cricket_loving_countries


# In[56]:


all_countries


# In[57]:


all_countries.loc['Cricket']


# # 3. The DataFrame Data Structure

# In[59]:


pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})


# In[60]:


import pandas as pd
purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})
df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])
df.head()


# In[61]:


df.loc['Store 2']


# In[62]:


type(df.loc['Store 2'])


# In[63]:


df.loc['Store 1']


# In[64]:


df.loc['Store 1', 'Cost']


# In[65]:


df.loc['Store 1']['Cost']


# In[66]:


df.T


# In[67]:


df.T.loc['Cost']


# In[68]:


df['Cost']


# In[69]:


df.loc['Store 1']['Cost']


# In[70]:


df.loc[:,['Name', 'Cost']]


# In[71]:


df.drop('Store 1')


# In[72]:


df


# In[73]:


copy_df = df.copy()
copy_df = copy_df.drop('Store 1')
copy_df


# In[74]:


get_ipython().run_line_magic('pinfo', 'copy_df.drop')


# In[75]:


del copy_df['Name']
copy_df


# In[76]:


df['Location'] = None
df


# # 4. Dataframe Indexing and Loading

# In[77]:


costs = df['Cost']
costs


# In[78]:


costs+=2
costs


# In[79]:


df


# In[80]:


get_ipython().system('cat olympics.csv')


# In[82]:


df = pd.read_csv('olympics.csv')
df.head()


# In[83]:


df = pd.read_csv('olympics.csv', index_col = 0, skiprows=1)
df.head()


# In[84]:


df.columns


# In[85]:


for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold' + col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver' + col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze' + col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#' + col[1:]}, inplace=True) 

df.head()


# # 5. Querying a DataFrame

# In[86]:


df['Gold'] > 0


# In[87]:


only_gold = df.where(df['Gold'] > 0)
only_gold.head()


# In[88]:


only_gold['Gold'].count()


# In[89]:


df['Gold'].count()


# In[90]:


only_gold = only_gold.dropna()
only_gold.head()


# In[91]:


only_gold = df[df['Gold'] > 0]
only_gold.head()


# In[92]:


len(df[(df['Gold'] > 0) | (df['Gold.1'] > 0)])


# In[93]:


df[(df['Gold.1'] > 0) & (df['Gold'] == 0)]


# # 6. Indexing Dataframe

# In[94]:


df.head()


# In[95]:


df['country'] = df.index
df = df.set_index('Gold')
df.head()


# In[96]:


df = df.reset_index()
df.head()


# In[100]:


df = pd.read_csv('census.csv')
df.head()


# In[101]:


df['SUMLEV'].unique()


# In[102]:


df=df[df['SUMLEV'] == 50]
df.head()


# In[103]:


columns_to_keep = ['STNAME',
                   'CTYNAME',
                   'BIRTHS2010',
                   'BIRTHS2011',
                   'BIRTHS2012',
                   'BIRTHS2013',
                   'BIRTHS2014',
                   'BIRTHS2015',
                   'POPESTIMATE2010',
                   'POPESTIMATE2011',
                   'POPESTIMATE2012',
                   'POPESTIMATE2013',
                   'POPESTIMATE2014',
                   'POPESTIMATE2015']
df = df[columns_to_keep]
df.head()


# In[104]:


df = df.set_index(['STNAME', 'CTYNAME'])
df.head()


# In[105]:


df.loc['Michigan', 'Washtenaw County']


# In[106]:


df.loc[ [('Michigan', 'Washtenaw County'),
         ('Michigan', 'Wayne County')] ]


# # 7. Missing values

# In[109]:


df = pd.read_csv('log.csv')
df


# In[110]:


get_ipython().run_line_magic('pinfo', 'df.fillna')


# In[111]:


df = df.set_index('time')
df = df.sort_index()
df


# In[112]:


df = df.reset_index()
df = df.set_index(['time', 'user'])
df


# In[113]:


df = df.fillna(method='ffill')
df.head()


# In[ ]:




