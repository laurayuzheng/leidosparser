import csv

# reads the plaintext from the csv file.
# filename is the csv file
# writeto is the file the plaintext is written to.
def read_csv(filename, writeto):
	with open(filename, mode='r') as csv_file:
		csv_reader = csv.DictReader(csv_file)
		line_count = 0
		file = open(writeto, "w+")
		for row in csv_reader:
			if line_count == 0:
				#print(f'Column names are {", ".join(row)}')
				line_count += 1
			#print(f'\tsummaryText: {row["summaryText"]}')
			#print(row["summaryText"])
			#file.write(f'{row["summaryText"]}')
			file.write(row["summaryText"])
			line_count += 1
		file.close()
		print(f'Processed {line_count} lines.')



if __name__ == "__main__":
	read_csv('b_result.csv','b_result_plaintext.txt')