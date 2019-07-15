# GPL 2 License 2011 Dealga McArdle July 12

import math

CMINCH = 0.393700787    # 1 centimeter = 0.393700787 inch 
INCHCM = 2.54           # 1 inch = 2.54 centimeters

# or whatever your machine can handle comfortably
largest_tile_dimension_wide = 1000
largest_tile_dimension_high = 1000

def get_pixels(mode, width, height, DPI):
    '''
    Takes realworld width, height and DPI to produce raster equivalent

    arguments   :   Description
    ------------------------------------------------------------
    mode        :   (string) ['CM','INCH'], prepares functions for input values
    width       :   (float) or int value for the real world measurement
    height      :   (float) or int value for the real world measurement
    DPI         :   (int) to declare what DPI you are aiming for.

    returns     :   by valid input:
                    cells_wide, cells_high, total_px_width, total_px_height

                    by invalid input: returns None
    '''
    
    if mode == 'CM':
        width_in_inches = width*CMINCH
        height_in_inches = height*CMINCH
    elif mode == 'INCH':
        width_in_inches = width
        height_in_inches = height
    else:
        print("mode must be 'INCH' or 'CM'")
        return None
    
    print("width", width, "x height", height, mode, "| DPI", DPI)
    if mode == 'CM':
        print("width", width_in_inches,"(inches)")
        print("height", height_in_inches, "(inches)")
        
    print("\nat", DPI, "DPI that gives: ")

    # [ ] todo verify if rounding up here is cool   
    w_in_px = width_in_inches*DPI
    h_in_px = height_in_inches*DPI
    w_in_px = math.floor(w_in_px)   
    h_in_px = math.floor(h_in_px)
    
    print("Width", w_in_px,"px. Height", h_in_px, "px")

    # determine number of tiles wide / high
    cells_wide = math.ceil(w_in_px / largest_tile_dimension_wide)
    cells_high = math.ceil(h_in_px / largest_tile_dimension_high)
    px_wide_per_tile = math.floor(w_in_px / cells_wide)
    px_high_per_tile = math.floor(h_in_px / cells_high)
    
    print(cells_wide, "tiles wide, at", px_wide_per_tile, "px wide")
    print(cells_high, "tiles high, at", px_high_per_tile, "px high")
    return cells_wide, cells_high, w_in_px, h_in_px
    
