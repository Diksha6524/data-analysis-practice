import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
#we use sns for heatmaps and correlations,eda,mlanalysis
#we use plt for simple line,bar,scatter graph,full customization


# import sweetviz as sv

# df=pd.read_csv('coffee.csv')
# print(df.head())

# report=sv.analyze(df)  
# report.show_html()   #tried using new tool for eda


#we will be woking with zomato data set so basically this dataset was n json format which is converted into csv file by the krishnaik(im referring his videos for the smae)
df=pd.read_csv(r'zomato/zomato.csv',encoding='latin1')
print(df.head())
print(df.columns)
print(df.info())#column names and dtype
print(df.describe())#only describes ntegers ie gives mean std etc


#numerical variables
#int64,float64
#used for: mean,max,min,correlations

#categorical variables
#objct,bool,category
#needs;encoding grouping,value_counts()


###missing values,explore numerical variableszand categorical variables,finding relations hsips between features


#missing values
print(df.isnull().sum())
#0r


null_value=[features for features in df.columns if df[features].isnull().sum()>0]
print(null_value)
  #heatmap->color-based table that shows how strong / weak values are.
plt.figure(figsize=(5,3),dpi=200)
sns_heatmap=sns.heatmap(df.isnull(),yticklabels=False,cbar=False,cmap='viridis')#cabra ->color bar,,Dark Blue  →  -1 Light Blue →   0  Red →  +1,,,cmap->color style of heatmap  excmap='coolwarm' Blue → negativen Red → positive
plt.show()
print(sns_heatmap)


df_country=pd.read_excel('zomato/Country-Code.xlsx')
print(df_country.head())


#merging two datasets cuz both have same column named country code
final_df=pd.merge(df,df_country,on='Country Code',how='left') #cuz i wnat left dataset that is df which is imp
print(final_df.head())

#id u wamma just check datatypes
print(final_df.dtypes)

#finiing out howman countries in dadatsetor in column country
print(final_df['Country'].value_counts()) #observation-> maximum number is of india ie many or more number of transactions in india
#if we only wanna know country names then ->final_df['Country'].value_counts().index
#if we only want valuse and no country name then->final_df['Country'].value_count().values
country_names=final_df['Country'].value_counts().index

Country_values=final_df['Country'].value_counts().values
print(Country_values)
# #lets create pie chart ob it
# plt.pie(Country_values,labels=country_names,autopct='%.2f%%')
# print(plt.show())

#lets create pie chart on top 3countries
# plt.pie(Country_values[:3],labels=country_names[:3],autopct='%.2f%%')
# print(plt.show())
#observation->zomatos max transaction is from india then usa then uk

#relations

#for wrking with many columns we can use grpby()

agg=final_df.groupby(['Aggregate rating','Rating color','Rating text']).size()#size() used for->“How many records exist for each combination of rating, color, and text
print(agg)

#opAggregate rating  Rating color  Rating text
# 0.0               White         Not rated      2148
# 1.8               Red           Poor              1
# 1.9               Red           Poor              2
# 2.0               Red           Poor              7
# 2.1               Red           Poor             15
# 2.2               Red           Poor             27
# 2.3               Red           Poor             47
# 2.4               Red           Poor             87
# 2.5               Orange        Average         110
# 2.6               Orange        Average         191
# 2.7               Orange        Average         250
# 2.8               Orange        Average         315
# 2.9               Orange        Average         381

# agg1=final_df.groupby(['Aggregate rating','Rating color','Rating text']).size().reset_index()#size() used for->“How many records exist for each combination of rating, color, and text
#here we used resetindex cuz here we want all this columns with indexing starting form 0
# print(agg1)
#op
#     Aggregate rating Rating color Rating text     0
# 0                0.0        White   Not rated  2148
# 1                1.8          Red        Poor     1
# 2                1.9          Red        Poor     2
# 3                2.0          Red        Poor     7
# 4                2.1          Red        Poor    15
# 5                2.2          Red        Poor    27
#here column 0 gives number or totla number of somthung which is rated a this this like tbhat
#example index hs agg rating as 0.0 and in totla 2148 has 0.0 rating

#so we nened to chnage 0 column name 
rating=final_df.groupby(['Aggregate rating','Rating color','Rating text']).size().reset_index().rename(columns={0:'rating count'})
print(rating)

# lts find relations bwteen agg rating and rating count
white=(rating['Aggregate rating']==0.0)
red=(rating['Aggregate rating']>=1.8) & (rating['Aggregate rating']<2.5)
orange=(rating['Aggregate rating']>=2.5) & (rating['Aggregate rating']<3.5)
yellow=(rating['Aggregate rating']>=3.5)& (rating['Aggregate rating']<4.0)
green=(rating['Aggregate rating']>=4.0) & (rating['Aggregate rating']>4.5)
darkgreen=(rating['Aggregate rating']>=4.5)
color=['white','red','orange','yellow','green','darkgreen'] #Zwe cann do this all for plt not for sns 
#for sns if we wanna see color similare to rating color wecn use attribute such as hue="column name  containing color", or use palette and pass on colors
# plt.figure(figsize=(5,3),dpi=200)
# relation_agg_color=sns.barplot(x='Aggregate rating',y='rating count',hue='Rating color',palette=color,data=rating)#data tarribute used to know frm where we hv to take data from which dataframe

# print(plt.show())
# observatons->not rated count is too high,max number of ratings is between 2.5 to 3.4
# we cam aslo conclude that is their is na value or null value for ratings then we can fill up that values using  the valuse from rnage  2.5 to 3.4

#count plot- used specially for categorical value
# sns.countplot(x='Rating color',data=rating,palette=color)
# plt.show() #from this graph we can se what color has occured more in dataset,ie orangehas many records(columns)


#find countries names that has given 0 ratings
# if final_df['Aggregate rating']==0.0:
#     print(final_df['Country']) this is wrong cuz if tstament only considers one boolvlaue nbut here their is series
# ?therefore we use boolean indexing
print(final_df[final_df['Aggregate rating'] == 0.0]['Country'])
print(final_df[final_df['Aggregate rating'] == 0.0].groupby('Country').size().reset_index())
#observation->max 0 ratings from india

#find out which currency is used by which country
print(final_df[['Currency','Country']].head(10))

corrency_country=final_df.groupby(['Country','Currency']).size()
print(corrency_country)

# which countries do hv online delivery
print(final_df[['Country','Has Online delivery']])

print(final_df[final_df['Has Online delivery']=='Yes'].groupby('Country').size())
#observations->ONLINE DILEVRIES ARE AVILABLE ONLY IN INDIA AND UAE BUT IN SOME PARTS OF INDIA NO NLINE DILIVERIES



#create a pie chart for cities distribution
# print(final_df.columns)
# city_name=final_df['City'].value_counts().index
# City_values=final_df['City'].value_counts().values
# plt.pie(City_values[:5],labels=city_name[:5],autopct='%.2f%%')
# plt.show()

#find top 10 cuisines
cuisines=final_df['Cuisines'].value_counts().head(10)
print(cuisines)
#if we use .index we get string  ie labels
#index is attribute not a function


















#now we hv to find relationshhipe of all this with differenet differenet countries
