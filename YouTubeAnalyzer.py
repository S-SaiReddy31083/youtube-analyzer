import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn

data = {
    "Video":["Pandas Tutorial","Numpy Tutorial","Matplotlib Tutorial","Pandas Projects","Scikit-learn Tutorial"],
    "Category":["Data","Data","Data Visualization","Data","Machine Learning"],
    "Upload Date":["01-01-2026","10-01-2026","26-01-2026","05-02-2026","10-03-2026"],
    "Upload Day":["Monday","Wednesday","Friday","Saturday","Sunday"],
    "Views":[200,526,220,1054,424],
    "Likes":[36,54,89,74,102],
    "Comments":[12,20,15,8,74],
    "Watch Time":[150,200,85,74,240]
}
df = pd.DataFrame(data)
print(df)

#Getting Basic Information 
df.info()
#Describe the Dataset
df.describe()

#Printing the Videos with More views In the Dataset
df_sort = df.sort_values(["Video"], ascending=False)
print(df_sort)

#Printing the Dataset with More views
df_view = df.sort_values(["Views"], ascending=False)
print(df_view)

#Printing the Data with Engagement Rate
df["Engagement Rate"] = df["Likes"] / df["Views"]
print(df)

#Finfing the Video with the Highest Engagement Rate
df_engage = df.sort_values(["Engagement Rate"],ascending=False)
print(df_engage)

#Checking the Category Performance by Views
print(df.groupby("Category")["Views"].sum())

#Checking the Average Likes by Category
print(df.groupby("Category")["Likes"].mean())

#Checking the Average Views By Upload Day
print(df.groupby("Upload Day")["Views"].mean())

#Finding the videos With Highest Comments
df_com = df.sort_values(["Comments"],ascending=False)
print(df_com)

#Finding the videos with highest watch time  
df_time = df.sort_values(["Watch Time"], ascending=False)
print(df_time)

#Printing the Bar graph of videos and views
plt.bar(df["Video"],df["Views"],color="green",edgecolor="black")
plt.xlabel("Videos")
plt.ylabel("Views")
plt.title("YouTube Analyzer")
plt.xticks(rotation=45)
plt.legend(["Views"])
plt.show()


plt.plot(df["Engagement Rate"],df["Views"],marker="*",color="brown",linestyle="--")
plt.grid()
plt.xlabel("Engagement Rate")
plt.ylabel("Views")
plt.legend(["Engagement Rate vs Views"])
plt.title("Engagement Rates vs Views")
plt.show()

#Creating Scatter plot for Likes and Comments using the Seaborn
sns.scatterplot(x="Likes",y="Comments",data=df,hue="Category",s=100)
plt.xlabel("Likes")
plt.ylabel("Comments")
plt.title("Likes vs Comments")
plt.legend(title="Category")
plt.show()

#Creating Histogram for Views using the seaborn
sns.histplot(df["Views"],bins=5,color='Orange',edgecolor="black")
plt.xlabel("Views")
plt.ylabel("Frequency")
plt.title("Distribution of Views")
plt.show()

#Predicting the Views Using the Linear Regression Model
from sklearn.linear_model import LinearRegression
x = df[["Likes"]]
y = df["Views"]
model = LinearRegression()
model.fit(x,y)
predicted_views = model.predict(x)
print(predicted_views)

#Creating a Scatter plot for Likes and Views with the Predicted views
plt.scatter(df["Likes"],df["Views"],color="green",edgecolors="black")
plt.xlabel("Likes")
plt.ylabel("Views")
plt.title("Likes vs Views with Predicted Views")
plt.show()





