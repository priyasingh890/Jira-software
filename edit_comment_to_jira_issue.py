import requests
import json
import io
url= 'https://siyas.atlassian.net//rest/api/3/issue/PRIYA-4/comment/10013'
header={
    "Accept": "application/json",
   "Content-Type": "application/json"
}
data=json.dumps({
  
  "body": {
    "type": "doc",
    "version": 1,
    "content": [
      {
        "type": "paragraph",
        "content": [
          {
            "text": "comment updated by python",
            "type": "text"
          }
        ]
      }
    ]
  }
})
respons=requests.put(url,headers=header,data=data,auth=("priyasingh21@navgurukul.org","g0j1C1iO8D9DyVcQZJBLDE87"))
print(respons.text)
