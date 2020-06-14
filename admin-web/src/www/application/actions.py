from notasquare.urad_web import actions
from django.http import HttpResponseRedirect
class Home(actions.BaseAction):
    def GET(self):
        return HttpResponseRedirect('/bucket/list')
