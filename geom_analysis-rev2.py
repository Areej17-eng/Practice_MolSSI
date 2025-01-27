#!/usr/bin/env python
# coding: utf-8

# In[24]:


## We will be using the same code that we developed in the last module.

# Now let's combine all the above functions to open an xyz file and change the code to accept user inputs:
# To allow our code to accpet user defined arguments, we will use "sys" library instead of "argparse"

import os
import numpy
import sys

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
    if bond_len > 0 and bond_len <= 1.5:
        return True
    else:
        return False

""" Function to call already defined "atomic_dist" funct for bond_length calculation using xyz file data"""
""" This is the main script to calculate and print bond lengths """
# Inputs:
# We create an argument to allow user to enter the name of any xyz file

if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise NameError("Incorrect input! Please specify a file to analyze.")
    
    xyz_filename = sys.argv[1]
    molecules, coordinates = open_xyz(xyz_filename)   # This assignment makes the "water_file" variables available in the main script.
    
    # Main Script:
    row_num = len(coordinates[:,0])
    for i_1 in range(0, row_num):
        for i_2 in range(0, row_num):
            if i_1 < i_2:
                bond_len = atomic_dist(coordinates[i_1] , coordinates[i_2])
                if bond_check(bond_len) is True:
                    print(F'{molecules[i_1]} to {molecules[i_2]}:' , bond_len)


# sys.argv is a list that contains command-line arguments passed to the script when it is executed.
# For a cammand line argument, "python script_name.py file.xyz", sys.argv[0] will be "script_name.py" and
# sys.argv[1] will be "file.xyz". In the above code, we specified xyz_filename as sys.argv[1].
# Everything after "python" is an argument, so sys.argv[0] is always considered the name of our script.

## To run the code in cammand line
# Use this command to covert to .py file: jupyter nbconvert --to script geom_analysis-rev2.ipynb
# Use this command to run the .py file: python geom_analysis-rev2.py "CMS Workshp (MolSSI data)/water.xyz"


# In[6]:


# ## ORIGINAL CODE ##


# ## We will be usiing the same code that we developed in the last module.

# # Now let's combine all the above functions to open an xyz file and calculate bond lengths for its atoms:

# import os
# import numpy
# import argparse

# """ Function to get/open the file"""
# def open_xyz(xyz_file_path):           # "xyz_file_path" is just a placeholder to take the needed xyz file path 
#     xyz_file = numpy.genfromtxt(fname = xyz_file_path, skip_header = 2, dtype = 'unicode')
#     molecules = xyz_file[:,0]
#     coordinates = xyz_file[:,1:]
#     coordinates = coordinates.astype(numpy.float64)
#     return molecules, coordinates

# """ Function to calculate the bond_len for any_xyz_file"""
# def atomic_dist(atom1_coord, atom2_coord):
#     x_distances = atom1_coord[0] - atom2_coord[0]
#     y_distances = atom1_coord[1] - atom2_coord[1]
#     z_distances = atom1_coord[2] - atom2_coord[2]
#     bond_len = numpy.sqrt(x_distances**2 + y_distances**2 + z_distances**2)
#     return bond_len

# """ Function to check if a distance qualifies as a bond define the max/min value for bond_len""" 
# def bond_check(bond_len, min_length = 0, max_length = 1.5):
#     if bond_len > 0 and bond_len <= 1.5:
#         return True
#     else:
#         return False

# """ Function to call already defined "atomic_dist" funct for bond_length calculation using xyz file data"""
# """ This is the main script to calculate and print bond lengths """
# # Inputs:
# water_file = os.path.join('CMS Workshp (MolSSI data)', 'water.xyz')   # This is my input for "xyz_file"  
# water_molecule, coordinates = open_xyz(water_file)   # This assignment makes the "water_file" variables available in the main script.

# # Main Script:
# row_num = len(coordinates[:,0])
# for i_1 in range(0, row_num):
#     for i_2 in range(0, row_num):
#         if i_1 < i_2:
#             bond_len = atomic_dist(coordinates[i_1] , coordinates[i_2])
#             if bond_check(bond_len) is True:
#                 print(F'{water_molecule[i_1]} to {water_molecule[i_2]}:' , bond_len)
                


# In[ ]:




