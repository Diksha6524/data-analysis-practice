import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


#in this we will be learing about eda and feature engg on black friday dataset
#cleaining and preparing the data for model training

#import dataset
df_train=pd.read_csv('blackfriday_train.csv')
print(df_train.head())
print(df_train.columns)


#problem statemnt->Problem Statement
# A retail company “ABC Private Limited” wants to understand the customer purchase behaviour (specifically, purchase amount) against various products of different categories. They have shared purchase summary of various customers for selected high volume products from last month. The data set also contains customer demographics (age, gender, marital status, city_type, stay_in_current_city), product details (product_id and product category) and Total purchase_amount from last month.
# Now, they want to build a model to predict the purchase amount of customer against various products which will help them to create personalized offer for customers against different products.




# we need to combine train and test dataset,so that we so preprocessing on both

#import test data
df_test=pd.read_csv('blackfriday_test.csv')
print(df_test.head())
print(df_test.columns)  #intest data we wot be able to see output variable ie ->Purchase


#merge both dataset
df=pd.concat([df_train,df_test])
print(df.head(15))
print(df.info())
#age in it is categorical vairable cuz its in range
print(df.describe())

#we can drop column user_id
df.drop(['User_ID'],axis=1,inplace=True) #axis =0 rowwise,axis=1 columnwise
print(df.columns)

#number of categorical variables are Gender,Age,Occupation,city_category
#we fix categorical variables
# Fixing categorical variables helps in:
# Correct value counts
# Clean bar charts
# Meaningful groupby analysis
# Reliable model input later


# Numerical variables → we check range, min, max, outliers
# Categorical variables → we check consistency, spelling, categories count




#gender->
#lets check m and f
#using dummies->numerical representation of categorical variables
print(pd.get_dummies(df['Gender'],dtype=int))  #it shows in true and false  without dtype=int it shows in bool
#now we will convet f /m into 0/1 s
#we use map method it will take conditions given and map it to the data accordingly
df['Gender']=df['Gender'].map({'F':0,'M':1})
print(df['Gender'].head())  
#this can be also done as
#df['Gender ']=df['Gender '].replace({'F':0,'M':1}) or df['Gender']=pd.get_dummies(df['Gender'],dtype=int,drop_first=1)
#why drop_first used-> to avoid dummy variable trap
#Drop one dummy category per feature to avoid multicollinearity
#example->if we have 3 categories A,B,C then if we create dummies for all 3 then if we know values of A and B we can easily find C
#so we drop one category to avoid this trap
#Pandas drops the first category in sorted order
# For ['Female', 'Male'] → Female is dropped
#drop_first=True removes one dummy variable per categorical feature to prevent multicollinearity.


#  age -> categorical variable to numerical
print(df['Age'].unique())  #it will give unique valuse in age column
df['Age']=df['Age'].map({'0-17':1,'18-25':2,'26-35':3,'36-45':4,'46-50':5,'51-55':6,'55+':7})
#here we gave rank,for target guiding encoding,that is ml will understand that 26-35 age group buys more than 18-25 age group
# Label Encoding means:(in the abve example we can use label encoding)
# Converting categorical (text) values into numbers by assigning a unique number to each category.
#it is mostly used when category ORDER matters

#example-
# from sklearn import preprocessing
# le=preprocessing.LabelEncoder() #creation of bject

# df['Age']=le.fit_transform(df['Age']) #fitting and transforming in one step
# print(df['Age'].unique())
#outpu['0-17' '55+' '26-35' '46-50' '51-55' '36-45' '18-25']
# [0 6 2 4 5 3 1]   
#for test we hv to do transfrm
# print(df.head(3))



#City_category
df_City=(pd.get_dummies(df['City_Category'],drop_first=True,dtype=int))
print(df_City.head())
#here we will concat it with aour og dataset
df=pd.concat([df,df_City],axis=1)  #it will concat the two dataset columnwise
print(df.head())
#now we can drop city category column
df.drop(['City_Category'], axis=1, inplace=True)#inplace=True means it will make changes in original dataset


# We didn’t map because mapping creates a fake order.
# We dropped the original column because one-hot columns already carry the city information correctly.


# print(df['City_Category'].unique())
#we can see that city category has 3 categories A,B,C
#we will use label encoding for this
# df['City_Category']=df['City_Category'].map({'A':1,'B':2,'C':3})
# print(df['City_Category'].head())







#missing values
print(df.isnull().sum())
#we can see that product category 2 and 3 have missing values even Purchase column has missing values in test dataset
#purchase should hv null values cuz Purchase is what we are trying to predict.


# Training data = questions with answers # u learn from it
# Test data = questions without answers #u have to predict the answers
# Train.csv → Purchase column filled
# Test.csv → Purchase column empty

#comapny doesnt kow future purchase amount so its missing in test data
#so we will only deal with missing values in product category 2 and 3

print(df['Purchase'])



