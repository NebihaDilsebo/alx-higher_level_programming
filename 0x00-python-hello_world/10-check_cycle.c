#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linkedlist contains a cycle
 * @list: a singly linked lists
 *
 * Return: if there is no cycle - 0.
 * if there is a cycle - 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if
