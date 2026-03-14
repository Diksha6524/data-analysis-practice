from unittest import result
import pandas as pd
##### for accessing data from csv file using pandas
dt=pd.read_csv("people_data.csv")
print(dt.columns)
print(dt.head())
# how many elements  present in dataframe
print(dt.info())
print(dt.describe())
print(dt.shape) 
 
# # what is the index of word micros
print(dt[dt['First Name']=='Lori'])
print(dt.loc[1])  # loc is used to access a row by its index label
# if we hv to find highestsalary or max value from any column
# print(dt['Salary'].max())  HERE WE DONT ANY COLUMN WITH VALUED LIKE THAT
print(dt.max()) # gives max value from all columns present
# print(dt.loc[dt['Age'].idxmax()]) # gives row with max age
print(dt.min()) # min value from all columns 


df=pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],columns=["a","b","c"]) #if we want to give index or row names then we can specify with the help of index parameter ie index=["x","y","z"]
print(df)
print(df.head())
print(df.head(1))
print(df.tail(2)) 
print(df.describe())
print(df.max())
print(df.min())
print(df.info())
print(df.nunique())
# for finding specific value
print(df[df['b']==5])
print(df.shape) #output of format(rows,columns)


#if i hv to load csv file from url
url="https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv"
D=pd.read_csv(url)
print(D.head())

#csv files takes up more memory so we can use other file formats like parquet or feather
results=pd.read_parquet("results.parquet")
print(results.head())
print(results.sample(5))  # Sample 5 rows from the results Data(gives random 5 rows)

#loc and iloc
#Loc= alows us to filter or access data by rows and columns
print(results.loc[0:2,["year","type"]]) #[[rows],[columns]]
print(results.loc[[0,2]])#specific rows
#iloc= access data by index value
print(results.iloc[0:3,0:4]) #[[rows],[columns]]
#iloc-upper index isnt inclusive,loc its inclusive
print(results.type) #accessing column named type
print(results['type']) #accessing column named type
results.index=results['discipline'] #changing index to discipline column, if we want want more columns ['discipline':'place']
print(results.head())
coffee=pd.read_csv("coffee.csv")
print(coffee.head())
#to make changes in og data of coffee
coffee.loc[1,"Units Sold"]=10 #we can also use slice for the same ie for rows
print(coffee.head())
#at and iat
print(coffee.at[1,"Day"])#accessing single value
print(coffee.iat[4,1])#accessing single value by index
#iloc and loc are used for multiple values,iat and at are used for single value
print(coffee.Day)#or print(coffee['Day']),but u cant do coffee.Units Sold bcoz of space in the word
print(coffee.Day.unique()) #gives unique values in day column
print(coffee.nunique()) #gives number of unique values in each column
print(coffee.sort_values("Units Sold")) #sorts data in ascending order
print(coffee.sort_values("Units Sold",ascending=False)) #sorts data in descending order
print(coffee.sort_values(["Units Sold","Coffee Type"],ascending=[0,1])) #sorts by Units sold in descending(decreasing order) and coffee type in ascending(by aplhabetical order)
#for - itrating  through rows, loose performance
for index,row in coffee.iterrows():
    print(index)
    print(row)# also add single row ie row['column name']
    print("\n")
    #or u can write like this
