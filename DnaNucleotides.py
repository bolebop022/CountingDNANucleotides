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

if __name__ == "__main__":
    print(transcribing_DNA_to_RNA(read_file("Nucleotide.txt")))