import os
import time
import numpy as np
import pandas as pd

class Tact_Random():
    """
        Tact Random instance to perform all random operations. 

        Will be adding more soon

        * Random small data for testing
        * Indian pincodes
        * Indian cities
        * Indian states
        * Indian Engineering Colleges
        * Canadian cities
        * US states
        * US cities
        * US Postal Codes
    """
    def __init__(self):
        pass

    def get_xy_for_math(self, content):
        """
        Find X and Y from the equation y = mx + c

        Input:
        content:str: String in the form y = mx + c

        Output:
        xs and ys from the function
        """

        # Sample : y = 2x + 2; y = mx + c
        
        parts = content.split("=")
        
        #print(parts)
        
        part_left  = parts[0].strip()
        part_right = parts[1].strip()
        
        math_sign = "+"
        
        if('+' in part_right):
            right_parts = part_right.split('+')
        else: # assume it is minus
            right_parts = part_right.split('-')
            math_sign = "-"
            
        mx_part = right_parts[0].strip().replace('x', '')
        c_part  = right_parts[1].strip()
        
        m = int(mx_part)
        c = int(c_part)
        
        xs_base = np.random.randint(10, size = 5)
        ys_base = (m * (xs_base)) + c
        
        xs = xs_base
        ys = ys_base
    
        return xs, ys

    def convert_hr_min(self, seconds): 
       """  
        Function to convert seconds to hours and minutes easily

        Input:
        seconds:int - Number of seconds in int

        Output:
        Time in Hours and Minutes(if available) in str 
       """ 
       
       return time.strftime("%H Hour %M Minute %S Seconds", time.gmtime(seconds)) 