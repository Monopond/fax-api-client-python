
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

class FaxResultsTotals:
    def __init__(self):
        self._faxMessages = []

    def _setSuccessTotal(self, total=None):
        self._successTotal = total
    def _getSuccessTotal(self):
        return self._successTotal

    def _setBlockedTotal(self, total=None):
        self._blockedTotal = total
    def _getBlockedTotal(self):
        return self._blockedTotal

    def _setFailedTotal(self, total=None):
        self._failedTotal = total
    def _getFailedTotall(self):
        return self._failedTotal

    def _setTotalAttempts(self, total=None):
        self._totalAttempts = total
    def _getotalAttempts(self):
        return self._totalAttempts

    def _setTotalFaxDuration(self, total=None):
        self._totalFaxDuration = total
    def _getTotalFaxDuration(self):
        return self._totalFaxDuration

    def _setTotalPages(self, total=None):
        self._totalPages = total
    def _getTotalPages(self):
        return self._totalPages

    successTotal = property(_setSuccessTotal, _getSuccessTotal)
    blockedTotal = property(_setBlockedTotal, _getBlockedTotal)
    failedTotal = property(_setFailedTotal, _getFailedTotall)
    totalAttempts = property(_setTotalAttempts, _getTotalFaxDuration)
    totalFaxDuration = property(_setTotalFaxDuration, _getTotalFaxDuration)
    totalPages = property(_setTotalPages, _getTotalPages)
    #faxMessages = property(_getFaxMessages)
    def __str__(self):
        return ("successTotal=%s, blockedTotal=%s, failedTotal=%s, totalAttempts=%s, totalFaxDuration=%s, totalPages=%s"
                %(self.successTotal, self.blockedTotal, self.failedTotal, self.totalAttempts, self.totalFaxDuration, self.totalPages))


class FaxStatusTotals:
    def _setPendingTotal(self, pendingTotal=None):
        self._pendingTotal = pendingTotal
    def _getPendingTotal(self):
        return self._pendingTotal

    def _setProcessingTotal(self, processingTotal=None):
        self._processingTotal = processingTotal
    def _getProcessingTotal(self):
        return self._processingTotal

    def _setQueuedTotal(self, queuedTotal=None):
        self._queuedTotal = queuedTotal
    def _getQueuedTotal(self):
        return self._queuedTotal

    def _setStartingTotal(self, startingTotal=None):
        self._startingTotal = startingTotal
    def _getStartingTotal(self):
        return self._startingTotal

    def _setSendingTotal(self, sendingTotal=None):
        self._sendingTotal = sendingTotal
    def _getSendingTotal(self):
        return self._sendingTotal

    def _setFinalizingTotal(self, finalizingTotal=None):
        self._finalizingTotal = finalizingTotal
    def _getFinalizingTotal(self):
        return self._finalizingTotal

    def _setDoneTotal(self, doneTotal=None):
        self._doneTotal = doneTotal
    def _getDoneTotal(self):
        return self._doneTotal

    pending = property(_setPendingTotal, _getPendingTotal)
    processing = property(_setProcessingTotal, _getProcessingTotal)
    queued = property(_setQueuedTotal, _getQueuedTotal)
    starting = property(_setStartingTotal, _getStartingTotal)
    sending = property(_setSendingTotal, _getSendingTotal)
    finalizing = property(_setFinalizingTotal, _getFinalizingTotal)
    done = property(_setDoneTotal, _getFinalizingTotal)

    def __str__(self):
        return ("pending=%s, processing=%s, queued=%s, starting=%s, sending=%s, finalizing=%s, done=%s"
                %(self.pending, self.processing, self.queued, self.starting, self.sending, self.finalizing, self.done))

