class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if (p == nullptr && q == nullptr) {  // Both trees are empty
            return true;
        } else if (p == nullptr || q == nullptr) {  // Only one tree is empty
            return false;
        } else if (p->val != q->val) {  // Node values don't match
            return false;
        } else {
            // Recursively check subtrees
            return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
        }
    }
};
