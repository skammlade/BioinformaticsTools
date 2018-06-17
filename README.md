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
chromosome	coordinate	sample1ID	sample2ID	sample3ID
```


Usage: python Main.py <matrix file> <array of column headers> <delimiter used in matrix file>

### ConsolidateMatrixToUniqueRows

This removes rows from a matrix that contain the same value across all columns, keeping only rows that are not homogenous across columns.

### TransposeMatrix

This transposes columns to rows, rows to columns.

### MultiFastaFromMatrix

This takes a matrix that looks like

 [sampleID	locus1	locus2	locus3]
 
 And generates a multi-fasta text file that looks like
 
 