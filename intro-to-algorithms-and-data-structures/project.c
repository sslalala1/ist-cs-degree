/* iaed26 - ist187565 - project */

/**
 * A program exemplifying a product and invoice management system
 * @file project.c
 * @author ist187565 (Simone Dias)
 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include "invoice.h"

#define DESC_MAX 50             /**< max. len. of product description */
#define EAN_MAX 13              /**< max. len. of EAN */
#define PRODUCTS_MAX 10000      /**< max. number of products in the warehouse*/

#define EINVALIDEAN "invalid ean\n"             /**< invalid EAN */
#define EINVALIDIVA "invalid iva\n"             /**< invalid iva */
#define EINVALIDPRICE "invalid price\n"         /**< invalid price */
#define EINVALIDQTY "invalid quantity\n"        /**< invalid product quantity*/
#define EINVALIDDESC "invalid description\n"    /**< invalid prod description*/
#define EPRODINUSE "product in use\n"           /**< product in cart */
#define EINVALIDPROD "invalid product\n"        /**< invalid product */
#define EINVALIDNIF "%d: no such nif\n"         /**< invalid nif */
#define EINVALIDNAME "invalid name\n"           /**< invalid name */
#define EINVALIDCLIENT "%s: no such client\n"   /**< client not found */
#define ENOMEMORY "No memory.\n"                /**< memory exhausted */
#define ENOSUCHPROD "%s: no such product\n"     /**< product not in warehouse*/

/** Represents a product in the warehouse */
typedef struct Product {
    char description [DESC_MAX + 1];    /**< product description */
    char ean [EAN_MAX + 1];             /**< product EAN */
    double price;                       /**< product price */
    char iva;                           /**< product iva */
    int quantity_available;             /**< product quantity available */
    int quantity_sold;                  /**< product quantity sold */
} Product;

/** Represents IVA including class and percentage */
typedef struct Iva {
    char class;         /**< iva class */
    int percentage;     /**< iva percentage */

} Iva;

/** Represents a product in the cart */
typedef struct Cart_Product {
    int quantity;               /**< product quantity in the cart */
    char ean [EAN_MAX +1];      /**< product ean */
} Cart_Product;

/**
 * Searches for a product in the warehouse by its ean
 * @param warehouse The array containing all registered products
 * @param total_products Number of different products in the warehouse
 * @param product_ean EAN of the product being searched
 * @return Product index in the array if found, return -1 if not 
 */
int find_product(Product warehouse[], int total_products, char product_ean[]) {
    int i;
    for(i=0;i<total_products;i++) {
        if(strcmp(warehouse[i].ean, product_ean) == 0)
            return i;
    }
    return -1;
}

/**
 * Searches for a product in the cart by its ean
 * @param cart The array containing all products in the cart
 * @param cart_products Number of different products in the cart
 * @param ean EAN of the product being searched
 * @return Product index in the array if found, returns -1 if not 
 */
int find_product_cart(Cart_Product cart[], int cart_products, char ean[]) {
    int i;
    for(i=0;i<cart_products;i++) {
        if(cart[i].quantity>0)
            if(strcmp(cart[i].ean, ean) == 0)
                return i;
    }
    return -1;
}

/**
 * Checks if EAN is valid
 * @param product_ean The string containing the product EAN
 * @return 1 if EAN is valid or 0 if not
 */
int check_ean(char product_ean[]) {
    int sum=0;
    int verification_digit;
    int calculated_verification_digit;
    int len = strlen(product_ean);
    int digit, i;

    if(len!=8 && len!=13) {
        return 0;
    }

    for(i=0;i<(len-1);i++) {
        /** transforms string character into numeric value */
        digit = product_ean[i] - '0';

        /** sums digits in even positions with digits in odd 
         * positions multiplied by 3 */
        if(i%2==0)
            sum += digit;
        else
            sum += digit*3;
        }
    
    calculated_verification_digit = ((10-(sum%10))%10);
    verification_digit = product_ean[len-1] - '0';

    return(calculated_verification_digit==verification_digit);
}


/**
 * Counts the number of IVA classes when given a file
 * @param arg_count Number of command lines passed to the program
 * @param arg_vector Array with command line strings: arg_vecto[0] is 
 * program name, arg_vector[1] is filename if given
 * @param iva_rates Array with all iva classes and its corresponding 
 * percentage
 * @return Number of iva classes if given a file or 4 if not
 */
