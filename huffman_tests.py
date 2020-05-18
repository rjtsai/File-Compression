import unittest
import filecmp
import subprocess
from ordered_list import *
from huffman import *


class TestList(unittest.TestCase):
    def test_cnt_freq(self):
        freqlist	= cnt_freq("file2.txt")
        anslist = [2, 4, 8, 16, 0, 2, 0] 
        self.assertListEqual(freqlist[97:104], anslist)
        with self.assertRaises(FileNotFoundError):
            cnt_freq('not_exist.txt')
        

    
    def test_lt_and_eq(self):
        freqlist = cnt_freq("file2.txt")
        anslist = [2, 4, 8, 16, 0, 2, 0]
        ascii = 97
        lst = OrderedList()
        for freq in anslist:
            node = HuffmanNode(chr(ascii), freq)
            lst.add(node)
            ascii += 1
        self.assertEqual(lst.index(HuffmanNode('e', 0)), 0)
        self.assertEqual(lst.index(HuffmanNode('d', 16)), 6)
        self.assertEqual(lst.index(HuffmanNode('a', 2)), 2)
        self.assertFalse(HuffmanNode('a', 2) == None)

    
    def test_create_header(self):
        freqlist = cnt_freq("file2.txt")
        empty = cnt_freq('empty_file.txt')
        self.assertEqual(create_header(freqlist), "97 2 98 4 99 8 100 16 102 2")
        self.assertEqual(create_header(empty), '')


    
    def test_create_huff_tree(self):
        freqlist = cnt_freq("file2.txt")
        hufftree = create_huff_tree(freqlist)
        self.assertEqual(hufftree.freq, 32)
        self.assertEqual(hufftree.char, 97)
        left = hufftree.left
        self.assertEqual(left.freq, 16)
        self.assertEqual(left.char, 97)
        right = hufftree.right
        self.assertEqual(right.freq, 16)
        self.assertEqual(right.char, 100)
        
        empty = cnt_freq('empty_file.txt')
        emptyTree = create_huff_tree(empty)
        self.assertEqual(emptyTree, None)

        single = cnt_freq('file3.txt')
        singleTree = create_huff_tree(single)
        self.assertEqual(singleTree.getRight(), None)
    
    def test_create_code(self):
        freqlist = cnt_freq("file2.txt")
        hufftree = create_huff_tree(freqlist)
        codes = create_code(hufftree)
        self.assertEqual(codes[ord('d')], '1')
        self.assertEqual(codes[ord('a')], '0000')
        self.assertEqual(codes[ord('f')], '0001')

    def test_01_textfile(self):
        huffman_encode("file1.txt", "file1_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb file1_out.txt file1_soln.txt", shell = True)
        self.assertEqual(err, 0)
        err = subprocess.call("diff -wb file1_out_compressed.txt file1_compressed_soln.txt", shell = True)
        self.assertEqual(err, 0)
        
    def test_02_textfile(self):
        huffman_encode('file2.txt', 'file2_out.txt')
        err = subprocess.call("diff -wb file2_out.txt file2_soln.txt", shell = True)
        self.assertEqual(err, 0)
        err = subprocess.call("diff -wb file2_out_compressed.txt file2_compressed_soln.txt", shell = True)
        self.assertEqual(err, 0)
    
    def test_03_multiline(self):
        huffman_encode('multiline.txt', 'multiline_out.txt')
        err = subprocess.call("diff -wb multiline_out.txt multiline_soln.txt", shell = True)
        self.assertEqual(err, 0)
        err = subprocess.call("diff -wb multiline_out_compressed.txt multiline_compressed_soln.txt", shell = True)
        self.assertEqual(err, 0)
    '''
    def test_04_WAP(self):
        huffman_encode('file_WAP.txt', 'file_WAP_out.txt')
        err = subprocess.call("diff -wb file_WAP_out.txt file_WAP_soln.txt", shell = True)
        self.assertEqual(err, 0)
        err = subprocess.call("diff -wb file_WAP_out_compressed.txt file_WAP_compressed_soln.txt", shell = True)
        self.assertEqual(err, 0)
    '''
    def test_05_empty(self):
        huffman_encode('empty_file.txt', 'empty_file_out.txt')

    def test_06_FileNotExist(self):
        with self.assertRaises(FileNotFoundError):
            huffman_encode('not_a_file.txt', 'not_out.txt')

    def test_07_singleUnique(self):
        huffman_encode('file3.txt', 'file3_out.txt')
        err = subprocess.call("diff -wb file3_out.txt file3_soln.txt", shell = True)
        self.assertEqual(err, 0)
        err = subprocess.call("diff -wb file3_out_compressed.txt file3_compressed_soln.txt", shell = True)
        self.assertEqual(err, 0)

    def test_08_declaration(self):
        huffman_encode('declaration.txt', 'declaration_out.txt')
        err = subprocess.call("diff -wb declaration_out.txt declaration_soln.txt", shell = True)
        self.assertEqual(err, 0)
        err = subprocess.call("diff -wb declaration_out_compressed.txt declaration_compressed_soln.txt", shell = True)
        self.assertEqual(err, 0)

#################################################################################
####################    PART 3B     #############################################

    def test_01a_test_file1_parse_header(self):
        f = open('file1_compressed_soln.txt', 'rb')
        header = f.readline()        
        f.close()
        expected = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.compare_freq_counts(parse_header(header), expected)
    
    
    def test_01_test_file1_decode(self):
        huffman_decode("file1_compressed_soln.txt", "file1_decoded.txt")
        err = subprocess.call("diff -wb file1.txt file1_decoded.txt", shell = True)
        self.assertEqual(err, 0) 
    
    def test_02_test_empty(self):
        huffman_decode("empty_file_out_compressed.txt", "empty_decoded.txt")
        err = subprocess.call("diff -wb empty_file.txt empty_decoded.txt", shell = True)
        self.assertEqual(err, 0) 

    def test_03_test_file3(self):
        huffman_decode("file3_compressed_soln.txt", "file3_decoded.txt")
        err = subprocess.call("diff -wb file3.txt file3_decoded.txt", shell = True)
        self.assertEqual(err, 0) 

    def test_04_test_NotAFile(self):
        with self.assertRaises(FileNotFoundError):
            huffman_decode('FakeFile.txt', 'FakeFile_decoded.txt')

    '''
    def test_04_test_WAP_decode(self):
        huffman_decode("file_WAP_compressed_soln.txt", "file_WAP_decoded.txt")
        err = subprocess.call("diff -wb file_WAP.txt file_WAP_decoded.txt", shell = True)
        self.assertEqual(err, 0) 
    '''
    def compare_freq_counts(self, freq, exp):
        for i in range(256):
            stu = 'Frequency for ASCII ' + str(i) + ': ' + str(freq[i])
            ins = 'Frequency for ASCII ' + str(i) + ': ' + str(exp[i])
            self.assertEqual(stu, ins)

if __name__ == '__main__': 
   unittest.main()
