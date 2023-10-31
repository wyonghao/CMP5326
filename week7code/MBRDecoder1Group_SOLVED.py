# Add the regex library to the program
import re
import struct
# 20 importing time finctions
import datetime

# open the disk image file
f = open('DiskImage.001', 'rb')

# Read the mbr which is the first 512 bytes
mbr = f.read(512)

# Close the file.
f.close()

# 1 The regex

mbr_re = b"^.{446}(?P<partition_table>.{64})\x55\xAA"

# 2 Create a regex object for the MBR regular expression.
regex = re.compile(mbr_re, re.DOTALL)

# 3 Match the MBR and store the resulting match object in m
m = regex.match(mbr)

# 4 Get the entire partition Table
partition_table_bytes = m.group("partition_table")

# 5 This statement defines a variable called partition_entry_offset.
# This variable is important as it will be used to specify the partition table entry being decoded
partition_entry_offset = 0

# 17 Open a file for writing Text
results_file = open('processing.txt', 'wt')

# 21 Create a datestamp of now
datetimestamp = datetime.datetime.now().strftime('%d/%m/%Y %H:%M')

# 22 Create a small timestamped header
results_file.write(f"Results of process image file on {datetimestamp}\n")
results_file.write(f"------------------------------------------------\n")

#6 Loop through the 4 partitions
for part_count in range(1,5):
    # 7
    print(f"Partition {part_count}")
    # 8
    active_byte = partition_table_bytes[partition_entry_offset:partition_entry_offset+1]
    # 9
    if active_byte == b'\x80':
        print("Partition is active")
        results_file.write('Partition is active\n')
    else:
        print("Partition is not active")
        results_file.write('Partition is not active\n')
    # 10
    partition_type_byte = partition_table_bytes[partition_entry_offset+4:partition_entry_offset+5]
    # 11
    if partition_type_byte == b'\x06':
        print("Partition is DOS 3.31 FAT (>32MB)")
    elif partition_type_byte == b'\x07':
        print("Partition is NTFS/OS2 HPFS/exFAT")
    elif partition_type_byte == b'\x0B':
        print("Partition is Win95 OSR2 FAT32")
    elif partition_type_byte == b'\x05':
        print("Partition is extended partition")
    else:
        print("Partition Type is not recognised)")

    # 12 Get the start lba
    start_lba_bytes = partition_table_bytes[partition_entry_offset+8:partition_entry_offset+12]

    # 13 Convert the Bytes obtained above into s single integer value
    start_lba = struct.unpack("<I",start_lba_bytes)

    # 14 Display the start LBA
    print(f"The partition start at sector {start_lba[0]}")

    # 15 Get the number of sectors un the partition, convert it and display
    num_sectors_bytes = partition_table_bytes[partition_entry_offset+12:partition_entry_offset+16]
    num_sectors = struct.unpack("<I", num_sectors_bytes)

    print(f"The number of sectors in the partition is {num_sectors[0]}")

    # 16 Update Partition entry offset to next partition entry in table
    partition_entry_offset += 16

# 18 Close the file
results_file.close()