class SubsetMatrix:

	def __init__(self, columnsToKeep, inputFile, delimiter="\t"): # constructor
		self.columnsToKeepDictionary = {}
		for column in columnsToKeep:
			self.columnsToKeepDictionary[column] = True
		self.inputFile = inputFile
		self.delimiter = delimiter
		
	def writeOutputFile (self,outputFile):
	
		outputFileHandle=open(outputFile, "w")
		
		with open(self.inputFile) as inputFileHandle:
			headerRow = inputFileHandle.readline()
			columnBitArray = self.__getColumnBitArray(headerRow)
			outputFileHandle.write(self.__processRow(headerRow, columnBitArray) + "\n")
			for line in inputFileHandle:
				outputFileHandle.write(self.__processRow(line, columnBitArray) + "\n")

		outputFileHandle.close
		
	def __getColumnBitArray(self, headerRow):
		returnValue = []
		headerRowArray = headerRow.split(self.delimiter)
		for headerValue in headerRowArray:
			if headerValue in self.columnsToKeepDictionary:
				returnValue.append(True)
			else:
				returnValue.append(False)
		return returnValue

	def __processRow(self, row, columnBitArray):
		returnValue = [] #empty list
		
		splitRow = row.split(self.delimiter)
		
		for value, columnBit in zip(splitRow, columnBitArray):
			if columnBit is True:
				returnValue.append(value)

		return self.delimiter.join(returnValue)
	 
	