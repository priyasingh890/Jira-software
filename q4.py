import requests
import json
import io
url = "https://siyas.atlassian.net/rest/api/2/issue/PRIYA-1/attachments"
header={
    "X-Atlassian-Token": "no-check"
}
files={
    "file":("userlist.csv",open("userlist.csv","rb"))
}
response=requests.post(url,headers=header,files=files,auth=("priyasingh21@navgurukul.org","e34pYpn3tZu57CYobTGgFAE5"))
print(response.text)