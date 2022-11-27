import requests
import json
import io
header={
   "Accept": "application/json",
   "Content-Type": "application/json"
}
with io.open("issuedelete.csv","r",encoding="utf-8")as f1:
    data=f1.read()
data=data.split("\n")
for id in data:
    url='https://siyas.atlassian.net/rest/api/2/issue/'+id
response=requests.delete(url,headers=header,auth=("priyasingh21@navgurukul.org","g0j1C1iO8D9DyVcQZJBLDE87"))
# print(response.text)