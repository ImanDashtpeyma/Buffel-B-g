import lib as person
import pandas as pd
import numpy as np
from datetime import datetime, timedelta


# ─── Read Data From The Old System Api And Converts It To A Data Frame ──────────

df = pd.read_table('https://builds.lundalogik.com/api/v1/builds/freebusy/versions/1.0.0/file', sep=';', names=[
    "ID", "starting", "ending", "Description"])


# ─── Fixing Irregularities And Making  a Pure Data Frame According Name ──────────

print("Please wait for the initial processing of data .......")
# replace NULL value
df = df.replace(np.nan, 'Name')
# create data frame By name
grouped = df.groupby(df.ending)
df_Name = grouped.get_group('Name')
# replace Null value with known value
df['ending'].replace('Name', np.nan, inplace=True)
# remove NuLL value
df.dropna(subset=['ending'], inplace=True)

# remove Null column
df_Name = df_Name.drop(columns=['ending'], axis=1)


# replace  ID in main data frame with Name
for ind in df_Name.index:
    df = df.replace(to_replace=df_Name['ID']
                    [ind], value=df_Name['starting'][ind])

# convert  all string date to  date object
df['starting'] = pd.to_datetime(df.starting)
df['ending'] = pd.to_datetime(df.ending)


# create  a new header for main data frame add  'busy' column
df.columns = ['name', 'starting', 'ending', 'date']
df.insert(3, 'busy', '')

# remove  wasted column value , and replace it with useful data  like Date
for ind in df.index:
    df = df.replace(to_replace=df['date']
                    [ind], value=df['starting'][ind].strftime("%Y-%m-%d"))


# ─── Starts Data Mining In The Main Data Frame ──────────────────────────────────

# Desired meeting length (minutes)
# I can add input validation in future
meeting_time_by_minutes = int(
    input(" Enter Your Meeting Duration (Number) : "))
# Meeting Date and time start
input_date = input(
    " Enter Your desired Meeting date in this format ( 2015-01-01 07:00:00)  : ")
meeting_date_start = datetime.strptime(input_date, '%Y-%m-%d %I:%M:%S')
# Meeting Date and time end
meeting_date_end = meeting_date_start + \
    timedelta(minutes=meeting_time_by_minutes)


# Creating a new Dataframe based on the desired meeting date to reduce complexity
grouped = df.groupby(df.date)
df = grouped.get_group(meeting_date_start.strftime("%Y-%m-%d"))
# sort Data by Date
df = df.sort_values(by="date")


# finding busy or free  employees at the start meeting time   (True means busy)
# is _busy() is function in lib.py
for ind in df.index:
    df['busy'][ind] = person.is_busy(
        meeting_date_start, df['starting'][ind], df['ending'][ind])

# create data frame base on free employees
grouped_free_start = df.groupby(df.busy)
df_free_start = grouped_free_start.get_group(False)

# finding busy or free  employees at the end  meeting time   (True means busy)
for ind in df_free_start.index:
    df_free_start['busy'][ind] = person.is_busy(
        meeting_date_end, df_free_start['starting'][ind], df_free_start['ending'][ind])

# create data frame base on free employees during meeting time
grouped_free_end = df_free_start.groupby(df_free_start.busy)
df_free_end = grouped_free_end.get_group(False)


# result Output in console
print(df_free_end)
# result Output in CSV format
df_free_end.to_csv('result.csv')
# result Output in Excel format  For someone who has run away from this old system :)
read_file = pd.read_csv(r'result.csv')
read_file.to_excel(r'result.xlsx', index=None, header=True)


print(" You can choose your non-busy employees from Result.csv or Result.xlsx ( Excel format) and see your next employees meeting date. Have a Nice meeting !!  Thanks : Iman Dashtpeyma")
