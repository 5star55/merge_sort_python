def merge_sort(list):
    """
    sorts a list in asccending order
    Returns a new sorted list
    Divide: find the mid point and divide into sublists 
    conquer: recursively sort the sublist created in previous step
    combine: merge the sorted sublists created in previous step
    """
    if len(list)<=1:
        return list

    left_half, right_half= split(list)

    left=merge_sort(left_half)
    right=merge_sort(right_half)

    return merge(left,right)

def split(list):

    """
    divide the unsorted list at mipoint
    returns two sublists- left and right
    """
    mid_point=(len(list))//2
    left= list[:mid_point]
    right= list[mid_point:]

    return left,right

def merge(left, right):
    """
    this function merges two list, sorting them in the process
    Returns a new merged list
    """

    new = []
    i=0
    j=0

    while i< len(left) and j< len(right):
       if left[i]<right[j]:
           new.append(left[i])
           i+=1
       else:
           new.append(right[j])
           j+=1
    
    while i< len(left):
        new.append(left[i])
        i+=2

    while j< len(right):
        new.append(right[j])
        j+=1
    return new
    
list=[1,9,6,2,0,9]

new=merge_sort(list)       
print(new)

           









