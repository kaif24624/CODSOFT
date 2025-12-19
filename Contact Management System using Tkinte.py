# Contact Management System using Tkinter
# Simple GUI based application

import tkinter as tk
from tkinter import messagebox

contacts = []


def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name == "" or phone == "":
        messagebox.showwarning("Warning", "Name and Phone are required")
        return

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    clear_fields()
    show_contacts()


def show_contacts():
    contact_list.delete(0, tk.END)
    for c in contacts:
        contact_list.insert(tk.END, f"{c['name']} - {c['phone']}")


def search_contact():
    key = search_entry.get().lower()
    contact_list.delete(0, tk.END)

    for c in contacts:
        if key in c["name"].lower() or key in c["phone"]:
            contact_list.insert(tk.END, f"{c['name']} - {c['phone']}")


def select_contact(event):
    try:
        index = contact_list.curselection()[0]
        contact = contacts[index]

        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        address_entry.delete(0, tk.END)

        name_entry.insert(0, contact["name"])
        phone_entry.insert(0, contact["phone"])
        email_entry.insert(0, contact["email"])
        address_entry.insert(0, contact["address"])
    except:
        pass


def update_contact():
    try:
        index = contact_list.curselection()[0]

        contacts[index]["name"] = name_entry.get()
        contacts[index]["phone"] = phone_entry.get()
        contacts[index]["email"] = email_entry.get()
        contacts[index]["address"] = address_entry.get()

        clear_fields()
        show_contacts()
    except:
        messagebox.showinfo("Info", "Select a contact to update")


def delete_contact():
    try:
        index = contact_list.curselection()[0]
        contacts.pop(index)
        clear_fields()
        show_contacts()
    except:
        messagebox.showinfo("Info", "Select a contact to delete")


def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)


# main window
root = tk.Tk()
root.title("Contact Management System")
root.geometry("500x450")
root.resizable(False, False)

# title
tk.Label(root, text="Contact Management System",
         font=("Arial", 16, "bold")).pack(pady=10)

# input fields
tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root, width=40)
name_entry.pack()

tk.Label(root, text="Phone").pack()
phone_entry = tk.Entry(root, width=40)
phone_entry.pack()

tk.Label(root, text="Email").pack()
email_entry = tk.Entry(root, width=40)
email_entry.pack()

tk.Label(root, text="Address").pack()
address_entry = tk.Entry(root, width=40)
address_entry.pack(pady=5)

# buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add", width=10,
          command=add_contact).grid(row=0, column=0, padx=5)

tk.Button(btn_frame, text="Update", width=10,
          command=update_contact).grid(row=0, column=1, padx=5)

tk.Button(btn_frame, text="Delete", width=10,
          command=delete_contact).grid(row=0, column=2, padx=5)

# search
tk.Label(root, text="Search").pack()
search_entry = tk.Entry(root, width=30)
search_entry.pack()

tk.Button(root, text="Search Contact",
          command=search_contact).pack(pady=5)

# contact list
contact_list = tk.Listbox(root, width=55, height=8)
contact_list.pack(pady=10)
contact_list.bind("<<ListboxSelect>>", select_contact)

root.mainloop()
