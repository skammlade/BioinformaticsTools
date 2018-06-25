class SubsetMatrixOnRow:

	def __init__(self, inputFile, headerFile, columnOffset, delimiter="\t"): # constructor
		self.columnsToKeepDictionary = self.__parseHeaderFile(headerFile)
		self.inputFile = inputFile
		self.delimiter = delimiter
		self.columnOffset = columnOffset
		self.indexOfReferenceColumn = None # no guarantee *which* reference column

	def __parseHeaderFile(self, headerFile):
		columnsToKeepDictionary = {}
		with open(headerFile) as headerFileHandle:
			for line in headerFileHandle:
				line = line.rstrip()
				columnsToKeepDictionary[line] = True
				# print("adding line to dic: "+line)
		# print(columnsToKeepDictionary)
		return columnsToKeepDictionary
		
	def writeOutputFile (self,outputFile):
	
		outputFileHandle=open(outputFile, "w")
		
		with open(self.inputFile) as inputFileHandle:
			headerRow = inputFileHandle.readline()
			columnBitArray = self.__getReferenceColumnBitArray(headerRow)
			# print(columnBitArray)
			outputFileHandle.write(headerRow)
			for line in inputFileHandle:
				if self.__checkRow(columnBitArray, line):
					outputFileHandle.write(line + "\n")
		outputFileHandle.close
		
	def __getReferenceColumnBitArray(self, headerRow):
		returnValue = []
		headerRow = headerRow.rstrip()
		headerRowArray = headerRow.split(self.delimiter)

		for index, headerValue in enumerate(headerRowArray[self.columnOffset:]):
			# print(headerValue)
			if headerValue in self.columnsToKeepDictionary:
				# print("in dictionary")
				returnValue.append(True)
				self.indexOfReferenceColumn = index
			else:
				# print("NOT in dictionary")
				returnValue.append(False)
		return returnValue


	def __processRow(self, row):
		row = row.rstrip()

		return row

	def __checkRow(self, columnBitArray, row):
		# get value in cell of first reference column

		rowArray = row.split(self.delimiter)[self.columnOffset:]



		refValue = rowArray[self.indexOfReferenceColumn]
		# for all data columns, 
		for i, cellValue in enumerate(rowArray):
			if (cellValue == refValue) != columnBitArray[i]:
				return False
		return True

	 
	