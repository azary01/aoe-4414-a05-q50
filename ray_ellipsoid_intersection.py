# script_name.py
#
# Usage: python3 ray_ellipsoid_intersection.py d_l_x d_l_y d_l_z c_l_x c_l_y c_l_z
#  Text explaining script usage
# Parameters:
# d_l_x: x-component of origin-referenced ray direction
# d_l_y: y-component of origin-referenced ray direction
# d_l_z: z-component of origin-referenced ray direction
# c_l_x: x-component offset of ray origin
# c_l_y: y-component offset of ray origin
# c_l_z: z-component offset of ray origin
# Output:
#  A description of the script output
#
# Written by Austin Zary
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
import math # math module
import sys # argv

# "constants"
R_E_KM = 6378.137
E_E    = 0.081819221456

# helper functions

## function description
# def calc_something(param1, param2):
#   pass

# initialize script arguments
d_l_x = float('nan')
d_l_y = float('nan')
d_l_z = float('nan')
c_l_x = float('nan')
c_l_y = float('nan')
c_l_z = float('nan')
# parse script arguments
if len(sys.argv)==7:
    d_l_x = float(sys.argv[1])
    d_l_y = float(sys.argv[2])
    d_l_z = float(sys.argv[3])
    c_l_x = float(sys.argv[4])
    c_l_y = float(sys.argv[5])
    c_l_z = float(sys.argv[6])
else:
    print(\
        'Usage: '\
        'python3 ray_ellipsoid_intersection.py d_l_x d_l_y d_l_z c_l_x c_l_y c_l_z'\
    )
    exit()

# write script below this line
a = d_l_x**2.0 + d_l_y**2.0 + (d_l_z**2.0)/(1.0-E_E**2.0)
b = 2.0 * (d_l_x*c_l_x + d_l_y*c_l_y + d_l_z*c_l_z/(1.0-E_E**2.0))
c = c_l_x**2.0 + c_l_y**2.0 + c_l_z**2.0/(1.0-E_E**2.0) - R_E_KM**2.0

discr = b*b - 4.0*a*c
if discr>=0.0:
    d = (-b-math.sqrt(discr))/(2.0*a)
    if d<0.0:
        d = (-b+math.sqrt(discr))/(2.0*a)
    if d>=0.0:
        l_x = d*d_l_x + c_l_x
        l_y = d*d_l_y + c_l_y
        l_z = d*d_l_z + c_l_z
        print(l_x)
        print(l_y)
        print(l_z)

