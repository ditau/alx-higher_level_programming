#include "lists.h"

/**
 * palindrome - recusive palindrome or not
 * @head: head list
 * Return: 0  if it is not a palindrome
 * 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (chk_palind(head, *head));
}

/**
 * chk_palind - funct to check if it is a palindrome
 * @head: head list
 * @end: end list
 */
int chk_palind(listint_t **head, listint_t *end)
{
	if end == NULL
		return (1);
	if (chk_palind(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
