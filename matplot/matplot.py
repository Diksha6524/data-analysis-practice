import pandas as pd
# """
# Matplotlib Data Visualization Examples
# This module demonstrates various matplotlib plotting techniques including:
# - Line plots with labeled axes and titles
# - Scatter plots for machine learning visualization
# - Integration with pandas DataFrames
# - Custom styling (fonts, colors, line styles, markers)
# - Figure sizing and DPI configuration
# - Tick customization
# - Legend usage for distinguishing multiple plot lines
# - Graph saving functionality
# - Bar charts with custom styling
# The legend() method is used to display a legend box that identifies and 
# distinguishes multiple plot lines or data series on a single graph. It improves 
# readability by showing which line corresponds to which data series (via the 
# 'label' parameter), making it easier to interpret graphs with multiple overlapping 
# or adjacent lines. The legend is particularly useful when plotting multiple lines 
# on the same figure to avoid confusion about what each line represents.
# """
# import matplotlib.pyplot as plt
# import numpy as np



x=[1,2,3,4,5]
y=[2,4,6,8,10]
plt.plot(x,y)
# print(plt.show())

# #if labeling
plt.xlabel('x axis')
plt.ylabel('y axis')
#title to that graph
plt.title("student Marks")
print(plt.show())



# #for ml we mstly use scattre plot
import matplotlib.pyplot as plt

A = [1, 2, 3, 4, 5]
B= [5, 7, 4, 6, 8]

plt.scatter(A, B)
plt.xlabel("A")
plt.ylabel("B")
plt.title("Scatter Plot Example")
print(plt.show())

# #using matplot with pandas

data={
    'day':['mon','tues','wed','thurs','fri','sat','sun'],
    'sales':[200,300,400,350,600,350,640] #here no. of values should be same in both x and y 
    }#its a dictionary as its in key : value pair
#if x={ 10,20} then its a set

df=pd.DataFrame(data)
plt.plot(df['day'],df['sales'])
plt.title(' daily sales')
plt.xlabel('Days')
plt.ylabel('Sales')
print(plt.show())



# #basic graph
plt.plot([0,1,2,3],[0,2,4,6]) #plt.plot(x,y)
plt.xlabel('random num1') #cn change fontsize and all here too
plt.ylabel('random num2')
plt.title('random graph', fontdict={'fontname':'Cosmic Sans MS ','fontsize': 10, 'color': 'yellow', 'weight': 'bold', 'family': 'serif'}) #we can chnage font too


# #we can chnage ticks too
plt.xticks([0,1,2,3])
plt.yticks([0,2,4,6])

print(plt.show())


a=[1,2,3,4]
b=[3,6,9,12]

# #resize graph
plt.figure(figsize=(5,3),dpi=180)

#plt.plot(a,b,label='3x',color='green',linestyle='--',linewidth=4,marker='*',markersize=10,markeredgecolor='blue')
#we can make changes using short hand notations too
#fmt='[color][marker][line]'
plt.plot(a,b,'r^--',label='2x')
plt.title('graph',fontdict={'fontname':'Comic Sans MS','fontsize':8})
plt.xlabel('random num1') #cn change fontsize and all here too
plt.ylabel('random num2')
A=np.arange(0,4.5,0.5)
# plt.plot(A,A**2,'r',label='A^2')
#wr want projection of only some values
plt.plot(A[:5],A[:5]**2,'r',label='A^2')
#for showig some diff type of line or some variation
plt.plot(A[4:],A[4:]**2,'r--')

# #we use legend to make the line of graph more interesting
# #we cana also change thickness color n many more of line
plt.legend()

# #we can save graph too
plt.savefig('mygraph.png',dpi=200)
print(plt.show())




# #barcharts
labels=['a','b','c']
values=[1,2,3]
# #can change fig size
bars=plt.bar(labels,values)
# bars[0].set_hatch('/')
# # or
patterns=['/','#','*']
for bar in bars:
    bar.set_hatch(patterns.pop(0))
plt.legend()

print(plt.show())
#alluppercode is commented

#realworld example
#line graph
gas=pd.read_csv('https://raw.githubusercontent.com/KeithGalli/matplotlib_tutorial/refs/heads/master/gas_prices.csv')
print(gas.head())
plt.figure(figsize=(8,5))
plt.plot(gas.Year,gas.USA,'r.-',label='USA')
plt.plot(gas.Year,gas.UK,'b.-',label='UK')
plt.plot(gas.Year,gas['South Korea'],'y.-',label='South Korea')

