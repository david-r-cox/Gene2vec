#!/usr/bin/python2.7
# David Cox 2016
import os
from sys import argv
from pprint import pprint
from multiprocessing import Pool

'''
Calculates some rudimentary statistics on genomic data.
'''

N = 'ATCG' # nucleotides
C = [n_0 + n_1 + n_2 for n_0 in N for n_1 in N for n_2 in N] # codons
three_chains = [c_0 + c_1 + c_2 for c_0 in C for c_1 in C for c_2 in C]

def argcheck():
    if len(argv) != 2:
        print('./simple_stats.py <input directory>')
        exit(1)
    if not os.path.isdir(argv[1]):
        print('Input directory not found or does not exist.')
        exit(1)
    return

def read_file(filepath):
    try: file_data = open(filepath, 'r').read()
    except: file_data = None
    return file_data.replace('\n','')

def import_samples():
    sample_db = {}
    for filename in os.listdir(argv[1]):
        if filename not in sample_db:
            filepath = argv[1] + '/' + filename
            sample_db[filename] = read_file(filepath)
    return sample_db

def get_nucleotide_stats(sample):
    num_A, num_T, num_C, num_G = (0,)*4
    for nucleotide in sample:
        if nucleotide == 'A': num_A += 1
        elif nucleotide == 'T': num_T += 1
        elif nucleotide == 'C': num_C += 1
        elif nucleotide == 'G': num_G += 1
    total = float(sum([num_A, num_T, num_C, num_G]))
    stats = { 'Nucleotide Counts' : {
                    'A' : num_A,
                    'T' : num_T,
                    'C' : num_C,
                    'G' : num_G,
                    'Total' : total
              },
              'Nucleotide Ratios' : {
                    'A' : num_A / total,
                    'T' : num_T / total,
                    'C' : num_C / total,
                    'G' : num_G / total,
              }
            }

    return stats

def chain_counts(sample):
    counts = {}
    for codon in window(9, sample):
        try: counts[codon.rstrip()] += 1
        except: counts[codon.rstrip()] = 1
    return counts

def chain_ratios(counts):
    total_chains = float(sum([counts[chain] for chain in counts.keys()]))
    codon_chain_ratios = { chain : (counts[chain] / total_chains) for chain in counts.keys()}
    return codon_chain_ratios      


def print_sample_stats(sample, name):
    counts = chain_counts(sample)
    sample_stats = { 'Sample' : name, 'Stats' :
	{ 'Nucleotide Stats' : get_nucleotide_stats(sample),
            'Codon Chain Counts' : sorted(counts.items(), key=lambda x: (x[1],x[0]), reverse=True)[:5],
            'Codon Chain Ratios' : sorted(chain_ratios(counts).items(), key=lambda x: (x[1],x[0]), reverse=True)[:5],
	} }
    pprint(sample_stats)

def window(length, data):
    for i in xrange(len(data) - length): yield data[i:i+length]

def main():
    argcheck()
    sample_db = import_samples()

    for filename in sample_db.keys():
        print_sample_stats(sample_db[filename], filename)


if __name__ == "__main__":
    main()
