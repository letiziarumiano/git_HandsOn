#!/usr/bin/env python

import sys, re
from argparse import ArgumentParser

<<<<<<< HEAD
parser = ArgumentParser(description="Classify a sequence as DNA or RNA and search for motifs")

# Create the ArgumentParser object
parser = ArgumentParser(description="Classify a sequence as DNA or RNA and search for motifs")

# Add arguments for the sequence and motif
>>>>>>> motif
parser.add_argument("-s", "--seq", type=str, required=True, help="Input sequence")
parser.add_argument("-m", "--motif", type=str, required=False, help="Motif")

# Parse the arguments
args = parser.parse_args()

<<<<<<< HEAD
args.seq = args.seq.upper()

# Convert sequence to uppercase
args.seq = args.seq.upper()
>>>>>>> motif

# Classify the sequence as DNA, RNA, or both
if re.search('^[ACGTU]+$', args.seq):
    if re.search('T', args.seq):
        print('The sequence is DNA')
    elif re.search('U', args.seq):
        print('The sequence is RNA')
    else:
        print('The sequence can be DNA or RNA')
else:
    print('The sequence is not DNA nor RNA')

# If a motif is provided, search for it in the sequence
if args.motif:
    args.motif = args.motif.upper()
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end='')
    if re.search(args.motif, args.seq):
        print("FOUND")
    else:
<<<<<<< HEAD
        print("Motif not found!")

        print("NOT FOUND")
>>>>>>> motif
