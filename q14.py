

import requests
import json
import io
url='https://siyas.atlassian.net/rest/api/3/issue/PRIYA-35/assignee'
header={
   "Accept": "application/json",
   "Content-Type": "application/json"
}
with io.open("issue_user.csv","r",encoding="utf-8")as f1:
    data=f1.read()
    f1.close()
data=data.split("\n")
for row in data:
    issue_id=row.split(",")[0]
    user_id=row.split(",")[1]
    url='https://siyas.atlassian.net/rest/api/3/issue/'+issue_id+'/assignee'
    payload=json.dumps({
            "accountId": user_id
            }
            )
    response=requests.put(url,headers=header,data=payload,auth=("priyasingh21@navgurukul.org","okE2cGJzACCpOBDXzy9y36C7"))
    print(response.text)
    print(url)