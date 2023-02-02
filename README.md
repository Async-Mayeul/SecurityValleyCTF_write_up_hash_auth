# SecurityValleyCTF_write_up_hash_auth
The write-up hash_auth of the CTF Security Valley 

## Introduction

In this challenge we have a piece of code in python. We are asked to test the the strength of the authentication function.

```python
from hashlib import sha256
import sys

def validate_password(password):
    # be creative. it has something to do with SecurityValley ;-)
    if sha256(password.encode("utf-8")).hexdigest() == "f51f333ed26c41bedd99e1e483c0a15d2caeed7dc5a9ae02159f196799a74893":
        return True 

    return False

def print_banner(payload):
    print("that was great !!!")
    print("run the following command to get the flag.")
    print("curl -X POST http://ctf.securityvalley.org:7777/api/v1/validate -H 'Content-Type: application/json' -d '{\"pass\": \""+payload+"\"}'")

if __name__ == "__main__":
    print("let's do more python ;-)")

    password = input("please enter password: ")
    if validate_password(password):
        print_banner(password)
        sys.exit()
    
    print("wrong!") 
```

We can see that the cryptographic algorithms used is SHA256 and that the password encrypted have a relation with SecurityValley.

## Script

I had write a little script to crack the password by using the hint `SecurityValley`. This script made a random string that replace random character in `SecurityValley` by special characters, lower-case and upper-case letter.
For sure they are other methods to valid this challenge, but I wanted to write a little script in Python :) .

```python
#!/usr/bin/python3

from hashlib import sha256
import random

characters = "azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN1234567890@!:._?$&#"
hint = "SecurityValley"
flag = False
index = [i for i, y in enumerate(hint) if not hint.isspace()]

for i in range(0, 1500):
    if (flag):
        break
    listHint = list(hint)
    sample = random.sample(index, 1)
    for y in sample:
        listHint[y] = random.choice(characters)
    print("".join(listHint))
    if sha256(("".join(listHint)).encode("utf-8")).hexdigest() == "f51f333ed26c41bedd99e1e483c0a15d2caeed7dc5a9ae02159f196799a74893":
        print("Find !!! : "+"".join(listHint))
        flag=True
```
```
$ python3 crack.py
SecurTtyValley
Secu&ityValley
SecurityHalley
SeculityValley
SDcurityValley
LecurityValley
Security.alley
SecuoityValley
Securitymalley
SecurityVTlley
EecurityValley
SecurityValkey
SecurityVwlley
SecurizyValley
Securit1Valley
SRcurityValley
Secu.ityValley
Secur.tyValley
S&curityValley
SecurStyValley
SqcurityValley
PecurityValley
SecurityV$lley
SecurityValWey
SecurityV#lley
Secur1tyValley
Find !!! : Secur1tyValley
$
```
This script is not optimal, if the password isn't directly found, run the script 2,3 times.

## Get the flag !!
```
$ python3 hash_auth.py
let's do more python ;-)
please enter password: Secur1tyValley
that was great !!!
run the following command to get the flag.
curl -X POST http://ctf.securityvalley.org:7777/api/v1/validate -H 'Content-Type: application/json' -d '{"pass": "Secur1tyValley"}'
```
Execute the curl command
```
$ curl -X POST http://ctf.securityvalley.org:7777/api/v1/validate -H 'Content-Type: application/json' -d '{"pass": "Secur1tyValley"}'
{"Value":"SecVal{To_51MPl3_foR_You}"}

```
Now we have the flag to validate the challenge : `SecVal{To_51MPl3_foR_You}`