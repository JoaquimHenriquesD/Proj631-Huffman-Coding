class ConvertisseurBinaire:
    
    
    def ecrireBinaireFichier(self,fileName,contenu):
        with open(fileName, "wb") as f:
            for octet in contenu:
                f.write((int(octet, base=2)).to_bytes((len(octet)//8), byteorder='big')) 
        f.close()
    
    def addBitManquant(self,contenu):
        while len(contenu)%8 != 0:
            contenu = contenu+"0"
            

    def get8pack(self,contenu):
        listeBin = []
        for i in range(8,len(contenu),8):
            listeBin.append(contenu[i-8:i])
        return listeBin
            
        
    def convertEnBinaire(self,text,binaryTable):
        contenuBinaire = ""
        for i in text:
            contenuBinaire = contenuBinaire + binaryTable[i]
        return contenuBinaire
    
    def ecrireValBinaire(self,alphabet,binaryTable,nomdufichier):
        with open(nomdufichier[:-4]+'_valCharBin.txt','a') as f:
            for i in alphabet:
                f.write(i+" : "+str(binaryTable[i])+'\n')
            f.close()