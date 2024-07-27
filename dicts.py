from pprint import pprint

d = {
    "key": "value",
     "another": "another value"
     }
user1 = {
    "name": "Petr",
    "age": 18,
    "id": 25
}
user2 = {
    "name": "Vasya",
    "age": 33,
    "id": 42
}

users = {
    25: user1,
    42: user2
}

users[42] = {
    "name": "Kirill",
    "age": 77
}
print(users[42])
print("*************************")
print(user1["name"])
print("*************************")
print(user2["name"])
print("*************************")

print(users[25])
print("*************************")
print(users.get(55, {"name": "default users"}))
print("*************************")

pprint(list(users.items()))