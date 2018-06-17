from SubsetMatrix import SubsetMatrix

sm=SubsetMatrix(("col1","col3"),"testData.txt", "\t")

sm.writeOutputFile("testOutput.txt")

# print (sm.processRow("foo\tbar\tduck",(True,False,True))