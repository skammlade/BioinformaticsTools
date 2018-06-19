# Bioinformatics Tools

- [Manipulating genome matrices](#Manipulating-genome-matrices)  
	* [SubsetMatrix](#SubsetMatrix)  
	* [ConsolidateMatrixToUniqueRows](#ConsolidateMatrixToUniqueRows)  
	* [TransposeMatrix](#TransposeMatrix)  
	* [MultiFastaFromMatrix](#MultiFastaFromMatrix)  
	
## Manipulating genome matrices

### SubsetMatrix

This subsets a matrix based on column header. 

My original purpose was for use in subsetting genome matrices which look like:

```
Chromosome	Coordinate	sample1	sample2	sample3
```

Running the program

```sh
python Main.py -i inputFile.txt -d "/t" -c columnHeaders.txt -o subsettedMatrix.txt
```

```
Usage: python Main.py [options]

  -inputFile, -i		The matrix file in text format.

  -delimiter, -d		The matrix file delimiter
                		(e.g. "\t" for tab, "," for comma).
				
  -columnHeader, -c		A text file with column headers to use for subsetting.
						Single column, one header per line.

  -outputFile, -o 		The output file for the resulting subsetted matrix.
```

### ConsolidateMatrixToUniqueRows

This removes rows from a matrix that contain the same value across all columns, keeping only rows that are not homogenous across columns.

### TransposeMatrix

This transposes columns to rows, rows to columns.

### MultiFastaFromMatrix

This takes a matrix that looks like

 [sampleID	locus1	locus2	locus3]
 
 And generates a multi-fasta text file that looks like
 
 