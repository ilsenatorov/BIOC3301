#!/usr/bin/python

### This scripts filters through a fasta file and returns only sequences with a certain barcode id

import argparse

parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("-b", help="number of barcode ID, for 515rcbc20 it will be 20", type=str)
parser.add_argument("-i", help="location of original sequence file", type=str)
parser.add_argument("-o", help="name and location of the output file", type=str)
args = parser.parse_args()

barcode = '515rcbc' + args.b
input_file = open(args.i, 'r')
inp = input_file.readlines()
output_file = open(args.o, 'w')
for line in inp:
    if barcode in line:
        output_file.write(line)
        output_file.write(inp[inp.index(line)+1])
input_file.close()
output_file.close()
