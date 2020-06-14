import urllib
from django.conf import settings
from notasquare.urad_web.page_contexts import standard
from notasquare.urad_web_material import renderers
from application.modules.user.manager import UserManager


class FullPageContext(standard.FullPageContext):
    def __init__(self,request):
        super(FullPageContext, self).__init__()
        self.app_title = 'Backup database tools'
        self.page_title = 'Backup database tools - Admin Panel'
        self.breadcrumb.add_entry('home', 'Dashboard', '/')

        #self.menu.create_menu_group('bucket', 'Bucket', '/bucket/list', 'zmdi-format-subject')
        self.menu.create_menu_group('backup', 'Backup', '/backup/list', 'zmdi-format-subject')
        self.menu.create_menu_group('restore', 'Restore', '/restore/list', 'zmdi-format-subject')
        self.renderer = renderers.page_contexts.FullPageContextRenderer()


        # User
        # self.user = request.META['USER']
        # self.user['logout_link'] = settings.SECURITY_SERVER_URL + '/user/logout?redirect=%s' % (settings.APPLICATION_URL)
