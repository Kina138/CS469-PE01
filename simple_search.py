class SimpleSearchClass:
    def __init__(self, name_list):
        self.name_list = name_list

    def simple_search(self, searching_item):
        for index, name in enumerate(self.name_list):
            if name == searching_item:
                return index  # Found the name, return its index
        raise ValueError(f"{searching_item} not found in the list")  # Name not found