# Add the regex library to the program
import re
import struct
# 20 importing time functions
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


# 3 Match the MBR and store the resulting match object in m


# 4 Get the entire partition Table


# 5 This statement defines a variable called partition_entry_offset.
# This variable is important as it will be used to specify the partition table entry being decoded


# 17 Open a file for writing Text


# 21 Create a datestamp of now


# 22 Create a small timestamped header


#6 Loop through the 4 partitions
for part_count in range(1,5):
    # 7

    # 8

    # 9

    # 10

    # 11


    # 12 Get the start lba


    # 13 Convert the Bytes obtained above into s single integer value

    # 14 Display the start LBA


    # 15 Get the number of sectors un the partition, convert it and display


    # 16 Update Partition entry offset to next partition entry in table


# 18 Close the file





