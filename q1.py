import requests
import json
url= 'https://siyas.atlassian.net//rest/api/2/issue'
header={"Accept": "application/json",
        "Content-Type": "application/json"
}
details=json.dumps({
    "fields": {
       "project":
       {
          "key": "PRIYA"
       },
       "summary": "create a text",
       "description": "Creating a text2",
       "issuetype": {
          "name": "Task"
       },       
   }
})
inform=requests.post(url,headers=header,data=details,auth=("priyasingh21@navgurukul.org","WmcntrNwlrglmfnghYzHF154"))
print(inform.text)