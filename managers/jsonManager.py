import os
import json
import csv
import collections
import pathlib
import inspect

"""
This python 3 class will manager json individually for you.

To generate HTML documentation for this module issue the command:

    pydoc -w jsonManager
"""

class JsonManager(object):
    _name = None
    _key_array = [None] * 0
    _json_data = json.dumps({})
    _input_path = "input/"
    _output_path = "output/"
    _current_filename = "None"
    _function_callback = None

    """
    Initialize JsonManager with a name to identify eash instance
    """
    @classmethod
    def __init__(self, name):
        """
        Construct a new 'JsonManager' object.

        :param current_json: Current json data readed in memory.
        :param current_read_file: Current file with a valid json.
        :param current_write_file: Current file in write mode to save json.
        :return: returns nothing
        """
        self._name = name

    """
    Print parser ID
    """
    @classmethod
    def print_ID(self):
        """
        Prints json Manager ID to the display.
        """
        print(self._name)
        return None

    """
    Print all methods
    """
    @classmethod
    def print_methods(self):
        print(inspect.getmembers(self, predicate=inspect.ismethod))
        return None

    """
    Test function
    """
    @classmethod
    def test(self):
        print("Test")
        print(inspect.getmembers(self, predicate=inspect.ismethod))
        return None

    """
    set_key_array
    """
    @classmethod
    def set_key_array(self, key_array):
        print("Setting keys: %s" % list(key_array) )
        _key_array = key_array
        return None

    """
    set_input_path
    """
    @classmethod
    def set_input_path(self, input_path = None):
        if input_path is None:
            input_path = self.input_path
        print("Setting input path: %s" % input_path)
        self._input_path = input_path
        return None

    """
    set_output_path
    """
    @classmethod
    def set_output_path(self, output_path = None):
        if output_path is None:
            output_path = self.output_path
        print("Setting output path: %s" % output_path)
        self._output_path = output_path
        return None

    """
    set_process_function
    """
    #@classmethod
    def set_process_function(self, function_callback = None):
        print("Setting process function: %s" % function_callback)
        self._function_callback = function_callback
        return None

    """
    process_function_default
    """
    @classmethod
    def process_function(self, *arg):
        if(self._function_callback == None):
            print("Default process... overload call with set_process_function!")
        else:
            print("Calling external process function")
            self._function_callback(arg)
        return None

    """
    print_json_value
    """
    @classmethod
    def print_json_value(self, json_data = None, key = None):
        value = None
        if json_data is None:
            json_data = self._json_data
        if(key in json_data):
            value = json_data[key]
            print("Value is: %s" % value)
        else:
            print("Missing value: %s in json" % key)
        return value

    """
    print_all_json_values
    """
    @classmethod
    def print_all_json_values(self, json_data = None):
        if json_data is None:
            json_data = self._json_data
        print("Json contains keys: %s" % list(json_data))
        for key, value in json_data.items():
            print("Key: %s with value: %s" % (key, value))
        return None

    """
    print_all_json_values_in_an_array
    """
    @classmethod
    def print_all_json_values_in_an_array(self, array_json_data = None):
        if array_json_data is None:
            array_json_data = self._array_json_data
        print("Json contains keys: %s" % list(array_json_data))
        array_index = 0
        for json_data in array_json_data:
            for key, value in json_data.items():
                print("Array: %d has a Key: %s with value: %s" % (array_index, key, value))
            array_index += 1
        return None

    """
    print_arraykey_json_values
    """
    @classmethod
    def print_arraykey_json_values(self, json_data = None, array_key = None):
        if json_data is None:
            json_data = self._json_data
        if array_key is None:
            array_key = self._array_key
        print("Json read only keys: %s" % list(array_key))
        for key in array_key:
            value = json_data[key]
            print("Key: %s with value: %s" % (key, value))
        return None

    """
    Read json
    :return: successful
    :return: _json_data data in json
    """
    @classmethod
    def read_json_from_file(self, file_name = None):
        successful = False
        json_data = json.dumps({})
        if file_name is None:
            return successful, json_data
        print("Reading file: %s" % file_name)
        full_source_name = os.path.join(self._input_path, file_name)
        if(pathlib.Path(full_source_name).is_file()):
            with open(full_source_name) as data_file:
                self._json_data = json.load(data_file, object_pairs_hook=collections.OrderedDict)
                successful = True
        else:
            print("File: %s no exist in input path." % file_name)
        return (successful, self._json_data)

    """
    Write json
    """
    @classmethod
    def write_json(self, file_name, json_data):
        print("Writing: %s" % file_name)
        full_destination_name = os.path.join(self._output_path, file_name)
        with open(full_destination_name, 'w') as outfile:
            json.dump(json_data, outfile, sort_keys=False)
        return None

    """
    Get value from json
    """
    @classmethod
    def get_value(self, json_data = None, key = None):
        value = None
        if json_data is None:
            json_data = self._json_data
        if(key in json_data):
            value = json_data[key]
        else:
            print("Missing value: %s in json" % key)
        return value

    """
    create_json_object_from_list
    """
    @classmethod
    def create_json_object_from_list(self, list_of_list = None, print_values = False):
        successful = True
        data = {}
        for pair in list_of_list:
            data[pair[0]] = pair[1]
            if print_values == True:
                print("pair with Key: %s and value %s" % (pair[0], pair[1]))
        return successful, data

    """
    create_json_object_from_csv
    """
    @classmethod
    def create_json_object_from_csv(self, csv_name, split_char = ';', print_values = False):
        print("Reading csv file: %s" % csv_name)
        full_source_name = os.path.join(self._input_path, csv_name)
        successful = True
        data = {}
        csv_file = open(full_source_name)
        csv_reader = csv.reader(csv_file)
        row_num = 0
        for row in csv_reader:
            row_str = "".join(row)
            values = row_str.split(split_char)
            if print_values == True:
                print("Key: %s has value %s" % (values[0], values[1]))
            data[values[0]] = values[1]
            row_num+=1
        print("Readed %d lines in csv file." % row_num)
        return successful, data

    """
    create_json_object_from_csv_with_title
    """
    @classmethod
    def create_json_object_from_csv_with_title(self, csv_name, split_char = ';', print_values = False):
        print("Reading csv file: %s" % csv_name)
        full_source_name = os.path.join(self._input_path, csv_name)
        print(full_source_name)
        successful = True
        data = [None] * 0
        csv_file = open(full_source_name)
        csv_reader = csv.reader(csv_file)
        row_num = 0
        columns_array = [None] * 0
        for row in csv_reader:
            row_str = "".join(row)
            values = row_str.split(split_char)
            if row_num == 0:
                columns_array = values;
            else:
                value_index = 0
                data_row = {}
                for value in values:
                    data_row[columns_array[value_index]] = value
                    value_index += 1
                data.append(data_row)
                if print_values == True:
                    print("Row %d has values: %s" % (row_num, values))
            row_num+=1
        print("Readed %d lines in csv file." % row_num)
        return successful, data
    """
    edit_json_from_lists
    """
    @classmethod
    def edit_json_from_lists(self, json_data = None, list_of_list = None):
        if json_data is None:
            json_data = self._json_data
        successful = True
        for pair in list_of_list:
            key = pair[0]
            value = pair[1]
            if key in json_data:
                print("Changing key: %s with value: %s" % (key, value))
                json_data[key] = value
        return successful, json_data

    """
    process_all_files: Require initialize process_function with set_process_function
    """
    @classmethod
    def process_all_files(self, path, print_files = False):
        self.set_input_path(path)
        for filename in os.listdir(path):
            basefilename, file_extension = os.path.splitext(filename)
            if print_files == True:
                print("File: %s will process, it has extension: %s" % (basefilename, file_extension))
            successful, json_data = self.read_json_from_file(filename)
            self.process_function(successful, json_data)
        return None
    """
    process_all_files_in_folders: Require initialize process_function with set_process_function
    """
    @classmethod
    def process_all_files_in_folders(self, path, print_folders = False, print_files = False):
        for root, directories, filenames in os.walk(path):
            print("Processing with root path: %s" % root)
            for directory in directories:
                if print_folders == True:
                    print("Checking folder: %s" % directory)
                    print("\n")
                current_dir = os.path.join(path, directory)
                self.set_input_path(current_dir)
                for filename in os.listdir(os.path.join(path, directory)):
                    basefilename, file_extension = os.path.splitext(filename)
                    if print_files == True:
                        print("File: %s will process" % basefilename)
                    successful, json_data = self.read_json_from_file(filename)
                    #print(successful)
                    self.process_function(successful, json_data)
        return None