# for index,row in coffee.iterrows():
#    print(f"Index: {index}, Day: {row['Day']}, Coffee Type: {row['Coffee Type']}, Units Sold: {row['Units Sold']}")
###filtering data
bios=pd.read_csv("bios.csv")
print(bios.head())
print(bios.tail())
#condition
print(bios['height_cm']>180) #gives true or false for each row
print(bios.loc[bios['height_cm']>180]) #gives rows where height>180
#or
print(bios[bios['height_cm']>180])#gives rows with height>180 
#for getting specific colums with the same 
print(bios[bios['height_cm']>180][["name","height_cm"]])#no in between ,( ie in between condn and columns)
#for getting specific columns only 
tA=bios.loc[bios['height_cm']>180,["name","height_cm"]]
print(tA)
#multiple conditions
Mul_Cond=bios[(bios['height_cm']>180)&( bios['weight_kg']>80)]
cond=Mul_Cond[['name','height_cm','weight_kg']]
print(cond)
#string operations
Diksha=bios[bios['name'].str.contains("Diksha")]#case senisitive
#If it shoulnd be case sensitive then
diksha=bios[bios['name'].str.contains("diksha",case=False)]
print(Diksha)
print(diksha)
#we can add conitions too
D_iksha=bios[bios['name'].str.contains('diksha|sara',case=False)]
print(D_iksha)
#startswith
start=bios[bios['name'].str.startswith('D')]
print(start)
#endswith
end=bios[bios['name'].str.endswith('a')]
print(end)
#string length
length=bios[bios['name'].str.len()>5]
print(length)
#missing values
miss=bios[bios['height_cm'].isnull()]
print(miss)
#athletexs born in cities that starts wuth a vowel
vowel_C=bios[bios['born_city'].str.contains(r'^[AEIOUaeiou]',na=False)]
#r-> raw string ,aviods escape char
#^ ->startswith  ie example if apple then a is the beggining of the word therfore its true or it will show the name cuz it starts with a vowel
#but for banana it will be false as letter b is at the beggining of the word 
# [AEIOUaeiou] -> any od these letters should be prsent at the beggining
#na=False -> to avoid NaN values
#or u can write it like this
vowel_c=bios[bios['born_city'].str.contains(r'^[aeiou]',case=False,na=False)]
#pandas cant filter rows with NaN values directly so we hv to use na parameterie if borncity has nan value then it will be considered as false
#case=False -> to avoid case sensitivity

print(vowel_C)
print(vowel_c)
#find athletes with names containing exactly two vowels
two_vowels=bios[bios['name'].str.contains(r'^[^AEIOUaeiou]*[AEIOUaeiou][^AEIOUaeiou]*[AEIOUaeiou][^AEIOUaeiou]*$',na=False)]
# ^ -> at the start is for start of the word
# $ -> at the end is for end of the word
# ^ inside []-> negation ie any letter except these
# *-> zero or more occurences of the preceding element
# [AEIOUaeiou]-> any one of these vowels
# [^AEIOUaeiou]*-> any number of non vowels

# exapmle
# R-nonvowel
# o-first vowel
# h-nonvowel
# i-second vowel
# t-nonvowel
# ^ → start

# $ → end

# [^vowels]* → any non-vowels

# [vowels] → one vowel


#athletes with nmes ending with son or sen
end_n=bios[bios['name'].str.contains(r'son$|sen$',na=False,case=False)]
print(end_n)

#find athlestes  with born year starting with 19
year_19=bios[bios['born_date'].str.contains(r'^19',na=False,)]
year_19_2=year_19[['name','born_date']]
print(year_19_2)
#find athletes born in cities containing double letters
double_l=bios[bios['born_city'].str.contains(r'(.)\1',na=False)]
# (.) -> any character
# \1 -> backreference to the first captured group
double_l_2=double_l[['name','born_city']]
#name containg 3 or more vowels
three_v=bios[bios['name'].str.contains(r'([AEIOUaeiou].*){3,}',na=False)]
#* -> zero or more occurences of the preceding element

#regular expressions
# Symbol	Meaning	Example
# ^	start of string	^A
# $	end of string	n$
# .	any one character	c.t
# *	0 or more	ab*
# +	1 or more	ab+
# []	choose one	[abc]
# [^ ]	NOT these	[^aeiou]

_is_in=bios[bios['born_country'].isin(['USA','FRA'])]
print(_is_in)
_is_in_=bios[bios['born_country'].isin(['USA','FRA']) &(bios['name'].str.startswith('A',na=False))]
print(_is_in_)
#instead of using bios again and again we can use query function
bios_query=bios.query('born_country=="USA" & name.str.startswith("Al")')
print(bios_query)
#####ADDING AND REMOVING COLUMNS FROM DATAFRAME
print(coffee.head())
#adding new column "pricez"
coffee['Price']=5.0
print(coffee.head())
#to be specific  we can use numpy function ie where
import numpy as np
coffee['new_Price']=np.where(coffee['Coffee Type']=='Espresso',4.0,5.0)
print(coffee.head())
#using loc 
coffee.loc[coffee['Coffee Type']=='Latte','new_Price']=4.5
print(coffee.head())
#i tried using query method for the same  just to realise im SToPiD, cuz query fun only fo filtering  not for assigning vals
#np.where() / .loc -> assigning vals


# #map is also used
# price_map = {
#     'Espresso': 4.0,
#     'Latte': 5.0
# }
# coffee['new_Price'] = coffee['Coffee Type'].map(price_map)

