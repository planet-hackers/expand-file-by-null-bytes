# expand-file-by-null-bytes

Script to expand a target file by appending NULL bytes to it until it reaches the desired given size in bytes.

## Usage

I created a `say-fuck` executable in C which outputs `fuck`

```
% ./say-fuck
fuck
```

The current size of the file is 16704 bytes

```
% stat say-fuck | grep -i size | cut -d " " -f 4
16704
```

I want my file to have a size of 17000 bytes so I run the script

```
% python3 expand-file-by-null-bytes.py "./say-fuck" 17000
expanding file by 296 bytes
```

Check the new size of the file

```
% stat say-fuck | grep -i size | cut -d " " -f 4
17000
```

Great! Now does it still run correctly?

```
% ./say-fuck
fuck
```

Yep. Cool.
