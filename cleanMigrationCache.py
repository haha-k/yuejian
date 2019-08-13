

import os
import shutil

dirname = os.listdir('.')

print(dirname)

for dir in dirname:
    path = os.path.join('E:\yuejian3\\',dir)
    if os.path.isdir(path):
        for dirs in os.listdir(path):
            if dirs=='migrations':
                print(os.path.join(path,dirs))
                shutil.rmtree(os.path.join(path,dirs))





