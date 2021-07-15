# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 11:17:50 2021

@author: 82108
"""

"""
Morse Code Translator
"""

moss_dict = {'.-':'A', '-...':'B', '-.-.':'C', '-..':'D', '.':'E', '..-.':'F',
             '--.':'G', '....':'H', '..':'I', '.---':'J', '-.-':'K', '.-..':'L',
             '--':'M', '-.':'N', '---':'O', '.--.':'P', '--.-':'Q', '.-.': 'R',
             '...':'S', '-':'T', '..-':'U', '...-':'V', '.--':'W', '-..-':'X',
             '-.--':'Y', '--..':'Z'}


def moss_trans(mos_str) : 
    word_list = []
    word_mos = mos_str.split('  ')
    for n in word_mos :
        alphabet_list = []
        alphabet_mos = n.split(' ')
        for a in alphabet_mos :
            alphabet = moss_dict[a]
            alphabet_list.append(alphabet)
        word = ''.join(alphabet_list)
        word_list.append(word)
    sentence = ' '.join(word_list)
    return sentence


answer = moss_trans('.... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--')
print(answer) # HE SLEEPS EARLY