python
# More Data Structures: Set, Dictionary

## Overview
In this project, I explored sets and dictionaries in Python and practiced using them along with lambda, map, filter, and reduce methods.

### Sets in Python
A set is an unordered collection of unique elements in Python. Sets are useful when you want to store multiple items in a single variable and ensure uniqueness. They support various operations such as union, intersection, difference, and symmetric difference.

#### Examples:
python
# Creating a set
my_set = {1, 2, 3, 4, 5}

# Adding elements to a set
my_set.add(6)

# Removing elements from a set
my_set.remove(3)

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
difference_set = set1.difference(set2)


### Dictionaries in Python
A dictionary is a collection of key-value pairs in Python. It is a mutable, unordered collection that is used to store and retrieve data efficiently. Each key in a dictionary must be unique, and you can use keys to access corresponding values. Dictionaries are widely used for tasks involving mapping and associative arrays.

#### Examples:
python
# Creating a dictionary
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

# Accessing values
print(my_dict['name'])  # Output: John

# Adding or updating key-value pairs
my_dict['occupation'] = 'Engineer'

# Removing a key-value pair
del my_dict['age']

# Dictionary operations
keys = my_dict.keys()
values = my_dict.values()


## Function Prototypes 💾

| File                          | Prototype                                               |
|-------------------------------|---------------------------------------------------------|
| 0-square_matrix_simple.py     | def square_matrix_simple(matrix=[]):                     |
| 1-search_replace.py           | def search_replace(my_list, search, replace):            |
| 2-uniq_add.py                 | def uniq_add(my_list=[]):                                |
| 3-common_elements.py          | def common_elements(set_1, set_2):                       |
| 4-only_diff_elements.py       | def only_diff_elements(set_1, set_2):                    |
| 5-number_keys.py              | def number_keys(a_dictionary):                           |
| 6-print_sorted_dictionary.py  | def print_sorted_dictionary(a_dictionary):               |
| 7-update_dictionary.py        | def update_dictionary(a_dictionary, key, value):        |
| 8-simple_delete.py            | def simple_delete(a_dictionary, key=""):                |
| 9-multiply_by_2.py            | def multiply_by_2(a_dictionary):                        |
| 10-best_score.py              | def best_score(a_dictionary):                            |
| 11-multiply_list_map.py       | def multiply_list_map(my_list=[], number=0):           |
| 12-roman_to_int.py            | def roman_to_int(roman_string):                         |
| 100-weight_average.py         | def weight_average(my_list=[]):                         |
| 101-square_matrix_map.py      | def square_matrix_map(matrix=[]):                       |
| 102-complex_delete.py         | def complex_delete(a_dictionary, value):                |
| 103-python.c                  | void print_python_list(PyObject *p);                    |
|                               | void print_python_bytes(PyObject *p);                   |

## Tasks 📃

### 0. Squared simple
- `0-square_matrix_simple.py`: Computes the square value of all integers in a matrix.
  - Parameters: matrix (two-dimensional array).
  - Returns: a matrix of the same size as the input matrix with squared values.

### 1. Search and replace
- `1-search_replace.py`: Replaces all occurrences of an element with another in a new list.
  - Parameters: my_list (initial list), search (element to replace), replace (new element).
  - Returns: a new list with replacements.

### 2. Unique addition
- `2-uniq_add.py`: Adds all unique integers in a list (once for each integer).
  - Parameters: my_list (list of integers).
  - Returns: the sum of unique integers.

### 3. Present in both
- `3-common_elements.py`: Returns a set of common elements in two sets.
  - Parameters: set_1, set_2 (sets).
  - Returns: a set of common elements.

### 4. Only differents
- `4-only_diff_elements.py`: Returns a set of elements present in only one set.
  - Parameters: set_1, set_2 (sets).
  - Returns: a set of unique elements.

### 5. Number of keys
- `5-number_keys.py`: Returns the number of keys in a dictionary.
  - Parameters: a_dictionary (dictionary).
  - Returns: the number of keys.

### 6. Print sorted dictionary
- `6-print_sorted_dictionary.py`: Prints a dictionary by ordered keys.
  - Parameters: a_dictionary (dictionary).
  - Prints: keys in alphabetical order with their corresponding values.

### 7. Update dictionary
- `7-update_dictionary.py`: Replaces or adds key/value pairs in a dictionary.
  - Parameters: a_dictionary (dictionary), key (string), value (any type).
  - Modifies: the input dictionary.

### 8. Simple delete by key
- `8-simple_delete.py`: Deletes a key in a dictionary.
  - Parameters: a_dictionary (dictionary), key (string).
  - Modifies: the input dictionary.

### 9. Multiply by 2
- `9-multiply_by_2.py`: Returns a new dictionary with all values multiplied by 2.
  - Parameters: a_dictionary (dictionary with integer values).
  - Returns: a new dictionary with values multiplied by 2.

### 10. Best score
- `10-best_score.py`: Returns a key with the biggest integer value in a dictionary.
  - Parameters: a_dictionary (dictionary with integer values).
  - Returns: the key with the highest value or None if the dictionary is empty.

### 11. Multiply by using map
- `11-multiply_list_map.py`: Returns a list with all values multiplied by a number using map.
  - Parameters: my_list (list of integers), number (integer).
  - Returns: a new list with each value multiplied by the given number.

### 12. Roman to Integer
- `12-roman_to_int.py`: Converts a roman numeral to an integer.
  - Parameters: roman_string (string representing a roman numeral).
  - Returns: the integer value corresponding to the roman numeral.

### 13. Weighted average!
- `100-weight_average.py`: Returns the weighted average of integers in a list of tuples.
  - Parameters: my_list (list of tuples in the format (<score>, <weight>)).
  - Returns: the weighted average or 0 if the list is empty.

### 14. Squared by using map
- `101-square_matrix_map.py`: Computes the square value of all integers in a matrix using map.
  - Parameters: matrix (two-dimensional array).
  - Returns: a new matrix with each value squared.

### 15. Delete by value
- `102-complex_delete.py`: Deletes keys with a specific value in a dictionary.
  - Parameters: a_dictionary (dictionary), value (value to delete).
  - Modifies: the input dictionary.

### 16. CPython #1: PyBytesObject
- `103-python.c`: C functions that print basic information about Python lists and Python bytes objects.
