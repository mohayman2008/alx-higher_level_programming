#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks whether a listint_t list is a palindrome or not
 * @head: pointer to pointer of first node of listint_t list
 *
 * Return: (1) if the list is palindrome or (0) elsewise
 */
int is_palindrome(listint_t **head)
{
	int len = 0, i = 0;
	int *list = NULL;
	listint_t *current;

	if (!head)
		return (0);
	if (!*head)
		return (1);

	current = *head;
	while (current)
		len++, current = current->next;

	list = malloc((len / 2 + 1) * sizeof(*list));
	if (!list)
		return (0);

	current = *head;
	while (current)
	{
		if (i <= len / 2)
			list[i] = current->n;
	        if (i >= len / 2 && list[len - i - 1] != current->n)
			return (0);
		current = current->next, i++;
	}

	return (1);
}