#removing index
print(coffee.drop(0)) #it doesnt alter the og data
#removing column
print(coffee.drop('new_Price',axis=1)) #axis=1 for column,axis=0 for row
#0r
print(coffee.drop(columns=['new_Price','Units Sold']))
#to make changes in og data
coffee.drop(columns=['new_Price','Price'],inplace=True)
print(coffee.head())

#if i want new dataframe without modifying og data
new_coffee=coffee
new_coffee['Discounted Price']=4.0
print(new_coffee.head())
print(coffee.head())# same output as new coffee bcoz both r pointing to same data in memory
#to avoid this we use copy function
new_coffee_copy=coffee.copy()
new_coffee_copy['Discounted Price']=10
print(new_coffee_copy.head())
print(coffee.head())#og data remains same

#new xcolumn
coffee['revenue']=coffee['Units Sold']*coffee['Discounted Price']
print(coffee.head())
#chnage name  of the columns
# #use dictionary for the same 
coffee.rename(columns={'Discounted Price':'price'},inplace=True)#if we dont want to use inplace i can assign this whole statement to coffee again ie coffee=coffee.rename(....)
print(coffee.head())

#using bios if i wnt to get just firts anme form name column
bios_new=bios.copy()
bios_new['first_name']=bios['name'].str.split(' ').str[0]
print(bios_new.head())
print(bios_new.query('first_name =="Diksha"'))


#for juts birth year from born_date column
#use pd.to_datetime to convert string to datetime object
bios_new['born_datetime']=pd.to_datetime(bios_new['born_date'])# here u might get errors therfore use  errors='coerce'
#for format issue use format for the same ie format='%Y-%m-%d'
print(bios_new.head())
#for getting just year 
bios_new['year']=bios_new['born_datetime'].dt.year
#dt-> datetime accessor
bios_new=bios_new[['name','year']]
print(bios_new.head())


####for dsaving the cahngesz in csv file
bios_new.to_csv("bios_new.csv",index=False) #index=false to avoid extra index column


#for diving hieght into categories
bios['heights_cat']=bios['height_cm'].apply(lambda x: 'Short' if x<170 else ('Medium' if x<=185 else 'Tall') )
print(bios.head())

#function
def cat_ath(row):
    if (row['height_cm']<170) & (row['weight_kg']<70):
        return 'lightwieght'
    elif (row['height_cm']<=185) & (row['weight_kg']<=85):
        return 'midweight'
    else:
        return 'heavyweight'
bios['category']=bios.apply(cat_ath,axis=1) #axis=1 for row,axis=0 for column
print(bios.head())


#concatenation
noc=pd.read_csv('noc_regions.csv')
print(noc.head())


#we can use joins 
#left join-> all rows from left dataframe and matching rows from right dataframe
#right join-> all rows from right dataframe and matching rows from left dataframe
#inner join-> only matching rows from both dataframes
#outer join-> all rows from both dataframes,non matching rows will have NaN values


bios_merged=pd.merge(bios,noc,left_on='born_country',right_on='NOC',how='left')#as a reulst it give suffixes to both nocs's ie here its NOC_y and NOC_x
#we can rename it using suffixes parameter
# bios_merged=pd.merge(bios,noc,left_on='born_country',right_on='NOC',how='left',suffixes=['_bio','_noc'])
print(bios_merged.head())
bios_merged.rename(columns={'region':'born_region'},inplace=True)
print(bios_merged.head())
print(bios_merged['NOC_x'])
# b=bios_merged[bios_merged['NOC_x'] !=bios_merged['born_region']][['name','born_country','NOC_x','born_region']]
# print(b)

#make seprate df based on country
usa=bios[bios['born_country']=='USA'].copy()
france=bios[bios['born_country']=='FRA'].copy()
print(usa.head())
print(france.head())

#if i wanna make new df of just france and usa 
usa_fra=pd.concat([usa,france])
print(usa_fra.head()) #head we see all usa data firts
print(usa_fra.tail())#tail we see all france data at last
print(results.head())
#merge = joins(),join data based on common columns
#concat = appends(),stack data vertically doesnt match based on common columns
#concat- syntax    pd.concat([df1,df2,...],axis=0 or 1) axis=0 for rows,axis=1 for columns
#Horizontal concat-
# pd.concat([df1, df2], axis=1)
# df1 = pd.DataFrame({
#     'id': [1, 2],
#     'name': ['A', 'B']
# })
# df2 = pd.DataFrame({
#     'id': [3, 4],
#     'name': ['C', 'D']
# })
#    id name  id name
# 0   1  A    3  C
# 1   2  B    4  D

