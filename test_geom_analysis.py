#!/usr/bin/env python
# coding: utf-8

# In[6]:


## Module 9: Testing Code with pytest


# In[73]:


# Just like we import other libraries, we import geom_analysis.py file here. The functions we defined 
# outside of our __main__ function are now accessible to us using the syntax "ga.function_name".
# However, all the functions defined in the __main__ function are not accessible with import command.

import geom_analysis_testing as ga        # Before importing the file, you need to save all its chnages as .py file 

# Now to test our "atomic_dist" function that we had defined in "geom_analysis" file:
def test_atomic_dist():            # The name of our function should begin with test to run with pytest
    coordinates_1 = [0, 0, 0]
    coordinates_2 = [1, 0, 0]
    expected = 1.0                 # The value we expect the test to return
    observed = ga.atomic_dist(coordinates_1, coordinates_2)
    assert observed == expected 

# Now save the file as .py and use this command interminal: pytest test_geom_analysis.py or pytest

# You should see this:
# test_geom_analysis.py .                                                                         [100%]
# ========================================== 1 passed in 0.10s ==========================================


# In[75]:


# You can also test your code like this for multiple values.

import geom_analysis_testing as ga
import numpy

def test_atomic_dist():
    # Case 1: Simple distance along the x-axis
    coordinates_1 = [0, 0, 0]
    coordinates_2 = [1, 0, 0]
    assert ga.atomic_dist(coordinates_1, coordinates_2) == 1.0     # observed == expected

    # Case 2: Distance along the y-axis
    coordinates_1 = [0, 0, 0]
    coordinates_2 = [0, 1, 0]
    assert ga.atomic_dist(coordinates_1, coordinates_2) == 1.0     # observed == expected

    # Case 3: Distance along the z-axis
    coordinates_1 = [0, 0, 0]
    coordinates_2 = [0, 0, 1]
    assert ga.atomic_dist(coordinates_1, coordinates_2) == 1.0     # observed == expected

    # Case 4: Diagonal distance
    coordinates_1 = [0, 0, 0]
    coordinates_2 = [1, 1, 1]
    assert ga.atomic_dist(coordinates_1, coordinates_2) == numpy.sqrt(3)    # sqrt(1**2 + 1**2 + 1**2) 

# You will again see the same above message.


# In[77]:


# Now to check if the bond_check function is working correctly:
import geom_analysis_testing as ga

def test_bond_check():
    bond_len = 1.2
    expected = True
    observed = ga.bond_check(bond_len)
    assert observed == expected

# You can also run using "pytest -v test_geom_analysis.py" or "pytest -v" to see more information.


# In[49]:


# To be very sure that the function "def bond_check(bond_len, min_length = 0, max_length = 1.5)" always works

def test_bond_check_true():
    bond_len = 1.2
    expected = True
    observed = ga.bond_check(bond_len)
    assert observed == expected 

def test_bond_check_false():
    bond_len = 2.0
    expected = False
    observed = ga.bond_check(bond_len)
    assert observed == expected 

def test_bond_check_0():       # To make for that for 0, the bond_len is discarded
    bond_len = 0
    expected = False
    observed = ga.bond_check(bond_len)
    assert observed == expected 
    
def test_bond_check_1_5():     # To make for that for 1.5, the bond_len is reported
    bond_len = 1.5
    expected = True
    observed = ga.bond_check(bond_len)
    assert observed == expected 
# You can also run using "pytest -v test_geom_analysis.py" or "pytest -v" to see more information.

# You will see this:
#collected 6 items                                                                                     
# test_geom_analysis.py::test_atomic_dist PASSED                                                  [ 16%]
# test_geom_analysis.py::test_bond_check PASSED                                                   [ 33%]
# test_geom_analysis.py::test_bond_check_true PASSED                                              [ 50%]
# test_geom_analysis.py::test_bond_check_false PASSED                                             [ 66%]
# test_geom_analysis.py::test_bond_check_0 PASSED                                                 [ 83%]
# test_geom_analysis.py::test_bond_check_1_5 PASSED                                               [100%]

# ========================================== 6 passed in 0.13s ==========================================


# In[85]:


# Let check if we define a -ve bond length. We modified our "geom_analysis" file to show error message.
import geom_analysis_testing as ga     # Before importing the file, you need to save all its chnages as .py file
import pytest

def test_bond_check_negative():       # To make for that for 0, the bond_len is discarded
    bond_len = -1.5
    expected = False
    with pytest.raises(ValueError):
        ga.bond_check(bond_len)

# So this function will raise an error if the data of bond_len contains any negative value. In our case,
# the data has no -ve value so the test will pass without displaying a value error, 
# otherwise it should pass and show the error statement.

# Currently, this test should pass like this:

# collected 7 items                                                                                     
# test_geom_analysis.py::test_atomic_dist PASSED                                                  [ 14%]
# test_geom_analysis.py::test_bond_check PASSED                                                   [ 28%]
# test_geom_analysis.py::test_bond_check_true PASSED                                              [ 42%]
# test_geom_analysis.py::test_bond_check_false PASSED                                             [ 57%]
# test_geom_analysis.py::test_bond_check_0 PASSED                                                 [ 71%]
# test_geom_analysis.py::test_bond_check_1_5 PASSED                                               [ 85%]
# test_geom_analysis.py::test_bond_check_negative PASSED                                          [100%]

# ========================================== 7 passed in 0.11s ==========================================


# In[89]:


# Let's create a test function to check the file extension (.xyz) and raise an error otherwise.

import geom_analysis_testing as ga     # Before importing the file, you need to save all its chnages as .py file
import pytest

def test_open_xyz():       # To make for that for 0, the bond_len is discarded
    my_file = "hello.txt"
    with pytest.raises(ValueError):
        ga.open_xyz(my_file)




# In[ ]:




