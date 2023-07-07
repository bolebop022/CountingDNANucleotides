# Nucleotide Manipulation

This Python code provides functions for manipulating nucleotide sequences. It includes the following functions:

## `read_file(file_name)`

This function reads the contents of a file specified by `file_name` and returns the first line of the file as a string. If the file does not exist, it returns the string "File does not exist!".

## `count_nucleotides(nucleotides)`

This function takes a nucleotide sequence as input and returns a tuple containing the counts of each nucleotide (A, C, G, T) in the sequence. The counts are calculated using the `count()` method of the string.

## `transcribing_DNA_to_RNA(nucleotides)`

This function replaces all occurrences of the nucleotide 'T' with 'U' in the input sequence and returns the modified sequence. It uses the `replace()` method of the string.

## `reverse_C_of_DNA(nucleotides)`

This function takes a nucleotide sequence as input and reverses it, while also complementing each nucleotide. It iterates over each character in the sequence and replaces 'A' with 'T', 'T' with 'A', 'G' with 'C', and 'C' with 'G'. The reversed and complemented sequence is then returned. The reversal is achieved by using string slicing with a step of -1 (`[::-1]`).

## Example Usage

```python
from nucleotide_manipulation import reverse_C_of_DNA, read_file

# Read nucleotide sequence from file and reverse complement it
nucleotide_sequence = read_file("Nucleotide.txt")
reversed_sequence = reverse_C_of_DNA(nucleotide_sequence)
print(reversed_sequence)
