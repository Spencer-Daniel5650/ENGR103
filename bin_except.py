# Author: Daniel Spencer
# GitHub Username: Spencer-Daniel5650
# Date: 1/23/2024
# Description: Creates a binary search and returns an exception when target is not found

def binary_search(a_list, target):
  """
  Searches a_list for an occurrence of target
  If found, returns the index of its position in the list
  If not found, returns -1, indicating the target value isn't in the list
  """

  class TargetNotFound(Exception):
      """Exception raised when the target is not found in the list."""

      def __init__(self, message="Target value not found in the list"):
          self.message = message
          super().__init__(self.message)

  def binary_search(a_list, target):
      first = 0
      last = len(a_list) - 1

      while first <= last:
          middle = (first + last) // 2
          if a_list[middle] == target:
              return middle
          elif a_list[middle] > target:
              last = middle - 1
          else:
              first = middle + 1

      raise TargetNotFound