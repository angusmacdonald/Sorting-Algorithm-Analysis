import logging
import Monitoring

"""
Simple implementation
Efficient for (quite) small data sets
Adaptive, i.e. efficient for data sets that are already substantially sorted: the time complexity is O(n + d), where d is the number of inversions
More efficient in practice than most other simple quadratic, i.e. O(n2) algorithms such as selection sort or bubble sort; the best case (nearly sorted input) is O(n)
Stable, i.e. does not change the relative order of elements with equal keys
In-place, i.e. only requires a constant amount O(1) of additional memory space
Online, i.e. can sort a list as it receives it

http://en.wikipedia.org/wiki/Insertion_sort

Worst case performance    O(n2)
Best case performance    O(n)
Average case performance    O(n2)
Worst case space complexity    O(n) total, O(1)

The size of list for which insertion sort has the advantage varies by environment and implementation, but is typically between eight and twenty elements.
"""

"""
Starts off (in the outer loop) looping from the second element till the end of the array. For every outer loop it is trying to find the highest place in
the array to place array[i] (the key). It does this by starting from i and going back towards the start of the array. It pushes 
the key down the array until no further improvement can be made. It doesn't have to assign the key to a new position every time - it only
pushes up the value in j to j+1. It assigns the key when no further improvement can be made.

It then increments i so that it can try to find the best position for the key.

This is good if an array is already mostly sorted, but could result in a lot of unnecessary back and forth if the next value up (i+1)
has to take the place of i, and so on. 
"""
def insertionSort(array , eval=Monitoring.Monitor()):
    for i in range(1, (len(array))): # start off on second element
        key = array[i] #the current value we're trying to push up the array.
        j= i-1 #initially this is the first element
        
        logging.debug("i is {0:d}, j is {1:d}, key is {2:d}, array is {3}".format(i, j, key, array))
        
        done = False
        
        while not done:
            eval.incrementComparisons()
            if array[j] > key: #if the first element is greater than the second element, GET READY TO swap them.
                array[j+1] = array[j] #there is an improvement to be made, so swap the higher value with the one above it in the array.
                eval.incrementMoves()
                j = j-1 # go down to the next element to see if it can be moved even further.
                logging.debug("improvement to be made for {0:d}, j= {1:d}, array={2}".format(key, j, array))
                if j < 0: #if j is >= 0, compare this element with the current ith element; if not, increment i.
                    done = True
            else: # if the jth element is smaller than the ith element we're done (because the start of the list -before i- is already sorted)
                done = True
        logging.debug("\t array[{0:d}]={1:d}".format(j+1, key))
        array[j+1] = key #j+1 is the position on which we became 'done' - i.e. the position for which the key value will be placed.
        #if no better place was found this assignment has no affect
    return array

if __name__ == '__main__':
    example = [2,6,7,2,6,9,9,1,1,5]
    
    logging.basicConfig(level=logging.DEBUG)
    
    eval= Monitoring.Monitor()
    
    print "Before : ", example
    insertionSort(example, eval)
    print "After : ", example
    print "Number of comparisons: {0}\nNumber of moves: {1}".format(eval.numberOfComparisons, eval.numberOfMoves)  
         
    '''               
    badInsertionSortExample = [x for x in range(10, 1, -1)]
    
    print "Before : ", badInsertionSortExample
    insertionSort(badInsertionSortExample)
    print "After : ", badInsertionSortExample
    '''  
                