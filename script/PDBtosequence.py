from modeller import *
# Get the sequence of the 6eqeA PDB file, and write to an alignment file
code = '6eqe.pdb'

e = environ()
m = model(e, file=code)
aln = alignment(e)
aln.append_model(m, align_codes=code)
aln.write(file=code+'.seq')