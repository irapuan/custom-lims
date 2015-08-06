from archetypes.schemaextender.interfaces import IOrderableSchemaExtender
from archetypes.schemaextender.interfaces import ISchemaModifier
from bika.lims import bikaMessageFactory as _
from bika.lims.browser.widgets import DateTimeWidget as bika_DateTimeWidget
from bika.lims.browser.widgets import DecimalWidget as bikaDecimalWidget
from Products.ATExtensions.ateapi import DateTimeField, DateTimeWidget
from bika.lims.fields import *
from bika.lims.interfaces import IAnalysisRequest
from Products.Archetypes.public import *
from Products.Archetypes import public as atapi
from zope.component import adapts
from zope.interface import implements

from archetypes.schemaextender.field import ExtensionField
from archetypes.schemaextender.interfaces import (
          ISchemaExtender, IOrderableSchemaExtender, IBrowserLayerAwareExtender)
#from bika.lims.browser.fields import bika_DateTimeField

'''
DataEntrega = ExtStringField(
    'DataEntrega',
    required=False,
    schemata = "Work Order Instructions",
    acquire=True,
    widget=StringWidget(
        label=_('Campo de teste'),
        visible={'view': 'visible',
                 'edit': 'visible',
                 'add' : 'edit'}
    ),
)
'''

class ExtensionDateField(ExtensionField, atapi.DateTimeField):
            """ Retrofitted date field """
class ExtStringField(ExtensionField, StringField):
            """A string field."""

