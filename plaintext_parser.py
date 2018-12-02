import csv

# Notes: bash script runs every 6 hours
# Pulls about 25 XML files (?)
# Erin's parser makes an XML file for each category
# Resulting CSV file has 1 row for each XML file.
# This parser should take each CSV (5 max, 2-3?) file 
	# and extract the summary data as strings or a file (currently for file)
# 

# reads the plaintext from the csv file.
# filename is the csv file
# writeto is the file the plaintext is written to.
# returns integer, number of files created.
def read_csv(filename, writeto):
	with open(filename, mode='r') as csv_file:
		csv_reader = csv.DictReader(csv_file)
		line_count = 0
		for row in csv_reader:
			if line_count == 0:
				#print(f'Column names are {", ".join(row)}')
				line_count += 1
			#file = open(writeto + "%d.txt" % line_count, "w+")
			#file.write(row["summaryText"])
			#file.close()
			result = [x.strip() for x in row["summaryText"].split(',')]
			print(f'Processed line {line_count}.')

			for i in range(0,len(result)):
				print(result[i])
			
			line_count += 1
		#print(f'Processed {line_count} lines.')
		return line_count


#def parse_text(file):

if __name__ == "__main__":
	num_files = read_csv('b_result.csv','b_result_plaintext')