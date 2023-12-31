/*
 * File: 13-insert_number.c
 * Auth: Samuel Stanley
 */

#include "lists.h"

/**
 * insert_node - this inserst a number inside a sorted singly-linked list.
 * @head: points to head of linked list
 * @number: The number to insert
 *
 * Return: if the function fails - NULL.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}
