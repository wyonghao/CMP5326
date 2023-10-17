'''
PartitionTableDecodify 0.5
A simple procedural piece of code to play with partitions.
This program has no style. It is intended to be easy to understand.
'''

# Run the below 4 times
for partition_num in range(0, 4):

    # inputs
    start_lba = int(input("Enter the start LBA for the partition > " ))
    number_of_sectors_in_partition = int(input("Please input number of sectors value for the partition> "))
    boot_byte = input("Please input The value of teh Active Byte> ")
    partition_type = input("Please input The value of the partition type byte> ")

    # calculations
    offset_to_partition_in_bytes = start_lba * 512
    size_of_partition_in_bytes = number_of_sectors_in_partition *512


    # outputs
    print(f"The size of the first partition, in bytes, is {size_of_partition_in_bytes}")
    print(f"The size of the first partition, in kibibytes, is {size_of_partition_in_bytes/1024}")
    print(f"The size of the first partition, in mibibytes, is {size_of_partition_in_bytes/1048576}")
    print(f"The size of the first partition, in gibibytes, is {size_of_partition_in_bytes/1073741824}")

    print(f"The active byte is: {boot_byte}")
    print(f"The partition type is: {partition_type}")


    print(f"The offset to the first partition, in bytes, is {offset_to_partition_in_bytes}")
    print(f"Use the winHex Navigation GoTo Offset to move the cursor to offset {offset_to_partition_in_bytes}" )

    if boot_byte == "80":
        print("Partition is bootable")
    else:
        print("Partition is not bootable")

    if partition_type == "05":
        print("The partition is DOS 3.3+ Extended Partition ")
    elif partition_type == "06":
        print("The partition is DOS 3.31+ 16-bit FAT (over 32M) ")
    elif partition_type == "07":
        print("The partition is Windows NT NTFS ")
    elif partition_type == "08":
        print("The partition is exFAT ")
    elif partition_type == "0B":
        print("The partition is WIN95 OSR2 FAT32 ")
    else:
        print("Unknown partition id value")

# End of Program