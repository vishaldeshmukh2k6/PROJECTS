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


What_you_get = int(input("What do you want from me?\n 1 is Account Detail\n 2 is Repo list \n 3 is Followers \n 4 is Follwings \n Enter any one :- "))

if What_you_get == 1:
    print(f"Name :- {res.get("name")}")   # Name
    print(f"company :- {res.get("company")}")     # company name
    print(f"Bio :- {res.get("bio")}")  # bio
    print(f"Location :- {res.get("location")}")   # location

if What_you_get == 2:
    print(f"Repo list :- {res.get("public_repos")}")

if What_you_get == 3:
    print(f"Followers :- {res.get("followers")}")  # Followers

if What_you_get == 4:
    print(f"Following :- {res.get("following")}")  # Following