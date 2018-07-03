import pandas as pd

name=["manish","aman","rakesh","ashok","dakshit"]
roll=[25,26,27,28,29]
percentage=[70,71,72,73,74]

joined=zip(name,roll,percentage)
#print joined

activity= pd.DataFrame(joined,index=range(5,10),columns=['name','roll','percentage'])
print activity
