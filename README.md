0x00. AirBnB clone - The console

- The Project: This project (AirBnB clone - The Console), is basically a clone of the famous AirBnB website which allows home owners to put up their houses, apartments, etc for rent at a rate to prospective guest(s) who may wish to occupy them for holidays, weekend getaway, etc, for a period of time. The project involves creating a BaseModel class that defines common attributes/methods for other class, Storage Class and Command Interpreter and then running test cases.

- The Command Interpreter: This is a console code program that takes care of how a user interract with a program. In this case, it is used to interract with storage engine using JSON (and mySQL in the future).

  - To start the Command Interpreter, the "./console.py" should be used.
  - To use the command interpreter, you can create, update, destroy and even store objects to a JSON file through serialization and also show stored JSON object file through deserialization, and quit.
  - The following is an example of how to use the command interpreter.

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
