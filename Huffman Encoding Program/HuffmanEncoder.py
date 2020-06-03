# Huffman Encoder
# Created by Connor Laurence
# COM701 19/20 WREXHAM Software Development: Object Oriented Programming
# Assignment 2 - Huffman coding
# Completed - 06/05/2020

# Code

# Imports
import heapq
import sys

# Binary Huffman tree
class HuffNode:
    def __init__(self, char, freq):
        # Create node for given character and frequency
        self.leftChild = None
        self.rightChild = None
        self.char = char
        self.freq = freq
        
    def __lt__(self, other):
        #Used to compare two Huffman Nodes
        return self.freq < other.freq

# Get Frequencies of unique characters in the string
def getFreq(string):
    freq = {}
    # builds a dictionary of frequencies
    for char in string:
        if char not in freq:
            freq[char] = 1
        else:
            freq[char] += 1 
    # creates a sorted list key, freq tuple pairs
    freqSorted = sorted(zip(freq.values(), freq.keys()))
    
    for i in range(len(freqSorted)):
        char = freqSorted[i][1] # second item - char
        freq = freqSorted[i][0] # first item - frequency
         
        freqSorted[i] = HuffNode(char, freq)
    #returns a sorted list of Huffman Nodes      
    return freqSorted  
    
def huffmanTree(string):
    #gets a sorted list of Huffman Nodes
    heap = getFreq(string)
    # Creates heap
    heapq.heapify(heap)
    # iterates pulling two lowest freq nodes from heap until only root remains
    while len(heap) != 1:
        Huff = HuffNode(None, None)
        # leftChild of new internal node = first heappop
        left = heapq.heappop(heap)
        Huff.leftChild  = left
        # rightChild of new internal node = second heappop
        right = heapq.heappop(heap)
        Huff.rightChild  = right
        # freq of new internal node = freq of leftChild + rightChild
        Huff.freq = left.freq + right.freq
        # Push new internal node to heap
        heapq.heappush(heap, Huff)
    # returns a list containing the root node of the heap    
    return heap 

def createHuffCodeTable(root):
    code = {}
    # A left edge traversal represents = 0, a right edge traversal represents = 1
    # Traverse the Huffman Tree to build the code table
    def getCode(huffNode, currentCode=""):
        # Exit if no nodes
        if (huffNode == None): 
            return
        # If node has no children add currentCode to Code book
        if (huffNode.leftChild == None and huffNode.rightChild == None):
            code[huffNode.char] = currentCode
        # Else recurse through tree - first w/ leftChild adding '0' to currentCode
        # then through rightChild adding '0' to currentCode
        # Assigns traversal bit at each branch to the currentCode for the end char
        getCode(huffNode.leftChild, currentCode + "0")
        getCode(huffNode.rightChild, currentCode + "1")
    getCode(root[0])
    return code

def huffmanEncode(string):
    # Exit if freq is 1, can't encode string
    if(len(getFreq(string))) == 1:
        return "0"*len(string)
    # Variable to store encoded string
    huffCode = ""
    # heap containing the Huffman root node
    root = huffmanTree(string)
    # Huffman code dictionary
    table = createHuffCodeTable(root)
    # Iterate through string to create encoded string
    for i in string:
        huffCode += table[i]
    return huffCode    

def huffmanTest(string):
    # If string input = empty
    if string == "":
        print("Empty String \n")
    else:
        # Original Message and Size
        print("Message: " + format(string))
        print("Original message size: " + format(sys.getsizeof(string)))
        # Encoding here
        encodedString = huffmanEncode(string)
        # Encoded Message and Size
        print("Encoded message: " + format(encodedString))
        print("Encoded message size: " + format(sys.getsizeof(int(encodedString, base=2))) + "\n")
    
    
# Testing
huffmanTest("")
huffmanTest("the quick brown fox jumps over the lazy dog")
huffmanTest("lorem ipsum dolor sit amet consectetur adipiscing elit pellentesque eleifend")
huffmanTest("data structures and algorithms")
huffmanTest("aaaabbbbbccccccdddddddeeeeeeee")

# Description of Approach

'''
The huffman approach I chose involved making a binary tree of Nodes using the HuffNode class. Initially, all the nodes are considered
leaf nodes which contain the character they represent and the frequency of which they are found within the test string that is passed
in.

The frequency collation is handled within the 'get_freq' method by using a dictionary (A mapping of unique 'keys' to 'values'). The
method loops through all characters of the data storing the key and counting how many times it occurs and storing that value. The
dictionary is then sorted using 'sorted' which comes from the 'sys' import and sent to the HuffNode class.

Once we have this sorted list of HuffNodes we use the 'huffmanTree' method to create a heap (imported via heapq) which we will use as
a priority queue. This is important because the huffman algorithm requires that we pull the two lowest probability nodes from our
collection of nodes in order to create a new node with these as the children. This new node will have both the characters of the
children combined in its char value, the combined frequency of both but will also have each child as a left and right child.
While the heap remains larger than one node, this method will continue to pull out the lowest two nodes, create a parent node and push
the parent node back to the heap. Once the heap reaches 1, that node remaining will be the root node and thus our tree is complete.

From here, we must now create a 'Code book' which is the huffman variable length codes that replace standard fixed length. These codes
are derived from our huffman tree and are indicated as traversal paths for individual characters. To avoid continuosly traversing the
tree, we need only traverse it once and store our traversals with their characters in a dictionary. The 'createHuffCodeTable' does this
recursively. If the node is empty, it escapes. If the node has no children, it stores the code traversal it has for that character thus
far. If the node has children, it calls the getCode function again for both left and right children and adds 0 and 1 respectively for
each to the 'currentCode'.

Now that we have a 'Code book', we use the 'huffmanEncode' method to loop through the data string and lookup the table for each character.
Once the character is found it is concatenated onto the 'HuffCode' string variable to collect all the codes as one. I had added an extra
method called 'huffmanEncoding' to act as an intermediary to test print the huffman tree but this is now redundant. Strings are encoded by
calling 'huffmanTest' and passing the string through. This method calls all the others in carrying out all the steps and then deals with
the formatting and printing of the output results which shows the; Message, Message Size, Encoded Message and Encoded Message size.

'''

