from colored import fg, attr, bg
from todo_functions import add_todo, remove_todo, mark_todo, view_todo
import csv
file_name = "list.csv"

try:
  #open the file in read mode
  todo_file = open(file_name, "r")
  todo_file.close()
  print("In try block")
  #if it throws error, it meas the file does not exist
  pass
except FileNotFoundError:
  #Now, we know the file doesn't exist
  #Create the file
  #We can also insert the firsy line into the file
  todo_file = open(file_name, "w")
  todo_file.write("title, completed\n")
  todo_file.close()
  print("In except block")
  pass

print(f"{fg('black')}{bg('white') }Welcome to your TODO list")

def create_menu():
  print("1. Enter 1 to add item to your list")
  print("2. Enter 2 to remove item from your list")
  print("3. Enter 3 to mark an item as completed")
  print("4. Enter 4 to view your todo list")
  print("5. Enter 5 to exit")
  choice = input("Enter your selection: ")
  return choice

users_choice = ""

while users_choice != "5":
  users_choice = create_menu()
  if users_choice == "1":
    add_todo(file_name)
  elif users_choice == "2":
    remove_todo(file_name)
  elif users_choice == "3":
    mark_todo(file_name)
  elif users_choice == "4":
    view_todo(file_name)
  elif users_choice == "5":
    continue
  else:
    print("Invalid Input")

print("Thank you for using todo list")