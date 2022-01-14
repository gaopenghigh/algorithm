class Node:
    def __init__(self, freq, symbol, left=None, right=None) -> None:
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.code = '' # 0 or 1

def build_huffman_tree(symbol_freq_map):
    nodes = []
    for symbol, freq in symbol_freq_map.items():
        n = Node(freq, symbol)
        nodes.append(n)
    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x.freq)
        left = nodes[0]
        left.code = '0'
        right = nodes[1]
        right.code = '1'
        new_node = Node(left.freq + right.freq, None, left, right)
        nodes = nodes[2:]
        nodes.append(new_node)
    return nodes[0]

def _get_coding_map(coding_map, node, val=''):
    val += node.code
    if node.left is not None:
        _get_coding_map(coding_map, node.left, val)
    if node.right is not None:
        _get_coding_map(coding_map, node.right, val)
    if node.left is None and node.right is None:
        coding_map[node.symbol] = val

def get_coding_map(huffman_tree_node):
    coding_map = {}
    _get_coding_map(coding_map, huffman_tree_node)
    return coding_map

def encode(s):
    symbol_freq_map = calc_symbol_freq(s)
    huffman_tree = build_huffman_tree(symbol_freq_map)
    coding_map = get_coding_map(huffman_tree)
    ret = ''
    for i in s:
        ret += coding_map[i]
    return ret

def decode(codes, huffman_tree):
    ret = ''
    p = huffman_tree
    for i in codes:
        if i == '0':
            p = p.left
        elif i == '1':
            p = p.right
        if p.left is None and p.right is None:
            ret += p.symbol 
            p = huffman_tree
    return ret

def calc_symbol_freq(s):
    d = {}
    for i in s:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    return d


if __name__ == '__main__':
    s = 'a' * 5 + 'b' * 9 + 'c' * 12 + 'd' * 13 + 'e' * 16 + 'f' * 45
    print(s)
    m = calc_symbol_freq(s)
    huffman_tree = build_huffman_tree(m)
    coding_map = get_coding_map(huffman_tree)
    for symbol, code in coding_map.items():
        print('%s -> %s' % (symbol, code))
    encoded = encode(s)
    print('--- encoded ---')
    print(encoded)
    decoded = decode(encoded, huffman_tree)
    print('--- decoded ---')
    print(decoded)
