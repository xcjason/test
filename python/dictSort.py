from collections import OrderedDict

D = OrderedDict()
D[6] = 'six'
D[1] = 'one'
print D
orderD = OrderedDict(sorted(D.items()))
print orderD