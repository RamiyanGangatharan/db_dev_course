# do not need pandas
import pandas as pd
import requests 
import json



# Function for this
def GetCatFacts(_amount):
    # Connection String SETUP
    # Check Documentation
    API_connect = f'https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount={_amount}'

    # CALL the API
    response = requests.get(API_connect)

    # PARSE the results
    response = json.loads(response.content)

    list_catFacts = []
    for fact in response:
        list_catFacts.append(fact['text'])
    
    #print (response)
    #print (response['status'])
    #print (response['text'])
    df = pd.DataFrame(list_catFacts, columns=['text'])
    df['newColumn'] = "cat fact"
    # to get a specific value
    #one_val = df.iloc[2,0]
    # to get a specific row, colon means everything in that row
    #one_row = df.iloc[0, :]
    #return one_row

    return df

CAT_FACTS = GetCatFacts(10)

print (CAT_FACTS)