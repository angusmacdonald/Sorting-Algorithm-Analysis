import selectionsort
import mergesort
import insertionsort
import bubblesort
import Monitoring


def Sort(list, sortingAlgorithm, eval=Monitoring.Monitor()):
    print "Using {0} algorithm".format(sortingAlgorithm.__name__)
    print "About to sort : \t", list
    list = sortingAlgorithm(list, eval)
    print "Sorted : \t\t", list
    print "\tNumber of comparisons: \t{0}\n\tNumber of moves: \t{1}\n".format(eval.numberOfComparisons, eval.numberOfMoves)  
    return list 

def SelectionSort(list, eval= Monitoring.Monitor()):
    return Sort(list, selectionsort.selectionSort, eval)

def InsertionSort(list, eval= Monitoring.Monitor()):
    return Sort(list, insertionsort.insertionSort, eval)

def MergeSort(list, eval= Monitoring.Monitor()):
    return Sort(list, mergesort.mergeSort, eval)