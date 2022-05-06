class FilesCoding():
    
    
    def getContentFile(self,FilePath):
        return open(FilePath).read()
    
    def TriDictByFreq(self,dicti):
        return sorted(dicti.items(), key=lambda x: (x[1],x[0]))
    
    def triDictioByFreq(self,dicti):
        dictiTriFreq = {k: v for k, v in sorted(dicti.items(), key=lambda item: item[1])}
        return dictiTriFreq

    def WriteFrequency(self,lettre,freq,FileName):
        with open(FileName[:-4]+'_Freq.txt','a') as f:
            if(freq != None):
                f.write(lettre+' '+str(freq)+'\n')
            else:
                f.write(lettre+'\n')
        f.close()

    def dictioAlphabetFreq(self,alphabet,freq):
        dictio = dict()
        for i in range(0,len(alphabet)):
            dictio[freq[i]] = alphabet[i]
        return dictio
    
    def triDictioASCII(self,dicti):
        dictiASCII = dict()
        for i in sorted(dicti.keys()):
            dictiASCII[i] = dicti[i]
        return dictiASCII
    

    def getAlphabetAndFreq(self,FilePath):
        
        content = self.getContentFile(FilePath)
        alphabet = []
        frequency = []
        for i in range(0,len(content)):
            if content[i] not in alphabet:
                alphabet.append(content[i])
                frequency.append(1)
            else:
                rang = alphabet.index(content[i])
                frequency[rang] = frequency[rang]+1
        return alphabet, frequency
    
    
    
    
    
   