class Response:
    def __init__(self):
        self.faxMessageStatusResultsList = []
    def _setFaxStatusTotals(self, faxStatusTotals):
        self._faxStatusTotals = faxStatusTotals
    def _getFaxStatusTotals(self):
        return self._faxStatusTotals

    def _setFaxResultTotals(self, faxResultTotals):
        self._faxResultTotals = faxResultTotals
    def _getFaxResultTotals(self):
        return self._faxResultTotals

    def addFaxMessageStatusResults(self, faxMessageStatusResults):
        self.faxMessageStatusResultsList.append(faxMessageStatusResults)
    def _getFaxMessageStatusResultsList(self):
        return self.faxMessageStatusResultsList



    faxResultTotals = property(_setFaxResultTotals, _getFaxResultTotals)
    faxStatusTotals = property(_setFaxStatusTotals, _getFaxStatusTotals)
    faxMessageStatusResultsList = property(_getFaxMessageStatusResultsList)
    def __str__(self):
        return ("faxResultTotals=[%s],\n faxStatusTotals=[%s],\n faxMessageStatusResultsList=[%s]"
                %(self.faxResultTotals, self.faxStatusTotals, self.faxMessageStatusResultsList))

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
    def _getRetries(self):
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
    retries = property(_setRetries, _getRetries)
    busyRetries = property(_setBusyRetries, _getBusyRetries)
    headerFormat = property(_setHeaderFormat, _getHeaderFormat)

