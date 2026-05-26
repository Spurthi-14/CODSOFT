print("===== CONTACT BOOK =====")
contacts = []
while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    choice = input("\nEnter your choice: ")
    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        if len(phone) != 10 or not phone.isdigit():
            print("Phone number must contain exactly 10 digits.")
            continue
        email = input("Enter Email: ")
        if "@" not in email or "." not in email:
            print("Invalid email address.")
            continue
        address = input("Enter Address: ")
        contact = {
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        }
        contacts.append(contact)
        print("Contact Added Successfully!")
    elif choice == "2":
        if len(contacts) == 0:
            print("No contacts found.")
        else:
            print("\nSaved Contacts:\n")
            for contact in contacts:
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])
                print("-" * 30)
    elif choice == "3":
        search_name = input("Enter name to search: ")
        found = False
        for contact in contacts:
            if contact["name"].lower() == search_name.lower():
                print("\nContact Found")
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])
                print("Address:", contact["address"])
                found = True
                break
        if found == False:
            print("Contact not found.")
    elif choice == "4":
        update_name = input("Enter contact name to update: ")
        found = False
        for contact in contacts:
            if contact["name"].lower() == update_name.lower():
                print("Enter new details")
                new_phone = input("New Phone: ")
                if len(new_phone) != 10 or not new_phone.isdigit():
                    print("Phone number must contain exactly 10 digits.")
                    break
                new_email = input("New Email: ")
                if "@" not in new_email or "." not in new_email:
                    print("Invalid email address.")
                    break
                contact["name"] = input("New Name: ")
                contact["phone"] = new_phone
                contact["email"] = new_email
                contact["address"] = input("New Address: ")
                print("Contact Updated Successfully!")
                found = True
                break
        if found == False:
            print("Contact not found.")
    elif choice == "5":
        delete_name = input("Enter contact name to delete: ")
        found = False
        for contact in contacts:
            if contact["name"].lower() == delete_name.lower():
                contacts.remove(contact)
                print("Contact Deleted Successfully!")
                found = True
                break
        if found == False:
            print("Contact not found.")
    elif choice == "6":
        print("Thank you for using Contact Book!")
        break
    else:
        print("Invalid choice. Please try again.")