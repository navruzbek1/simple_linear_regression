# -*- coding: utf-8 -*-
"""Untitled24.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1E3RRKJ5n3Wd4xJNB5nh1p5wnJYKYF1uL

# Simple linear regression - kichik loyiha

---
*qanday ishlashini ko'ramiz*

```



                                                                                                                created by Navruzbek_Abduganiyev
"""

import pandas as pd
df=pd.read_csv("/content/housing_LR.csv",index_col=0)
df.head()

"""**Ayrim ustunlar ta'rifi**


*   level - qavati
*   max_level - uy necha qavat ekanligi 


"""

# SIMPLE LINEAR REGRESSION da bitta ustundan foydalangan holda model yaratamiz
df.info()

df.describe()

df["district"].value_counts()

#chilonzorda uylar ko'p ekan,biz aynan  shu hudud uchun model yaratamiz
df=df[df['district']=="Чиланзарский"]

# SLR da aytdikki bitta ustundan foydalanamiz
df.corrwith(df["price"]).sort_values(ascending=False)

#demak kattagina korrelyatsiya size ustunimizda ekan
X = df["size"]
Y = df['price']

# Commented out IPython magic to ensure Python compatibility.
#bular o'rtasidagi chiziqli bo'g'liqlikni tekshirib ko'ramiz
import numpy as np
import matplotlib.pyplot as plt
import  seaborn as sns
# %matplotlib inline

plt.figure(figsize=(8,6))
sns.scatterplot(data = df,x=X,y=Y)
plt.show()

plt.figure(figsize=(8,6))
sns.regplot(data=df,x=X,y=Y,line_kws={"color":"r"})
plt.show()  # bizda yaxshigina chiziqli bog'liqlik bor,ayrim noodatiy qiynatlarni aytmaganda

# chiziqli bo'gliqlikda gradient tushishini aniqlashimiz kerak.Buning uchun SLR ning maxsus 
#koeffitsient formulalari bor

theta1 = sum((x1-Xmean)*(y1-Ymean))/sum((x1-Xmean)**2)

theta0 = Ymean - theta1*Xmean

Xmean = np.mean(X.to_numpy())
Ymean = np.mean(Y.to_numpy())

theta1 = sum((X-Xmean)*(Y-Ymean))/sum((X-Xmean)**2)
theta0=Ymean - theta1*Xmean   #koeffitsiyentlarimmiz tayyor

# y = theta0 + theta1*X   ----> ushbu formula orqali biz qiymatlarni olishumiz mumkin.Aynan SLR ham shu  formul asosida ishlaydi
#bog'liqlik grafigunu chizib ko'ramiz
plt.figure(figsize=(8,6))
sns.scatterplot(data=df,x=X,y=Y)
plt.plot(np.asanyarray(X),theta0 + theta1*X,c="r")
plt.show()  #bundan oldin biz bog'liqlik chizig'ini bitta funksiya orqali chizgan edik,hozir uzimiz keltirib chizdik

#Model yaratamiz
from sklearn.model_selection import train_test_split
train_set, test_set = train_test_split(df,random_state=12,train_size=0.8)

X_train = np.asanyarray(train_set[["size"]])
Y_train = np.asanyarray(train_set[['price']])

from sklearn.linear_model import LinearRegression
LR_model = LinearRegression()

LR_model.fit(X_train,Y_train)

X_test = np.asanyarray(test_set[["size"]])
Y_test = np.asanyarray(test_set[["price"]])

predict_test = LR_model.predict(X_test)

#modelni baholaymiz
from sklearn.metrics import mean_squared_error,mean_absolute_error
RMSE = np.sqrt(mean_squared_error(predict_test,Y_test))
MAE = mean_absolute_error(predict_test,Y_test)
print(f'RMSE = {RMSE}')
print(f"MAE = {MAE}")

