
# print("Day 30 starts here.....")

#file not found error --------
# with open("a_file.txt") as file:
#     file.read()    #as there is no file so it will give file not error 

# -------key error------
# a_dictionary = {"key" : "value"}
# value = a_dictionary["non existing key"]

# ------Deal with Exception ----------

try:
    file = open("a_file.txt")

    a_dict = {"key" : "value"}
    print(a_dict["asdf"])

except FileNotFoundError:
    # print("There was an error")
    file = open("a_file.txt", "w")
    file.write("Something")

except KeyError as error_message:
    print(f"The key {error_message} does not exist")

else:
    content = file.read()
    print(content)   #if try and except has no problem then it will run

finally:
    file.close()
    print("File has closed")

