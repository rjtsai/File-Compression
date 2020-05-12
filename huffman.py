from huffman_bit_writer import *
from ordered_list import *

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char   # stored as an integer - the ASCII character code value
        self.freq = freq   # the freqency associated with the node
        self.left = None   # Huffman tree (node) to the left
        self.right = None  # Huffman tree (node) to the right

    def getChar(self):
        return self.char

    def getFreq(self):
        return self.freq

    def getRight(self):
        return self.right

    def getLeft(self):
        return self.left

    def setRight(self, newRight):
        self.right = newRight

    def setLeft(self, newLeft):
        self.left = newLeft

    def setChar(self, newChar):
        self.char = newChar

    def setFreq(self, newFreq):
        self.freq = newFreq
        
    def __eq__(self, other):
        '''Needed in order to be inserted into OrderedList'''
        return type(other) == HuffmanNode and self.char == other.char and self.freq == other.freq and self.left == other.left and self.right == other.right
        
    def __lt__(self, other):
        '''Needed in order to be inserted into OrderedList'''
        if self.freq == other.freq:
            return (self.char) < (other.char)
        return (self.freq) < (other.freq)

    def __repr__(self):
        return "HuffmanNode(%s, %s)" % (self.char, self.freq)

def cnt_freq(filename):
    '''Opens a text file with a given file name (passed as a string) and counts the 
    frequency of occurrences of all the characters within that file'''
    f = open(filename)
    fr = f.read()
    countList = []
    for i in range(256):
        countList.append(0)
    for char in fr:
        if ord(char) < 256:
            countList[ord(char)] += 1
    f.close()
    return countList

def create_list(countList):
    lst = OrderedList()
    for i in range(len(countList)):
        if countList[i] > 0:
            lst.add(HuffmanNode(i, countList[i]))
    return lst

def combine(item1, item2):
    newNode = HuffmanNode(None, None)
    item1 = item1.getItem()
    item2 = item2.getItem()
    if item1.getChar() < item2.getChar():
        newNode.setChar(item1.getChar())
    else:
        newNode.setChar(item2.getChar()) 
    newNode.setFreq(item1.getFreq()+item2.getFreq())
    if item1.getFreq() < item2.getFreq():
        newNode.setRight(item2)
        newNode.setLeft(item1)
    elif item1.getFreq() > item2.getFreq():
        newNode.setRight(item1)
        newNode.setLeft(item2)
    else:
        if item1.getChar() < item2.getChar():
            newNode.setRight(item2)
            newNode.setLeft(item1)
        else:
            newNode.setRight(item1)
            newNode.setLeft(item2)
    return newNode



def create_huff_tree(char_freq):
    '''Create a Huffman tree for characters with non-zero frequency
    Returns the root node of the Huffman tree'''
    lst = create_list(char_freq)
    if lst.size() == 0:
        return HuffmanNode(None,None)
    while lst.size() > 1:
        item1 = lst.dummy.getNext()
        lst.remove(item1.getItem())
        item2 = lst.dummy.getNext()
        lst.remove(item2.getItem())
        newNode = combine(item1, item2)
        lst.add(newNode)
    return lst.dummy.getNext().getItem()
    



def create_code(node):
    '''Returns an array (Python list) of Huffman codes. For each character, use the integer ASCII representation 
    as the index into the arrary, with the resulting Huffman code for that character stored at that location'''
    codeList = []
    for i in range(256):
        codeList.append(None)
    assignCode_helper(node, '', codeList)
    return codeList
    
def assignCode_helper(node, code, codeList):
    if node.getRight() is None and node.getLeft() is None:
        codeList[node.getChar()] = code
    if node.getRight() is not None and node.getLeft() is not None:
        assignCode_helper(node.getRight(), code + '1', codeList)
        assignCode_helper(node.getLeft(), code + '0', codeList)
    

def create_header(freqs):
    '''Input is the list of frequencies. Creates and returns a header for the output file
    Example: For the frequency list asscoaied with "aaabbbbcc, would return “97 3 98 4 99 2” '''
    freqList = []
    for i in range(256):
        if freqs[i] > 0:
            freqList.append(str(i))
            freqList.append(str(freqs[i]))
    freq_str = ' '.join(freqList)
    return freq_str

def huffman_encode(in_file, out_file):
    '''Takes inout file name and output file name as parameters - both files will have .txt extensions
    Uses the Huffman coding process on the text from the input file and writes encoded text to output file
    Also creates a second output file which adds _compressed before the .txt extension to the name of the file.
    This second file is actually compressed by writing individual 0 and 1 bits to the file using the utility methods 
    provided in the huffman_bits_io module to write both the header and bits.
    Take not of special cases - empty file and file with only one unique character'''
    countList = cnt_freq(in_file)
    hufftree = create_huff_tree(countList)
    codeList = create_code(hufftree)
    header = create_header(countList)
    compressed_out = out_file[:-4] + '_compressed' + out_file[-4:]

    inF = open(in_file)
    readinF = inF.read()
    outF = open(out_file, 'w')

    outF.write(header + '\n')
    code = ''
    for char in readinF:
        for i in range(len(codeList)):
            if ord(char) == i:
                code += codeList[i]
    outF.write(code)

    compress = HuffmanBitWriter(compressed_out)
    compress.write_str(header)
    compress.write_str('\n')
    compress.write_code(code)

    
    inF.close()
    outF.close()
    compress.close()
    



