from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from notasquare.urad_web import actions, page_contexts, widgets
from notasquare.urad_web_material import renderers
from application import constants
from . import components
import os, sys, time, boto, boto3
from django.conf import settings

class List(actions.crud.ListAction):
    def create_page_context(self):
        return components.FullPageContext(self.params, self.container)
    class TableRenderer(renderers.widgets.table.DataTableRenderer):
        def render_cell_actions(self, table, row):
            html  = '<div class="btn-group btn-group">'
            # html += '    <a class="btn btn-xs btn-primary" href="/gene/update/%s">Edit</a>' % (row['id'])
            # html += '    <a class="btn btn-xs btn-danger" href="/backup/delete/%s" onclick="return confirm(\'Are you really want to delete this?\')">Delete</a>'  % (row['id'])
            html += '</div>'
            return html
    def create_table(self):
        table = widgets.table.DataTable()
        table.set_title('List of backup database')
        table.set_subtitle('List of backup database')
        table.create_button('create', '/backup/create', 'zmdi-plus')
        table.create_column('id', 'ID', '7%', sortable=True)
        table.create_column('code', 'CODE', '15%')
        table.create_column('name', 'NAME', '10%')
        table.create_column('url', 'URL', '15%')
        table.create_column('time', 'TIMESTAMP', '15%')
        table.create_column('aws_bucket', 'AWS BUCKET', '15%')
        table.create_column('aws_filename', 'AWS FILENAME', '15%')
        table.create_column('actions', '', '14%')
        table.add_field(widgets.field.Textbox('name'))
        table.renderer = self.TableRenderer()
        table.renderer.table_form_renderer = renderers.widgets.form.TableFormRenderer()
        table.renderer.table_form_renderer.add_field('name', 'Name', colspan=8)
        table.renderer.table_form_renderer.set_field_renderer('textbox', renderers.widgets.field.TextboxRenderer())
        # table.renderer.table_form_renderer.set_field_renderer('combobox', renderers.widgets.field.ComboboxRenderer())
        return table
    def load_table_data(self, table_form_data, sortkey, sortdir, page_number):
        return components.PageStore(self.get_container()).list(table_form_data, sortkey, sortdir, page_number)

class Create(actions.crud.CreateAction):
    def create_page_context(self):
        return components.FullPageContext(self.params, self.container)
    def create_form(self):
        form = widgets.form.Form()
        form.set_title('Backup database')
        form.add_field(widgets.field.Textbox('aws_bucket'))
        form.add_field(widgets.field.Textbox('database_url'))
        form.add_field(widgets.field.Textbox('database_port'))
        form.add_field(widgets.field.Textbox('database_username'))
        form.add_field(widgets.field.Textbox('database_password'))
        form.add_field(widgets.field.Textbox('database_name'))
        form.add_field(widgets.field.Textbox('aws_filename'))

        form.renderer = renderers.widgets.form.HorizontalFormRenderer()

        form.renderer.add_field('aws_bucket', 'AWS BUCKET')
        form.renderer.add_field('database_url', 'DATABASE URL')
        form.renderer.add_field('database_port', 'DATABASE PORT (default 3306)')
        form.renderer.add_field('database_username', 'DATABASE USERNAME')
        form.renderer.add_field('database_password', 'DATABASE PASSWORD')
        form.renderer.add_field('database_name', 'DATABASE NAME')
        form.renderer.add_field('aws_filename', 'AWS FILENAME (* the name that you want to save)')
        

        form.renderer.set_field_renderer('textbox', renderers.widgets.field.TextboxRenderer())

        return form
    def load_form(self, form):
        form.set_form_data({
    })

    def process_form_data(self, data):
        return components.PageStore(self.get_container()).create(data)
