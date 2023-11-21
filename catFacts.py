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
    
    print (response)
    #print (response['status'])
    #print (response['text'])
    return list_catFacts

CAT_FACTS = GetCatFacts(2)

print (CAT_FACTS)