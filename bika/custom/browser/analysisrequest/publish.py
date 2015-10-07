from bika.lims.browser.analysisrequest.publish import \
    AnalysisRequestPublishView as _AnalysisRequestPublishView
from bika.lims import bikaMessageFactory as _
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
import glob, os, sys, traceback
from datetime import date

class AnalysisRequestPublishView(_AnalysisRequestPublishView):

    def __call__(self):
        return super(AnalysisRequestPublishView, self).__call__()

    def get_PropostaComercial(self, ar):
        return ar.Schema().getField('PropostaComercial').get(ar) \
            if 'PropostaComercial' in ar.Schema() else None
    def get_Method(self,analise):
        return analise.Schema().getField('Method').get(analise) \
            if 'Method' in analise.Schema() else None
    def get_DataValidade(self, ar):
        return ar.Schema().getField('DataDeValidade').get(ar) \
            if 'DataDeValidade' in ar.Schema() else None
    def get_Coletor(self, ar):
        return ar.Schema().getField('MicrolabColetor').get(ar) \
            if 'MicrolabColetor' in ar.Schema() else None
            
    def get_date_received(self, ar):
        return ar.Schema().getField('DateReceived').get(ar).strftime('%d/%m/%Y %H:%M' ) \
            if 'DateReceived' in ar.Schema() else None
    def get_date_sampled_(self, ar):
        return ar.Schema().getField('SamplingDate').get(ar) \
            if 'SamplingDate' in ar.Schema() else None
    def get_hora_coleta(self, ar):
        return ar.Schema().getField('DataDaColeta').get(ar) \
            if 'DataDaColeta' in ar.Schema() else None
