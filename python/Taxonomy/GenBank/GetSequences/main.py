from Bio import Entrez
from Bio import SeqIO
import pandas as pd
from sortedcontainers import SortedDict

def get_dataframe(fname):
    df = pd.read_csv(fname)
    return df

def getGenus(df):
    genus = SortedDict()
    for index, row in df.iterrows():
        genusVal = str(row['Genus'])
        genus[genusVal] = (0)
    return genus
def fetch_genbank_sequences(genus, retmax=100):
    """Fetches GenBank sequences for a given genus.

    Args:
        genus: The genus name.
        email: Your email address for NCBI queries.
        retmax: Maximum number of sequences to retrieve per batch.

    Returns:
        A list of SeqRecord objects.
    """
    email = "lawrence.perepolkin@gmail.com"

    Entrez.email = email
    sterm = 'Nematoda [Organism] AND genus [All Fields] AND ' + genus + ' [Organism]'
    handle = Entrez.esearch(db="nucleotide", term=sterm)
    record = Entrez.read(handle)
    handle.close()

    idlist = record["IdList"]
    count = int(record["Count"])
    print(genus)
    print("Found %i sequences" % count)

    sequences = []
    for start in range(0, count, retmax):
        end = min(start + retmax, count)
        print("Downloading records %i to %i" % (start+1, end))
        handle = Entrez.efetch(db="nucleotide", rettype="fasta", retmode="text", id=idlist[start:end])
        seqs = SeqIO.parse(handle, "fasta")
        sequences.extend(seqs)
        handle.close()

    with open(genus + ".fasta", "w") as output_file:
        SeqIO.write(sequences, output_file, "fasta")

    return sequences

def main():
    fname1 = '../../combine_TAXA_NCBI_WoRMS_GenBank/txtFile.csv'
    fname1Df = get_dataframe(fname1)
    genusDict = getGenus(fname1Df)

    cnt = 0
    for g in genusDict:
        genus = g
        sequences = fetch_genbank_sequences(genus)
        print (sequences)

if __name__ == '__main__':
    main()