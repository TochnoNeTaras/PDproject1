# місце для твого коду
import pandas as pd
df = pd.read_csv('StudentsPerformance .csv')
df.info()
def meanscore(data):
    return round((data["math score"] + data["reading score"] + data["writing score"])/3)
df['Av sc'] =df.apply(meanscore, axis=1 )
df.to_csv('cleaned.csv',index = False)
