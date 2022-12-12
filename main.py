# Python Pandas Tutorial Series
import pandas as pd

# Ready to start doing some coding!!

# Datasets and Dataframes
# Let's say we have a vehicle company, and they sell
# different types of vehicles, and they record how many of
# each vehicle they have in stock


my_dataset = {
    'Vehicle': ['Car', 'Bicycle', 'Motorbike', 'Truck'],
    'In-stock': [10, 20, 15, 5]
}

my_dataframe = pd.DataFrame(my_dataset)
print(my_dataframe)

# Datasets in Python are multiple dimensional tables which
# we write as pd.DataFrame. DataFrame is the whole table of data
# We can introduce something know as Series which I'll explore
# later

# Recall elements in a dataframe
print(my_dataframe.loc[0])
# This returns the first row in the dataframe
print(my_dataframe.loc[2])
# this returns the third row in the dataframe
print(my_dataframe.loc[[0, 2]])

# We can take a slice
print(my_dataframe.loc[0:2])


# Renaming Indexes and locating them

# creating a new dataset:
dataset2 = {
    'Cars' : [20, 15, 12],
    'Bicycles' : [25, 23, 15]
}
dataframe2 = pd.DataFrame(dataset2, index=['Monday', 'Tuesday', 'Wednesday'])
print(dataframe2)

# We can locate elements in the new dataframe using their renamed index
print(dataframe2.loc['Wednesday'])


# Series
a = [20, 15, 12]    # This is a list
series = pd.Series(a)
print(series)

# We can also locate elements within a series
print(series[1])

# Similar to dataframes, we can also relabel Series!
b = [21, 10, 12]
series2 = pd.Series(b,index=['Monday', 'Tuesday', "Wednesday"])
print(series2)

# Excel

# Now that we have explored series and dataframes , we're going to
# import excel!

# Pandas to read csv file:
df = pd.read_csv('my_data.csv')
print(df)

# Locating rows
# This will return the first row
print(df.loc[0])
# Lets return different rows
print(df.loc[[0,3]])
# We can also take a slice
print(df.loc[0:3])

# We can use the head() and tail() operation in pandas
# This will return the first 5 rows
print(df.head())
# This will return the first 7 rows
print(df.head(7))
# This will return last 5 rows
print(df.tail())
# This will return last 3 rows
print(df.tail(3))
# Let's return some information about the dataset:
print(df.info())

# Now we've looked at an Excel dataset wth full entries
# Let's explore a dataset that has entries missing
df2 = pd.read_csv('my_data2.csv')
print(df2)

# Utilize the .info() section of Pandas
print(df2.info())

# We can drop the rows that have empty entries in
complete_df = df2.dropna()
print(complete_df)

# Instead of completely removing rows, we can replace them
# with a given value
# df2.fillna(10, inplace=True)
# print(df2)

# Let's say we just want to replace the empty entries in the car column
df2['Trucks'].fillna(130, inplace=True)
print(df2)

# Mean, Mode and Median and replacing empty entries
# Mean and replacing the entries with this mean value
mean = df2['Cars'].mean()
print(mean)
df2['Cars'].fillna(mean, inplace=True)
print(df2)

# Mode
mode = df2['Cars'].mode()[0]
print(mode)

# Median
median = df2['Cars'].median()
print(median)

# Finally, we can simply replace an index by doing the following:
df2.loc[6, 'Cars'] = 4000
print(df2)

# Finally I'm going to show you how you can incorporate
# matplotlib with Pandas
# Plotting with Pandas

# Import matplotlib
import matplotlib.pyplot as plt

# This will plot the dataframe df as defined above
df.plot()
plt.show()