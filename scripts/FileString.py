'''
class which handles the fileName stuff

convention is 

[C]%Y-%m-%dT%H:%M:%S[.EXT]

[.EXT] can be:
-null, raw SDR outputted binary file
-.hdr, header file
-.npy numpy array

[C] indicates whether the file is the final compressed
'''

import os 
from datetime import datetime


class FileString:
    def __init__(self,file):
        #split the file into its fileName and the ascociated extension
        self.fileName,self.fileExt = os.path.splitext(file)
        #find the type of file
        self.findType()
        #find the pseudo_start_time
        self.pseudo_start_time = self.findPseudoStartTime()

    #find the type of file. 
    def findType(self):
        #if there is no file extension, the file must be a binary file
        if not self.fileExt:
            self.type = "bin"
        #if it is a numpy file, and the first character is C, then we must have a compressed spectrogram
        elif self.fileExt == ".npy" and self.fileName[0]=="C":
            self.type = "compressed-spectrogram"
        #if we have a numpy file, and the first character is NOT C, then we have a 
        elif self.fileExt == ".npy" and self.fileName[0]!="C":
            self.type = "spectrogram"
        #if the file extension is .hdr then we have a header file
        elif self.fileExt==".hdr":
            self.type="header"

    #extract pseudo_start_time from the filename [careful! if we have a compressed file]
    def findPseudoStartTime(self):
        #if the file begins with a C, take the rest of the filename [without the extension]
        if self.fileName[0]=="C":
            return self.fileName[1:]
        else:
            return self.fileName
        




