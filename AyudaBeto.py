import json

users = None
most_befriend = None
max_number_of_friends = 0
with open("data/users_10k.json", "r") as file:
    users = json.loads(file.read())
    # print(json.dumps(users))

for u in users:
    # a. most befriend person process
    if len(u['friends']) > max_number_of_friends:
        most_befriend = u



# Printing results
print("most befriended person: ", most_befriend)
