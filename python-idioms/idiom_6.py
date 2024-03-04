d = {'a':'5'}

try:
  value = int(d['a'])
except(KeyError,ValueError):
  value = None