'''

PartitionTableDecodify 0.1
A simple procedural piece of code to play with partitions.
'''

start_lba = int(input("Enter the start LBA for the partition >" ))

offset_to_partition_in_bytes = start_lba * 512

print(f"The offset to the first partition, in bytes, is {offset_to_partition_in_bytes}")

print(f"Use the winHex Navigation GoTo Offset to move the cursor to offset {offset_to_partition_in_bytes}" )
