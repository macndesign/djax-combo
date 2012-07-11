# API JSON
from django.http import HttpResponse
from django.utils import simplejson
from django.views.generic.detail import BaseDetailView
from django.views.generic.list import BaseListView
from django.db.models.query import QuerySet

class JSONResponseMixin(object):
    def render_to_response(self, context):
        return self.get_json_response(self.convert_context_to_json(context))

    def get_json_response(self, content, **httpresponse_kwargs):
        return HttpResponse(content, content_type='application/json', **httpresponse_kwargs)

    def convert_context_to_json(self, context):
        return simplejson.dumps(context)


class JSONDetailView(JSONResponseMixin, BaseDetailView):
    def render_to_response(self, context):
        obj = context['object'].as_dict()
        return JSONResponseMixin.render_to_response(self, obj)


class JSONListView(JSONResponseMixin, BaseListView):
    def render_to_response(self, context):
        obj_list = list(self.model.objects.values())
        return JSONResponseMixin.render_to_response(self, obj_list)