#this is how to plot all or many countries 
for country in gas:
    if country != 'Year':
        plt.plot(gas.Year,gas[country],marker='.',label=country)


plt.title('USA vs UK vs SK gas prices')
plt.xlabel('years')
plt.ylabel('Dollar/Gallon')
plt.legend()

#if i want ticks till 2011    .tolist()+[2011]
plt.xticks(gas.Year[::3].tolist()+[2011])
print(plt.show())



#histogram

fifa=pd.read_csv('fifa_data.csv')

print(fifa.head())
bins=[40,50,60,70,80,90,100]
plt.xticks(bins)
plt.yticks([0,100])
plt.ylabel('number of players')
plt.xlabel('skill level')
plt.title('distribution of  player skils in fifa')
plt.hist(fifa.Overall,bins=bins,color='blue')
print(plt.show())


#pie chart

# #lets see using pie chart what leg is prefferable by  player
left_leg=fifa.loc[fifa['Preferred Foot']=='Left'].count()[0]
print(left_leg)
right_leg=fifa.loc[fifa['Preferred Foot']=='Right'].count()[0]
print(right_leg)
labels=['left_leg','right_leg']
color=['#abcdef',"#69c5f3"]
plt.pie([left_leg,right_leg],labels=labels,colors=color,autopct='%.2f %%') #we used percentage  of right and left leg with  .2f ,we used %% to show % sign in utput
plt.title('foot preffered by fifa players')
print(plt.show())


#weights of fifa players using pie chart
#as weights are in format 159lbs and we just want numbers 
# print(fifa['Weight'].head(10))
fifa_weight_onlyNumber=fifa['Weight'].str.extract(r'(\d+)')
print(fifa_weight_onlyNumber)
print(fifa_weight_onlyNumber.isna().sum())
fifa['Weight']=fifa_weight_onlyNumber

fifa['Weight']=pd.to_numeric(fifa['Weight'],errors='coerce')
print(fifa['Weight'])
# fifa_weight_onlyNumber = fifa_weight_onlyNumber.astype(int),wanted to do tis to chnage datatype to int but as this clumns hv na valus we cant actually to it
# print(fifa_weight_onlyNumber.info())


light_players=fifa.loc[(fifa.Weight < 125)].count()[0]#[0] ->[0] is used to extract a single count from a Series returned by .count()  best way .shape[0]
light_medium_players=fifa.loc[(fifa.Weight >= 125) &(fifa.Weight < 150)].shape[0]
medium_players=fifa.loc[(fifa.Weight >= 150) &(fifa.Weight < 175)].shape[0]
medium_heavy_players=fifa.loc[(fifa.Weight >= 175) &(fifa.Weight < 200)].shape[0]
heavy_players=fifa.loc[(fifa.Weight >= 200)].shape[0]
print(light_players,light_medium_players,medium_players,medium_heavy_players,heavy_players)
weights=[light_players,light_medium_players,medium_players,medium_heavy_players,heavy_players]
labels=['under 125','125-150','150-175','175-200','over 200']
plt.style.use('ggplot')
plt.title('weight distribution')
explode=(.4,.2,0,0,.4)
plt.pie(weights,labels=labels,autopct='%.2f %%',pctdistance=0.8,explode=explode)
print(plt.show())

#lets see diffirenet teams  ## box plot
barcelona=fifa.loc[fifa.Club=='FC Barcelona']['Overall']
madrid=fifa.loc[fifa.Club=='Real Madrid']['Overall']
NER=fifa.loc[fifa.Club=='New England Revolution']['Overall']
plt.style.use('default')
labels=['FC Barcelona',"Real Madrid",'New England Revolution']
boxes=plt.boxplot([barcelona,madrid,NER],labels=labels,patch_artist=True,medianprops={'linewidth':2})
# colors=['red''blue','yelow']
for box in boxes['boxes']:
    #seeting edge color
    box.set(color="#001a30",linewidth=2)
#fill color chnage
    box.set(facecolor="#a814a3")

plt.title('proffesional soccer playerteams compariosn')
plt.ylabel('oVER ALL RATINGS')
print(plt.show())
