#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * reverse_list - Reverses a singly linked list.
 * @head: Double pointer to the head of the list.
 * Return: Pointer to the new head of the reversed list.
 */
listint_t *reverse_list(listint_t *head)
{
    listint_t *prev = NULL;
    listint_t *current = head;
    listint_t *next = NULL;

    while (current != NULL)
    {
        next = current->next;  // Store next node
        current->next = prev;  // Reverse current node's pointer
        prev = current;        // Move pointers one position forward
        current = next;
    }
    return prev;
}

/**
 * find_middle - Finds the middle of the list.
 * @head: Pointer to the head of the list.
 * Return: Pointer to the middle node of the list.
 */
listint_t *find_middle(listint_t *head)
{
    listint_t *slow = head;
    listint_t *fast = head;

    while (fast != NULL && fast->next != NULL)
    {
        slow = slow->next;
        fast = fast->next->next;
    }
    return slow;
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Double pointer to the head of the list.
 * Return: 1 if the list is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
    if (head == NULL || *head == NULL)
        return 1;  // Empty list is considered a palindrome

    listint_t *middle = find_middle(*head);
    listint_t *second_half = reverse_list(middle);
    listint_t *first_half = *head;
    listint_t *temp = second_half;
    int is_pal = 1;

    // Compare first half and reversed second half
    while (second_half != NULL)
    {
        if (first_half->n != second_half->n)
        {
            is_pal = 0;
            break;
        }
        first_half = first_half->next;
        second_half = second_half->next;
    }

    // Restore the list (optional)
    reverse_list(temp);

    return is_pal;
}

