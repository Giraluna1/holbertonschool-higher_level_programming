#include "lists.h"

/**
 * insert_node - function to insert sort new node on list
 * @head: beegining the list
 * @number: value of node
 */

listint_t *insert_node(listint_t **head, int number)
{
listint_t *new_node, *ptr1, *ptr2;
int i;

new_node = malloc(sizeof(listint_t));
if (!new_node)
    return (NULL);

new_node->n = number;
new_node->next = NULL;    

if (*head == NULL)
{
    *head = new_node;
    return (new_node);
}

ptr1 = *head;
ptr2 = *head;

ptr1 = ptr1->next;
for (i = 0; ptr1 != NULL; i++)
{
    if(ptr1->n >= number)
    {
        ptr2->next = new_node;
        new_node->next = ptr1;
        break;
    }
    else
    {
        ptr1 = ptr1->next;
        ptr2 = ptr2->next;
    }
}
if(!ptr1)
{
    ptr2->next = new_node;
    new_node->next = ptr1;
}
 return (new_node);

}