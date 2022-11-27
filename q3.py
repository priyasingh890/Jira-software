import requests
import json
import io
url="https://siyas.atlassian.net//rest/api/2/user"
header={
    "Accept":"application/json",
    "content-Type":"application/json"
}
with io.open("userlist.csv","r",encoding="utf-8")as f1:
    user_data=f1.read()
    f1.close()
user_data=user_data.split("\n")[1:] 
for user in user_data:
    displayName=user.split(",")[0]
    # pwd=user.split(",")[1]
    email=user.split(",")[2]
    # name=user.split(",")[2]
    detail=json.dumps({
            "emailAddress": email,
            "displayName":  displayName,
            # "name": name,
            }
            )
    response=requests.post(url,headers=header,data=detail,auth=("priyasingh21@navgurukul.org","e34pYpn3tZu57CYobTGgFAE5"))
    print(response.text)


# import requests
# import json
# import io
# url="'https://kanwar.atlassian.net//rest/api/3/users"
# heaader={
#     "Accept":"application/json",
#     "content-Type":"application/json"
# }
# with io.open("userlist.csv","r",encoding="utf-8")as f1:

#     user_data=f1.read()
#     f1.close()
# user_data=user_data.split("\n")[1:] 
# for user in user_data:
#     displayName=user.split(",")[0]
#     pwd=user.split(",")[1]
#     email=user.split(",")[2]
#     name=user.split(",")[2]
# print(user_data) 
# payload=json.dumps(
#     {
#         "password":"pwd",
#         "emailAddress":"email",
#         "displayName":"displayame",
#         "name":"name"
        
#     }
# )
# response=requests.post(url,heaader=heaader,data=payload,auth=("teenakanawar21@navgurukul.org","GlIPyLzIDtgQhar9GUaX9278"))
# print(response.text)
