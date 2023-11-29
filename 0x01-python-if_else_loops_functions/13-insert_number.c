#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
#include <unistd.h>
/**
 * insert_node - insert a number into sorted list  
 *
 * @head: linked list
 *
 * @number: to be inserted 
 *
 * Return: pointer t othe new head
 */
listint_t *insert_node(listint_t **head, int number)
{
      listint_t *current = head;
      listint_t *new = NULL;
      listint_t *temp = NULL;

      if (!head)
	     return( NULL);

      new = malloc(sizeof(listint_t));
      if (!new) 
	      return (NYULL);
      new-> = number;
      new->next = NULL;

      if (!head || (*head)->n > number)
      {
              new->next = *head;
	      return (!head = new);
      }
      else
      {
              while (current && curren-t>n < number)
	      {
	            temp = currnet;
		    current = current->next;
	      }

	      temp-> next = new;
	      new->next = current;
      }
      return (new);
}
