
from suds.client import Client
from suds.bindings import binding
from suds.sax.element import Element, Attribute

class SendFaxRequest:

    def __init__(self):
        self._faxMessages = []
        self._documents = []

    def _setBroadcastRef(self, broadcastRef=None):
        self._broadcastRef = broadcastRef
    def _getBroadcastRef(self):
        return self._broadcastRef

    def _setSendRef(self, sendRef=None):
        self._sendRef = sendRef
    def _getSendRef(self):
        return self._sendRef

    def _setResolution(self, resolution=None):
        self._resolution = resolution
    def _getResolution(self):
        return self._resolution

    def addFaxMessage(self, faxMessage=None):
        self._faxMessages.append(faxMessage)
    def _setFaxMessages(self, faxMessages=None):
        self._faxMessages = faxMessages
    def _getFaxMessages(self):
        return self._faxMessages

    def addDocument(self, document=None):
        self._documents.append(document)
    def _setDocuments(self, documents=None):
        self._documents = documents
    def _getDocuments(self):
        return self._documents

    def _setBlocklists(self, blocklists=None):
        self._blocklists = blocklists
    def _getBlocklists(self):
        return self._blocklists

    def _setSendFrom(self, sendFrom=None):
        self._sendFrom = sendFrom
    def _getSendFrom(self):
        return self._sendFrom

    def _setScheduledStartTime(self, scheduledStartTime=None):
        self._scheduledStartTime = scheduledStartTime
    def _getScheduledStartTime(self):
        return self._scheduledStartTime

    def _setRetries(self, retries=None):
        self._retries = retries
    def _getRetriese(self):
        return self._retries

    def _setBusyRetries(self, busyRetries=None):
        self._busyRetries = busyRetries
    def _getBusyRetries(self):
        return self._busyRetries

    def _setHeaderFormat(self, headerFormat=None):
        self._headerFormat = headerFormat
    def _getHeaderFormat(self):
        return self._headerFormat

    broadcastRef = property(_setBroadcastRef, _getBroadcastRef)
    sendRef = property(_setSendRef, _getSendRef)
    resolution = property(_setResolution, _getResolution)
    faxMessages = property(_getFaxMessages)
    documents = property(_getDocuments)
    blocklists = property(_setBlocklists, _getBlocklists)
    sendFrom = property(_setSendFrom, _getSendFrom)
    scheduledStartTime = property(_setScheduledStartTime, _getScheduledStartTime)
    retries = property(_setRetries, _getRetriese)
    busyRetries = property(_setBusyRetries, _getBusyRetries)
    headerFormat = property(_setHeaderFormat, _getHeaderFormat)

    def __str__(self):
        return ("broadcastRef=%s, sendRef=%s, resolution=%s,  sendFrom=%s, scheduledStartTime=%s, retries=%s, busyRetries=%s, headerFormat=%s, faxMessages=%s, documents=%s"
                %(self.broadcastRef, self.sendRef, self.resolution, self.sendFrom, self.scheduledStartTime, self.retries, self.busyRetries, self.headerFormat, self.faxMessages, self.documents))

class FaxStatusRequest:

    def _setMessageRef(self, messageRef=None):
        self._messageRef = messageRef
    def _getMessageRef(self):
        return self._messageRef

    def _setSendRef(self, sendRef=None):
        self._sendRef = sendRef
    def _getSendRef(self):
        return self._sendRef

    def _setBroadcastRef(self, broadcastRef=None):
        self._broadcastRef = broadcastRef
    def _getBroadcastRef(self):
        return self._broadcastRef

    def _setVerbosity(self, verbosity=None):
        self._verbosity = verbosity
    def _getVerbosity(self):
        return self._verbosity

    messageRef = property(_setMessageRef, _getMessageRef)
    sendRef = property(_setSendRef, _getSendRef)
    broadcastRef = property(_setBroadcastRef, _getBroadcastRef)
    verbosity = property(_setVerbosity, _getVerbosity)

    def __str__(self):
        return ("messageRef=%s, sendRef=%s, broadcastRef=%s, verbosity=%s" %(self.messageRef, self.sendRef, self.broadcastRef, self.verbosity))

