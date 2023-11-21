import pytsk3
import hashlib
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

    evidence_file_name = input("Please enter name of evidence file to open> ")

    evidence_file = pytsk3.Img_Info(evidence_file_name)
#5
def list_partitions():
    global evidence_file

    partition_table = pytsk3.Volume_Info(evidence_file)

    print("List of Partitions \n\n")
    print('Partition number \tDesc\t\t\t\t\tStart Sector\t Number of Sectors')
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