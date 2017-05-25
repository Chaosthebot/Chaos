
def get_num_watchers(api, urn):
    """ returns the number of watchers for a repo """
    path = "/repos/{urn}".format(urn=urn)
    data = api("get", path)
    # this is the field for watchers.  do not be tricked by "watchers_count"
    # which always matches "stargazers_count"
    return data["subscribers_count"]

# returns the latest commit to master if one occurred within the last fallback window
def get_latest_commit(api, urn):
    path = "/repos/{urn}/commits".format(urn=urn)
    data = api("get", path)
    if(len(data) > 0)
        return data[0]
    else
        return None

