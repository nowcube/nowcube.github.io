import os

for root,dirs,files in os.walk('.'):
    print(root)
    # print('---')
    # print(dirs)
    # print('---')
    # print(files)
    os.chdir(r'{}'.format(root))
    # os.system("cd {}".format(root))
    os.system("dir")
    os.system("cd {}".format(os.path.pardir))

    # os.system("cd ../")
    