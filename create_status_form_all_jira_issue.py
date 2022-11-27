
import requests
import json
import io
url= 'https://siyas.atlassian.net//rest/api/3/search'
header={
    "Accept": "application/json",
   "Content-Type": "application/json"
}
query = {
  'jql': "project=PRIYA"
}
respons=requests.get(url,headers=header,auth=("priyasingh21@navgurukul.org","g0j1C1iO8D9DyVcQZJBLDE87"))
print(respons.text)
