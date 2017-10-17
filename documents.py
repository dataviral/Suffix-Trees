from suffix_tree import SuffixTree

class Documents():
    def __init__(self, documents_dict):
        self.documents = documents_dict
        self.document_trees = {}
        self._build()

    def _build(self):
        for doc in self.documents:
            self.document_trees[doc] = SuffixTree([self.documents[doc]])

    def all_in_all(self, query):
        "Search for all occurences"
        result = {}
        for doc in self.document_trees:
            matches = self.document_trees[doc].find(query)
            if len(matches) != 0:
                result[doc] = {}
            for i,match in enumerate(matches):
                fh = self.documents[doc][:match].split(".")[-1]
                lh = self.documents[doc][match:].split(".")[0]
                result[doc][i]  = fh+lh
        return result

    def one_in_all(self, query):
        "Search for first occurence"
        result = {}
        for doc in self.document_trees:
            matches = self.document_trees[doc].find(query)
            if len(matches) != 0:
                result[doc] = []
            else:
                str = self.document_trees[doc].lcs(query, self.documents[doc])
                # str = list(str
                if len(str) != 0:
                    result[doc] = list(str)[0]
                continue
            for match in matches:
                fh = self.documents[doc][:match].split(".")[-1]
                lh = self.documents[doc][match:].split(".")[0]
                result[doc]  = fh+lh
                break
        return result

    def relevence(self, query):
        "Grade documents based on relavance"
        exact_matches = self.all_in_all(query)
        approx_matches = {}
        for doc in self.document_trees:
            matches = self.document_trees[doc].lcs(query, self.documents[doc])
            if len(matches) != 0:
                approx_matches[doc] = matches
        rel = []
        for doc in self.documents:
            cnt = 0
            if doc in exact_matches.keys():
                cnt +=10 * len(exact_matches[doc])
            if doc in approx_matches.keys():
                for ele in approx_matches[doc]:
                    if len(ele) > 3:
                        cnt += .1 * len(ele)
            rel.append( [doc, cnt] )
        rel.sort(key=lambda x: x[1], reverse=True)
        return [i for i in rel]
