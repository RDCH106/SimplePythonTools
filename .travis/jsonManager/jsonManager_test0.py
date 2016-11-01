import sys
import os
from shutil import copyfile

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../../")
from managers.jsonManager import JsonManager

# Global variables
scriptname = ""
pathname = ""
full_path_name = ""

# Sample functions
#############################################################
def abort_exe( exit_message ):
    print(exit_message)
    print("Aborting...")
    sys.exit(0)
    return

def external_process_key(*arg):
    isJsonValid = arg[0]
    if isJsonValid == True:
        print(arg[1])
    else:
        print("Cannot process a invalid json")
    return

def testinfo(self):
    print("testinfo")

def try_read_wrong_file():
    print("== try_read_wrong_file ===========================================")
    # Create instance
    parser = JsonManager('parser')
    # Try to parse wrong file
    successful, json_data = parser.read_json_from_file("wrong_file.json")
    print("successful? %s with data: %s" % (successful, json_data))
    print("==================================================================")
    return

def try_read_file():
    print("== try_read_file ===========================================")

    # Configure variables to provide to class sample
    #############################################################
    jsonkeys = ['a', 'b', 'd']
    input_path = os.path.join(os.getcwd(), "input/")

    # Create instance
    parser = JsonManager('parser')
    # Set array with keys
    parser.set_key_array(jsonkeys)
    # Set input path
    parser.set_input_path(input_path)
    # Parse json file
    successful, json_data = parser.read_json_from_file("test.json")
    print("successful? %s" % successful)

    # Get a value if exist or print error
    value = parser.get_value(json_data, 'f')
    print("Value is: %s" % value)
    # Print and get a value
    value = parser.print_json_value(json_data, 'a')
    # Print all json values
    parser.print_all_json_values(json_data)
    # Print only values in array
    parser.print_arraykey_json_values(json_data, jsonkeys)
    print("==================================================================")
    return

def try_create_file_from_list():
    print("== try_create_file_from_list ===========================================")
    output_path = os.path.join(full_path_name, "output/")
    json_values_array = []
    json_values_array.append(["key1", "value1"])
    json_values_array.append(["key2", "value2"])
    json_values_array.append(["key3", "value4"])

    # Create instance
    parser = JsonManager('parser')
    parser.set_output_path(output_path)

    # Try to create json object
    successful, json_data = parser.create_json_object_from_list(json_values_array, True)
    parser.print_all_json_values(json_data)
    print("successful? %s" % successful)
    parser.write_json("test_output.json", json_data)
    print("==================================================================")
    return

def try_create_file_from_csv():
    print("== try_create_file_from_csv ===========================================")
    input_path = os.path.join(full_path_name, "input/")
    output_path = os.path.join(full_path_name, "output/")

    # Create instance
    parser = JsonManager('parser')
    parser.set_input_path(input_path)
    parser.set_output_path(output_path)

    # Try to create json object
    successful, json_data = parser.create_json_object_from_csv("csv_file.csv", ';')
    parser.print_all_json_values(json_data)
    print("successful? %s" % successful)
    parser.write_json("test_csv_output.json", json_data)
    print("==================================================================")
    return

def try_create_file_from_csv_with_title():
    print("== try_create_file_from_csv_with_title ===========================================")
    input_path = os.path.join(full_path_name, "input/")
    output_path = os.path.join(full_path_name, "output/")

    # Create instance
    parser = JsonManager('parser')
    parser.set_input_path(input_path)
    parser.set_output_path(output_path)

    # Try to create json object
    successful, json_data = parser.create_json_object_from_csv_with_title("csv_with_custom_col.csv", ';', False)
    parser.print_all_json_values_in_an_array(json_data)
    print("successful? %s" % successful)
    #parser.write_json("test_csv_output.json", json_data)
    print("==================================================================")
    return

def try_process_all_files_in_all_folder():
    print("== try_process_with_external_function ===========================================")
    # Create instance
    parser = JsonManager('parser')
    input_path = os.path.join(full_path_name, "input/")

    parser.set_process_function(external_process_key)
    parser.process_all_files_in_folders(input_path, True, True)
    print("==================================================================")
    return

def try_process_all_files_in_a_folder():
    print("== try_process_with_external_function2 ===========================================")
    # Create instance
    parser = JsonManager('parser')
    input_path = os.path.join(full_path_name, "input/folder2")

    parser.set_process_function(external_process_key)
    parser.process_all_files(input_path, True)
    print("==================================================================")
    return

def try_edit_file_with_list():
    print("== try_edit_without_copy ===========================================")
    filename = "test.json"

    # Create instance
    parser = JsonManager('parser')
    os.path.join(full_path_name, "input")

    json_values_array = []
    json_values_array.append(["a", "new a value"])
    json_values_array.append(["b", "new b value"])
    json_values_array.append(["c", "new c value"])

    successful, json_data = parser.read_json_from_file(filename)
    if successful == True:
        print("Processing...")
        successful, json_data = parser.edit_json_from_lists(json_data, json_values_array)
        print("Saving...")
        parser.write_json(filename, json_data)

    print("==================================================================")
    return

def initialize():
    scriptname = sys.argv[0]
    pathname = os.path.dirname(sys.argv[0])
    full_path_name = os.path.abspath(pathname)

    print("\n")
    print("==================================================================")
    print('   Executing: ', scriptname)
    print("==================================================================")
    print("\n")

    # Create output path if needed
    output_path = os.path.join(full_path_name, "output/")
    if not os.path.exists(output_path):
        print("Creating output path...")
        os.makedirs(output_path)

    # Restore test.json is if needed
    print("Restoring test.json...")
    src_file = os.path.join(full_path_name, "input/test_original.json")
    dst_file = os.path.join(full_path_name, "input/test.json")
    copyfile(src_file, dst_file)
    print("initialize done!\n")
    return

if __name__ == '__main__':
    # Initialize
    ###########################################################
    initialize()

    # Use class
    ###########################################################
    try_read_wrong_file()
    try_read_file()
    try_create_file_from_list()
    try_create_file_from_csv()
    try_create_file_from_csv_with_title()
    try_process_all_files_in_all_folder()
    try_process_all_files_in_a_folder()
    try_edit_file_with_list()

    # parser.print_methods()
    # parser.test()
    print("\n")
    print("==================================================================")
    print("   Finish.")
    print("==================================================================")
    print("\n")
