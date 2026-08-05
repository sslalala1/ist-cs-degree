/**
 * Invoice linked list implementation
 * @file invoice.c
 * @author ist187565 (Simone Dias)
 */

#include <stdlib.h>
#include "invoice.h"
#include <string.h>
#include <stdio.h>

#define ENOMEMORY "No memory.\n"		/**< memory exausted	*/


/** 
 * Creates an empty invoice list
 * @return an empty invoice list  
 */
InvoiceList *mk_invoice_list() {
    InvoiceList *list = malloc(sizeof(InvoiceList));

    if (list == NULL) {
        printf(ENOMEMORY);
        return NULL;
    }

    list->next_number = 1;
    list->total_items = 0;
    list->total_value = 0;
    list->head = NULL;

    return list; 
}

/** Adds a new invoice at the tail of the invoice list 
 * @param list pointer to list of invoices 
 * @param nif client's nif
 * @param name pointer to client's name
 * @param total_items number of items bought in an invoice
 * @param total_value total value paid in an invoice
 * @return a pointer to the added InvoiceNode or NULL if memory exhausted
*/
InvoiceNode *add_invoice(InvoiceList *list, int nif, char *name, 
int total_items, double total_value) {
    
    InvoiceNode *node = malloc(sizeof(InvoiceNode));
    if(node == NULL) {
        printf(ENOMEMORY);
        return NULL;
    }

    /**copies name string into newly allocated memory */
    node->name = strdup(name);
    if(node->name == NULL) {
        free(node);
        printf(ENOMEMORY);
        return NULL;
    }

    node->nif = nif;
    node->total_items = total_items;
    node->total_value = total_value;
    node->number = list->next_number;
    list->next_number++;

    node->next = NULL;

    /**if list is empty, head becomes the new node */
    if(list->head == NULL) {
        list->head = node;
    }

    /**if list not empty, jumps nodes until it finds the last one */
    else {
        InvoiceNode *current = list->head;
        while(current->next != NULL)
            current = current->next;
        
        current->next = node;
    }

    list->total_items +=total_items;
    list->total_value +=total_value;

    return node;
}

/** Finds invoice in invoice list by its number
 * @param list pointer to list of invoices
 * @param number invoice number
 * @return a pointer to the InvoiceNode if number found, NULL if not
*/
InvoiceNode *find_invoice(InvoiceList *list, int number) {
    InvoiceNode *current = list->head;

    while(current != NULL) {
        if(current->number == number)
            return current;
        
        current = current->next;
    }

    return NULL;
}

/**
 * Removes invoice from invoice list
 * @param list pointer to list of invoices
 * @param number number of invoice to be removed
 * @return -1 if invoice not found or 1 when found and removed
 */
int remove_invoice(InvoiceList *list, int number) {
    
    InvoiceNode *invoice_found = find_invoice(list,number);

    if(invoice_found == NULL)
        return -1;

    /**if invoice to be removed is the head */
    if(invoice_found == list->head)
        list->head = invoice_found->next;
    
    /**finds the node before the invoice to be removed, skips over the removed node
     * and connects the previous node to the one after
     */
    else {
        InvoiceNode *current = list->head;
        while(current != NULL && current->next != invoice_found) {
            current = current->next;
        }
        current->next = invoice_found->next;
    }

    list->total_items -= invoice_found->total_items;
    list->total_value -= invoice_found->total_value;

    free(invoice_found->name);
    free(invoice_found);

    return 1; 
}

/**
 * Frees all memory taken by the invoice list
 * @param list pointer to the list of invoices
 */
void free_invoice_list(InvoiceList *list) {
    InvoiceNode *current = list->head;

    while(current != NULL) {
        InvoiceNode *next = current->next;
        free(current->name);
        free(current);

        current = next;
    }

    free(list);
}