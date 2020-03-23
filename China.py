#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import sys
import os
import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
from matplotlib import colors as mcolors

dir = r'C:\Users\chandra\Desktop\DataSets\Commodities'
os.chdir(dir)

full_dataset = pd.read_csv('commodity_trade_statistics_data.csv', dtype={"user_id": int, "username": object})

export_data = full_dataset.loc[full_dataset['flow'] == 'Export']

import_data = full_dataset.loc[full_dataset['flow'] == 'Import']

country_import_data = import_data.loc[import_data['country_or_area'] == 'China']

country_export_data = export_data.loc[export_data['country_or_area'] == 'China']


# In[2]:


country_export_data.head(5)


# In[3]:


country_exp_columns = list(country_export_data.columns)
country_exp_columns


# In[5]:


for column in country_exp_columns:
    print(column, ":", country_export_data[column].dtypes)


# In[6]:


commodities_exp = list(country_export_data.category.unique())
commodities_exp


# In[7]:


country_export_data = country_export_data[country_export_data.category != 'all_commodities']
commodities_exp = list(country_export_data.category.unique())
commodities_exp


# In[9]:


years = list(country_export_data.year.unique())
years.sort()
years


# In[67]:


top5_years = list()
total_years = list()


# In[68]:


y1992 = country_export_data.loc[(country_export_data.year == 1992)]

y1992_total = y1992.groupby(['category','year']).trade_usd.agg([sum])
y1992_total = y1992_total.sort_values(by='sum', ascending = False)
y1992_final = y1992_total.head(5)
top5_years.append(y1992_final)
total_years.append(y1992_total)


# In[69]:


y1993 = country_export_data.loc[(country_export_data.year == 1993)]

y1993_total = y1993.groupby(['category','year']).trade_usd.agg([sum])
y1993_total = y1993_total.sort_values(by='sum', ascending = False)
y1993_final = y1993_total.head(5)
top5_years.append(y1993_final)
total_years.append(y1993_total)


# In[70]:


y1994 = country_export_data.loc[(country_export_data.year == 1994)]

y1994_total = y1994.groupby(['category','year']).trade_usd.agg([sum])
y1994_total = y1994_total.sort_values(by='sum', ascending = False)
y1994_final = y1994_total.head(5)
top5_years.append(y1994_final)
total_years.append(y1994_total)


# In[71]:


y1995 = country_export_data.loc[(country_export_data.year == 1995)]

y1995_total = y1995.groupby(['category','year']).trade_usd.agg([sum])
y1995_total = y1995_total.sort_values(by='sum', ascending = False)
y1995_final = y1995_total.head(5)
top5_years.append(y1995_final)
total_years.append(y1995_total)


# In[72]:


y1996 = country_export_data.loc[(country_export_data.year == 1996)]

y1996_total = y1996.groupby(['category','year']).trade_usd.agg([sum])
y1996_total = y1996_total.sort_values(by='sum', ascending = False)
y1996_final = y1996_total.head(5)
top5_years.append(y1996_final)
total_years.append(y1996_total)


# In[73]:


y1997 = country_export_data.loc[(country_export_data.year == 1997)]

y1997_total = y1997.groupby(['category','year']).trade_usd.agg([sum])
y1997_total = y1997_total.sort_values(by='sum', ascending = False)
y1997_final = y1997_total.head(5)
top5_years.append(y1997_final)
total_years.append(y1997_total)


# In[74]:


y1998 = country_export_data.loc[(country_export_data.year == 1998)]

y1998_total = y1998.groupby(['category','year']).trade_usd.agg([sum])
y1998_total = y1998_total.sort_values(by='sum', ascending = False)
y1998_final = y1998_total.head(5)
top5_years.append(y1998_final)
total_years.append(y1998_total)


# In[75]:


y1999 = country_export_data.loc[(country_export_data.year == 1999)]

y1999_total = y1999.groupby(['category','year']).trade_usd.agg([sum])
y1999_total = y1999_total.sort_values(by='sum', ascending = False)
y1999_final = y1999_total.head(5)
top5_years.append(y1999_final)
total_years.append(y1999_total)


