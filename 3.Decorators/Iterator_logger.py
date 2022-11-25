import datetime


def logger(old_function):
    def new_function(*args, **kwargs):
        with open("main.log", "a", encoding="utf8", newline='') as f:
            now = datetime.datetime.now()
            str = old_function(*args, **kwargs)
            data_str = f'{now},{old_function.__name__},{kwargs},{args},{str}\n'
            f.write(data_str)
        return str
    return new_function

class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.joinedlist = []
        for i in self.list_of_list:
            self.joinedlist = self.joinedlist + i
        return iter(self.joinedlist)

@logger
def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        print(flat_iterator_item,check_item)
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
