# import requests
# import json
# import io
# url='https://siyas.atlassian.net/rest/api/3/issue/PRIYA-35/assignee'
# header={
#    "Accept": "application/json",
#    "Content-Type": "application/json"
# }
# payload=json.dumps({
#         "accountId": user_id
#         }
#         )
# response=requests.put(url,headers=header,data=payload,auth=("priyasingh21@navgurukul.org","okE2cGJzACCpOBDXzy9y36C7"))
# print(response.text)
# print(url)














# import requests
# import json
# import io
# url='https://siyas.atlassian.net//rest/api/3/issue/PRIYA-38/transitions'
# header={
#    "Accept": "application/json",
#    "Content-Type": "application/json"
# }

# payload=json.dumps({
#     "transition":{
#         "id":"13"
#     }
# }
#     )
# response=requests.post(url,headers=header,data=payload,auth=("priyasingh21@navgurukul.org","okE2cGJzACCpOBDXzy9y36C7"))
# print(response.text)



import requests
import json
import io
url='https://siyas.atlassian.net/rest/api/3/issue/PRIYA-39/transitions'
header={
   "Accept": "application/json",
   "Content-Type": "application/json"
}

payload=json.dumps(
   {
    
    "transition": {
        "id": "21"
    }
}
        
)
response=requests.post(url,headers=header,data=payload,auth=("priyasingh21@navgurukul.org","okE2cGJzACCpOBDXzy9y36C7"))
print(response.text)


