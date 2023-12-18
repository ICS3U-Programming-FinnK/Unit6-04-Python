#!/usr/bin/env python3
# Created by: Finn Kitor
# Created on: December 18th, 2023
# this program is a 2d array that makes the user input the rows and columns and
# is will generate 50 random numbers and will calculate the average
import random

MIN_NUM = 1
MAX_NUM = 50


def create_2d_array(rows: int, columns: int) -> list:
    try:
        if rows <= 0 or columns <= 0:
            raise ValueError("Number of rows and columns must be positive integers")
        # Create an empty 2D array
        array_2d = []
        # Generate random numbers and place them in the 2D array
        for i in range(rows):
            row = []
            for j in range(columns):
                # Generate a random number between MIN_NUM and MAX_NUM
                num = random.randint(MIN_NUM, MAX_NUM)
                row.append(num)
            array_2d.append(row)
        return array_2d
    except ValueError as e:
        print(f"Error creating 2D array: {e}")
        return None


def calc_average(array_2d: list) -> float:
    try:
        if not array_2d:
            raise ValueError("Array is empty")
        # Initialize variables for sum and count
        total_sum = 0
        count = 0
        # Calculate the sum of all the numbers in the 2D array
        for row in array_2d:
            for num in row:
                total_sum += num
                count += 1
        # Calculate the average
        average = total_sum / count
        return average
    except ValueError as e:
        print(f"Error calculating average: {e}")
        return 0.0


def main():
    try:
        # Ask the user for the number of rows and columns
        rows = int(input("Enter the number of rows: "))
        columns = int(input("Enter the number of columns: "))
        # Create the 2D array
        array_2d = create_2d_array(rows, columns)
        if not array_2d:
            return

        # Display the 2D array
        print("2D Array:")
        for row in array_2d:
            print(row)
        # Calculate and display the average
        average = calc_average(array_2d)
        print("Average:", average)
    except ValueError as e:
        print(f"Error: Invalid input, you inputted a string, not a number")


# Call the main function
if __name__ == "__main__":
    main()
