#You want to create a frequency counter for a string
#E.g. for string 'iiloveeny' - {'i' : 2, 'l' : 1, 'o' : 1, 'v' : 1, 'e' : 2, 'n' : 1, 'y' : 1}
s = 'iiloveeny'
#First Way
def classic_dict_check(s):
    dicti = {}
    for i in s:
        if i in dicti:
            dicti[i] += 1
        else:
            dicti[i] = 1
    return dicti

def dicti_get_method(s):
    dicti = {}
    for i in s:
        dicti[i] = 1 + dicti.get(i, 0)
    return dicti

from collections import defaultdict
def default_dict(s):
    dicti = defaultdict(int)
    for i in s:
        dicti[i] += 1
    return dicti

from collections import Counter
def counter_method(s):
    return Counter(s)


