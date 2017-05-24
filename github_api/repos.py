
def get_num_watchers(api, urn):
    path = "/repos/{urn}".format(urn=urn)
    data = api("get", path)
    return data["watchers_count"]

# returns the latest commit to master if one occurred within the last fallback window
def get_latest_commit(api, urn):
    path = "/repos/{urn}/commits".format(urn=urn)
    data = api("get", path)
    if(len(data) > 0)
      # return previous commit sha if it exists
      if(len(data) >= 1)
        data[0]['last_commit_sha'] =
      else
        return data[0]
    else
        return None

