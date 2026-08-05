/**
 * Header file for invoice linked list
 * @file invoice.h
 * @author ist187565 (Simone Dias)
 */

/**Node to a linked list of invoices */
typedef struct InvoiceNode {
    int number; /**< invoice number */
    int nif; /**< client nif */
    char *name; /**< name of the client */
    int total_items; /**< total items bought in 1 invoice */
    double total_value; /**< total value paid */
    struct InvoiceNode *next; /**< pointer to the next invoice in the list */
} InvoiceNode;

/** Linked list of all the invoices created */
typedef struct InvoiceList {
    InvoiceNode *head; /**< pointer to the first invoice of the list */
    int next_number; /**< number to be assigned to the next invoice */
    int total_items; /**< total items bought across all invoices */
    double total_value; /**< total value paid across all invoices */
} InvoiceList;

/** Creates an empty invoice list */
InvoiceList *mk_invoice_list();

/** Frees all memory taken by the invoice list  */
void free_invoice_list(InvoiceList *list);

/** Adds a new invoice at the tail of the invoice list */
InvoiceNode *add_invoice(InvoiceList *list, int nif, char *name,
int total_items, double total_value);

/** Finds invoice by its number */
InvoiceNode *find_invoice(InvoiceList *list, int number);

/** Removes an invoice by its number */
int remove_invoice(InvoiceList *list, int number);