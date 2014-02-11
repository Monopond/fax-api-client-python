
from suds.client import Client
from suds.bindings import binding
from suds.sax.element import Element, Attribute
import base64
import os
from pymonopond.monopond_python_client import *


class MappingUtils(object):
    '''
        Abstract class that contains mapping methods.
    '''
    def __init__(self, client):
        self._client = client

    def mapApiResponseToResponse(self, apiResponse):
        response = Response()
        statusTotals = FaxStatusTotals()
        if hasattr(apiResponse, 'FaxStatusTotals'):
            if hasattr(apiResponse.FaxStatusTotals, '_pending'):
                statusTotals.pendingTotal = apiResponse.FaxStatusTotals._pending
            if hasattr(apiResponse.FaxStatusTotals, '_processing'):
                statusTotals.processingTotal = apiResponse.FaxStatusTotals._processing
            if hasattr(apiResponse.FaxStatusTotals, '_queued'):
                statusTotals.queuedTotal = apiResponse.FaxStatusTotals._queued
            if hasattr(apiResponse.FaxStatusTotals, '_starting'):
                statusTotals.startingTotal = apiResponse.FaxStatusTotals._starting
            if hasattr(apiResponse.FaxStatusTotals, '_sending'):
                statusTotals.sendingTotal = apiResponse.FaxStatusTotals._sending
            if hasattr(apiResponse.FaxStatusTotals, '_finalizing'):
                statusTotals.finalizingTotal = apiResponse.FaxStatusTotals._finalizing
            if hasattr(apiResponse.FaxStatusTotals, '_done'):
                statusTotals.doneTotal = apiResponse.FaxStatusTotals._done

        resultsTotals = FaxResultsTotals()
        if hasattr(apiResponse, 'FaxResultsTotals'):
            if hasattr(apiResponse.FaxResultsTotals, '_success'):
                resultsTotals.successTotal = apiResponse.FaxResultsTotals._success
            if hasattr(apiResponse.FaxResultsTotals, '_blocked'):
                resultsTotals.blockedTotal = apiResponse.FaxResultsTotals._blocked
            if hasattr(apiResponse.FaxResultsTotals, '_failed'):
                resultsTotals.failedTotal = apiResponse.FaxResultsTotals._failed
            if hasattr(apiResponse.FaxResultsTotals, '_totalAttempts'):
                resultsTotals.totalAttempts = apiResponse.FaxResultsTotals._totalAttempts
            if hasattr(apiResponse.FaxResultsTotals, '_totalFaxDuration'):
                resultsTotals.totalFaxDuration = apiResponse.FaxResultsTotals._totalFaxDuration
            if hasattr(apiResponse.FaxResultsTotals, '_totalPages'):
                resultsTotals.totalPages = apiResponse.FaxResultsTotals._totalPages

        response.faxResultTotals = resultsTotals
        response.faxStatusTotals = statusTotals
        if hasattr(apiResponse, 'FaxMessages'):
            if hasattr(apiResponse.FaxMessages, 'FaxMessage'):
                for faxMessage in apiResponse.FaxMessages.FaxMessage:
                    response.addFaxMessageStatusResults(self.mapApiFaxMessageStatusToFaxMessageStatusResults(faxMessage))
        return response

    def mapApiFaxMessageStatusToFaxMessageStatusResults(self, faxMessage):
        faxMessageStatusResults = FaxMessageStatusResults()
        if hasattr(faxMessage, '_messageRef'):
            faxMessageStatusResults.messageRef = faxMessage._messageRef
        if hasattr(faxMessage, '_sendRef'):
            faxMessageStatusResults.sendRef = faxMessage._sendRef
        if hasattr(faxMessage, '_broadcastRef'):
            faxMessageStatusResults.broadcastRef = faxMessage._broadcastRef
        if hasattr(faxMessage, '_sendTo'):
            faxMessageStatusResults.sendTo = faxMessage._sendTo
        if hasattr(faxMessage, '_status'):
            faxMessageStatusResults.status = faxMessage._status
        if hasattr(faxMessage, 'FaxDetails'):
            if hasattr(faxMessage.FaxDetails, '_sendFrom'):
                faxMessageStatusResults.sendFrom = faxMessage.FaxDetails._sendFrom
            if hasattr(faxMessage.FaxDetails, '_resolution'):
                faxMessageStatusResults.resolution = faxMessage.FaxDetails._resolution
            if hasattr(faxMessage.FaxDetails, '_retries'):
                faxMessageStatusResults.retries = faxMessage.FaxDetails._retries
            if hasattr(faxMessage.FaxDetails, '_busyRetries'):
                faxMessageStatusResults.busyRetries = faxMessage.FaxDetails._busyRetries
            if hasattr(faxMessage.FaxDetails, '_headerFormat'):
                faxMessageStatusResults.headerFormat = faxMessage.FaxDetails._headerFormat

        if hasattr(faxMessage, 'FaxResults'):
            if hasattr(faxMessage.FaxResults, 'FaxResult'):
                for faxResult in faxMessage.FaxResults.FaxResult:
                    if hasattr(faxResult, '_attempt'):
                        faxMessageStatusResults.attempt = faxResult._attempt
                    if hasattr(faxResult, '_dateCallStarted'):
                        faxMessageStatusResults.dateCallStarted = faxResult._dateCallStarted
                    if hasattr(faxResult, '_dateCallEnded'):
                        faxMessageStatusResults.dateCallEnded = faxResult._dateCallEnded
                    if hasattr(faxResult, '_scheduledStartTime'):
                        faxMessageStatusResults.scheduledStartTime = faxResult._scheduledStartTime
                    if hasattr(faxResult, '_cost'):
                        faxMessageStatusResults.cost = faxResult._cost
                    if hasattr(faxResult, '_result'):
                        faxMessageStatusResults.result = faxResult._result
                    if hasattr(faxResult, '_pages'):
                        faxMessageStatusResults.pages = faxResult._pages
                    if hasattr(faxResult, '_totalFaxDuration'):
                        faxMessageStatusResults.totalFaxDuration = faxResult._totalFaxDuration
                    if hasattr(faxResult, 'Error'):
                        if hasattr(faxResult.Error, '_code'):
                            faxMessageStatusResults.errorCode = faxResult.Error._code
                        if hasattr(faxResult.Error, '_name'):
                            faxMessageStatusResults.errorName = faxResult.Error._name
        return faxMessageStatusResults


    def mapBlocklistsToApiFaxMessageBlocklist(self, blocklists):
        apiFaxMessageBlocklist = self._client.factory.create("apiFaxMessageBlocklist")
        apiFaxMessageBlocklist._dncr = blocklists.dncr
        apiFaxMessageBlocklist._fps = blocklists.fps
        apiFaxMessageBlocklist._smartblock = blocklists.smartblock
        return apiFaxMessageBlocklist

    def mapFaxMessageToApiFaxMessage(self, faxMessage, apiFaxMessage):
        apiFaxMessage.MessageRef = faxMessage.messageRef
        apiFaxMessage.SendTo = faxMessage.sendTo
        apiFaxMessage.SendFrom = faxMessage.sendFrom
        if faxMessage.documents is not None:
            apiFaxMessage.Documents = self.mapDocumentListToApiFaxDocumentList(faxMessage.documents)
        apiFaxMessage.Resolution = faxMessage.resolution
        #if faxMessage.blocklist is not None:
        #apiFaxMessage.Blocklists = self.mapBlocklistsToApiFaxMessageBlocklist(faxMessage.blocklist)
        apiFaxMessage.ScheduledStartTime = faxMessage.scheduledStartTime
        apiFaxMessage.Retries = faxMessage.retries
        apiFaxMessage.BusyRetries = faxMessage.busyRetries
        apiFaxMessage.HeaderFormat = faxMessage.headerFormat

    def mapFaxMessageListToApiFaxMessageList(self, faxMessageList):
        apiFaxMessageList = []
        for faxMessage in faxMessageList:
            apiFaxMessage = self._client.factory.create("apiFaxMessage")
            self.mapFaxMessageToApiFaxMessage(faxMessage, apiFaxMessage)
            apiFaxMessageList.append(apiFaxMessage)
        apiFaxMessageList = {'FaxMessage':apiFaxMessageList}
        return apiFaxMessageList

    def mapDocumentToApiFaxDocument(self, document, apiFaxDocument):
        apiFaxDocument.FileName = document.fileName
        apiFaxDocument.FileData = document.fileData
        apiFaxDocument.Order = document.order

    def mapDocumentListToApiFaxDocumentList(self, documentList):
        apiFaxDocumentList = []
        for document in documentList:
            apiFaxDocument = self._client.factory.create("apiFaxDocument")
            self.mapDocumentToApiFaxDocument(document, apiFaxDocument)
            apiFaxDocumentList.append(apiFaxDocument)
        apiFaxDocumentList = {'Document':apiFaxDocumentList}
        return apiFaxDocumentList

    def mapDocMergeFieldListToApiFaxDocumentDocMergeFieldList(self, docMergeFieldList):
        apiFaxDocumentDocMergeFieldList = []
        for docMergeField in docMergeFieldList:
            apiFaxDocumentDocMergeField = self._client.factory.create("apiFaxDocumentDocMergeField")
            apiFaxDocumentDocMergeField.Key =  docMergeField.key
            apiFaxDocumentDocMergeField.Value = docMergeField.value
            apiFaxDocumentDocMergeFieldList.append(apiFaxDocumentDocMergeField)
        apiFaxDocumentDocMergeFieldList = {'MergeField':apiFaxDocumentDocMergeFieldList}
        return apiFaxDocumentDocMergeFieldList

    def mapStampMergeFieldListToApiFaxDocumentStampMergeFieldList(self, stampMergeFieldList):
        apiFaxDocumentDocMergeFieldList = []
        for stampMergeField in stampMergeFieldList:
            apiFaxDocumentStampMergeField = self._client.factory.create("apiFaxDocumentStampMergeField")
            apiFaxDocumentStampMergeFieldKey = self._client.factory.create("apiFaxDocumentStampMergeFieldKey")
            apiFaxDocumentStampMergeFieldKey._xCoord = stampMergeField.keyXCoord
            apiFaxDocumentStampMergeFieldKey._yCoord = stampMergeField.keyYCoord
            apiFaxDocumentStampMergeField.Key = apiFaxDocumentStampMergeFieldKey
            if isinstance(stampMergeField, TextStampMergeData) is True:
                apiFaxDocumentStampMergeFieldTextValue = self._client.factory.create("apiFaxDocumentStampMergeFieldTextValue")
                apiFaxDocumentStampMergeFieldTextValue.value = stampMergeField.textValue
                apiFaxDocumentStampMergeFieldTextValue._fontName = stampMergeField.fontName
                apiFaxDocumentStampMergeFieldTextValue._fontSize = stampMergeField.fontSize
                apiFaxDocumentStampMergeField.TextValue = apiFaxDocumentStampMergeFieldTextValue
            elif isinstance(stampMergeField, ImageStampMergeData) is True:
                apiFaxDocumentStampMergeFieldImageValue = self._client.factory.create("apiFaxDocumentStampMergeFieldImageValue")
                apiFaxDocumentStampMergeFieldImageValue.FileName = stampMergeField.fileName
                apiFaxDocumentStampMergeFieldImageValue.FileData = stampMergeField.fileData
                apiFaxDocumentStampMergeFieldImageValue._width = stampMergeField.width
                apiFaxDocumentStampMergeFieldImageValue._height = stampMergeField.height
                apiFaxDocumentStampMergeField.ImageValue = apiFaxDocumentStampMergeFieldImageValue
            apiFaxDocumentDocMergeFieldList.append(apiFaxDocumentStampMergeField)

        '''for imageStampMergeField in imageStampMergeFieldList:
            apiFaxDocumentStampMergeField = self._client.factory.create("apiFaxDocumentStampMergeField")
            apiFaxDocumentStampMergeFieldKey = self._client.factory.create("apiFaxDocumentStampMergeFieldKey")
            apiFaxDocumentStampMergeFieldKey.xCoord = textStampMergeField.keyXCoord
            apiFaxDocumentStampMergeFieldKey.yCoord = textStampMergeField.keyYCoord
            apiFaxDocumentStampMergeField.Key = apiFaxDocumentStampMergeFieldKey
            apiFaxDocumentStampMergeFieldImageValue = self._client.factory.create("apiFaxDocumentStampMergeFieldImageValue")
            apiFaxDocumentStampMergeFieldImageValue.FileName = imageStampMergeField.fileName
            apiFaxDocumentStampMergeFieldImageValue.FileData = imageStampMergeField.fileData
            apiFaxDocumentStampMergeFieldImageValue.width = imageStampMergeField.width
            apiFaxDocumentStampMergeFieldImageValue.height = imageStampMergeField.height
            apiFaxDocumentStampMergeField.ImageValue = apiFaxDocumentStampMergeFieldImageValue
            apiFaxDocumentDocMergeFieldList.append(apiFaxDocumentStampMergeField)'''

        apiFaxDocumentDocMergeFieldList = {'MergeField':apiFaxDocumentDocMergeFieldList}
        return apiFaxDocumentDocMergeFieldList

