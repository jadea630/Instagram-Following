import json

"""
DOWNLOAD DATA HERE (MAKE SURE TO SELECT JSON FORMAT):
https://accountscenter.instagram.com/info_and_permissions/
"""

followers_path = r'C:\Users\CHANGE_ME\Desktop\followers_1.json'
following_path = r'C:\Users\CHANGE_ME\Desktop\following.json'

with open(followers_path) as f1:
    followers = json.load(f1)

with open(following_path) as f2:
    following = json.load(f2)


following_list = []
for indx in range(0, len(following['relationships_following'])):
    user_info = following['relationships_following'][indx]['string_list_data']
    for user in user_info:
        following_list.append(user['value'])


followers_list = []
for indx in range(0, len(followers)):
    user_info = followers[indx]['string_list_data']
    for user in user_info:
        followers_list.append(user['value'])


no_follow_back = []
for user in following_list:
    if user not in followers_list:
        no_follow_back.append(user)
no_follow_back.sort()

print("Followers:", len(followers_list))
print("Following:", len(following_list))
print(no_follow_back)


