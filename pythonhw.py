#Calculating AT Content

length = len(dna)
numA = dna.count("A")
numT = dna.count("T")
ATcount = float(numA+numT)/length
print ATcount


#Complementing DNA
#Make new variable called temporary that replaces old nucleotide with a complementary nucleotide
temporary = str (DNA.replace("A","tempt").replace("T","tempa").replace("C","tempg").replace("G","tempc"))
#Replace temporary with permanent complementary base
complement = str (temporary.replace("tempt","T").replace("tempa","A").replace("tempg","G").replace("tempc","C"))
print (complement)


#Restriction fragment length
dna_to_cut = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
frag1_length = dna_to_cut.find("GAATTC") + 1
frag2_length = len(dna_to_cut) - frag1_length
print str(frag1_length)
print str(frag2_length)

#splicing pt 1
dna_to_splice = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGAT$
exon1 = dna_to_splice[0:63]
exon2 = dna_to_splice[90:]
print exon1+exon2

#splicing pt 2
coding_length = len(exon1+exon2)
total_length = len(dna_to_splice)
percentlength = (100*coding_length / total_length)
print str(percentlength)

#splicing pt 3
intron = (dna_to_splice[63:90])
print exon1 + intron.lower() + exon2
