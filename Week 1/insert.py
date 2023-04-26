# importing required library 
import pandas as pd
import s3fs

# reading the csv file form s3 bucket.
df=pd.read_csv('s3://data-aiot-interns/Week-1/Insert-Table.csv',encoding = "ISO-8859-1")
print("Initial Data :")
print(df.head(10))

# Added first name and alst name into a Full name
df["Full_Name"]=df['firstname']+" "+df['lastname']

f=df.pop('Full_Name')
df.insert(3,"Full_Name",f)

#dropping the first and last name columns
df.drop(columns=['firstname','lastname'],inplace=True)

# Chnaged the date format
a=df['Date of Exam'] = pd.to_datetime(df['Date of Exam']).dt.date

#Convert Percentage column from float to decimal and approximate to 2 significant figures after the decimal point.
df['Percentage']=round(df['Percentage'],2)
print('\nUpdated CSV file:')
print(df.head())

# saving the updated csv file
df.to_csv("/var/lib/mysql-files/Insert-TableNew.csv",index=False)