"""  Run whatever I'm doing at the time

Stuff in here probably belongs elsewhere.
"""

# run script from galleries folder
import sys

# fixme, make it md2py 
import md2py
import json2py
import show

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-t', '--time',
                    default=10, type=int,
                    help='time for slideshow in minutes')
parser.add_argument('-f', '--folder',
                    default='.',
                    help="folder of slides")
parser.add_argument('-s', '--slides',
                    default='slides.txt',
                    help='list of slides to show')

args = parser.parse_args()

folder = args.folder
infile = args.slides

msg = open(infile)

mj = md2py

if infile.endswith('json'):
    mj = json2py
    msg = open(infile).read()

slides = mj.interpret(msg)

print(slides[:5])

ss = show.SlideShow()

ss.interpret(dict(slides=slides, captions=folder))

ss.set_duration(args.time * 60)

print('wait:', ss.wait)

ss.run()