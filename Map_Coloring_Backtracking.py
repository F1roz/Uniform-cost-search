import random

adj = {
       'WA': ['NT', 'SA'],
       'NT': ['WA', 'SA', 'Q'],
       'Q': ['NT', 'SA', 'NSW'],
       'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
       'NSW': ['Q','SA', 'V'],
       'V': ['SA', 'NSW'],
       'T': []
       }

assignment = {}


def select_unassigned_Varible():
    
    unassigned_vars = []
    for item in adj.keys():
        if item in assignment:
            continue
        else: 
            unassigned_vars.append(item)
    return random.choice(unassigned_vars)  


def ordered_domain_value():
    return ['R', 'G', 'B']


def value_is_consistent(variable, value):
    for item in adj[variable]:
        if item in assignment:
            if assignment[item] == value:
                return False
            
    return True
    

def recursive_backtracking():
    if len(assignment) == len(adj):
        return assignment
  
    var = select_unassigned_Varible()  
    for value in ordered_domain_value():
        if value_is_consistent(var, value):
            assignment[var] = value
            result = recursive_backtracking()
            if result != 'failure':
                return result
            
            del assignment[var]
    return 'failure'



print(recursive_backtracking())
            
            
            
            
            
            
