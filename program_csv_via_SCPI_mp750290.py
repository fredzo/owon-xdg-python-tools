### Tested with Multicomp Pro MP750290
### However. Some of the commands cause it to lock-up
### or fail communication. (Cannot figure out why)

import pyvisa
import time

# variables
file_name = 'decimated.csv'
ip_addr = '192.168.128.99' # set ip here
mp_arb_string = 'TCPIP0::' + ip_addr + '::3000::SOCKET'


#############################################	
#############################################
# file handling stuff
# need sample count before programming arb
def count_lines():
	input_file = open(file_name)
	line_counter = 0
	for line in input_file:
		line_counter = line_counter + 1
	#print ('Found: ' + str(line_counter) + ' lines.')
	input_file.close()
	return str(line_counter)

def program_samples(samples):
	input_file = open(file_name)
	line_counter = 0
	wait_time = 0.1
	est_seconds = wait_time * samples
	print("Estimated: " + str(est_seconds) + " seconds.")
	for line in input_file:
		# skip the header
		if (line_counter > 0):
			line_list = line.split(',')
			sample = line_list[1].strip()
			#print(sample.strip() + 'V')
			# DATA:DATA:VALue EMEMory,200,1.5V
			arb.write('DATA:DATA:VALue EMEMory, ' + str(line_counter) + ',' + sample + 'V')
			time.sleep(wait_time)
			if (line_counter % 10 == 0):
				print(".", end='')
		line_counter = line_counter + 1
	print('Done.')
	input_file.close()

#############################################	
#############################################
# get this
rm = pyvisa.ResourceManager()

# connect to box
arb = rm.open_resource(mp_arb_string)

# get timeouts without these
arb.read_termination = '\n'
arb.write_termination = '\n'

# check to see if it responds
print(arb.query('*IDN?'))

point_count = count_lines().strip()
print ('Found: ' + point_count + ' lines.')

arb.write('DATA:POINts EMEMory, ' + point_count)

program_samples(int(point_count))


# kthxbai
rm.close()