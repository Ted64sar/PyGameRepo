import argparse
parser = argparse.ArgumentParser()

parser.add_argument('--upper', action='store_true')
parser.add_argument('--lines', type=int, default=0)
parser.add_argument(dest='file1', type=argparse.FileType('r'))
parser.add_argument(dest='file2', type=argparse.FileType('w+'))
arguments = parser.parse_args()
lines = arguments.file1.readlines()

if arguments.upper:
    for i in range(len(lines)):
        lines[i] = lines[i].upper()

if arguments.lines != 0:
    if arguments.lines < len(lines):
        lines = '\n'.join(lines[0:arguments.lines:1])


for i in range(len(lines)):
    arguments.file2.write(lines[i])
arguments.file2.close()
arguments.file1.close()