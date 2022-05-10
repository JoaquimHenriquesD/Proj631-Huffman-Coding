import os
from huffmanfilescoding import FilesCoding
from huffmantree import HuffmanTree
from codagehuffmanbinary import BinaryConverter

class main:
    
    traitFic = FilesCoding()
    
    try:
        nomFic = input('Files path to be compressed : \n')
        alphaEtFreq = traitFic.getAlphabetAndFreq(nomFic)
    except FileNotFoundError:
        print("")
        nomFic = input('Error try again : \n')
        alphaEtFreq = traitFic.getAlphabetAndFreq(nomFic)
    
    listeFreq = alphaEtFreq[1]
    listeAlphabet = alphaEtFreq[0]
    
    alpha = listeAlphabet
    
    dictioAlphaFreq = traitFic.dictioAlphabetFreq(listeFreq,listeAlphabet)
    dictioFreqPuisASCII = traitFic.TriDictByFreq(dictioAlphaFreq)
    
    
    tailleAlphabet = len(listeAlphabet)
    
    listeFreq = []
    listeAlphabet = []
    
    traitFic.WriteFrequency("Taille de l'alphabet : "+ str(tailleAlphabet),None,nomFic);
    for couple in dictioFreqPuisASCII:
        traitFic.WriteFrequency(couple[0],couple[1],nomFic)
        listeFreq.append(couple[1])
        listeAlphabet.append(couple[0])
    
    liste_arbre=[]
    for i in range(0,len(listeFreq)):
        liste_arbre.append(HuffmanTree(listeFreq[i],listeAlphabet[i]))
        
    while(len(liste_arbre)>1):
        min1=min(liste_arbre)
        liste_arbre.remove(min1)
        min2=min(liste_arbre)
        liste_arbre.remove(min2)
        liste_arbre.append(HuffmanTree(min1.freq+min2.freq,"",min1,min2))
    
    
    #Quand notre arbre est fini la racine est le premier (et unique) élément de notre liste d'arbre
    racine = liste_arbre[0]
    
    
    tableBin = racine.path()
        
    convBin = BinaryConverter()
    
    convBin.writeBinaryValue(alpha,tableBin,nomFic)
    
    contenu = traitFic.getContentFile(nomFic)
    
    
    listeBin = convBin.BinaryConvertion(contenu,tableBin)
    
    
    convBin.addLastBit(listeBin)
            
    listeBin8 = convBin.get8pack(listeBin)

            
    convBin.writeBinaryFile(nomFic[:-4]+'_comp.bin',listeBin8)
    
    tailleDepart = (os.path.getsize(nomFic[:-4]+'_comp.bin'))
    tailleArrivee = (os.path.getsize(nomFic))

    #calcul du taux de compression :
    taux_de_compression=1-(tailleDepart/tailleArrivee)

    print("\n Le taux de compression pour "+ nomFic+" est de "+str(round(taux_de_compression,2)*100)+"%")


    charTot = 0 
    
    #pour chaque char de l'alphabet on multiplie le nombre de bits sur lequel il est codé par le nombre de fois qu'il apparait
    for i in range(0,len(listeAlphabet)):
        charTot = charTot + len(tableBin[listeAlphabet[i]])*listeFreq[i]
    nb_moy_bits=round(charTot/sum(listeFreq),2)

    print("\n Le nombre moyen de bits pour un caractère du fichier "+ nomFic +" est de "+str(nb_moy_bits))