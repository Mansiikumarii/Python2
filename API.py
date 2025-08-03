from randomuser import RandomUser
import pandas as pd
r = RandomUser()
some_list = r.generate_users(10)
print(some_list)  # Print the list of generated users

for user in some_list:
    print(user.get_full_name()," ", user.get_email())  # Print each user's full name and email
    print(user.get_picture())  # Print each user's picture URL

def get_users():
    users = []
    for user in RandomUser.generate_users(10):
        users.append({
            'name': user.get_full_name(),
             "Gender": user.get_gender(),
             "City": user.get_city(),
             "State": user.get_state(),
             "Email": user.get_email(),
             "DOB": user.get_dob(),
                "Picture": user.get_picture()
        })
get_users()
df1 = pd.DataFrame(get_users())