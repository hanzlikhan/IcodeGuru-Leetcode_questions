#include <iostream>
#include <stack>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

void process(int value) {
    // This is where you define what PROCESS does
    std::cout << value << " ";
}

void preOrderTraversal(TreeNode* root) {
    if (root == NULL) return;

    // Initialize the stack with NULL and set PTR to root
    std::stack<TreeNode*> stack;
    stack.push(NULL);
    TreeNode* PTR = root;

    while (PTR != NULL) {
        // Apply PROCESS to INFO[PTR]
        process(PTR->val);

        // If there is a right child, push it onto the stack
        if (PTR->right != NULL) {
            stack.push(PTR->right);
        }

        // If there is a left child, move PTR to the left child
        // Else, pop from the stack
        if (PTR->left != NULL) {
            PTR = PTR->left;
        } else {
            PTR = stack.top();
            stack.pop();
        }
    }
}

int main() {
    // Create a sample tree: 
    //      1
    //     / \
    //    2   3
    //   / \
    //  4   5
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);

    std::cout << "Pre-order traversal: ";
    preOrderTraversal(root);
    std::cout << std::endl;

    // Clean up dynamically allocated memory
    delete root->left->right;
    delete root->left->left;
    delete root->right;
    delete root->left;
    delete root;

    return 0;
}
