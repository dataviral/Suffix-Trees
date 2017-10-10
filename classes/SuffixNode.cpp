#include "../headers/SuffixNode.h"

class SuffixNode{
    public:
        final int TOTAL = 256;
        SuffixNode[] child = new SuffixNode[TOTAL];

        int start;
        End  end;
        int index;

        SuffixNode suffixLink;

        public static SuffixNode createNode(int start, End, end){
            SuffixNode node = new SuffixNode();
            node.start = start;
            node.end = end;
            return node;
        }

        public string toString(){
            string str = new string();
            int i=0;
            for(SuffixNode node: child){
                if(node != null){
                    str += (char)i + " ";
                }
                i++;
            }
            return "SuffixNode [start=" + start + "]" + " " + str;
        }

}
