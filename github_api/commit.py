class Commit:
    def __init__(self, commit_object)
        self.url = commit_object['url']
        self.sha = commit_object['sha']
        self.html_url = commit_object['html_url']
        self.comments_url = commit_object['comments_url']
        self.commit = commit_object['commit']
        self.author = commit_object['author']
        self.commiter = commit_object['commiter']
        self.parents = commit_object['parents']

    def get_url():
        return self.url
    def get_sha():
        return self.sha
    def get_commit():
        return self.commit
    def get_author():
        return self.author
    def get_commiter():
        return self.commiter
    def get_parents():
        return self.parents

    def get_author_name():
        return get_author()['login']

    # returns the first parent, should be used carefully
    def get_parent_sha():
        return get_parents()[0]['sha']
    def get_parent_url():
        return get_parents()[0]['url']

    def get_commit_time():
        return get_author()['date']
