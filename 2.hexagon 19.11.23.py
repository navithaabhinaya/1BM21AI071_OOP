#LAB 2 19/11/2023
#2.Write a function called hexagon ... 
import math

def hexagon(side_length):
   
    area = (3 * math.sqrt(3) * side_length ** 2) / 2
    return area

side_length = float(input("Enter the side length of the hexagon: "))

hexagon_area = hexagon(side_length)
print(f"The area of the hexagon with side length {side_length} is: {hexagon_area:.2f}")
