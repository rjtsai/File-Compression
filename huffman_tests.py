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
        self.assertEqual(create_header(freqlist), "97 2 98 4 99 8 100 16 102 2")

    
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

if __name__ == '__main__': 
   unittest.main()
