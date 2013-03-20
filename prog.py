__author__ = 'minya'

import Image
import sys
import util
import os

i_dir = sys.argv[1]
o_dir = sys.argv[2]
for file in os.listdir(i_dir):
    i_fname = os.path.join(i_dir, file)
    img = Image.open(i_fname, "r")
    box = int(640), int(480)
    o_fname = os.path.join(o_dir, file)
    print "converting %s out to %s ..." % (i_fname, o_fname)
    util.resize(img, box, False, o_fname)
print "done."
