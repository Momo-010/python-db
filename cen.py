import pymongo

# Creating the database
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["students"]

# Adding to the database
mydict = [{ "_id": 1,"name": "Molayo", "Hall": "Daniel", "Room":"E210", "Matric-number": "20CJ027410" },
           { "_id": 2, "name": "Isaac", "Hall": "paul", "Room":"F301", "Matric-number": "20CJ027450" },
            { "_id": 3, "name": "George", "Hall": "John", "Room":"E201", "Matric-number": "20CJ027426" }, 
            { "_id": 4, "name": "Samuel", "Hall": "Daniel", "Room":"E306", "Matric-number": "20CJ027470" },
            { "_id": 5, "name": "Jessica", "Hall": "Dorcas", "Room":"D205", "Matric-number": "20CJ027420" }        
            ]

# x = mycol.insert_many(mydict)

# Deleting from the database
myquery = { "name": "Samuel" }
mycol.delete_one(myquery)

# Adding a new record to the database
def add_new_record(mycol, record):

  result = mycol.insert_one(record)
  return result.inserted_id

  
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
new_record_id = add_new_record(mycol, new_record)

# Print a confirmation message.
print("New record added successfully!")
