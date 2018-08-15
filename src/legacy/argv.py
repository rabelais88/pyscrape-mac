import sys

if len(sys.argv) > 1:
  customarg = sys.argv[1]
  print(customarg)
else:
  print('no argv detected')