class ClientWrapper(object):
    """
    A custom wrapper of suds web service client for the monopond fax web services.
    Extends mapping utils to handle mapping of api objects to client objects.
    @ivar _client: suds client.
    @type _client:L{Client}
    """
    def __init__(self, url, username, password):
        self._client = Client(url)
        wsse_ns = ("wsse", "http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd")
        mustAttribute = Attribute('SOAP-ENV:mustUnderstand', '1')
        security_header = Element("Security", ns=wsse_ns).append(mustAttribute)

        message_header = Element("UsernameToken", ns=wsse_ns)
        message_header.insert(Element("Username", ns=wsse_ns).setText(username))
        message_header.insert(Element("Password", ns=wsse_ns).setText(password))
        security_header.insert(message_header)
        self._client.set_options(soapheaders = security_header)

        self.mappingUtils = MappingUtils(self._client)

    def sendFax(self, request):
        if isinstance(request, SendFaxRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        apiFaxDocuments = self.mappingUtils.mapDocumentListToApiFaxDocumentList(request.documents)
        apiFaxMessages = self.mappingUtils.mapFaxMessageListToApiFaxMessageList(request.faxMessages)
        apiFaxMessageBlocklist = None
        #if request.blocklists is not None:
        #apiFaxMessageBlocklist = self.mappingUtils.mapBlocklistsToApiFaxMessageBlocklist(request.blocklists)
        result = self._client.service.SendFax(BroadcastRef=request.broadcastRef, SendRef=request.sendRef,
                                              FaxMessages= apiFaxMessages, Documents=apiFaxDocuments, Resolution=request.resolution,
                                              Blocklists = apiFaxMessageBlocklist, Retries=request.retries, HeaderFormat=request.headerFormat)
        wrappedResult = self.mappingUtils.mapApiResponseToResponse(result)
        return wrappedResult

    def faxStatus(self, request):
        if isinstance(request, FaxStatusRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        result = self._client.service.FaxStatus(MessageRef=request.messageRef, SendRef=request.sendRef,
                                                BroadcastRef=request.broadcastRef, Verbosity=request.verbosity)
        wrappedResult = self.mappingUtils.mapApiResponseToResponse(result)
        return wrappedResult

    def pauseFax(self, request):
        if isinstance(request, PauseFaxRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        result = self._client.service.PauseFax(MessageRef=request.messageRef, SendRef=request.sendRef,
                                               BroadcastRef=request.broadcastRef)
        wrappedResult = self.mappingUtils.mapApiResponseToResponse(result)
        return wrappedResult

    def resumeFax(self, request):
        if isinstance(request, ResumeFaxRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        result = self._client.service.ResumeFax(MessageRef=request.messageRef, SendRef=request.sendRef,
                                                BroadcastRef=request.broadcastRef)
        wrappedResult = self.mappingUtils.mapApiResponseToResponse(result)
        return wrappedResult

    def stopFax(self, request):
        if isinstance(request, StopFaxRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        result = self._client.service.StopFax(MessageRef=request.messageRef, SendRef=request.sendRef,
                                              BroadcastRef=request.broadcastRef)
        wrappedResult = self.mappingUtils.mapApiResponseToResponse(result)
        print result
        return wrappedResult

    def deleteFaxDocument(self, request):
        if isinstance(request, DeleteFaxDocumentRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        result = self._client.service.DeleteFaxDocument(DocumentRef=request.documentRef)
        wrappedResult = self.mappingUtils.mapApiResponseToResponse(result)
        print result
        return wrappedResult

    def faxDocumentPreview(self, request):
        if isinstance(request, FaxDocumentPreviewRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        apiFaxDocumentDocMergeFieldList = self.mappingUtils.mapDocMergeFieldListToApiFaxDocumentDocMergeFieldList(request.docMergeData)
        apiFaxDocumentStampMergeFieldList = self.mappingUtils.mapStampMergeFieldListToApiFaxDocumentStampMergeFieldList(request.stampMergeData)
        print apiFaxDocumentDocMergeFieldList
        print "-------"
        print apiFaxDocumentStampMergeFieldList
        result = self._client.service.FaxDocumentPreview(DocumentRef=request.documentRef, Resolution=request.resolution,
                                                         DitheringTechnique=request.ditheringTechnique, DocMergeData=apiFaxDocumentDocMergeFieldList,
                                                         StampMergeData=apiFaxDocumentStampMergeFieldList)
        print self._client.last_sent()
        #wrappedResult = self.mappingUtils.mapApiResponseToResponse(result)
        #print result
        #TODO add the mapping method here
        #return wrappedResult

    def getTypeInstance(self, typeName):
        return self._client.factory.create(typeName)

    def __str__(self):
        return self._client.__str__()


class SendFaxRequest(object):
    '''
        send fax request client object
    '''
    def __init__(self):
        self._broadcastRef = None
        self._sendRef = None
        self._resolution = None
        self._faxMessages = []
        self._documents = []
        self._blocklists = None
        self._sendFrom = None
        self._scheduledStartTime = None
        self._retries = None
        self._busyRetries = None
        self._headerFormat = None

    @property
    def broadcastRef(self):
        return self._broadcastRef
    @broadcastRef.setter
    def broadcastRef(self, broadcastRef=None):
        self._broadcastRef = broadcastRef

    @property
    def sendRef(self):
        return self._sendRef
    @sendRef.setter
    def sendRef(self, sendRef=None):
        self._sendRef = sendRef

    @property
    def resolution(self):
        return self._resolution
    @resolution.setter
    def resolution(self, resolution=None):
        self._resolution = resolution

    @property
    def faxMessages(self):
        return self._faxMessages
    def addFaxMessage(self, faxMessage=None):
        self._faxMessages.append(faxMessage)

    @property
    def documents(self):
        return self._documents
    def addDocument(self, document=None):
        self._documents.append(document)

        #blocklist will not be used in soap v2.0
        #@property
        #def blocklists(self):
        #return self._blocklists
        #@blocklists.setter
        #def blocklists(self, blocklists=None):
        #self._blocklists = blocklists

    @property
    def sendFrom(self):
        return self._sendFrom
    @sendFrom.setter
    def sendFrom(self, sendFrom=None):
        self._sendFrom = sendFrom

    @property
    def scheduledStartTime(self):
        return self._scheduledStartTime
    @scheduledStartTime.setter
    def scheduledStartTime(self, scheduledStartTime=None):
        self._scheduledStartTime = scheduledStartTime

    @property
    def retries(self):
        return self._retries
    @retries.setter
    def retries(self, retries=None):
        self._retries = retries

    @property
    def busyRetries(self):
        return self._busyRetries
    @busyRetries.setter
    def busyRetries(self, busyRetries=None):
        self._busyRetries = busyRetries

    @property
    def headerFormat(self):
        return self._headerFormat
    @headerFormat.setter
    def headerFormat(self, headerFormat=None):
        self._headerFormat = headerFormat

    def __str__(self):
        return ("broadcastRef=%s, sendRef=%s, resolution=%s,  sendFrom=%s, scheduledStartTime=%s, retries=%s, busyRetries=%s, headerFormat=%s, faxMessages=%s, documents=%s"
                %(self.broadcastRef, self.sendRef, self.resolution, self.sendFrom, self.scheduledStartTime, self.retries, self.busyRetries, self.headerFormat, self.faxMessages, self.documents))

class FaxStatusRequest(object):
    '''
        fax status request client object
    '''
    def __init__(self):
        self._messageRef = None
        self._sendRef = None
        self._broadcastRef = None
        self._verbosity = None

    @property
    def messageRef(self):
        return self._messageRef
    @messageRef.setter
    def messageRef(self, messageRef=None):
        self._messageRef = messageRef

    @property
    def sendRef(self):
        return self._sendRef
    @sendRef.setter
    def sendRef(self, sendRef=None):
        self._sendRef = sendRef

    @property
    def broadcastRef(self):
        return self._broadcastRef
    @broadcastRef.setter
    def broadcastRef(self, broadcastRef=None):
        self._broadcastRef = broadcastRef

    @property
    def verbosity(self):
        return self._verbosity
    @verbosity.setter
    def verbosity(self, verbosity=None):
        self._verbosity = verbosity

    def __str__(self):
        return ("messageRef=%s, sendRef=%s, broadcastRef=%s, verbosity=%s" %(self.messageRef, self.sendRef, self.broadcastRef, self.verbosity))

class PauseFaxRequest(object):
    '''
        pause fax request client object
    '''
    def __init__(self):
        self._messageRef = None
        self._sendRef = None
        self._broadcastRef = None

    @property
    def messageRef(self):
        return self._messageRef
    @messageRef.setter
    def messageRef(self, messageRef=None):
        self._messageRef = messageRef

    @property
    def sendRef(self):
        return self._sendRef
    @sendRef.setter
    def sendRef(self, sendRef=None):
        self._sendRef = sendRef

    @property
    def broadcastRef(self):
        return self._broadcastRef
    @broadcastRef.setter
    def broadcastRef(self, broadcastRef=None):
        self._broadcastRef = broadcastRef

    def __str__(self):
        return ("messageRef=%s, sendRef=%s, broadcastRef=%s" %(self.messageRef, self.sendRef, self.broadcastRef))


class ResumeFaxRequest(object):
    '''
        resume fax request client object
    '''
    def __init__(self):
        self._messageRef = None
        self._sendRef = None
        self._broadcastRef = None

    @property
    def messageRef(self):
        return self._messageRef
    @messageRef.setter
    def messageRef(self, messageRef=None):
        self._messageRef = messageRef

    @property
    def sendRef(self):
        return self._sendRef
    @sendRef.setter
    def sendRef(self, sendRef=None):
        self._sendRef = sendRef

    @property
    def broadcastRef(self):
        return self._broadcastRef
    @broadcastRef.setter
    def broadcastRef(self, broadcastRef=None):
        self._broadcastRef = broadcastRef


    def __str__(self):
        return ("messageRef=%s, sendRef=%s, broadcastRef=%s" %(self.messageRef, self.sendRef, self.broadcastRef))

class StopFaxRequest(object):
    '''
        stop fax request client object
    '''
    def __init__(self):
        self._messageRef = None
        self._sendRef = None
        self._broadcastRef = None

    @property
    def messageRef(self):
        return self._messageRef
    @messageRef.setter
    def messageRef(self, messageRef=None):
        self._messageRef = messageRef

    @property
    def sendRef(self):
        return self._sendRef
    @sendRef.setter
    def sendRef(self, sendRef=None):
        self._sendRef = sendRef

    @property
    def broadcastRef(self):
        return self._broadcastRef
    @broadcastRef.setter
    def broadcastRef(self, broadcastRef=None):
        self._broadcastRef = broadcastRef

    def __str__(self):
        return ("messageRef=%s, sendRef=%s, broadcastRef=%s" %(self.messageRef, self.sendRef, self.broadcastRef))

class DeleteFaxDocumentRequest(object):
    '''
        delete fax request client object
    '''
    def __init__(self):
        self._documentRef = None

    @property
    def documentRef(self):
        return self._documentRef
    @documentRef.setter
    def documentRef(self, documentRef=None):
        self._documentRef = documentRef

    def __str__(self):
        return ("documentRef=%s" %(self._documentRef))


class FaxDocumentPreviewRequest(object):
    '''
        delete fax request client object
    '''
    def __init__(self):
        self._documentRef = None
        self._resolution = None
        self._ditheringTechnique = None
        self._docMergeData = []
        self._stampMergeData = []

    @property
    def documentRef(self):
        return self._documentRef
    @documentRef.setter
    def documentRef(self, documentRef=None):
        self._documentRef = documentRef

    @property
    def resolution(self):
        return self._resolution
    @resolution.setter
    def resolution(self, resolution=None):
        self._resolution = resolution

    @property
    def ditheringTechnique(self):
        return self._ditheringTechnique
    @ditheringTechnique.setter
    def ditheringTechnique(self, ditheringTechnique=None):
        self._ditheringTechnique = ditheringTechnique

    @property
    def docMergeData(self):
        return self._docMergeData
    def addDocMergeData(self, docMergeData=None):
        self._docMergeData.append(docMergeData)


    @property
    def stampMergeData(self):
        return self._stampMergeData
    def addStampMergeData(self, stampMergeData=None):
        self._stampMergeData.append(stampMergeData)



    def __str__(self):
        return ("documentRef=%s" %(self._documentRef))

class FaxResultsTotals(object):
    '''
        fax result totals client object
    '''
    def __init__(self):
        self._faxMessages = []
        self._successTotal = None
        self._blockedTotal = None
        self._failedTotal = None
        self._totalAttempts = None
        self._totalFaxDuration = None
        self._totalPages = None

    @property
    def successTotal(self):
        return self._successTotal
    @successTotal.setter
    def successTotal(self, total=None):
        self._successTotal = total

    @property
    def blockedTotal(self):
        return self._blockedTotal
    @blockedTotal.setter
    def blockedTotal(self, total=None):
        self._blockedTotal = total

    @property
    def failedTotal(self):
        return self._failedTotal
    @failedTotal.setter
    def failedTotal(self, total=None):
        self._failedTotal = total

    @property
    def totalAttempts(self):
        return self._totalAttempts
    @totalAttempts.setter
    def totalAttempts(self, total=None):
        self._totalAttempts = total

    @property
    def totalFaxDuration(self):
        return self._totalFaxDuration
    @totalFaxDuration.setter
    def totalFaxDuration(self, total=None):
        self._totalFaxDuration = total

    @property
    def totalPages(self):
        return self._totalPages
    @totalPages.setter
    def totalPages(self, total=None):
        self._totalPages = total

    def __str__(self):
        return ("successTotal=%s, blockedTotal=%s, failedTotal=%s, totalAttempts=%s, totalFaxDuration=%s, totalPages=%s"
                %(self.successTotal, self.blockedTotal, self.failedTotal, self.totalAttempts, self.totalFaxDuration, self.totalPages))


class FaxStatusTotals(object):
    '''
        fax status totals client object
    '''
    def __init__(self):
        self._pendingTotal = None
        self._processingTotal = None
        self._queuedTotal = None
        self._startingTotal = None
        self._sendingTotal = None
        self._finalizingTotal = None
        self._doneTotal = None

    @property
    def pendingTotal(self):
        return self._pendingTotal
    @pendingTotal.setter
    def pendingTotal(self, pendingTotal=None):
        self._pendingTotal = pendingTotal

    @property
    def processingTotal(self):
        return self._processingTotal
    @processingTotal.setter
    def processingTotal(self, processingTotal=None):
        self._processingTotal = processingTotal

    @property
    def queuedTotal(self):
        return self._queuedTotal
    @queuedTotal.setter
    def queuedTotal(self, queuedTotal=None):
        self._queuedTotal = queuedTotal

    @property
    def startingTotal(self):
        return self._startingTotal
    @startingTotal.setter
    def startingTotal(self, startingTotal=None):
        self._startingTotal = startingTotal



    @property
    def sendingTotal(self):
        return self._sendingTotal
    @sendingTotal.setter
    def sendingTotal(self, sendingTotal=None):
        self._sendingTotal = sendingTotal

    @property
    def finalizingTotal(self):
        return self._finalizingTotal
    @finalizingTotal.setter
    def finalizingTotal(self, finalizingTotal=None):
        self._finalizingTotal = finalizingTotal

    @property
    def doneTotal(self):
        return self._doneTotal
    @doneTotal.setter
    def doneTotal(self, doneTotal=None):
        self._doneTotal = doneTotal

    def __str__(self):
        return ("pending=%s, processing=%s, queued=%s, starting=%s, sending=%s, finalizing=%s, done=%s"
                %(self.pendingTotal, self.processingTotal, self.queuedTotal, self.startingTotal, self.sendingTotal, self.finalizingTotal, self.doneTotal))

class Response(object):
    '''
        response client object
        mapped to all types of api responses
    '''
    def __init__(self):
        self._faxMessageStatusResultsList = []
        self._faxResultTotals = None
        self._faxStatusTotals = None

    @property
    def faxStatusTotals(self):
        return self._faxStatusTotals
    @faxStatusTotals.setter
    def faxStatusTotals(self, faxStatusTotals):
        self._faxStatusTotals = faxStatusTotals

    @property
    def faxResultTotals(self):
        return self._faxResultTotals
    @faxResultTotals.setter
    def faxResultTotals(self, faxResultTotals):
        self._faxResultTotals = faxResultTotals

    @property
    def faxMessageStatusResultsList(self):
        return self._faxMessageStatusResultsList

    def addFaxMessageStatusResults(self, faxMessageStatusResults):
        self._faxMessageStatusResultsList.append(faxMessageStatusResults)


    def __str__(self):
        return ("faxResultTotals=[%s],\n faxStatusTotals=[%s],\n faxMessageStatusResultsList=[%s]"
                %(self.faxResultTotals, self.faxStatusTotals, self.faxMessageStatusResultsList))

class FaxMessage(object):
    '''
        fax message client object
    '''
    def __init__(self):
        self._messageRef = None
        self._sendTo = None
        self._sendFrom = None
        self._documents = []
        self._resolution = None
        self._blocklist = None
        self._scheduledStartTime = None
        self._retries = None
        self._busyRetries = None
        self._headerFormat = None

    @property
    def messageRef(self):
        return self._messageRef
    @messageRef.setter
    def messageRef(self, messageRef):
        self._messageRef = messageRef

    @property
    def sendTo(self):
        return self._sendTo
    @sendTo.setter
    def sendTo(self, sendTo):
        self._sendTo = sendTo

    @property
    def sendFrom(self):
        return self._sendFrom
    @sendFrom.setter
    def sendFrom(self, sendFrom):
        self._sendFrom = sendFrom

    def addDocument(self, document=None):
        self._documents.append(document)
    @property
    def documents(self):
        #return {'Document':self._documents}
        return self._documents

    @property
    def resolution(self):
        return self._resolution
    @resolution.setter
    def resolution(self, resolution):
        self._resolution = resolution

    @property
    def blocklist(self):
        return self._blocklist
    @blocklist.setter
    def blocklist(self, blocklist=None):
        self._blocklist = blocklist

    @property
    def scheduledStartTime(self):
        return self._scheduledStartTime
    @scheduledStartTime.setter
    def scheduledStartTime(self, scheduledStartTime):
        self._scheduledStartTime = scheduledStartTime

    @property
    def retries(self):
        return self._retries
    @retries.setter
    def retries(self, retries=None):
        self._retries = retries

    @property
    def busyRetries(self):
        return self._busyRetries
    @busyRetries.setter
    def busyRetries(self, busyRetries=None):
        self._busyRetries = busyRetries

    @property
    def headerFormat(self):
        return self._headerFormat
    @headerFormat.setter
    def headerFormat(self, headerFormat=None):
        self._headerFormat = headerFormat


class FaxMessageStatusResults(object):

    def __init__(self):
        self._errorCode = None
        self._errorName = None
        self._sendFrom  = None
        self._resolution = None
        self._retries = None
        self._busyRetries = None
        self._headerFormat = None
        self._messageRef = None
        self._sendRef = None
        self._broadcastRef = None
        self._sendTo = None
        self._status = None
        self._attempt = None
        self._result = None
        self._cost = None
        self._pages = None
        self._totalFaxDuration = None
        self._scheduledStartTime = None
        self._dateCallStarted = None
        self._dateCallEnded = None

    '''
        fax message status results client object
    '''

    @property
    def sendFrom(self):
        return self._sendFrom
    @sendFrom.setter
    def sendFrom(self, sendFrom=None):
        self._sendFrom = sendFrom

    @property
    def resolution(self):
        return self._resolution
    @resolution.setter
    def resolution(self, resolution=None):
        self._resolution = resolution

    @property
    def retries(self):
        return self._retries
    @retries.setter
    def retries(self, retries=None):
        self._retries = retries

    @property
    def busyRetries(self):
        return self._busyRetries
    @busyRetries.setter
    def busyRetries(self, busyRetries=None):
        self._busyRetries = busyRetries

    @property
    def headerFormat(self):
        return self._headerFormat
    @headerFormat.setter
    def headerFormat(self, headerFormat=None):
        self._headerFormat = headerFormat

    @property
    def messageRef(self):
        return self._messageRef
    @messageRef.setter
    def messageRef(self, messageRef=None):
        self._messageRef = messageRef

    @property
    def sendRef(self):
        return self._sendRef
    @sendRef.setter
    def sendRef(self, sendRef=None):
        self._sendRef = sendRef

    @property
    def broadcastRef(self):
        return self._broadcastRef
    @broadcastRef.setter
    def broadcastRef(self, broadcastRef=None):
        self._broadcastRef = broadcastRef

    @property
    def sendTo(self):
        return self._sendTo
    @sendTo.setter
    def sendTo(self, sendTo=None):
        self._sendTo = sendTo

    @property
    def status(self):
        return self._status
    @status.setter
    def status(self, status=None):
        self._status = status

    @property
    def errorCode(self):
        return self._errorCode
    @errorCode.setter
    def errorCode(self, errorCode=None):
        self._errorCode = errorCode

    @property
    def errorName(self):
        return self._errorName
    @errorName.setter
    def errorName(self, errorName=None):
        self._errorName = errorName

    @property
    def attempt(self):
        return self._attempt
    @attempt.setter
    def attempt(self, attempt=None):
        self._attempt = attempt

    @property
    def result(self):
        return self._result
    @result.setter
    def result(self, result=None):
        self._result = result

    @property
    def cost(self):
        return self._cost
    @cost.setter
    def cost(self, cost=None):
        self._cost = cost

    @property
    def pages(self):
        return self._pages
    @pages.setter
    def pages(self, pages=None):
        self._pages = pages

    @property
    def totalFaxDuration(self):
        return self._totalFaxDuration
    @totalFaxDuration.setter
    def totalFaxDuration(self, totalFaxDuration=None):
        self._totalFaxDuration = totalFaxDuration

    @property
    def scheduledStartTime(self):
        return self._scheduledStartTime
    @scheduledStartTime.setter
    def scheduledStartTime(self, scheduledStartTime=None):
        self._scheduledStartTime = scheduledStartTime

    @property
    def dateCallStarted(self):
        return self._dateCallStarted
    @dateCallStarted.setter
    def dateCallStarted(self, dateCallStarted=None):
        self._dateCallStarted = dateCallStarted

    @property
    def dateCallEnded(self):
        return self._dateCallEnded
    @dateCallEnded.setter
    def dateCallEnded(self, dateCallEnded=None):
        self._dateCallEnded = dateCallEnded


    def __str__(self):
        return ("errorCode=%s, errorName=%s, sendFrom=%s, resolution=%s, retries=%s, busyRetries=%s, headerFormat=%s, messageRef=%s, sendRef=%s, broadcastRef=%s, sendTo=%s, status=%s, attempt=%s, result=%s, "
                "cost=%s, pages=%s, totalFaxDuration=%s, scheduledStartTime=%s, dateCallStarted=%s, dateCallEnded=%s\n"
                %(self.errorCode, self.errorName, self.sendFrom, self.resolution, self.retries, self.busyRetries, self.headerFormat, self.messageRef, self.sendRef, self.broadcastRef, self.sendTo, self.status, self.attempt, self.result,
                  self.cost, self.pages, self.totalFaxDuration, self.scheduledStartTime, self.dateCallStarted, self.dateCallEnded))
    def __repr__(self):
        return self.__str__()

class FaxDocument(object):
    '''
        Document client object
    '''
    def __init__(self):
        self._fileData = None
        self._fileName = None
        self._filePath = None
        self._order = None

    @property
    def filePath(self):
        return self._filePath
    @filePath.setter
    def filePath(self, filePath):
        self._fileName = self.fileParser(filePath)
        file = open(filePath, "rb")
        binary_data = file.read()
        file.close()
        self._fileData = base64.b64encode(binary_data)

    @property
    def fileName(self):
        return self._fileName

    @property
    def fileData(self):
        return self._fileData

    @property
    def order(self):
        return self._order
    @order.setter
    def order(self, order):
        self._order = order

    def fileParser(self, fileName):
        parsedFilePath = os.path.split(fileName)
        return parsedFilePath[1]

class DocMergeData(object):
    def __init__(self):
        self._key = None
        self._value= None

    @property
    def key(self):
        return self._key
    @key.setter
    def key(self, key=None):
        self._key = key

    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, value=None):
        self._value = value

class StampMergeData(object):
    def __init__(self):
        self._keyXCoord = None
        self._keyYCoord = None

    @property
    def keyXCoord(self):
        return self._keyXCoord
    @keyXCoord.setter
    def keyXCoord(self, keyXCoord=None):
        self._keyXCoord = keyXCoord

    @property
    def keyYCoord(self):
        return self._keyYCoord
    @keyYCoord.setter
    def keyYCoord(self, keyYCoord=None):
        self._keyYCoord = keyYCoord

class TextStampMergeData(StampMergeData):
    def __init__(self):
        StampMergeData.__init__(self)
        self._textValue = None
        self._fontName = None
        self._fontSize = None

    @property
    def textValue(self):
        return self._textValue
    @textValue.setter
    def textValue(self, textValue=None):
        self._textValue = textValue

    @property
    def fontName(self):
        return self._fontName
    @fontName.setter
    def fontName(self, fontName=None):
        self._fontName = fontName

    @property
    def fontSize(self):
        return self._fontSize
    @fontSize.setter
    def fontSize(self, fontSize=None):
        self._fontSize = fontSize

class ImageStampMergeData(StampMergeData):
    def __init__(self):
        StampMergeData.__init__(self)
        self._fileName = None
        self._fileData = None
        self._width = None
        self._height = None

    @property
    def fileName(self):
        return self._fileName
    @fileName.setter
    def fileName(self, fileName=None):
        self._fileName = fileName

    @property
    def fileData(self):
        return self._fileData
    @fileData.setter
    def fileData(self, fileData=None):
        self._fileData = fileData

    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, width=None):
        self._width = width

    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, height=None):
        self._height = height

class Blocklist(object):

    def __init__(self):
        self._dncr = None
        self._fps = None
        self._smartblock = None
    '''
        blocklist client object
    '''
    @property
    def dncr(self):
        return self._dncr
    @dncr.setter
    def dncr(self, dncr=None):
        self._dncr = dncr


    @property
    def fps(self):
        return self._fps
    @fps.setter
    def fps(self, fps=None):
        self._fps = fps

    @property
    def smartblock(self):
        return self._smartblock
    @smartblock.setter
    def smartblock(self, smartblock=None):
        self._smartblock = smartblock



