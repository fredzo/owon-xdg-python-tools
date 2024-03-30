#########################
# Generated a BIN file from the provided 406 Mhz Cospas/Sarsat beacon frame
# This bin file can be loaded in an Owon XDG or Multicomp MP75xxx
# Arbitrary waveform generator.
#
# by @fredzo, 2024-03-30

# In/Out Filenames
output_filename = 'frame_406.bin'
input_frame  = 'FFFED0D6E6202820000C29FF51041775302D'
input_bits = bin(int(input_frame, base=16))[2:]

input_bits_nrz = ''
last_bit = int(input_bits[0])
last_nrzbit = 0b0
for input_bit in input_bits:
	if last_bit == int(input_bit):
		input_bits_nrz += str(int(not last_nrzbit))
		input_bits_nrz += str(last_nrzbit)
	else:
		input_bits_nrz += str(last_nrzbit)
		input_bits_nrz += str(int(not last_nrzbit))
		last_nrzbit = int(not last_nrzbit)
	last_bit = int(input_bit)


#########################
# get the min, max voltages and number of points
# arb's min/max is 0 to 20000
minValue = 0
maxValue = 20000
# Target size for the bin file (number of samples, max is 10,000,000)
waveSize = 1000000
zero = int(maxValue/2)
ttl = int(zero + 3.3 * 1000) # 1 volt = 1000 units
bitNumber = len(input_bits_nrz)
bitSize = round(waveSize / bitNumber)
# update waveSize with the exact value according to number of bits and bit size
waveSize = bitSize * bitNumber

print("Wave preparation :")
print("Bytes : " + input_frame)
print("Bits : " + input_bits)
print("BitsNrz : " + input_bits_nrz)
print("0 v : " + str(zero))
print("Ttl : " + str(ttl))
print("Bit number: " + str(bitNumber))
print("Bit size: " + str(bitSize))

#########################
# write binary file
print("\nCreating binary file...", end='')
# open files
output_file = open(output_filename, 'wb')

# 4 bytes of 0x0 for insert mode
output_file.write(int(0).to_bytes(4,'little'))

# 4 bytes for max voltage
output_file.write(ttl.to_bytes(4,'little'))

# 4 bytes for min voltage
output_file.write(zero.to_bytes(4,'little'))

# 4 bytes for sample count
output_file.write(waveSize.to_bytes(4,'little'))

# 32 bytes for filename
encoded_string = output_filename.encode()
output_file.write(bytearray(encoded_string))
padding_bytes = 32-len(output_filename)
output_file.write(int(0).to_bytes(padding_bytes,'little'))

# scan through CSV and append binary values
sampleCount = 0
for bit in input_bits_nrz:
	for sample in range(0,bitSize):
		voltage = zero if (bit == '0') else ttl
		output_file.write(voltage.to_bytes(2,'little'))
		sampleCount=sampleCount+1

print("done")
