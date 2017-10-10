remove_blocks_from_aln
======================
remove_blocks_from_aln is a tool to mask, remove or keep regions in an alignment. The regions are defined in an EMBL style tab-delimited file.

###Installation
Download the latest release from this github repository, or clone the repository. Then run the tests:

    python setup.py test
    
If the tests all pass, install:

    python setup.py install

###Usage
remove_block_from_aln.py [options]

	-a <file name>     alignment file name
	-o <file name>     output file name
	-t <file name>     tab file name (containing regions to keep/remove)
	-r <name>          reference name (optional, but required if there are gaps in the reference sequence relative to the tab file)
	-k                 keep regions in tab file (default is to mask them)
	-c                 cut regions in tab file (default is to mask them)
	-R                 do not remove blocks from reference sequence (default is to remove from all sequences)
	-s <N|X|?|->       Symbol to use for removed regions (default = N)
	-h                 Show help menu

###Inputs
####Alignment file
Alignment file must be in fasta format:

	>sequence1
	AAAATTTTCCCCGGGG
	>sequence2
	TTTTGGGGAAAACCCC

####Tab file
Tab file should emulate the EMBL file format, using only feature (FT) lines to define your regions:

	FT   misc_feature   5070..5095
	FT                   /note="26 bp;mummer_exact"
	FT   misc_feature   8163..8182
	FT                   /note="20 bp;mummer_exact"
	FT   misc_feature   9569..9588
	FT                   /note="20 bp;mummer_exact"
	
Note: while complemented regions can be handled, joins cannot and should be split into separate regions.

Build status: [![Build Status](https://travis-ci.org/sanger-pathogens/remove_blocks_from_aln.svg?branch=master)](https://travis-ci.org/sanger-pathogens/remove_blocks_from_aln)