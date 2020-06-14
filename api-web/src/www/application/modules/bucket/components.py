from application.models import *

class SentenceHelper(object):
    def load_variation_db(self, start, end):
        result = []
        query = Variation.objects
        query = query.filter(position__gte=start,position__lte=end)
        if query:
            for variation in query:
                result.append(self.serialize_entry(variation))
        return result

    def serialize_entry(self, variation):
        return {
            'id':            variation.id,
            'chromosome':    variation.chromosome,
            'position':      variation.position,
            'rsnumber':      variation.rsnumber,
            'gene':          variation.gene,
            'associated_disease': variation.associated_disease
        }