from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import db_setup  # Import database functions

# Initialize main window
root = Tk()
root.title ('Inventory Management System')
root.geometry('500x400')

# Labels and Entry Fields
Label(root, text='Product Name').grid(row=0, column=0, padx=10, pady=5)
name_entry = Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

Label(root, text='Quantity').grid(row=1, column=0, padx=10, pady=5)
qty_entry = Entry(root)
qty_entry.grid(row=1, column=1, padx=10, pady=5)

# Function to Add Product
def add_product():
    name = name_entry.get().strip()
    qty = qty_entry.get().strip()

    if name and qty.isdigit():
        db_setup.add_product(name, int(qty))
        name_entry.delete(0, END)
        qty_entry.delete(0, END)
        messagebox.showinfo('Success', 'Product added successfully')
        view_products()
    else:
        messagebox.showerror('Error', 'Please enter a valid product name and numeric quantity')

# Function to View Products
def view_products():
    products = db_setup.get_products()
    
    # Clear previous data
    product_list.delete(*product_list.get_children())

    # Insert new data
    for row in products:
        product_list.insert('', END, values=row)

# Function to Delete Product
def delete_product():
    selected = product_list.selection()
    if selected:
        item = product_list.item(selected[0])
        product_id = item['values'][0]
        db_setup.delete_product(product_id)
        messagebox.showinfo('Deleted', 'Product deleted successfully')
        view_products()
    else:
        messagebox.showerror('Error', 'Please select a product to delete')

# Function to Update Product Quantity
def update_product():
    selected = product_list.selection()
    if selected:
        item = product_list.item(selected[0])
        product_id = item['values'][0]
        new_qty = qty_entry.get().strip()

        if new_qty.isdigit():
            db_setup.update_product(product_id, int(new_qty))
            messagebox.showinfo('Updated', 'Product updated successfully')
            view_products()
        else:
            messagebox.showerror('Error', 'Please enter a valid numeric quantity')
    else:
        messagebox.showerror('Error', 'Please select a product to update')

# Buttons
Button(root, text='Add Product', command=add_product).grid(row=2, column=0, padx=10, pady=5)
Button(root, text='Update Product', command=update_product).grid(row=2, column=1, padx=10, pady=5)
Button(root, text='Delete Product', command=delete_product).grid(row=2, column=2, padx=10, pady=5)

# Product List Table
product_list = ttk.Treeview(root, columns=('ID', 'Name', 'Quantity'), show='headings')
product_list.heading('ID', text='ID')
product_list.heading('Name', text='Product Name')
product_list.heading('Quantity', text='Quantity')
product_list.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

# Load products on startup
view_products()
# Run the application
root.mainloop()
