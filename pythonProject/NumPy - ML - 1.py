import pandas as pd
import numpy as np

students_performance = pd.read_csv('C:\pythonProject2\StudentsPerformance.csv')
print(students_performance)
#print(students_performance.head(8))
#print(students_performance.describe())
#print(students_performance.dtypes)
#print(students_performance.groupby('gender').aggregate({'math score': 'mean'}))
#print(students_performance.shape)

#print(students_performance.iloc[0:3, 0:3])
#print(students_performance.iloc[0:6])
#print(students_performance.iloc[[0, 3, 10], 0:4])
#print(students_performance.iloc[[0, 3, 10], [-3, -2, -1]])
#
#print(students_performance.loc[0:3])

#students_performance_with_names = students_performance.iloc[[0, 3, 4, 7, 8]]
#print(students_performance_with_names)
#students_performance_with_names.index = ["Row 1", "Row 2", "Row 3", "Row 4", "Row 5"]
#print(students_performance_with_names)
#
# print(students_performance_with_names.iloc[0:3])
# print(students_performance_with_names.loc[['Row 1', 'Row 5'], ['gender', 'math score']])
# print(students_performance_with_names.loc['Row 1':'Row 3'])
#print(students_performance_with_names.iloc[:, 0])
# print(students_performance_with_names.iloc[0:5, 0])
# print(type(students_performance_with_names.iloc[:, 1:2]))
# print(type(students_performance.iloc[0:3, 0:3]))
# print(type(students_performance.iloc[:, 0:3]))

my_series_1 = pd.Series([1, 2, 4], index=[0, 1, "Row 3"])
print(my_series_1)
print(students_performance[['gender']])
print(students_performance['gender'])
print(type(students_performance[['gender']]))
print(type(students_performance['gender']))
