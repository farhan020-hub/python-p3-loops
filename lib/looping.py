#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    numbers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    for number in numbers:
        print(number)
        print("Happy New Year!")
    

def square_integers(int_list):
    squared_list = []
    for num in int_list:
        squared_list.append(num * num)
    return squared_list
    

def fizzbuzz():
    # code goes here!
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)