class AnalysisRequestSchemaExtender(object):
    adapts(IAnalysisRequest)
    implements(IOrderableSchemaExtender)

    fields = [
        ExtensionDateField(
            'PrevisaoDeEntrega',
            schemata = 'Dates',
            widget=bika_DateTimeWidget(
                label='Previsao de entrega',
                size=20,
                render_own_label=False,
                visible={'edit': 'visible',
                         'view': 'visible',
                         'add': 'edit',
                         'header_table': 'visible',
                         'sample_registered': {'view': 'visible', 'edit': 'visible', 'add': 'edit'},
                         'to_be_sampled':     {'view': 'visible', 'edit': 'visible'},
                         'sampled':           {'view': 'visible', 'edit': 'visible'},
                         'to_be_preserved':   {'view': 'visible', 'edit': 'visible'},
                         'sample_due':        {'view': 'visible', 'edit': 'visible'},
                         'sample_received':   {'view': 'visible', 'edit': 'visible'},
                         'attachment_due':    {'view': 'visible', 'edit': 'visible'},
                         'to_be_verified':    {'view': 'visible', 'edit': 'visible'},
                         'verified':          {'view': 'visible', 'edit': 'visible'},
                         'published':         {'view': 'visible', 'edit': 'visible'},
                         'invalid':           {'view': 'visible', 'edit': 'visible'},
                         },
            ),
        ),
        BooleanField(
            'ColetaRealizadaMicrolab',
            default=True,
            mode="rw",
            widget=BooleanWidget(
                label = _("Coleta Realizada pela Microlab"),
                render_own_label=False,
                visible={'edit': 'visible',
                         'view': 'visible',
                         'add': 'edit',
                         'header_table': 'visible',
                         'sample_registered': {'view': 'visible', 'edit': 'visible', 'add': 'edit'},
                         'to_be_sampled':     {'view': 'visible', 'edit': 'visible'},
                         'sampled':           {'view': 'visible', 'edit': 'visible'},
                         'to_be_preserved':   {'view': 'visible', 'edit': 'visible'},
                         'sample_due':        {'view': 'visible', 'edit': 'visible'},
                         'sample_received':   {'view': 'visible', 'edit': 'visible'},
                         'attachment_due':    {'view': 'visible', 'edit': 'visible'},
                         'to_be_verified':    {'view': 'visible', 'edit': 'visible'},
                         'verified':          {'view': 'visible', 'edit': 'visible'},
                         'published':         {'view': 'visible', 'edit': 'invisible'},
                         'invalid':           {'view': 'visible', 'edit': 'invisible'},
                         },
            ),
        ),
        ExtStringField('PropostaComercial',
            required = 0,
            widget = atapi.StringWidget(
                label = _(u"Proposta Comercial"),
                visible={'edit': 'visible',
                         'view': 'visible',
                         'add': 'edit',
                         'header_table': 'visible',
                         'sample_registered': {'view': 'visible', 'edit': 'visible', 'add': 'edit'},
                         'to_be_sampled':     {'view': 'visible', 'edit': 'visible'},
                         'sampled':           {'view': 'visible', 'edit': 'visible'},
                         'to_be_preserved':   {'view': 'visible', 'edit': 'visible'},
                         'sample_due':        {'view': 'visible', 'edit': 'visible'},
                         'sample_received':   {'view': 'visible', 'edit': 'visible'},
                         'attachment_due':    {'view': 'visible', 'edit': 'visible'},
                         'to_be_verified':    {'view': 'visible', 'edit': 'visible'},
                         'verified':          {'view': 'visible', 'edit': 'visible'},
                         'published':         {'view': 'visible', 'edit': 'invisible'},
                         'invalid':           {'view': 'visible', 'edit': 'invisible'},
                         },
            ),
        ),
        ExtensionDateField(
            'DataDeFabricacao',
            schemata = 'Dates',
            widget=bika_DateTimeWidget(
                label='Data de Fabricacao',
                size=20,
                render_own_label=False,
                visible={'edit': 'visible',
                         'view': 'visible',
                         'add': 'edit',
                         'header_table': 'visible',
                         'sample_registered': {'view': 'visible', 'edit': 'visible', 'add': 'edit'},
                         'to_be_sampled':     {'view': 'visible', 'edit': 'visible'},
                         'sampled':           {'view': 'visible', 'edit': 'visible'},
                         'to_be_preserved':   {'view': 'visible', 'edit': 'visible'},
                         'sample_due':        {'view': 'visible', 'edit': 'visible'},
                         'sample_received':   {'view': 'visible', 'edit': 'visible'},
                         'attachment_due':    {'view': 'visible', 'edit': 'visible'},
                         'to_be_verified':    {'view': 'visible', 'edit': 'visible'},
                         'verified':          {'view': 'visible', 'edit': 'visible'},
                         'published':         {'view': 'visible', 'edit': 'invisible'},
                         'invalid':           {'view': 'visible', 'edit': 'invisible'},
                         },
            ),
        ),
        ExtensionDateField(
            'DataDeValidade',
            schemata = 'Dates',
            widget=bika_DateTimeWidget(
                label='Data de Validade',
                size=20,
                render_own_label=False,
                visible={'edit': 'visible',
                         'view': 'visible',
                         'add': 'edit',
                         'header_table': 'visible',
                         'sample_registered': {'view': 'visible', 'edit': 'visible', 'add': 'edit'},
                         'to_be_sampled':     {'view': 'visible', 'edit': 'visible'},
                         'sampled':           {'view': 'visible', 'edit': 'visible'},
                         'to_be_preserved':   {'view': 'visible', 'edit': 'visible'},
                         'sample_due':        {'view': 'visible', 'edit': 'visible'},
                         'sample_received':   {'view': 'visible', 'edit': 'visible'},
                         'attachment_due':    {'view': 'visible', 'edit': 'visible'},
                         'to_be_verified':    {'view': 'visible', 'edit': 'visible'},
                         'verified':          {'view': 'visible', 'edit': 'visible'},
                         'published':         {'view': 'visible', 'edit': 'invisible'},
                         'invalid':           {'view': 'visible', 'edit': 'invisible'},
                         },
            ),
        ),
    ]

    def __init__(self, context):
        self.context = context

    def getOrder(self, schematas):
        return schematas

    def getFields(self):
        return self.fields

class AnalysisRequestSchemaModifier(object):
    adapts(IAnalysisRequest)
    implements(ISchemaModifier)

    def __init__(self, context):
        self.context = context

    def fiddle(self, schema):
        return schema
