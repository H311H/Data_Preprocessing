import pandas as pd
import numpy as np
import csv
from collections import Counter
from sklearn.preprocessing import KBinsDiscretizer



filename='percepolis_stdnt_enrl_class_grd_20190724.csv'
#header_list = ["student – anonymized", "um_acad_plan1 – major", "college – CEC only", "admit_type", ]

#Load the percepolis data in a data frame
df = pd.read_csv(filename, header=None, sep='\n')
df = df[0].str.split(',', expand=True)
print(df)

##
## 1. Date
##
##



# Set MM/DD/YYYY as date format.  
# df['date'] = pd.to_datetime(df.date)
# df['date'] = df['date'].dt.strftime('%m/%d/%Y')
# Set 1994 as the year for all dates  
# df = df.replace({'date':r'/\d\d\d\d$'}, {'date': '/1994'}, regex=True)



##
## 2. Code to replace missing data with most frequent value
##
##


# I will replace '?' with the most frequent value in the attribute
# Code to find the most frequent value of an atribute "column"  
with open(filename, 'r') as f:
    # Print and store the most frequent value of attribute "column"    
    column = (row[2] for row in csv.reader(f))
    subjectMostFreq = Counter(column).most_common()[0][0]
    print(type(subjectMostFreq))
    print("Most frequent value for SUBJECT: ", subjectMostFreq)

# Replace the '?' in each attribute with its most frequent value
#df = df.replace({'?':{' ?': valueMean}})


##
## 4. GRADING_BASIS_ENRL
##
##

# Normalize the values
# max_value = df['GRADING_BASIS_ENRL'].max()
# min_value = df['GRADING_BASIS_ENRL'].min()
# df['GRADING_BASIS_ENRL'] = (df['GRADING_BASIS_ENRL'] - min_value) / (max_value - min_value)





##
## 6. Fix typos and decode the '4 attribute
##
##
# Correct typos in the STRM attribute with the use of regex
df = df.replace({4:r'4043'}, {4: '2012 Fall Semester'}, regex=True)
df = df.replace({4:r'4127'}, {4: '2013 Spring Semester'}, regex=True)
df = df.replace({4:r'4135'}, {4: '2013 Summer Semester'}, regex=True)
df = df.replace({4:r'4143'}, {4: '2013 Fall Semester'}, regex=True)
df = df.replace({4:r'4227'}, {4: '2014 Spring Semester'}, regex=True)
df = df.replace({4:r'4235'}, {4: '2014 Summer Semester'}, regex=True)
df = df.replace({4:r'4243'}, {4: '2014 Fall Semester'}, regex=True)
df = df.replace({4:r'4327'}, {4: '2015 Spring Semester'}, regex=True)
df = df.replace({4:r'4335'}, {4: '2015 Summer Semester'}, regex=True)
df = df.replace({4:r'4343'}, {4: '2015 Fall Semester'}, regex=True)
df = df.replace({4:r'4427'}, {4: '2016 Spring Semester'}, regex=True)
df = df.replace({4:r'4435'}, {4: '2016 Summer Semester'}, regex=True)
df = df.replace({4:r'4443'}, {4: '2016 Fall Semester'}, regex=True)
df = df.replace({4:r'4527'}, {4: '2017 Spring Semester'}, regex=True)
df = df.replace({4:r'4535'}, {4: '2017 Summer Semester'}, regex=True)
df = df.replace({4:r'4543'}, {4: '2017 Fall Semester'}, regex=True)
df = df.replace({4:r'4627'}, {4: '2018 Spring Semester'}, regex=True)
df = df.replace({4:r'4635'}, {4: '2018 Summer Semester'}, regex=True)


# Export changes to a new .CSV file
df.to_csv('PercepolisNEWFILE.csv')

