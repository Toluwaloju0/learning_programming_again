#include "binary_trees.h"

/**
 * binary_tree_insert_left - a function to insert a node to the left of the binary tree
 * @parent: the parent node of the new node
 * @value: the value of the new node
 *
 * Return: a pointer to the new node
 */



binary_tree_t *binary_tree_insert_left(binary_tree_t *parent, int value)
{
    binary_tree_t *new, *tmp = NULL;

    if (parent == NULL)
        return NULL;

    new = binary_tree_node(parent, value);
    if (new == NULL)
        return NULL;

    if (parent->left)
    {
        tmp = parent->left;
        tmp->parent = new;
    }
    parent->left = new;
    new->left = tmp;

    return new;
}