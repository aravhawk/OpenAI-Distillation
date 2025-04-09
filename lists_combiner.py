from problem_lists import *

def combine_all_lists():
    all_vars = globals()
    
    all_lists = []
    for var_name, var_value in all_vars.items():
        if isinstance(var_value, list):
            all_lists.append(var_value)

    combined_list = []
    for lst in all_lists:
        combined_list.extend(lst)
    
    return combined_list
