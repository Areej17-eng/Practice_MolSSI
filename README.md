# geom_analysis code description

## This file contains the description of geom_analysis code. For the reference code, refer to the file "geom_analysis-unparsed (original)".

This code combines three functions to work together and calculate the **bond length** between various atoms and *print only realistic ones*. Following is the description of individual functions.
1. **"open_xyz"** function is used to open any xyz file specified in the code and finds the molecules and coordinates data to process.
2. **"atomic_dist"** function calculates the bond length based on the coordinates data obtained from the **"open_xyz"** function.
3. **"bond_check"** function check if the bond lengths calculated are realistic to print.
Then in the **Input** part, we specify the xyz file to be processed, and finally in the **Main Script** part, we are printing the bond length avoiding repetition of the same bonds.