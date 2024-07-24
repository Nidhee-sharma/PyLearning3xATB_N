#walk me in current drectoty  wal IN dir

import os

for root ,dir,files in os.walk("C:\\Users\\lenovo\\FirstPycharmProjects\\PyLearning3xATB\\05072024"):
    print(f'current dir{root}')
    print(f'sub dir dir{dir}')
    print(f'files dir{files}')
    print(len(files))