int iva_count(int arg_count,char *arg_vector[], Iva iva_rates[]) {
    int count = 0;

    iva_rates[0].class = 'A'; iva_rates[0].percentage = 0;
    iva_rates[1].class = 'B'; iva_rates[1].percentage = 6;
    iva_rates[2].class = 'C'; iva_rates[2].percentage = 13;
    iva_rates[3].class = 'D'; iva_rates[3].percentage = 23;

    /** file with IVA classes was given */
    if(arg_count>1) {
        FILE *myfile = fopen(arg_vector[1], "r");
        if(myfile!=NULL) {
            while(count<26 && fscanf(myfile," %c %d", &iva_rates[count].class,
            &iva_rates[count].percentage)==2)
                count++;
            fclose(myfile);
            if(count > 0) return count;
        }
    }
    /** no file was given */
    return 4;
}

/**
 * Command p: adds or updates a product to the warehouse
 * @param warehouse Array containing all registered products
 * @param cart Array containing the products in the cart
 * @param total_products Total products currently registered in the warehouse
 * @param cart_products Number of products in the cart
 * @param iva_rates Array with all iva classes and their corresponding
 * percentage
 * @param num_iva  Number of iva classes
 * @return Stock quantity of added/updated product
 */
int process_product(Product warehouse[], Cart_Product cart[],
int total_products, int cart_products, Iva iva_rates[], int num_iva) {
    char ean[1000];
    char iva;
    double price;
    int quantity;
    char description [1000];
    int i,j;

    scanf(" %s %c %lf %d %[^\n]", ean, &iva, &price, &quantity, description);

    i = find_product(warehouse, total_products, ean);

    if(check_ean(ean)!=1) {
        printf(EINVALIDEAN);
        return total_products;
    }
    
    int found_iva = 0;
    for(j=0;j<num_iva;j++) {
        if(iva==iva_rates[j].class) {
            found_iva = 1;
            break;
        }
    }

    if(found_iva==0) {
        printf(EINVALIDIVA);
        return total_products;
    }

    if(price<=0) {
        printf(EINVALIDPRICE);
        return total_products;
    }
    
    if(quantity<0) {
        printf(EINVALIDQTY);
        return total_products;
    }
    
    if(strlen(description)>DESC_MAX || 
    (description[0]>='a' && description[0]<='z')) {
        printf(EINVALIDDESC);
        return total_products;
    }
    
    /** product already registered in the warehouse */
    if(i!=-1) {
        /** product in the cart and price change */
        if(find_product_cart(cart,cart_products,ean)!=-1 &&
        warehouse[i].price!=price) {
            printf(EPRODINUSE);
            return total_products;
        }

        /** allows updates when price has not changed */
        warehouse[i].iva = iva;
        warehouse[i].price = price;
        warehouse[i].quantity_available += quantity;
        strcpy(warehouse[i].description, description);

        printf("%d\n", warehouse[i].quantity_available);
        return total_products;
    }

    /**product not in the warehouse */
    else if(i==-1) {
        if(total_products >= PRODUCTS_MAX) {
            printf(EINVALIDPROD);
            return total_products;
        }
        else {
            strcpy(warehouse[total_products].description, description);
            strcpy(warehouse[total_products].ean, ean);
            warehouse[total_products].price = price;
            warehouse[total_products].iva = iva;
            warehouse[total_products].quantity_available = quantity;
            warehouse[total_products].quantity_sold = 0;

            printf("%d\n", warehouse[total_products].quantity_available);
            return total_products+1;
        }
    }
    return total_products;
}

/**
 * Matches wildcard pattern with product EAN
 * @param input String with wildcard input
 * @param i_input Position in input string
 * @param ean String with product EAN
 * @param i_ean Position in EAN string
 * @return 1 when match, 0 if not
 */
