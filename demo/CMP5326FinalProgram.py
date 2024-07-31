import pytsk3
import hashlib
import os
import tkinter as tk
from tkinter import filedialog
import pyewf
import csv

# Global variables to hold the evidence file and file system information
evidence_file = None
file_system = None

# Program options menu
menu = (
    "Program Options Menu\n"
    "--------------------\n"
    "\n"
    "1. Open an evidence file\n"
    "2. List Partitions in evidence file\n"
    "3. Open a partition in evidence file\n"
    "4. List files in partition\n"
    "5. Display details about file\n"
    "6. Exit program\n"
    "\n"
)

def display_menu():
    """Function to print the menu string"""
    print(menu)

def get_option():
    """Function to get an option from the user"""
    option_num = input("Please enter menu option> ")
    return option_num

def open_evidence_file():
    """Function to open a forensic image file"""
    global evidence_file

    evidence_file_name = input("Please enter name of evidence file to open (default: diskimageMT.001)> ")
    if evidence_file_name == "":
        evidence_file_name = "diskimageMT.001"
        print(f"Using default file name {evidence_file_name}")
    else:
        print(f"Using file name {evidence_file_name}")

    if not os.path.exists(evidence_file_name):
        print("ERROR: File does not exist!!!")
        input("Press enter to continue")
        return
    else:
        try:
            evidence_file = pytsk3.Img_Info(evidence_file_name)
            print("Evidence file opened successfully!!")

            print("#" * 45)
            size = evidence_file.get_size()
            print(f"The image file is {size} bytes in size")
            total_sectors = size // 512
            print(f"Total number of sectors in image is {total_sectors} ")

            volume_info = pytsk3.Volume_Info(evidence_file)
            print(f'Size of the block is set to {volume_info.info.block_size}')

            partition_table_type = volume_info.info.vstype
            if partition_table_type == pytsk3.TSK_VS_TYPE_DOS:
                print("Partition table is MBR")
            elif partition_table_type == pytsk3.TSK_VS_TYPE_GPT:
                print("Partition table is GPT")
            else:
                print("Unknown partition table type")
            print("#" * 45)

        except Exception as e:
            print(f"ERROR: {e}")
        input("Press enter to continue")

def list_partitions():
    """Function to list partitions in the forensic image"""
    global evidence_file
    if evidence_file is None:
        print("No evidence file is open. Please open an evidence file first.")
        input("Press enter to continue")
        return

    try:
        partition_table = pytsk3.Volume_Info(evidence_file)
        print("List of Partitions \n\n")
        print('Partition number \tDesc\t Start Sector\t Number of Sectors')
        print('-' * 89)

        partition_count = 1
        for partition in partition_table:
            print(f"{partition_count:<20}{partition.desc.decode('ascii'):<24}{partition.start:<17}{partition.len:<16}")
            partition_count += 1
        print('\n\n')
    except Exception as e:
        print(f"ERROR: {e}")
    input("Press enter to continue")

def open_partition():
    """Function to open a specific partition in the forensic image"""
    global evidence_file, file_system

    if evidence_file is None:
        print("No evidence file is open. Please open an evidence file first.")
        input("Press enter to continue")
        return

    try:
        partition_table = pytsk3.Volume_Info(evidence_file)
        partition_num = int(input("Enter the partition number to open: "))
        partition = list(partition_table)[partition_num - 1]
        offset = partition.start * 512  # Assuming sector size is 512 bytes
        file_system = pytsk3.FS_Info(evidence_file, offset)
        print(f"Partition {partition_num} opened.")
    except (ValueError, IndexError):
        print("Invalid partition number.")
    except Exception as e:
        print(f"ERROR: {e}")
    input("Press enter to continue")

def list_files_in_directory(dir_path, depth=0, max_depth=3):
    """Recursive function to list files in a directory up to a certain depth"""
    global file_system

    if file_system is None:
        print("No partition is open. Please open a partition first.")
        return

    if depth > max_depth:
        return

    try:
        directory = file_system.open_dir(path=dir_path)
        for file in directory:
            file_name = file.info.name.name.decode("utf-8")
            full_path = os.path.join(dir_path, file_name)
            print(full_path)

            if file.info.name.type == pytsk3.TSK_FS_NAME_TYPE_DIR and file_name not in [".", ".."]:
                list_files_in_directory(full_path, depth + 1, max_depth)
    except IOError:
        pass

def list_files():
    """Function to list files in the currently open partition"""
    directory_path = input("Enter the directory path to list files (default: root '/'): ")
    if directory_path == "":
        directory_path = "/"
    list_files_in_directory(directory_path)
    input("Press enter to continue")

def display_file_details():
    """Function to display details about a specific file"""
    global file_system

    if file_system is None:
        print("No partition is open. Please open a partition first.")
        input("Press enter to continue")
        return

    file_path = input("Enter the file path to display details: ")
    if file_path == "":
        print("No file path entered.")
        return

    try:
        file_object = file_system.open(file_path)
        print(f"File name: {file_object.info.name.name.decode('utf-8')}")
        print(f"File size: {file_object.info.meta.size} bytes")
        print(f"Created time: {file_object.info.meta.crtime}")
        print(f"Modified time: {file_object.info.meta.mtime}")
        print(f"Accessed time: {file_object.info.meta.atime}")
        print(f"Changed time: {file_object.info.meta.ctime}")

        file_hash = hashlib.sha1()
        for file_attr in file_object:
            if file_attr.info.type == pytsk3.TSK_FS_ATTR_TYPE_DEFAULT:
                file_data = file_attr.read_random(0, file_attr.info.size)
                file_hash.update(file_data)
        print(f"SHA1 Hash: {file_hash.hexdigest()}")

        if hasattr(file_object.info.meta, 'mode'):
            print(f"Permissions: {oct(file_object.info.meta.mode)}")

    except IOError:
        print(f"Could not open file {file_path}.")
    except Exception as e:
        print(f"ERROR: {e}")

    input("Press enter to continue")

def run_main():
    """Main function to run the program"""
    selected_option = 0
    while selected_option != 6:
        display_menu()
        selected_option = get_option()
        if selected_option == '1':
            open_evidence_file()
        elif selected_option == '2':
            list_partitions()
        elif selected_option == '3':
            open_partition()
        elif selected_option == '4':
            list_files()
        elif selected_option == '5':
            display_file_details()
        elif selected_option == '6':
            print("Exiting Program.")
            break
        else:
            print('Input not recognized')

if __name__ == "__main__":
    run_main()
