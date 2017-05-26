def get_commit(api, urn, sha):
    path = "/repos/{urn}/commits/{sha}".format(urn=urn, sha=sha)
    commit = api("GET", path)
    return commit
