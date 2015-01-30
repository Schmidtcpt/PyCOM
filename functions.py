def users_reload(arg):
    import loader
    loader.load_users()
    return True

def methods_reload(arg):
    import loader
    loader.load_methods()
    return True