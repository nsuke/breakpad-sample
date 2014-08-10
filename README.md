### Build
```
$ gn gen out/Debug --args=is_debug=true
$ ninja -C out/Debug
```

### Generate symbols
```
$ cd out/Debug
$ ../../dump_syms.py breakpad-example
```

### Crush
```
$ ./breakpad-example
```

### View minidump
```
$ ./minidump_stackwalk -m <dump path> ./symbols
```
