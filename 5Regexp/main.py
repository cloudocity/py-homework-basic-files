from pprint import pprint
import csv
import re
import itertools
dict_adressbook ={}
adressbook_all = {}
k=[]
with open("phonebook_raw.csv",encoding="utf8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
#pprint(contacts_list)
header = contacts_list[0]
contacts_list.pop(0)
for row in contacts_list:
  LFSname = row[0] + ' ' + row[1] + ' ' + row[2]
  #print(LFSname.split())
  list_LFS = LFSname.split()
  # if len(list_LFS) == 3:
  #   dict_adressbook = {
  #     'lastname' : list_LFS[0],
  #     'firstname' : list_LFS[1],
  #     'surname' : list_LFS[2]
  #   }
  # else:
  #   dict_adressbook['lastname'] = {
  #     'lastname' : list_LFS[0],
  #     'firstname' : list_LFS[1],
  #     'surname' : ''
  #   }
  # adressbook_all[list_LFS[0]] = dict_adressbook
  k.append(list_LFS)
k.sort()
#group = list(k for k,_ in itertools.groupby(k))
first_line = k[0]
k.pop(0)
for rows in k:
  print(first_line[0],rows[0])
  if first_line[0] == rows[0]:
    print(rows)

#pprint(k)

#pprint(adressbook_all)
  #dict_adressbook[LFSname.split()[0]] = LFSname.split()


# код для записи файла в формате CSV
# with open("phonebook.csv", "w") as f:
#   datawriter = csv.writer(f, delimiter=',')
#   # Вместо contacts_list подставьте свой список
#   datawriter.writerows(contacts_list)


