import unittest
import sys
import pymonopond
from mockito import *
#sys.path.append("/home/froilan/Documents/ut_2/ut/idea/pymonopond")
from pymonopond.monopond_python_client import *
from suds.client import *
from unittest import *
# def  setup():
# 	print "SETUP!"

# def teardown():
# 	print "TEAR DOWN!"

# def test_basic():
# 	print "I RAN!"

class TestClientFunctions(unittest.TestCase):
    def setUp(self):
        pass
    def testMapDocumentListToApiFaxDocumentList(self):
        client = ClientWrapper('file:///home/froilan/Documents/ut_2/ut/idea/pymonopond/tests/faxapi-v2.wsdl','user','pass')

        documentList = [self.initialize_document(), self.initialize_document()]
        apiFaxDocumentList = client.mapDocumentListToApiFaxDocumentList(documentList)

        apiFaxDocumentList = apiFaxDocumentList.get('Document')
        self.assertEqual('test', apiFaxDocumentList[0].FileName)
        self.assertEqual('VGhpcyBpcyBhbm90aGVyIGZheA==', apiFaxDocumentList[0].FileData)
        self.assertEqual(0, apiFaxDocumentList[0].Order)
        self.assertEqual('test', apiFaxDocumentList[1].FileName)
        self.assertEqual('VGhpcyBpcyBhbm90aGVyIGZheA==', apiFaxDocumentList[1].FileData)
        self.assertEqual(0, apiFaxDocumentList[1].Order)

    def testMapBlocklistsToApiFaxMessageBlocklist(self):
        client = ClientWrapper('file:///home/froilan/Documents/ut_2/ut/idea/pymonopond/tests/faxapi-v2.wsdl','user','pass')

        blocklist = self.initialize_blocklist()
        apiFaxMessageBlocklist = client.mapBlocklistsToApiFaxMessageBlocklist(blocklist)
        self.assertEqual('true', apiFaxMessageBlocklist._dncr)
        self.assertEqual('false', apiFaxMessageBlocklist._fps)
        self.assertEqual('false', apiFaxMessageBlocklist._smartblock)

    def testMapFaxMessageListToApiFaxMessageList(self):
        client = ClientWrapper('file:///home/froilan/Documents/ut_2/ut/idea/pymonopond/tests/faxapi-v2.wsdl','user','pass')
        faxMessageList = [self.initialize_message(), self.initialize_message()]
        apiFaxMessageList = client.mapFaxMessageListToApiFaxMessageList(faxMessageList)

        apiFaxMessageList = apiFaxMessageList.get('FaxMessage')
        apiFaxMessageList
        self.assertEqual('test-2-1-1', apiFaxMessageList[0].MessageRef)
        self.assertEqual('61280039890', apiFaxMessageList[0].SendTo)
        self.assertEqual('123', apiFaxMessageList[0].SendFrom)
        apiFaxDocumentList = apiFaxMessageList[0].Documents
        apiFaxDocumentList = apiFaxDocumentList.get('Document')
        self.assertEqual('test', apiFaxDocumentList[0].FileName)
        self.assertEqual('VGhpcyBpcyBhbm90aGVyIGZheA==', apiFaxDocumentList[0].FileData)
        self.assertEqual(0, apiFaxDocumentList[0].Order)
        self.assertEqual('test', apiFaxDocumentList[1].FileName)
        self.assertEqual('VGhpcyBpcyBhbm90aGVyIGZheA==', apiFaxDocumentList[1].FileData)
        self.assertEqual(0, apiFaxDocumentList[1].Order)
        apiFaxDocumentList = apiFaxMessageList[1].Documents
        apiFaxDocumentList = apiFaxDocumentList.get('Document')
        self.assertEqual('test', apiFaxDocumentList[0].FileName)
        self.assertEqual('VGhpcyBpcyBhbm90aGVyIGZheA==', apiFaxDocumentList[0].FileData)
        self.assertEqual(0, apiFaxDocumentList[0].Order)
        self.assertEqual('test', apiFaxDocumentList[1].FileName)
        self.assertEqual('VGhpcyBpcyBhbm90aGVyIGZheA==', apiFaxDocumentList[1].FileData)
        self.assertEqual(0, apiFaxDocumentList[1].Order)
        apiFaxMessageBlocklist = apiFaxMessageList[0].Blocklists
        self.assertEqual('true', apiFaxMessageBlocklist._dncr)
        self.assertEqual('false', apiFaxMessageBlocklist._fps)
        self.assertEqual('false', apiFaxMessageBlocklist._smartblock)
        apiFaxMessageBlocklist = apiFaxMessageList[1].Blocklists
        self.assertEqual('true', apiFaxMessageBlocklist._dncr)
        self.assertEqual('false', apiFaxMessageBlocklist._fps)
        self.assertEqual('false', apiFaxMessageBlocklist._smartblock)
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
        sendFaxRequest.faxMessages = [self.initialize_message(), self.initialize_message()]

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

    def mockClient(self):
        client = ClientWrapper('file:///home/froilan/Documents/ut_2/ut/idea/pymonopond/tests/faxapi-v2.wsdl','user','pass')
        client._client = mock(Client)
        client._client.service = mock(ServiceSelector)
        client._client.factory = mock(Factory)
        return client

    def initialize_document(self):
        document = Document()
        document.fileName = 'test'
        document.fileData = 'VGhpcyBpcyBhbm90aGVyIGZheA=='
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
        documents = [document, document]
        blocklists = self.initialize_blocklist()
        faxMessage.blocklist = blocklists
        faxMessage.documents = documents
        faxMessage.scheduledStartTime = None
        faxMessage.retries = 3
        faxMessage.busyRetries = 4
        faxMessage.headerFormat = "From %from%, To %to%|%a %b %d %H:%M %Y"
        faxMessage.resolution = 'fine'
        return faxMessage

class StubObject:
    pass

if __name__ == '__main__':
    unittest.main()