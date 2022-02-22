
// This program uses two arrays to record the names of 5 types of pizza

// and the sales numbers for each of these types

// The program then finds the best and the worst selling pizzas

#include <iostream>

#include <string>

using namespace std;

int main()

{
    /*1. const and int are to be separated which declares a ineteger variable of constant size. 6 is changed to 5 since the first line of comment states there are 5 pizzas.*/

    const int ARR_SIZE = 5; // Declare the array size and set it to 6

    // Declare the array of pizza names and record values in it

    /*2. Since we have changed the number of pizzas to 5 according to question, let us remove the last string "Mozzarella" in the array name*/

    string name[ARR_SIZE] = {"Pepperoni", "Prosciutto", "Vegetarian",

                             "Sausage", "Supreme"};

    int sales[ARR_SIZE]; // Declare the sales array

    int worstseller_number, bestseller_number; // The sale numbers of the best- and worstseller

    string worstseller_name, bestseller_name; // The subscripts of the best- and worstseller

    /*3.The variable i must initialize to 0 in the for loop since a loop to enter all sales numbers is required. Arrays in C++ are indexed starting from 0*/

    for (int i = 0; i < ARR_SIZE; i++) // A loop to enter all sales numbers

    {

        cout << "Enter sales for " << name[i] << ": ";

        cin >> sales[i];
    }

    // Make the first element in name[] the bestseller and the worstseller name

    worstseller_name = bestseller_name = name[0];

    // Make the first element in sales[] the bestseller and the worstseller sales amount

    worstseller_number = bestseller_number = sales[0];

    /*4. Replacing the <= sign with < as index will be out of range on the last iteration*/
    for (int i = 0; i < ARR_SIZE; i++) // Loop through all elements in sales[]

    {

        if (sales[i] < worstseller_number) // If an element is less than the lowest...

        {
            /*5. Replacing i with sales[i] since we need to assign lowest sales number to worstseller_number. Using i will only assign the index of the lowest sales number */

            worstseller_number = sales[i]; // make the lowest sales equal to its sales

            worstseller_name = name[i]; // make the worstseller name equal to its name
        }

        /*6. The sign must be greater than and not less than*/

        if (sales[i] > bestseller_number) // If an element is higher than the highest...

        {

            bestseller_number = sales[i]; // make the highest sales equal to its sales

            bestseller_name = name[i]; // make the bestseller name equal to its name
        }
    }

    cout << "The bestselling pizza is " << bestseller_name << " with the sales of "

         << bestseller_number << endl; // Display the best selling pizza

    cout << "The worst selling pizza is " << worstseller_name << " with the sales of "

         // Commenting outside the block is not useful to readers
         << worstseller_number << endl; // display the worst selling pizza
}
