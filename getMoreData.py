# Importing libraries
import pandas as pd
import requests
import bs4
import time

def GetAdditionalFeatures(df):
    additionalFeaturesList = []
    counter = 0
    loops = df.shape[0]
    # Loop through all rows
    for i in df['boligurl']:
        try:
            response = requests.get(i)
            html = response.text
            soup = bs4.BeautifulSoup(html, "html.parser")
            additionalFeatures = soup.find_all('span', {"class": ["info-property","info-value"]})

            # Loop through each span in the list
            count = 0
            keys = []
            values = []
            for feat in additionalFeatures:
                if count % 2: # Odd number is a value
                    values.append(feat.text.strip())
                else: # Even number is a key
                    keys.append(feat.text.strip())
                count +=1 
        except:
            keys.append('Connection timed out')
            values.append('True')
        additionalFeaturesList.append(dict(zip(keys, values)))
        time.sleep(2)
        counter += 1
        print((float(counter)/float(loops))*100.)
    df2 = df.join(pd.DataFrame(additionalFeaturesList))
    return df2
    
df_new = pd.read_csv('baseData.csv',index_col = 0 )
#df_new.head()

df_new2 = GetAdditionalFeatures(df_new)

df_new2.to_csv('extendedData.csv')