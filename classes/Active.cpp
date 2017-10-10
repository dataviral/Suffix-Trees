#include "../headers/Active.h"

class Active{

    SuffixNode activeNode;
    int activeEdge;
    int active Length;

    Active(SuffixNode node){
        activeLength = 0;
        activeNode = node;
        activeEdge = -1;
    }

    string toString() {
        return "Active [activeNode=]" + activeNode + ", activeIndex="
                        + activeEdge + ", activeLength=" + activeLength + "]";
    }

}
