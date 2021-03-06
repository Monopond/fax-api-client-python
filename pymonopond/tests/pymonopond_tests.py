import unittest
import sys
import pymonopond
from mockito import *
#sys.path.append("/home/froilan/Documents/ut_2/ut/idea/pymonopond")
from pymonopond.monopond_python_client import *
from suds.client import *
import unittest
# def  setup():
# 	print "SETUP!"

# def teardown():
# 	print "TEAR DOWN!"

# def test_basic():
# 	print "I RAN!"

#Only used for mocking
class StubObject:
    pass

class TestClientFunctions(unittest.TestCase):
    def setUp(self):
        pass

    def testMapApiResponseToResponse(self):
        client = mock(Client)
        mappingUtils = MappingUtils(client)
        client.service = mock(ServiceSelector)
        client.factory = mock(Factory)
        when(client.factory).create(any()).thenReturn(StubObject())
        apiResponse = StubObject()
        apiResponse.FaxStatusTotals = self.initializeStatusTotals()
        apiResponse.FaxResultsTotals = self.initializeResultTotals()
        apiFaxMessageStatus = StubObject()
        apiFaxMessageStatus.FaxDetails = self.initializeStatusDetails()
        faxResults = StubObject()
        apiFaxMessageStatus.FaxResults = faxResults
        apiFaxMessageStatus.FaxResults.FaxResult = [self.initializeStatusResults(),]
        faxMessages = StubObject()
        apiResponse.FaxMessages = faxMessages
        apiResponse.FaxMessages.FaxMessage=[apiFaxMessageStatus,]
        response = mappingUtils.mapApiResponseToResponse(apiResponse)

        self.assertEqual(4,response.faxResultTotals.successTotal)
        self.assertEqual(2,response.faxResultTotals.blockedTotal)
        self.assertEqual(2,response.faxResultTotals.failedTotal)
        self.assertEqual(5,response.faxResultTotals.totalAttempts)
        self.assertEqual(3,response.faxResultTotals.totalFaxDuration)
        self.assertEqual(1,response.faxResultTotals.totalPages)

        self.assertEqual(1,response.faxStatusTotals.pendingTotal)
        self.assertEqual(2,response.faxStatusTotals.processingTotal)
        self.assertEqual(3,response.faxStatusTotals.queuedTotal)
        self.assertEqual(4,response.faxStatusTotals.startingTotal)
        self.assertEqual(5,response.faxStatusTotals.sendingTotal)
        self.assertEqual(6,response.faxStatusTotals.finalizingTotal)
        self.assertEqual(7,response.faxStatusTotals.doneTotal)

        self.assertEqual('x',response.faxMessageStatusResultsList[0].sendFrom)
        self.assertEqual('fine',response.faxMessageStatusResultsList[0].resolution)
        self.assertEqual(1,response.faxMessageStatusResultsList[0].retries)
        self.assertEqual(1,response.faxMessageStatusResultsList[0].busyRetries)
        self.assertEqual('format',response.faxMessageStatusResultsList[0].headerFormat)
        self.assertEqual('error code',response.faxMessageStatusResultsList[0].errorCode)
        self.assertEqual('error name',response.faxMessageStatusResultsList[0].errorName)
        self.assertEqual(1,response.faxMessageStatusResultsList[0].attempt)
        self.assertEqual('success',response.faxMessageStatusResultsList[0].result)
        self.assertEqual(1,response.faxMessageStatusResultsList[0].cost)
        self.assertEqual(1,response.faxMessageStatusResultsList[0].pages)
        self.assertEqual('1',response.faxMessageStatusResultsList[0].totalFaxDuration)
        self.assertEqual('2010-10-10T00:00:00Z',response.faxMessageStatusResultsList[0].scheduledStartTime)
        self.assertEqual('date',response.faxMessageStatusResultsList[0].dateCallStarted)
        self.assertEqual('2010-10-10T00:00:10Z',response.faxMessageStatusResultsList[0].dateCallEnded)

    def testMapDocumentListToApiFaxDocumentList(self):
        client = mock(Client)
        mappingUtils = MappingUtils(client)
        client.service = mock(ServiceSelector)
        client.factory = mock(Factory)
        when(client.factory).create(any()).thenReturn(StubObject())
        documentList = [self.initialize_document(), self.initialize_document()]
        apiFaxDocumentList = mappingUtils.mapDocumentListToApiFaxDocumentList(documentList)

        apiFaxDocumentList = apiFaxDocumentList.get('Document')
        self.assertEqual('sampleFile.txt', apiFaxDocumentList[0].FileName)
        self.assertEqual('VGhpcyBpcyBhIHRlc3QgdGV4dCBmaWxl', apiFaxDocumentList[0].FileData)
        self.assertEqual(0, apiFaxDocumentList[0].Order)
        self.assertEqual('sampleFile.txt', apiFaxDocumentList[1].FileName)
        self.assertEqual('VGhpcyBpcyBhIHRlc3QgdGV4dCBmaWxl', apiFaxDocumentList[1].FileData)
        self.assertEqual(0, apiFaxDocumentList[1].Order)

    def testMapBlocklistsToApiFaxMessageBlocklist(self):
        client = mock(Client)
        mappingUtils = MappingUtils(client)
        client.service = mock(ServiceSelector)
        client.factory = mock(Factory)
        when(client.factory).create(any()).thenReturn(StubObject())
        blocklist = self.initialize_blocklist()
        apiFaxMessageBlocklist = mappingUtils.mapBlocklistsToApiFaxMessageBlocklist(blocklist)
        self.assertEqual('true', apiFaxMessageBlocklist._dncr)
        self.assertEqual('false', apiFaxMessageBlocklist._fps)
        self.assertEqual('false', apiFaxMessageBlocklist._smartblock)

    def testMapFaxMessageListToApiFaxMessageList(self):
        client = mock(Client)
        mappingUtils = MappingUtils(client)
        client.service = mock(ServiceSelector)
        client.factory = mock(Factory)
        when(client.factory).create(any()).thenReturn(StubObject())
        faxMessageList = [self.initialize_message(), self.initialize_message()]
        apiFaxMessageList = mappingUtils.mapFaxMessageListToApiFaxMessageList(faxMessageList)

        apiFaxMessageList = apiFaxMessageList.get('FaxMessage')
        apiFaxMessageList
        self.assertEqual('test-2-1-1', apiFaxMessageList[0].MessageRef)
        self.assertEqual('61280039890', apiFaxMessageList[0].SendTo)
        self.assertEqual('123', apiFaxMessageList[0].SendFrom)
        apiFaxDocumentList = apiFaxMessageList[0].Documents
        apiFaxDocumentList = apiFaxDocumentList.get('Document')
        self.assertEqual('sampleFile.txt', apiFaxDocumentList[0].FileName)
        self.assertEqual('VGhpcyBpcyBhIHRlc3QgdGV4dCBmaWxl', apiFaxDocumentList[0].FileData)
        self.assertEqual(0, apiFaxDocumentList[0].Order)
        self.assertEqual('sampleFile.txt', apiFaxDocumentList[1].FileName)
        self.assertEqual('VGhpcyBpcyBhIHRlc3QgdGV4dCBmaWxl', apiFaxDocumentList[1].FileData)
        self.assertEqual(0, apiFaxDocumentList[1].Order)
        apiFaxDocumentList = apiFaxMessageList[1].Documents
        apiFaxDocumentList = apiFaxDocumentList.get('Document')
        self.assertEqual('sampleFile.txt', apiFaxDocumentList[0].FileName)
        self.assertEqual('VGhpcyBpcyBhIHRlc3QgdGV4dCBmaWxl', apiFaxDocumentList[0].FileData)
        self.assertEqual(0, apiFaxDocumentList[0].Order)
        self.assertEqual('sampleFile.txt', apiFaxDocumentList[1].FileName)
        self.assertEqual('VGhpcyBpcyBhIHRlc3QgdGV4dCBmaWxl', apiFaxDocumentList[1].FileData)
        self.assertEqual(0, apiFaxDocumentList[1].Order)
        #apiFaxMessageBlocklist = apiFaxMessageList[0].Blocklists
        #self.assertEqual('true', apiFaxMessageBlocklist._dncr)
        #self.assertEqual('false', apiFaxMessageBlocklist._fps)
        #self.assertEqual('false', apiFaxMessageBlocklist._smartblock)
        #apiFaxMessageBlocklist = apiFaxMessageList[1].Blocklists
        #self.assertEqual('true', apiFaxMessageBlocklist._dncr)
        #self.assertEqual('false', apiFaxMessageBlocklist._fps)
        #self.assertEqual('false', apiFaxMessageBlocklist._smartblock)
        self.assertEqual('fine', apiFaxMessageList[0].Resolution)
        self.assertEqual(None, apiFaxMessageList[0].ScheduledStartTime)
        self.assertEqual(3, apiFaxMessageList[0].Retries)
        self.assertEqual(4, apiFaxMessageList[0].BusyRetries)
        self.assertEqual('From %from%, To %to%|%a %b %d %H:%M %Y', apiFaxMessageList[0].HeaderFormat)

    def testSendFax(self):
        client=self.mockClient()
        sendFaxRequest = SendFaxRequest()
        sendFaxRequest.resolution="fine"
        sendFaxRequest.broadcastRef = "123"
        sendFaxRequest.sendRef="test-2-1"
        sendFaxRequest.headerFormat="test"
        sendFaxRequest.retries=0
        sendFaxRequest.headerFormat="1-1-1"
        # sendFaxRequest.faxMessages = [self.initialize_message(), self.initialize_message()]
        sendFaxRequest.addFaxMessage(self.initialize_message())
        sendFaxRequest.addFaxMessage(self.initialize_message())

        when(client._client.factory).create(any()).thenReturn(StubObject())
        client.sendFax(sendFaxRequest)

        verify(client._client.service).SendFax(BroadcastRef='123', SendRef='test-2-1',
            FaxMessages= any(), Documents=any(), Resolution='fine',
            Blocklists = any(), Retries=0, HeaderFormat='1-1-1')

        #check handling for improper request
        with self.assertRaises(TypeError):
            client.sendFax(StubObject())

    def testStopFax(self):
        client=self.mockClient()

        stopFaxRequest = StopFaxRequest()
        stopFaxRequest.broadcastRef="123"
        stopFaxRequest.messageRef="456"
        stopFaxRequest.sendRef="aaa"

        client.stopFax(stopFaxRequest)
        verify(client._client.service).StopFax(MessageRef='456', SendRef='aaa',
            BroadcastRef='123')

        #check handling for improper request
        with self.assertRaises(TypeError):
            client.stopFax(StubObject())

    def testStopFax(self):
        client=self.mockClient()

        stopFaxRequest = StopFaxRequest()
        stopFaxRequest.broadcastRef="123"
        stopFaxRequest.messageRef="456"
        stopFaxRequest.sendRef="aaa"

        client.stopFax(stopFaxRequest)
        verify(client._client.service).StopFax(MessageRef='456', SendRef='aaa',
            BroadcastRef='123')

        #check handling for improper request
        with self.assertRaises(TypeError):
            client.stopFax(StubObject())

    def testResumeFax(self):
        client=self.mockClient()

        resumeFaxRequest = ResumeFaxRequest()
        resumeFaxRequest.broadcastRef="123"
        resumeFaxRequest.messageRef="456"
        resumeFaxRequest.sendRef="aaa"

        client.resumeFax(resumeFaxRequest)
        verify(client._client.service).ResumeFax(MessageRef='456', SendRef='aaa',
            BroadcastRef='123')

        #check handling for improper request
        with self.assertRaises(TypeError):
            client.resumeFax(StubObject())

    def testPauseFax(self):
        client=self.mockClient()

        pauseFaxRequest = PauseFaxRequest()
        pauseFaxRequest.broadcastRef="123"
        pauseFaxRequest.messageRef="456"
        pauseFaxRequest.sendRef="aaa"

        client.pauseFax(pauseFaxRequest)
        verify(client._client.service).PauseFax(MessageRef='456', SendRef='aaa',
            BroadcastRef='123')

        #check handling for improper request
        with self.assertRaises(TypeError):
            client.pauseFax(StubObject())

    def testFaxStatus(self):
        client=self.mockClient()

        faxStatusRequest = FaxStatusRequest()
        faxStatusRequest.broadcastRef="123"
        faxStatusRequest.messageRef="456"
        faxStatusRequest.sendRef="aaa"
        faxStatusRequest.verbosity="brief"

        client.faxStatus(faxStatusRequest)
        verify(client._client.service).FaxStatus(MessageRef='456', SendRef='aaa',
            BroadcastRef='123', Verbosity='brief')

        #check handling for improper request
        with self.assertRaises(TypeError):
            client.faxStatus(StubObject())

    def testFileNameIsConvertedToBase64FileData(self):
        document = self.initialize_document()
        self.assertEqual("VGhpcyBpcyBhIHRlc3QgdGV4dCBmaWxl", document.fileData)

    def testFileParserWithOnlyTheFileNameReturnsOnlyTheFileName(self):
        document = FaxDocument()
        parsed = document.fileParser("file.txt")
        self.assertEqual("file.txt", parsed)

    def testFileParserWithOneLevelDirectoryReturnsOnlyTheFileName(self):
        document = FaxDocument()
        parsed = document.fileParser("/home/file.txt")
        self.assertEqual("file.txt", parsed)

    def testFileParserWithTwoLevelDirectoryReturnsOnlyTheFileName(self):
        document = FaxDocument()
        parsed = document.fileParser("/home/someDirectory/file.txt")
        self.assertEqual("file.txt", parsed)

    def testFileParserWithTwoLevelDirectoryReturnsOnlyTheFileName(self):
        document = FaxDocument()
        parsed = document.fileParser("home/somedirectory/file.txt")
        self.assertEqual("file.txt", parsed)

    def mockClient(self):
        client = ClientWrapper('file:///' + os.path.join(os.path.dirname(__file__), 'faxapi-v2.wsdl'),'user','pass')
        client._client = mock(Client)
        client._client.service = mock(ServiceSelector)
        client._client.factory = mock(Factory)
        return client

    def initialize_document(self):
        document = FaxDocument()
        document.filePath = 'sampleFile.txt'
        document.order = 0
        return document

    def initialize_blocklist(self):
        blocklist = Blocklist()
        blocklist.dncr='true'
        blocklist.fps='false'
        blocklist.smartblock='false'
        return blocklist

    def initialize_message(self):
        faxMessage = FaxMessage()
        faxMessage.messageRef = 'test-2-1-1'
        faxMessage.sendTo = '61280039890'
        faxMessage.sendFrom = '123'
        document = self.initialize_document()
        # documents = [document, document]
        blocklists = self.initialize_blocklist()
        faxMessage.blocklist = blocklists
        faxMessage.addDocument(document)
        faxMessage.addDocument(document)
        faxMessage.scheduledStartTime = None
        faxMessage.retries = 3
        faxMessage.busyRetries = 4
        faxMessage.headerFormat = "From %from%, To %to%|%a %b %d %H:%M %Y"
        faxMessage.resolution = 'fine'
        return faxMessage

    def initializeStatusTotals(self):
        statusTotals = StubObject()
        statusTotals._pending = 1
        statusTotals._processing = 2
        statusTotals._queued = 3
        statusTotals._starting = 4
        statusTotals._sending = 5
        statusTotals._finalizing = 6
        statusTotals._done = 7
        return statusTotals

    def initializeResultTotals(self):
        resultTotals = StubObject()
        resultTotals._totalPages = 1
        resultTotals._failed = 2
        resultTotals._totalFaxDuration = 3
        resultTotals._success = 4
        resultTotals._totalAttempts = 5
        resultTotals._blocked=2
        return resultTotals

    def initializeStatusDetails(self):
        statusDetails = StubObject()
        statusDetails._sendFrom = "x"
        statusDetails._resolution = "fine"
        statusDetails._retries = 1
        statusDetails._busyRetries = 1
        statusDetails._headerFormat = "format"
        return statusDetails

    def initializeStatusResults(self):
        statusResults = StubObject()
        error = StubObject()
        error._code='error code'
        error._name='error name'
        statusResults.Error=error
        statusResults._attempt = 1
        statusResults._result = "success"
        statusResults._cost = 1
        statusResults._pages = 1
        statusResults._totalFaxDuration = "1"
        statusResults._scheduledStartTime = "2010-10-10T00:00:00Z"
        statusResults._dateCallStarted = "date"
        statusResults._dateCallEnded = "2010-10-10T00:00:10Z"
        return statusResults


if __name__ == '__main__':
    unittest.main()



