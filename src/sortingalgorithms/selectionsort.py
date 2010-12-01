import Monitoring

'''
Selection sort looks for the minimum value in the loop, then swaps this with the first element.
It then loops round again from the second element (and so on) doing the same thing.

Wikipedia: Insertion sort is very similar in that after the kth iteration, the first k elements in the array are in sorted order. 
Insertion sort's advantage is that it only scans as many elements as it needs in order to place the k + 1st element,
 while selection sort must scan all remaining elements to find the k + 1st element.

Worst case performance    O(n2)
Best case performance    O(n2)
Average case performance O(n2)
Worst case space complexity    O(n) total, O(1) auxiliary
'''
def selectionSort(array, eval=Monitoring.Monitor()):
    pos = 0
    min = 0
     
    # advance the position through the entire array
    for pos in range(0, len(array)):
      #find the min element in this iteration of the array

      min = pos # assume the min is the first element
      #test against all other elements 
      for i  in range (pos+1, len(array)):
          #if this element is less, then it is the new minimum 
          eval.incrementComparisons()
          if array[i] < array[min]:
              # found new minimum; remember its index
              min = i;

      # min is the index of the minimum element. Swap it with the current position */
      swap(array, pos, min, eval);
    return array

def swap(list, first, second, eval):
    list[first], list[second] = list[second], list[first]
    eval.incrementMoves()

if __name__ == '__main__':
    example = [2,6,7,2,6,9,9,1,1,5]
    eval= Monitoring.Monitor()
    print "Before : ", example
    selectionSort(example, eval)
    print "After : ", example
    
    print "Number of comparisons: {0}\nNumber of moves: {1}".format(eval.numberOfComparisons, eval.numberOfMoves)