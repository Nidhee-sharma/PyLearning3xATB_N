my_dict = {'a': 1, 'b': 2, 'w':5,'c': 3}
print(my_dict)

for k,v in  list(my_dict.items()):
    print(k,v)

from collections import OrderedDict
my_dict = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(my_dict)

#dict -It will not keep the order of elements
my_dict = {'a': 1, 'b': 2, 'c': 3}
#ordered dict - It will keep the order of elements
from collections import OrderedDict
my_dict = OrderedDict([('a', 1), ('b', 2), ('c', 3)])