from django import template
from django.utils.safestring import mark_safe
from wiki.models import Article, ArticleRevision
from wiki.models.pluginbase import RevisionPlugin, RevisionPluginRevision
from wiki.plugins.metadata.models import MetadataRevision, deepest_instance

register = template.Library()

@register.simple_tag(takes_context=True)
def metadata_display(context, metadata):
    meta = deepest_instance(metadata)
    generic_flds = MetadataRevision._meta.get_fields()
    display = '<h4 id="metadata">Metadata</h4>\n<table class="metadata">\n'
    for fld in meta._meta.get_fields(include_hidden=False):
        if fld not in generic_flds and not fld.name.endswith('_ptr'):
            display += f'    <tr><th style="padding: 10px;">{fld.name}</th><td>'
            v = getattr(meta, fld.name)
            if hasattr(v, 'html'):
                display += v.html()
            else:
                display += str(v)
            display += '</td></tr>\n'
    display += '</table>'
    display += str(meta) + '; ' + str(metadata)
    return mark_safe(display)