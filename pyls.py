import glob
files = glob.glob('./*')
for file in files:
    print file.split('/')[-1]