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

###Encoding base64 string from file

```python
filePath="/home/user/file"
file = open(filePath, "rb")
binary_data = file.read()
file.close()
fileData = base64.b64encode(binary_data)

print fileData # this prints the base64 string

```

###SendFax
SendFax Request allows you to send fax/es on the platform.

####SendFaxRequest Properties:
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
|**fontName** |  | *String* | Font name to be used. See list of support font names [here](#list-of-supported-font-names-for-stampmergefield-textvalue). |
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

####Sending a single fax:

To send a fax to a single destination, a request similar to the following example can be used:

```python
# Setup Document
document = Document()
document.fileName = 'test'
document.fileData = 'base64 string of file' #convert your file to base64 string and place it here
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
document1 = FaxDocument()
document1.documentRef = 'testDocument'
document1.fileName = 'test 1'
document1.fileData = 'base64 string of file' #convert your file to base64 string and place it here
document1.order = 0

# This will save 'test 1' file without any document ref
document2 = FaxDocument()
document2.fileName = 'test 2'
document2.fileData = 'maryhadalittlelamb'
document2.order = 0

# This will get a document with document ref of 'previouslySavedDocument'
document3 = FaxDocument()
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
document.fileData = 'base64 string of file'; #convert your file to base64 string and place it here
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

####Sending a faxStatus Request with “brief” verbosity:

```python
# Setup FaxStatusRequest
faxStatusRequest = FaxStatusRequest()
faxStatusRequest.messageRef = 'test-2-1-1'

# Call Fax Status method
faxStatusResponse = client.faxStatus(faxStatusRequest)
print faxStatusResponse

```
####Status Request with “send” verbosity:

```python
# Setup FaxStatusRequest
faxStatusRequest = FaxStatusRequest()
faxStatusRequest.messageRef = 'test-2-1-1'
faxStatusRequest.verbosity = 'send'

# Call Fax Status method
faxStatusResponse = client.faxStatus(faxStatusRequest)
print faxStatusResponse

```
####Status Request with “details” verbosity:

```python
# Setup FaxStatusRequest
faxStatusRequest = FaxStatusRequest()
faxStatusRequest.messageRef = 'test-2-1-1'
faxStatusRequest.verbosity = 'details'

# Call Fax Status method
faxStatusResponse = client.faxStatus(faxStatusRequest)
print faxStatusResponse

```
####Status Request with “results” verbosity:

```python
# Setup FaxStatusRequest
faxStatusRequest = FaxStatusRequest()
faxStatusRequest.messageRef = 'test-2-1-1'
faxStatusRequest.verbosity = 'results'

# Call Fax Status method
faxStatusResponse = client.faxStatus(faxStatusRequest)
print faxStatusResponse
```
###Response
The response received depends entirely on the verbosity level specified.

**FaxStatusResponse:**

| Name | Type | Verbosity | Description |
| --- | --- | --- | --- |
| **FaxStatusTotals** | *FaxStatusTotals* | *brief* | Counts of how many faxes are at each status. See below for more details. |
| **FaxResultsTotals** | *FaxResultsTotals* | *brief* | FaxResultsTotals FaxResultsTotals brief Totals of the end results of the faxes. See below for more details. |
| **FaxMessages** | *Array of FaxMessage* | *send* | send List of each fax in the query. See below for more details. |

**FaxStatusTotals:**

Contains the total count of how many faxes are at each status. 
To see more information on each fax status, view the FaxStatus table below.

| Name | Type | Verbosity | Description |
| --- | --- | --- | --- |
| **pending** | *Long* | *brief* | Fax is pending on the system and waiting to be processed.|
| **processing** | *Long* | *brief* | Fax is in the initial processing stages. |
| **queued** | *Long* | *brief* | Fax has finished processing and is queued, ready to send out at the send time. |
| **starting** | *Long* | *brief* | Fax is ready to be sent out. |
| **sending** | *Long* | *brief* | Fax has been spooled to our servers and is in the process of being sent out. |
| **finalizing** | *Long* | *brief* | Fax has finished sending and the results are being processed.|
| **done** | *Long* | *brief* | Fax has completed and no further actions will take place. The detailed results are available at this status. |

**FaxResultsTotals:**

Contains the total count of how many faxes ended in each result, as well as some additional totals. To view more information on each fax result, view the FaxResults table below.

| Name | Type | Verbosity | Description |
| --- | --- | --- | --- |
| **success** | *Long* | *brief* | Fax has successfully been delivered to its destination.|
| **blocked** | *Long* |  *brief* | Destination number was found in one of the block lists. |
| **failed** | *Long* | *brief* | Fax failed getting to its destination.|
| **totalAttempts** | *Long* | *brief* |Total attempts made in the reference context.|
| **totalFaxDuration** | *Long* | *brief* |totalFaxDuration Long brief Total time spent on the line in the reference context.|
| **totalPages** | *Long* | *brief* | Total pages sent in the reference context.|


**apiFaxMessageStatus:**

| Name | Type | Verbosity | Description |
| --- | --- | --- | --- |
| **messageRef** | *String* | *send* | |
| **sendRef** | *String* | *send* | |
| **broadcastRef** | *String* | *send* | |
| **sendTo** | *String* | *send* | |
| **status** |  | *send* | The current status of the fax message. See the FaxStatus table above for possible status values. |
| **FaxDetails** | *FaxDetails* | *details* | Contains the details and settings the fax was sent with. See below for more details. |
| **FaxResults** | *Array of FaxResult* | *results* | Contains the results of each attempt at sending the fax message and their connection details. See below for more details. |

**FaxDetails:**

| Name | Type | Verbosity |
| --- | --- | --- | --- |
| **sendFrom** | *Alphanumeric String* | *details* |
| **resolution** | *String* | *details* |
| **retries** | *Integer* | *details* |
| **busyRetries** | *Integer* | *details* |
| **headerFormat** | *String* | *details* |

**FaxResults:**

| Name | Type | Verbosity | Description |
| --- | --- | --- | --- |
| **attempt** | *Integer* | *results* | The attempt number of the FaxResult. |
| **result** | *String* | *results* | The result of the fax message. See the FaxResults table above for all possible results values. |
| **Error** | *FaxError* | *results* |  The fax error code if the fax was not successful. See below for all possible values. |
| **cost** | *BigDecimal* | *results* | The final cost of the fax message. | 
| **pages** | *Integer* | *results* | Total pages sent to the end fax machine. |
| **scheduledStartTime** | *DateTime* | *results* | The date and time the fax is scheduled to start. |
| **dateCallStarted** | *DateTime* | *results* | Date and time the fax started transmitting. |
| **dateCallEnded** | *DateTime* | *results* | Date and time the fax finished transmitting. |

**FaxError:**

| Value | Error Name |
| --- | --- |
| **DOCUMENT_EXCEEDS_PAGE_LIMIT** | Document exceeds page limit |
| **DOCUMENT_UNSUPPORTED** | Unsupported document type |
| **DOCUMENT_FAILED_CONVERSION** | Document failed conversion |
| **FUNDS_INSUFFICIENT** | Insufficient funds |
| **FUNDS_FAILED** | Failed to transfer funds |
| **BLOCK_ACCOUNT** | Number cannot be sent from this account |
| **BLOCK_GLOBAL** | Number found in the Global blocklist |
| **BLOCK_SMART** | Number found in the Smart blocklist |
| **BLOCK_DNCR** | Number found in the DNCR blocklist |
| **BLOCK_CUSTOM** | Number found in a user specified blocklist |
| **FAX_NEGOTIATION_FAILED** | Negotiation failed |
| **FAX_EARLY_HANGUP** | Early hang-up on call |
| **FAX_INCOMPATIBLE_MACHINE** | Incompatible fax machine |
| **FAX_BUSY** | Phone number busy |
| **FAX_NUMBER_UNOBTAINABLE** | Number unobtainable |
| **FAX_SENDING_FAILED** | Sending fax failed |
| **FAX_CANCELLED** | Cancelled |
| **FAX_NO_ANSWER** | No answer |
| **FAX_UNKNOWN** | Unknown fax error |

###SOAP Faults

This function will throw one of the following SOAP faults/exceptions if something went wrong:

**InvalidArgumentsException**, **NoMessagesFoundException**, or **InternalServerException**.
You can find more details on these faults [here](#section5).

##StopFax

###Description
Stops a fax message from sending. This fax message must either be paused, queued, starting or sending. Please note the fax cannot be stopped if the fax is currently in the process of being transmitted to the destination device.

When making a stop request you must provide at least a `BroadcastRef`, `SendRef` or `MessageRef`. The function will also accept a combination of these to further narrow down the request.

###Request
####StopFaxRequest Properties:

| Name | Required | Type | Description |
| --- | --- | --- | --- | --- |
| **BroadcastRef** | | *String* | User-defined broadcast reference. |
| **SendRef** |  | *String* | User-defined send reference. |
| **MessageRef** |  | *String* | User-defined message reference. |

####StopFax Request limiting by BroadcastRef:

```python
# Setup StopFaxRequest
stopFaxRequest = StopFaxRequest()
stopFaxRequest.broadcastRef = 'Broadcast-test-1’

# Call Stop Fax Method
stopFaxResponse = client.stopFax(stopFaxRequest)
print stopFaxResponse
```
####StopFax Request limiting by SendRef:

```python
# Setup StopFaxRequest
stopFaxRequest = StopFaxRequest()
stopFaxRequest.broadcastRef = 'Send-Ref-1’

# Call Stop Fax Method
stopFaxResponse = client.stopFax(stopFaxRequest)
print stopFaxResponse

```

####StopFax Request limiting by MessageRef:

```python
# Setup StopFaxRequest
stopFaxRequest = StopFaxRequest()
stopFaxRequest.messageRef = 'Testing-message-1’

# Call Stop Fax Method
stopFaxResponse = client.stopFax(stopFaxRequest)
print stopFaxResponse

```
###Response
The response received from a `StopFaxRequest` is the same response you would receive when calling the `FaxStatus` method call with the `send` verbosity level.

###SOAP Faults
This function will throw one of the following SOAP faults/exceptions if something went wrong:

**InvalidArgumentsException**, **NoMessagesFoundException**, or **InternalServerException**.
You can find more details on these faults [here](#section5).
##PauseFax

###Description
Pauses a fax message before it starts transmitting. This fax message must either be queued, starting or sending. Please note the fax cannot be paused if the message is currently being transmitted to the destination device.

When making a pause request, you must provide at least a `BroadcastRef`, `SendRef` or `MessageRef`. The function will also accept a combination of these to further narrow down the request. 

###Request
####PauseFaxRequest Properties:
| Name | Required | Type | Description |
| --- | --- | --- | --- |
| **BroadcastRef** | | *String* | User-defined broadcast reference. |
| **SendRef** | | *String* | User-defined send reference. |
| **MessageRef** | | *String* | User-defined message reference. |


###PauseFax Request limiting by BroadcastRef:
```python
# Setup PauseFaxRequest
pauseFaxRequest = PauseFaxRequest()
pauseFaxRequest.broadcastRef = 'Broadcast-test-1'

# Call Pause Fax method
pauseFaxResponse = client.pauseFax(pauseFaxRequest)
print pauseFaxResponse

```
###PauseFax Request limiting by SendRef:
```python
# Setup PauseFaxRequest
pauseFaxRequest = PauseFaxRequest()
pauseFaxRequest.sendRef = 'Send-Ref-1'

# Call Pause Fax method
pauseFaxResponse = client.pauseFax(pauseFaxRequest)
print pauseFaxResponse

```
###PauseFax Request limiting by MessageRef:
```python
# Setup PauseFaxRequest
pauseFaxRequest = PauseFaxRequest()
pauseFaxRequest.messageRef = 'Testing-message-1'

# Call Pause Fax method
pauseFaxResponse = client.pauseFax(pauseFaxRequest)
print pauseFaxResponse
```
###Response
The response received from a `PauseFaxRequest` is the same response you would receive when calling the `FaxStatus` method call with the `send` verbosity level. 

###SOAP Faults
This function will throw one of the following SOAP faults/exceptions if something went wrong:
**InvalidArgumentsException**, **NoMessagesFoundException**, or **InternalServerException**.
You can find more details on these faults in [here](#section5).

##ResumeFax

When making a resume request, you must provide at least a `BroadcastRef`, `SendRef` or `MessageRef`. The function will also accept a combination of these to further narrow down the request. 

###Request
####ResumeFaxRequest Properties:
| Name | Required | Type | Description |
| --- | --- | --- | --- |
| **BroadcastRef** | | *String* | User-defined broadcast reference. |
| **SendRef** | | *String* | User-defined send reference. |
| **MessageRef** | | *String* | User-defined message reference. |

###ResumeFax Request limiting by BroadcastRef:

```python
# Setup Resume Fax request
resumeFaxRequest = ResumeFaxRequest()
resumeFaxRequest.broadcastRef= 'Broadcast-test-1’

# Call Resume Fax method
resumeFaxResponse = client.resumeFax(resumeFaxRequest)
print resumeFaxResponse
```
###ResumeFax Request limiting by SendRef:
```python
# Setup Resume Fax request
resumeFaxRequest = ResumeFaxRequest()
resumeFaxRequest.sendRef= 'Send-ref-1’

# Call Resume Fax method
resumeFaxResponse = client.resumeFax(resumeFaxRequest)
print resumeFaxResponse
```
###ResumeFax Request limiting by MessageRef:
```python
# Setup Resume Fax request
resumeFaxRequest = ResumeFaxRequest()
resumeFaxRequest.messageRef= 'Testing-message-1’

# Call Resume Fax method
resumeFaxResponse = client.resumeFax(resumeFaxRequest)
print resumeFaxResponse
```
##SaveFaxDocument
###Description

This function allows you to upload a document and save it under a document reference (DocumentRef) for later use. (Note: These saved documents only last 30 days on the system.)

###Request
**SaveFaxDocumentRequest Parameters:**

| **Name** | **Required** | **Type** | **Description** |
|--- | --- | --- | --- | ---|
|**DocumentRef**| **X** | *String* | Unique identifier for the document to be uploaded. |
|**FileName**| **X** | *String* | The document filename including extension. This is important as it is used to help identify the document MIME type. |
| **FileData**|**X**| *Base64* |The document encoded in Base64 format.| |

###SOAP Faults
This function will throw one of the following SOAP faults/exceptions if something went wrong:
**DocumentRefAlreadyExistsException**, **DocumentContentTypeNotFoundException**, **InternalServerException**.
You can find more details on these faults in Section 5 of this document.You can find more details on these faults in the next section of this document.


###Saving Fax Document

```python
# Setup save fax document request
saveFaxDocumentRequest = SaveFaxDocumentRequest()
saveFaxDocumentRequest.fileName='testing'
saveFaxDocumentRequest.fileData='base64 string of file'
saveFaxDocumentRequest.documentRef='testing'

# Call save fax document method
client.saveFaxDocument(saveFaxDocumentRequest)

```


##DeleteFaxDocument
###Description

This function removes a saved fax document from the system.

###Request
**DeleteFaxDocumentRequest Parameters:**

| **Name** | **Required** | **Type** | **Description** |
|--- | --- | --- | --- | ---|
|**DocumentRef**| **X** | *String* | Unique identifier for the document to be deleted. |

###SOAP Faults
This function will throw one of the following SOAP faults/exceptions if something went wrong:
**DocumentRefDoesNotExistException**, **InternalServerException**.
You can find more details on these faults in Section 5 of this document.You can find more details on these faults in the next section of this document.

###Deleting fax document:
```python
# Setup delete request
deleteFaxDocumentRequest = DeleteFaxDocumentRequest()
deleteFaxDocumentRequest.documentRef='wasabi'

# Call Delete Fax Document method
client.deleteFaxDocument(deleteFaxDocumentRequest)

```
##PreviewFaxDocument
###Description

This function provides you with a method to generate a preview of a saved document at different resolutions with various dithering settings. It returns a tiff data in base64 along with a page count.

###Request
**FaxDocumentPreviewRequest Parameters:**

| **Name** | **Required** | **Type** | **Description** | **Default** |
|--- | --- | --- | --- | ---|
|**DocumentRef**| **X** | *String* | Unique identifier for the document to be deleted. |
|**Resolution**|  | *Resolution* |Resolution setting of the fax document. Refer to the resolution table below for possible resolution values.| normal |
|**DitheringTechnique**| | *FaxDitheringTechnique* | Applies a custom dithering method to the fax document before transmission. | |
|**DocMergeData** | | *Array of DocMergeData MergeFields* | Each mergefield has a key and a value. The system will look for the keys in a document and replace them with their corresponding value. ||
|**StampMergeData** | | *Array of StampMergeData MergeFields* | Each mergefield has a key a corressponding TextValue/ImageValue. The system will look for the keys in a document and replace them with their corresponding value. | | |

**DocMergeData Mergefield Parameters:**

|**Name** | **Required** | **Type** | **Description** |
|-----|-----|-----|-----|
|**Key** | | *String* | A unique identifier used to determine which fields need replacing. |
|**Value** | | *String* | The value that replaces the key. |

**StampMergeData Mergefield Parameters:**

|**Name** | **Required** | **Type** | **Description** |
|-----|-----|-----|-----|
|**Key** |  | *StampMergeFieldKey* | Contains x and y coordinates where the ImageValue or TextValue should be placed. |
|**TextValue** |  | *StampMergeFieldTextValue* | The text value that replaces the key. |
|**ImageValue** |  | *StampMergeFieldImageValue* | The image value that replaces the key. |

 **StampMergeFieldKey Parameters:**

| **Name** | **Required** | **Type** | **Description** |
|----|-----|-----|-----|
| **xCoord** |  | *Int* | X coordinate. |
| **yCoord** |  | *Int* | Y coordinate. |

**StampMergeFieldTextValue Parameters:**

|**Name** | **Required** | **Type** | **Description** |
|-----|-----|-----|-----|
|**fontName** |  | *String* | Font name to be used. See list of support font names [here](#list-of-supported-font-names-for-stampmergefield-textvalue). |
|**fontSize** |  | *Decimal* | Font size to be used. |

**StampMergeFieldImageValue Parameters:**

|**Name** | **Required** | **Type** | **Description** |
|-----|-----|-----|-----|
|**fileName** |  | *String* | The document filename including extension. This is important as it is used to help identify the document MIME type. |
|**fileData** |  | *Base64* | The document encoded in Base64 format. |

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

####Sending FaxDocumentPreview 

```python
# Setup Requests
faxDocumentPreviewRequest = FaxDocumentPreviewRequest()

# Document Ref of the document you want to see.
faxDocumentPreviewRequest.documentRef='txtRef'
faxDocumentPreviewRequest.ditheringTechnique='fine'
faxDocumentPreviewRequest.resolution='normal'

#Call the faxDocument preview method
faxDocumentPreviewResponse = client.faxDocumentPreview(faxDocumentPreviewRequest)

```
Note that Document ref should be previously saved. Either by SaveFaxDocumentRequest or by adding a document ref in SendFax.

####Sending FaxDocumentPreview with doc merge fields

```python
# Setup Merge fields
docMergeData = DocMergeData()
docMergeData.key='key'
docMergeData.value='value'

# Setup Requests
faxDocumentPreviewRequest = FaxDocumentPreviewRequest()

# Document Ref of the document you want to see.
faxDocumentPreviewRequest.documentRef='docxRef'
faxDocumentPreviewRequest.addDocMergeData(docMergeData)

#Call the faxDocument preview method
faxDocumentPreviewResponse = client.faxDocumentPreview(faxDocumentPreviewRequest)

```
The sample above shows a preview of a document with doc merge data. This works the same with using merge Fields in SendFax. 

####Sending FaxDocumentPreview with stamp merge fields

```python
# Setup Merge fields
imageStampMergeData = ImageStampMergeData()
imageStampMergeData.fileData="base64 string of file"
imageStampMergeData.keyXCoord="283"
imageStampMergeData.keyYCoord="175"
imageStampMergeData.fileName="corgi.jpg"
imageStampMergeData.width="120"
imageStampMergeData.height="130"

textStampMergeData = TextStampMergeData()
textStampMergeData.textValue='some dude'
textStampMergeData.keyXCoord="424"
textStampMergeData.keyYCoord="844"
textStampMergeData.fontName='Times-Roman'

# Setup Requests
faxDocumentPreviewRequest = FaxDocumentPreviewRequest()

# Document Ref of the document you want to see.
faxDocumentPreviewRequest.documentRef='pdfRef'
faxDocumentPreviewRequest.addStampMergeData(imageStampMergeData)
faxDocumentPreviewRequest.addStampMergeData(textStampMergeData)

#Call the faxDocument preview method
faxDocumentPreviewResponse = client.faxDocumentPreview(faxDocumentPreviewRequest)

```
The sample above shows a preview of a document with stamp merge data. This works the same with using merge Fields in SendFax.

###Response
**FaxDocumentPreviewResponse**

**Name** | **Type** | **Description** 
-----|-----|-----
**TiffPreview** | *String* | A preview version of the document encoded in Base64 format. 
**NumberOfPages** | *Int* | Total number of pages in the document preview.

###SOAP Faults
This function will throw one of the following SOAP faults/exceptions if something went wrong:
**DocumentRefDoesNotExistException**, **InternalServerException**, **UnsupportedDocumentContentType**, **MergeFieldDoesNotMatchDocumentTypeException**, **UnknownHostException**.
You can find more details on these faults in Section 5 of this document.You can find more details on these faults in the next section of this document.

## List of Supported font names for StampMergeField TextValue
```
Andale-Mono-Regular
Arial-Black-Regular
Arial-Bold
Arial-Bold-Italic
Arial-Italic
Arial-Regular
AvantGarde-Book
AvantGarde-BookOblique
AvantGarde-Demi
AvantGarde-DemiOblique
Bitstream-Charter-Bold
Bitstream-Charter-Bold-Italic
Bitstream-Charter-Italic
Bitstream-Charter-Regular
Bitstream-Vera-Sans-Bold
Bitstream-Vera-Sans-Bold-Oblique
Bitstream-Vera-Sans-Mono-Bold
Bitstream-Vera-Sans-Mono-Bold-Oblique
Bitstream-Vera-Sans-Mono-Oblique
Bitstream-Vera-Sans-Mono-Roman
Bitstream-Vera-Sans-Oblique
Bitstream-Vera-Sans-Roman
Bitstream-Vera-Serif-Bold
Bitstream-Vera-Serif-Roman
Bookman-Demi
Bookman-DemiItalic
Bookman-Light
Bookman-LightItalic
Century-Schoolbook-Bold
Century-Schoolbook-Bold-Italic
Century-Schoolbook-Italic
Century-Schoolbook-Roman
Comic-Sans-MS-Bold
Comic-Sans-MS-Regular
Courier
Courier-Bold
Courier-BoldOblique
Courier-New-Bold
Courier-New-Bold-Italic
Courier-New-Italic
Courier-New-Regular
Courier-Oblique
Dingbats-Regular
Georgia-Bold
Georgia-Bold-Italic
Georgia-Italic
Georgia-Regular
Helvetica
Helvetica-Bold
Helvetica-BoldOblique
Helvetica-Narrow
Helvetica-Narrow-Bold
Helvetica-Narrow-BoldOblique
Helvetica-Narrow-Oblique
Helvetica-Oblique
Impact-Regular
NewCenturySchlbk-Bold
NewCenturySchlbk-BoldItalic
NewCenturySchlbk-Italic
NewCenturySchlbk-Roman
Nimbus-Mono-Bold
Nimbus-Mono-Bold-Oblique
Nimbus-Mono-Regular
Nimbus-Mono-Regular-Oblique
Nimbus-Roman-No9-Bold
Nimbus-Roman-No9-Bold-Italic
Nimbus-Roman-No9-Regular
Nimbus-Roman-No9-Regular-Italic
Nimbus-Sans-Bold
Nimbus-Sans-Bold-Italic
Nimbus-Sans-Condensed-Bold
Nimbus-Sans-Condensed-Bold-Italic
Nimbus-Sans-Condensed-Regular
Nimbus-Sans-Condensed-Regular-Italic
Nimbus-Sans-Regular
Nimbus-Sans-Regular-Italic
Palatino-Bold
Palatino-BoldItalic
Palatino-Italic
Palatino-Roman
Standard-Symbols-Regular
Symbol
Tahoma-Regular
Times-Bold
Times-BoldItalic
Times-Italic
Times-New-Roman-Bold
Times-New-Roman-Bold-Italic
Times-New-Roman-Italic
Times-New-Roman-Regular
Times-Roman
Trebuchet-MS-Bold
Trebuchet-MS-Bold-Italic
Trebuchet-MS-Italic
Trebuchet-MS-Regular
URW-Bookman-Demi-Bold
URW-Bookman-Demi-Bold-Italic
URW-Bookman-Light
URW-Bookman-Light-Italic
URW-Chancery-Medium-Italic
URW-Gothic-Book
URW-Gothic-Book-Oblique
URW-Gothic-Demi
URW-Gothic-Demi-Oblique
URW-Palladio-Bold
URW-Palladio-Bold-Italic
URW-Palladio-Italic
URW-Palladio-Roman
Utopia-Bold
Utopia-Bold-Italic
Utopia-Italic
Utopia-Regular
Verdana-Bold
Verdana-Bold-Italic
Verdana-Italic
Verdana-Regular
Webdings-Regular
```