class PauseFaxRequest:

    def _setMessageRef(self, messageRef=None):
        self._messageRef = messageRef
    def _getMessageRef(self):
        return self._messageRef

    def _setSendRef(self, sendRef=None):
        self._sendRef = sendRef
    def _getSendRef(self):
        return self._sendRef

    def _setBroadcastRef(self, broadcastRef=None):
        self._broadcastRef = broadcastRef
    def _getBroadcastRef(self):
        return self._broadcastRef

    messageRef = property(_setMessageRef, _getMessageRef)
    sendRef = property(_setSendRef, _getSendRef)
    broadcastRef = property(_setBroadcastRef, _getBroadcastRef)

    def __str__(self):
        return ("messageRef=%s, sendRef=%s, broadcastRef=%s" %(self.messageRef, self.sendRef, self.broadcastRef))


class ResumeFaxRequest:

    def _setMessageRef(self, messageRef=None):
        self._messageRef = messageRef
    def _getMessageRef(self):
        return self._messageRef

    def _setSendRef(self, sendRef=None):
        self._sendRef = sendRef
    def _getSendRef(self):
        return self._sendRef

    def _setBroadcastRef(self, broadcastRef=None):
        self._broadcastRef = broadcastRef
    def _getBroadcastRef(self):
        return self._broadcastRef

    messageRef = property(_setMessageRef, _getMessageRef)
    sendRef = property(_setSendRef, _getSendRef)
    broadcastRef = property(_setBroadcastRef, _getBroadcastRef)

    def __str__(self):
        return ("messageRef=%s, sendRef=%s, broadcastRef=%s" %(self.messageRef, self.sendRef, self.broadcastRef))

class StopFaxRequest:

    def _setMessageRef(self, messageRef=None):
        self._messageRef = messageRef
    def _getMessageRef(self):
        return self._messageRef

    def _setSendRef(self, sendRef=None):
        self._sendRef = sendRef
    def _getSendRef(self):
        return self._sendRef

    def _setBroadcastRef(self, broadcastRef=None):
        self._broadcastRef = broadcastRef
    def _getBroadcastRef(self):
        return self._broadcastRef

    messageRef = property(_setMessageRef, _getMessageRef)
    sendRef = property(_setSendRef, _getSendRef)
    broadcastRef = property(_setBroadcastRef, _getBroadcastRef)

    def __str__(self):
        return ("messageRef=%s, sendRef=%s, broadcastRef=%s" %(self.messageRef, self.sendRef, self.broadcastRef))

class Response:
    def __init__(self):
        self._faxResultTotals = {'pending':None,'processing':None,'queued':None,'starting':None,'sending':None,'finalizing':None}

class FaxMessage:
    def _setMessageRef(self, messageRef):
        self._messageRef = messageRef
    def _getMessageRef(self):
        return self._messageRef

    def _setSendTo(self, sendTo):
        self._sendTo = sendTo
    def _getSendTo(self):
        return self._sendTo

    def _setSendFrom(self, sendFrom):
        self._sendFrom = sendFrom
    def _getSendFrom(self):
        return self._sendFrom

    def addDocument(self, document=None):
        self._documents.append(document)
    def _setDocuments(self, documents=None):
        self._documents = documents
    def _getDocuments(self):
        #return {'Document':self._documents}
        return self._documents

    def _setResolution(self, resolution):
        self._resolution = resolution
    def _getResolution(self):
        return self._resolution

    def _setBlocklist(self, blocklist=None):
        self._blocklist = blocklist
    def _getBlocklist(self):
        return self._blocklist

    def _setScheduledStartTime(self, scheduledStartTime):
        self._scheduledStartTime = scheduledStartTime
    def _getScheduledStartTime(self):
        return self._scheduledStartTime

    def _setRetries(self, retries=None):
        self._retries = retries
    def _getRetriese(self):
        return self._retries

    def _setBusyRetries(self, busyRetries=None):
        self._busyRetries = busyRetries
    def _getBusyRetries(self):
        return self._busyRetries

    def _setHeaderFormat(self, headerFormat=None):
        self._headerFormat = headerFormat
    def _getHeaderFormat(self):
        return self._headerFormat

    messageRef = property(_setMessageRef, _getMessageRef)
    sendFrom = property(_setSendFrom, _getSendFrom)
    sendTo = property(_setSendTo, _getSendTo)
    documents = property(_getDocuments)
    resolution = property(_setResolution, _getResolution)
    blocklist = property(_setBlocklist, _getBlocklist)
    scheduledStartTime = property(_setScheduledStartTime, _getScheduledStartTime)
    retries = property(_setRetries, _getRetriese)
    busyRetries = property(_setBusyRetries, _getBusyRetries)
    headerFormat = property(_setHeaderFormat, _getHeaderFormat)

