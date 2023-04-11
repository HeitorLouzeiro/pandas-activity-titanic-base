import statistics

import pandas as pd

space = '-' * 50

url = 'https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv'  # noqa
titanic = pd.read_csv(url)

# print(titanic)

print('Identify and classify as variables:')
print('Qualitative Variables: Survived, Pclass, Gender, Name')
print('Quantitative Variables: Age, Siblings/Spouses on Board, Parents/Children on Board, Fare')  # noqa
print(space)

'''
Calculate the following measures of passenger age:
a) the average
b) median
c) fashion
d) standard deviation
e) total range
f) coefficient of variation
'''
# a) the average
average = statistics.mean(titanic['Age'])
print('Average: ', average)

# b) median
median = statistics.median(titanic['Age'])
print('Median: ', median)

# c) fashion
fashion = statistics.mode(titanic['Age'])
print('Fashion: ', fashion)

# d) standard deviation
standardDeviation = statistics.pstdev(titanic['Age'])
print('Standard Deviation: ', standardDeviation)

# e) total range
totalRange = max(titanic['Age']) - min(titanic['Age'])
print('total Range: ', totalRange)

# coefficient_variation
coefficientvariation = statistics.pstdev(titanic['Age']) / statistics.mean(titanic['Age'])  # noqa
print('Coefficient of variation: ', coefficientvariation)

# Or that other way

# coefficientvariation = standardDeviation / average
# print('Coefficient of variation: ', coefficientvariation)

print(space)

'''
Separate the data by Pclass and check:
a) Which class had the highest survival rate?
b) Which class had the highest average age?
'''

titanicPclass = titanic['Pclass'].unique()
print('Pclass: ', titanicPclass)

titanicPclass1 = titanic[titanic['Pclass'] == 1]
titanicPclass2 = titanic[titanic['Pclass'] == 2]
titanicPclass3 = titanic[titanic['Pclass'] == 3]

print('Pclass 1: ', titanicPclass1.head(10))
print('Pclass 2: ', titanicPclass2.head(10))
print('Pclass 3: ', titanicPclass3.head(10))

print(space)
print('Which Pclass had the highest median survival?')

averageT1 = statistics.mean(titanicPclass1['Survived'])
averageT2 = statistics.mean(titanicPclass2['Survived'])
averageT3 = statistics.mean(titanicPclass3['Survived'])

print('Average Pclass 1: ', averageT1)
print('Average Pclass 2: ', averageT2)
print('Average Pclass 3: ', averageT3)

print(space)

print('Which Pclass had the highest average age?')
averageAgeT1 = statistics.mean(titanicPclass1['Age'])
averageAgeT2 = statistics.mean(titanicPclass2['Age'])
averageAgeT3 = statistics.mean(titanicPclass3['Age'])

print('Middle Age Pclass 1: ', averageAgeT1)
print('Middle Age Pclass 2: ', averageAgeT2)
print('Middle Age Pclass 3: ', averageAgeT3)

print(space)

# c) rank each Idade in order of homogeneity
print('\nc) rank each Age in order of homogeneity?')

titanicPclass1Homogeneity = statistics.pstdev(titanicPclass1['Age']) / statistics.mean(titanicPclass1['Age'])  # noqa
titanicPclass2Homogeneity = statistics.pstdev(titanicPclass2['Age']) / statistics.mean(titanicPclass2['Age'])  # noqa
titanicPclass3Homogeneity = statistics.pstdev(titanicPclass3['Age']) / statistics.mean(titanicPclass3['Age'])  # noqa

print('Homogeneity Pclass 1: ', titanicPclass1Homogeneity)
print('Homogeneity Pclass 2: ', titanicPclass2Homogeneity)
print('Homogeneity Pclass 3: ', titanicPclass3Homogeneity)

print(space)
