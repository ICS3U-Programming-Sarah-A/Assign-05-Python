#!/usr/bin/env python3

# Created by: Sarah
# Created on: May 12th, 2022.
# This program asks the user several questions regarding their address. It then
# formats it and displays it to the user.

# this function calculates the volume of a square pyramid. 
def calculate_volume(base, height):
    volume = (height/3)*base**2
    
    return volume
    

def main():
    
    print("This program calculates the volume of a square pyrmaid.")
    print("")
    
    # get user input
    base_edge_string = input("Enter the base of the square pyrmaid: ")
    
    try:
        # convert from string to float
        base_edge_float = float(base_edge_string)
        
        height_string = input("Enter the height of the square pyramid: ")
        try:
            height_float = float(height_string)
            
            if base_edge_float > 0 and height_float > 0:
                square_volume = calculate_volume(base_edge_float, height_float)
            else:
                print("The base and height must be greater than 0.")
            
            print("")
            print("The volume of the square pyramid is {:,.2f} cm^3."
                  .format(square_volume))
            
        except Exception:
            print("{} is not valid input.".format(height_string))

    except Exception:
        print("{} is not a valid input.".format(base_edge_string))

if __name__ == "__main__":
    main()