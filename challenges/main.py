def path_hits_blocked(blocked, path):
    # TODO: check whether any position in `path` also appears in `blocked`
    return any (position in blocked for position in path)