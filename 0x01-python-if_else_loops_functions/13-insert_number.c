#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include "lists.h"

/**
 *insert_node - function to insert number into list
 *@head: linked lists
 *@number: number to be inserted
 *Return: pointer to new head
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr = *head;
	listint_t *new = NULL;
	listint_t *tem = NULL;

	if (!head)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (!*head || (*head)->n > number)
	{
		new->next = *head;
		return (*head = new);
	}
	else
	{
		while (curr && curr->n < number)
		{
			tem = curr;
			curr = curr->next;
		}
		tem->next = new;
		new->next = curr;
	}
	return (new);
}
