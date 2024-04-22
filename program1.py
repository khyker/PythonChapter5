'''
Katellyn Hyker
Chapter 5 Project 1
Create a set of functions to calculate median, mean, and mode of a set of numbers.
Each function expects a list of numbers and returns a single number or 0 if the list is empty
Main function to test the calculation functions

'''
import random

LIST_LENGTH = 15

def main():
    numbers = []
    while len(numbers) <= LIST_LENGTH:
        n = random.randint(1, 200)
        numbers.append(n)


    print(f"The median of your numbers is", calcMedian(numbers))
    print(f"The mean of your numbers is", calcMean(numbers))
    print(f"The mode of your numbers is", calcMode(numbers))

def calcMedian(num_list):
    if len(num_list) != 0:
        num_list = sorted(num_list)
        mid_point = len(num_list) // 2
        if len(num_list) % 2 == 1:
            num_median = num_list[mid_point]
        else:
            num_median = (num_list[mid_point] + num_list[mid_point - 1]) / 2
    else:
        num_median = 0
    return num_median

def calcMean(num_list):
    total = 0
    if len(num_list) != 0:
        for num in num_list:
            total += num
            num_mean = total / len(num_list)
    else: 
        num_mean = 0
    return round(num_mean, 2)

def calcMode(num_list):
    num_dict = {}
    for number in num_list:
        if number != "":
            if number in num_dict:
                num_dict[number] += 1
            else:
                num_dict[number] = 1
    count = 0
    num_mode = ""
    for num in num_dict:
        if num_dict[num] > count:
            count = num_dict[num]
            num_mode = num
    return num_mode

if __name__ == "__main__":
    main()