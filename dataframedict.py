import pandas as pd 

area = pd.Series({'California': 423967, 'Texas': 695662,
                  'New York': 141297, 'Florida': 170312,
                  'Illinois': 149995})
pop = pd.Series({'California': 38332521, 'Texas': 26448193,
                 'New York': 19651127, 'Florida': 19552860,
                 'Illinois': 12882135})
data = pd.DataFrame({'area':area, 'pop':pop})
print("Data: ", data)
print("\nData area:\n",data['area'])
print(" \nData pop:\n",data['pop'])   
print("\nData area['California']:\n",data['area']['California'])    
data1= data['density'] = data['pop'] / data['area']
print("This data: \n", data1) 
print(data.values)

print(data.T)