int wildcard_match(char input[], int i_input, char ean[], int i_ean) {
    /** base case: both strings ended */
    if(input[i_input]=='\0' && ean[i_ean]=='\0')
        return 1;
    
    /** input ended before EAN -> no match */
    if(input[i_input]=='\0')
        return 0;

    if(input[i_input]=='*') {
        /** when '*' means zero characters -> moves to the next 
         * character in input */
        if(wildcard_match(input, i_input+1, ean, i_ean)) return 1;

        /** when '*' means one or more characters -> moves to the next
         * character in ean */
        if(ean[i_ean]!='\0' && 
        wildcard_match(input, i_input, ean, i_ean+1)) return 1;

        return 0;
    }

    /** handles ? or exact match */
    if(input[i_input]=='?' || input[i_input]==ean[i_ean]) {
        if(ean[i_ean] != '\0')
            return wildcard_match(input, i_input+1, ean, i_ean+1);
    }
    return 0;
}

/**
 * Command l: lists all the products in the warehouse
 * Uses wildcard matching where '*' can match any sequence and '?'
 * matches a single character
 * If no arguments or '*' lists all the products with stock > 0
 * Otherwise, lists products matching the wildcard pattern
 * @param warehouse Array containing all registered products in the warehouse
 * @param total_products Number of products registered in the warehouse
 */
void lists_products(Product warehouse[], int total_products) {
    char input[1000];
    int c;
    int i;
    c = getchar();

    /** ignores the spaces and gets next character */
    while(c==' ') 
        c=getchar();

    /** User just writes 'l' */
    if(c=='\n' || c == EOF) {
        if(total_products==0) {
            printf("*: no such product\n");
        }
        else {
            int found_any = 0;
            for(i=0;i<total_products;i++) {
                if(warehouse[i].quantity_available>0) {
                    printf("%s %c %.2lf %d %d %s\n", warehouse[i].ean, 
                    warehouse[i].iva, warehouse[i].price, 
                    warehouse[i].quantity_sold,
                    warehouse[i].quantity_available, 
                    warehouse[i].description);

                    found_any = 1;
                }
            }
            if(found_any == 0) 
                printf("*: no such product\n");
        }
    }
    
    /** User writes complete EAN or wildcard pattern */
    else {
        ungetc(c, stdin);

        while(scanf("%s", input)==1) {
            int found_match = 0;
            
            for(i=0;i<total_products;i++) {

                if(wildcard_match(input, 0, warehouse[i].ean, 0)==1) {
                    found_match = 1;

                    if(warehouse[i].quantity_available>0) {
                        printf("%s %c %.2lf %d %d %s\n", warehouse[i].ean, 
                        warehouse[i].iva, warehouse[i].price, 
                        warehouse[i].quantity_sold,
                        warehouse[i].quantity_available, 
                        warehouse[i].description);

                        
                    }
                }
            }
            
            if(found_match==0)
                printf(ENOSUCHPROD, input);
            
            c = getchar();
            while(c==' ') 
                c = getchar();

            if (c == '\n' || c==EOF) {
                break;
            }
            else ungetc(c, stdin);
        }
    }
}

/**
 * Calculates the total price with iva
 * @param price Unitary price
 * @param quantity Number of products 
 * @param iva_rate Iva percentage to apply 
 */
double price_with_iva(double price, int quantity, int iva_rate) {
    double total_price = (double)quantity * price;
    double total_w_iva = total_price+(total_price*(double)(iva_rate/100.0));
    double total_rounded = (long long)((total_w_iva*100)+0.5+1e-9) / 100.00;

    return total_rounded;    
}

/**
 * Prints all the information of a product in the cart
 * Includes iva class, price, quantity, price with iva and product description
 * @param warehouse_product Array with all the warehouse product information
 * @param cart_product Array with all the cart product information
 * @param iva_rates Array with all iva classes and their corresponding 
 * percentage
 * @param num_iva Number of iva classes
 */
void prints_cart_product(Product warehouse_product, Cart_Product cart_product,
Iva iva_rates[], int num_iva) {
    int j;
    int iva_rate = 0;

    /**finds the iva rate assigned to iva class  */
    for(j=0;j<num_iva;j++) {
        if(warehouse_product.iva == iva_rates[j].class) {
            iva_rate = iva_rates[j].percentage;
            break;
        }
    }

    /**applies iva rate to products in the cart */
    double price_iva = price_with_iva(warehouse_product.price,
    cart_product.quantity, iva_rate);

    printf("%c %.2lf %d %.2lf %s\n",
    warehouse_product.iva,
    warehouse_product.price,
    cart_product.quantity,
    price_iva,
    warehouse_product.description);
}

