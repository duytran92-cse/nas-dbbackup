import gzip

from notasquare.urad_api import *
from application.models import *
from application.settings import dev as settings
from application.modules.sequences import components
from django.core.management.base import BaseCommand, CommandError
from application.models import *

from multiprocessing.pool import ThreadPool
import time

class Command(BaseCommand):
	def resolve_offset(self, pos):
		num_lines = int(pos / 60)
		line_offset = pos % 60
		return (num_lines * 61) + line_offset - 1

	def get_data(self, data = {}):	
		# push chromosome, position (start)
		start = data['start']
		end = start + 200
		chromosome = data['chromosome']
		file = settings.FASTSA[chromosome]

		with gzip.open(file) as file:
			base_offset = 0
			for line in file:
				base_offset = len(line)
				break
			start_offset = base_offset + self.resolve_offset(start)
			end_offset = base_offset + self.resolve_offset(end)
			if start_offset > end_offset:
				return ''
			sequence = ''
			file.seek(start_offset, 0)
			for i in range(start_offset, end_offset):
				c = file.read(1)
				if c == '\n':
					continue
				sequence += c
			print sequence
			# return {
   #              'parameters': {'chromosome': '1','start': start, 'end': end, 'position':95010},
   #              'sequence': sequence,
   #          }
   		print sequence
		return {}			

	def handle(self, *args, **kwargs):
		# read dataset

		chromosome = ''	#empty string
		start = 0

		start_time = time.time()	#start timer
		
		with open('test100request.txt') as f:		#==> using text file to test => need to: insert text file (e.g: test5000request.txt, test10000request.txt)
			dataSet = f.readlines()
			for index in range(len(dataSet)):
				stringDataSet = dataSet[index].replace('(', '').replace(')', '').split(',')
				chromosome = stringDataSet[0]
				start = int(stringDataSet[1])
				data = {
						'start': start,
						'chromosome': chromosome,
				}
				# self.get_data(data)
				results = ThreadPool(10).imap_unordered(self.get_data, data)
				# print(results)
		elapsed_time = time.time() - start_time
		print(elapsed_time)