#focusing on replacing missing values in product category 2 and 3
print(df['Product_Category_2'].unique())
#this will be a DISCRETE variable because it has only few unique values
print(df['Product_Category_2'].value_counts())#vales count used for knowing the number of values are present for howmany times 
#in discrete / categorical variable we can replace missing values with mode 
#mode->most frequently occurring value in the column
print(df['Product_Category_2'].mode()[0]) #it will give the mode value of product category 2
#therefore mode is 8.0

#now we will fillna
df['Product_Category_2']=df['Product_Category_2'].fillna(df['Product_Category_2'].mode()[0])
#we can check if values are filled or not
print(df['Product_Category_2'].isnull().sum()) #it should give 0 if all null values are filled

# df['Product_Category_3']=df['Product_Category_3'].fillna(df['Product_Category_3'].mode()[0])

print(df['Product_Category_3'].unique())
print(df['Product_Category_3'].mode()[0]) #it will give the mode value of product category 3
df['Product_Category_3']=df['Product_Category_3'].fillna(df['Product_Category_3'].mode()[0])
print(df['Product_Category_3'].isnull().sum()) #it should give 0



#stay in current city years
print(df['Stay_In_Current_City_Years'].unique())# output-> ['2' '4+' '3' '1' '0']
# now we dont wnat that 4+ so we gonna  replace + with empty space
df['Stay_In_Current_City_Years']=df['Stay_In_Current_City_Years'].str.replace('+'," ")
print(df['Stay_In_Current_City_Years'].unique())# output   ['2' '4 ' '3' '1' '0']``

print(df.info())
#now we need to convert Stay_In_Current_City_Years into int cuz ognally its in obj
df['Stay_In_Current_City_Years']=df['Stay_In_Current_City_Years'].astype('int')
print(df.info())









#visualization 
#A pairplot is a plot that shows relationships between every pair of numerical features in a dataset at once.
# sns.barplot(x='Age',y='Purchase',hue='Gender',data=df)
# plt.show()
# # # hue = an extra categorical variable used to split bars by color
# # #observation->we can see that 26-35 age group has highest purchase amount and 0-17 age group has lowest purchase amount,also we can see that    male customers have higher purchase amount than female customers across all age groups. 


# # #visulaizatio n of purscahe wrt to occupation
sns.barplot(x='Occupation',y='Purchase',hue='Gender',data=df)
plt.show()
# #observation->we can see that occupation 0 has highest purchase amount and occupation 20 has lowest purchase amount,also we can see that male customers have higher purchase amount than female customers across all occupation groups.
print(df['Occupation'].unique())

#now fro product category 2
sns.barplot(x='Product_Category_2',y='Purchase',hue='Gender',data=df)
plt.show()
# #observation->we can see that product category 8 has highest purchase amount and product category 5 has lowest purchase amount,also we can see that male customers have higher purchase amount than female customers across all product category 2 groups.

print(df.head())


#now we can drop product_Id

#now we ca split data ie test and train data

#feature scailing

df_test=df[df['Purchase'].isnull()]


df_train=df[~df['Purchase'].isnull()]

print(df_test['Purchase'].head())
print(df_test['Purchase'].tail())


print(df_train['Purchase'].head())
print(df_train['Purchase'].tail())

#train  test split

#feature scailing

          # In supervised learning:

          # X = features (inputs)

        #  y = target (what we want to predict) #Gender → feature

                                                 # Age → feature

                                                    # City_Category → feature

                                                 # Purchase → target

# X = df_train.drop('Purchase', axis=1)
# y = df_train['Purchase'] optional way


X=df_train.drop('Purchase',axis=1) #In supervised learning, X = features (inputs)  This is what my model will learn from.
y=df_train['Purchase'] #In supervised learning, y = target variable                This is what my model should learn to predict.
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.33, random_state=42)

X_train.drop('Product_ID',axis=1,inplace=True)
X_test.drop('Product_ID',axis=1,inplace=True)


#feature scailing-> it is a technique to standardize the range of independent variables or features of data. In data preprocessing, it is also known as normalization. The main purpose of feature scaling is to bring all the features to the same scale so that no feature dominates the other and it helps in faster convergence of the model.

#scaling is done to bring all the features to the same scale so that no feature dominates the other and it helps in faster convergence of the model
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.transform(X_test)


#train ur model

# Full Flow Summary

# Separate X and y

# Split into train & test

# Remove useless columns

# Scale training data

# Scale test data using same scaler
















































# Usually our multivariate EDA will be bivariate (looking at exactly
# two variables), but occasionally it will involve three or more variables. It is almost
# always a good idea to perform univariate EDA on each of the components of a
# multivariate EDA before performing the multivariate EDA

# The four types of EDA are univariate non-graphical, multivariate nongraphical, univariate graphical, and multivariate graphical.

# UNIVARIATE NON-GRAPHICAL EDA 63
# at single variables, then moves on to looking at multiple variables at once, mostly
# to investigate the relationships between the variables.
        #    Categorical data
