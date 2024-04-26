import requests
import datetime

USER_ID = input("ds_user_id : ")
SESSION = input("sessionid : ")

url = f"https://www.instagram.com/api/v1/friendships/{USER_ID}/followers/"

user_name_list = []

headers = {
    "sec-fetch-site": "same-origin",
    "x-ig-app-id": "936619743392459"
}

params = {
    "count": 20,
    "search_surface": "follow_list_page",
}

cookies = {"sessionid": SESSION}

while True : 
    # Request
    response = requests.get(url, headers=headers, params=params, cookies=cookies)

    # Response
    data = response.json()

    # join list
    user_name = [user['username'] for user in data['users']]
    user_name_list.extend(user_name)
    print(f"총 {len(user_name_list)} 명 찾았습니다.")

    # continue or break
    try :
        # update next key
        next_max_id = data['next_max_id']
        params["max_id"] = next_max_id
    except : 
        break

# saved file
now = datetime.datetime.now()
current_time = now.strftime("%Y-%m-%d %H:%M:%S")
with open(f"{current_time}.txt", "w") as file:
    file.write("\n".join(user_name_list))