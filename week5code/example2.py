'''

PartitionTableDecodify 0.2
A simple procedural piece of code to play with partitions.
'''

# inputs
start_lba = int(input("Enter the start LBA for the partition > " ))
number_of_sectors_in_partition = int(input("Please input number of sectors value for the partition> "))
boot_byte = int(input("Please input The value of teh Active Byte> "))
partition_type = int(input("Please input The value of the partition type byte> "))

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