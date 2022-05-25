#!/usr/bin/env python3

# Created by: Sarah
# Created on: May 18th, 2022.
# This program asks the user for the base and height. It then
# calculates the volume of a square pyramid and its lateral surface area. It
# displays the results to the user.
import math


# this function is used to calculate the volume.
def calculate_volume(base, height):
    volume = (height/3)*base**2

    return volume


# this function is used to calculate the lateral surface area.
def calculate_lat_area(base, height):
    lateral_area = base * (math.sqrt(base**2 + 4*height**2))

    return lateral_area


def main():
    print("This program calculates the volume of a square pyramid & "
          "the lateral surface area.")
    print("")

    # get user input
    base_edge_string = input("Enter the base of the square pyramid: ")

    try:
        # convert from string to float
        base_edge_float = float(base_edge_string)

        # gets user input
        height_string = input("Enter the height of the square pyramid: ")
        try:
            # converts from string to float
            height_float = float(height_string)

            # sets a range & calls the function
            if base_edge_float > 0 and height_float > 0:
                # calls functions
                square_volume = calculate_volume(base_edge_float, height_float)
                area_lat = calculate_lat_area(base_edge_float, height_float)
                # display results.
                print("")
                print("The volume of the square pyramid is {:,.2f} cm³ and"
                      .format(square_volume))

                # displays results
                print("the lateral surface area of the square pyramid is "
                      "{:,.2f} cm².".format(area_lat))
            else:
                print("")
                print("The base and height must be greater than 0.")

        # handles the error case
        except Exception:
            print("")
            print("{} is not valid input.".format(height_string))

    # handles the error case
    except Exception:
        print("")
        print("{} is not a valid input.".format(base_edge_string))


if __name__ == "__main__":
    main()
