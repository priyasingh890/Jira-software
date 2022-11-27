import requests
import json
import io
url= 'https://siyas.atlassian.net//rest/api/3/issue/PRIYA-4/comment/10012'
header={
      "Accept": "application/json",
   "Content-Type": "application/json"

}
response=requests.delete(url,headers=header,auth=("priyasingh21@navgurukul.org","g0j1C1iO8D9DyVcQZJBLDE87"))
print(response.text)
