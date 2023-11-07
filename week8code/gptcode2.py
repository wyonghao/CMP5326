import pytsk3

# Replace 'disk_image_path' with the path to your disk image file.
disk_image_path = 'path/to/your/disk_image.dd'

# Open the disk image using pytsk3.
img_info = pytsk3.Img_Info(disk_image_path)

# Create a TSK filesystem object for the disk image.
fs_info = pytsk3.FS_Info(img_info)

# Get the list of partitions on the disk image.
partitions = fs_info.info.meta

# Display the partition table.
print("Partition Table:")
for partition in partitions:
    print("Partition ID: {}".format(partition.addr))
    print("Description: {}".format(partition.desc.decode('utf-8')))
    print("Offset (in sectors): {}".format(partition.start))
    print("Length (in sectors): {}".format(partition.len))
    print("File System Type: {}".format(partition.fstype))
    print()

# Close the disk image.
fs_info.close()
