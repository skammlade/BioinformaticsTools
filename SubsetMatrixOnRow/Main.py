from SubsetMatrixOnRow import SubsetMatrixOnRow
import sys, argparse

parser = argparse.ArgumentParser(description='=====\n SubsetMatrixOnRow: Subset a matrix on column headers. \n ===== ', epilog="===== \n Find more tools like this written by Sara at https://github.com/skammlade/BioinformaticsTools \n =====")

# parser.add_argument("-inputFile", "-i", type=str, #nargs='+',
#                     help='Matrix text file path.')

# parser.add_argument("-delimiter", "-d", type=str, #nargs='+',
#                     help='Matrix text file path.')

# parser.add_argument("-columnHeaders", "-c", type=str, #nargs='+',
#                     help='Matrix text file path.')

# parser.add_argument("-outputFile", "-o", type=str, #nargs='+',
#                     help='Matrix text file path.')

requiredNamed = parser.add_argument_group('required named arguments')

requiredNamed.add_argument('-inputFile','-i', type=str, required=True,
                    help='Matrix text file path.')

requiredNamed.add_argument('-delimiter', '-d', type=str, default="/t", required=True,
                    help='The matrix file delimiter (e.g. \"\\t\" for tab; "," for comma). Default is tab delimited.')

requiredNamed.add_argument('-columnHeaders', '-c', type=str, required=True,
                    help='The file path to a text file of column headers to use for subsetting.')

requiredNamed.add_argument('-outputFile', '-o', type=str, default="subsettedMatrix.txt", required=True,
                    help='The file path for the resulting subsetted matrix.')

args = parser.parse_args()

print(args)


sm=SubsetMatrixOnRow(args.inputFile,args.columnHeaders,2,bytes(args.delimiter, 'utf-8').decode('unicode_escape'))

# sm=SubsetMatrixOnRow(sys.argv[1],sys.argv[2], "\t")
# sm=SubsetMatrixOnRow(("col1","col3"),"testData.txt", "\t")


sm.writeOutputFile(args.outputFile)
# sm.writeOutputFile("testOutput.txt")