class FaxMessageStatusResults:

    def _setSendFrom(self, sendFrom=None):
        self._sendFrom = sendFrom
    def _getSendFrom(self):
        return self._sendFrom

    def _setResolution(self, resolution=None):
        self._resolution = resolution
    def _getResolution(self):
        return self._resolution

    def _setRetries(self, retries=None):
        self._retries = retries
    def _getRetries(self):
        return self._retries

    def _setBusyRetries(self, busyRetries=None):
        self._busyRetries = busyRetries
    def _getBusyRetries(self):
        return self._busyRetries

    def _setHeaderFormat(self, headerFormat=None):
        self._headerFormat = headerFormat
    def _getHeaderFormat(self):
        return self._headerFormat

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

    def _setSendTo(self, sendTo=None):
        self._sendTo = sendTo
    def _getSendTo(self):
        return self._sendTo

    def _setStatus(self, status=None):
        self._status = status
    def _getStatus(self):
        return self._status

    def _setErrorCode(self, errorCode=None):
        self._errorCode = errorCode
    def _getErrorCode(self):
        return self._setErrorCode

    def _setErrorName(self, errorName=None):
        self._errorName = errorName
    def _getErrorName(self):
        return self._errorName

    def _setAttempt(self, attempt=None):
        self._attempt = attempt
    def _getAttempt(self):
        return self._attempt

    def _setResult(self, result=None):
        self._result = result
    def _getResult(self):
        return self._result

    def _setCost(self, cost=None):
        self._cost = cost
    def _getCost(self):
        return self._cost

    def _setPages(self, pages=None):
        self._pages = pages
    def _getPages(self):
        return self._pages

    def _setTotalFaxDurationt(self, totalFaxDuration=None):
        self._totalFaxDuration = totalFaxDuration
    def _getTotalFaxDuration(self):
        return self._totalFaxDuration

    def _setScheduledStartTime(self, scheduledStartTime=None):
        self._scheduledStartTime = scheduledStartTime
    def _getScheduledStartTime(self):
        return self._scheduledStartTime

    def _setDateCallStarted(self, dateCallStarted=None):
        self._dateCallStarted = dateCallStarted
    def _getDateCallStarted(self):
        return self._dateCallStarted

    def _setDateCallEnded(self, dateCallEnded=None):
        self._dateCallEnded = dateCallEnded
    def _getDateCallEnded(self):
        return self._dateCallEnded

    errorCode = property(_setErrorCode, _getErrorCode)
    errorName = property(_setErrorName, _getErrorName)
    sendFrom = property(_setSendFrom, _getSendFrom)
    resolution = property(_setResolution, _getResolution)
    retries = property(_setRetries, _getRetries)
    busyRetries = property(_setBusyRetries, _getBusyRetries)
    headerFormat = property(_setHeaderFormat, _getHeaderFormat)
    messageRef = property(_setMessageRef, _getMessageRef)
    sendRef = property(_setSendRef, _getSendRef)
    broadcastRef = property(_setBroadcastRef, _getBroadcastRef)
    sendTo = property(_setSendTo, _getSendTo)
    status = property(_setStatus, _getStatus)
    attempt = property(_setAttempt, _getAttempt)
    result = property(_setResult, _getResult)
    cost = property(_setCost, _getCost)
    pages = property(_setPages, _getPages)
    totalFaxDuration = property(_setTotalFaxDurationt, _getTotalFaxDuration)
    scheduledStartTime = property(_setScheduledStartTime, _getScheduledStartTime)
    dateCallStarted = property(_setDateCallStarted, _getDateCallStarted)
    dateCallEnded = property(_setDateCallEnded, _getDateCallEnded)

    def __str__(self):
        return ("errorCode=%s, errorName=%s, sendFrom=%s, resolution=%s, retries=%s, busyRetries=%s, headerFormat=%s, messageRef=%s, sendRef=%s, broadcastRef=%s, sendTo=%s, status=%s, attempt=%s, result=%s, "
                "cost=%s, pages=%s, totalFaxDuration=%s, scheduledStartTime=%s, dateCallStarted=%s, dateCallEnded=%s\n"
                %(self.errorCode, self.errorName, self.sendFrom, self.resolution, self.retries, self.busyRetries, self.headerFormat, self.messageRef, self.sendRef, self.broadcastRef, self.sendTo, self.status, self.attempt, self.result,
                self.cost, self.pages, self.totalFaxDuration, self.scheduledStartTime, self.dateCallStarted, self.dateCallEnded))
    def __repr__(self):
        return self.__str__()

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

    def mapApiResponseToResponse(self, apiResponse):
        response = Response()
        statusTotals = FaxStatusTotals()
        if hasattr(apiResponse, 'FaxStatusTotals'):
            if hasattr(apiResponse.FaxStatusTotals, '_pending'):
                statusTotals.pending = apiResponse.FaxStatusTotals._pending
            if hasattr(apiResponse.FaxStatusTotals, '_processing'):
                statusTotals.processing = apiResponse.FaxStatusTotals._processing
            if hasattr(apiResponse.FaxStatusTotals, '_queued'):
                statusTotals.queued = apiResponse.FaxStatusTotals._queued
            if hasattr(apiResponse.FaxStatusTotals, '_starting'):
                statusTotals.starting = apiResponse.FaxStatusTotals._starting
            if hasattr(apiResponse.FaxStatusTotals, '_sending'):
                statusTotals.sending = apiResponse.FaxStatusTotals._sending
            if hasattr(apiResponse.FaxStatusTotals, '_finalizing'):
                statusTotals.finalizing = apiResponse.FaxStatusTotals._finalizing
            if hasattr(apiResponse.FaxStatusTotals, '_done'):
                statusTotals.done = apiResponse.FaxStatusTotals._done

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
        wrappedResult = self.mapApiResponseToResponse(result)
        return wrappedResult

    def faxStatus(self, request):
        if isinstance(request, FaxStatusRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        result = self._client.service.FaxStatus(MessageRef=request.messageRef, SendRef=request.sendRef,
            BroadcastRef=request.broadcastRef, Verbosity=request.verbosity)
        wrappedResult = self.mapApiResponseToResponse(result)
        return wrappedResult

    def pauseFax(self, request):
        if isinstance(request, PauseFaxRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        result = self._client.service.PauseFax(MessageRef=request.messageRef, SendRef=request.sendRef,
            BroadcastRef=request.broadcastRef)
        wrappedResult = self.mapApiResponseToResponse(result)
        return wrappedResult

    def resumeFax(self, request):
        if isinstance(request, ResumeFaxRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        result = self._client.service.ResumeFax(MessageRef=request.messageRef, SendRef=request.sendRef,
            BroadcastRef=request.broadcastRef)
        wrappedResult = self.mapApiResponseToResponse(result)
        return wrappedResult

    def stopFax(self, request):
        if isinstance(request, StopFaxRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        result = self._client.service.StopFax(MessageRef=request.messageRef, SendRef=request.sendRef,
            BroadcastRef=request.broadcastRef)
        wrappedResult = self.mapApiResponseToResponse(result)
        print result
        return wrappedResult

    def getTypeInstance(self, typeName):
        return self._client.factory.create(typeName)

    def __str__(self):
        return self._client.__str__()
