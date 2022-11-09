from pprint import pprint
import csv
import re
import itertools


dict_book = {}
with open("phonebook_raw.csv",encoding="utf8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
header = contacts_list[0]

contacts_list.pop(0)
for row in contacts_list:
    dict_list_book ={}
    LFSname = row[0] + ' ' + row[1] + ' ' + row[2]
    organization = row[3]
    position = row[4]
    phone = row[5]
    items =  re.findall(r"(\d{1})", phone)
    dopphone = re.findall(r"доб\. (\d+)", phone)
    email = row[6]
    list_LFS = LFSname.split()
    if len(list_LFS) > 2:
        dict_list_book['lastname'] = list_LFS[0]
        dict_list_book['firstname'] = list_LFS[1]
        dict_list_book['surname'] = list_LFS[2]
    else:
        dict_list_book['lastname'] = list_LFS[0]
        dict_list_book['firstname'] = list_LFS[1]
    if organization:
        dict_list_book['organization'] = organization

    if position:
        dict_list_book['position'] = position

    if phone:
        if dopphone:
            phonenew = '+7' + '(' + items[1] + items[2] + items[3] + ')'+ items[4] + items[5] + \
                   items[6] + '-' + items[7] + items[8] + '-' + items[9] + items[10] + ' доб.' + dopphone[0]

        else:
            phonenew = '+7' + '(' + items[1] + items[2] + items[3] + ')' + items[4] + items[5] + \
                   items[6] + '-' + items[7] + items[8] + '-' + items[9] + items[10]

        dict_list_book['phone'] = phonenew

    if email:
        dict_list_book['email'] = email

    if dict_list_book['lastname'] in dict_book:
        dict_book[dict_list_book['lastname']].update(dict_list_book)
    else:
        dict_book[dict_list_book['lastname']] = dict_list_book

contacts_list=[]
contacts_list.append(['lastname', 'firstname', 'surname', 'organization', 'position', 'phone', 'email'])

for value in dict_book.values():
    list_LFS = []
    if 'surname' in value:
        i=0
    else:
        value['surname'] = 'null'
    if 'organization' in value:
        i = 0
    else:
        value['organization'] = 'null'
    if 'position' in value:
        i = 0
    else:
        value['position'] = 'null'
    if 'phone' in value:
        i = 0
    else:
        value['phone'] = 'null'
    if 'email' in value:
        i = 0
    else:
        value['email'] = 'null'
    list_LFS.append(value['lastname'] + ',' + value['firstname'] + ',' + value['surname'] + ',' + value['organization'] + ',' + value['position'] + ',' + value['phone'] + ',' + value['email'])
    split_list = list_LFS[0].split(",")
    contacts_list.append(split_list)
print(contacts_list)


with open("phonebook.csv", "w",encoding="utf8",newline='') as f:
      datawriter = csv.writer(f, delimiter=',')
      datawriter.writerows(contacts_list)


