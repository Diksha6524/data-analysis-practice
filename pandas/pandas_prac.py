import pandas as pd

toys = pd.DataFrame({
    'Order_ID': [101,102,103,104,105,106,107,108,109,110],
    'Toy_Name': ['Car','Doll','Car','Puzzle','Doll','Car','Puzzle','Doll','Car','Puzzle'],
    'Category': ['Vehicle','Figure','Vehicle','Educational','Figure','Vehicle','Educational','Figure','Vehicle','Educational'],
    'Age_Group': ['3-5','3-5','6-8','6-8','3-5','6-8','3-5','6-8','3-5','6-8'],
    'Price': [300,500,320,400,520,310,420,510,330,410],
    'Units_Sold': [10,5,8,7,6,9,4,6,11,5],
    'Day': ['Mon','Mon','Tue','Tue','Wed','Wed','Thu','Thu','Fri','Fri']
})

print(toys)
print(toys.info())


#total units sold per toy

print(toys.groupby('Toy_Name')['Units_Sold'].sum())

#avg price of toys by category
print(toys.groupby('Category')['Price'].mean())

#tota revenue per order
toys['revenue']=toys['Price']*toys['Units_Sold']
print(toys['revenue'])

#highest selling toy (by units)
print(toys.groupby('Toy_Name')['Units_Sold'].sum().head(1))#instead of head(1) we can write .idxmax()

print(toys.groupby('Toy_Name')['Units_Sold'].sum().idxmax())



#Filter toys sold more than 8 units

# toys['morethen_8_units']=toys.loc[toys['Units_Sold']>8]]
print(toys.loc[toys['Units_Sold']>8])

#sort toys by price (descending)
toys_sorted = toys.sort_values(by='Price', ascending=False)
print(toys_sorted)


#add cumulative unts sold
toys['cum_sum']=toys['Units_Sold'].cumsum()
print(toys[['cum_sum','Toy_Name']])


#ranks based on price
toys['rank']=toys['Price'].rank()
print(toys[['rank','Toy_Name']])

#pivot questions


#diffrence between pivot() and pivot_table()

#pivot->used for reshaping
#used only when each row is unique
#example
#df.pivot(index='Day', columns='Toy_Name', values='Units_Sold')
# One value per (index, column) pair
# No aggregation needed
# DataFrame.pivot(
#     index='row_column',
#     columns='column_to_spread',
#     values='values_column'
# )

# df.pivot(
#     index='Day',
#     columns='Toy_Name',
#     values='Units_Sold'
# )




#pivot_table()->Use when duplicates exist and you need aggregation
#Can use sum, mean, count, max
#mostly used in data preprocessing
#DataFrame.pivot_table(
#     index='row_column',
#     columns='column_to_spread',
#     values='values_column',
#     aggfunc='mean'   # default
# )

# df.pivot_table(
#     index='Day',
#     columns='Toy_Name',
#     values='Units_Sold',
#     aggfunc='sum'
# )





#pivot() reshapes data without aggregation and fails on duplicates, while pivot_table() supports aggregation and handles duplicate values.
#If dataset is real-world → ALWAYS use pivot_table()




#Pivot: Units sold per Day vs Toy_Name
pivot1=toys.pivot_table(
    index='Day',
    columns='Toy_Name',
    values='Units_Sold',
    aggfunc='sum'


)
pivot1.columns.name='Units_sold_by_toys'#added this lne cuz i wnted my columns to br named and not name less
print(pivot1)


#Pivot: Total revenue by Category & Age Group

pivot2=toys.pivot_table(
    index='Category',
    columns='Age_Group',
    values='revenue',
    aggfunc='sum'
   

)
pivot2.columns.name='total reveneue _by age'

print(pivot2)

#Pivot: Average price per Toy_Name

pivot3=toys.pivot_table(
    index='Toy_Name',
    # columns='',#no columns
    values='Price',
    aggfunc='mean'
)
pivot3.columns.name='avg_price'
print(pivot3)

#Which day has highest total sales?
toy=toys.groupby('Day')['revenue'].sum().idxmax()
print(toy)




# 1️⃣ Linear Regression → how ML thinks
# 2️⃣ Logistic Regression → how ML decides
# 3️⃣ KNN → how ML compares
# 4️⃣ Trees → how ML reasons
