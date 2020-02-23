from flask import Flask

server = Flask(__name__)
@server.route('/')                                                         #@ = a docorator; helps to ensure a particular conditions that needs to be met before a function is executed
def home():
    return "My application is running succcessfully"
    
    
if __name__ == "__main__":
    server.run()                          #A constructor is a special method that is used to initialize a newly created object and is called just after the memory is allocated for the object. ... If no user-defined constructor is provided for a class, compiler initializes member variables to its default values.
                                                                               #('/') directory