/**
 * Lists products in cart ordered by ean
 * @param cart Array containing all products in the cart
 * @param warehouse Array containing all registered products in the warehouse
 * @param total_products Total products currently registered in the warehouse
 * @param cart_products Number of products in the cart
 * @param iva_rates Array with all iva classes and their corresponding
 * percentage
 * @param num_iva  Number of iva classes
 */
void lists_cart(Cart_Product cart[], Product warehouse[], int total_products,
int cart_products, Iva iva_rates[], int num_iva) {
    int i, j, done;
    int i_warehouse;

    /**bubble sort to sort products by ean */
    for (i=0;i<cart_products-1;i++) {
        done = 1;   
        for (j=cart_products-1;j>i;j--) {
            if (strcmp(cart[j].ean, cart[j-1].ean) < 0) {
                Cart_Product temp = cart[j-1]; /**saves a copy of j-1 */
                cart[j-1] = cart[j]; /**overwrites j-1 with j */
                cart[j] = temp; /**saved j-1 goes into j */
                
                done = 0; 
            }
        }
        if(done) break; 
    }
    /**prints all products in the cart sorted by ean */
    for(i=0;i<cart_products;i++) {
        if(cart[i].quantity>0) {
            i_warehouse = find_product(warehouse,total_products,cart[i].ean);

            prints_cart_product(warehouse[i_warehouse],cart[i],
            iva_rates,num_iva);
        }
    }
}

/**
 * Command a: Adds product to cart
 * @param warehouse Array containing all registered products in the warehouse
 * @param cart Array containing the products in the cart
 * @param total_products Total products currently registered in the warehouse
 * @param cart_products Number of products in the cart
 * @param iva_rates Array with all iva classes and their corresponding
 * percentage
 * @param num_iva  Number of iva classes
 * @return Updated number of products in the cart
 */
int add_to_cart(Product warehouse[], Cart_Product cart[], Iva iva_rates[],
int cart_products, int total_products, int num_iva) {
    
    char rest_of_input[100];
    char ean[EAN_MAX+1];
    int qty_to_add = 1;
    int i_warehouse, i_cart;

    if (fgets(rest_of_input, 100, stdin) == NULL) 
        return cart_products;
    
    int arguments = sscanf(rest_of_input,"%d %s", &qty_to_add, ean); 

    /**command a with no arguments */
    if(arguments<1) {
        lists_cart(cart,warehouse,total_products,
        cart_products,iva_rates,num_iva);
        return cart_products;
    }

    /**considers quantity=1 if ean with no quantity */
    else if(arguments==1) {
        sscanf(rest_of_input, "%s", ean);
        qty_to_add = 1;
    }

    if(check_ean(ean)!=1) {
        printf(EINVALIDEAN);
        return cart_products;
    }

    i_warehouse = find_product(warehouse, total_products, ean);
    i_cart = find_product_cart(cart, cart_products, ean);

    /**product not in the warehouse */
    if (i_warehouse == -1) {
        printf(ENOSUCHPROD, ean);
        return cart_products;
    }
    
    /**user wants to remove product quantity from cart */
    if(qty_to_add<0) {
        int abs_qty = -qty_to_add; 
        
        if(i_cart==-1) {
            printf(EINVALIDQTY);
            return cart_products;
        }

        if (cart[i_cart].quantity < abs_qty) {
            printf(EINVALIDQTY);
            return cart_products;
        }

        /**updates quantity availabe and sold in the warehouse */
        warehouse[i_warehouse].quantity_available += abs_qty;
        warehouse[i_warehouse].quantity_sold -= abs_qty;
        cart[i_cart].quantity -= abs_qty;
    }

    /**user wants do add product quantity to cart */
    if(qty_to_add>0) {
        /**checks warehouse stock */
        if(warehouse[i_warehouse].quantity_available<qty_to_add) {
            printf("no stock\n");
            return cart_products;
        }

        /**updates cart quantity if product already in cart */
        if (i_cart != -1) {
            cart[i_cart].quantity += qty_to_add;
        } 
        /**adds product to cart if product not yet in cart */
        else {
            strcpy(cart[cart_products].ean, ean);
            cart[cart_products].quantity = qty_to_add;
            i_cart = cart_products; 
            cart_products++;
        }

        warehouse[i_warehouse].quantity_available -= qty_to_add;
        warehouse[i_warehouse].quantity_sold += qty_to_add;
    }

    /**prints product whether it was added or removed */
    if (i_cart != -1) {
        prints_cart_product(warehouse[i_warehouse], cart[i_cart], 
        iva_rates, num_iva);
    }

    return cart_products;
}

