import csv

def add_todo(file_name):
  print("Add todo")
  # Ask the title of the todo
  todo_name = input("Enter a todo: ")
  # open file - list.csv
  with open(file_name, "a") as f:
    writer = csv.writer(f)
      #while insertig - title = user entered
      #completed = False by default
    writer.writerow([todo_name, "False"])
  
def remove_todo(file_name):
  print("Remove todo")

def mark_todo(file_name):
  print("mark todo")

def view_todo(file_name):
  print("View todo")
  with open(file_name, "r") as f:
    reader = csv.reader(f)
    reader.__next__()
    for row in reader:
      if row[1] == "True":
        print(f"Todo{row[0]} is complete")
      else:
        print(f"Todo{row[0]} is not complete")