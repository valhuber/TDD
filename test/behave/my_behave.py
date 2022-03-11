#!/usr/bin/env python

# -*- coding: utf-8 -*-
# ASSUMPTION: behave is installed.

# shoutout: https://github.com/behave/behave/issues/709

import sys
from behave.__main__ import main as behave_main  # behave is pip'd...

if __name__ == "__main__":
    sys.exit(behave_main())