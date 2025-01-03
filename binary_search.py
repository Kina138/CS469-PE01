class BinarySearchClass:
    def __init__(self, name_list):
        self.name_list = name_list

    def binary_search(self, searching_item):
        left, right = 0, len(self.name_list) - 1
        while left <= right:
            mid = (left + right) // 2  # Find the middle index
            if self.name_list[mid] == searching_item:
                return mid  # Found the name
            elif self.name_list[mid] < searching_item:
                left = mid + 1  # Search in the right half
            else:
                right = mid - 1  # Search in the left half
        raise ValueError(f"{searching_item} not found in the list")  # Name not found
