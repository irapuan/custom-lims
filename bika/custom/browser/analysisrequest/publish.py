from bika.lims.browser.analysisrequest.publish import \
    AnalysisRequestPublishView as _AnalysisRequestPublishView
from bika.lims import bikaMessageFactory as _
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
import glob, os, sys, traceback

class AnalysisRequestPublishView(_AnalysisRequestPublishView):

    def __call__(self):
        return super(AnalysisRequestPublishView, self).__call__()

    def get_PropostaComercial(self, ar):
        return ar.Schema().getField('PropostaComercial').get(ar) \
            if 'PropostaComercial' in ar.Schema() else None
    def get_Method(self,analise):
        return analise.Schema().getField('Method').get(analise) \
            if 'Method' in analise.Schema() else None