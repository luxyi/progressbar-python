#!/usr/bin/python

import os
import sys

module_path = os.path.join(os.path.dirname(__file__), '..', 'src')
sys.path.append(module_path)

import progressbar

items_count = 10000
progress_bar = progressbar.ProgressBar(items_count)
for i in xrange(items_count):
    progress_bar.update()
print ''
