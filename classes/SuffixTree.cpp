#include "../headers/SuffixTree.h"

class SuffixTree {
    // static void main(string args[]){
    //     SuffixTree st = new SuffixTree()
    // }

    SuffixNode root;
    Active active;
    int remainingSuffixCount;
    End end;
    char input[];
    static char UNIQUR_CHAR = "$";

    public SuffixTree(char input[]) {
        this.input = new char[input.length+1];
        for(int i=0; i < input.length; i++){(
            this.input[i] = input[i];
        }
        this.input[input.length] = UNIQUE_CHAR;
    }

    public void build(){
        root = SuffixNode.createNode(1, new End(0));
        root.index = -1;
        active = new Active(root);
        this.end = new End(-1);

        for(int i=0; i < input.length; i++) {
            startPhase(i);
        }

        if (remainingSuffixCount != 0)  {
            cout<<"Something went wrong";
        }
        setIndexUsingDfs(root, 0, input.length);
    }

    public void startPhase(int i){
        SuffixNode lastCreatedInternalNode = NULL;
        end.end++;

        remainingSuffixCount++;

        while(remainingSuffixCount > 0){

            if(active.activeLength == 0){
                if(selectNode(i) != NULL){
                    active.activeEdge = selectNode(i).start;
                    active.activeLength++;
                    break;
                }
                else{
                    root.child[input[i]] = SuffixNode.createNode(i, end);
                    remainingSuffixCount--;
                }
            } else{

                try{
                    char ch = nextChar(i);

                    if(ch == input[i]){

                        if(lastCreatedInternalNode != NULL){
                            lastCreatedInternalNode.suffixLink = selectNode();
                        }

                        walkDown(i);
                        break;
                    }
                    else{
                        SuffixNode node = selectNode();
                        int oldStart = node.start;
                        node.start = node.start + active.activeLength;

                        SuffixNode newLeafNode = SuffixNode.createNode(i, this.end);

                        newInternalNode.child[input[newInternalNode.start + active.activeLength]] = node;
                        newInternalNode.child[input[i]] = newLeafNode;
                        newInternalNode.index = -1;
                        active.activeNode.child[input[newInternalNode.start]] = newInternalNode;

                        if(lastCreatedInternalNode != NULL){
                            lastCreatedInternalNode.suffixLink = newInternalNode;
                        }

                        lastCreatedInternalNode = newInternalNode;
                        newInternalNode.suffixLink = root;

                        if(active.activeNode != root){
                            active.activeNode = active.activeNode.suffixLink;
                        }
                        else{
                            active.activeEdge++;
                            active.activeLength--;
                        }
                        remainingSuffixCount--;
                    }
                } catch (EndOfPathException &e) {
                    SuffixNode node = selectNode();
                    node.child[input[i]] = SuffixNode.createNode(i, end);
                    if(lastCreatedInternalNode !+ NULL){
                        lastCreatedInternalNode.suffixLink = node;
                    }
                    lastCreatedInternalNode = node;

                    if(active.activeNode != root){
                        active.activeNode = acitve.activeNode.suffixLink;
                    }
                    else{
                        active.activeEdge++;
                        active.activeLength--;
                    }
                    remainingSuffixCount--;
                }
            }
        }
    }

    void walkDown(int index){
        SuffixNode node = selectNode();

        if(diff(node)  >= active.activeLength ){
            return input[active.activeNode.child[input.[active.activeEdge]].start + active.activeLength];
        }
        if(diff(node) + 1 == active.activeLength ){
                if(node.child[input[i]] != NULL ){
                    return input[i];
                }
        }
        else{
            active.activeNode = node;
            active.activeLength -= diff(node)-1;
            active.activeEdge += diff(node)+1;
            return nextChar(i);
        }
        throw EndOfPathException;
    }

    SuffixNode selectNode(){
        return active.activeNode.child[input[active.activeEdge]];
    }
    SuffixNode selectNode(int index){
        return active.activeNode.child[input[index]];
    }

    int diff(SuffixNode node){
        return node.end.end - node.start;
    }

    void setIndexUsingDfs(SuffixNode root, int val, int size){
        if(root == NULL){
            return;
        }
        val += root.end.end -root.start+ 1;

        if(root.index != -1){
            root.index = size - val;
            return;
        }

        for(SuffixNode node : root.child){
            setIndexUsingDfs(node, val, size);
        }

    }

    public void dfsTraversal(){
        vector<char> result = new vector<char>();
        for(SuffixNode node : root.child){
            dfsTraversal(node, result);
        }
    }

    void dfsTraversal(SuffixNode root, vector<char> result){
        if(root == NULL){
            return;
        }
        if(root.index != -1){
            for(int i=root.start; i <= root.end.end; i++){
                result.add(input[i]);
            }
        }
    }
}
