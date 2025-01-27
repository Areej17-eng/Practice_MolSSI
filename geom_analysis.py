#!/usr/bin/env python
# coding: utf-8

# In[59]:


### Running code from the Linux Command Line ###

## We will be usiing the same code that we developed in the last module.

# Now let's combine all the above functions to open an xyz file and calculate bond lengths for its atoms:

import os
import numpy
import argparse

""" Function to get/open the file"""
def open_xyz(xyz_file_path):           # "xyz_file_path" is just a placeholder to take the needed xyz file path 
    xyz_file = numpy.genfromtxt(fname = xyz_file_path, skip_header = 2, dtype = 'unicode')
    molecules = xyz_file[:,0]
    coordinates = xyz_file[:,1:]
    coordinates = coordinates.astype(numpy.float64)
    return molecules, coordinates

""" Function to calculate the bond_len for any_xyz_file"""
def atomic_dist(atom1_coord, atom2_coord):
    x_distances = atom1_coord[0] - atom2_coord[0]
    y_distances = atom1_coord[1] - atom2_coord[1]
    z_distances = atom1_coord[2] - atom2_coord[2]
    bond_len = numpy.sqrt(x_distances**2 + y_distances**2 + z_distances**2)
    return bond_len

""" Function to check if a distance qualifies as a bond define the max/min value for bond_len""" 
def bond_check(bond_len, min_length = 0, max_length = 1.5):
    if bond_len < 0:
        raise ValueError(F'Invalid bond length{bond_len}. Distance can not be less than 0!')
    if bond_len > min_length and bond_len <= max_length:
        return True
    else:
        return False

""" Function to call already defined "atomic_dist" funct for bond_length calculation using xyz file data"""
""" This is the main script to calculate and print bond lengths """
# This time, we will use argument parse commands to run any xyz file from the terminal.
if __name__ == "__main__":
    # Initialize argparse
    parser = argparse.ArgumentParser(description="This script analyzes a user given xyz file and outputs the length of the bonds.")
    # Generate argument for xyz file
    parser.add_argument("xyz_file", help="The filepath for the xyz file to analyze.") # Here xyz_file is the argument name (can be any name)
    # Generate argument for min_bond length
    parser.add_argument("--min_bond_len", help="The minimum distance to consider atoms bonded.", type=float, default=0) # Here min_bond_len is the argument name (-- means optional)
    # Generate argument for max_bond length
    parser.add_argument("--max_bond_len", help="The maximum distance to consider atoms bonded.", type=float, default=1.5) # Here max_bond_len is the argument name (-- means optional)
    args = parser.parse_args()
    
    xyz_file = args.xyz_file
    min_bond_len = args.min_bond_len
    max_bond_len = args.max_bond_len

    molecules , coordinates = open_xyz(xyz_file)

    # We add another argparse to allow user specification of min bond length
    
    # Main Script:
    row_num = len(coordinates[:,0])
    for i_1 in range(0, row_num):
        for i_2 in range(0, row_num):
            if i_1 < i_2:
                bond_len = atomic_dist(coordinates[i_1] , coordinates[i_2])    #coordinates[i_1] or [i_2] is the real data that we put in place of placeholders atom1_coord & atom2_coord
                if bond_check(bond_len, min_bond_len, max_bond_len) is True:
                    print(F'{molecules[i_1]} to {molecules[i_2]}:' , bond_len)


## To use this code on terminal ##
# Convert ipynb file to py using: jupyter nbconvert --to script geom_analysis.ipynb
# Use this command to enter the directory: cd /Users/areejnad/Documents/Areej\ Academic\ Data/My\ Research/CCR\ and\ Simulation\ Learning/Learning\ Python/Learning\ Data/
# Use this command to execute: python geom_analysis.py "CMS Workshp (MolSSI data)/water.xyz"

# Values in bond_check: The function bond_check(bond_len, min_length=0, max_length=1.5) uses default 
# values for the min_length and max_length. If no values are passed explicitly to the function, it will use these defaults.
# The default values in bond_check are overridden if the user-specified values 
# (min_bond_len and max_bond_len) are passed explicitly when calling the function.

# Now run the code as: python geom_analysis.py "CMS Workshp (MolSSI data)/water.xyz" --min_bond_len 0.5 --max_bond_len 2.0 



# In[ ]:





# In[ ]:




