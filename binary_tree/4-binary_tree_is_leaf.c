#include "binary_trees.h"

/**
 * binary_tree_is_leaf - a function to check if a binary node is a leaf
 * @node: the node to check
 *
 * Return: 1 if node is a leaf and 0 if not
 */

int binary_tree_is_leaf(const binary_tree_t *node)
{
    if (node == NULL)
        return 0;

    if (node->right || node->left)
        return 0;
    return 1;
}