class Document:
    def _setFileName(self, fileName):
        self._fileName = fileName
    def _getFileName(self):
        return self._fileName

    def _setFileData(self, fileData):
        self.fileData = fileData
    def _getFileData(self):
        return self._fileDate

    def _setOrder(self, order):
        self._order = order
    def _getOrder(self):
        return self._order

    fileName = property(_setFileName, _getFileName)
    fileData = property(_setFileData, _getFileData)
    order = property(_setOrder, _getOrder)

class Blocklist:
    def _setDncr(self, dncr=None):
        self._dncr = dncr
    def _getDncr(self):
        return self._dncr

    def _setFps(self, fps=None):
        self._fps = fps
    def _getFps(self):
        return self._fps

    def _setSmartblock(self, smartblock=None):
        self._smartblock = smartblock
    def _getSmartblock(self):
        return self._smartblock

    dncr = property(_setDncr, _getDncr)
    fps = property(_setFps, _getFps)
    smartblock = property(_setSmartblock, _getSmartblock)

class MappingUtils:

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
        if faxMessage.blocklist is not None:
            apiFaxMessage.Blocklists = self.mapBlocklistsToApiFaxMessageBlocklist(faxMessage.blocklist)
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

class ClientWrapper(MappingUtils):
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

    def sendFax(self, request):
        if isinstance(request, SendFaxRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        apiFaxDocuments = self.mapDocumentListToApiFaxDocumentList(request.documents)
        apiFaxMessages = self.mapFaxMessageListToApiFaxMessageList(request.faxMessages)
        apiFaxMessageBlocklist = None
        if request.blocklists is not None:
            apiFaxMessageBlocklist = self.mapBlocklistsToApiFaxMessageBlocklist(request.blocklists)
        result = self._client.service.SendFax(BroadcastRef=request.broadcastRef, SendRef=request.sendRef,
            FaxMessages= apiFaxMessages, Documents=apiFaxDocuments, Resolution=request.resolution,
            Blocklists = apiFaxMessageBlocklist, Retries=request.retries, HeaderFormat=request.headerFormat)
        return result

    def faxStatus(self, request):
        if isinstance(request, FaxStatusRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        result = self._client.service.FaxStatus(MessageRef=request.messageRef, SendRef=request.sendRef,
            BroadcastRef=request.broadcastRef, Verbosity=request.verbosity)
        return result

    def pauseFax(self, request):
        if isinstance(request, PauseFaxRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        result = self._client.service.PauseFax(MessageRef=request.messageRef, SendRef=request.sendRef,
            BroadcastRef=request.broadcastRef)
        return result

    def resumeFax(self, request):
        if isinstance(request, ResumeFaxRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        result = self._client.service.ResumeFax(MessageRef=request.messageRef, SendRef=request.sendRef,
            BroadcastRef=request.broadcastRef)
        return result

    def stopFax(self, request):
        if isinstance(request, StopFaxRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        result = self._client.service.StopFax(MessageRef=request.messageRef, SendRef=request.sendRef,
            BroadcastRef=request.broadcastRef)
        return result

    def getTypeInstance(self, typeName):
        return self._client.factory.create(typeName)

    def __str__(self):
        return self._client.__str__()
