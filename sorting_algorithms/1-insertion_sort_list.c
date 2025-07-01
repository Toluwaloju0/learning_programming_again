#include "sort.h"

/**
 * insertion_sort_list - A function to sort a linked list of numbers
 *
 * @list: the head of the linked list
 */

void insertion_sort_list(listint_t **list)
{
	listint_t *temp, *prev, *head, *next;

	if (!list)
		return;
	
	head = *list;

	while(head)
	{
		if (!head->prev)
		{
			head = head->next;
			continue;
		}
		if (head->prev->n > head->n)
		{
			prev = head->prev;
			next = head->next;
			head->prev = prev->prev;
			head->next = prev;
			if (prev->prev)
				prev->prev->next = head;
			prev->next = next;
			prev->prev = head;
			if (next)
				next->prev = prev;
			/* to print the linked list */
			temp = head;
			while (temp->prev)
				temp = temp->prev;
			print_list(temp);
			*list = temp;
			continue;
		}
		head = head->next;
	}
}