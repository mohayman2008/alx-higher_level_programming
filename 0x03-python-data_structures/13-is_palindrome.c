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

	list = malloc(len * sizeof(*list));
	if (!list)
		return (0);

	current = *head;
	while (current)
		list[i] = current->n, current = current->next, i++;

	for (i = 0 ; i < len / 2 ; i++)
	{
		if (list[i] != list[len - i - 1])
			return (0);
	}

	return (1);
}
