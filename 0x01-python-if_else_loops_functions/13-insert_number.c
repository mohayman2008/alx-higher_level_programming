#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list listint_t
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current, *previous;

	if (!head)
		return (NULL);
	current = *head;

	new = malloc(sizeof(*new));
	if (new == NULL)
		return (NULL);

	new->n = number;
	if (!*head || (*head)->n >= number)
	{
		new->next = *head;
		*head = new;
	}
	else
	{
		previous = *head;
		current = (*head)->next;
		do {
			if (current->n >= number)
			{
				new->next = current;
				previous->next = new;
				break;
			}
			else if (current->next == NULL)
			{
				new->next = current->next;
				current->next = new;
				break;
			}
			previous = current;
			current = current->next;
		} while (current);
	}

	return (new);
}
