"""
 New methods can be placed here. Simply define a new method and always add the arg even
 if you don't use it. You can't place a second argument inside those methods but you can
 always use a split(() method in order to brake the main arg in to pieces.
"""


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


def lsus(arg):
    import service
    import xml.etree.ElementTree as ET
    users_file = ET.parse('users.xml')
    uroot = users_file.getroot()
    for uchild in uroot:
        service.returned[uchild.attrib['name']] = uchild.attrib['level']


def lsfn(arg):
    import service
    import xml.etree.ElementTree as ET
    functions_file = ET.parse('functions.xml')
    froot = functions_file.getroot()
    for fchild in froot:
        service.returned[fchild.attrib['name']] = fchild.attrib['level']