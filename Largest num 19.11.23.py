#LAB 2 19/11/2023
#Write a python program using function to find the largest element in the list
def max_num(list):
    max = list[0]
    for a in list:
        if a > max:
            max = a
    return max
print(max_num([14, 10, -6, 9]))