import json
from django.utils.module_loading import import_string
from notasquare.urad_api import tests
from application.models import *


class UnitTest(tests.BaseUnitTest):
    def setUp(self):
        pass

    def test_basic(self):
        self.init()
        self.set_headers({
            'NAS-TEST-USER-ID':       1,
            'NAS-TEST-USER-USERNAME': 'vaquan'
        })
        self.get ('List all diseases', '/disease/list')
        self.post('Create new chromosome', '/chromosome/create', {
            'name':    'Chromosome',
            'alias':   'Chromosome Alias',
            'start':   12,
            'end':     34
        })
        self.post('Create new gene', '/gene/create', {
            'chromosome':    1,
            'name':             'GENE_NAME'
        })
        self.post('Create new gene', '/gene/create', {
            'chromosome':    2,
            'name':             'GENE_NAME 2'
        })
        self.post('Create new publication', '/publication/create', {
            'pmid':     'PMID',
            'title':    'Title'
        })
        self.post('Create new publication', '/publication/create', {
            'pmid':     'PMID 2',
            'title':    'Title 2'
        })

        self.post('Create new publication', '/publication/create', {
            'pmid':     'PMID 5',
            'title':    'Title 5'
        })

        self.post('Create new disease', '/disease/create', {
            'name':             'Disease #1',
            'chromosome_id':    1,
            'genes':            [2],
            'publications': [2,3]
            # 'publications':     [
            #     {'pmid': 'pmid123', 'title': 'Bla bla bla'},
            #     {'pmid': 'pmid456', 'title': 'Bla bla bla'}
            # ]
        })
        self.post('Create new disease (empty)', '/disease/create', {
        })
        self.post('Create new disease (empty 2)', '/disease/create', {
            'name':             '',
            'chromosome_id':    '',
            'genes':            [],
            'publications':     []
        })
        self.get('GET disease id=1', '/disease/get?id=1')
        self.get ('List all diseases', '/disease/list')
        self.post('Update disease id=1', '/disease/update', {
            'id':               1,
            'name':             'Disease #1 (updated)',
            'chromosome_id':    1,
            'genes':            [1],
            'publications': [1,2]
            # 'publications':
            # [
            #     {'pmid': 'pmid123', 'title': 'Bla bla bla (updated)'},
            #     {'pmid': 'pmid456', 'title': 'Bla bla bla (updated)'}
            # ]
        })
        self.get ('List all diseases', '/disease/list')
        self.post('Delete disease id=1', '/disease/delete', {
            'id':        1
        })
        self.get ('List all diseases', '/disease/list')
