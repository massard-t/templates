# bpm

Bob's Template Manager


## Description

bpm is inspired by other template manager (such as cookiecutter).
It aims to be a lot simpler, have less feature, and mostly only work with local
templates.

## Usage

```bash
$ bpm flask
```

## File example


### Python

```
#!/usr/bin/env {{python_interp}}
# coding: utf-8
"""
{{project_name}}

TODO: Write description
"""
import os
import sys


__author__ = "{{author}}" # Configuration file ?


def main():
    pass


if __name__ == '__main__':
    main()
```
