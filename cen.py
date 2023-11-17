import pymongo

# Creating the database
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["students"]

# Adding to the database
mydict = [
    {"_id": 1, "name": "Molayo", "Hall": "Daniel", "Room": "E210", "Matric-number": "20CJ027410"},
    {"_id": 2, "name": "Isaac", "Hall": "paul", "Room": "F301", "Matric-number": "20CJ027450"},
    {"_id": 3, "name": "George", "Hall": "John", "Room": "E201", "Matric-number": "20CJ027426"},
    {"_id": 4, "name": "Samuel", "Hall": "Daniel", "Room": "E306", "Matric-number": "20CJ027470"},
    {"_id": 5, "name": "Jessica", "Hall": "Dorcas", "Room": "D205", "Matric-number": "20CJ027420"}
]

# x = mycol.insert_many(mydict)

# Adding a new record to the database
def add_new_record(mycol):
    # Prompt the user for the student's name.
    name = input("Enter the student's name: ")
    # Prompt the user for the student's hall.
    hall = input("Enter the student's hall: ")
    # Prompt the user for the student's room.
    room = input("Enter the student's room: ")
    # Prompt the user for the student's matric number.
    matric_number = input("Enter the student's matric number: ")

    # Create a new record dictionary.
    new_record = {
        "name": name,
        "hall": hall,
        "room": room,
        "matric-number": matric_number
    }
    # Add the new record to the database.
    result = mycol.insert_one(new_record)

    # Print a confirmation message.
    print("New record added successfully!")

def find_record(mycol):
    print("1. Name")
    print("2. Hall")
    print("3. Room")
    print("4. Matric-Number")
    find = input("What do you want to find: ")

    if find == "1":
        field_to_check = "name"
        for x in mycol.find({field_to_check: {"$exists": True}}):
            print(x)

    if find == "2":
        field_to_check = "hall"
        for x in mycol.find({field_to_check: {"$exists": True}}):
            print(x)

    if find == "3":
        field_to_check = "room"
        for x in mycol.find({field_to_check: {"$exists": True}}):
            print(x)

    if find == "4":
        field_to_check = "matric-number"
        for x in mycol.find({field_to_check: {"$exists": True}}):
            print(x)

def update_record(mycol):
    print("1. Name")
    print("2. Hall")
    print("3. Room")
    print("4. Matric-Number")
    update_field = input("Which field do you want to update: ")
    update_value = input("Enter the new value: ")

    query_field = None

    if update_field == "1":
        query_field = "name"
    elif update_field == "2":
        query_field = "hall"
    elif update_field == "3":
        query_field = "room"
    elif update_field == "4":
        query_field = "matric-number"

    if query_field:
        record_to_update = input(f"Enter the {query_field} of the record to update: ")

        filter_query = {query_field: record_to_update}
        update_operation = {"$set": {query_field: update_value}}

        result = mycol.update_one(filter_query, update_operation)

        if result.matched_count > 0:
            print(f"Successfully updated the {query_field} field.")
        else:
            print(f"No document found with {query_field} equal to {record_to_update}.")
    else:
        print("Invalid input for the field to update.")

def delete_record(mycol):
    print("1. Name")
    print("2. Hall")
    print("3. Room")
    print("4. Matric-Number")
    delete_field = input("Which field do you want to use for deletion: ")
    delete_value = input(f"Enter the {delete_field} of the record to delete: ")

    delete_query = {delete_field: delete_value}

    result = mycol.delete_one(delete_query)

    if result.deleted_count > 0:
        print(f"Successfully deleted the document with {delete_field} equal to {delete_value}.")
    else:
        print(f"No document found with {delete_field} equal to {delete_value}.")

run = True
while run:
    print("1. Add a new record")
    print("2. Find a record")
    print("3. Update a record")
    print("4. Delete a record")
    print("5. Exit")
    res = input("What would you like to do:")

    if res == "1":
        print("You want to add a new record")
        add_new_record(mycol)
    elif res == "2":
        print("You want to find a record")
        find_record(mycol)
    elif res == "3":
        print("You want to update a record")
        update_record(mycol)
    elif res == "4":
        print("You want to delete a record")
        delete_record(mycol)
    elif res == "5":
        print("Do you want to quit:")
        res2 = input("Y/N:")
        if res2.upper() == "Y":
            run = False
            print("Goodbye")
        elif res2.upper() == "N":
            run = True