# In[76]:


y2000 = country_export_data.loc[(country_export_data.year == 2000)]

y2000_total = y2000.groupby(['category','year']).trade_usd.agg([sum])
y2000_total = y2000_total.sort_values(by='sum', ascending = False)
y2000_final = y2000_total.head(5)
top5_years.append(y2000_final)
total_years.append(y2000_total)


# In[77]:


y2001 = country_export_data.loc[(country_export_data.year == 2001)]

y2001_total = y2001.groupby(['category','year']).trade_usd.agg([sum])
y2001_total = y2001_total.sort_values(by='sum', ascending = False)
y2001_final = y2001_total.head(5)
top5_years.append(y2001_final)
total_years.append(y2001_total)


# In[78]:


y2002 = country_export_data.loc[(country_export_data.year == 2002)]

y2002_total = y2002.groupby(['category','year']).trade_usd.agg([sum])
y2002_total = y2002_total.sort_values(by='sum', ascending = False)
y2002_final = y2002_total.head(5)
top5_years.append(y2002_final)
total_years.append(y2002_total)


# In[79]:


y2003 = country_export_data.loc[(country_export_data.year == 2003)]

y2003_total = y2003.groupby(['category','year']).trade_usd.agg([sum])
y2003_total = y2003_total.sort_values(by='sum', ascending = False)
y2003_final = y2003_total.head(5)
top5_years.append(y2003_final)
total_years.append(y2003_total)


# In[80]:


y2004 = country_export_data.loc[(country_export_data.year == 2004)]

y2004_total = y2004.groupby(['category','year']).trade_usd.agg([sum])
y2004_total = y2004_total.sort_values(by='sum', ascending = False)
y2004_final = y2004_total.head(5)
top5_years.append(y2004_final)
total_years.append(y2004_total)


# In[81]:


y2005 = country_export_data.loc[(country_export_data.year == 2005)]

y2005_total = y2005.groupby(['category','year']).trade_usd.agg([sum])
y2005_total = y2005_total.sort_values(by='sum', ascending = False)
y2005_final = y2005_total.head(5)
top5_years.append(y2005_final)
total_years.append(y2005_total)


# In[82]:


y2006 = country_export_data.loc[(country_export_data.year == 2006)]

y2006_total = y2006.groupby(['category','year']).trade_usd.agg([sum])
y2006_total = y2006_total.sort_values(by='sum', ascending = False)
y2006_final = y2006_total.head(5)
top5_years.append(y2006_final)
total_years.append(y2006_total)


# In[83]:


y2007 = country_export_data.loc[(country_export_data.year == 2007)]

y2007_total = y2007.groupby(['category','year']).trade_usd.agg([sum])
y2007_total = y2007_total.sort_values(by='sum', ascending = False)
y2007_final = y2007_total.head(5)
top5_years.append(y2007_final)
total_years.append(y2007_total)


# In[84]:


y2008 = country_export_data.loc[(country_export_data.year == 2008)]

y2008_total = y2008.groupby(['category','year']).trade_usd.agg([sum])
y2008_total = y2008_total.sort_values(by='sum', ascending = False)
y2008_final = y2008_total.head(5)
top5_years.append(y2008_final)
total_years.append(y2008_total)


# In[85]:


y2009 = country_export_data.loc[(country_export_data.year == 2009)]

y2009_total = y2009.groupby(['category','year']).trade_usd.agg([sum])
y2009_total = y2009_total.sort_values(by='sum', ascending = False)
y2009_final = y2009_total.head(5)
top5_years.append(y2009_final)
total_years.append(y2009_total)


# In[86]:


y2010 = country_export_data.loc[(country_export_data.year == 2010)]

y2010_total = y2010.groupby(['category','year']).trade_usd.agg([sum])
y2010_total = y2010_total.sort_values(by='sum', ascending = False)
y2010_final = y2010_total.head(5)
top5_years.append(y2010_final)
total_years.append(y2010_total)


