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
    issue_key=issue["key"]
    url1 ="https://siyas.atlassian.net/rest/api/3/issue/"+issue_key
    response=requests.get(url1,headers=header,auth=("priyasingh21@navgurukul.org","g0j1C1iO8D9DyVcQZJBLDE87"))
    data=response.json()
    print(f'issue id is {issue_key} and status is {data["fields"]["status"]["name"]}')








    
    # url1="https://siyas.atlassian.net//rest/api/3/issue"+issue_key
    # response=requests.get(url1,headers=header,auth=("priyasingh21@navgurukul.org","g0j1C1iO8D9DyVcQZJBLDE87"))
    # print(response.json())
    # print(response.json())
    # print(response.json())
    # data=response.json()
    # # print(data)
    # print(data.keys())
    # print(data['fields'])