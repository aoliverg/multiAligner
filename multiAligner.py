import sys
import codecs
import argparse
import itertools

def addToLadderLC(element):
    element=tuple(sorted(element))
    if not is_subtuple_in_list_of_tuples(ladderLC,element):
        n = len(element)
        ladderLC[tuple(element)]=1
        for i in range(n-1, 0, -1):
        # Calculate combinations of length n
            combs = list(itertools.combinations(element, i))
            # Print combinations
            for comb in combs:
                comb=tuple(sorted(comb))
                if comb in ladderLC:
                    del ladderLC[comb]

def is_subtuple_in_tuple(larger, sub):
    len_sub = len(sub)
    return any(sub == larger[i:i+len_sub] for i in range(len(larger) - len_sub + 1))
    
def is_subtuple_in_list_of_tuples(list_of_tuples, sub_tuple):
    len_sub = len(sub_tuple)
    for larger_tuple in list_of_tuples:
        if any(sub_tuple == larger_tuple[i:i+len_sub] for i in range(len(larger_tuple) - len_sub + 1)):
            return True
    return False

# Create the parser
parser = argparse.ArgumentParser(description='Align multiple files.')

# Add an argument for the list of files
parser.add_argument( '-l','--ladders', type=str, nargs='+', help='The ladder files to process')
parser.add_argument( '-f','--files',  type=str, nargs='+', help='The common source and target segmented files')
parser.add_argument( '-o','--output',  type=str, help='The common source and target segmented files')

# Parse the command-line arguments
args = parser.parse_args()

# Access the list of files
ladder_list = args.ladders

files=args.files

output=args.output

falineacion=output
ffladders=output.replace(".txt","")+".ladder"

sortidaalineacion=codecs.open(falineacion,"w",encoding="utf-8")
sortidaladders=codecs.open(ffladders,"w",encoding="utf-8")


# Print the list of files (for demonstration purposes)
print('Files to process:', ladder_list)

segmentedfiles=[]
segments={}
cont=0
for f in files:
    segmentedfiles.append(f)
    entrada=codecs.open(f,"r",encoding="utf-8")
    segments[cont]=[]
    for linia in entrada:
        linia=linia.rstrip()
        segments[cont].append(linia)
    cont+=1
    entrada.close()

ladderLC={}
LC2Ln={}
Ln2LC={}
for ladderfile in ladder_list:
    entrada=codecs.open(ladderfile,"r",encoding="utf-8")
    LC2Ln[ladderfile]={}
    for l in entrada:
        l=l.rstrip()
        (iLC,iLn,score)=l.split("\t")
        score=float(score)
        iC=iLC.split(" ~~~ ")
        iL=iLn.split(" ~~~ ")
        if True:#score>0:
            addToLadderLC(iC)
            for i in iC:
                LC2Ln[ladderfile][i]=iL



finalLadders=[]
for k in ladderLC:
    aliLC=":".join(k)
   
    targets=[]
    for ladderfile in LC2Ln:
        target=[]
        for p in k:
            try:
                target.extend(LC2Ln[ladderfile][p])
            except:
                pass
        target=":".join(list(set(target)))
        targets.append(target)
    cadenaLadder=aliLC+"\t"+"\t".join(targets)
    finalLadders.append(cadenaLadder)

for fl in finalLadders:
    sortidaladders.write(fl+"\n")
    camps=fl.split("\t")
    cont=0
    alineacio=[]
    for c in camps:
        cadena=[]
        if not c=="":
            sns=c.split(":")
            sns.sort()
            for i in sns:
                try:
                    i=int(i)
                    cadena.append(segments[cont][i])
                except:
                    pass
        alineacio.append(" ".join(cadena))
        cont+=1
    cadenafinal="\t".join(alineacio)
    if cadenafinal.find("<p>")==-1:
        sortidaalineacion.write(cadenafinal+"\n")
    
    

    
    
