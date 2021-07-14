# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 10:18:15 2021

@author: 82108
"""

"""
No.16 [Power digit sum]

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

def Power_digit_sum_2(square) :
    result = 0
    num = 2 ** square
    str_num = str(num)
    for s in str_num :
        result += int(s)
    return result

answer = Power_digit_sum_2(1000)
print(answer) # 1366

'''
[The answer]
1366
'''











"""
No.17 [Number letter counts]

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters 
and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

num_dict = {0:'', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten',
            11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen',
            18:'eighteen', 19:'nineteen', 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'senventy',
            80:'eighty', 90:'ninety', 100:'onehundredand', 200:'twohundredand', 300:'threehundredand', 400:'fourhundredand',
            500:'fivehundredand', 600:'sixhundredand', 700:'sevenhundredand', 800:'eighthundredand', 900:'ninehundredand',
            1000:'onethousand'}

def num_trans_str(number) :
    word_list = []
    for i in range(1, number+1) : # 1 ~ 19
        if i < 20 :
            word = num_dict[i]
            word_list.append(word)
        elif i >= 20 and i < 100 : # 20 ~ 99
            if i % 10 == 0 :
                word = num_dict[i]
                word_list.append(word)
            else : 
                tenth = i - (i % 10)
                oneth = (i % 10)
                word = num_dict[tenth] + num_dict[oneth]
                word_list.append(word)
        elif i >= 100 and i < 1000 : # 100 ~ 999
            if i % 100 == 0 :
                word = num_dict[i]
                word_list.append(word)
            elif i % 10 == 0 :
                hundredth = i - (i % 100)
                tenth = i % 100
                word = num_dict[hundredth] + num_dict[tenth]
                word_list.append(word)
            elif i % 10 != 0 :
                hundredth = i - (i % 100)
                tenth = (i % 100) - (i % 10)
                oneth = i % 10
                word = num_dict[hundredth] + num_dict[tenth] + num_dict[oneth]
                word_list.append(word)
        elif i == 1000 : # 1000
            word = num_dict[i]
            word_list.append(word)
    return word_list
                

final_word_list = num_trans_str(1000) 
print(final_word_list)
len(final_word_list) # 1000

cnt = 0
for word in final_word_list :
    cnt += len(word)

print(cnt) # 21215
