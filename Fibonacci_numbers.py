# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 16:44:40 2021

@author: 82108
"""

"""
Making Function for calculating the "Fibonacci Numbers."
"""

def Fibonacci_cal(number) :
    list_1 = [1]
    list_2 = [1]
    Fibonacci = 0
    cnt = 0
    
    if number == 1 :
        Fibonacci = 1
    elif number == 2 :
        Fibonacci = 1
    else :        
        while cnt < number - 2 :
            cnt += 1
            Fibonacci = list_1[-1] + list_2[-1]
            if cnt % 2 == 1 :
                list_1.append(Fibonacci)
            else :
                list_2.append(Fibonacci)
    return Fibonacci
    

Fibonacci_cal(1) # 1
Fibonacci_cal(2) # 1
Fibonacci_cal(3) # 2
Fibonacci_cal(4) # 3
Fibonacci_cal(5) # 5