# Justification of data structures and algorithms

'''
In this program, I have used a binary tree data structure to describe the huffman tree as this tree data structure has only two children
which matches the encoding style of Huffman coding with either 0 or 1 to represent traversal to the character in the tree and allow for
variable length codes.

To develop this huffman tree, I used a heap which is imported from the heapq library. As mentioned previously, a heap is a priority queue.
Having covered queues in class already I was already familiar with the structure and after initial research, I found the priority queue
implementation to be the natural candidate for the huffman algorithm as the heap allows for the initial leaf nodes to be pulled from the
queue as lowest frequency using 'heappop' so that a new node can be made from them and pushed back to the queue using 'heappush'.

The other data structures I used in this program were dictionaries and tuples. The dictionary was used in getting the frequencies of the
characters a bit like a two dimensional array works. I could store the character and its frequency value which I gained from looping
through the data. I also used a dictionary in the 'createHuffCodeTable' which stored associated traversal code garnered for each character.
The tuple I had used in the 'getFreq' method to create a sorted list in order to make a sorted list of huffman nodes. Tuples are sequences
(like lists, but immutable so cannot be changed lists can).

The algorithm I chose to follow was the same that I had found consistently from my initial research and was similar to that of the one
suggested from the huffman encoding visualisation resource found on our moodle.
This resource also helped my understanding of the algorithm - https://www.geeksforgeeks.org/huffman-coding-greedy-algo-3/

    The first step is to build the huffman tree by creating leaf nodes for each unique character and buidling a min heap of all leaf nodes and
    the frequency field used to compare the two nodes.

    The second step involves extracting two min frequency nodes from the heap and creating a new internal node with freq = freq of child 1 +
    freq of child 2. The lowest frequency being the left child and second being the right.

    Step three is to repeat step 2 until only one node remains i.e. the root node (of our binary huffman tree)

    Step four is the traverse the huffman tree and store our traversals for each character in a list/dictionary to be accessed later

    Step five is to create the encoded string by finding each character in out input string in the 'Code book' and concatenating that traversal
    code onto our encoded string and then display the completed encoded string.

'''

# Complexity of Solution

'''
The complexity of this solution worst case is >>> O(nlogn) <<< as the efficient priority queue data structure (heapq) it relies on require O(nlogn) per
insertion and a tree with 	'n' leaves has '2n-1' nodes in total. This means that once sorted by frequency, theres a linear O(n) aspect to creating
the Huffman tree. In any case, this is negligible as 'n' usually is not a significant number due to there being a general upper limit to the number
of characters and symbols that may be used in any sentence given i.e. the english alphabet is only 26 characters and ASCII is 128 total characters. 
'''

# Reflection on coding practice
'''
Had redundant code within and bad spacing as I was going along which upon finalising all of this I decided to fix. This method below was removed.

def huffmanEncoding(data):
    #returns encoded data and root of huffman tree
    return huffmanEncode(data), huffmanTree(data)
    
I had used this method to return the huffmanTree to view and had initially had a print function within my Huffnode class too. Since the code is now
working as intended, this is unnecessary code and may lead to some slight performance costs if left in.

Also fixed was the method 'def getCode(huffNode, currentCode=""):' whereby originally huffNode was HuffNode as gave the warning
'Redefining name 'HuffNode' from outer scope (line 7)'. This was an initial flaw on my part for poor naming convention and not checking with other areas
of my work for reuse of the same nomenclature.
Throughout, I have endeavoured to use proper variable and function names. For the most part, I have stuck to the typical convention of 'camelCase' so
that my methods are easily identifiable as such. Things I would have changed might be the formatting I used in the test method for showing the strings and
their sizes. Since all characters are stored as 8 bit integers, I could have just multiplied the length of the sentence by 8 and displayed but was having
issues converting int to string and this workaround seemed to work.
I also have the remaining warnings 'dict.values / dict.keys referenced when not iterating' in getFreq. The get frequency code was based on my understanding
of examples I had found in my intial research and the results is as I had hoped however upon reflection it seems that it is safe code but an inferior method
of constructing a list was implemented whereby iterating over them is apparently a much faster approach.
'''


