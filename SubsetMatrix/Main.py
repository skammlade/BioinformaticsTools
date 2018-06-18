from SubsetMatrix import SubsetMatrix
import sys

sm=SubsetMatrix(sys.argv[1],sys.argv[2], "\t")
# sm=SubsetMatrix(("col1","col3"),"testData.txt", "\t")

sm.writeOutputFile("testOutput.txt")