# In[87]:


y2011 = country_export_data.loc[(country_export_data.year == 2011)]

y2011_total = y2011.groupby(['category','year']).trade_usd.agg([sum])
y2011_total = y2011_total.sort_values(by='sum', ascending = False)
y2011_final = y2011_total.head(5)
top5_years.append(y2011_final)
total_years.append(y2011_total)


# In[88]:


y2012 = country_export_data.loc[(country_export_data.year == 2012)]

y2012_total = y2012.groupby(['category','year']).trade_usd.agg([sum])
y2012_total = y2012_total.sort_values(by='sum', ascending = False)
y2012_final = y2012_total.head(5)
top5_years.append(y2012_final)
total_years.append(y2012_total)


# In[89]:


y2013 = country_export_data.loc[(country_export_data.year == 2013)]

y2013_total = y2013.groupby(['category','year']).trade_usd.agg([sum])
y2013_total = y2013_total.sort_values(by='sum', ascending = False)
y2013_final = y2013_total.head(5)
top5_years.append(y2013_final)
total_years.append(y2013_total)


# In[90]:


y2014 = country_export_data.loc[(country_export_data.year == 2014)]

y2014_total = y2014.groupby(['category','year']).trade_usd.agg([sum])
y2014_total = y2014_total.sort_values(by='sum', ascending = False)
y2014_final = y2014_total.head(5)
top5_years.append(y2014_final)
total_years.append(y2014_total)


# In[91]:


y2015 = country_export_data.loc[(country_export_data.year == 2015)]

y2015_total = y2015.groupby(['category','year']).trade_usd.agg([sum])
y2015_total = y2015_total.sort_values(by='sum', ascending = False)
y2015_final = y2015_total.head(5)
top5_years.append(y2015_final)
total_years.append(y2015_total)


# In[92]:


y2016 = country_export_data.loc[(country_export_data.year == 2016)]

y2016_total = y2016.groupby(['category','year']).trade_usd.agg([sum])
y2016_total = y2016_total.sort_values(by='sum', ascending = False)
y2016_final = y2016_total.head(5)
top5_years.append(y2016_final)
total_years.append(y2016_total)


# In[93]:


final_categories = []
for i in range(len(top5_years)):
    temp = top5_years[i].reset_index()
    temp_categories = temp.category.unique()
    for category in temp_categories:
        if category not in final_categories:
            final_categories.append(category)

final_categories


# In[94]:


final_tables = []
for i in range(len(total_years)):
    temp = total_years[i].reset_index()
    temp_table = temp.loc[temp['category'].isin(final_categories)]
    final_tables.append(temp_table)

final_tables


# In[95]:


for i in range(len(final_tables)):
    if len(final_tables[i].category) > 0:
        lenght = len(final_tables[i].category)
        temp_ranker = [l for l in range(len(final_categories))]
        temp_ranker = temp_ranker[::-1]
        ranker = temp_ranker[:lenght]
        final_tables[i]['Rank'] = ranker
        
final_tables


# In[96]:


for i in range(len(final_tables)):
    final_tables[i] = final_tables[i].sort_values(by='category', ascending = False)

final_tables


# In[97]:


final_array = []

for i in range(len(final_tables)):
    final_array.append(final_tables[i].Rank)

final_array


# In[98]:


for i in range(len(final_array)):
    final_array[i] = final_array[i] -(len(final_categories)-6)
    final_array[i][final_array[i]<1] = 0

final_array


# In[99]:


new_categories = sorted(final_categories, reverse = True)
new_categories


# In[100]:


plotting_table = pd.DataFrame(np.array(final_array), columns = new_categories)
plotting_table['Year'] = years
plotting_table = plotting_table.set_index('Year')
plotting_table


# In[101]:


plotting_table.columns = new_categories
plotting_table.head()


# In[103]:


plt.figure(figsize = (20,20))

plt.title("China Major Export Category Ranking Change")

plt.ylabel('Ranking')

sns.lineplot(data = plotting_table, dashes = False)

