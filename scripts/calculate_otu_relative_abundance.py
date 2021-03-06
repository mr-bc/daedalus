#!/usr/bin/env python 

from __future__ import division
import argparse

import numpy as np

from biom.parse import parse_biom_table as pbt



def parse_argument():
	parser = argparse.ArgumentParser()

	parser.add_argument("-i",help = "",required = True , dest = "otu_table_p" , type = str)
	parser.add_argument("-o",help = "The filename to where the results will be written to. ", default = ".", dest = "working_path", type = str)
	opt = parser.parse_args()

	return opt




def main():
	opt = parse_argument()

	biom_table = pbt(open(opt.otu_table_p,"r"))
	abundance = calculate_otu_relative_abundance(biom_table)
	print_relative_abundance_table(abundance,opt.working_path)

	return 




def calculate_otu_relative_abundance(biom_table):
	
	totalCount = biom_table.sum()

	abundance = []

	for otu in biom_table.iterObservations():
		element = (otu[1],otu[0].sum(),otu[0].sum()/totalCount)
		abundance.append(element)

	return abundance



def print_relative_abundance_table(abundance,filep):
	head = "OTU\tABUNDANCE\tRELATIVE_ABUNDANCE\n"
	tmpl = "{}\t{}\t{}\n"

	doc = open(filep,"w")
	doc.write(head)
	for e in abundance:
		doc.write(tmpl.format(*e))

	doc.close()
	return 



if __name__ == "__main__":
	main()