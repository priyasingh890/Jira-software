import requests
import json
url= 'https://siyas.atlassian.net/rest/api/2/users/search'
header={"Accept": "application/json",
        "Content-Type": "application/json"
}

inform=requests.get(url,headers=header,auth=("priyasingh21@navgurukul.org","t13ccvD2dqQclhr8yRjHE96A"))
p=inform.json()
for i in p:
    print(i["displayName"])
