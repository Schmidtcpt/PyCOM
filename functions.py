def users_reload(arg):
    import loader
    loader.load_users()
    return True


def methods_reload(arg):
    import loader
    loader.load_methods()
    return True


def Led(arg):
    import serialcom
    serialcom.send('COM3', 9600, arg)
    return True