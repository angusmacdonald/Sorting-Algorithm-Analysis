import logging
import Monitoring

"""
Merge sort breaks the list down recursively, ultimately resulting in a sort operation (merge) between two lists of size 1.
This list is returned up the call stack and it is merged with another list of similar size, until the final two lists are merged
to create the complete sorted set.

http://en.wikipedia.org/wiki/Merge_sort

Merge sort incorporates two main ideas to improve its runtime:
A small list will take fewer steps to sort than a large list.
Fewer steps are required to construct a sorted list from two sorted lists than two unsorted lists. 
For example, you only have to traverse each list once if they're already sorted.

Although heapsort has the same time bounds as merge sort, it requires only O(1) auxiliary space instead of merge sort's O(n), 
and is often faster in practical implementations. On typical modern architectures, efficient quicksort implementations generally 
outperform mergesort for sorting RAM-based arrays. On the other hand, merge sort is a stable sort, parallelizes better, and is more 
efficient at handling slow-to-access sequential media. Merge sort is often the best choice for sorting a linked list: in this situation 
it is relatively easy to implement a merge sort in such a way that it requires only O(1) extra space, and the slow random-access performance 
of a linked list makes some other algorithms (such as quicksort) perform poorly, and others (such as heapsort) completely impossible.

Merge sort's merge operation is useful in online sorting, where the list to be sorted is received a piece at a time, 
instead of all at the beginning. In this application, we sort each new piece that is received using any sorting algorithm, 
and then merge it into our sorted list so far using the merge operation. However, this approach can be expensive in time 
and space if the received pieces are small compared to the sorted list - a better approach in this case is to store the 
list in a self-balancing binary search tree and add elements to it as they are received.


Worst case performance    O(nlogn)
Best case performance    O(nlogn) typical, O(n) natural variant
Average case performance    O(nlogn)
Worst case space complexity    O(n) auxiliary
"""

def mergeSort(listToMerge, eval=Monitoring.Monitor()):
    logging.debug("MERGE_SORT: {0}".format(listToMerge))
    
    if len(listToMerge) <= 1:
        return listToMerge

    middle_pos = len(listToMerge) / 2
    
    eval.incrementMovesByN(len(listToMerge))
    
    left_list = listToMerge[0:middle_pos] # split the lists by the middle position.
    right_list = listToMerge[middle_pos:len(listToMerge)]
    
    
    logging.debug("left list is : {0}, right list is : {1}".format(left_list, right_list))

    left_list = mergeSort(left_list, eval)
    right_list = mergeSort(right_list, eval)
    
    logging.debug("POST MERGE_SORT: left list is : {0}, right list is : {1}".format(left_list, right_list))
    
    result = merge(left_list, right_list, eval)
    
    return result
 
"""
Creates a new list which is the sorted, merged, result of two lists.
"""
def merge(left_list, right_list, eval):
    result = []
    logging.debug("MERGE: left list is {0}, right list is {1}".format(left_list, right_list))
    while len(left_list) > 0 or len(right_list) > 0:
        
        if len(left_list) > 0 and len(right_list) > 0:
            eval.incrementMoves()
            eval.incrementComparisons()
            if left_list[0] <= right_list[0]:
                result.append(left_list[0])
                left_list = left_list[1:]
            else:
                result.append(right_list[0])
                right_list = right_list[1:]
        elif len(left_list) > 0:
            eval.incrementMoves()
            result = result + left_list
            break
        elif len(right_list) > 0:
            eval.incrementMoves()
            result = result + right_list
            break
        
    logging.debug("MERGE RESULT: {0}".format(result))
    return result

if __name__ == '__main__':
    example = [2, 5, 2, 8, 1, 4, 9, 20, 0]
    
    logging.basicConfig(level=logging.DEBUG) #DEBUG
    
    eval= Monitoring.Monitor()
    
    print "Before : ", example
    result = mergeSort(example, eval)
    print "After : ", result
    print "Number of comparisons: {0}\nNumber of moves: {1}".format(eval.numberOfComparisons, eval.numberOfMoves)  