#vertical concat-
# pd.concat([df1, df2], axis=0)
# df1 = pd.DataFrame({
#     'id': [1, 2],
#     'name': ['A', 'B']
# })
# df2 = pd.DataFrame({
#     'id': [3, 4],
#     'name': ['C', 'D']
# })
#    id name
# 0   1  A
# 1   2  B
# 0   3  C
# 1   4  D
#mergre-combines df based on common columns
#like sql joins
#ex-
#left=pd.DataFrame({
#    'id': [1, 2, 3],   
#    'name': ['A', 'B', 'C']
#})
#right=pd.DataFrame({
#    'id': [2, 3, 4],
#    'age': [30, 40]
#})
#pd.merge(left,right,on='id',how='inner')
#   id name age
#0  2  B   30
#1  3  C   40
#pd.merge(left,right,on='id',how='left')
#   id name age
#0  1  A   NaN
#1  2  B   30
#2  3  C   40             #left join- all rows from left df and matching rows from right df
#pd.merge(left,right,on='id',how='right')
#   id name age
#0  2  B   30
#1  3  C   40
#2  4  NaN 40             #right join- all rows from right
#pd.merge(left,right,on='id',how='outer')
#   id name age
#0  1  A   NaN
#1  2  B   30
#2  3  C   40
#3  4  NaN 40             #outer join- all rows from both dfs
#merge creates suffixes for common columns
combined_df=pd.merge(results,bios,on='athlete_id',how='left')#left cuz we wall all rows from left df ir results
print(combined_df.head())
print(combined_df[['athlete_id','name','year','type']].head())
print(combined_df.info())






#HANDLING NULL DATA
print(coffee.head())
null_val=coffee.loc[[1,3],'Units Sold']=np.nan
print(coffee.head())
#to see sum of nan's in each column
print(coffee.isna().sum())




#for nan values in specific columns we can fill it with some numbers or mean/median(as i hv learned in DWM)
fill=coffee.fillna(10)
print(fill)
#mean
fill_mean=coffee.fillna(coffee['Units Sold'].mean())
print(fill_mean)
#interpolate-> used for missing datas
#it fills missing values  using existing patterns
# dates = pd.date_range("2024-01-01", periods=5)
# data = pd.Series([100, None, None, 160, 180], index=dates)
# data.interpolate()
# Output:
# Copy code
# 2024-01-01    100
# 2024-01-02    120
# 2024-01-03    140
# 2024-01-04    160
# 2024-01-05    180
#fills missing values by estimating them from surrounding data points
coffee.loc[[1],'Units Sold']=25
coffee.loc[[2,3],'Units Sold']=np.nan
print(coffee.head())
# coffee['Units Sold']=coffee['Units Sold'].interpolate()
# print(coffee)
#we can drop nan rows too
print(coffee.dropna())
#we can use subset['column names']
print(coffee.dropna(subset=['Units Sold']))
#if i just wanna access rows with na values
print(coffee[coffee['Units Sold'].isna()])
#if i wanna access data with non na values
print(coffee[coffee['Units Sold'].notna()])
#if i hv to lter it permanently the (inplace=true)
print(coffee.dropna(subset=['Units Sold'],inplace=True))
print(coffee)


####DATA AGGREGATION
#basicallu from many values we get one summarizedb value example mean


#example i want to see which city has highest number of olympics winner
bios_most=bios['born_city'].value_counts()
print(bios_most)

#if i only want  to see which region of usa has most winners
bios_Usa=bios[bios['born_country']=='USA']['born_region'].value_counts()
#i can get tail or head for the same
print(bios_Usa.head(10)) #top 10
#groupby
print(coffee)
#changing price of latte coffee
# coffee.loc[coffee['Coffee Type']=='Latte','price']=6
# #.loc[row_condition, column]
# print(coffee)
#sum
cof_sum=coffee.groupby(['Coffee Type'])['Units Sold'].sum()
print(cof_sum)
#mean
cof_mean=coffee.groupby(['Coffee Type'])['Units Sold'].mean()
print(cof_mean)
#agg
coff_agg=coffee.groupby(['Coffee Type']).agg({'Units Sold':'sum','price':'mean'})
print(coff_agg)
print(coffee)

