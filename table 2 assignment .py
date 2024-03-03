#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import os


# In[3]:


patents_df = pd.read_stata(r"C:\Users\majji\Downloads\EDA\Patents_1975-2010.dta")


# In[4]:


citations_df1 = pd.read_stata(r"C:\Users\majji\Downloads\EDA\Citations_1975-1999.dta")


# In[5]:


citations_df2 = pd.read_stata(r"C:\Users\majji\Downloads\EDA\Citations_2000-2010 part 1.dta")


# In[6]:


citations_df3 = pd.read_stata(r"C:\Users\majji\Downloads\EDA\Citations_2000-2010 part 2.dta")


# In[7]:


class_subclass_df = pd.read_stata(r"C:\Users\majji\Downloads\EDA\Class-Subclass_1975-2010.dta")


# In[8]:


inventors_part1 = pd.read_stata(r"C:\Users\majji\Downloads\EDA\Inventors_1975-2010 part 1.dta")
inventors_part2 = pd.read_stata(r"C:\Users\majji\Downloads\EDA\Inventors_1975-2010 part 2.dta")


# In[9]:


citations_df = pd.concat([citations_df1, citations_df2, citations_df3], ignore_index=True)


# In[10]:


citations_count = citations_df.groupby('patent')['citation'].count().reset_index()


# In[11]:


patents_citations_merged = pd.merge(patents_df, citations_count, left_on='patent', right_on='patent')


# In[12]:


final_merged_df = pd.merge(patents_citations_merged, class_subclass_df, on='patent')


# In[13]:


print(final_merged_df.head())


# In[14]:


# Check for missing values
print(final_merged_df.isnull().sum())

# Remove missing values
final_merged_df.dropna(inplace=True)

# Remove duplicates
final_merged_df.drop_duplicates(inplace=True)

# Remove outliers
# (Perform outlier detection and removal if necessary)


# In[15]:


# Calculate citation counts
citation_counts = final_merged_df.groupby(['patent', 'gyear']).size().reset_index(name='citation_count')

# Calculate unique classes
unique_classes = final_merged_df.groupby(['patent', 'gyear'])['class'].nunique().reset_index(name='unique_classes')

# Calculate unique subclasses
unique_subclasses = final_merged_df.groupby(['patent', 'gyear'])['subclass'].nunique().reset_index(name='unique_subclasses')


# In[16]:


table1_data = pd.merge(patents_df[['patent', 'gyear']], citation_counts, left_on=['patent', 'gyear'], right_on=['patent', 'gyear'])
table1_data = pd.merge(table1_data, unique_classes, on=['patent', 'gyear'])
table1_data = pd.merge(table1_data, unique_subclasses, on=['patent', 'gyear'])


# In[17]:


import pandas as pd
import numpy as np


# In[18]:


#Step 1: Calculate subclass counts for each patent
subclass_counts = final_merged_df.groupby(['patent', 'subclass']).size().reset_index(name='subclass_count')


# In[19]:


# Step 2: Calculate class citations for each subclass
class_citations = final_merged_df.groupby(['patent', 'subclass', 'class']).size().reset_index(name='class_citations')


# In[20]:


# Step 3: Calculate originality scores for each patent
originality_scores = {}

# Create a dictionary to store subclass_sum and class_sum for each patent
patent_stats = {}


# In[ ]:


# Calculate subclass_sum for each patent
for patent, group in final_merged_df.groupby('patent'):
    subclass_sum = subclass_counts[subclass_counts['patent'] == patent]['subclass_count'].sum()
    patent_stats[patent] = {'subclass_sum': subclass_sum}

# Calculate class_sum for each patent
for patent, group in final_merged_df.groupby('patent'):
    class_sum = class_citations[class_citations['patent'] == patent]['class_citations'].sum()
    patent_stats[patent]['class_sum'] = class_sum

# Calculate originality scores
for patent, stats in patent_stats.items():
    subclass_sum = stats['subclass_sum']
    class_sum = stats['class_sum']
    citations = final_merged_df[final_merged_df['patent'] == patent]['citation'].sum()
    
    if class_sum != 0:
        originality_scores[patent] = subclass_sum / class_sum
    else:
        originality_scores[patent] = 0


# In[ ]:


# Convert originality scores to DataFrame
originality_df = pd.DataFrame(originality_scores.items(), columns=['Patent', 'Originality'])


# In[ ]:


# Step 4: Calculate familiarity scores for each patent
familiarity_scores = {}


# In[ ]:


# Group by patent and calculate subclass counts
subclass_counts_patent = subclass_counts.groupby('patent')

for patent, group in final_merged_df.groupby('patent'):
    subclass_counts_patent_patent = subclass_counts_patent.get_group(patent)
    
    # Calculate individual component familiarity for each subclass
    subclass_counts_patent_patent['individual_familiarity'] = subclass_counts_patent_patent.apply(
        lambda row: row['subclass_count'] / (final_merged_df['appdate'].max() - row['appdate']).days, axis=1)
    
    # Calculate average component familiarity for all subclasses
    avg_familiarity = subclass_counts_patent_patent['individual_familiarity'].mean()
    
    familiarity_scores[patent] = avg_familiarity


# In[ ]:


# Convert familiarity scores to DataFrame
familiarity_df = pd.DataFrame(familiarity_scores.items(), columns=['Patent', 'Familiarity'])


# In[ ]:


# Combine originality and familiarity DataFrames
table2_data = pd.merge(originality_df, familiarity_df, on='Patent')


# In[ ]:


# Merge with patents_df to add year information
table2_data = pd.merge(table2_data, patents_df[['patent_number', 'gyear']], left_on='Patent', right_on='patent_number')


# In[ ]:


# Rename columns and select required columns
table2_data = table2_data.rename(columns={'gyear': 'Year'}).drop(columns=['patent_number'])


# In[ ]:


# Display Table 2
print(table2_data)

