
"""
Approach 1: Store peek value 
store the next item as a variable and return it as peek value when needed.

TC: O(1)
SC: O(1)

"""
# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.peek_val = iterator.next()
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.peek_val
        

    def next(self):
        """
        :rtype: int
        """
        next_item = self.peek_val
        if self.iterator.hasNext():
            self.peek_val = self.iterator.next()
        else:
            self.peek_val = None
        return next_item
            
        

    def hasNext(self):
        """
        :rtype: bool
        """
        
        return self.peek_val is not None
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].