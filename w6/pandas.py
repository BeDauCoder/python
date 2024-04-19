import pandas as pd

a = {'car':["BMW","Tesla","MC"],
     'count':[2,6,5]}
ab = pd.DataFrame(a)

print(ab)

c =["BMW","Tesla","MC"]
a_id = pd.Series(c,index=["x","y","z"])
print("")
print(a_id)

d = {"car1":12,"car2":13,"car3":14}

cd = pd.Series(d)
print("")
print(cd)