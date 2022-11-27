import requests
import json
import io
url='https://siyas.atlassian.net//rest/api/2/search'
header={
      "Accept": "application/json",
   "Content-Type": "application/json"
}
query={
    'jql':"project=PRIYA"
}
response=requests.get(url,headers=header,params=query,auth=("priyasingh21@navgurukul.org","g0j1C1iO8D9DyVcQZJBLDE87"))
data=response.json()
issues=data["issues"]
for issue in issues:
    print(issue["key"])
