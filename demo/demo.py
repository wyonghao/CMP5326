import pytsk3
import hashlib
import os
#1
evidence_file = None

#2
menu = ("Program Options Menu\n"
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

# Function to print the menu string
def display_menu():
    print(menu)

# 3 Function to get an option from the user
def get_option():
    option_num = input("Please enter menu option> ")
    return option_num

#4
def open_evidence_file():

    global evidence_file

#prompt the user for the name of the evidence file to open
#if user presses enter, use the default file name "diskimageMT.001"

    evidence_file_name = input("Please enter name of evidence file to open (default: diskimageMT.001)> ")  
    if evidence_file_name == "":
        evidence_file_name = "diskimageMT.001"
        print(f"Using default file name {evidence_file_name}")
    else:
        print(f"Using file name {evidence_file_name}")

#open the evidence file and assign it to the evidence_file variable
#if the file does not exist, print an error message and return to the main menu
    if os.path.exists(evidence_file_name) == False:
        print("ERROR: File does not exist!!!")
        input("Press enter to continue")
        return
    else:
        evidence_file = pytsk3.Img_Info(evidence_file_name)
        print("Evidence file opened successfully!!")
        
        print("#"*45)
        # 4.1 Display the size of the disk image in raw bytes
        size =evidence_file.get_size()
        print(f"The image file is {size} bytes in size")
        totalSecors = size/512
        print(f"Total number of sectors in image is {totalSecors} ")

        volume_info = pytsk3.Volume_Info(evidence_file)
        print(f'Size of the block is set to {volume_info.info.block_size}')

        # 6
        partition_table = pytsk3.Volume_Info(evidence_file)
        
        # 14 Determining Partition Layout, Slide 18
        partition_table_type = partition_table.info.vstype
        if partition_table_type == pytsk3.TSK_VS_TYPE_DOS:
            print ("Partition table is MBR")
        else:
            print("Partition table is  GPT")
        
        print("#"*45)
        
        input("Press enter to continue")
        return
#5
def list_partitions():
    global evidence_file

    partition_table = pytsk3.Volume_Info(evidence_file)

    print("List of Partitions \n\n")
    print('Partition number \tDesc\t Start Sector\t Number of Sectors')
    print('-' * 89)

    partition_count = 1
    for partition in partition_table:
        print(f"{partition_count:<20}{partition.desc.decode('ascii'):<24}{partition.start:<17}{partition.len:<16}")
        partition_count += 1
    print('\n\n')

def open_partition():
    print("TODO")

def list_files():
    print("TODO")

def display_file_details():
    print("TODO")

#6
def run_main():
    #7
    selected_option =0
    #8
    while selected_option != 6:
        #9
        display_menu()
        #10
        selected_option = get_option()
        #11
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
        else:
            print('Input not recongnised')

#12
if __name__ == "__main__":
    run_main()