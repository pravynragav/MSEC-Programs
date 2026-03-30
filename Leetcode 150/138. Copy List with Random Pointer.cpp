
class Solution {
public:
    RandomListNode *copyRandomList(RandomListNode *head) {
        unordered_map<RandomListNode*, RandomListNode*>m;
        auto p = head;
        while(p){
            m[p] = new RandomListNode(p->label);
            p = p->next;
        }
        p = head;
        while(p){
            m[p]->next = m[p->next];
            m[p]->random = m[p->random];
            p = p->next;
        }
        return m[head];
    }
};
