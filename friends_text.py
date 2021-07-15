# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 13:36:39 2021

@author: 82108
"""

"""
Friends script
"""
import re
import os

os.chdir(r"C:\Users\82108\Desktop\Study\Educational Background\Programming\개인 공부\6_생활 프로그래밍\chapter03")

with open("friends101.txt", mode = 'r') as f :
    script101 = f.read()

print(script101)
type(script101) # str


# Check the lines by sitcom character

def Friends_Character(script, name) :
    Line = re.findall(f"{name}:.+", script)
    return Line

Monica_script = Friends_Character(script101, 'Monica')
Monica_script[:3]
'''
["Monica: There's nothing to tell! He's just some guy I work with!",
 "Monica: Okay, everybody relax. This is not even a date. It's just two people going out to dinner and- not having sex.",
 "Monica: And they weren't looking at you before?!"]
'''


# Making characters_list

def Friends_Character_List(script) :
    names = []
    char_names = re.findall("[A-Z][a-z]+:", script)
    for n in char_names :
        name = n.replace(":", "")
        if name not in names :
            names.append(name)
    names.remove("All")
    return names

character_names = Friends_Character_List(script101)
print(character_names)
# ['Scene', 'Monica', 'Joey', 'Chandler', 'Phoebe', 'Ross', 'Rachel', 'Waitress', 'Paul', 'Frannie', 'Customer']
len(character_names) # 11
