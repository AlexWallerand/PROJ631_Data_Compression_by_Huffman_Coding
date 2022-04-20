from operator import attrgetter

def count_occurences(text):
    d = {}
    for char in text:
        if char in d:
            d[char] += 1
        else:
            d[char] = 1
    d = dict(sorted(d.items(), key = lambda x: (x[1], x[0])))
    return d

class Node:

    def __init__(self, label, frequency, leftChild = None, rightChild = None):
        self.label = label
        self.frequency = frequency
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.edge = ''
        
    def getFrequency(self):
        return self.frequency

    def setEdge(self, value):
        self.edge = value

    def __str__(self):
        return f'{self.label} {self.edge} [{self.leftChild},{self.rightChild}]'

def build_huffman_tree(char_dict):
    nodes = []

    for char in char_dict:
        nodes.append(Node(char, char_dict[char]))

    while len(nodes) > 1:
        nodes.sort(key = attrgetter('frequency'))

        left = nodes[0]
        left.setEdge('0')

        right = nodes[1]
        right.setEdge('1')

        sum = left.getFrequency() + right.getFrequency()
        node = Node(str(sum), sum, left, right)
        
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(node)
    
    HuffmanTree = nodes
    return HuffmanTree

def calculateCodes(node, value = '', code_dict = {}):
    newValue = value + node.edge

    if node.leftChild != None:
        calculateCodes(node.leftChild, newValue, code_dict)
    if node.rightChild != None:
        calculateCodes(node.rightChild, newValue, code_dict)
    
    if node.leftChild == None and node.rightChild == None:
        code_dict[node.label] = newValue
    
    return code_dict

if __name__ == '__main__':
    file = open('./Tests/textesimple.txt', 'r')
    text = file.read()
    dict = count_occurences(text)
    print(dict)
    tree = build_huffman_tree(dict)
    codes = calculateCodes(tree[0])
    print(codes)
    res = ""
    for char in text:
        res += codes[char]
    print('\nTexte compressé :\n')
    print(res)