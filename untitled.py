import pandas as pd

df = pd.read_csv("weather.csv")
print(df.shape)
print(df.head(2))
print(df.tail())
print(" df[2:5]: \n",df[2:5])
print("df.columns: ",df.columns)
df.rename(columns=lambda x: x.strip(), inplace=True)  
print("df['Location']: ", df["Station.City"])
print("df['Location']: ", df["Station.City"].unique())
print("df['Location']: ", df["Station.City"].nunique())
print("df['Location']: ", df["Station.City"].value_counts())
print("df['Location']: ", df["Station.City"].value_counts().count())