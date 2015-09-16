from Products.CMFCore.utils import getToolByName
from bika.lims.browser.analysisrequest import AnalysisRequestWorkflowAction,\
    AnalysisRequestsView
from bika.lims import bikaMessageFactory as _b
from bika.lims.permissions import *
from bika.lims.subscribers import doActionFor, skip
from bika.lims.utils import isActive
from operator import itemgetter
from plone.app.content.browser.interfaces import IFolderContentsView
from plone.app.layout.globals.interfaces import IViewView
from zope.i18n import translate
from zope.interface import implements
import json
import plone
import logging

logger = logging.getLogger("Plone")


class AnalysisRequestsView(AnalysisRequestsView):

    def __init__(self, context, request):
        super(AnalysisRequestsView, self).__init__(context, request)
        self.columns['DataDeValidade'] = {'title': _b('Data de Validade')}
        self.columns['PrevisaoDeEntrega'] = {'title': _b('Previsao de Entrega')}
        
        for rs in self.review_states:
            i = rs['columns'].index('BatchID') + 1
            rs['columns'].insert(i, 'DataDeValidade')
            rs['columns'].insert(i, 'PrevisaoDeEntrega')

    def __call__(self):
        return super(AnalysisRequestsView, self).__call__()

