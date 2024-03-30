#########################
# CSV to BIN converter for Multicomp Pro MP750290 
# Arbitrary waveform generator. (May work for others)
#
# Note CSV should NOT have a header
#
# by @baldengineer, 2021-08-03

# In/Out Filenames
output_filename = 'sine_1meg.bin'
input_filename  = 'SINE_1MEG.CSV'

# CSV Stuff
csv_delim = ','
csv_column = 1  # zero-based column index

#########################
# get the min, max voltages and number of points
# arb's min/max is 0 to 20000
# seeds to find the min max (don't change these)
max = 0
min = 20000

print("Getting data stats...", end='')
csv_file = open(input_filename)
sample_count = 0
for line in csv_file:
	sample_count = sample_count + 1
	fields = line.strip().split(csv_delim)
	voltage = int((float("{:.3f}".format(float(fields[csv_column]))) * 1000) + 10000)
	if (voltage > max):
		max = voltage
	if (voltage < min):
		min = voltage
csv_file.close()

print("done")
print("Max: " + str(max))
print("Min: " + str(min))
print("Line Count: " + str(sample_count))

#########################
# write binary file
print("\nCreating binary file...", end='')
# open files
csv_file = open(input_filename)
output_file = open(output_filename, 'wb')

# 4 bytes of 0x0 for insert mode
output_file.write(int(0).to_bytes(4,'little'))

# 4 bytes for max voltage
output_file.write(max.to_bytes(4,'little'))

# 4 bytes for min voltage
output_file.write(min.to_bytes(4,'little'))

# 4 bytes for sample count
output_file.write(sample_count.to_bytes(4,'little'))

# 32 bytes for filename
encoded_string = output_filename.encode()
output_file.write(bytearray(encoded_string))
padding_bytes = 32-len(output_filename)
output_file.write(int(0).to_bytes(padding_bytes,'little'))

# scan through CSV and append binary values
for line in csv_file:
	fields = line.strip().split(csv_delim)
	voltage = int((float("{:.3f}".format(float(fields[csv_column]))) * 1000) + 10000)
	output_file.write(voltage.to_bytes(2,'little'))
print("done")
