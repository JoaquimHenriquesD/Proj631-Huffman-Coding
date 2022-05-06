class BinaryConverter:

    def writeBinaryFile(self,fileName,content):
        with open(fileName, "wb") as f:
            for octet in content:
                f.write((int(octet, base=2)).to_bytes((len(octet)//8), byteorder='big')) 
        f.close()
    
    def addLastBit(self,content):
        while len(content)%8 != 0:
            content = content+"0"

    def BinaryConvertion(self,text,binaryTable):
        textBinary = ""
        for i in text:
            textBinary = textBinary + binaryTable[i]
        return textBinary     

    def get8pack(self,content):
        listeBin = []
        for i in range(8,len(content),8):
            listeBin.append(content[i-8:i])
        return listeBin    
    
    def writeBinaryValue(self,alphabet,binaryTable,fileName):
        with open(fileName[:-4]+'_valCharBin.txt','a') as f:
            for i in alphabet:
                f.write(i+" : "+str(binaryTable[i])+'\n')
            f.close()
