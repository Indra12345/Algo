numbers =  [1,2,[21,22,[23,24,25,26]],3,4,["A,B", "ab", "a", "b"],100]
def flatten(lst):   
    controller = True
    while controller:
        lst, controller = helper(lst)  # this will return a tuple of list and controller            
    return lst

def helper(input):
    modified = False
    newlist = []
    
    for num in input:
        if type(num) is list:
            newlist.extend(num)
            modified = True
        else:
            newlist.append(num) 
          
    return newlist, modified

print(flatten(numbers))