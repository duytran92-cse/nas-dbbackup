from django.core.management.base import BaseCommand#, CommandError
from django.utils import timezone
from notasquare.urad_api.containers.standard import Container
from application.models import *
from django.conf import settings
import json,pika,os

# import json, pika, os


class Command(BaseCommand):
    # def handle(self, *args, **kwargs):

    # 	params = {}
    # 	params['_pagernum'] = 10
    # 	params['_sort_key'] = 'id'
    # 	params['_sortdir']	= 'desc'

    # 	variation_bulk 	= []
    # 	gene_bulk		= []
    #     exon_bulk       = []

    # 	isDone = False
    # 	page = 1
    # 	while not isDone:
    # 		params['_pageroffset'] = (page - 1) * 10

    # 		_variation = Container().call_api(settings.GENODATA_API_URL + '/variation/list_detail', GET=params)
    # 		variation_records = _variation['records']
    		
    # 		page = page + 1
    # 		if len(variation_records) == 0:
    # 			isDone = True
    # 		for item in variation_records:
				# variation = Variation()
				# variation.rsnumber = item.keys()[0]
				# variation.chromosome = item.values()[0].get('chromosome')
				# variation.position 				= item.values()[0].get('position')
				# variation.gene 					= item.values()[0].get('gene')
				# variation.associated_disease 	= item.values()[0].get('associated_disease')
				
				# # #--- hard code -----
				# # variation.chromosome = '21'
				# # variation.position = 10000
				# # variation.gene = 'ABC'
				# # variation.associated_disease = 'true'	
			
				# variation_bulk.append(variation)																																							
											
    #     Variation.objects.bulk_create(variation_bulk)

        # # import Gene
        # isDone = False
        # page = 1
        # while not isDone:
        #     params['_pageroffset'] = (page - 1) * 10 
        #     _gene = Container().call_api(settings.GENODATA_API_URL + '/gene/list_detail', GET=params) 			# get json of variation
        #     gene_records = _gene['records']
        #     page = page + 1  
        #     if len(gene_records) == 0:
        #         isDone = True                                                                                   # no data to read 
        #     for item in gene_records:
        #         gene = Gene()
        #         gene.name = item.keys()[0]
        #         gene.start = item.values()[0].get('start')                            
        #         gene.end = item.values()[0].get('end')
        #         gene.description = item.values()[0].get('description')
        #         gene.normal_function = item.values()[0].get('normal_function')
        #         gene.biotype = item.values()[0].get('biotype')
        #         gene.havana_gene = item.values()[0].get('havana_gene')
        #         gene.chromosome = item.values()[0].get('chromosome')
        #         gene.num_of_gene = item.values()[0].get('num_of_gene')
        #         gene.num_of_snp = item.values()[0].get('num_of_snp')
        #         gene.is_reversed = item.values()[0].get('is_reversed')
        #         gene_bulk.append(gene)                                                                                                                                                                
        # #     #end for ----> bulk_create                                   
        # Gene.objects.bulk_create(gene_bulk)


        # # import Exon
        # isDone = False
        # page = 1
        # while not isDone:
        #     params['_pageroffset'] = (page - 1) * 10 
        #     _exon = Container().call_api(settings.GENODATA_API_URL + '/exon/list_detail', GET=params)           # get json of variation
        #     exon_records = _exon['records']
        #     page = page + 1  
        #     if len(exon_records) == 0:
        #         isDone = True                                                                                   # no data to read 
        #     for item in exon_records:
        #         exon = Exon()
        #         exon.name = item.keys()[0]
        #         exon.rank = item.values()[0].get('rank')                            
        #         exon.start = item.values()[0].get('start')
        #         exon.end = item.values()[0].get('end')
        #         exon.gene = item.values()[0].get('gene')
        #         exon.id_gene = item.values()[0].get('id_gene')
        #         exon.num_variation = item.values()[0].get('num_variation')
        #         exon.chromosome = item.values()[0].get('chromosome')
        #         exon_bulk.append(exon)                                                                                                                                                                
        # #     #end for ----> bulk_create                                   
        # Exon.objects.bulk_create(exon_bulk)
	# def consume(self, ch, method, properties, body):
	# 	_variation = json.loads(body)

	# 	variation_bulk = []

	# 	variation = Variation()

	# 	variation.rsnumber = _variation[2]
	# 	variation.chromosome = '21'
	# 	variation.position = 10000
	# 	variation.gene = 'ABC'
	# 	variation.associated_disease = 'true'
	# 	variation_bulk.append(variation)
	# 	Variation.objects.bulk_create(variation_bulk)

	# 	print 'import done'
		# print '------> %s' %(body)
		# params = {}
		# params['_pagernum'] = 10
		# params['_sort_key'] = 'id'
		# params['_sortdir']	= 'desc'

		# variation_bulk 	= []
		# isDone = False
		# page = 1
		# while not isDone:
		# 	params['_pageroffset'] = (page - 1) * 10
		# 	_variation = json.loads(body)
		# 	page = page + 1
		# 	if len(_variation) == 0:
		# 		isDone = True
		# 		# print _variation
		# 	for item in _variation:
		# 		variation = Variation()
		# 		variation.rsnumber = item[0]
		# 		print variation.rsnumber

	# def process(self, params = {}):
	def handle(self, *args, **kwargs):
		print "[x] RECEIVING DATA"
		# credentials = pika.PlainCredentials(settings.RABBITMQ_USER, settings.RABBITMQ_PASS)
		# connection = pika.BlockingConnection(pika.ConnectionParameters(settings.RABBITMQ_HOST, settings.RABBITMQ_PORT, '/', credentials))
		# channel = connection.channel()
		# channel.queue_declare(queue="test_queue", durable=True)
		# print "[*] Waiting for data. To exit press CTRL+C"     
		# channel.basic_consume(self.consume, queue="test_queue", no_ack=True)
		# channel.start_consuming()