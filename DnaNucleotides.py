def read_file(file_name):
    try:
        with open(file_name) as file:
            return ''.join(file.readlines()[0])
    except FileNotFoundError:
        return "File does not exist!"


def count_nucleotides(nucleotides):
    return (nucleotides.count('A'), nucleotides.count('C')
            ,nucleotides.count('G'),nucleotides.count('T'))

def transcribing_DNA_to_RNA(nucleotides):
    return nucleotides.replace('T','U')


def reverse_C_of_DNA(nucleotides):
    new_nucleotides = ""
    for i in range(0, len(nucleotides)):
        if nucleotides[i] == 'A':
            new_nucleotides = f'{new_nucleotides}T'
        elif nucleotides[i] == 'T':
            new_nucleotides = f'{new_nucleotides}A'
        elif nucleotides[i] == 'G':
            new_nucleotides = f'{new_nucleotides}C'
        elif nucleotides[i] == 'C':
            new_nucleotides = f'{new_nucleotides}G'

    return new_nucleotides[::-1]
    

if __name__ == "__main__":
    print(reverse_C_of_DNA(read_file("Nucleotide.txt")))