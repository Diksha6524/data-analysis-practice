import pandas  as pd
import numpy as np
import matplotlib.pylab as plt
dt=pd.read_csv('churn_modelling.csv')
print(dt.head(10))
print(dt.isna().sum())#o na values in any column
#Check shape, columns, and data types
print(dt.info())
print(dt.shape)
#How many male vs female customers?
female=(dt['Gender']=='Female').sum()
male=(dt['Gender']=='Male').sum()
print(female,male) #op:4543 5457
#Count customers from each country
german=(dt['Geography']=='Germany').sum()
france=(dt['Geography']=='France').sum()
spain=(dt['Geography']=='Spain').sum()
# print(german,france,spain)#2509 5014 2477
#How many customers churned (Exited=1)?
exited_cust=(dt['Exited']==1)
print(exited_cust)#2037
# # Average age of customers who churned vs didn’t churn
no_exited_cust=(dt['Exited']==0)
print(dt.loc[exited_cust,'Age'].mean())#this was lowkey confusing gpt helped op:44.8379970544919
print(dt.loc[no_exited_cust,'Age'].mean())#37.40838879819164

# Average balance country-wise
german_balance=(dt['Geography']=='Germany')
france_balance=(dt['Geography']=='France')
spain_balance=(dt['Geography']=='Spain')

print(dt.loc[german_balance,'Balance'].mean())
print(dt.loc[france_balance,'Balance'].mean())
print(dt.loc[spain_balance,'Balance'].mean())
# # """ 119730.1161339179
# 62092.63651575588
# 61818.14776342349 """

# Find customers with:
# Age > 40
# Balance > 100000


cutsomer_age_balance=(dt['Age']>40)&(dt['Balance']>100000)
print(dt.loc[cutsomer_age_balance])#took help of gpt here cuz i wanted to show all rows of this custmers

#What percentage of customers are active members?
#is active yes=1,is active no=0
is_active_customer=(dt['IsActiveMember']==1).mean()*100
print(is_active_customer)#51.51

#Group by NumOfProducts → count churned customers
churned_cust=dt.groupby('NumOfProducts')['Exited'].agg(['count', 'sum'])
print(churned_cust)

# Create a new column Balance_Category:
# Low (<50k)
# Medium (50k–150k)
# High (>150k)
dt['balance_category'] = None
dt.loc[dt['Balance'] < 50000, 'balance_category'] = 'low'
dt.loc[(dt['Balance'] >= 50000) & (dt['Balance']<150000), 'balance_category'] = 'medium'
dt.loc[dt['Balance'] >150000, 'balance_category'] = 'high'
#took help of gpt

# elif (dt['Balance']>=50000)&(dt['Balance']<150000) :
#    dt['balance_category']='medium'
# elif (dt['Balance']>150000) :
#    dt['balance_category']='high' #this is what i did


print(dt['balance_category'])
print(dt.info)


#Which balance category has highest churn?

churn_low=((dt['balance_category']=='low')&(dt['Exited']==1))
print(churn_low.sum())#526

churn_medium=((dt['balance_category']=='medium')&(dt['Exited']==1))
print(churn_medium.sum())#1287

churn_high=((dt['balance_category']=='high')&(dt['Exited']==1))
print(churn_high.sum())#224
    
######numpy
array=np.array[dt['Balance'],dt['Age'],dt['EstimatedSalary']]#this is what i did before using gpt
array = dt[['Balance', 'Age', 'EstimatedSalary']].to_numpy()
print(array)#took hel og gpt cu i wsd too unsure about it

# Find:
# Mean age
# Max salary
# Min balance

min_age=dt['Age'].min()
max_salary=dt['EstimatedSalary'].max()
min_balance=dt['Balance'].min()
print(min_age,max_salary,min_balance)#18 199992.48 0.0

# Normalize EstimatedSalary->“Put everyone on the same measuring scale”
   #Standardization (used a lot in ML)
      #(x - mean) / std
dt['Salary_Standardized'] = (dt['EstimatedSalary'] - dt['EstimatedSalary'].mean()) / dt['EstimatedSalary'].std()
print(dt['Salary_Standardized'])


# #for correltion in between churn and age
co_relation=dt['Age'].corr(dt['Exited'])
print(co_relation)  #0.2853......


# A NumPy mask is:
#  an array of True/False values used to select elements from another array.
#treu values visible ,false values hdden

#if we write just print(mask) it gives array of true and false
#if we put it in arr[mask] it gives array of values which are true 
mask=(dt['Age'] > 35) & (dt['Balance'] > 100000)
print(mask)

print(dt.loc[mask])





#matplotlib
  #basic plot


# # Bar chart: churned vs non-churned customers
exited_cust=(dt['Exited']==1)
no_exited=(dt['Exited']==0)
exited_count=exited_cust.sum()
non_exited_count=no_exited.sum()
plt.bar(['churned ','nonchurned'],[exited_count,non_exited_count])
plt.xlabel('exited customer')
plt.ylabel('non exited customer')
plt.title('curned nd nonchurnec customers')
print(plt.show())

#bar syntax   plt.bar([labels],[values])



#histogarm of cutomers age

bins=[20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]

plt.xticks(bins)
plt.yticks([0,])
plt.hist(dt['Age'],bins=bins,color='blue')

print(plt.show())


#piecutomer by country

german=dt.loc[dt['Geography']=='Germany'].shape[0]
france=dt.loc[dt['Geography']=='France'].shape[0]
spain=dt.loc[dt['Geography']=='Spain'].shape[0]

label=['german_customers','france_cutsomer','spain_customers']
plt.pie([german,france,spain],labels=label,autopct='%.2f%%')
plt.title('customers acroess world')
print(plt.show())