






















import requests
import json
import io
url= 'https://siyas.atlassian.net//rest/api/3/issue/PRIYA-1/comment'
header={
    "Accept": "application/json",
   "Content-Type": "application/json"
}
respons=requests.get(url,headers=header,auth=("priyasingh21@navgurukul.org","g0j1C1iO8D9DyVcQZJBLDE87"))
data=respons.json()

with io.open("comments.CSV","w",encoding="utf-8")as f1:
    for i in data["comments"]:
        f1.write(i['id']+","+i['body']['content'][0]['content'][0]['text']+"\n")
    f1.close()