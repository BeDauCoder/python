import pandas as pd
df = pd.read_csv('euro2012.csv')

# print(df.shape())

print("Values Goals")
print(df['Goals'])
print("")
print("Count Team: ",df['Team'].count())
print("")


discipline = df[['Team','Red Cards','Yellow Cards']]

print(discipline)

sort = discipline.sort_values(['Red Cards','Yellow Cards'],ascending=[False,False])
print(sort)

print(discipline['Yellow Cards'].mean())

discipline_goals = df[['Goals']]
print(discipline_goals[discipline_goals['Goals']>6])
print("")

discipline_Teams_startWith = df[df['Team'].str.startswith('G')]
print(discipline_Teams_startWith)

col7_start= df.iloc[:,0:7]
print(col7_start)
print("")

col3_sub3 = df.iloc[:,:-3]
print(col3_sub3)


c11 = df[['Team','Shooting Accuracy'].isin(['Russia','Italy','England'])]
print(c11)