/**
 * Command d: Removes product or invoice
 * @param warehouse Array containing all registered products in the warehouse
 * @param cart Array contanining all products in the cart
 * @param invoices Pointer to invoice list
 * @param total_products Total products currently registered in the warehouse
 * @param cart_products Number of products in the cart
 * @return Updated number of products in the warehouse 
 */
int removes_prod_inv(Product warehouse[], Cart_Product cart[],
InvoiceList *invoices, int total_products, int cart_products) {
    
    char rest_of_input[100];
    char ean[EAN_MAX+1];
    int i,j;
    int qty_to_delete, invoice_num;

    fgets(rest_of_input,100,stdin);

    /**user writes ean and quantity */
    if(sscanf(rest_of_input, "%s %d", ean, &qty_to_delete)==2) {
        if(check_ean(ean)!=1) {
            printf(EINVALIDEAN);
            return total_products;
        }
        
        i = find_product(warehouse, total_products, ean);

        if(i==-1) {
            printf(ENOSUCHPROD, ean);
            return total_products;
        }

        if(find_product_cart(cart,cart_products,ean)!=-1) {
            printf(EPRODINUSE);
            return total_products;
        }
        
        if(qty_to_delete>warehouse[i].quantity_available || qty_to_delete<=0) {
            printf(EINVALIDQTY);
            return total_products;
        }

        else {
            warehouse[i].quantity_available -= qty_to_delete;

            printf("%d %s\n", 
            warehouse[i].quantity_available,
            warehouse[i].description);

            /**final quantity=0 -> removes from warehouse */
            if(warehouse[i].quantity_available==0) {
                for(j=i;j<total_products-1;j++) {
                    warehouse[j]=warehouse[j+1];
                }
                total_products--;
            }
        }
    }
    
    /**user writes invoice number */
    else if(sscanf(rest_of_input, "%d", &invoice_num)==1) {
        InvoiceNode *invoice = find_invoice(invoices, invoice_num);
        
        if(invoice==NULL) {
            printf("%d: no such invoice\n", invoice_num);
        }

        /**removes invoice but products are not restocked */
        else {
            printf("%.2f %d %s\n", invoice->total_value, invoice->nif,
            invoice->name);
            remove_invoice(invoices,invoice_num);
        }
    }

    return total_products;
}

/**
 * Command r: Prints invoices
 * If invoked with ean, prints invoice info for that product
 * If invoked with no arguments, prints billing summary and IVA table
 * @param warehouse Array containing all registered products in the warehouse
 * @param total_products Total products currently registered in the warehouse
 * @param iva_rates Array with all iva classes and their corresponding
 * percentage
 * @param num_iva  Number of iva classes
 * @param invoices Pointer to invoice list
 */
void billing_review(Product warehouse[], int total_products, Iva iva_rates[],
int num_iva, InvoiceList *invoices) {
    
    char rest_of_input[100];
    char ean[EAN_MAX+1];
    int i,j,k,done;
    Iva temp;

    fgets(rest_of_input, 100, stdin);
    
    /** invoked with ean */
    if(sscanf(rest_of_input, "%s", ean)==1) {
        if(check_ean(ean)!=1) {
            printf(EINVALIDEAN);
            return;
        }
        
        i = find_product(warehouse, total_products, ean);

        if(i==-1) {
            printf(ENOSUCHPROD, ean);
            return;
        }

        else {
            printf("%d %d %s\n", warehouse[i].quantity_available,
            warehouse[i].quantity_sold,
            warehouse[i].description);
        }
    }
    /** no arguments */
    else {
        printf("%d %d %.2f\n", invoices->total_items, invoices->next_number-1,
        invoices->total_value);

        /**bubble sort to sort IVA table in alphabetical order */
        for (k=0;k<num_iva-1;k++) {
            done=1;
            for(j=num_iva-1;j>k;j--) {
                if (iva_rates[j].class < iva_rates[j-1].class) {
                temp = iva_rates[j-1];
                iva_rates[j-1] = iva_rates[j];
                iva_rates[j] = temp;
                done = 0;
                }
            }
            if(done) break;
        }
        /**prints sorted IVA table */
        for (k=0;k<num_iva;k++) 
            printf("%c %d%%\n", iva_rates[k].class, iva_rates[k].percentage);
    }
}

