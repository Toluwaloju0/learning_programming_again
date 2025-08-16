#include "binary_trees.h"

/**
 * binary_tree_node - a function to create a new node on a binary tree
 * @parent: the parent of the node to create
 * @value: integer value for the new node
 * Return: a pointer to the new node
  */

binary_tree_t *binary_tree_node(binary_tree_t *parent, int value)
{
    binary_tree_t *new;

    new = malloc(sizeof(binary_tree_t));
    if (new == NULL)
        return NULL;

    new->n = value;
    new->parent = parent;
    new->right = NULL;
    new->left = NULL;

    return new;
}