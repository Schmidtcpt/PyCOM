import xml.etree.ElementTree as ET

"""
 This poart is loading the configuration files. It includes basic functions for
 editing the files and accessing them.
"""

users = {}
permissions = {}
func_perm = {}

"""
 Load the available functions from the xml file in to a new dictionary
"""


def load_methods():
    functions_file = ET.parse('functions.xml')
    froot = functions_file.getroot()
    print "Loading methods..."
    for fchild in froot:
        print fchild.attrib['name'] + "(arg) with level " + fchild.attrib['level']
        func_perm[fchild.attrib['name']] = fchild.attrib['level']
    print "-----------------------------"

"""
 Load the users and the permissions in to a new dictionary
"""


def load_users():
    users_file = ET.parse('users.xml')
    uroot = users_file.getroot()
    print "Loading users..."
    for uchild in uroot:
        print uchild.attrib['name'] + " (" + uchild.attrib['password'] + ") and level " + uchild.attrib['level']
        users[uchild.attrib['name']] = uchild.attrib['password']
        permissions[uchild.attrib['name']] = uchild.attrib['level']
    print "-----------------------------"