/**
 * Command f: Creates invoice for products in cart
 * @param warehouse Array containing all registered products in the warehouse
 * @param cart Array containing the products in the cart
 * @param invoices Pointer to invoice list
 * @param total_products Total products currently registered in the warehouse
 * @param cart_products Number of products in the cart
 * @param iva_rates Array with all iva classes and their corresponding
 * percentage
 * @param num_iva  Number of iva classes
 * @return Updated number of products in cart
 */
int process_invoice(Product warehouse[],Cart_Product cart[],
InvoiceList *invoices, int total_products, int cart_products, 
Iva iva_rates[], int num_iva) {
    
    char input[65536];
    int i=0, arg_num, j, k, m;
    int nif = 999999999; /**no nif */
    char name[65536] = "Cliente final"; /**no name */
    char nquotes_name[65536];
    double total_value = 0.0;
    int iva_rate = 0;
    int total_items = 0;

    fgets(input,65536,stdin);

    while(input[i] == ' ')
        i++;
    
    arg_num=sscanf(input+i,"%d %[^\n]",&nif,name);

    /** input has name but no nif */
    if(arg_num==0) {
        sscanf(input+i,"%[^\n]",name);
    }

    /**removes "" from name  */
    if(name[0]=='"') {
        name[strlen(name)-1] = '\0';
        strcpy(nquotes_name, name+1);
    }
    else {
        strcpy(nquotes_name, name);
    }

    if(nif>999999999 || nif<100000000) {
        printf(EINVALIDNIF, nif);
        return cart_products;
    }

    if(isalpha(nquotes_name[0])==0) {
        printf(EINVALIDNAME);
        return cart_products;
    }

    /**if name=error all products return to warehouse and no invoice 
     * is created*/
    if(strcmp(nquotes_name,"error")==0) {
        for(j=0;j<cart_products;j++) {
            k=find_product(warehouse,total_products,cart[j].ean);
            warehouse[k].quantity_available += cart[j].quantity;
            warehouse[k].quantity_sold -= cart[j].quantity;
            
        }
        return 0;
    }

    for(j=0;j<cart_products;j++) {
        k=find_product(warehouse,total_products,cart[j].ean);

        /** finding the iva rate */
        for(m=0;m<num_iva;m++) {
            if(warehouse[k].iva==iva_rates[m].class) {
                iva_rate = iva_rates[m].percentage;
                break;
            }
        }

        total_value += price_with_iva(warehouse[k].price,cart[j].quantity,
        iva_rate);

        total_items += cart[j].quantity;

    }

    add_invoice(invoices,nif,nquotes_name,total_items,total_value);
    printf("%d %.2f %d\n", total_items, total_value, invoices->next_number-1);
    return 0;
}

/**
 * Merges two sorted halves of an array into a sorted sequence
 * @param array Array of InvoiceNode pointers
 * @param aux Auxiliary array used for merging
 * @param l Left boundary index of the array
 * @param m Middle index of the array
 * @param r Right boundary index of the array
 */
void invoice_merge(InvoiceNode *array[], InvoiceNode *aux[],
int l, int m, int r) {
    int i, j, k;

    /**copies left half in normal order to aux */
    for(i=m+1;i>l;i--) {
        aux[i-1]=array[i-1];
    }

    /**copies right half in reverse order to aux */
    for(j=m;j<r;j++) {
        aux[r+m-j]=array[j+1];
    }

    /**merging both halves into the original array */
    for(k=l;k<=r;k++) {
        if(strcmp(aux[j]->name,aux[i]->name)<0) {
            array[k]=aux[j];
            j--;
        }
        else {
            array[k]=aux[i];
            i++;
        }
    }
}

/**
 * Uses merge sort to recursively sorts an array of InvoiceNode pointers
 * @param array Array of InvoiceNode pointers
 * @param aux Auxiliary array used for sorting
 * @param l Left boundary index of array
 * @param r Right boundary index of array
 */
