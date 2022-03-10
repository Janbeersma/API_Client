import requests
from JsonToObject import JsonToObject

def GetFromAPI():
    response = requests.get("placeholder")
    print("Statuscode van aanvraag: ", response.status_code)
    users = response.json()
    #print(users)
    for x in users:
        newUserObject = jsonToObject.DeserializeUserFromJson(x)
        # print(type(newUserDict))
        # newUserObject = jsonToObject.DeserializeUserFromJson(newUserDict)
        # print("na deserialisatie van JSON")
        # print(newUserObject.fullname, newUserObject.username)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    jsonToObject = JsonToObject()
    GetFromAPI()
