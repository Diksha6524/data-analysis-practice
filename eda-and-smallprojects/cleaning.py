import pandas as pd

bios=pd.read_csv('bios (1).csv')
print(bios.head())


# #what we actually want to see in this dataset
# #ie what should we clean up?
# # |
# # --->
# #get rid of bullet points used in names column
# #removing unnecessary columns
# #split height/weight
# #parse out dates from born and died column
# #parse out city,region and country from 'born' column

df=bios.copy()
print(df.info())

# #removing bullet points
# print(df[df['Used name'].str.contains('•')])

# #lets chnage this bullet point to space
# df['name_contains_bulletpoints']=df['Used name'].str.replace('•',' ')
# print(df.head())


# #spliting height and weight 
# df[['height','weight']]=df['Measurements'].str.split('/',expand=True)#we used expand=true cux we want two columns
# print(df[['height','weight']])
# print(df)

# print(df.info()) 
# # in o/p we noticed that this two columns height and weight were objecst we want them to be numeric values
# # and in the columsn of height and weight they hv 'cm' and 'kg' units with them which we dont want 
# # i wanna check if measurement column has same pattern that is all rows or va;ues in columns has / pattern or not



# #check / from all rows of mr=easurements
# print(df[~df['Measurements'].str.contains('/',na=False) & df['Measurements'].notna()]) #here we just seeing values which hv no / in it plus no na values,~ means negotiation     and it returns true or false value
#  # now i wanna see if i split just '180cm' by / whats output will i get?
#  #consider small dataset
# # small_dataset=pd.DataFrame(['180 cm','183 cm/ 150 kg','188 cm/ 120 kg','100 kg'],columns=['measures'])
# # print(small_dataset)

# # #now ill split it
# # small_dataset[['height','weight']]=small_dataset['measures'].str.split('/',expand=True)
# # small_dataset['weight'].fillna(small_dataset['height'],inplace=True) #this copies single value on both columns
# # print(small_dataset.head()) # in here 100 kgs went into height column rather then weight#
# # #op
# # #          measures  height   weight
# # # 0          180 cm  180 cm     None
# # # 1  183 cm/ 150 kg  183 cm   150 kg
# # # 2  188 cm/ 120 kg  188 cm   120 kg
# # # 3          100 kg  100 kg     None


# # # we need only cm into height column n so open
# # #therefore we use strip method

# # small_dataset['height']=pd.to_numeric(small_dataset['height'].str.strip(' cm'),errors='coerce')
# # small_dataset['weight']=pd.to_numeric(small_dataset['weight'].str.strip(' kg'),errors='coerce')
# # print(small_dataset)
# # #output
# # #          measures  height  weight
# # # 0          180 cm   180.0     NaN
# # # 1  183 cm/ 150 kg   183.0   150.0
# # # 2  188 cm/ 120 kg   188.0   120.0
# # # 3          100 kg     NaN   100.0



# # and in the columsn of height and weight they hv 'cm' and 'kg' units with them which we dont want
# df['height']=df['height'].str.extract(r'(\d+)') #r'(\d+)'-> means r means regulare expression and rest means we just need to extrac digtd from thet column srather then words like 'cm' and 'kgs' 
# # df['weight']=df['weight'].str.extract(r'(\d+)')# or me can do 
# df['weight']=df['weight'].str.split(' kg') #more efficient way to doit 

# print(df[['height','weight']])
# #o/p
# #          NaN      NaN
# # 1         183  [ 76, ]
# # 2         183  [ 76, ]
# # 3         168  [ 64, ]
# # 4         NaN      NaN
# # ...       ...      ...
# # 145495    167  [ 61, ]
# # 145496    168  [ 65, ]
# # 145497    163  [ 55, ]
# # 145498    166     None

# print(df.head(2))

# df['height']=pd.to_numeric(df['height'].str.strip(' cm'),errors='coerce')
# df['weight']=pd.to_numeric(df['weight'].str.strip(' kg'),errors='coerce')


# # print(df['Measurements'])#from this i can see some people hv na values and some just hv height 
# print(df.head)


#parse out dates from born and died column
date_pattern=r'(\d+ \w+ \d{4}|\d{4})'

df['born_dates']=df['Born'].str.extract(date_pattern)
df['born_dates']=pd.to_datetime(df['born_dates'],format='mixed',errors='coerce')
#if i just want year or month i can do   df.born_dates.dt.month/year
#we can use to_datetime()
print(df.head(95))
print(df[['born_dates','Born']]) 


print(df['Died'])
#asme we can do for die date
df['Died_dates']=df['Died'].str.extract(date_pattern)
df['Died_dates']=pd.to_datetime(df['Died_dates'],format='mixed',errors='coerce')

print(df[['born_dates','Died_dates']])

print(df.info())
#if i just want year or month i can do   df.born_dates.dt.month/year




#we can check first ig everything is in the same patter in born column ie like this ' 30 January 2002 in Serov, Sverdlovsk (RUS)    '
# not_born_samepattren=df[~df['Born'].str.match(date_pattern,na=False)]#usde nego cuz we wanna ssee srows whch doesnt match the same pattern
# print(not_born_samepattren.head(10))

# not_born_samepattren2=df[~df['Born'].str.match(date_pattern,na=False) & df['Born'].notna() ] # gives same result but filter outs na rows
# print(not_born_samepattren2.head(10))

#get city,region and country for m the born column

# loc_pattern=r'in ([\w\s-]+),([\w\s-]+)\+\((\w+)\)'
# df['Born'].str.extract(loc_pattern) 


#df[['Born_city','Born_region','Born_country']]=df['Born'].str.extract(loc_pattern,expand=True)
# df['city']=df['Born'].str.extract(r)



df['city'] = df['Born'].str.extract(r'in ([A-Za-z0-9\s]+),')
df['country'] = df['Born'].str.extract(r'\((\w+)\)')
df['region'] = df['Born'].str.extract(r',\s*([^()]+?)\s*\(')# here i used gpt

print(df[['city','country']])
print(df['region'].head(20))


#use regex101 if confused and want soluion on more kind of examples

#get rid of extra columns


