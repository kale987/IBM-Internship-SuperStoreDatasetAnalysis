# -*- coding: utf-8 -*-
"""Analysis of Superstore  Dataset.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11RE6GAmLHOSqk11BL88cMamwbAmApjam

# Analysis of SuperStore  Dataset

##Content
      Used Libraries

      Load and Check Data

      Data Cleaning

      Understanding Data

      Profit and Sales Analysis of Products

      Geo-Analysis based on profits and sales

      Profit and Sales Anlysis (based on the category)

      Conclusion

## Used Libraries
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

"""## Load Datasset"""

path="/content/drive/MyDrive/dataset/SampleSuperstore.csv"
dataset=pd.read_csv(path)

"""## Understanding the Data"""

dataset

dataset.head()

#details about dataset
dataset.info()

#details about the dataset
dataset.describe()

"""##Data Cleaning"""

dataset.duplicated().sum()#getting the duplicate values

dataset.drop_duplicates(inplace=True)#taking care of duplicate values

dataset.duplicated().sum()

for feature in dataset.columns:
    print(feature,':',dataset[feature].nunique())#to find the unique values in each columns

"""## Profit and Sales Analysis

## Top Products in Sales
"""

# Group the data by Product Name and sum up the sales by product
product_group = dataset.groupby(["Sub-Category"]).sum()["Sales"]

product_group.head()

"""## Top 5 Selling Products"""

# Sort the data by sales in descending order
top_selling_products = product_group.sort_values(ascending=False)
top5_selling_products=top_selling_products[0:5]

top5_selling_products

top5_selling_products.plot(kind="bar")

# title
plt.title("Top 5 Selling Products in Superstore")

#  labels for the x and y axes
plt.xlabel("Product Name")
plt.ylabel("Total Sales")

# plot
plt.show()

"""The top 5 selling products consist of everyday items such as phones, chairs, storage solutions, tables, and binders. This suggests that there is consistent demand for these products, making them essential commodities in the market.

##Top 5 Profit Products
"""

#grouping the data according to profit
product_group = dataset.groupby(["Sub-Category"]).sum()["Profit"]

top_profit_products = product_group.sort_values(ascending=False)

top5_profit_products =pd.DataFrame(top_profit_products[:5])

top5_profit_products

top5_profit_products.plot(kind="bar")

plt.title("Top 5 Profit Products in Superstore")

plt.xlabel("Product Name")
plt.ylabel("Total Profit")

plt.show()

"""the top 5 profit products differ slightly from the top-selling products, with copiers taking the lead in terms of generating profits. This could be due to higher margins or the sale of premium models within this category. Phones, accessories, papers, and binders also rank high in terms of profitability, indicating that these items are not only popular but also lucrative for the Superstore.

##City wih most Profits
"""

dataset["City"].unique()

cities_profit=pd.DataFrame(dataset.groupby("City")["Profit"].sum())
cities_profit.reset_index(inplace=True)

cities_profit.head(10)

fig = px.treemap(cities_profit,
                 path=['City' ,'Profit'],
                 color_continuous_scale='deep',
                 values='Profit',color='Profit')

fig.update_layout(width=1000, height=500)
fig.show()

"""The top 5 cities with the most profits are dominated by major urban centers, with New York City and Los Angeles leading the pack. These cities likely have strong consumer markets and robust economies, contributing to their high-profit margins.

##States by Most Profit
"""

dataset["State"].unique()

state_profit=pd.DataFrame(dataset.groupby("State")["Profit"].sum())
state_profit.reset_index(inplace=True)

state_profit=state_profit.sort_values(by="Profit",ascending=False)
state_profit.head(10)

fig=px.treemap(state_profit,path=["State","Profit"],color_continuous_scale="sunset",
               values="Profit",color="Profit")
fig.update_layout(width=1000,height=500)
fig.show()

"""The top 5 states with the most profits include California and New York, which are two of the most populous and economically influential states in the US. Washington, Michigan, and Virginia also feature on this list, indicating a diverse spread of profitable regions across the country.

## Sales and Profits Comparison between the different regions.
"""

dataset.Region.value_counts()

product = dataset[dataset["Sub-Category"] == "Copiers"]
# Grouping the data by Region
region_group = product.groupby(["Region"]).mean()[["Sales", "Profit"]]
# Ploting
region_group.plot(kind="bar")
plt.show()

"""The analysis highlights an interesting trend between the regions. The East Region records the highest sales, indicating strong consumer demand and extensive market reach. However, the Central Region leads in profits, suggesting that this region is particularly effective in managing costs, optimizing pricing, or selling higher-margin products.

##Profit according to the category of Products
"""

#pie graph for representation of profit
dataset.groupby("Category")["Profit"].sum().plot.pie(autopct="%1.0f%%")

plt.figure()
ax = sns.stripplot(y='Category', x='Profit', data=dataset)
plt.tight_layout()

"""##Sales according to the category of Products"""

#Pie graph for representation of Sales
dataset.groupby("Category")["Sales"].sum().plot.pie(autopct="%1.0f%%")

plt.figure()
ax = sns.stripplot(y='Category', x='Sales', data=dataset)
plt.tight_layout()

"""##Conclusion

####These are the top 5 Cities with most Profits:
*   New York City
*   Los Angeles
*   Seattle
*   San Francisco
*   Detroit  

####These are the top 5 States with most Profits:

*   California
*   New York
*   Washington
*   Michigan
*   virginia

####These are the top 5 selling Products:

*   Phones
*   Chairs
*   Storage
*   Tables
*   Binders

####These are the top 5 profit Products:
*   Copiers
*   Phones
*   Accessories
*   Papers
*   Binders

####The East Region has most sales but the Central Region is leading in profits after selling the products.

####Based on the provided Sales and Profit analysis of the Superstore Data, we can draw several significant conclusions.
####In conclusion, the sales and profit analysis reveals valuable insights into the Superstore's performance. It showcases the most profitable cities, states, and products, as well as the regional variations in sales and profitability. Armed with this information, the Superstore can make informed business decisions to further enhance its operations and capitalize on its strengths to drive sustainable growth and success.
"""

