import json
data = '''{
    "name" : "Cansel",
    "phone" : {
        "type" : "intl",
        "number" : "+90 506 940 8304"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

info = json.loads(data)
print('Name:', info["name"])
print('Attribute:', info["email"]["hide"])