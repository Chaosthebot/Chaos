
def get_num_watchers(api, urn):
    path = "/repos/{urn}".format(urn=urn)
    data = api("get", path)
    return data["watchers_count"]

