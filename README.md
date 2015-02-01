# PyCOM Bootstrap
PyCOM is a bootstrap core written in Python 2.7 which helps yopu bridge the gap between an http-controlled server and your Arduino.


## What is it?
PyCOM combines the flexibility of the Python programming language and the endless posibilities of a REST webservice.
You can controll almost everything and do anything.  It uses the `basehttp` module to handle post requests from any remote location.
 

## Installation
Download the files from Github and run main.py
By default it runs on localhost:8000


## Features

* Pre-build http server
* User management
* User & function permission level
* Enable/Disable functions on the fly
* Serial communication protocol

# Guide

### Add new functions

Start by editing `functions.py` and add a new method (always include `arg` and an argument even is you dont use it)

*Example:*

```
def play_sound(arg):
    print "Hello world"
    return True
```

Then register the function on `functions.xml` 

`<function name="play_sound" level="1"> </function>`

* name: the name of the method
* level: the required permission level


### Add new user

Start by editing the `users.xml` and add a new line as follows:

`<user name="john" password="12345" level="3"> </user>`

* name: the desired name for the 
* password: is equired for user authendication
* level: the permission level for the user

### Using the serialcom module

The serialcom module treats the serial port as it should be treated in order to work properly

**Included functions:**

`send(port, baud, command)`
Opens a connection with the arduino on the specified port and sends a string

`readline(port, baud)`
When called it can read whatever the board sends back (`Serial.println()`) It can be looped with a `while True`

`send_request(port, baud, command)`
In comparison with `send()` and `readline()` this method sends something on the arduino but waits for a reponse and returns the results

*Example*

```
def comtest(arg):
    # Import the module
    import serialcom
    # Import the service (see below for instructions)
    import service
    # Send the request
    out = serialcom.send_request('COM3', 9600, arg)
    # Put the striped output inside the dictionary
    service.returned[arg] = out.strip()
    # Check and return whatever you want
    if out.strip() == "Correct":
        return True
    else:
        return False
```

More features to come :D
