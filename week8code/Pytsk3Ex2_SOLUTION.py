# 1 Import the required Library
import pytsk3

# 2 Create a new IMG_Info object by opening the file and name object as diskimage
file_name = "diskimageMT.001"
diskimage = pytsk3.Img_Info(file_name)

# # 3 Display the size of the disk image in raw bytes
# print(f"The image file size is {diskimage.get_size()} bytes in size")

# 4 Display a message to the iuser that the image has been loaded:
print(f'Loaded {file_name} image file')
print("#"*35)

# 4,2 closes the disk image much like the close method unlinked a file from a program using Python File I/O.
diskimage.close()

# 5 Display the number of sectors there are in the disk image file
size =diskimage.get_size()
print(f"The image file is {size} bytes in size")
totalSecors = size/512
print(f"Total number of sectors in image is {totalSecors} ")

volume_info = pytsk3.Volume_Info(diskimage)
print(f'Size of the block is set to {volume_info.info.block_size}')

# 6
partition_table = pytsk3.Volume_Info(diskimage)

# 14 Determining Partition Layout, Slide 18
partition_table_type = partition_table.info.vstype
if partition_table_type == pytsk3.TSK_VS_TYPE_DOS:
    print ("Partition table is MBR")
else:
    print("Partition table is  GPT")


#7
print ('Partition number \tDesc\t\t\t\t\tStart Sector\t Number of Sectors')
print ('-'*89)



#8
partition_count =1

#9
partition_offsets = []

# 42 Summing up the unallocated
unallocated =0

#10
for partition in partition_table:
    # 42b totalling the unallocated space
    if partition.desc.decode('ascii') == "Unallocated":
        unallocated += partition.len
    print(f"{partition_count:<20}{partition.desc.decode('ascii'):<24}{partition.start:<17}{partition.len:<16}")
    partition_offsets.append(partition.start)
    partition_count +=1

# Print out the  Total allocated vs total unallocated sectors as per Task 2
print ('-'*89)
print (f"Total unallocated sectors = {unallocated}")
# Think about why I did this. If in doubt, ask!

# Fixed, Thanks to Leila for contributing the code.
print (f"Total allocated sectors = {totalSecors-unallocated}")


