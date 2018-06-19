class SubsetMatrix:

	def __init__(self, inputFile, headerFile, delimiter="\t"): # constructor
		self.columnsToKeepDictionary = self.__parseHeaderFile(headerFile)
		self.inputFile = inputFile
		self.delimiter = delimiter

	def __parseHeaderFile(self, headerFile):
		columnsToKeepDictionary = {}
		with open(headerFile) as headerFileHandle:
			for line in headerFileHandle:
				line = line.rstrip()
				columnsToKeepDictionary[line] = True
				print("adding line to dic: "+line)
		print(columnsToKeepDictionary)
		return columnsToKeepDictionary
		
	def writeOutputFile (self,outputFile):
	
		outputFileHandle=open(outputFile, "w")
		
		with open(self.inputFile) as inputFileHandle:
			headerRow = inputFileHandle.readline()
			columnBitArray = self.__getColumnBitArray(headerRow)
			print(columnBitArray)
			outputFileHandle.write(self.__processRow(headerRow, columnBitArray) + "\n")
			for line in inputFileHandle:
				outputFileHandle.write(self.__processRow(line, columnBitArray) + "\n")

		outputFileHandle.close
		
	def __getColumnBitArray(self, headerRow):
		returnValue = []
		headerRow = headerRow.rstrip()
		headerRowArray = headerRow.split(self.delimiter)
		for headerValue in headerRowArray:
			print(headerValue)
			if headerValue in self.columnsToKeepDictionary:
				print("in dictionary")
				returnValue.append(True)
			else:
				print("NOT in dictionary")
				returnValue.append(False)
		return returnValue

	def __processRow(self, row, columnBitArray):
		returnValue = [] #empty list
		
		row = row.rstrip()

		splitRow = row.split(self.delimiter)

		for value, columnBit in zip(splitRow, columnBitArray):
			if columnBit is True:
				returnValue.append(value)

		return self.delimiter.join(returnValue)
	 
	