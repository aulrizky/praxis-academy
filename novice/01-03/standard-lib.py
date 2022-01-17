# import os
# os.getcwd

# os.getcwd()
# '/home/aul'

# dir(os)

# >>> import shutil
# >>> shutil.copyfile('data.db', 'archive.db')
# 'archive.db'
# >>> shutil.move('/build/executables', 'installdir')
# 'installdir'

# import glob
# glob.glob('*.py')

# import sys
# >>> print(sys.argv)

# import argparse

# parser = argparse.ArgumentParser(prog = 'top',
#     description = 'Show top lines from each file')
# parser.add_argument('filenames', nargs='+')
# parser.add_argument('-l', '--lines', type=int, default=10)
# args = parser.parse_args()
# print(args)


# >>> import math
# >>> math.cos(math.pi/4)
# 0.7071067811865476
# >>> math.log(1024, 2)
# 10.0
# >>> 


import random
print(random.choice(['apple', 'pear', 'banana']))

random.sample(range(100), 10) 
random.random() 
random.randrange(6)

import statistics
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
statistics.mean(data)

statistics.median(data)
statistics.variance