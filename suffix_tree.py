import sys

class Node():
    def __init__(self, id=-1, parentNode=None, depth=-1):
        self.id = id
        self.depth = depth
        self.suffixLink = None
        self.tLinks = []
        self.parent = parentNode
        self.g_index = {}


    def _has_transition(self, suffix):
        for node,_suffix in self.tLinks:
            if _suffix == '__@__' or suffix == _suffix:
                return True
        return False

    def is_leaf(self):
        return self.tLinks == []

    def to_string(self):
        return("SNode: id:"+ str(self.id) + " depth:"+str(self.depth) +
            " transitons:" + str(self.tLinks))

    def _traverse(self, nn):
        for (n, _) in self.tLinks:
            n._traverse(nn)
        nn(self)

    def _get_leaves(self):
        if self.is_leaf():
            return list([self])
        else:
            return [q for (n,_) in self.tLinks for q in n._get_leaves()]

    def _add_suffixLink(self, suffix_node):
        self.suffixLink = suffix_node

    def _get_suffixLink(self):
        if self.suffixLink != None:
            return self.suffixLink
        else:
            return False

    def _get_tLink(self, suffix):
        for node,suff in self.tLinks:
            if suff == '__@__' or suffix == suff:
                return node
        return False

    def _add_tLink(self, snode, suffix=''):
        tl = self._get_tLink(suffix)
        if tl: # TODO: imporve this.
            self.tLinks.remove((tl,suffix))
        self.tLinks.append((snode,suffix))

class SuffixTree():
    def __init__(self, ip=[]):
        self.root = Node()
        self.root.depth = 0
        self.root.id = 0
        self.root.parent = self.root
        self.root._add_suffixLink(self.root)
        self.terminals = (i for i in list(list(range(0xE000,0xF8FF+1)) + list(range(0xF0000,0xFFFFD+1)) + list(range(0x100000, 0x10FFFD+1))))

        if len(ip) != 0:
           self._build_tree(ip)

    def _build(self, q):
        self.word = q
        r = self.root
        wl = 0
        for i in range(len(q)):
            while r.depth == wl and r._has_transition(q[wl+i]):
                r = r._get_tLink(q[wl+i])
                wl = wl + 1
                while wl < r.depth and q[r.id + wl] == q[i + wl]:
                    wl = wl + 1
            if wl < r.depth:
                r = self._create_node(q, r, wl)
            self._make_leaf(q, i, r, wl)
            if not r._get_suffixLink():
                self._compute_suffixLink(q, r)
            r = r._get_suffixLink()
            wl = wl - 1
            if wl < 0:
                wl = 0

    def _create_node(self, q, r, wl):
        i = r.id
        p = r.parent
        v = Node(id=i, depth=wl)
        v._add_tLink(r,q[i+wl])
        r.parent = v
        p._add_tLink(v, q[i+p.depth])
        v.parent = p
        return v

    def _make_leaf(self, q, i, r, wl):
        w = Node()
        w.id = i
        w.depth = len(q) - i
        r._add_tLink(w, q[i + wl])
        w.parent = r
        return w

    def _build_tree(self, ww):

        www = ''.join([q + chr(next(self.terminals)) for q in ww])
        self.word = www
        self.wordss(ww)
        self._build(www)
        self.root._traverse(self._label)

    def _label(self, node):
        if node.is_leaf():
            q = {self._word_start_index(node.id)}
        else:
            q = {n for ns in node.tLinks for n in ns[0].g_index}
        node.g_index = q

    def _word_start_index(self, id):
        i = 0
        for _idx in self.word_starts[1:]:
            if id < _idx:
                return i
            else:
                i+=1
        return i

    def find(self, st):
        y_input = st
        node = self.root
        while True:
            edge = self._edgeLabel(node, node.parent)
            if edge.startswith(st):
                break

            i = 0
            while(i < len(edge) and edge[i] == st[0]):
                st = st[1:]
                i += 1

            if i != 0:
                if i == len(edge) and st != '':
                    pass
                else:
                    return []

            node = node._get_tLink(st[0])
            if not node:
                return []

        leaves = node._get_leaves()
        return [n.id for n in leaves]

    def wordss(self, w):
        self.word_starts = []
        i = 0
        for n in range(len(w)):
            self.word_starts.append(i)
            i += len(w[n]) + 1

    def lcs(self, S,T):
        m = len(S)
        n = len(T)
        counter = [[0]*(n+1) for x in range(m+1)]
        longest = 0
        lcs_set = set()
        for i in range(m):
            for j in range(n):
                if S[i] == T[j]:
                    c = counter[i][j] + 1
                    counter[i+1][j+1] = c
                    if c > longest:
                        lcs_set = set()
                        longest = c
                        lcs_set.add(S[i-c+1:i+1])
                    elif c == longest:
                        lcs_set.add(S[i-c+1:i+1])

        return lcs_set

    def _edgeLabel(self, node, parent):
        return self.word[node.id + parent.depth : node.id + node.depth]

    def _compute_suffixLink(self, q, r):
        wl = r.depth
        v = r.parent._get_suffixLink()
        while v.depth < wl - 1:
            v = v._get_tLink(q[r.id + v.depth + 1])
        if v.depth > wl - 1:
            v = self._create_node(q, v, wl-1)
        r._add_suffixLink(v)
