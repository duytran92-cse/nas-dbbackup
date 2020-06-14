import urllib2
import shutil
import os

url = "ftp://ftp.ensembl.org/pub/release-88/fasta/homo_sapiens/dna/"

dataset = ["Homo_sapiens.GRCh38.dna.chromosome.1.fa.gz", "Homo_sapiens.GRCh38.dna.chromosome.2.fa.gz", "Homo_sapiens.GRCh38.dna.chromosome.3.fa.gz",
			"Homo_sapiens.GRCh38.dna.chromosome.4.fa.gz", "Homo_sapiens.GRCh38.dna.chromosome.5.fa.gz", "Homo_sapiens.GRCh38.dna.chromosome.6.fa.gz",
			"Homo_sapiens.GRCh38.dna.chromosome.7.fa.gz", "Homo_sapiens.GRCh38.dna.chromosome.8.fa.gz", "Homo_sapiens.GRCh38.dna.chromosome.9.fa.gz",	
			"Homo_sapiens.GRCh38.dna.chromosome.10.fa.gz", "Homo_sapiens.GRCh38.dna.chromosome.11.fa.gz", "Homo_sapiens.GRCh38.dna.chromosome.12.fa.gz",
			"Homo_sapiens.GRCh38.dna.chromosome.13.fa.gz", "Homo_sapiens.GRCh38.dna.chromosome.14.fa.gz", "Homo_sapiens.GRCh38.dna.chromosome.15.fa.gz",
			"Homo_sapiens.GRCh38.dna.chromosome.16.fa.gz", "Homo_sapiens.GRCh38.dna.chromosome.17.fa.gz", "Homo_sapiens.GRCh38.dna.chromosome.18.fa.gz",
			"Homo_sapiens.GRCh38.dna.chromosome.19.fa.gz", "Homo_sapiens.GRCh38.dna.chromosome.20.fa.gz", "Homo_sapiens.GRCh38.dna.chromosome.21.fa.gz",
			"Homo_sapiens.GRCh38.dna.chromosome.22.fa.gz", "Homo_sapiens.GRCh38.dna.chromosome.MT.fa.gz", "Homo_sapiens.GRCh38.dna.chromosome.X.fa.gz",
			"Homo_sapiens.GRCh38.dna.chromosome.Y.fa.gz"]

for index in range(len(dataset	)):
	file_name = url + dataset[index]
	u = urllib2.urlopen(file_name)
	#urllib.urlretrieve(file_name, "/home/ttduy/Desktop")
	f = open(dataset[index], 'wb')
	meta = u.info()
	file_size = int(meta.getheaders("Content-Length")[0])
	print "Downloading: %s Bytes: %s" % (file_name, file_size)

	file_size_dl = 0
	block_sz = 8192
	while True:
		buffer = u.read(block_sz)
		if not buffer:
			break

		file_size_dl += len(buffer)
		f.write(buffer)
		status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
		status = status + chr(8)*(len(status)+1)
		print status,
	f.close()
	#move dataset to /opt/data
	shutil.move(os.getcwd() + '/' + dataset[index], "/opt/data")