coff_agg1=coffee.groupby(['Coffee Type','revenue']).agg({'Units Sold':'sum','price':'mean'})
print(coff_agg1)


#pivot-> converison on rows to columns
  #example if i wanna get latte and espresso as columns
print(coffee)
pivot=coffee.pivot(columns='Coffee Type',index='Day', values='revenue')
print(pivot)
#output
# Coffee Type  Espresso  Latte
# Day
# Friday          180.0  140.0
# Monday          100.0   40.0
# Saturday        180.0  140.0
# Sunday          180.0  140.0
# Thursday        160.0  120.0
# Wednesday       140.0  100.0
#if i want to grab mondays latte count 
print(pivot.loc['Monday','Latte'])
#sum
print(pivot.sum())
#axis=1 sum(axis=1 is for columns)
print(pivot.sum(axis=1))
print(bios.head)

#in bios if i wanna group people with the year they born
bios['born_date']=pd.to_datetime(bios['born_date'])
bios_borny=bios.groupby(bios['born_date'].dt.year)['name'].count()
print(bios_borny)
#for indexing the same
bios_bornyy=bios.groupby(bios['born_date'].dt.year)['name'].count().reset_index().sort_values('name',ascending=False)
print(bios_bornyy)
#month wise
bios['month_born']=bios['born_date'].dt.month
bios['year_born']=bios['born_date'].dt.year
bios_grp=bios.groupby([bios['year_born'],bios['month_born']])['name'].count().reset_index().sort_values('name',ascending=False)
print(bios_grp)




#ADVANCD FUNCTIONALITY

#SHIFT(),RANK(),ROLLING(),CUMSUM()

#df.shift()

coffee['yest']=coffee['revenue'].shift(1)#shift(1)-> movining data down by 1 row
#example->
# Index	revenue
# 0	100
# 1	120
# 2	90
# 3	150
# coffee['revenue'].shift(1)
# output
# Index	yest
# 0	NaN
# 1	100
# 2	120
# 3	90

# Code	Meaning
# shift(1)	Previous row
# shift(-1)	Next row
# shift(7)	7 rows earlier
# shift(30)	30 days earlier (time-series)
print(coffee['yest'])
print(coffee[['yest','Coffee Type','revenue']])
coffee['pct_change']=coffee['revenue']/coffee['yest']
print(coffee['pct_change'])

#df.rank()-> assigns rank(positions) to values in column based on their order
bios['height_rank']=bios['height_cm'].rank(ascending=False)
print(bios.sort_values(['height_rank']))
print(bios.sort_values(['height_rank']).sample(8))
print(bios.sort_values(['height_rank'])[['height_rank','name']])

#df.rolling()->Takes a fixed-size window
# Moves it row by row
# Computes statistics like mean, sum, max, min


#lets see lasst 3 days revenue
latte=coffee[coffee['Coffee Type']=='Latte'].copy()
print(latte)

latte['3days_revenue']=latte['revenue'].rolling(3).sum()
print(latte[['3days_revenue','revenue','Coffee Type','Day']])


#cumsum->cumulative sum
# Adds values step by step
# Keeps accumulating previous results
#Each row = previous total + current value

# Method	Task
# cumsum()	Cumulative sum
# cummax()	Running maximum
# cummin()	Running minimum
# cumprod()	Cumulative product
print(coffee.head(2))
coffee['cum_sum']=coffee['revenue'].cumsum()
print(coffee[['Day','revenue','cum_sum']])


#NEW FUNCTIONALITY
print(pd.__version__) #2.2.3
#PYARROW
results_numpy=pd.read_csv('people_data.csv')
results_arrow=pd.read_csv('people_data.csv',engine='pyarrow',dtype_backend='pyarrow')
print(results_numpy.info())    
print(results_arrow.info())  


print(results_numpy['First Name'].str.contains('Lori'))
print(results_arrow['First Name'].str.contains('Lori'))


#ai stuff

olympians_filter = bios[(bios['born_region'] == 'New Hampshire') | (bios['born_city'] == 'San Francisco')]
print(olympians_filter.sample(4))

 #using gpt to give dataset to work on 
#cleaing dataset,matplotlib,seaborn
#->ml->dl->pytorch and tensorflow->project



