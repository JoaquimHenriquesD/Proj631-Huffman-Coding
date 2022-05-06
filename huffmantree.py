class HuffmanTree:
    
    def __init__(self,freq,label,fg=None,fd=None):
        self.freq=freq
        self.label=label 
        self.fg = fg
        self.fd = fd
        
    def __str__(self):
        return "label :"+self.label+" frequence : " + str(self.freq) + " gauche : " + str(self.fg.freq) + " droit : " + str(self.fd.freq)
    
    """gt = greater than"""
    def __gt__(self, other):
        if isinstance(other, HuffmanTree):
            if self.freq > other.freq:
                return True
            elif self.freq <= other.freq:
                return False
            
    """lt = lower than """            
    def __lt__(self, other):
       if isinstance(other, HuffmanTree):
           if self.freq < other.freq:
               return True
           elif self.freq >= other.freq:
               return False
    
    
     #setters :
    def set_frequence(self,freq):
        self.freq=freq
    
    
    #getters :
    def getFreq(self):
        return self.freq
    
    def getFd(self):
        return self.fd
    
    def getFg(self):
        return self.fg
    
    
    def path(self,pathing=None,res={}):
        """
        path(arbre,String,Dictionary{String etiquette:String chemin})
        return Dictionary{String etiquette:String chemin}

        function that take the path in depht
        """
        if self.getFd() is None and self.getFg() is None:
            res[self.label]=pathing
        if not self.getFg() is None:
            if pathing is None:
                self.getFg().path('0')
            else:
                self.getFg().path(pathing + '0')            
        if not self.getFd() is None:        
            if pathing is None:
                self.getFd().path('1')
            else:
                self.getFd().path(pathing + '1')            
        
        return res