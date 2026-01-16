import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("superstore_large.csv")
print(df.head())

print(df.info())
print(df.describe())

print(df.columns)

print(df.isnull().sum())


#bar plot 

sns.set(style="darkgrid")
sns.barplot(x="City",y="Sales",data=df,hue="Category",palette="viridis")
plt.title("Distribution of Sales by City")
plt.savefig("barplot.png",dpi=300,bbox_inches="tight")
plt.show()


#histogram plot 

sns.set(style="darkgrid")
sns.histplot(x="Sales",data=df,kde="True",hue="Category",bins=40,palette="deep")
plt.title("Distribution of Sales by Category")
plt.savefig("histplot.png",dpi=300,bbox_inches="tight")
plt.show()


#kde plot 

sns.set(style="darkgrid")
sns.kdeplot(x="Sales",data=df,hue="Region",palette="mako",linestyle=":")
plt.xlabel("profit")
plt.ylabel("Density")
plt.title("Sales Density by Region")
plt.savefig("kdeplot.png",dpi=300,bbox_inches="tight")
plt.show()


#box plot 

sns.set(style="dark")
sns.boxplot(x="Category",y="Profit",data=df,hue="Region",palette="plasma")
plt.title("Profit Distribution by Category and Region")
plt.savefig("boxplot.png",dpi=300,bbox_inches="tight")
plt.show()


#violin plot

sns.violinplot(x="Category",y="Sales",data=df,hue="Segment",split=True,palette="viridis")
plt.title("Sales Distribution by Category and Segment")
plt.savefig("violinplot.png",dpi=300,bbox_inches="tight")
plt.show()


#strip plot with box plot

sns.boxplot(data=df, x="Category", y="Profit", color="lightgray")
sns.stripplot(data=df, x="Category", y="Profit", jitter=True)
plt.title("Profit Distribution with Actual Points")
plt.savefig("stripplot.png",dpi=300,bbox_inches="tight")
plt.show()


#jointplot

sns.jointplot(x="Sales",y="Profit",data=df,kind="hex",palette="deep")
plt.savefig("jointplot.png",dpi=300,bbox_inches="tight")
plt.show()


#pairplot

sns.pairplot(df[["Sales","Profit","Discount","Quantity","Category"]], hue="Category",palette="deep",kind="scatter",diag_kind="kde")
plt.savefig("pairplot.png",dpi=300,bbox_inches="tight")
plt.show()


#relplot

sns.relplot(data=df, x="Sales", y="Profit", hue="Category", col="Region")
plt.savefig("relplot.png",dpi=300,bbox_inches="tight")
plt.show()


#heatmap with pivot table

pivot = df.pivot_table(values="Sales", index="Category", columns="Region", aggfunc="mean")
sns.heatmap(pivot, annot=True, fmt=".0f",cmap="Accent")
plt.title("Average Sales by Category and Region")
plt.savefig("Heatmaplot.png",dpi=300,bbox_inches="tight")
plt.show()


#lineplot 

df["Order Date"] = pd.to_datetime(df["Order Date"])
monthly = df.groupby([df["Order Date"].dt.to_period("M"), "Category"])["Sales"].sum().reset_index()
monthly["Order Date"] = monthly["Order Date"].astype(str)

sns.lineplot(data=monthly, x="Order Date", y="Sales", hue="Category")
plt.xticks(rotation=45)
plt.title("Monthly Sales Trend by Category")
plt.savefig("lineplot.png",dpi=300,bbox_inches="tight")
plt.show()

