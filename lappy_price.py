# -*- coding: utf-8 -*-
"""lappy price

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BK7J0zSTNLn8KRzZ88bntoZWl4pZLH_a
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df1=pd.read_csv("/content/laptop_data.csv")

df1.head()

df1.columns

df1.shape

df1.info()

df1.isnull().sum() #for checking missing values

df1.duplicated().sum() #for duplication



df1=df1.drop(["Unnamed: 0"],axis=1)#deleting

df1.head()

df1["Ram"]=df1["Ram"].str.replace("GB","")
df1["Weight"]=df1["Weight"].str.replace("kg","")

df1.head()

df1.info()

#here ram and weight are objects we are converting in to int and float respectivily

df1["Ram"]=df1["Ram"].astype("int32")
df1["Weight"]=df1["Weight"].astype("float32")

df1.info()

#EDA data analysis for univeriant and biveriant

import seaborn as sns

sns.distplot(df1["Price"])#for price analyis

#this graph is skewed beacuse many laptop prices are low in price and some laptops are high prices

df1["Company"].value_counts().plot(kind="bar")

#how many laptops are there accounding to the campany

#average price for each campany
#costly are razar

sns.barplot(x=df1["Company"],y=df1["Price"])
plt.xticks(rotation="vertical")
plt.show()

# type name are total how many types

df1["TypeName"].value_counts().plot(kind="bar")

#price according to type how price varies with type

sns.barplot(x=df1["TypeName"],y=df1["Price"])
plt.xticks(rotation="vertical")
plt.show()

sns.distplot(df1["Inches"])

#as the laptop size increases price also incresing
#there is very small dependency to the size with price

sns.scatterplot(x=df1["Inches"],y=df1["Price"])



#here in each type we are getting resolution type and alse representing wheather laptop
#is touchscreen or not and ips pannel

df1["ScreenResolution"].value_counts()#for different types of resolution

#adding one column for touchscreen

df1["TouchScreen"]=df1["ScreenResolution"].apply(lambda x:1 if "Touchscreen " in x else 0)

df1.head()

df1.sample(25)

df1["TouchScreen"].value_counts().plot(kind="bar")#how many are ts and how many are not

sns.barplot(x=df1["TouchScreen"],y=df1["Price"])

df1["Ips"]=df1["ScreenResolution"].apply(lambda x:1 if "IPS" in x else 0)

df1.head()

df1["Ips"].value_counts().plot(kind="bar")

sns.barplot(x=df1["Ips"],y=df1["Price"])

new=df1["ScreenResolution"].str.split("x",n=1,expand=True)

df1["xres"]=new[0]
df1["yres"]=new[1]

df1.head()

#for x resolution we are using some regular expression
#these are in list we have to remove from list for this we use

df1["xres"]=df1["xres"].str.replace(","," ").str.findall(r'(\d+\.?\d+)').apply(lambda x:x[0])

df1.head()

df1.info()

#datatypes of these are bjects we are converting in to int

df1["xres"]=df1["xres"].astype("int32")

df1["yres"]=df1["yres"].astype("int32")

df1.info()

df1.corr()["Price"]

#pixel per inches as ppi increse cost increase by using xres yres and inches

#to calculate ppi we have forula root(xres,yres)//inches

df1["PPI"]=(((df1["xres"]**2) + (df1["yres"]**2))**0.5/df1["Inches"]).astype("float")

df1.corr()["Price"]

df1.drop(columns=["ScreenResolution"],inplace=True)

df1.head()

df1.columns

df1.drop(columns=["xres"],inplace=True)

df1.drop(columns=["yres","Inches"],inplace=True)

df1.head()

#different types of process like i5,i6,i7

df1["Cpu"].value_counts()

#here we extracted first three words like intel core i5,i6,i7 etc

df1["cpu name"]=df1["Cpu"].apply(lambda x:" ".join(x.split()[0:3]))

df1.head()

def fetch_processor(text):
  if text=="Intel Core i7" or text=="Intel Core i5" or text=="Intel Core i3":
    return text
  else:
    if text.split()[0]=="Intel":
      return "other intel processor"
    else:
      return "AMD PROCESSSOR"

df1["cpu brand"]=df1["cpu name"].apply(fetch_processor)

df1.sample(93)

df1["cpu brand"].value_counts().plot(kind="bar")

sns.barplot(x=df1["cpu brand"],y=df1["Price"])
plt.xticks(rotation="vertical")
plt.show()

df1.drop(columns=["Cpu","cpu name"],inplace=True)

df1.columns

df1["Ram"].value_counts().plot(kind="bar")

sns.barplot(x=df1["Ram"],y=df1["Price"])
plt.xticks(rotation="vertical")
plt.show()

#now feature engineering on memeory column

df1["Memory"].value_counts()

#these have different values this can be transformed by creating 4 new types of
#coulumns HDD,SSD,FLASH  STORAGE AND HYBRID

df1["Memory"]=df1["Memory"].astype(str).replace("\.0", "" ,regex=True)
df1["Memory"]=df1["Memory"].str.replace("GB"," ")
df1["Memory"]=df1["Memory"].str.replace("TB","000")
new=df1["Memory"].str.split("+",n=1,expand=True)

new

df1["first"]=new[0]
df1["first"]
df1["first"]=df1["first"].str.strip()

df1["first"]

df1["second"]=new[1]
df1["second"]
df1["layer1hdd"]=df1["first"].apply(lambda x: 1 if "HDD" in x else 0)
df1["layer1sdd"]=df1["first"].apply(lambda x: 1 if "SSD" in x else 0)
df1["layer1hybrid"]=df1["first"].apply(lambda x: 1 if "Hybrid" in x else 0)
df1["layer1flash_storage"]=df1["first"].apply(lambda x: 1 if"Flash Storage" in x else 0)

df1["layer1hdd"]

df1["first"]

df1["first"]=df1["first"].str.replace(r"\D"," ")

df1["second"].fillna("0",inplace=True)

df1["second"].sample(5)



df1["second"]

df1["layer2hdd"]=df1["second"].apply(lambda x: 1 if "HDD" in x else 0)
df1["layer2sdd"]=df1["second"].apply(lambda x: 1 if "SSD" in x else 0)
df1["layer2hybrid"]=df1["second"].apply(lambda x: 1 if "Hybrid" in x else 0)
df1["layer2flash_storage"]=df1["second"].apply(lambda x: 1 if"Flash Storage" in x else 0)

df1["second"]=df1["second"].str.replace(r"\D"," ")

df1["first"]=df1["first"].astype(int)

df1["second"]=df1["second"].astype(int)

df1["second"]

df1["HDD"]=(df1["first"]*df1["layer1hdd"]+df1["second"]*df1["layer2hdd"])
df1["SSD"]=(df1["first"]*df1["layer1sdd"]+df1["second"]*df1["layer2sdd"])
df1["hybrid"]=(df1["first"]*df1["layer1hybrid"]+df1["second"]*df1["layer2hybrid"])
df1["flash_storage"]=(df1["first"]*df1["layer1flash_storage"]+df1["second"]*df1["layer2flash_storage"])

df1["HDD"]

df1.drop(columns=["first","second","layer1hdd","layer2hdd","layer1sdd","layer2sdd","layer1hybrid","layer2hybrid","layer1flash_storage","layer2flash_storage"],inplace=True)

df1.sample(9)

df1.drop(columns=["Memory"],inplace=True)

df1.head()



df1.corr()["Price"]

#ssd have full corelation than hdd beacause they are numerical as hdd will more thane price will be low
#ssd is more than price will be more here flash storage and hybrid are not depended more on predicting price

df1.drop(columns=["hybrid","flash_storage"],inplace=True)

df1.sample(3)

#gpu (graphical processor unit) graphics cards are wht is in pc

df1["Gpu"].value_counts()

#here we have to many categiries in this we are extracting only brand name beacause wwe dont have huge dqta
#if that happen we may use wisely and we are not extracting more because its not showing much difference

df1["Gpu brand"]=df1["Gpu"].apply(lambda x:x.split()[0])

df1.sample(7)



df1["Gpu brand"].value_counts().plot(kind="bar")

df1=df1[df1["Gpu brand"]!="ARM"]

df1

df1["Gpu brand"].value_counts()

sns.barplot(x=df1["Gpu brand"],y=df1["Price"])
plt.xticks(rotation="vertical")
plt.show()

df1.drop(columns=["Gpu"],inplace=True)

df1.head()

df1["OpSys"].value_counts()

sns.barplot(x=df1["OpSys"],y=df1["Price"])
plt.xticks(rotation="vertical")
plt.show()

#here we are categaraized the os with different format like windows mac linx and others

#we are wring function for the categaraization

def cat_os(inp):
  if inp=="Windows 10" or inp=="Windows 7" or inp=="Windows 10 S":
    return "Windows"
  elif inp=="macOS" or inp=="Mac OS X":
    return "Mac"
  else:
    return "Others/No OS/Linux"

df1["os"]=df1["OpSys"].apply(cat_os)

df1.head()

df1.drop(columns=["OpSys"],inplace=True)

sns.barplot(x=df1["os"],y=df1["Price"])
plt.xticks(rotation="vertical")
plt.show()

sns.distplot(df1["Weight"])

sns.scatterplot(x=df1["Weight"],y=df1["Price"])

#as weight increasing price slightly increasing

df1.corr()["Price"]

df1.corr()

sns.heatmap(df1.corr())

#lighter shade haves the strong co-relation

#here our target column is skewed it will lead to improper result and lead to prblms for ml algorithms

#we can apply log transformation

sns.distplot(df1["Price"])

sns.distplot(np.log(df1["Price"]))

X=df1.drop(columns=["Price"])
y=np.log(df1["Price"])

X

y

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.15,random_state=2)

X_train.shape

X_test.shape

X_train

#here we have ccategorical data to conert it in to numerical we perform one hot encodding

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn import set_config
set_config(display="diagarm")

from sklearn.linear_model import LinearRegression,Ridge,Lasso
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor,GradientBoostingRegressor,ExtraTreesRegressor
from xgboost import XGBRFRegressor
from sklearn.metrics import r2_score,mean_absolute_error

# step1=ColumnTransformer(transformers=[
#     ("col_tnf",OneHotEncoder(sparse=False,drop="first",handle_unknown='ignore'),[0,1,7,10,11])
# ],remainder="passthrough")
# step2=LinearRegression()
# pipe=Pipeline([
#     ("step1",step1),
#     ("step2",step2)
# ])
# pipe.fit(X_train,y_train)
# y_pred=pipe.predict(X_test)
# print("r2_score",r2_score(y_test,y_pred))
# print("mean absolute error",mean_absolute_error(y_test,y_pred))

# step1=ColumnTransformer(transformers=[
#     ("col_tnf",OneHotEncoder(sparse=False,drop="first",handle_unknown='ignore'),[0,1,7,8,9,10,11])
# ],remainder="passthrough")
# step2=KNeighborsRegressor(n_neighbors=3)
# pipe=Pipeline([
#     ("step1",step1),
#     ("step2",step2)
# ])
# pipe.fit(X_train,y_train)
# y_pred=pipe.predict(X_test)
# print("r2_score",r2_score(y_test,y_pred))
# print("mean absolute error",mean_absolute_error(y_test,y_pred))

step1=ColumnTransformer(transformers=[
    ("col_tnf",OneHotEncoder(sparse=False,drop="first",handle_unknown='ignore',dtype="int32"),[0,1,7,10,11])
],remainder="passthrough")
step2=DecisionTreeRegressor(max_depth=8)
pipe=Pipeline([
    ("step1",step1),
    ("step2",step2)
])
pipe.fit(X_train,y_train)

y_pred=pipe.predict(X_test)
print("r2_score",r2_score(y_test,y_pred))
print("mean absolute error",mean_absolute_error(y_test,y_pred))

y_pred

pipe.named_steps

# from scipy.sparse import random
# step1=ColumnTransformer(transformers=[
#     ("col_tnf",OneHotEncoder(sparse=False,drop="first",handle_unknown="ignore"),[0,1,7,10,11])
# ],remainder="passthrough")
# step2=RandomForestRegressor(n_estimators=100,
#                             random_state=3,
#                             max_samples=0.5,
#                             max_features=0.75,
#                             max_depth=15)
# pipe=Pipeline([
#     ("step1",step1),
#     ("step2",step2)
# ])
# pipe.fit(X_train,y_train)
# y_pred=pipe.predict(X_test)
# print("r2_score",r2_score(y_test,y_pred))
# print("mean absolute error",mean_absolute_error(y_test,y_pred))

#website creation
#exporting the model

import pickle
pickle.dump(df1,open("df1.pkl","wb"))#opend in write binary mode
pickle.dump(pipe,open("pipw.pkl","wb"))

df1

df1.shape