fax-api-client-python
=====================

Monopond Fax API Python Client

###Overview:

* This is a soap web serice client for monopond web serivces built on top of Suds.

* Requires Suds web services Client to be installed.(https://fedorahosted.org/suds/wiki/Documentation)

* Provides concrete classes that you can use to map values to requests and read responses.

###Logging:

* Raw xml requests/response are automatically printed out

* For suds api logging, use this:

```python
   import logging
    logging.basicConfig(level=logging.INFO)
```

###Basic Usage:

* Install python monopond client by running 'pymonopond/setup.py':

```bash
'python setup.py'
```

* ClientWrapper - the client object that hold the methods to send requests.
Request methods:(sendFax, faxStatus, pauseFax, resumeFax, stopFax, deleteFaxDocument, faxDocumentPreview)

###Building A Request

To use Monopond SOAP Python Client, start by including the monopond_python_client.py then creating an instance of the client by supplying your credentials (line 5). Your username and password should be enclosed in quotation marks.

```python
from pymonopond.monopond_python_client import *

# Enter your own credentials here
client = ClientWrapper('http://192.168.1.35:8000/fax/soap/v2?wsdl','username','password')

# Setup your request here
```
###SendFax
SendFax Request allows you to send fax/es on the platform.

####Sending a single fax:

To send a fax to a single destination, a request similar to the following example can be used:

```python
# Setup Document
document = Document()
document.fileName = 'test'
document.fileData = 'thequickbrownfoxjumpsoverthelazydog'
document.order = 0

# Setup FaxMessage
faxMessage = FaxMessage()
faxMessage.messageRef = 'Testing-message-1'
faxMessage.sendTo = '61011111111'
faxMessage.sendFrom = 'Test Fax'
faxMessage.addDocument(document)
faxMessage.resolution = 'normal'
faxMessage.retries = 0
faxMessage.busyRetries = 2

# Setup FaxSendRequest
sendFaxRequest = SendFaxRequest()
sendFaxRequest.resolution='fine
sendFaxRequest.broadcastRef = '123
sendFaxRequest.sendRef='test-2-1
sendFaxRequest.headerFormat='test
sendFaxRequest.retries=0
sendFaxRequest.headerFormat='1-1-1
sendFaxRequest.addFaxMessage(faxMessage)
sendFaxRequest.addDocument(document)

# Call Send Fax method
clientResponse = client.sendFax(sendFaxRequest)
print clientResponse
```
####Sending multiple faxes:

To send faxes to multiple destinations, a request similar to the following example can be used. Please note the addition of another “FaxMessage”:

```python

# Setup Document in 3 ways.
# This will save 'test 1' file with document ref 'testDocument'
document1 = Document()
document1.documentRef = 'testDocument'
document1.fileName = 'test 1'
document1.fileData = 'thequickbrownfoxjumpsoverthelazydog'
document1.order = 0

# This will save 'test 1' file without any document ref
document2 = Document()
document2.fileName = 'test 2'
document2.fileData = 'maryhadalittlelamb'
document2.order = 0

# This will get a document with document ref of 'previouslySavedDocument'
document3 = Document()
document2.documentRef = 'previouslySavedDocument'
document3.order = 0

# Setup FaxMessage
faxMessage = FaxMessage()
faxMessage.messageRef = 'Testing-message-1'
faxMessage.sendTo = '61011111111'
faxMessage.sendFrom = 'Test Fax'
faxMessage.addDocument(document1)
faxMessage.resolution = 'normal'
faxMessage.retries = 0
faxMessage.busyRetries = 2

faxMessage2 = FaxMessage()
faxMessage2.messageRef = 'Testing-message-2'
faxMessage2.sendTo = '61011111123'
faxMessage2.sendFrom = 'Test Fax 2'
faxMessage2.addDocument(document2)
faxMessage2.addDocument(document3)
faxMessage2.resolution = 'fine'
faxMessage2.retries = 0
faxMessage2.busyRetries = 1

# Setup FaxSendRequest
sendFaxRequest = SendFaxRequest()
sendFaxRequest.resolution='fine'
sendFaxRequest.broadcastRef = '123'
sendFaxRequest.sendRef='test-2-1'
sendFaxRequest.headerFormat='test'
sendFaxRequest.retries=0
sendFaxRequest.headerFormat='1-1-1'
sendFaxRequest.addFaxMessages(faxMessage)
sendFaxRequest.addFaxMessages(faxMessage2)
sendFaxRequest.addDocument(document)

# Call Send Fax method
clientResponse = client.sendFax(sendFaxRequest)
print clientResponse

```

####Sending faxes to multiple destinations with the same document (broadcasting):

To send the same fax content to multiple destinations (broadcasting), a request similar to the example below can be used.
This method is recommended for broadcasting as it takes advantage of the multiple tiers in the send request. This eliminates the repeated parameters out of the individual fax message elements which are instead inherited from the parent send fax request.

```python

#Setup Document
document = Document();
document.fileName = "AnyFileName1.txt";
document.fileData = $filedata;
document.order = 0;

#Setup FaxMessage
faxMessage = FaxMessage();
faxMessage.messageRef = 'Testing-message-1';
faxMessage.sendTo = '61011111111';
faxMessage.sendFrom = 'Test Fax';
faxMessage.addDocument(document);
faxMessage.resolution = 'normal';
faxMessage.retries = 0;
faxMessage.busyRetries = 2;

faxMessage2 = FaxMessage();
faxMessage2.messageRef = 'Testing-message-2';
faxMessage2.sendTo = '61011111123';
faxMessage2.sendFrom = 'Test Fax 2';
faxMessage2.addDocument(document);
faxMessage2.resolution = 'fine';
faxMessage2.retries = 0;
faxMessage2.busyRetries = 1;

#Setup FaxSendRequest
sendFaxRequest = SendFaxRequest();
sendFaxRequest.resolution='fine'
sendFaxRequest.broadcastRef = '123'
sendFaxRequest.sendRef='test-2-1'
sendFaxRequest.headerFormat='test'
sendFaxRequest.retries=0
sendFaxRequest.headerFormat='1-1-1'
sendFaxRequest.addFaxMessages(faxMessage);
sendFaxRequest.addFaxMessages(faxMessage2);
sendFaxRequest.addDocument(document);

# Call Send Fax method
clientResponse = client.sendFax(sendFaxRequest);
print clientResponse

```
When sending multiple faxes in batch it is recommended to group them into requests of around 600 fax messages for optimal performance. If you are sending the same document to multiple destinations it is strongly advised to only attach the document once in the root of the send request rather than attaching a document for each destination.

####Sending Microsoft Documents With DocMergeData:
(This request only works in version 2.1(or higher) of the fax-api.)

This request is used to send a Microsoft document with replaceable variables or merge fields. The merge field follows the pattern ```<mf:key>```.  If your key is ```field1```, it should be typed as ```<mf:field1>``` in the document. Note that the key must be unique within the whole document. The screenshots below are examples of what the request does.

![before](https://github.com/Monopond/fax-api/raw/master/img/DocMergeData/before.png)

This is what the file looks like after the fields ```field1```,```field2``` and ```field3``` have been replaced with values ```lazy dog```, ```fat pig``` and ```fat pig```:

![stamp](https://github.com/Monopond/fax-api/raw/master/img/DocMergeData/after.png)

##### Sample Request
The example below shows ```field1``` will be replaced by the value of ```Test```.

```python
# setup doc merge data
docMergeData = DocMergeData()
docMergeData.key='field1'
docMergeData.value='Test'

# setup fax document, must be microsoft document
document = FaxDocument()
document.fileName = 'sampleFile.docx'
document.faxDitheringTechnique='normal'
document.fileData = 'base64String of sampleFile.docx' #convert your file to base64 string and place it here

# adds the doc merge data to the document, you can have multiple docMergeData per document 
document.addDocMergeData(docMergeData)

faxMessage = FaxMessage()
faxMessage.messageRef = 'test-2-1-1'
faxMessage.sendTo = '61280039890'
faxMessage.sendFrom = '123'
faxMessage.scheduledStartTime = None
faxMessage.retries = 3
faxMessage.busyRetries = 4
faxMessage.headerFormat = "From %from%, To %to%|%a %b %d %H:%M %Y"
faxMessage.resolution = 'fine'


sendFaxRequest = SendFaxRequest()
sendFaxRequest.addFaxMessage(faxMessage)
sendFaxRequest.addDocument(document)
sendFaxRequest.resolution="fine"
sendFaxRequest.broadcastRef = "123"
sendFaxRequest.sendRef="test-2-1"
sendFaxRequest.headerFormat="test"
sendFaxRequest.retries=0
sendFaxRequest.headerFormat="1-1-1"

clientResponse = client.sendFax(sendFaxRequest);
print clientResponse

```
####Sending Tiff and PDF files with StampMergeData:
(This request only works in version 2.1(or higher) of the fax-api.)

This request allows a PDF or TIFF file to be stamped with an image or text, based on X-Y coordinates. The x and y coordinates (0,0) starts at the top left part of the document. The screenshots below are examples of what the request does.

Original tiff file:

![before](https://github.com/Monopond/fax-api/raw/master/img/StampMergeData/image_stamp/before.png)

Sample stamp image:

![stamp](https://github.com/Monopond/fax-api/raw/master/img/StampMergeData/image_stamp/stamp.png)

This is what the tiff file looks like after stamping it with the image above:

![after](https://github.com/Monopond/fax-api/raw/master/img/StampMergeData/image_stamp/after.png) 

The same tiff file, but this time, with a text stamp:

![after](https://github.com/Monopond/fax-api/raw/master/img/StampMergeData/text_stamp/after.png) 

##### Sample Request

The example below shows a PDF that will be stamped with the text “Hello” at xCoord=“1287” and yCoord=“421”, and an image at xCoord=“283” and yCoord=“120”


```python

textStampMergeData = TextStampMergeData()
textStampMergeData.textValue='Hello'
textStampMergeData.keyXCoord="1287"
textStampMergeData.keyYCoord="421"
textStampMergeData.fontName='Times-Roman'

document = FaxDocument()
document.fileName = 'sampleFile.docx'
document.faxDitheringTechnique='normal'
document.fileData = 'base64String of sampleFile.docx' #convert your file to base64 string and place it here

#add stamp merge data to document
document.addStampMergeData(textStampMergeData)

faxMessage = FaxMessage()
faxMessage.messageRef = 'test-2-1-1'
faxMessage.sendTo = '61280039890'
faxMessage.sendFrom = '123'
faxMessage.scheduledStartTime = None
faxMessage.retries = 3
faxMessage.busyRetries = 4
faxMessage.headerFormat = "From %from%, To %to%|%a %b %d %H:%M %Y"
faxMessage.resolution = 'fine'

sendFaxRequest = SendFaxRequest()
sendFaxRequest.addFaxMessage(faxMessage)
sendFaxRequest.addDocument(document)
sendFaxRequest.resolution="fine"
sendFaxRequest.broadcastRef = "123"
sendFaxRequest.sendRef="test-2-1"
sendFaxRequest.headerFormat="test"
sendFaxRequest.retries=0
sendFaxRequest.headerFormat="1-1-1"

clientResponse = client.sendFax(sendFaxRequest);
print clientResponse

```

```python

imageStampMergeData = ImageStampMergeData()
imageStampMergeData.fileData = base64String of sampleFile.docx' #convert your file to base64 string and place it here
imageStampMergeData.keyXCoord="283"
imageStampMergeData.keyYCoord="120"
imageStampMergeData.fileName="classified.jpg"
imageStampMergeData.width="120"
imageStampMergeData.height="130"

document = FaxDocument()
document.fileName = 'sampleFile.docx'
document.faxDitheringTechnique='normal'
document.fileData = 'base64String of sampleFile.docx' #convert your file to base64 string and place it here

#add stamp merge data to document
document.addStampMergeData(imageStampMergeData)

faxMessage = FaxMessage()
faxMessage.messageRef = 'test-2-1-1'
faxMessage.sendTo = '61280039890'
faxMessage.sendFrom = '123'
faxMessage.scheduledStartTime = None
faxMessage.retries = 3
faxMessage.busyRetries = 4
faxMessage.headerFormat = "From %from%, To %to%|%a %b %d %H:%M %Y"
faxMessage.resolution = 'fine'

sendFaxRequest = SendFaxRequest()
sendFaxRequest.addFaxMessage(faxMessage)
sendFaxRequest.addDocument(document)
sendFaxRequest.resolution="fine"
sendFaxRequest.broadcastRef = "123"
sendFaxRequest.sendRef="test-2-1"
sendFaxRequest.headerFormat="test"
sendFaxRequest.retries=0
sendFaxRequest.headerFormat="1-1-1"

clientResponse = client.sendFax(sendFaxRequest);
print clientResponse


```
###SendFaxRequest Parameters:
**Name**|**Required**|**Type**|**Description**|**Default**
-----|-----|-----|-----|-----
**BroadcastRef**||String|Allows the user to tag all faxes in this request with a user-defined broadcastreference. These faxes can then be retrieved at a later point based on this reference.|
**SendRef**||String|Similar to the BroadcastRef, this allows the user to tag all faxes in this request with a send reference. The SendRef is used to represent all faxes in this request only, so naturally it must be unique.|
**FaxMessages**|**X**| Array of FaxMessage |FaxMessages describe each individual fax message and its destination. See below for details.|
**SendFrom**||Alphanumeric String|A customisable string used to identify the sender of the fax. Also known as the Transmitting Subscriber Identification (TSID). The maximum string length is 32 characters|Fax
**Documents**|**X**|Array of FaxDocument|Each FaxDocument object describes a fax document to be sent. Multiple documents can be defined here which will be concatenated and sent in the same message. See below for details.|
**Resolution**||Resolution|Resolution setting of the fax document. Refer to the resolution table below for possible resolution values.|normal
**ScheduledStartTime**||DateTime|The date and time the transmission of the fax will start.|Current time (immediate sending)
**Blocklists**||Blocklists|The blocklists that will be checked and filtered against before sending the message. See below for details.WARNING: This feature is inactive and non-functional in this (2.1) version of the Fax API.|
**Retries**||Unsigned Integer|The number of times to retry sending the fax if it fails. Each account has a maximum number of retries that can be changed by consultation with your account manager.|Account Default
**BusyRetries**||Unsigned Integer|Certain fax errors such as “NO_ANSWER” or “BUSY” are not included in the above retries limit and can be set separately. Each account has a maximum number of busy retries that can be changed by consultation with your account manager.|Account default
**HeaderFormat**||String|Allows the header format that appears at the top of the transmitted fax to be changed. See below for an explanation of how to format this field.| From: X, To: X
**MustBeSentBeforeDate** | | DateTime |  Specifies a time the fax must be delivered by. Once the specified time is reached the fax will be cancelled across the system. | 
**MaxFaxPages** | | Unsigned Integer |  Sets a limit on the amount of pages allowed in a single fax transmission. Especially useful if the user is blindly submitting their customer's documents to the platform. | 20

***FaxMessage Parameters:***
This represents a single fax message being sent to a destination.

**Name** | **Required** | **Type** | **Description** | **Default** 
-----|-----|-----|-----|-----
**MessageRef** | **X** | String | A unique user-provided identifier that is used to identify the fax message. This can be used at a later point to retrieve the results of the fax message. |
**SendTo** | **X** | String | The phone number the fax message will be sent to. |
**SendFrom** | | Alphanumeric String | A customisable string used to identify the sender of the fax. Also known as the Transmitting Subscriber Identification (TSID). The maximum string length is 32 characters | Empty
**Documents** | **X** | Array of FaxDocument | Each FaxDocument object describes a fax document to be sent. Multiple documents can be defined here which will be concatenated and sent in the same message. See below for details. | 
**Resolution** | | Resolution|Resolution setting of the fax document. Refer to the resolution table below for possible resolution values.| normal
**ScheduledStartTime** | | DateTime | The date and time the transmission of the fax will start. | Start now
**Blocklists** | | Blocklists | The blocklists that will be checked and filtered against before sending the message. See below for details. WARNING: This feature is inactive and non-functional in this (2.1) version of the Fax API. |
**Retries** | | Unsigned Integer | The number of times to retry sending the fax if it fails. Each account has a maximum number of retries that can be changed by consultation with your account manager. | Account Default
**BusyRetries** | | Unsigned Integer | Certain fax errors such as “NO_ANSWER” or “BUSY” are not included in the above retries limit and can be set separately. Please consult with your account manager in regards to maximum value.|account default
**HeaderFormat** | | String | Allows the header format that appears at the top of the transmitted fax to be changed. See below for an explanation of how to format this field. | From： X, To: X
**MustBeSentBeforeDate** | | DateTime |  Specifies a time the fax must be delivered by. Once the specified time is reached the fax will be cancelled across the system. | 
**MaxFaxPages** | | Unsigned Integer |  Sets a limit on the amount of pages allowed in a single fax transmission. Especially useful if the user is blindly submitting their customer's documents to the platform. | 20
**CLI**| | String| Allows a customer called ID. Note: Must be enabled on the account before it can be used.

***FaxDocument Parameters:***
Represents a fax document to be sent through the system. Supported file types are: PDF, TIFF, PNG, JPG, GIF, TXT, PS, RTF, DOC, DOCX, XLS, XLSX, PPT, PPTX.

**Name**|**Required**|**Type**|**Description**|**Default**
-----|-----|-----|-----|-----
**FileName**|**X**|String|The document filename including extension. This is important as it is used to help identify the document MIME type.|
**FileData**|**X**|Base64|The document encoded in Base64 format.|
**Order** | | Integer|If multiple documents are defined on a message this value will determine the order in which they will be transmitted.|0
**DitheringTechnique** | | FaxDitheringTechnique | Applies a custom dithering method to their fax document before transmission. | 
**DocMergeData**|||An Array of MergeFields|
**StampMergeData**|||An Array of MergeFields|

**FaxDitheringTechnique:**

| Value | Fax Dithering Technique |
| --- | --- |
| **none** | No dithering. |
| **normal** | Normal dithering.|
| **turbo** | Turbo dithering.|
| **darken** | Darken dithering.|
| **darken_more** | Darken more dithering.|
| **darken_extra** | Darken extra dithering.|
| **ligthen** | Lighten dithering.|
| **lighten_more** | Lighten more dithering. |
| **crosshatch** | Crosshatch dithering. |
| **DETAILED** | Detailed dithering. |

**Resolution Levels:**

| **Value** | **Description** |
| --- | --- |
| **normal** | Normal standard resolution (98 scan lines per inch) |
| **fine** | Fine resolution (196 scan lines per inch) |

***Header Format:iff***
Determines the format of the header line that is printed on the top of the transmitted fax message.
This is set to **rom %from%, To %to%|%a %b %d %H:%M %Y”**y default which produces the following:

From TSID, To 61022221234 Mon Aug 28 15:32 2012 1 of 1

**Value** | **Description**
--- | ---
**%from%**|The value of the **SendFrom** field in the message.
**%to%**|The value of the **SendTo** field in the message.
**%a**|Weekday name (abbreviated)
**%A**|Weekday name
**%b**|Month name (abbreviated)
**%B**|Month name
**%d**|Day of the month as a decimal (01 – 31)
**%m**|Month as a decimal (01 – 12)
**%y**|Year as a decimal (abbreviated)
**%Y**|Year as a decimal
**%H**|Hour as a decimal using a 24-hour clock (00 – 23)
**%I**|Hour as a decimal using a 12-hour clock (01 – 12)
**%M**|Minute as a decimal (00 – 59)
**%S**|Second as a decimal (00 – 59)
**%p**|AM or PM
**%j**|Day of the year as a decimal (001 – 366)
**%U**|Week of the year as a decimal (Monday as first day of the week) (00 – 53)
**%W**|Day of the year as a decimal (001 – 366)
**%w**|Day of the week as a decimal (0 – 6) (Sunday being 0)
**%%**|A literal % character

TODO: The default value is set to: “From %from%, To %to%|%a %b %d %H:%M %Y”

<a name="docMergeDataParameters"></a> 

**DocMergeData Mergefield Properties:**

|**Name** | **Required** | **Type** | **Description** |
|-----|-----|-----|-----|
|**Key** | | *String* | A unique identifier used to determine which fields need replacing. |
|**Value** | | *String* | The value that replaces the key. |

<a name="stampMergeDataParameters"></a> 
**StampMergeData Mergefield Properties:**

|**Name** | **Required** | **Type** | **Description** |
|-----|-----|-----|-----|
|**Key** |  | *StampMergeFieldKey* | Contains x and y coordinates where the ImageValue or TextValue should be placed. |
|**TextValue** |  | *StampMergeFieldTextValue* | The text value that replaces the key. |
|**ImageValue** |  | *StampMergeFieldImageValue* | The image value that replaces the key. |

 **StampMergeFieldKey Properties:**

| **Name** | **Required** | **Type** | **Description** |
|----|-----|-----|-----|
| **xCoord** |  | *Int* | X coordinate. |
| **yCoord** |  | *Int* | Y coordinate. |

**StampMergeFieldTextValue Properties:**

|**Name** | **Required** | **Type** | **Description** |
|-----|-----|-----|-----|
|**fontName** |  | *String* | Font name to be used. |
|**fontSize** |  | *Decimal* | Font size to be used. |

**StampMergeFieldImageValue Properties:**

|**Name** | **Required** | **Type** | **Description** |
|-----|-----|-----|-----|
|**fileName** |  | *String* | The document filename including extension. This is important as it is used to help identify the document MIME type. |
|**fileData** |  | *Base64* | The document encoded in Base64 format. |

###Response
The response received from a `SendFaxRequest` matches the response you receive when calling the `FaxStatus` method call with a `send` verbosity level.

###SOAP Faults
This function will throw one of the following SOAP faults/exceptions if something went wrong:
**InvalidArgumentsException, NoMessagesFoundException, DocumentContentTypeNotFoundException, or InternalServerException.**
You can find more details on these faults [here](#section5).

##FaxStatus
###Description

This function provides you with a method of retrieving the status, details and results of fax messages sent. While this is a legitimate method of retrieving results we strongly advise that you take advantage of our callback service, which will push these fax results to you as they are completed.

When making a status request, you must provide at least a `BroadcastRef`, `SendRef` or `MessageRef`. The 
function will also accept a combination of these to further narrow the request query.
- Limiting by a `BroadcastRef` allows you to retrieve faxes contained in a group of send requests.
- Limiting by `SendRef` allows you to retrieve faxes contained in a single send request.
- Limiting by `MessageRef` allows you to retrieve a single fax message.

There are multiple levels of verbosity available in the request; these are explained in detail below.

**FaxStatusRequest Properties:**

| **Name** | **Required** | **Type** | **Description** |
|--- | --- | --- | --- | ---|
|**BroadcastRef**|  | *String* | User-defined broadcast reference. |
|**SendRef**|  | *String* | User-defined send reference. |
|**MessageRef**|  | *String* | User-defined message reference. |
|**Verbosity**|  | *String* | Verbosity String The level of detail in the status response. Please see below for a list of possible values.| |

**Verbosity Levels:**	
  
| **Value** | **Description** |
| --- | --- |
| **brief** | Gives you an overall view of the messages. This simply shows very high-level statistics, consisting of counts of how many faxes are at each status (i.e. processing, queued,sending) and totals of the results of these faxes (success, failed, blocked). |
| **send** | send Includes the results from ***“brief”*** while also including an itemised list of each fax message in the request. |
| **details** | details Includes the results from ***“send”*** along with details of the properties used to send the fax messages. |
| **results** |Includes the results from ***“send”*** along with the sending results of the fax messages. |
| **all** | all Includes the results from both ***“details”*** and ***“results”*** along with some extra uncommon fields. |

###Sending a faxStatus Request with “brief” verbosity:
```




