from SubsetMatrixOnRow import SubsetMatrixOnRow
import sys, argparse

parser = argparse.ArgumentParser(description='=====\n SubsetMatrixOnRow: Subset a matrix on rows. \n ===== ', epilog="===== \n Find more tools like this at https://github.com/skammlade/BioinformaticsTools \n =====")

requiredNamed = parser.add_argument_group('required named arguments')

requiredNamed.add_argument('-inputFile','-i', type=str, required=True,
                    help='Matrix text file path.')

requiredNamed.add_argument('-delimiter', '-d', type=str, default="/t", required=True,
                    help='The matrix file delimiter (e.g. \"\\t\" for tab; "," for comma). Default is tab delimited.')

requiredNamed.add_argument('-referenceColumnHeaders', '-r', type=str, required=True,
                    help='The file path to a text file of column headers to use for subsetting.')

requiredNamed.add_argument('-outputFile', '-o', type=str, default="subsettedMatrix.txt", required=True,
                    help='The file path for the resulting subsetted matrix.')

args = parser.parse_args()

sm=SubsetMatrixOnRow(args.inputFile,args.referenceColumnHeaders,2,bytes(args.delimiter, 'utf-8').decode('unicode_escape'))

sm.writeOutputFile(args.outputFile)

