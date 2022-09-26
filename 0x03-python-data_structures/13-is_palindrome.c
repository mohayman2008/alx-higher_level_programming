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
	int len = 0, i = 0, result = 1, center;
	listint_t *current, *next, *previous = NULL, *middle, *last, *right;

	if (!head)
		return (0);
	if (!*head)
		return (1);

	current = *head;
	while (current)
		len++, current = current->next;

	center = len % 2 ? len / 2 : len / 2 - 1, middle = *head;
	for (; i < center ; i++)
		middle = middle->next;

	previous = NULL, next = current = middle->next;
	while (next)
		next = current->next, current->next = previous, previous = current,
		current = next;
	last = previous;

	current = *head, right = last;
	while (right)
	{
		if (right->n != current->n)
			result = 0;
		current = current->next, right = right->next;
	}

	previous = NULL, next = current = last;
	while (next)
		next = current->next, current->next = previous, previous = current,
		current = next;

	return (result);
}
