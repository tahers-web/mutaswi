import sklearn
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#preprocessing

file="BHRRC.csv"
df=pd.read_csv(file)

#df=df.drop(['URL'],axis=1)
df=df.drop(['Regions'],axis=1)
df=df.drop(['Gender'],axis=1)
df=df.drop(['URL'],axis=1)

companies=df["Companies"].unique()

le=LabelEncoder()

df['Authors']=le.fit_transform(df['Authors'])
df['Companies']=le.fit_transform(df['Companies'])
df['Issues']=le.fit_transform(df['Issues'])
df['Authors']=le.fit_transform(df['Authors'])
df=df.fillna(0)

issue_count=(df.groupby('Companies')["Issues"].count())
df_issues=pd.DataFrame()

df_issues['Companies']=companies
df_issues['Count']=issue_count
df_issues.fillna(0)
df_non_viable=pd.DataFrame()

df_non_viable=df_issues[df_issues['Count'] >1]
df_viable=df_issues[df_issues['Count'] <=1]

non_viable_count=df_non_viable['Count'].values
nonviable_companies=df_non_viable['Companies'].values

print(df_viable)

df_viable.to_csv("viable.csv",index=False)
df_non_viable.to_csv("nonviable.csv",index=False)
issue_count=issue_count.astype(int)
companies=companies.astype(str)
fig=plt.figure()
ax=fig.add_axes([0,0,1,1])
ax.set_xlabel('Companies')
ax.set_ylabel('Number of issues')
ax.bar(nonviable_companies,non_viable_count)
plt.show()

