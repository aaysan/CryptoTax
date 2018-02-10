# Parsing the json data

import json
import pprint
              

file = open("json.txt","r") #get the json
texts = file.read() #read it
data = json.loads(texts) #parse it

# OUTPUTS:
# Description of Property
# Date Acquired (Month, Day, Year)
# Date Sold or disposed (Month, Day, Year)
# Proceeds (sales price)
# Cost


# for elem in data['data']:
#     pprint.pprint(elem["amount"]["amount"])
#
#     print('-----------------')

for transactions in data['data']:
    description = transactions["details"]["title"]
    date_acquired = None
    date_sold = None



    if "buy" in transactions:
        date_acquired = transactions["updated_at"]
    else:
        date_sold = transactions["updated_at"]

    proceeds = transactions["native_amount"]["amount"]
    currency = transactions["native_amount"]["currency"]

    