import requests
import json
import io
url='https://siyas.atlassian.net/rest/api/3/issue/PRIYA-37/assignee'
header={
   "Accept": "application/json",
   "Content-Type": "application/json"
}
payload=json.dumps({
    "accountId": "637db9a9489de2f7f4634358"
}
)
response=requests.put(url,headers=header,data=payload,auth=("priyasingh21@navgurukul.org","okE2cGJzACCpOBDXzy9y36C7"))
print(response.text)







