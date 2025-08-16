#include "binary_trees.h"

/**
 * binary_tree_delete - a function to delete a binary tree
 * @tree: the tree to be deleted
 */

void binary_tree_delete(binary_tree_t *tree)
{
    binary_tree_t *tmp;

    if (tree == NULL)
        return;

    if (tree->right) {
        tmp = tree->right;
        binary_tree_delete(tmp);
        // free(tmp);
    }
    if (tree->left) {
        tmp = tree->left;
        binary_tree_delete(tmp);
        // free(tmp);
    }
    free(tree);
}