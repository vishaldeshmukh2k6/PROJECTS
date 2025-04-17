# Welcome to Github API.
# Input: Enter your username: pratikdeshmukh2004
# Hello, Pratik Deshmukh
# What do you want from me?
# 1. Account Detail
# 2. Repo list
# 3. Followers
# 4. Follwings

# 1 {username: Username, Email: email}







import requests

print("Welcome to Github API") 

User_name = str(input("Enter your user name :- "))

api = "https://api.github.com/users/" + User_name


res = requests.get(api).json()

print(f"Hello, {res.get("name")}")


What_you_get = int(input("What do you want from me?\n Enter 1 is Account Detail\n Enter 2 is All Repo name  \n Enter 3 is All Followers Name  \n Enter 4 is All Follwings Name  \n Enter any one :- "))

if What_you_get == 1:
    print(f"Name :- {res.get("name")}")   # Name
    print(f"company :- {res.get("company")}")     # company name
    print(f"Bio :- {res.get("bio")}")  # bio
    print(f"Location :- {res.get("location")}")   # location


if What_you_get == 2:
    api2 = api + "/repos"
    new1 = requests.get(api2,  params = {"page" : 1, "per_page": 100}).json()

    i = 1

    for repos in new1:
        print(f"{i} Repositories :- {repos.get("name")}")
        i+= 1

if What_you_get == 3:
    api1 = api + "/followers"
    new2 = requests.get(api1, params = {"page" : 1, "per_page": 100}).json()
    
    i = 1
    for user in new2:
        print(f"{i} Followers :- {user.get("login")}")
        i += 1


if What_you_get == 4:

    api3 = api + "/following"
    new3 = requests.get(api3, params = {"page" : 1, "per_page": 100}).json()

    i = 1

    for Foll in new3:
        print(f"{i} following :- {Foll.get("login")}")
        i += 1


