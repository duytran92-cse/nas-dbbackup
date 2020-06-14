from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from notasquare.urad_web import actions, page_contexts, widgets
from notasquare.urad_web_material import renderers
from application import constants
from . import components

class List(actions.crud.ListAction):
    def create_page_context(self):
        return components.FullPageContext(self.params, self.container)
    class TableRenderer(renderers.widgets.table.DataTableRenderer):
        def render_cell_actions(self, table, row):
            html  = '<div class="btn-group btn-group">'
            html += '    <a class="btn btn-xs btn-primary" href="/exon/update/%s">Edit</a>' % (row['id'])
            html += '    <a class="btn btn-xs btn-danger" href="/exon/delete/%s" onclick="return confirm(\'Are you really want to delete this?\')">Delete</a>'  % (row['id'])
            html += '</div>'
            return html
        def render_cell_is_override(self, table, row):
        	if row['is_override'] == 'true':
        		return '<span style="color:#4fb11d"> <div style="font-size:20px"><i class="zmdi zmdi-check"></i>'
        	else:
        	    return '<span style="color:red"> <div style="font-size:20px"><i class="zmdi zmdi-close"></i>'
    def create_table(self):
        table = widgets.table.DataTable()
        table.set_title('List of restore database')
        table.set_subtitle('List of restore database')
        table.create_button('create', '/restore/create', 'zmdi-plus')
        table.create_column('id', 'ID', '6%', sortable=True)
        table.create_column('code', 'CODE', '10%')
        table.create_column('name', 'DATABASE NAME', '10%')
        table.create_column('aws_bucket', 'AWS BUCKET', '10%')
        table.create_column('aws_filename', 'AWS FILENAME', '10%')
        table.create_column('time', 'TIMESTAMP', '15%')
        table.create_column('is_override', 'IS OVERRIDE', '10%')

        table.add_field(widgets.field.Textbox('name'))

        table.renderer = self.TableRenderer()
        table.renderer.table_form_renderer = renderers.widgets.form.TableFormRenderer()
        table.renderer.table_form_renderer.add_field('name', 'Name', colspan=4)

        table.renderer.table_form_renderer.set_field_renderer('textbox', renderers.widgets.field.TextboxRenderer())
        return table
    def load_table_data(self, table_form_data, sortkey, sortdir, page_number):
        return components.PageStore(self.get_container()).list(table_form_data, sortkey, sortdir, page_number)
        # print '----->'
class Create(actions.crud.CreateAction):
    def create_page_context(self):
        return components.FullPageContext(self.params, self.container)
    def create_form(self):
        form = widgets.form.Form()
        form.set_title('Restore database')
        form.add_field(widgets.field.Textbox('aws_bucket'))
        form.add_field(widgets.field.Textbox('aws_filename'))
        form.add_field(widgets.field.Textbox('database_url'))
        form.add_field(widgets.field.Textbox('database_port'))
        form.add_field(widgets.field.Textbox('database_username'))
        form.add_field(widgets.field.Textbox('database_password'))
        form.add_field(widgets.field.Textbox('database_name'))

        form.add_field(widgets.field.Checkbox('is_override'))

        form.renderer = renderers.widgets.form.HorizontalFormRenderer()
        form.renderer.add_field('aws_bucket', 'AWS BUCKET')
        form.renderer.add_field('aws_filename', 'AWS FILENAME (*without extension)')
        form.renderer.add_field('database_url', 'MYSQL URL')
        form.renderer.add_field('database_port', 'MYSQL PORT (default 3306)')
        form.renderer.add_field('database_username', 'MYSQL USERNAME')
        form.renderer.add_field('database_password', 'MYSQL PASSWORD')
        form.renderer.add_field('database_name', 'MYSQL DBNAME (*database name)')
        form.renderer.add_field('is_override', 'IS OVERRIDE (*override the existing database)')

        form.renderer.set_field_renderer('textbox', renderers.widgets.field.TextboxRenderer())
        form.renderer.set_field_renderer('checkbox', renderers.widgets.field.CheckboxRenderer())

        return form
    def load_form(self, form):
        form.set_form_data({
    })
    def process_form_data(self, data):
    	if "is_override" in self.params:
    		pass
    	else:
    		pass
        return components.PageStore(self.get_container()).create(data)
