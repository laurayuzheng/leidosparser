import csv

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
			file = open(writeto + "%d.txt" % line_count, "w+")
			file.write(row["summaryText"])
			file.close()
			print(f'Processed line {line_count}.')
			line_count += 1
		#print(f'Processed {line_count} lines.')
		return line_count


#def parse_text(file):

if __name__ == "__main__":
	num_files = read_csv('b_result.csv','b_result_plaintext')