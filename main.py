# -*- coding: utf8 -*-
import sys

def getInput(message):
    if sys.version_info[0] == 2:
        return raw_input(message)
    else:
        return input(message)


# ============================================================================
import string

repassword = []
characterCount = 0
inputLoopToggle = True

while inputLoopToggle:
    password = getInput("Geben Sie ihr Passwort ein: ")
    if password.isalnum():
        inputLoopToggle = False
    else:
        print("Geben Sie bitte nur Klein-/Großbuchstaben ein.\n")

# ==============================================================================
x = 0
mainloop = True

while mainloop:
    for i in range(10):
        subPassword = int(password) 
        if i == subPassword[x]:
           repassword.append(i)

    for i2 in string.ascii_letters:
        if i2 == password[x]:
           repassword.append(i2)

    x += 1

    if x >= len(password):
        mainloop = False

print(str(repassword))
