import os
directory = 'sorted'

def count_line(directory):
    dict_count = {}
    for filename in os.listdir(directory):
        a = os.path.join(directory, filename)
        if os.path.isfile(a):
            with open(a, 'r', encoding='UTF8') as f:
                count = 0
                for line in f:
                    count += 1
                    dict_count[filename] = count
    return(dict_count)

def sorted_dict(dict):
    sorted_values = sorted(dict.values())
    sorted_dict = {}

    for i in sorted_values:
        for k in dict.keys():
            if dict[k] == i:
                sorted_dict[k] = dict[k]
    return sorted_dict

def write_result(dict_sort_result,directory):
    for filename in dict_sort_result:
        a = os.path.join(directory, filename)
        if os.path.isfile(a):
            with open('result.txt', 'a', encoding='UTF8') as w:
                w.write(filename + '\n')
                w.write(str(dict_sort_result[filename]) + '\n')
                with open(a, 'r', encoding='UTF8') as f:
                    for line in f:
                        w.write(line + '\n')

dict_sort_result = sorted_dict(count_line(directory))
write_result(dict_sort_result, directory)




