import numpy

a = {"a": "hola"}
b = {"b": "adios"}
ak = a.keys()
av = a.values()
bk = b.keys()
bv = b.values()
ak.concatenate(bk)
print(ak)
