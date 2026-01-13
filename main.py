user_table_response = sender_stand_request.get_users_table()
str_user = user_body['firstName'] + "," + user_body['phone'] + "," \
           + user_body['address'] + ",,," + user_response.json()["authToken"]
assert user_table_response.text.count(str_user) == 1

str_user = user_body['firstName'] + "," + user_body['phone'] + "," \
    + user_body['address'] + ",,," + str(user_response.json()["code"])
    print(f" {str_user}")
assert user_table_response.text.count(str_user) == 1

# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
