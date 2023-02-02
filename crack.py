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