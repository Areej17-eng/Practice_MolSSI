#!/usr/bin/env python
# coding: utf-8

# In[48]:


### Running code from the Linux Command Line ###

# For this homework assignment, we will use the code from "Processing Multiple Files and Writing Files" 
# where we processed the file "03_Prod.mdout". We will create another Jupyter "analyze_mdout.ipynb". 
# Refer to this file for further details about the assignment.
# We will modify this using argparse to run in terminal.

## My Code ##
# Let us do an assignment now to find the total energy from any user defined *.mdout file (wild card).

import os
import glob                         # Import glob to handle wildcard patterns
import argparse

def open_mdout(mdout_file_path):    # "mdout_file_path" is just a placeholder to take the needed xyz file path

    
    # Create a .txt file to store Etot data (to have a variable file name, we use basename function):
    filename = os.path.basename(mdout_file_path)
    split_filename = filename.split('.')
    mdout_filename = split_filename[0]
    with open (F'*{mdout_filename}_Etot_file.txt' , 'w+') as Etot_txt_file:  # This line create a txt file
    
    # open the mdout file to get Etot data:
        with open (mdout_file_path , 'r') as outfile:    # "mdout_file_path" is user defined file path in terminal 
            data = outfile.readlines()
            for line in data:
                if "Etot" in line:
                    Etot_line = line
                    #print(Etot_line)
                    split_Etot_line = Etot_line.split()
                    Etot_value = float(split_Etot_line[2])
                    print(Etot_value)
                    Etot_txt_file.write(F'The total energy value is {Etot_value} \n')
                        

if __name__ == "__main__":
    # Initialize argparse
    parser = argparse.ArgumentParser(description = "The script analyzes a user given mdout file and outputs Etot.")
    # Generate argument for mdout file (Replace argparse setup with the following to allow multiple files)
    parser.add_argument("all_mdout_files", nargs="+", help="The file paths to multiple mdout files")
    args = parser.parse_args()
    all_mdout_files = args.all_mdout_files
    print(all_mdout_files)
# To call a function, I need input    
    for mdout_file in all_mdout_files:
        open_mdout(mdout_file)
        print(mdout_file)

## To use this code on terminal ##
# Convert ipynb file to py using: jupyter nbconvert --to script analyze_all_mdout.ipynb
# Use this command to enter the directory: cd /Users/areejnad/Documents/Areej\ Academic\ Data/My\ Research/CCR\ and\ Simulation\ Learning/Learning\ Python/Learning\ Data/
# Use this command to check the files: ls "CMS Workshp (MolSSI data)"/*.mdout      (notice the quotes location here)
# Use this command to execute: python analyze_all_mdout.py "CMS Workshp (MolSSI data)"/*.mdout
# Or use this command to execute: python analyze_all_mdout.py CMS\ Workshp\ \(MolSSI\ data\)/*.mdout


# In[7]:


## Original Code (Previously written by me) ##
# Let us do an assignment now to find the total energy from 03_Prod.mdout file.

# # Create a .txt file:
# with open ('Etot.txt' , 'w+') as Etot_txt_file:

# # Define the file path:
#     os_file_path = os.path.join('CMS Workshp (MolSSI data)' , '03_Prod.mdout')
#     print(os_file_path)

# # Remember that in the previous example, we used 2 for loops as we were processing 
# # multiple files in a directory. Here, we don't need that as there is only one file to process
#     with open (os_file_path , 'r') as outfile:
#         data = outfile.readlines()
#         for line in data:
#             if "Etot" in line:
#                 Etot_line = line
#                 #print(Etot_line)
#                 split_Etot_line = Etot_line.split()
#                 Etot_value = split_Etot_line[2]
#                 print(Etot_value)
#                 Etot_txt_file.write(F'The total energy value is {Etot_value} \n')
# Etot_txt_file.close()


# In[33]:


# import os
# import glob                         # Import glob to handle wildcard patterns
# import argparse

# def open_mdout(mdout_file_path):
#     # Extract filename and create the output file
#     filename = os.path.basename(mdout_file_path)
#     split_filename = filename.split('.')
#     mdout_filename = split_filename[0]
#     with open(f"{mdout_filename}_Etot_file.txt", 'w') as Etot_txt_file:
#         with open(mdout_file_path, 'r') as outfile:
#             data = outfile.readlines()
#             for line in data:
#                 if "Etot" in line:
#                     print("DEBUG: Found line ->", line)  # Add this to inspect the line
#                     split_Etot_line = line.split()
#                     print("DEBUG: Split line ->", split_Etot_line)  # Add this to inspect the split content
#                     Etot_value = float(split_Etot_line[2])
#                     Etot_txt_file.write(f"The total energy value is {Etot_value}\n")

# if __name__ == "__main__":
#     # Allow multiple file paths
#     parser = argparse.ArgumentParser(description="The script analyzes one or more mdout files and outputs Etot.")
#     parser.add_argument("mdout_files", nargs="+", help="Paths to one or more mdout files (use glob pattern for multiple files).")
#     args = parser.parse_args()

#     # Iterate through the provided files
#     for mdout_file in args.mdout_files:
#         open_mdout(mdout_file)


# In[ ]:




