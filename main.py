import pandas as pd

df = pd.read_csv('grades.csv')

allAvgs=df.mean(axis=1)
maxAvg = allAvgs.max()
minAvg = allAvgs.min()

count = 0
for row in allAvgs:
    if row < 50:
        count += 1


df['[Average Score]'] = allAvgs
print(df)
print("Max Average: "+str(maxAvg)+" Min Average: "+str(minAvg))
print("num of failed students is: "+str(count))



