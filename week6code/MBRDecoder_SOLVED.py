# Add the regex library to the program
import re

# 1 open the disk image file
f = open('DiskImage.001', 'rb')

# 2 Read the mbr which is the first 512 bytes
mbr = f.read(512)

# Close the file.
f.close()

# 3 Display the value of the byte at the offset
print(f"Active part of the first partition is {mbr[446]}")

# 8 We are building a regex that is looking at bytes here. So each . represent a single byte.
# mbr_re = b"^.{446}((?P<active_byte>.)(?P<start_chs>.{3})(?P<partition_type>.)(?P<end_chs>.{3})(?P<start_lba>.{4})(?P<num_sectors>.{4})){4}\x55\xAA"
mbr_re = b"^.{446}(?P<active_byte_part1>.)(?P<start_chs_part1>.{3})(?P<partition_type_part1>.)(?P<end_chs_part1>.{3})(?P<start_lba_part1>.{4})(?P<num_sectors_part1>.{4})(?P<active_byte_part2>.)(?P<start_chs_part2>.{3})(?P<partition_type_part2>.)(?P<end_chs_part2>.{3})(?P<start_lba_part2>.{4})(?P<num_sectors_part2>.{4})(?P<active_byte_part3>.)(?P<start_chs_part3>.{3})(?P<partition_type_part3>.)(?P<end_chs_part3>.{3})(?P<start_lba_part3>.{4})(?P<num_sectors_part3>.{4})(?P<active_byte_part4>.)(?P<start_chs_part4>.{3})(?P<partition_type_part4>.)(?P<end_chs_part4>.{3})(?P<start_lba_part4>.{4})(?P<num_sectors_part4>.{4})\x55\xAA"

# 9 Create a regex object for the MBR regular expression.
regex = re.compile(mbr_re, re.DOTALL)

# 10 Match the MBR and store the resulting match object in m
m = regex.match(mbr)

# 11 Process the match provided there is one
if m is not None:
  # 12 We are taking this from the named regex
    active_byte = m.group('active_byte_part1')

    # 13. Check if active byte is ox80. Note to have to check for character code x80
    if active_byte ==b'\x80':
        print('Partition is active')
    else:
        print('Partition is not active')
#
    #14  Get the partition type byte value
    partition_type_byte = m.group('partition_type_part1')
    # print(partition_type_byte)
#
    # 15 Check partition type byte value against a number of values as there are different partitions.
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
