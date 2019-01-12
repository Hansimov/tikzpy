import struct

my_number = 4
with open('z_test_binary.dat', 'wb') as file_handle:
    file_handle.write(struct.pack('i', my_number))



with open('z_test_binary.dat', 'rb') as file_handle:
    my_number_back = struct.unpack('i', file_handle.read())[0]
    print(my_number_back)