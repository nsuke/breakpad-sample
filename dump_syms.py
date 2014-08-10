#!/usr/bin/env python
import os
import re
import shutil
import subprocess
import sys


if __name__ == '__main__':
  target = sys.argv[1]
  sym_filename = target + '.sym'
  o, _ = subprocess.Popen(['./dump_syms', target],
      stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
  m = re.search('^MODULE \w+ \w+ ([A-Z0-9]+)', o.splitlines()[0])
  num = m.group(1)
  sym_dir = os.path.join('symbols', target, num)
  os.makedirs(sym_dir)
  with open(os.path.join(sym_dir, sym_filename), 'w') as fp:
    fp.write(o)
  sys.exit(0)
