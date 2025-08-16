#include "binary_trees.h"

/**
 * binary_tree_insert_right - a function to insert a node to the right of the parent node
 * @parent: the parent node
 * @value: the value to be added to the node
 *
 * Return: a pointer to the new node
 */

binary_tree_t *binary_tree_insert_right(binary_tree_t *parent, int value)
{
    binary_tree_t *new, *tmp = NULL;

    if (parent == NULL)
        return NULL;

    new = binary_tree_node(parent, value);
    if (new == NULL)
        return NULL;

    if (parent->right) {
        tmp = parent->right;
        tmp->parent = new;
    }
    parent->right = new;
    new->right = tmp;

    return new;
}