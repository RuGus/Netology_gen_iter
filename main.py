nested_list = [
    ["a", "b", "c"],
    ["d", "e", "f"],
    [1, 2, None],
]


def flat_list(nested_list: list) -> list:
    """Flattening a non flat list

    Args:
        nested_list (list): non flat list

    Returns:
        list: flat list
    """
    flattening_list = []
    for element in nested_list:
        if isinstance(element, list):
            flattening_list += flat_list(element)
        else:
            flattening_list.append(element)
    return flattening_list

class FlatIterator:
    def __init__(self, nested_list):
        self.iterator_list = flat_list(nested_list)
        self.iterator_len = len(self.iterator_list) - 1

    def __iter__(self):
        self.start = -1
        return self

    def __next__(self):
        self.start += 1
        if self.start > self.iterator_len:
            raise StopIteration
        return self.iterator_list[self.start]


def flat_generator(nested_list):
    generator_list = flat_list(nested_list)
    for element in generator_list:
        yield element


if __name__ == "__main__":

    for item in FlatIterator(nested_list):
        print(item)

    for item in flat_generator(nested_list):
        print(item)
