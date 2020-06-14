from django.conf import settings
from application.modules.common import page_contexts
import json
class PageStore(object):
    def __init__(self, container):
        self.container = container
    def list(self, params={}, sortkey='id', sortdir='desc', page_number=1):
        params['_page_start'] = (page_number - 1) * 10
        params['_page_num'] = 10
        params['_sort_key'] = sortkey
        params['_sort_dir'] = sortdir
        data = self.container.call_api(settings.SEQUENCE_VIEWER_API_URL + '/backup/list', GET=params)
        # print data
        return data['data']
    def create(self, data):
        return self.container.call_api(settings.SEQUENCE_VIEWER_API_URL + '/backup/create', POST=data)

class FullPageContext(page_contexts.FullPageContext):
    def __init__(self, params, container):
        super(FullPageContext, self).__init__(container.request)
        if 'page_id' in params:
            self.submenu.create_menu_group('update', 'Update', '/gene/update/%s' % (str(params['page_id'])), 'zmdi-border-all')