#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if listint_t list contains a cycle or not
 * @list: pointer to head of list
 *
 * Return: 1 if a cycle was found or 0 elsewise
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (!list)
		return (0);

	slow = fast = list;
	while (slow && slow->next)
	{
		slow = slow->next;
		if (fast->next && fast->next->next)
			fast = fast->next->next;
		else
			return (0);

		if (slow == fast)
			return (1);
	}

	return (0);
}
