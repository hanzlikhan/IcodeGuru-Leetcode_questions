#include <iostream>
#include <unordered_map>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

class Product {
public:
    string name;
    string category;
    double price;
    double rating;
    int stock;

    Product(string _name, string _category, double _price, double _rating, int _stock) {
        name = _name;
        category = _category;
        price = _price;
        rating = _rating;
        stock = _stock;
    }

    void printProduct() {
        cout << "Name: " << name << ", Category: " << category
             << ", Price: $" << price << ", Rating: " << rating
             << ", Stock: " << stock << endl;
    }

    void addToCart(int quantity, vector<Product>& cart) {
        if (stock >= quantity) {
            stock -= quantity;
            cart.push_back(*this);
            cout << quantity << " " << name << "(s) added to the cart." << endl;
        } else {
            cout << "Insufficient stock!" << endl;
        }
    }
};

void displayCart(vector<Product>& cart) {
    if (cart.empty()) {
        cout << "Your cart is empty." << endl;
    } else {
        cout << "Items in your cart:" << endl;
        for (int i = 0; i < cart.size(); ++i) {
            cart[i].printProduct();
        }
    }
}

int main() {
    vector<Product> products;
    products.push_back(Product("Laptop X", "Electronics", 899.99, 4.5, 5));
    products.push_back(Product("Book Y", "Books", 19.99, 4.8, 10));
    products.push_back(Product("Headphones Z", "Electronics", 79.99, 4.2, 8));
    products.push_back(Product("Shirt A", "Clothing", 24.99, 4.0, 15));

    unordered_map<string, vector<Product>> productByCategory;
    for (int i = 0; i < products.size(); ++i) {
        productByCategory[products[i].category].push_back(products[i]);
    }

    vector<Product> cart;
    while (true) {
        cout << "\n** Online Shopping System **\n";
        cout << "1. Sort products by price\n2. Sort products by rating\n3. Browse by category\n4. Manage cart\n5. Exit\nEnter choice: ";
        
        int choice;
        cin >> choice;

        if (choice == 1) {
            sort(products.begin(), products.end(), [](Product a, Product b) { return a.price < b.price; });
            for (int i = 0; i < products.size(); ++i) {
                products[i].printProduct();
            }
        } else if (choice == 2) {
            sort(products.begin(), products.end(), [](Product a, Product b) { return a.rating > b.rating; });
            for (int i = 0; i < products.size(); ++i) {
                products[i].printProduct();
            }
        } else if (choice == 3) {
            cout << "Enter category (or 'all'): ";
            string category;
            cin >> category;
            if (category == "all") {
                for (int i = 0; i < products.size(); ++i) {
                    products[i].printProduct();
                }
            } else if (productByCategory.find(category) != productByCategory.end()) {
                for (int i = 0; i < productByCategory[category].size(); ++i) {
                    productByCategory[category][i].printProduct();
                }
            } else {
                cout << "Category not found.\n";
            }
        } else if (choice == 4) {
            cout << "1. View cart\n2. Add to cart\n3. Remove from cart\n4. Checkout\nEnter choice: ";
            int cartChoice;
            cin >> cartChoice;

            if (cartChoice == 1) {
                displayCart(cart);
            } else if (cartChoice == 2) {
                cout << "Enter product name: ";
                string productName;
                cin.ignore();
                getline(cin, productName);
                cout << "Enter quantity: ";
                int quantity;
                cin >> quantity;
                bool productFound = false;
                for (int i = 0; i < products.size(); ++i) {
                    if (products[i].name == productName) {
                        products[i].addToCart(quantity, cart);
                        productFound = true;
                        break;
                    }
                }
                if (!productFound) {
                    cout << "Product not found.\n";
                }
            } else if (cartChoice == 3) {
                cout << "Enter product name to remove: ";
                string productName;
                cin.ignore();
                getline(cin, productName);
                bool productFound = false;
                for (int i = 0; i < cart.size(); ++i) {
                    if (cart[i].name == productName) {
                        cart[i].stock++;
                        cart.erase(cart.begin() + i);
                        cout << "Product removed from cart.\n";
                        productFound = true;
                        break;
                    }
                }
                if (!productFound) {
                    cout << "Product not found in cart.\n";
                }
            } else if (cartChoice == 4) {
                double total = 0;
                for (int i = 0; i < cart.size(); ++i) {
                    total += cart[i].price;
                }
                cout << "Total: $" << total << "\nThank you for shopping with us!\n";
                break;
            }
        } else if (choice == 5) {
            break;
        } else {
            cout << "Invalid choice.\n";
        }
    }
    return 0;
}
