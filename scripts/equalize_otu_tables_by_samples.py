#!/usr/bin/env python 

import os
import shutil as sh
import argparse

from biom.parse import parse_biom_table as pbt

import daedalus.lib.utils as du




def parse_argument():
	parser = argparse.ArgumentParser()

	parser.add_argument("-i",help = "",required = True , dest = "otu_table_p" , type = str)
	parser.add_argument("-r",help = "",required = True ,  dest = "reference_table_p",type = str)
	parser.add_argument("-n",help="",required = True , dest = 'seq_number',type = int)
	parser.add_argument("-o",help = "The filename to where the results will be written to. ", default = ".", dest = "working_path", type = str)
	parser.add_argument("-f",help = "force override of the output files if they exist", action='store_true' , dest = "override")
	opt = parser.parse_args()

	return opt



def main():

	opt = parse_argument()

	if not os.path.exists(opt.working_path):
		os.mkdir(opt.working_path)

	elif opt.override:
		sh.rmtree(opt.working_path)
		os.mkdir(opt.working_path)
	else:
		raise OSError(" File already exist!")


	du.equalize_tables_at_rarefaction_point(
		pbt(open(opt.otu_table_p,"r")),
		opt.otu_table_p.split(".biom")[0],
		pbt(open(opt.reference_table_p,"r")),
		opt.reference_table_p.split(".biom")[0],
		opt.seq_number,
		opt.working_path)

	pass

if __name__ == "__main__":
	main()
