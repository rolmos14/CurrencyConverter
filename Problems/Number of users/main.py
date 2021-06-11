with open('users.json') as users_file:
    users_dict = json.load(users_file)

print(len(users_dict['users']))
