from application.models import *

class GeneHelper(object):
    def load_exon_db(self, gene):
        result = []
        query = Exon.objects
        query = query.filter(gene=gene).order_by('start')
        if query:
            for exon in query:
                result.append(self.serialize_entry(exon))
        return result

    def serialize_entry(self, exon):
        return {
            'id':            exon.id,
            'name':    exon.name,
            'start':      exon.start,
            'end':      exon.end,
            'rank':     exon.rank,
            'num_variation': exon.num_variation
        }
