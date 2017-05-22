
def get_user(api, user):
    path = "/users/{user}".format(user=user)
    data = api("get", path)
    return data