#                 categorical variable are simply the range of
# values and the frequency (or relative frequency) of occurrence for each value
#                      Categorical variables represent groups or labels. They describe a "quality" rather than a measurement. 
             # Nominal Variables: Categories with no natural order. You can’t say one is "higher" than the other.
# Examples: Eye color (Blue, Brown, Green), Country (USA, India, Brazil), Gender, or Marital Status.
           # Ordinal Variables: Categories that have a defined order or rank, but the mathematical distance between them isn't consistent.
# Examples: Satisfaction level (Poor, Fair, Good, Excellent), Education level (High School, Masters, PhD), or T-shirt size (S, M, L, XL). 


# Numerical variables represent measurable quantities. You can perform math (adding, averaging) on these. 
               # Discrete Variables: Countable values that are usually whole numbers. You cannot have "half" of a unit.Examples: Number of children in a family, number of cars in a parking lot, or number of clicks on a link.
              # Continuous Variables: Values that can take any value within a range (including decimals). They are measured rather than counted.Examples: Height (\(175.5\) cm), Temperature (\(22.4\)°C), or Price (\(19.99\)). 




# Types of Exploratory Data Analysis
# There are various types of EDA based on nature of records
# 1. Univariate Analysis->focuses on studying one variable to understand its characteristics.
# Summary statistics like mean, median, mode, variance and standard deviation helps in describing the central tendency and spread of the data


# 2. Bivariate Analysis->Bivariate Analysis focuses on identifying relationship between two variables to find connections, correlations and dependencies

# 3. Multivariate Analysis
# Multivariate Analysis identify relationships between two or more variables in the dataset and aims to understand how variables interact with one another which is important for statistical modeling techniques.





#from gpt -steps(imp steps in eda in data from data importing till data which is cleaned to train model)
# 1️⃣ Import Libraries & Data
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns

# df = pd.read_csv('data.csv')

# 2️⃣ Basic Data Understanding

# Purpose: What does my data look like?

# df.head()
# df.tail()
# df.shape
# df.columns
# df.info()
# df.describe()


# ✔ rows & columns
# ✔ data types
# ✔ numeric summary

# 3️⃣ Identify Target & Features
# X = df.drop('target', axis=1)
# y = df['target']


# Understand:

# prediction type (regression / classification)

# feature roles

# 4️⃣ Check Missing Values
# df.isnull().sum()
# df.isnull().mean() * 100


# Decide:

# drop

# fill (mean / median / mode)

# domain-based fill

# 5️⃣ Handle Missing Values
# df['col'].fillna(df['col'].median(), inplace=True)
# df.dropna(inplace=True)

# 6️⃣ Feature Type Identification (VERY IMPORTANT)

# Classify columns as:

# Continuous

# Discrete

# Categorical

# Ordinal

# Datetime

# This decides what preprocessing to apply.

# 7️⃣ Handle Categorical Variables
# pd.get_dummies(df, drop_first=True)


# or

# LabelEncoder / OneHotEncoder

# 8️⃣ Outlier Detection
# sns.boxplot(x=df['col'])
# df['col'].quantile([0.01, 0.99])


# Handle by:

# capping

# removing

# transformation

# 9️⃣ Univariate Analysis
# sns.histplot(df['col'])
# sns.countplot(x='category', data=df)


# Understand distribution & skewness.

# 🔟 Bivariate / Multivariate Analysis
# sns.scatterplot(x='col1', y='col2', data=df)
# sns.barplot(x='cat', y='target', data=df)
# sns.heatmap(df.corr(), annot=True)


# Find:

# relationships

# correlations

# multicollinearity

# 1️⃣1️⃣ Feature Engineering

# Create new features:

# df['total_price'] = df['units'] * df['price']
# df['year'] = df['date'].dt.year


# Drop useless ones:

# df.drop(['id', 'name'], axis=1, inplace=True)

# 1️⃣2️⃣ Scaling / Normalization
# from sklearn.preprocessing import StandardScaler
# scaler = StandardScaler()
# df_scaled = scaler.fit_transform(df)


# Needed for:

# Linear models

# KNN

# SVM

# Neural Networks

# 1️⃣3️⃣ Train-Test Split
# from sklearn.model_selection import train_test_split

# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=42
# )

# 1️⃣4️⃣ Final Check (Model-Ready?)

# ✔ No missing values
# ✔ All numeric
# ✔ No leakage
# ✔ Scaled if required

# X_train.info()

# 🧠 One-Page Memory Flow (EXAM GOLD)
# Import →
# Understand →
# Clean →
# Analyze →
# Engineer →
# Encode →
# Scale →
# Split →
# Model

# One-line exam answer 💯

# EDA involves understanding data structure, handling missing values and outliers, analyzing distributions and relationships, engineering features, encoding categorical variables, and preparing clean data for model training.