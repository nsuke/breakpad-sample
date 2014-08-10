#!/usr/bin/env python
import argparse
import os
import subprocess
import sys

root_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


def execute(cmd, cwd):
  sys.stdout.write('%s\n' % cmd)
  return subprocess.Popen(cmd, cwd=cwd).wait()


def patch(repo_dir, patch_file):
  cmd = [
    'patch',
    '-t',
    '-N',
    '-u',
    '-p0',
    '-d',
    repo_dir,
    '-i',
    patch_file
  ]
  return execute(cmd, repo_dir)


def svn_revert(repo_dir):
  cmd = [
    'svn',
    'revert',
    '-R',
    '.',
  ]
  return execute(cmd, repo_dir)


def main():
  p = argparse.ArgumentParser()
  p.add_argument('--revert', '-R', action='store_true')
  p.add_argument('--ignore-errors', '-I', action='store_true')
  args = p.parse_args()
  repo_dir = os.path.join(root_dir, 'build')
  if args.revert is True:
    res = svn_revert(repo_dir)
    return 0 if args.ignore_errors else res
  else:
    patch_file = os.path.join(root_dir, 'patches', 'build.patch')
    res = patch(repo_dir, patch_file)
    return 0 if args.ignore_errors else res
  return 1


if __name__ == '__main__':
  sys.exit(main())