void invoice_mergesort(InvoiceNode *array[], InvoiceNode *aux[], 
int l, int r) {
    int m;
    /**calculates the middle element*/
    m = (r+l)/2;
    /**if 0 or 1 elements, already sorted */
    if(r<=l) return;

    invoice_mergesort(array,aux,l,m);
    invoice_mergesort(array,aux,m+1,r);
    invoice_merge(array,aux,l,m,r);

}

/**
 * Command c: Lists system invoices
 * Invoked with no arguments: lists all invoices sorted by name
 * Invoked with name: lists all client invoices in chronological order
 * @param invoices Pointer to invoice list
 */
void lists_invoices(InvoiceList *invoices) {
    char input[65536];
    int i=0, arg_num, j;
    char name[65536] = "";
    char nquotes_name[65536];
    InvoiceNode *current = invoices->head;
    int found = 0;

    fgets(input,65536,stdin);

    /**skips all leading spaces */
    while(input[i] == ' ')
        i++;
    
    /**reads name starting at first character thats not a space */
    arg_num=sscanf(input+i,"%[^\n]",name);

    if(arg_num==1) {
        if(name[0]=='"') {
            name[strlen(name)-1] = '\0';
            strcpy(nquotes_name,name+1);
        }
        else {
            strcpy(nquotes_name,name);
        }

        if(isalpha(nquotes_name[0])==0) {
            printf(EINVALIDNAME);
            return;
        }
    }

    /**invoked with clients name */
    if(arg_num==1) {
        while(current!=NULL) {
            if(strcmp(current->name,nquotes_name)==0) {
                printf("%d %.2f %s\n", current->number, current->total_value,
                current->name);
                
                found = 1;
            }
            current = current->next;
        }

        if(found==0) {
            printf(EINVALIDCLIENT, nquotes_name);
        }
    }
    /**invoked with no arguments*/
    else {
        int count = 0; /**<number of InvoiceNode in the invoice list */
        current = invoices->head;
        while(current!=NULL) {
            count++;
            current = current->next;
        }

        if(count==0) {
            return;
        }

        /**allocates memory for array and aux */
        InvoiceNode **array = malloc(count * sizeof(InvoiceNode *));
        InvoiceNode **aux = malloc(count * sizeof(InvoiceNode *));

        /**checks if malloc worked */
        if(array==NULL || aux==NULL) {
            printf(ENOMEMORY);
            free(array);
            free(aux);
            return;
        }

        current = invoices->head;
        for(j=0;j<count;j++) {
            array[j]=current;
            current = current->next;
        }

        invoice_mergesort(array,aux,0,count-1);

        for(j=0;j<count;j++) {
            printf("%d %.2f %s\n", array[j]->number, array[j]->total_value,
            array[j]->name);
        }

        free(array);
        free(aux);
    }
}
/**
 * Main function: reads and processes commands
 * @param arg_count Number of command line arguments 
 * @param arg_vector Array of pointers to command line arguments
 * @return 0 when sucessful
 */
int main(int arg_count, char *arg_vector[]) {
    Product warehouse[PRODUCTS_MAX];
    Cart_Product cart[PRODUCTS_MAX];
    InvoiceList *invoices = mk_invoice_list();
    int total_products = 0;
    int cart_products = 0;
    char command;
    
    Iva iva_rates[26];
    int num_iva = iva_count(arg_count,arg_vector,iva_rates);

    while(scanf(" %c", &command) == 1 && command != 'q') {
        switch(command) {
            case 'p':
                total_products=process_product(warehouse, cart, total_products,
                cart_products,iva_rates,num_iva);
                break;
            case 'l':
                lists_products(warehouse, total_products);
                break;
            case 'a':
                cart_products=add_to_cart(warehouse,cart,iva_rates,
                cart_products,total_products,num_iva);
                break;
            case 'r':
                billing_review(warehouse, total_products,iva_rates,num_iva,
                invoices);
                break;
            case 'f':
                cart_products=process_invoice(warehouse,cart,invoices,
                total_products,cart_products,iva_rates,num_iva);
                break;

            case 'd':
                total_products=removes_prod_inv(warehouse, cart, invoices,
                total_products, cart_products);
                break;
            
            case 'c': {
                lists_invoices(invoices);
                break;
            }
        }
    }
    free_invoice_list(invoices);
    return 0;
}