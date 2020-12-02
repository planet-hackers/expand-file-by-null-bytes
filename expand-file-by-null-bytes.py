import sys
import os

USAGE = 'python3 expand-file-by-null-bytes.py [FILE-PATH] [NEW-FILE-SIZE-IN-BYTES]'

args = sys.argv[1:]
if len(args) != 2:
    print(USAGE)
    exit(1)

file_path = args[0]

try:
    new_file_size = int(args[1])
except Exception as e:
    print('invalid number for file size')
    exit(1)

try:
    file_stat = os.lstat(file_path)
except Exception as e:
    print(e)
    exit(1)

if file_stat.st_size == new_file_size:
    print('the given file already has a size of %d bytes' % new_file_size)
    exit(0)

if file_stat.st_size > new_file_size:
    print('can''t expand. the given file has a size of %d bytes which is larger than the desired new size of %d byes' % (
        file_stat.st_size, new_file_size))
    exit(1)

num_nullbytes_to_expand_by = new_file_size - file_stat.st_size

print('expanding file by %d bytes' % num_nullbytes_to_expand_by)

with open(file_path, 'ab') as f:
    f.write(b'\x00' * num_nullbytes_to_expand_by)
