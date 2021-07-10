# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 11:05:05 2021

@author: 82108
"""

'''
Making Bulls and Cows Game

# Rules
1. A computer chooses three numbers randomly. (users don't know what is the answer.') # the range is 1 t 10.
2. Users have five chances to get the correct answer.
3. If numbers that users enter are in the answer, but not located in the right place,
   a computer prints "ball!"
4. If numbers that users enter are in the answer and located in the right place, 
   a computer prints "strike!"
   
ex)
answer = 123
the numbers that users enter = 152

then, a computer prints "1 Strike!, 1 Ball!"
'''


# First Step : Generating three numbers
import random

answer = []
while len(answer) < 3 :
    random_number = random.randint(1, 9)
    if random_number not in answer :
        answer.append(random_number)
  
    
# Second Step : Enter numbers

count = 0
your_numbers = []

while count < 3 :
    count += 1
    number = int(input("Enter number : "))
    your_numbers.append(number)
    
print(your_numbers)

# Third Step : Check
s_count = 0
b_count = 0



for i in range(0 ,3) :
    if your_numbers[i] == answer[i] :
        s_count += 1
    elif your_numbers[i] in answer and your_numbers[i] != answer[i] :
        b_count += 1

print(f"{s_count} Strike!, {b_count} Ball!")


# Final Step : Complete

import random

chance_count = 5


answer = []
while len(answer) < 3 :
    random_number = random.randint(1, 9)
    if random_number not in answer :
        answer.append(random_number)

while chance_count > 0 :
    enter_count = 0
    your_numbers = []
    
    while enter_count < 3 :
        enter_count += 1
        number = int(input("Enter number : "))
        your_numbers.append(number)
    
    s_count = 0
    b_count = 0
    
    for i in range(0, 3) :
        if your_numbers[i] == answer[i] :
            s_count += 1
        elif your_numbers[i] in answer and your_numbers[i] != answer[i] :
            b_count += 1
    
    chance_count -= 1
    
    if s_count == 3 :
        print("Success!")
        break
    elif chance_count == 0 :
        print("Fail!")
        break
    
    print(f"{s_count} Strike!, {b_count} Ball!")
    print("Now, you have {} chances.".format(chance_count))
    
    
    
