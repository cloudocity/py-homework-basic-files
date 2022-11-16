class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        pass

    def __iter__(self):
        self.item = []
        self.counter = 0
        self.iter = 0
        return self

    def __next__(self):
        #self.counter += 1
        if self.counter < len(self.list_of_list):
            if self.iter < len(self.list_of_list[self.counter]):
                #print(self.iter , self.counter)
                for value in self.list_of_list[self.counter]:
                    print(value)
                    #print(self.list_of_list[self.iter])
                    #for symbol in value:
                    self.iter += 1
                    #return value
                    #print(symbol)
                #self.counter += 1
                #self.item.append(value)
                    #return value
                #print(value)
            #self.counter += 1
            else:
                self.counter += 1
                self.iter = 0
        else:
            raise StopIteration
        #return symbol
        # elif self.counter == len(self.list_of_list):
        #     self.counter += 1
        self.counter += 1
        #raise StopIteration
        # #     return self.item
        # else:
        #     raise StopIteration
        #return self.item


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

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    #test_1()
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]
    for item in FlatIterator(list_of_lists_1):
        print(item)
