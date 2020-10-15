from ._5 import *

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListCompanyActiveCallsResponseRecordsItemLegsItemMessage(DataClassJsonMixin):
    """ Linked message (Fax/Voicemail) """
    
    id: Optional[str] = None
    """ Internal identifier of a message """
    
    type: Optional[str] = None
    """ Type of a message """
    
    uri: Optional[str] = None
    """ Link to a message resource """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListCompanyActiveCallsResponseRecordsItemLegsItem(DataClassJsonMixin):
    action: Optional[ListCompanyActiveCallsResponseRecordsItemLegsItemAction] = None
    """ Action description of the call operation """
    
    direction: Optional[ListCompanyActiveCallsResponseRecordsItemLegsItemDirection] = None
    """ Call direction """
    
    billing: Optional[ListCompanyActiveCallsResponseRecordsItemLegsItemBilling] = None
    """ Billing information related to the call """
    
    delegate: Optional[ListCompanyActiveCallsResponseRecordsItemLegsItemDelegate] = None
    """
    Information on a delegate extension that actually implemented a call action. For Secretary call
    log the field is returned if the current extension implemented a call. For Boss call log the
    field contains information on a Secretary extension which actually implemented a call on behalf
    of the current extension
    """
    
    extension_id: Optional[str] = None
    """ Internal identifier of an extension """
    
    duration: Optional[int] = None
    """ Call duration in seconds """
    
    extension: Optional[ListCompanyActiveCallsResponseRecordsItemLegsItemExtension] = None
    """ Information on extension """
    
    leg_type: Optional[ListCompanyActiveCallsResponseRecordsItemLegsItemLegType] = None
    """ Leg type """
    
    start_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """
    The call start datetime in (ISO 8601)[https://en.wikipedia.org/wiki/ISO_8601] format including
    timezone, for example 2016-03-10T18:07:52.534Z
    """
    
    type: Optional[ListCompanyActiveCallsResponseRecordsItemLegsItemType] = None
    """ Call type """
    
    result: Optional[ListCompanyActiveCallsResponseRecordsItemLegsItemResult] = None
    """ Status description of the call operation """
    
    reason: Optional[ListCompanyActiveCallsResponseRecordsItemLegsItemReason] = None
    """
    Reason of a call result:
    
    * `Accepted` - The call was connected to and accepted by this number
    
    * `Connected` - The call was answered, but there was no response on how to handle the call (for
    example, a voice mail system answered the call and did not push "1" to accept)
    
    * `Line Busy` - The phone number you dialed was busy
    
    * `Not Answered` - The phone number you dialed was not answered
    
    * `No Answer` - You did not answer the call
    
    * `Hang Up` - The caller hung up before the call was answered
    
    * `Stopped` - This attempt was stopped because the call was answered by another phone
    
    * `Internal Error` - An internal error occurred when making the call. Please try again
    
    * `No Credit` - There was not enough Calling Credit on your account to make this call
    
    * `Restricted Number` - The number you dialed is restricted by RingCentral
    
    * `Wrong Number` - The number you dialed has either been disconnected or is not a valid phone
    number. Please check the number and try again
    
    * `International Disabled` - International calling is not enabled on your account. Contact
    customer service to activate International Calling
    
    * `International Restricted` - The country and/or area you attempted to call has been
    prohibited by your administrator
    
    * `Bad Number` - An error occurred when making the call. Please check the number before trying
    again
    
    * `Info 411 Restricted` - Calling to 411 Information Services is restricted
    
    * `Customer 611 Restricted` - 611 customer service is not supported. Please contact customer
    service at <(888) 555-1212>
    
    * `No Digital Line` - This DigitalLine was either not plugged in or did not have an internet
    connection
    
    * `Failed Try Again` - Call failed. Please try again
    
    * `Max Call Limit` - The number of simultaneous calls to your account has reached its limit
    
    * `Too Many Calls` - The number of simultaneous calls for per DigitalLine associated with Other
    Phone has reached its limit. Please contact customer service
    
    * `Calls Not Accepted` - Your account was not accepting calls at this time
    
    * `Number Not Allowed` - The number that was dialed to access your account is not allowed
    
    * `Number Blocked` - This number is in your Blocked Numbers list
    
    * `Number Disabled` - The phone number and/or area you attempted to call has been prohibited by
    your administrator
    
    * `Resource Error` - An error occurred when making the call. Please try again
    
    * `Call Loop` - A call loop occurred due to an incorrect call forwarding configuration. Please
    check that you are not forwarding calls back to your own account
    
    * `Fax Not Received` - An incoming fax could not be received because a proper connection with
    the sender's fax machine could not be established
    
    * `Fax Partially Sent` - The fax was only partially sent. Possible explanations include phone
    line quality to poor to maintain the connection or the call was dropped
    
    * `Fax Not Sent` - An attempt to send the fax was made, but could not connect with the
    receiving fax machine
    
    * `Fax Poor Line` - An attempt to send the fax was made, but the phone line quality was too
    poor to send the fax
    
    * `Fax Prepare Error` - An internal error occurred when preparing the fax. Please try again
    
    * `Fax Save Error` - An internal error occurred when saving the fax. Please try again
    
    * `Fax Send Error` - An error occurred when sending the fax. Please try again
    """
    
    reason_description: Optional[str] = None
    from_: Optional[ListCompanyActiveCallsResponseRecordsItemLegsItemFrom] = field(metadata=config(field_name='from'), default=None)
    """ Caller information """
    
    to: Optional[ListCompanyActiveCallsResponseRecordsItemLegsItemTo] = None
    """ Callee information """
    
    transport: Optional[ListCompanyActiveCallsResponseRecordsItemLegsItemTransport] = None
    """ Call transport """
    
    recording: Optional[ListCompanyActiveCallsResponseRecordsItemLegsItemRecording] = None
    """ Call recording data. Returned if the call is recorded """
    
    short_recording: Optional[bool] = None
    """
    Indicates that the recording is too short and therefore wouldn't be returned. The flag is not
    returned if the value is false
    """
    
    master: Optional[bool] = None
    """ Returned for 'Detailed' call log. Specifies if the leg is master-leg """
    
    message: Optional[ListCompanyActiveCallsResponseRecordsItemLegsItemMessage] = None
    """ Linked message (Fax/Voicemail) """
    
    telephony_session_id: Optional[str] = None
    """ Telephony identifier of a call session """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListCompanyActiveCallsResponseRecordsItemBilling(DataClassJsonMixin):
    """ Billing information related to the call. Returned for 'Detailed' view only """
    
    cost_included: Optional[float] = None
    """
    Cost per minute, paid and already included in your RingCentral Plan. For example International
    Calls
    """
    
    cost_purchased: Optional[float] = None
    """ Cost per minute, paid and not included in your RingCentral Plan """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListCompanyActiveCallsResponseRecordsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a cal log record """
    
    uri: Optional[str] = None
    """ Canonical URI of a call log record """
    
    session_id: Optional[str] = None
    """ Internal identifier of a call session """
    
    extension: Optional[ListCompanyActiveCallsResponseRecordsItemExtension] = None
    telephony_session_id: Optional[str] = None
    """ Telephony identifier of a call session """
    
    transport: Optional[ListCompanyActiveCallsResponseRecordsItemTransport] = None
    """ Call transport """
    
    from_: Optional[ListCompanyActiveCallsResponseRecordsItemFrom] = field(metadata=config(field_name='from'), default=None)
    """ Caller information """
    
    to: Optional[ListCompanyActiveCallsResponseRecordsItemTo] = None
    """ Callee information """
    
    type: Optional[ListCompanyActiveCallsResponseRecordsItemType] = None
    """ Call type """
    
    direction: Optional[ListCompanyActiveCallsResponseRecordsItemDirection] = None
    """ Call direction """
    
    message: Optional[ListCompanyActiveCallsResponseRecordsItemMessage] = None
    """ Linked message (Fax/Voicemail) """
    
    delegate: Optional[ListCompanyActiveCallsResponseRecordsItemDelegate] = None
    """
    Information on a delegate extension that actually implemented a call action. For Secretary call
    log the field is returned if the current extension implemented a call. For Boss call log the
    field contains information on a Secretary extension which actually implemented a call on behalf
    of the current extension
    """
    
    deleted: Optional[bool] = None
    """ Indicates whether the record is deleted. Returned for deleted records, for ISync requests """
    
    action: Optional[ListCompanyActiveCallsResponseRecordsItemAction] = None
    """ Action description of the call operation """
    
    result: Optional[ListCompanyActiveCallsResponseRecordsItemResult] = None
    """ Status description of the call operation """
    
    reason: Optional[ListCompanyActiveCallsResponseRecordsItemReason] = None
    reason_description: Optional[str] = None
    start_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """
    The call start datetime in (ISO 8601)[https://en.wikipedia.org/wiki/ISO_8601] format including
    timezone, for example 2016-03-10T18:07:52.534Z
    """
    
    duration: Optional[int] = None
    """ Call duration in seconds """
    
    recording: Optional[ListCompanyActiveCallsResponseRecordsItemRecording] = None
    """ Call recording data. Returned if a call is recorded """
    
    short_recording: Optional[bool] = None
    """
    Indicates that the recording is too short and therefore wouldn't be returned. The flag is not
    returned if the value is false
    """
    
    legs: Optional[List[ListCompanyActiveCallsResponseRecordsItemLegsItem]] = None
    """ For 'Detailed' view only. Leg description """
    
    billing: Optional[ListCompanyActiveCallsResponseRecordsItemBilling] = None
    """ Billing information related to the call. Returned for 'Detailed' view only """
    
    last_modified_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """
    For 'Detailed' view only. The datetime when the call log record was modified in (ISO
    8601)[https://en.wikipedia.org/wiki/ISO_8601] format including timezone, for example
    2016-03-10T18:07:52.534Z
    """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListCompanyActiveCallsResponseNavigationFirstPage(DataClassJsonMixin):
    """ Canonical URI for the first page of the list """
    
    uri: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListCompanyActiveCallsResponseNavigationNextPage(DataClassJsonMixin):
    """ Canonical URI for the next page of the list """
    
    uri: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListCompanyActiveCallsResponseNavigationPreviousPage(DataClassJsonMixin):
    """ Canonical URI for the previous page of the list """
    
    uri: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListCompanyActiveCallsResponseNavigationLastPage(DataClassJsonMixin):
    """ Canonical URI for the last page of the list """
    
    uri: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListCompanyActiveCallsResponseNavigation(DataClassJsonMixin):
    """ Information on navigation """
    
    first_page: Optional[ListCompanyActiveCallsResponseNavigationFirstPage] = None
    """ Canonical URI for the first page of the list """
    
    next_page: Optional[ListCompanyActiveCallsResponseNavigationNextPage] = None
    """ Canonical URI for the next page of the list """
    
    previous_page: Optional[ListCompanyActiveCallsResponseNavigationPreviousPage] = None
    """ Canonical URI for the previous page of the list """
    
    last_page: Optional[ListCompanyActiveCallsResponseNavigationLastPage] = None
    """ Canonical URI for the last page of the list """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListCompanyActiveCallsResponsePaging(DataClassJsonMixin):
    """ Information on paging """
    
    page: Optional[int] = None
    """
    The current page number. 1-indexed, so the first page is 1 by default. May be omitted if result
    is empty (because non-existent page was specified or perPage=0 was requested)
    """
    
    per_page: Optional[int] = 100
    """
    Current page size, describes how many items are in each page. Maximum value is 1000. If perPage
    value in the request is greater than 1000, the maximum value (1000) is applied
    """
    
    page_start: Optional[int] = None
    """
    The zero-based number of the first element on the current page. Omitted if the page is omitted
    or result is empty
    """
    
    page_end: Optional[int] = None
    """
    The zero-based index of the last element on the current page. Omitted if the page is omitted or
    result is empty
    """
    
    total_pages: Optional[int] = None
    """
    The total number of pages in a dataset. May be omitted for some resources due to performance
    reasons
    """
    
    total_elements: Optional[int] = None
    """
    The total number of elements in a dataset. May be omitted for some resource due to performance
    reasons
    """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListCompanyActiveCallsResponse(DataClassJsonMixin):
    """
    Required Properties:
     - navigation
     - paging
     - records
    
    Generated by Python OpenAPI Parser
    """
    
    records: List[ListCompanyActiveCallsResponseRecordsItem]
    """ List of call log records """
    
    navigation: ListCompanyActiveCallsResponseNavigation
    """ Information on navigation """
    
    paging: ListCompanyActiveCallsResponsePaging
    """ Information on paging """
    
    uri: Optional[str] = None
    """ Link to the list of company active call records """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadCallRecordingResponse(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a call recording """
    
    content_uri: Optional[str] = None
    """ Link to a call recording binary content """
    
    content_type: Optional[str] = None
    """ Call recording file format. Supported format is audio/x-wav """
    
    duration: Optional[int] = None
    """ Recorded call duration """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateSMSMessageRequestFrom(DataClassJsonMixin):
    """
    Message sender information. The `phoneNumber` value should be one the account phone numbers
    allowed to send text messages
    
    Generated by Python OpenAPI Parser
    """
    
    phone_number: Optional[str] = None
    """ Phone number in E.164 format """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateSMSMessageRequestToItem(DataClassJsonMixin):
    phone_number: Optional[str] = None
    """ Phone number in E.164 format """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateSMSMessageRequestCountry(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a country """
    
    uri: Optional[str] = None
    """ Canonical URI of a country """
    
    name: Optional[str] = None
    """ Official name of a country """
    
    iso_code: Optional[str] = None
    """ ISO code of a country """
    
    calling_code: Optional[str] = None
    """ Calling code of a country """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateSMSMessageRequest(DataClassJsonMixin):
    """
    Required Properties:
     - from_
     - text
     - to
    
    Generated by Python OpenAPI Parser
    """
    
    from_: CreateSMSMessageRequestFrom = field(metadata=config(field_name='from'))
    """
    Message sender information. The `phoneNumber` value should be one the account phone numbers
    allowed to send text messages
    """
    
    to: List[CreateSMSMessageRequestToItem]
    """ Message receiver(s) information. The `phoneNumber` value is required """
    
    text: str
    """
    Text of a message. Max length is 1000 symbols (2-byte UTF-16 encoded). If a character is
    encoded in 4 bytes in UTF-16 it is treated as 2 characters, thus restricting the maximum
    message length to 500 symbols
    """
    
    country: Optional[CreateSMSMessageRequestCountry] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateSMSMessageRequestFrom(DataClassJsonMixin):
    """
    Message sender information. The `phoneNumber` value should be one the account phone numbers
    allowed to send text messages
    
    Generated by Python OpenAPI Parser
    """
    
    phone_number: Optional[str] = None
    """ Phone number in E.164 format """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateSMSMessageRequestCountry(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a country """
    
    uri: Optional[str] = None
    """ Canonical URI of a country """
    
    name: Optional[str] = None
    """ Official name of a country """
    
    iso_code: Optional[str] = None
    """ ISO code of a country """
    
    calling_code: Optional[str] = None
    """ Calling code of a country """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateSMSMessageRequest(DataClassJsonMixin):
    """
    Required Properties:
     - from_
     - text
     - to
    
    Generated by Python OpenAPI Parser
    """
    
    from_: CreateSMSMessageRequestFrom = field(metadata=config(field_name='from'))
    """
    Message sender information. The `phoneNumber` value should be one the account phone numbers
    allowed to send text messages
    """
    
    to: List[dict]
    """ Message receiver(s) information. The `phoneNumber` value is required """
    
    text: str
    """
    Text of a message. Max length is 1000 symbols (2-byte UTF-16 encoded). If a character is
    encoded in 4 bytes in UTF-16 it is treated as 2 characters, thus restricting the maximum
    message length to 500 symbols
    """
    
    country: Optional[CreateSMSMessageRequestCountry] = None

class CreateSMSMessageResponseAttachmentsItemType(Enum):
    """ Type of message attachment """
    
    AudioRecording = 'AudioRecording'
    AudioTranscription = 'AudioTranscription'
    Text = 'Text'
    SourceDocument = 'SourceDocument'
    RenderedDocument = 'RenderedDocument'
    MmsAttachment = 'MmsAttachment'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateSMSMessageResponseAttachmentsItem(DataClassJsonMixin):
    id: Optional[int] = None
    """ Internal identifier of a message attachment """
    
    uri: Optional[str] = None
    """ Canonical URI of a message attachment """
    
    type: Optional[CreateSMSMessageResponseAttachmentsItemType] = None
    """ Type of message attachment """
    
    content_type: Optional[str] = None
    """ MIME type for a given attachment, for instance 'audio/wav' """
    
    vm_duration: Optional[int] = None
    """ Supported for `Voicemail` only. Duration of a voicemail in seconds """
    
    file_name: Optional[str] = None
    """ Name of a file attached """
    
    size: Optional[int] = None
    """ Size of attachment in bytes """
    
    height: Optional[int] = None
    """ Attachment height in pixels if available """
    
    width: Optional[int] = None
    """ Attachment width in pixels if available """
    

class CreateSMSMessageResponseAvailability(Enum):
    """
    Message availability status. Message in 'Deleted' state is still preserved with all its
    attachments and can be restored. 'Purged' means that all attachments are already deleted and
    the message itself is about to be physically deleted shortly
    
    Generated by Python OpenAPI Parser
    """
    
    Alive = 'Alive'
    Deleted = 'Deleted'
    Purged = 'Purged'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateSMSMessageResponseConversation(DataClassJsonMixin):
    """ SMS and Pager only. Identifier of a conversation the message belongs to """
    
    id: Optional[str] = None
    """ Internal identifier of a conversation """
    
    uri: Optional[str] = None
    """ Deprecated. Link to a conversation resource """
    

class CreateSMSMessageResponseDirection(Enum):
    """
    Message direction. Note that for some message types not all directions are allowed. For example
    voicemail messages can be only inbound
    
    Generated by Python OpenAPI Parser
    """
    
    Inbound = 'Inbound'
    Outbound = 'Outbound'

class CreateSMSMessageResponseFaxResolution(Enum):
    """
    Fax only. Resolution of a fax message. 'High' for black and white image scanned at 200 dpi,
    'Low' for black and white image scanned at 100 dpi
    
    Generated by Python OpenAPI Parser
    """
    
    High = 'High'
    Low = 'Low'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateSMSMessageResponseFrom(DataClassJsonMixin):
    """ Sender information """
    
    extension_number: Optional[str] = None
    """
    Extension short number (usually 3 or 4 digits). This property is filled when parties
    communicate by means of short internal numbers, for example when calling to other extension or
    sending/receiving Company Pager message
    """
    
    extension_id: Optional[str] = None
    """ Internal identifier of an extension """
    
    location: Optional[str] = None
    """
    Contains party location (city, state) if one can be determined from phoneNumber. This property
    is filled only when phoneNumber is not empty and server can calculate location information from
    it (for example, this information is unavailable for US toll-free numbers)
    """
    
    name: Optional[str] = None
    """
    Symbolic name associated with a party. If the phone does not belong to the known extension,
    only the location is returned, the name is not determined then
    """
    
    phone_number: Optional[str] = None
    """
    Phone number of a party. Usually it is a plain number including country and area code like
    18661234567. But sometimes it could be returned from database with some formatting applied, for
    example (866)123-4567. This property is filled in all cases where parties communicate by means
    of global phone numbers, for example when calling to direct numbers or sending/receiving SMS
    """
    

class CreateSMSMessageResponseMessageStatus(Enum):
    """
    Message status. Different message types may have different allowed status values. For outbound
    faxes the aggregated message status is returned: If status for at least one recipient is
    'Queued', then 'Queued' value is returned If status for at least one recipient is
    'SendingFailed', then 'SendingFailed' value is returned In other cases Sent status is returned
    
    Generated by Python OpenAPI Parser
    """
    
    Queued = 'Queued'
    Sent = 'Sent'
    Delivered = 'Delivered'
    DeliveryFailed = 'DeliveryFailed'
    SendingFailed = 'SendingFailed'
    Received = 'Received'

class CreateSMSMessageResponsePriority(Enum):
    """ Message priority """
    
    Normal = 'Normal'
    High = 'High'

class CreateSMSMessageResponseReadStatus(Enum):
    """ Message read status """
    
    Read = 'Read'
    Unread = 'Unread'

class CreateSMSMessageResponseToItemMessageStatus(Enum):
    """ Status of a message. Returned for outbound fax messages only """
    
    Queued = 'Queued'
    Sent = 'Sent'
    Delivered = 'Delivered'
    DeliveryFailed = 'DeliveryFailed'
    SendingFailed = 'SendingFailed'
    Received = 'Received'

class CreateSMSMessageResponseToItemFaxErrorCode(Enum):
    """
    Error code returned in case of fax sending failure. Returned if messageStatus value is
    'SendingFailed'. Supported for fax messages only
    
    Generated by Python OpenAPI Parser
    """
    
    AllLinesInUse = 'AllLinesInUse'
    Undefined = 'Undefined'
    NoFaxSendPermission = 'NoFaxSendPermission'
    NoInternationalPermission = 'NoInternationalPermission'
    NoFaxMachine = 'NoFaxMachine'
    NoAnswer = 'NoAnswer'
    LineBusy = 'LineBusy'
    CallerHungUp = 'CallerHungUp'
    NotEnoughCredits = 'NotEnoughCredits'
    SentPartially = 'SentPartially'
    InternationalCallingDisabled = 'InternationalCallingDisabled'
    DestinationCountryDisabled = 'DestinationCountryDisabled'
    UnknownCountryCode = 'UnknownCountryCode'
    NotAccepted = 'NotAccepted'
    InvalidNumber = 'InvalidNumber'
    CallDeclined = 'CallDeclined'
    TooManyCallsPerLine = 'TooManyCallsPerLine'
    CallFailed = 'CallFailed'
    RenderingFailed = 'RenderingFailed'
    TooManyPages = 'TooManyPages'
    ReturnToDBQueue = 'ReturnToDBQueue'
    NoCallTime = 'NoCallTime'
    WrongNumber = 'WrongNumber'
    ProhibitedNumber = 'ProhibitedNumber'
    InternalError = 'InternalError'
    FaxSendingProhibited = 'FaxSendingProhibited'
    ThePhoneIsBlacklisted = 'ThePhoneIsBlacklisted'
    UserNotFound = 'UserNotFound'
    ConvertError = 'ConvertError'
    DBGeneralError = 'DBGeneralError'
    SkypeBillingFailed = 'SkypeBillingFailed'
    AccountSuspended = 'AccountSuspended'
    ProhibitedDestination = 'ProhibitedDestination'
    InternationalDisabled = 'InternationalDisabled'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateSMSMessageResponseToItem(DataClassJsonMixin):
    extension_number: Optional[str] = None
    """
    Extension short number (usually 3 or 4 digits). This property is filled when parties
    communicate by means of short internal numbers, for example when calling to other extension or
    sending/receiving Company Pager message
    """
    
    extension_id: Optional[str] = None
    location: Optional[str] = None
    """
    Contains party location (city, state) if one can be determined from phoneNumber. This property
    is filled only when phoneNumber is not empty and server can calculate location information from
    it (for example, this information is unavailable for US toll-free numbers)
    """
    
    target: Optional[bool] = None
    """
    'True' specifies that message is sent exactly to this recipient. Returned in to field for group
    MMS. Useful if one extension has several phone numbers
    """
    
    message_status: Optional[CreateSMSMessageResponseToItemMessageStatus] = None
    """ Status of a message. Returned for outbound fax messages only """
    
    fax_error_code: Optional[CreateSMSMessageResponseToItemFaxErrorCode] = None
    """
    Error code returned in case of fax sending failure. Returned if messageStatus value is
    'SendingFailed'. Supported for fax messages only
    """
    
    name: Optional[str] = None
    """
    Symbolic name associated with a party. If the phone does not belong to the known extension,
    only the location is returned, the name is not determined then
    """
    
    phone_number: Optional[str] = None
    """
    Phone number of a party. Usually it is a plain number including country and area code like
    18661234567. But sometimes it could be returned from database with some formatting applied, for
    example (866)123-4567. This property is filled in all cases where parties communicate by means
    of global phone numbers, for example when calling to direct numbers or sending/receiving SMS
    """
    

class CreateSMSMessageResponseType(Enum):
    """ Message type """
    
    Fax = 'Fax'
    SMS = 'SMS'
    VoiceMail = 'VoiceMail'
    Pager = 'Pager'
    Text = 'Text'

class CreateSMSMessageResponseVmTranscriptionStatus(Enum):
    """
    Voicemail only. Status of voicemail to text transcription. If VoicemailToText feature is not
    activated for account, the 'NotAvailable' value is returned
    
    Generated by Python OpenAPI Parser
    """
    
    NotAvailable = 'NotAvailable'
    InProgress = 'InProgress'
    TimedOut = 'TimedOut'
    Completed = 'Completed'
    CompletedPartially = 'CompletedPartially'
    Failed = 'Failed'
    Unknown = 'Unknown'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateSMSMessageResponse(DataClassJsonMixin):
    id: Optional[int] = None
    """ Internal identifier of a message """
    
    uri: Optional[str] = None
    """ Canonical URI of a message """
    
    attachments: Optional[List[CreateSMSMessageResponseAttachmentsItem]] = None
    """ The list of message attachments """
    
    availability: Optional[CreateSMSMessageResponseAvailability] = None
    """
    Message availability status. Message in 'Deleted' state is still preserved with all its
    attachments and can be restored. 'Purged' means that all attachments are already deleted and
    the message itself is about to be physically deleted shortly
    """
    
    conversation_id: Optional[int] = None
    """ SMS and Pager only. Identifier of a conversation the message belongs to """
    
    conversation: Optional[CreateSMSMessageResponseConversation] = None
    """ SMS and Pager only. Identifier of a conversation the message belongs to """
    
    creation_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """
    Message creation datetime in ISO 8601 format including timezone, for example
    2016-03-10T18:07:52.534Z
    """
    
    delivery_error_code: Optional[str] = None
    """ SMS only. Delivery error code returned by gateway """
    
    direction: Optional[CreateSMSMessageResponseDirection] = None
    """
    Message direction. Note that for some message types not all directions are allowed. For example
    voicemail messages can be only inbound
    """
    
    fax_page_count: Optional[int] = None
    """ Fax only. Page count in a fax message """
    
    fax_resolution: Optional[CreateSMSMessageResponseFaxResolution] = None
    """
    Fax only. Resolution of a fax message. 'High' for black and white image scanned at 200 dpi,
    'Low' for black and white image scanned at 100 dpi
    """
    
    from_: Optional[CreateSMSMessageResponseFrom] = field(metadata=config(field_name='from'), default=None)
    """ Sender information """
    
    last_modified_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """
    The datetime when the message was modified on server in ISO 8601 format including timezone, for
    example 2016-03-10T18:07:52.534Z
    """
    
    message_status: Optional[CreateSMSMessageResponseMessageStatus] = None
    """
    Message status. Different message types may have different allowed status values. For outbound
    faxes the aggregated message status is returned: If status for at least one recipient is
    'Queued', then 'Queued' value is returned If status for at least one recipient is
    'SendingFailed', then 'SendingFailed' value is returned In other cases Sent status is returned
    """
    
    pg_to_department: Optional[bool] = None
    """ 'Pager' only. 'True' if at least one of the message recipients is 'Department' extension """
    
    priority: Optional[CreateSMSMessageResponsePriority] = None
    """ Message priority """
    
    read_status: Optional[CreateSMSMessageResponseReadStatus] = None
    """ Message read status """
    
    sms_delivery_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """
    SMS only. The datetime when outbound SMS was delivered to recipient's handset in ISO 8601
    format including timezone, for example 2016-03-10T18:07:52.534Z. It is filled only if the
    carrier sends a delivery receipt to RingCentral
    """
    
    sms_sending_attempts_count: Optional[int] = None
    """
    SMS only. Number of attempts made to send an outbound SMS to the gateway (if gateway is
    temporary unavailable)
    """
    
    subject: Optional[str] = None
    """
    Message subject. For SMS and Pager messages it replicates message text which is also returned
    as an attachment
    """
    
    to: Optional[List[CreateSMSMessageResponseToItem]] = None
    """ Recipient information """
    
    type: Optional[CreateSMSMessageResponseType] = None
    """ Message type """
    
    vm_transcription_status: Optional[CreateSMSMessageResponseVmTranscriptionStatus] = None
    """
    Voicemail only. Status of voicemail to text transcription. If VoicemailToText feature is not
    activated for account, the 'NotAvailable' value is returned
    """
    
    cover_index: Optional[int] = None
    """
    Cover page identifier. For the list of available cover page identifiers please call the Fax
    Cover Pages method
    """
    
    cover_page_text: Optional[str] = None
    """
    Cover page text, entered by the fax sender and printed on the cover page. Maximum length is
    limited to 1024 symbols
    """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateMMSRequest(DataClassJsonMixin):
    """
    Required Properties:
     - attachments
     - from_
     - to
    
    Generated by Python OpenAPI Parser
    """
    
    from_: dict = field(metadata=config(field_name='from'))
    """
    Message sender information. The `phoneNumber` value should be one the account phone numbers
    allowed to send media messages
    """
    
    to: list
    """ Message receiver(s) information. The `phoneNumber` value is required """
    
    attachments: List[bytes]
    """ Media file(s) to upload """
    
    text: Optional[str] = None
    """
    Text of a message. Max length is 1000 symbols (2-byte UTF-16 encoded). If a character is
    encoded in 4 bytes in UTF-16 it is treated as 2 characters, thus restricting the maximum
    message length to 500 symbols
    """
    
    country: Optional[dict] = None

class CreateMMSResponseAttachmentsItemType(Enum):
    """ Type of message attachment """
    
    AudioRecording = 'AudioRecording'
    AudioTranscription = 'AudioTranscription'
    Text = 'Text'
    SourceDocument = 'SourceDocument'
    RenderedDocument = 'RenderedDocument'
    MmsAttachment = 'MmsAttachment'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateMMSResponseAttachmentsItem(DataClassJsonMixin):
    id: Optional[int] = None
    """ Internal identifier of a message attachment """
    
    uri: Optional[str] = None
    """ Canonical URI of a message attachment """
    
    type: Optional[CreateMMSResponseAttachmentsItemType] = None
    """ Type of message attachment """
    
    content_type: Optional[str] = None
    """ MIME type for a given attachment, for instance 'audio/wav' """
    
    vm_duration: Optional[int] = None
    """ Supported for `Voicemail` only. Duration of a voicemail in seconds """
    
    file_name: Optional[str] = None
    """ Name of a file attached """
    
    size: Optional[int] = None
    """ Size of attachment in bytes """
    
    height: Optional[int] = None
    """ Attachment height in pixels if available """
    
    width: Optional[int] = None
    """ Attachment width in pixels if available """
    

class CreateMMSResponseAvailability(Enum):
    """
    Message availability status. Message in 'Deleted' state is still preserved with all its
    attachments and can be restored. 'Purged' means that all attachments are already deleted and
    the message itself is about to be physically deleted shortly
    
    Generated by Python OpenAPI Parser
    """
    
    Alive = 'Alive'
    Deleted = 'Deleted'
    Purged = 'Purged'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateMMSResponseConversation(DataClassJsonMixin):
    """ SMS and Pager only. Identifier of a conversation the message belongs to """
    
    id: Optional[str] = None
    """ Internal identifier of a conversation """
    
    uri: Optional[str] = None
    """ Deprecated. Link to a conversation resource """
    

class CreateMMSResponseDirection(Enum):
    """
    Message direction. Note that for some message types not all directions are allowed. For example
    voicemail messages can be only inbound
    
    Generated by Python OpenAPI Parser
    """
    
    Inbound = 'Inbound'
    Outbound = 'Outbound'

class CreateMMSResponseFaxResolution(Enum):
    """
    Fax only. Resolution of a fax message. 'High' for black and white image scanned at 200 dpi,
    'Low' for black and white image scanned at 100 dpi
    
    Generated by Python OpenAPI Parser
    """
    
    High = 'High'
    Low = 'Low'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateMMSResponseFrom(DataClassJsonMixin):
    """ Sender information """
    
    extension_number: Optional[str] = None
    """
    Extension short number (usually 3 or 4 digits). This property is filled when parties
    communicate by means of short internal numbers, for example when calling to other extension or
    sending/receiving Company Pager message
    """
    
    extension_id: Optional[str] = None
    """ Internal identifier of an extension """
    
    location: Optional[str] = None
    """
    Contains party location (city, state) if one can be determined from phoneNumber. This property
    is filled only when phoneNumber is not empty and server can calculate location information from
    it (for example, this information is unavailable for US toll-free numbers)
    """
    
    name: Optional[str] = None
    """
    Symbolic name associated with a party. If the phone does not belong to the known extension,
    only the location is returned, the name is not determined then
    """
    
    phone_number: Optional[str] = None
    """
    Phone number of a party. Usually it is a plain number including country and area code like
    18661234567. But sometimes it could be returned from database with some formatting applied, for
    example (866)123-4567. This property is filled in all cases where parties communicate by means
    of global phone numbers, for example when calling to direct numbers or sending/receiving SMS
    """
    

class CreateMMSResponseMessageStatus(Enum):
    """
    Message status. Different message types may have different allowed status values. For outbound
    faxes the aggregated message status is returned: If status for at least one recipient is
    'Queued', then 'Queued' value is returned If status for at least one recipient is
    'SendingFailed', then 'SendingFailed' value is returned In other cases Sent status is returned
    
    Generated by Python OpenAPI Parser
    """
    
    Queued = 'Queued'
    Sent = 'Sent'
    Delivered = 'Delivered'
    DeliveryFailed = 'DeliveryFailed'
    SendingFailed = 'SendingFailed'
    Received = 'Received'

class CreateMMSResponsePriority(Enum):
    """ Message priority """
    
    Normal = 'Normal'
    High = 'High'

class CreateMMSResponseReadStatus(Enum):
    """ Message read status """
    
    Read = 'Read'
    Unread = 'Unread'

class CreateMMSResponseToItemMessageStatus(Enum):
    """ Status of a message. Returned for outbound fax messages only """
    
    Queued = 'Queued'
    Sent = 'Sent'
    Delivered = 'Delivered'
    DeliveryFailed = 'DeliveryFailed'
    SendingFailed = 'SendingFailed'
    Received = 'Received'

class CreateMMSResponseToItemFaxErrorCode(Enum):
    """
    Error code returned in case of fax sending failure. Returned if messageStatus value is
    'SendingFailed'. Supported for fax messages only
    
    Generated by Python OpenAPI Parser
    """
    
    AllLinesInUse = 'AllLinesInUse'
    Undefined = 'Undefined'
    NoFaxSendPermission = 'NoFaxSendPermission'
    NoInternationalPermission = 'NoInternationalPermission'
    NoFaxMachine = 'NoFaxMachine'
    NoAnswer = 'NoAnswer'
    LineBusy = 'LineBusy'
    CallerHungUp = 'CallerHungUp'
    NotEnoughCredits = 'NotEnoughCredits'
    SentPartially = 'SentPartially'
    InternationalCallingDisabled = 'InternationalCallingDisabled'
    DestinationCountryDisabled = 'DestinationCountryDisabled'
    UnknownCountryCode = 'UnknownCountryCode'
    NotAccepted = 'NotAccepted'
    InvalidNumber = 'InvalidNumber'
    CallDeclined = 'CallDeclined'
    TooManyCallsPerLine = 'TooManyCallsPerLine'
    CallFailed = 'CallFailed'
    RenderingFailed = 'RenderingFailed'
    TooManyPages = 'TooManyPages'
    ReturnToDBQueue = 'ReturnToDBQueue'
    NoCallTime = 'NoCallTime'
    WrongNumber = 'WrongNumber'
    ProhibitedNumber = 'ProhibitedNumber'
    InternalError = 'InternalError'
    FaxSendingProhibited = 'FaxSendingProhibited'
    ThePhoneIsBlacklisted = 'ThePhoneIsBlacklisted'
    UserNotFound = 'UserNotFound'
    ConvertError = 'ConvertError'
    DBGeneralError = 'DBGeneralError'
    SkypeBillingFailed = 'SkypeBillingFailed'
    AccountSuspended = 'AccountSuspended'
    ProhibitedDestination = 'ProhibitedDestination'
    InternationalDisabled = 'InternationalDisabled'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateMMSResponseToItem(DataClassJsonMixin):
    extension_number: Optional[str] = None
    """
    Extension short number (usually 3 or 4 digits). This property is filled when parties
    communicate by means of short internal numbers, for example when calling to other extension or
    sending/receiving Company Pager message
    """
    
    extension_id: Optional[str] = None
    location: Optional[str] = None
    """
    Contains party location (city, state) if one can be determined from phoneNumber. This property
    is filled only when phoneNumber is not empty and server can calculate location information from
    it (for example, this information is unavailable for US toll-free numbers)
    """
    
    target: Optional[bool] = None
    """
    'True' specifies that message is sent exactly to this recipient. Returned in to field for group
    MMS. Useful if one extension has several phone numbers
    """
    
    message_status: Optional[CreateMMSResponseToItemMessageStatus] = None
    """ Status of a message. Returned for outbound fax messages only """
    
    fax_error_code: Optional[CreateMMSResponseToItemFaxErrorCode] = None
    """
    Error code returned in case of fax sending failure. Returned if messageStatus value is
    'SendingFailed'. Supported for fax messages only
    """
    
    name: Optional[str] = None
    """
    Symbolic name associated with a party. If the phone does not belong to the known extension,
    only the location is returned, the name is not determined then
    """
    
    phone_number: Optional[str] = None
    """
    Phone number of a party. Usually it is a plain number including country and area code like
    18661234567. But sometimes it could be returned from database with some formatting applied, for
    example (866)123-4567. This property is filled in all cases where parties communicate by means
    of global phone numbers, for example when calling to direct numbers or sending/receiving SMS
    """
    

class CreateMMSResponseType(Enum):
    """ Message type """
    
    Fax = 'Fax'
    SMS = 'SMS'
    VoiceMail = 'VoiceMail'
    Pager = 'Pager'
    Text = 'Text'

class CreateMMSResponseVmTranscriptionStatus(Enum):
    """
    Voicemail only. Status of voicemail to text transcription. If VoicemailToText feature is not
    activated for account, the 'NotAvailable' value is returned
    
    Generated by Python OpenAPI Parser
    """
    
    NotAvailable = 'NotAvailable'
    InProgress = 'InProgress'
    TimedOut = 'TimedOut'
    Completed = 'Completed'
    CompletedPartially = 'CompletedPartially'
    Failed = 'Failed'
    Unknown = 'Unknown'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateMMSResponse(DataClassJsonMixin):
    id: Optional[int] = None
    """ Internal identifier of a message """
    
    uri: Optional[str] = None
    """ Canonical URI of a message """
    
    attachments: Optional[List[CreateMMSResponseAttachmentsItem]] = None
    """ The list of message attachments """
    
    availability: Optional[CreateMMSResponseAvailability] = None
    """
    Message availability status. Message in 'Deleted' state is still preserved with all its
    attachments and can be restored. 'Purged' means that all attachments are already deleted and
    the message itself is about to be physically deleted shortly
    """
    
    conversation_id: Optional[int] = None
    """ SMS and Pager only. Identifier of a conversation the message belongs to """
    
    conversation: Optional[CreateMMSResponseConversation] = None
    """ SMS and Pager only. Identifier of a conversation the message belongs to """
    
    creation_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """
    Message creation datetime in ISO 8601 format including timezone, for example
    2016-03-10T18:07:52.534Z
    """
    
    delivery_error_code: Optional[str] = None
    """ SMS only. Delivery error code returned by gateway """
    
    direction: Optional[CreateMMSResponseDirection] = None
    """
    Message direction. Note that for some message types not all directions are allowed. For example
    voicemail messages can be only inbound
    """
    
    fax_page_count: Optional[int] = None
    """ Fax only. Page count in a fax message """
    
    fax_resolution: Optional[CreateMMSResponseFaxResolution] = None
    """
    Fax only. Resolution of a fax message. 'High' for black and white image scanned at 200 dpi,
    'Low' for black and white image scanned at 100 dpi
    """
    
    from_: Optional[CreateMMSResponseFrom] = field(metadata=config(field_name='from'), default=None)
    """ Sender information """
    
    last_modified_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """
    The datetime when the message was modified on server in ISO 8601 format including timezone, for
    example 2016-03-10T18:07:52.534Z
    """
    
    message_status: Optional[CreateMMSResponseMessageStatus] = None
    """
    Message status. Different message types may have different allowed status values. For outbound
    faxes the aggregated message status is returned: If status for at least one recipient is
    'Queued', then 'Queued' value is returned If status for at least one recipient is
    'SendingFailed', then 'SendingFailed' value is returned In other cases Sent status is returned
    """
    
    pg_to_department: Optional[bool] = None
    """ 'Pager' only. 'True' if at least one of the message recipients is 'Department' extension """
    
    priority: Optional[CreateMMSResponsePriority] = None
    """ Message priority """
    
    read_status: Optional[CreateMMSResponseReadStatus] = None
    """ Message read status """
    
    sms_delivery_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """
    SMS only. The datetime when outbound SMS was delivered to recipient's handset in ISO 8601
    format including timezone, for example 2016-03-10T18:07:52.534Z. It is filled only if the
    carrier sends a delivery receipt to RingCentral
    """
    
    sms_sending_attempts_count: Optional[int] = None
    """
    SMS only. Number of attempts made to send an outbound SMS to the gateway (if gateway is
    temporary unavailable)
    """
    
    subject: Optional[str] = None
    """
    Message subject. For SMS and Pager messages it replicates message text which is also returned
    as an attachment
    """
    
    to: Optional[List[CreateMMSResponseToItem]] = None
    """ Recipient information """
    
    type: Optional[CreateMMSResponseType] = None
    """ Message type """
    
    vm_transcription_status: Optional[CreateMMSResponseVmTranscriptionStatus] = None
    """
    Voicemail only. Status of voicemail to text transcription. If VoicemailToText feature is not
    activated for account, the 'NotAvailable' value is returned
    """
    
    cover_index: Optional[int] = None
    """
    Cover page identifier. For the list of available cover page identifiers please call the Fax
    Cover Pages method
    """
    
    cover_page_text: Optional[str] = None
    """
    Cover page text, entered by the fax sender and printed on the cover page. Maximum length is
    limited to 1024 symbols
    """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateInternalTextMessageRequestFrom(DataClassJsonMixin):
    """ Sender of a pager message. """
    
    extension_id: Optional[str] = None
    """
    Extension identifier
    
    Example: `123456789`
    """
    
    extension_number: Optional[str] = None
    """
    Extension number
    
    Example: `105`
    """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateInternalTextMessageRequestToItem(DataClassJsonMixin):
    extension_id: Optional[str] = None
    """
    Extension identifier
    
    Example: `123456789`
    """
    
    extension_number: Optional[str] = None
    """
    Extension number
    
    Example: `105`
    """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateInternalTextMessageRequest(DataClassJsonMixin):
    """
    Required Properties:
     - text
    
    Generated by Python OpenAPI Parser
    """
    
    text: str
    """
    Text of a pager message. Max length is 1024 symbols (2-byte UTF-16 encoded). If a character is
    encoded in 4 bytes in UTF-16 it is treated as 2 characters, thus restricting the maximum
    message length to 512 symbols
    
    Example: `hello world`
    """
    
    from_: Optional[CreateInternalTextMessageRequestFrom] = field(metadata=config(field_name='from'), default=None)
    """ Sender of a pager message. """
    
    reply_on: Optional[int] = None
    """ Internal identifier of a message this message replies to """
    
    to: Optional[List[CreateInternalTextMessageRequestToItem]] = None
    """ Optional if replyOn parameter is specified. Receiver of a pager message. """
    

class CreateInternalTextMessageResponseAttachmentsItemType(Enum):
    """ Type of message attachment """
    
    AudioRecording = 'AudioRecording'
    AudioTranscription = 'AudioTranscription'
    Text = 'Text'
    SourceDocument = 'SourceDocument'
    RenderedDocument = 'RenderedDocument'
    MmsAttachment = 'MmsAttachment'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateInternalTextMessageResponseAttachmentsItem(DataClassJsonMixin):
    id: Optional[int] = None
    """ Internal identifier of a message attachment """
    
    uri: Optional[str] = None
    """ Canonical URI of a message attachment """
    
    type: Optional[CreateInternalTextMessageResponseAttachmentsItemType] = None
    """ Type of message attachment """
    
    content_type: Optional[str] = None
    """ MIME type for a given attachment, for instance 'audio/wav' """
    
    vm_duration: Optional[int] = None
    """ Supported for `Voicemail` only. Duration of a voicemail in seconds """
    
    file_name: Optional[str] = None
    """ Name of a file attached """
    
    size: Optional[int] = None
    """ Size of attachment in bytes """
    
    height: Optional[int] = None
    """ Attachment height in pixels if available """
    
    width: Optional[int] = None
    """ Attachment width in pixels if available """
    

class CreateInternalTextMessageResponseAvailability(Enum):
    """
    Message availability status. Message in 'Deleted' state is still preserved with all its
    attachments and can be restored. 'Purged' means that all attachments are already deleted and
    the message itself is about to be physically deleted shortly
    
    Generated by Python OpenAPI Parser
    """
    
    Alive = 'Alive'
    Deleted = 'Deleted'
    Purged = 'Purged'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateInternalTextMessageResponseConversation(DataClassJsonMixin):
    """ SMS and Pager only. Identifier of a conversation the message belongs to """
    
    id: Optional[str] = None
    """ Internal identifier of a conversation """
    
    uri: Optional[str] = None
    """ Deprecated. Link to a conversation resource """
    

class CreateInternalTextMessageResponseDirection(Enum):
    """
    Message direction. Note that for some message types not all directions are allowed. For example
    voicemail messages can be only inbound
    
    Generated by Python OpenAPI Parser
    """
    
    Inbound = 'Inbound'
    Outbound = 'Outbound'

class CreateInternalTextMessageResponseFaxResolution(Enum):
    """
    Fax only. Resolution of a fax message. 'High' for black and white image scanned at 200 dpi,
    'Low' for black and white image scanned at 100 dpi
    
    Generated by Python OpenAPI Parser
    """
    
    High = 'High'
    Low = 'Low'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateInternalTextMessageResponseFrom(DataClassJsonMixin):
    """ Sender information """
    
    extension_number: Optional[str] = None
    """
    Extension short number (usually 3 or 4 digits). This property is filled when parties
    communicate by means of short internal numbers, for example when calling to other extension or
    sending/receiving Company Pager message
    """
    
    extension_id: Optional[str] = None
    """ Internal identifier of an extension """
    
    location: Optional[str] = None
    """
    Contains party location (city, state) if one can be determined from phoneNumber. This property
    is filled only when phoneNumber is not empty and server can calculate location information from
    it (for example, this information is unavailable for US toll-free numbers)
    """
    
    name: Optional[str] = None
    """
    Symbolic name associated with a party. If the phone does not belong to the known extension,
    only the location is returned, the name is not determined then
    """
    
    phone_number: Optional[str] = None
    """
    Phone number of a party. Usually it is a plain number including country and area code like
    18661234567. But sometimes it could be returned from database with some formatting applied, for
    example (866)123-4567. This property is filled in all cases where parties communicate by means
    of global phone numbers, for example when calling to direct numbers or sending/receiving SMS
    """
    

class CreateInternalTextMessageResponseMessageStatus(Enum):
    """
    Message status. Different message types may have different allowed status values. For outbound
    faxes the aggregated message status is returned: If status for at least one recipient is
    'Queued', then 'Queued' value is returned If status for at least one recipient is
    'SendingFailed', then 'SendingFailed' value is returned In other cases Sent status is returned
    
    Generated by Python OpenAPI Parser
    """
    
    Queued = 'Queued'
    Sent = 'Sent'
    Delivered = 'Delivered'
    DeliveryFailed = 'DeliveryFailed'
    SendingFailed = 'SendingFailed'
    Received = 'Received'

class CreateInternalTextMessageResponsePriority(Enum):
    """ Message priority """
    
    Normal = 'Normal'
    High = 'High'

class CreateInternalTextMessageResponseReadStatus(Enum):
    """ Message read status """
    
    Read = 'Read'
    Unread = 'Unread'

class CreateInternalTextMessageResponseToItemMessageStatus(Enum):
    """ Status of a message. Returned for outbound fax messages only """
    
    Queued = 'Queued'
    Sent = 'Sent'
    Delivered = 'Delivered'
    DeliveryFailed = 'DeliveryFailed'
    SendingFailed = 'SendingFailed'
    Received = 'Received'

class CreateInternalTextMessageResponseToItemFaxErrorCode(Enum):
    """
    Error code returned in case of fax sending failure. Returned if messageStatus value is
    'SendingFailed'. Supported for fax messages only
    
    Generated by Python OpenAPI Parser
    """
    
    AllLinesInUse = 'AllLinesInUse'
    Undefined = 'Undefined'
    NoFaxSendPermission = 'NoFaxSendPermission'
    NoInternationalPermission = 'NoInternationalPermission'
    NoFaxMachine = 'NoFaxMachine'
    NoAnswer = 'NoAnswer'
    LineBusy = 'LineBusy'
    CallerHungUp = 'CallerHungUp'
    NotEnoughCredits = 'NotEnoughCredits'
    SentPartially = 'SentPartially'
    InternationalCallingDisabled = 'InternationalCallingDisabled'
    DestinationCountryDisabled = 'DestinationCountryDisabled'
    UnknownCountryCode = 'UnknownCountryCode'
    NotAccepted = 'NotAccepted'
    InvalidNumber = 'InvalidNumber'
    CallDeclined = 'CallDeclined'
    TooManyCallsPerLine = 'TooManyCallsPerLine'
    CallFailed = 'CallFailed'
    RenderingFailed = 'RenderingFailed'
    TooManyPages = 'TooManyPages'
    ReturnToDBQueue = 'ReturnToDBQueue'
    NoCallTime = 'NoCallTime'
    WrongNumber = 'WrongNumber'
    ProhibitedNumber = 'ProhibitedNumber'
    InternalError = 'InternalError'
    FaxSendingProhibited = 'FaxSendingProhibited'
    ThePhoneIsBlacklisted = 'ThePhoneIsBlacklisted'
    UserNotFound = 'UserNotFound'
    ConvertError = 'ConvertError'
    DBGeneralError = 'DBGeneralError'
    SkypeBillingFailed = 'SkypeBillingFailed'
    AccountSuspended = 'AccountSuspended'
    ProhibitedDestination = 'ProhibitedDestination'
    InternationalDisabled = 'InternationalDisabled'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateInternalTextMessageResponseToItem(DataClassJsonMixin):
    extension_number: Optional[str] = None
    """
    Extension short number (usually 3 or 4 digits). This property is filled when parties
    communicate by means of short internal numbers, for example when calling to other extension or
    sending/receiving Company Pager message
    """
    
    extension_id: Optional[str] = None
    location: Optional[str] = None
    """
    Contains party location (city, state) if one can be determined from phoneNumber. This property
    is filled only when phoneNumber is not empty and server can calculate location information from
    it (for example, this information is unavailable for US toll-free numbers)
    """
    
    target: Optional[bool] = None
    """
    'True' specifies that message is sent exactly to this recipient. Returned in to field for group
    MMS. Useful if one extension has several phone numbers
    """
    
    message_status: Optional[CreateInternalTextMessageResponseToItemMessageStatus] = None
    """ Status of a message. Returned for outbound fax messages only """
    
    fax_error_code: Optional[CreateInternalTextMessageResponseToItemFaxErrorCode] = None
    """
    Error code returned in case of fax sending failure. Returned if messageStatus value is
    'SendingFailed'. Supported for fax messages only
    """
    
    name: Optional[str] = None
    """
    Symbolic name associated with a party. If the phone does not belong to the known extension,
    only the location is returned, the name is not determined then
    """
    
    phone_number: Optional[str] = None
    """
    Phone number of a party. Usually it is a plain number including country and area code like
    18661234567. But sometimes it could be returned from database with some formatting applied, for
    example (866)123-4567. This property is filled in all cases where parties communicate by means
    of global phone numbers, for example when calling to direct numbers or sending/receiving SMS
    """
    

class CreateInternalTextMessageResponseType(Enum):
    """ Message type """
    
    Fax = 'Fax'
    SMS = 'SMS'
    VoiceMail = 'VoiceMail'
    Pager = 'Pager'
    Text = 'Text'

class CreateInternalTextMessageResponseVmTranscriptionStatus(Enum):
    """
    Voicemail only. Status of voicemail to text transcription. If VoicemailToText feature is not
    activated for account, the 'NotAvailable' value is returned
    
    Generated by Python OpenAPI Parser
    """
    
    NotAvailable = 'NotAvailable'
    InProgress = 'InProgress'
    TimedOut = 'TimedOut'
    Completed = 'Completed'
    CompletedPartially = 'CompletedPartially'
    Failed = 'Failed'
    Unknown = 'Unknown'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateInternalTextMessageResponse(DataClassJsonMixin):
    id: Optional[int] = None
    """ Internal identifier of a message """
    
    uri: Optional[str] = None
    """ Canonical URI of a message """
    
    attachments: Optional[List[CreateInternalTextMessageResponseAttachmentsItem]] = None
    """ The list of message attachments """
    
    availability: Optional[CreateInternalTextMessageResponseAvailability] = None
    """
    Message availability status. Message in 'Deleted' state is still preserved with all its
    attachments and can be restored. 'Purged' means that all attachments are already deleted and
    the message itself is about to be physically deleted shortly
    """
    
    conversation_id: Optional[int] = None
    """ SMS and Pager only. Identifier of a conversation the message belongs to """
    
    conversation: Optional[CreateInternalTextMessageResponseConversation] = None
    """ SMS and Pager only. Identifier of a conversation the message belongs to """
    
    creation_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """
    Message creation datetime in ISO 8601 format including timezone, for example
    2016-03-10T18:07:52.534Z
    """
    
    delivery_error_code: Optional[str] = None
    """ SMS only. Delivery error code returned by gateway """
    
    direction: Optional[CreateInternalTextMessageResponseDirection] = None
    """
    Message direction. Note that for some message types not all directions are allowed. For example
    voicemail messages can be only inbound
    """
    
    fax_page_count: Optional[int] = None
    """ Fax only. Page count in a fax message """
    
    fax_resolution: Optional[CreateInternalTextMessageResponseFaxResolution] = None
    """
    Fax only. Resolution of a fax message. 'High' for black and white image scanned at 200 dpi,
    'Low' for black and white image scanned at 100 dpi
    """
    
    from_: Optional[CreateInternalTextMessageResponseFrom] = field(metadata=config(field_name='from'), default=None)
    """ Sender information """
    
    last_modified_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """
    The datetime when the message was modified on server in ISO 8601 format including timezone, for
    example 2016-03-10T18:07:52.534Z
    """
    
    message_status: Optional[CreateInternalTextMessageResponseMessageStatus] = None
    """
    Message status. Different message types may have different allowed status values. For outbound
    faxes the aggregated message status is returned: If status for at least one recipient is
    'Queued', then 'Queued' value is returned If status for at least one recipient is
    'SendingFailed', then 'SendingFailed' value is returned In other cases Sent status is returned
    """
    
    pg_to_department: Optional[bool] = None
    """ 'Pager' only. 'True' if at least one of the message recipients is 'Department' extension """
    
    priority: Optional[CreateInternalTextMessageResponsePriority] = None
    """ Message priority """
    
    read_status: Optional[CreateInternalTextMessageResponseReadStatus] = None
    """ Message read status """
    
    sms_delivery_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """
    SMS only. The datetime when outbound SMS was delivered to recipient's handset in ISO 8601
    format including timezone, for example 2016-03-10T18:07:52.534Z. It is filled only if the
    carrier sends a delivery receipt to RingCentral
    """
    
    sms_sending_attempts_count: Optional[int] = None
    """
    SMS only. Number of attempts made to send an outbound SMS to the gateway (if gateway is
    temporary unavailable)
    """
    
    subject: Optional[str] = None
    """
    Message subject. For SMS and Pager messages it replicates message text which is also returned
    as an attachment
    """
    
    to: Optional[List[CreateInternalTextMessageResponseToItem]] = None
    """ Recipient information """
    
    type: Optional[CreateInternalTextMessageResponseType] = None
    """ Message type """
    
    vm_transcription_status: Optional[CreateInternalTextMessageResponseVmTranscriptionStatus] = None
    """
    Voicemail only. Status of voicemail to text transcription. If VoicemailToText feature is not
    activated for account, the 'NotAvailable' value is returned
    """
    
    cover_index: Optional[int] = None
    """
    Cover page identifier. For the list of available cover page identifiers please call the Fax
    Cover Pages method
    """
    
    cover_page_text: Optional[str] = None
    """
    Cover page text, entered by the fax sender and printed on the cover page. Maximum length is
    limited to 1024 symbols
    """
    

class CreateFaxMessageRequestFaxResolution(Enum):
    """ Resolution of Fax """
    
    High = 'High'
    Low = 'Low'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateFaxMessageRequest(DataClassJsonMixin):
    """
    Required Properties:
     - attachment
     - to
    
    Generated by Python OpenAPI Parser
    """
    
    attachment: bytes
    """ File to upload """
    
    to: List[str]
    """ To Phone Number """
    
    fax_resolution: Optional[CreateFaxMessageRequestFaxResolution] = None
    """ Resolution of Fax """
    
    send_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """ Timestamp to send fax at. If not specified (current or the past), the fax is sent immediately """
    
    iso_code: Optional[str] = None
    """ ISO Code. e.g UK """
    
    cover_index: Optional[int] = None
    """
    Cover page identifier. For the list of available cover page identifiers please call the method
    Fax Cover Pages. If not specified, the default cover page which is configured in 'Outbound Fax
    Settings' is attached
    """
    
    cover_page_text: Optional[str] = None
    """
    Cover page text, entered by the fax sender and printed on the cover page. Maximum length is
    limited to 1024 symbols
    """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateFaxMessageResponseFrom(DataClassJsonMixin):
    """ Sender information """
    
    phone_number: Optional[str] = None
    name: Optional[str] = None
    location: Optional[str] = None

class CreateFaxMessageResponseToItemMessageStatus(Enum):
    Sent = 'Sent'
    SendingFailed = 'SendingFailed'
    Queued = 'Queued'

class CreateFaxMessageResponseToItemFaxErrorCode(Enum):
    Undefined = 'Undefined'
    NoFaxSendPermission = 'NoFaxSendPermission'
    NoInternationalPermission = 'NoInternationalPermission'
    NoFaxMachine = 'NoFaxMachine'
    NoAnswer = 'NoAnswer'
    LineBusy = 'LineBusy'
    CallerHungUp = 'CallerHungUp'
    NotEnoughCredits = 'NotEnoughCredits'
    SentPartially = 'SentPartially'
    InternationalCallingDisabled = 'InternationalCallingDisabled'
    DestinationCountryDisabled = 'DestinationCountryDisabled'
    UnknownCountryCode = 'UnknownCountryCode'
    NotAccepted = 'NotAccepted'
    InvalidNumber = 'InvalidNumber'
    CallDeclined = 'CallDeclined'
    TooManyCallsPerLine = 'TooManyCallsPerLine'
    CallFailed = 'CallFailed'
    RenderingFailed = 'RenderingFailed'
    TooManyPages = 'TooManyPages'
    ReturnToDBQueue = 'ReturnToDBQueue'
    NoCallTime = 'NoCallTime'
    WrongNumber = 'WrongNumber'
    ProhibitedNumber = 'ProhibitedNumber'
    InternalError = 'InternalError'
    FaxSendingProhibited = 'FaxSendingProhibited'
    ThePhoneIsBlacklisted = 'ThePhoneIsBlacklisted'
    UserNotFound = 'UserNotFound'
    ConvertError = 'ConvertError'
    DBGeneralError = 'DBGeneralError'
    SkypeBillingFailed = 'SkypeBillingFailed'
    AccountSuspended = 'AccountSuspended'
    ProhibitedDestination = 'ProhibitedDestination'
    InternationalDisabled = 'InternationalDisabled'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateFaxMessageResponseToItem(DataClassJsonMixin):
    phone_number: Optional[str] = None
    name: Optional[str] = None
    location: Optional[str] = None
    message_status: Optional[CreateFaxMessageResponseToItemMessageStatus] = None
    fax_error_code: Optional[CreateFaxMessageResponseToItemFaxErrorCode] = None

class CreateFaxMessageResponseReadStatus(Enum):
    """ Message read status """
    
    Read = 'Read'
    Unread = 'Unread'

class CreateFaxMessageResponsePriority(Enum):
    """ Message priority """
    
    Normal = 'Normal'
    High = 'High'

class CreateFaxMessageResponseAttachmentsItemType(Enum):
    """ Type of message attachment """
    
    AudioRecording = 'AudioRecording'
    AudioTranscription = 'AudioTranscription'
    Text = 'Text'
    SourceDocument = 'SourceDocument'
    RenderedDocument = 'RenderedDocument'
    MmsAttachment = 'MmsAttachment'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateFaxMessageResponseAttachmentsItem(DataClassJsonMixin):
    id: Optional[int] = None
    """ Internal identifier of a message attachment """
    
    uri: Optional[str] = None
    """ Canonical URI of a message attachment """
    
    type: Optional[CreateFaxMessageResponseAttachmentsItemType] = None
    """ Type of message attachment """
    
    content_type: Optional[str] = None
    """ MIME type for a given attachment, for instance 'audio/wav' """
    
    vm_duration: Optional[int] = None
    """ Voicemail only Duration of the voicemail in seconds """
    
    filename: Optional[str] = None
    """ Name of a file attached """
    
    size: Optional[int] = None
    """ Size of attachment in bytes """
    

class CreateFaxMessageResponseDirection(Enum):
    """ Message direction """
    
    Inbound = 'Inbound'
    Outbound = 'Outbound'

class CreateFaxMessageResponseAvailability(Enum):
    """
    Message availability status. Message in 'Deleted' state is still preserved with all its
    attachments and can be restored. 'Purged' means that all attachments are already deleted and
    the message itself is about to be physically deleted shortly
    
    Generated by Python OpenAPI Parser
    """
    
    Alive = 'Alive'
    Deleted = 'Deleted'
    Purged = 'Purged'

class CreateFaxMessageResponseMessageStatus(Enum):
    """
    Message status. 'Queued' - the message is queued for sending; 'Sent' - a message is
    successfully sent; 'SendingFailed' - a message sending attempt has failed; 'Received' - a
    message is received (inbound messages have this status by default)
    
    Generated by Python OpenAPI Parser
    """
    
    Queued = 'Queued'
    Sent = 'Sent'
    SendingFailed = 'SendingFailed'
    Received = 'Received'

class CreateFaxMessageResponseFaxResolution(Enum):
    """
    Resolution of a fax message. ('High' for black and white image scanned at 200 dpi, 'Low' for
    black and white image scanned at 100 dpi)
    
    Generated by Python OpenAPI Parser
    """
    
    High = 'High'
    Low = 'Low'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateFaxMessageResponse(DataClassJsonMixin):
    id: Optional[int] = None
    """ Internal identifier of a message """
    
    uri: Optional[str] = None
    """ Canonical URI of a message """
    
    type: Optional[str] = None
    """ Message type - 'Fax' """
    
    from_: Optional[CreateFaxMessageResponseFrom] = field(metadata=config(field_name='from'), default=None)
    """ Sender information """
    
    to: Optional[List[CreateFaxMessageResponseToItem]] = None
    """ Recipient information """
    
    creation_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """
    Message creation datetime in ISO 8601 format including timezone, for example
    2016-03-10T18:07:52.534Z
    """
    
    read_status: Optional[CreateFaxMessageResponseReadStatus] = None
    """ Message read status """
    
    priority: Optional[CreateFaxMessageResponsePriority] = None
    """ Message priority """
    
    attachments: Optional[List[CreateFaxMessageResponseAttachmentsItem]] = None
    """ The list of message attachments """
    
    direction: Optional[CreateFaxMessageResponseDirection] = None
    """ Message direction """
    
    availability: Optional[CreateFaxMessageResponseAvailability] = None
    """
    Message availability status. Message in 'Deleted' state is still preserved with all its
    attachments and can be restored. 'Purged' means that all attachments are already deleted and
    the message itself is about to be physically deleted shortly
    """
    
    message_status: Optional[CreateFaxMessageResponseMessageStatus] = None
    """
    Message status. 'Queued' - the message is queued for sending; 'Sent' - a message is
    successfully sent; 'SendingFailed' - a message sending attempt has failed; 'Received' - a
    message is received (inbound messages have this status by default)
    """
    
    fax_resolution: Optional[CreateFaxMessageResponseFaxResolution] = None
    """
    Resolution of a fax message. ('High' for black and white image scanned at 200 dpi, 'Low' for
    black and white image scanned at 100 dpi)
    """
    
    fax_page_count: Optional[int] = None
    """ Page count in a fax message """
    
    last_modified_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """
    Datetime when the message was modified on server in ISO 8601 format including timezone, for
    example 2016-03-10T18:07:52.534Z
    """
    
    cover_index: Optional[int] = None
    """
    Cover page identifier. For the list of available cover page identifiers please call the Fax
    Cover Pages method
    """
    
    cover_page_text: Optional[str] = None
    """
    Cover page text, entered by the fax sender and printed on the cover page. Maximum length is
    limited to 1024 symbols
    """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListFaxCoverPagesResponseRecordsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """
    Internal identifier of a fax cover page. The possible value range is 0-13 (for language setting
    en-US) and 0, 15-28 (for all other languages)
    """
    
    name: Optional[str] = None
    """ Name of a fax cover page pattern """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListFaxCoverPagesResponseNavigationFirstPage(DataClassJsonMixin):
    """ Canonical URI for the first page of the list """
    
    uri: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListFaxCoverPagesResponseNavigationNextPage(DataClassJsonMixin):
    """ Canonical URI for the next page of the list """
    
    uri: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListFaxCoverPagesResponseNavigationPreviousPage(DataClassJsonMixin):
    """ Canonical URI for the previous page of the list """
    
    uri: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListFaxCoverPagesResponseNavigationLastPage(DataClassJsonMixin):
    """ Canonical URI for the last page of the list """
    
    uri: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListFaxCoverPagesResponseNavigation(DataClassJsonMixin):
    """ Information on navigation """
    
    first_page: Optional[ListFaxCoverPagesResponseNavigationFirstPage] = None
    """ Canonical URI for the first page of the list """
    
    next_page: Optional[ListFaxCoverPagesResponseNavigationNextPage] = None
    """ Canonical URI for the next page of the list """
    
    previous_page: Optional[ListFaxCoverPagesResponseNavigationPreviousPage] = None
    """ Canonical URI for the previous page of the list """
    
    last_page: Optional[ListFaxCoverPagesResponseNavigationLastPage] = None
    """ Canonical URI for the last page of the list """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListFaxCoverPagesResponsePaging(DataClassJsonMixin):
    """ Information on paging """
    
    page: Optional[int] = None
    """
    The current page number. 1-indexed, so the first page is 1 by default. May be omitted if result
    is empty (because non-existent page was specified or perPage=0 was requested)
    """
    
    per_page: Optional[int] = None
    """
    Current page size, describes how many items are in each page. Default value is 100. Maximum
    value is 1000. If perPage value in the request is greater than 1000, the maximum value (1000)
    is applied
    """
    
    page_start: Optional[int] = None
    """
    The zero-based number of the first element on the current page. Omitted if the page is omitted
    or result is empty
    """
    
    page_end: Optional[int] = None
    """
    The zero-based index of the last element on the current page. Omitted if the page is omitted or
    result is empty
    """
    
    total_pages: Optional[int] = None
    """
    The total number of pages in a dataset. May be omitted for some resources due to performance
    reasons
    """
    
    total_elements: Optional[int] = None
    """
    The total number of elements in a dataset. May be omitted for some resource due to performance
    reasons
    """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListFaxCoverPagesResponse(DataClassJsonMixin):
    uri: Optional[str] = None
    records: Optional[List[ListFaxCoverPagesResponseRecordsItem]] = None
    navigation: Optional[ListFaxCoverPagesResponseNavigation] = None
    """ Information on navigation """
    
    paging: Optional[ListFaxCoverPagesResponsePaging] = None
    """ Information on paging """
    

class ListMessagesAvailabilityItem(Enum):
    Alive = 'Alive'
    Deleted = 'Deleted'
    Purged = 'Purged'

class ListMessagesDirectionItem(Enum):
    Inbound = 'Inbound'
    Outbound = 'Outbound'

class ListMessagesMessageTypeItem(Enum):
    Fax = 'Fax'
    SMS = 'SMS'
    VoiceMail = 'VoiceMail'
    Pager = 'Pager'
    Text = 'Text'

class ListMessagesReadStatusItem(Enum):
    Read = 'Read'
    Unread = 'Unread'

class ListMessagesResponseRecordsItemAttachmentsItemType(Enum):
    """ Type of message attachment """
    
    AudioRecording = 'AudioRecording'
    AudioTranscription = 'AudioTranscription'
    Text = 'Text'
    SourceDocument = 'SourceDocument'
    RenderedDocument = 'RenderedDocument'
    MmsAttachment = 'MmsAttachment'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListMessagesResponseRecordsItemAttachmentsItem(DataClassJsonMixin):
    id: Optional[int] = None
    """ Internal identifier of a message attachment """
    
    uri: Optional[str] = None
    """ Canonical URI of a message attachment """
    
    type: Optional[ListMessagesResponseRecordsItemAttachmentsItemType] = None
    """ Type of message attachment """
    
    content_type: Optional[str] = None
    """ MIME type for a given attachment, for instance 'audio/wav' """
    
    vm_duration: Optional[int] = None
    """ Supported for `Voicemail` only. Duration of a voicemail in seconds """
    
    file_name: Optional[str] = None
    """ Name of a file attached """
    
    size: Optional[int] = None
    """ Size of attachment in bytes """
    
    height: Optional[int] = None
    """ Attachment height in pixels if available """
    
    width: Optional[int] = None
    """ Attachment width in pixels if available """
    

class ListMessagesResponseRecordsItemAvailability(Enum):
    """
    Message availability status. Message in 'Deleted' state is still preserved with all its
    attachments and can be restored. 'Purged' means that all attachments are already deleted and
    the message itself is about to be physically deleted shortly
    
    Generated by Python OpenAPI Parser
    """
    
    Alive = 'Alive'
    Deleted = 'Deleted'
    Purged = 'Purged'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListMessagesResponseRecordsItemConversation(DataClassJsonMixin):
    """ SMS and Pager only. Identifier of a conversation the message belongs to """
    
    id: Optional[str] = None
    """ Internal identifier of a conversation """
    
    uri: Optional[str] = None
    """ Deprecated. Link to a conversation resource """
    

class ListMessagesResponseRecordsItemDirection(Enum):
    """
    Message direction. Note that for some message types not all directions are allowed. For example
    voicemail messages can be only inbound
    
    Generated by Python OpenAPI Parser
    """
    
    Inbound = 'Inbound'
    Outbound = 'Outbound'

class ListMessagesResponseRecordsItemFaxResolution(Enum):
    """
    Fax only. Resolution of a fax message. 'High' for black and white image scanned at 200 dpi,
    'Low' for black and white image scanned at 100 dpi
    
    Generated by Python OpenAPI Parser
    """
    
    High = 'High'
    Low = 'Low'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListMessagesResponseRecordsItemFrom(DataClassJsonMixin):
    """ Sender information """
    
    extension_number: Optional[str] = None
    """
    Extension short number (usually 3 or 4 digits). This property is filled when parties
    communicate by means of short internal numbers, for example when calling to other extension or
    sending/receiving Company Pager message
    """
    
    extension_id: Optional[str] = None
    """ Internal identifier of an extension """
    
    location: Optional[str] = None
    """
    Contains party location (city, state) if one can be determined from phoneNumber. This property
    is filled only when phoneNumber is not empty and server can calculate location information from
    it (for example, this information is unavailable for US toll-free numbers)
    """
    
    name: Optional[str] = None
    """
    Symbolic name associated with a party. If the phone does not belong to the known extension,
    only the location is returned, the name is not determined then
    """
    
    phone_number: Optional[str] = None
    """
    Phone number of a party. Usually it is a plain number including country and area code like
    18661234567. But sometimes it could be returned from database with some formatting applied, for
    example (866)123-4567. This property is filled in all cases where parties communicate by means
    of global phone numbers, for example when calling to direct numbers or sending/receiving SMS
    """
    

class ListMessagesResponseRecordsItemMessageStatus(Enum):
    """
    Message status. Different message types may have different allowed status values. For outbound
    faxes the aggregated message status is returned: If status for at least one recipient is
    'Queued', then 'Queued' value is returned If status for at least one recipient is
    'SendingFailed', then 'SendingFailed' value is returned In other cases Sent status is returned
    
    Generated by Python OpenAPI Parser
    """
    
    Queued = 'Queued'
    Sent = 'Sent'
    Delivered = 'Delivered'
    DeliveryFailed = 'DeliveryFailed'
    SendingFailed = 'SendingFailed'
    Received = 'Received'

class ListMessagesResponseRecordsItemPriority(Enum):
    """ Message priority """
    
    Normal = 'Normal'
    High = 'High'

class ListMessagesResponseRecordsItemReadStatus(Enum):
    """ Message read status """
    
    Read = 'Read'
    Unread = 'Unread'

class ListMessagesResponseRecordsItemToItemMessageStatus(Enum):
    """ Status of a message. Returned for outbound fax messages only """
    
    Queued = 'Queued'
    Sent = 'Sent'
    Delivered = 'Delivered'
    DeliveryFailed = 'DeliveryFailed'
    SendingFailed = 'SendingFailed'
    Received = 'Received'

class ListMessagesResponseRecordsItemToItemFaxErrorCode(Enum):
    """
    Error code returned in case of fax sending failure. Returned if messageStatus value is
    'SendingFailed'. Supported for fax messages only
    
    Generated by Python OpenAPI Parser
    """
    
    AllLinesInUse = 'AllLinesInUse'
    Undefined = 'Undefined'
    NoFaxSendPermission = 'NoFaxSendPermission'
    NoInternationalPermission = 'NoInternationalPermission'
    NoFaxMachine = 'NoFaxMachine'
    NoAnswer = 'NoAnswer'
    LineBusy = 'LineBusy'
    CallerHungUp = 'CallerHungUp'
    NotEnoughCredits = 'NotEnoughCredits'
    SentPartially = 'SentPartially'
    InternationalCallingDisabled = 'InternationalCallingDisabled'
    DestinationCountryDisabled = 'DestinationCountryDisabled'
    UnknownCountryCode = 'UnknownCountryCode'
    NotAccepted = 'NotAccepted'
    InvalidNumber = 'InvalidNumber'
    CallDeclined = 'CallDeclined'
    TooManyCallsPerLine = 'TooManyCallsPerLine'
    CallFailed = 'CallFailed'
    RenderingFailed = 'RenderingFailed'
    TooManyPages = 'TooManyPages'
    ReturnToDBQueue = 'ReturnToDBQueue'
    NoCallTime = 'NoCallTime'
    WrongNumber = 'WrongNumber'
    ProhibitedNumber = 'ProhibitedNumber'
    InternalError = 'InternalError'
    FaxSendingProhibited = 'FaxSendingProhibited'
    ThePhoneIsBlacklisted = 'ThePhoneIsBlacklisted'
    UserNotFound = 'UserNotFound'
    ConvertError = 'ConvertError'
    DBGeneralError = 'DBGeneralError'
    SkypeBillingFailed = 'SkypeBillingFailed'
    AccountSuspended = 'AccountSuspended'
    ProhibitedDestination = 'ProhibitedDestination'
    InternationalDisabled = 'InternationalDisabled'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListMessagesResponseRecordsItemToItem(DataClassJsonMixin):
    extension_number: Optional[str] = None
    """
    Extension short number (usually 3 or 4 digits). This property is filled when parties
    communicate by means of short internal numbers, for example when calling to other extension or
    sending/receiving Company Pager message
    """
    
    extension_id: Optional[str] = None
    location: Optional[str] = None
    """
    Contains party location (city, state) if one can be determined from phoneNumber. This property
    is filled only when phoneNumber is not empty and server can calculate location information from
    it (for example, this information is unavailable for US toll-free numbers)
    """
    
    target: Optional[bool] = None
    """
    'True' specifies that message is sent exactly to this recipient. Returned in to field for group
    MMS. Useful if one extension has several phone numbers
    """
    
    message_status: Optional[ListMessagesResponseRecordsItemToItemMessageStatus] = None
    """ Status of a message. Returned for outbound fax messages only """
    
    fax_error_code: Optional[ListMessagesResponseRecordsItemToItemFaxErrorCode] = None
    """
    Error code returned in case of fax sending failure. Returned if messageStatus value is
    'SendingFailed'. Supported for fax messages only
    """
    
    name: Optional[str] = None
    """
    Symbolic name associated with a party. If the phone does not belong to the known extension,
    only the location is returned, the name is not determined then
    """
    
    phone_number: Optional[str] = None
    """
    Phone number of a party. Usually it is a plain number including country and area code like
    18661234567. But sometimes it could be returned from database with some formatting applied, for
    example (866)123-4567. This property is filled in all cases where parties communicate by means
    of global phone numbers, for example when calling to direct numbers or sending/receiving SMS
    """
    

class ListMessagesResponseRecordsItemType(Enum):
    """ Message type """
    
    Fax = 'Fax'
    SMS = 'SMS'
    VoiceMail = 'VoiceMail'
    Pager = 'Pager'
    Text = 'Text'

class ListMessagesResponseRecordsItemVmTranscriptionStatus(Enum):
    """
    Voicemail only. Status of voicemail to text transcription. If VoicemailToText feature is not
    activated for account, the 'NotAvailable' value is returned
    
    Generated by Python OpenAPI Parser
    """
    
    NotAvailable = 'NotAvailable'
    InProgress = 'InProgress'
    TimedOut = 'TimedOut'
    Completed = 'Completed'
    CompletedPartially = 'CompletedPartially'
    Failed = 'Failed'
    Unknown = 'Unknown'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListMessagesResponseRecordsItem(DataClassJsonMixin):
    id: Optional[int] = None
    """ Internal identifier of a message """
    
    uri: Optional[str] = None
    """ Canonical URI of a message """
    
    attachments: Optional[List[ListMessagesResponseRecordsItemAttachmentsItem]] = None
    """ The list of message attachments """
    
    availability: Optional[ListMessagesResponseRecordsItemAvailability] = None
    """
    Message availability status. Message in 'Deleted' state is still preserved with all its
    attachments and can be restored. 'Purged' means that all attachments are already deleted and
    the message itself is about to be physically deleted shortly
    """
    
    conversation_id: Optional[int] = None
    """ SMS and Pager only. Identifier of a conversation the message belongs to """
    
    conversation: Optional[ListMessagesResponseRecordsItemConversation] = None
    """ SMS and Pager only. Identifier of a conversation the message belongs to """
    
    creation_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """
    Message creation datetime in ISO 8601 format including timezone, for example
    2016-03-10T18:07:52.534Z
    """
    
    delivery_error_code: Optional[str] = None
    """ SMS only. Delivery error code returned by gateway """
    
    direction: Optional[ListMessagesResponseRecordsItemDirection] = None
    """
    Message direction. Note that for some message types not all directions are allowed. For example
    voicemail messages can be only inbound
    """
    
    fax_page_count: Optional[int] = None
    """ Fax only. Page count in a fax message """
    
    fax_resolution: Optional[ListMessagesResponseRecordsItemFaxResolution] = None
    """
    Fax only. Resolution of a fax message. 'High' for black and white image scanned at 200 dpi,
    'Low' for black and white image scanned at 100 dpi
    """
    
    from_: Optional[ListMessagesResponseRecordsItemFrom] = field(metadata=config(field_name='from'), default=None)
    """ Sender information """
    
    last_modified_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """
    The datetime when the message was modified on server in ISO 8601 format including timezone, for
    example 2016-03-10T18:07:52.534Z
    """
    
    message_status: Optional[ListMessagesResponseRecordsItemMessageStatus] = None
    """
    Message status. Different message types may have different allowed status values. For outbound
    faxes the aggregated message status is returned: If status for at least one recipient is
    'Queued', then 'Queued' value is returned If status for at least one recipient is
    'SendingFailed', then 'SendingFailed' value is returned In other cases Sent status is returned
    """
    
    pg_to_department: Optional[bool] = None
    """ 'Pager' only. 'True' if at least one of the message recipients is 'Department' extension """
    
    priority: Optional[ListMessagesResponseRecordsItemPriority] = None
    """ Message priority """
    
    read_status: Optional[ListMessagesResponseRecordsItemReadStatus] = None
    """ Message read status """
    
    sms_delivery_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """
    SMS only. The datetime when outbound SMS was delivered to recipient's handset in ISO 8601
    format including timezone, for example 2016-03-10T18:07:52.534Z. It is filled only if the
    carrier sends a delivery receipt to RingCentral
    """
    
    sms_sending_attempts_count: Optional[int] = None
    """
    SMS only. Number of attempts made to send an outbound SMS to the gateway (if gateway is
    temporary unavailable)
    """
    
    subject: Optional[str] = None
    """
    Message subject. For SMS and Pager messages it replicates message text which is also returned
    as an attachment
    """
    
    to: Optional[List[ListMessagesResponseRecordsItemToItem]] = None
    """ Recipient information """
    
    type: Optional[ListMessagesResponseRecordsItemType] = None
    """ Message type """
    
    vm_transcription_status: Optional[ListMessagesResponseRecordsItemVmTranscriptionStatus] = None
    """
    Voicemail only. Status of voicemail to text transcription. If VoicemailToText feature is not
    activated for account, the 'NotAvailable' value is returned
    """
    
    cover_index: Optional[int] = None
    """
    Cover page identifier. For the list of available cover page identifiers please call the Fax
    Cover Pages method
    """
    
    cover_page_text: Optional[str] = None
    """
    Cover page text, entered by the fax sender and printed on the cover page. Maximum length is
    limited to 1024 symbols
    """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListMessagesResponseNavigationFirstPage(DataClassJsonMixin):
    """ Canonical URI for the first page of the list """
    
    uri: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListMessagesResponseNavigationNextPage(DataClassJsonMixin):
    """ Canonical URI for the next page of the list """
    
    uri: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListMessagesResponseNavigationPreviousPage(DataClassJsonMixin):
    """ Canonical URI for the previous page of the list """
    
    uri: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListMessagesResponseNavigationLastPage(DataClassJsonMixin):
    """ Canonical URI for the last page of the list """
    
    uri: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListMessagesResponseNavigation(DataClassJsonMixin):
    """ Information on navigation """
    
    first_page: Optional[ListMessagesResponseNavigationFirstPage] = None
    """ Canonical URI for the first page of the list """
    
    next_page: Optional[ListMessagesResponseNavigationNextPage] = None
    """ Canonical URI for the next page of the list """
    
    previous_page: Optional[ListMessagesResponseNavigationPreviousPage] = None
    """ Canonical URI for the previous page of the list """
    
    last_page: Optional[ListMessagesResponseNavigationLastPage] = None
    """ Canonical URI for the last page of the list """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListMessagesResponsePaging(DataClassJsonMixin):
    """ Information on paging """
    
    page: Optional[int] = None
    """
    The current page number. 1-indexed, so the first page is 1 by default. May be omitted if result
    is empty (because non-existent page was specified or perPage=0 was requested)
    """
    
    per_page: Optional[int] = None
    """
    Current page size, describes how many items are in each page. Default value is 100. Maximum
    value is 1000. If perPage value in the request is greater than 1000, the maximum value (1000)
    is applied
    """
    
    page_start: Optional[int] = None
    """
    The zero-based number of the first element on the current page. Omitted if the page is omitted
    or result is empty
    """
    
    page_end: Optional[int] = None
    """
    The zero-based index of the last element on the current page. Omitted if the page is omitted or
    result is empty
    """
    
    total_pages: Optional[int] = None
    """
    The total number of pages in a dataset. May be omitted for some resources due to performance
    reasons
    """
    
    total_elements: Optional[int] = None
    """
    The total number of elements in a dataset. May be omitted for some resource due to performance
    reasons
    """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListMessagesResponse(DataClassJsonMixin):
    """
    Required Properties:
     - navigation
     - paging
     - records
    
    Generated by Python OpenAPI Parser
    """
    
    records: List[ListMessagesResponseRecordsItem]
    """ List of records with message information """
    
    navigation: ListMessagesResponseNavigation
    """ Information on navigation """
    
    paging: ListMessagesResponsePaging
    """ Information on paging """
    
    uri: Optional[str] = None
    """ Link to the list of user messages """
    

class DeleteMessageByFilterType(Enum):
    Fax = 'Fax'
    SMS = 'SMS'
    VoiceMail = 'VoiceMail'
    Pager = 'Pager'
    Text = 'Text'
    All = 'All'

class ReadMessageResponseAttachmentsItemType(Enum):
    """ Type of message attachment """
    
    AudioRecording = 'AudioRecording'
    AudioTranscription = 'AudioTranscription'
    Text = 'Text'
    SourceDocument = 'SourceDocument'
    RenderedDocument = 'RenderedDocument'
    MmsAttachment = 'MmsAttachment'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadMessageResponseAttachmentsItem(DataClassJsonMixin):
    id: Optional[int] = None
    """ Internal identifier of a message attachment """
    
    uri: Optional[str] = None
    """ Canonical URI of a message attachment """
    
    type: Optional[ReadMessageResponseAttachmentsItemType] = None
    """ Type of message attachment """
    
    content_type: Optional[str] = None
    """ MIME type for a given attachment, for instance 'audio/wav' """
    
    vm_duration: Optional[int] = None
    """ Supported for `Voicemail` only. Duration of a voicemail in seconds """
    
    file_name: Optional[str] = None
    """ Name of a file attached """
    
    size: Optional[int] = None
    """ Size of attachment in bytes """
    
    height: Optional[int] = None
    """ Attachment height in pixels if available """
    
    width: Optional[int] = None
    """ Attachment width in pixels if available """
    

class ReadMessageResponseAvailability(Enum):
    """
    Message availability status. Message in 'Deleted' state is still preserved with all its
    attachments and can be restored. 'Purged' means that all attachments are already deleted and
    the message itself is about to be physically deleted shortly
    
    Generated by Python OpenAPI Parser
    """
    
    Alive = 'Alive'
    Deleted = 'Deleted'
    Purged = 'Purged'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadMessageResponseConversation(DataClassJsonMixin):
    """ SMS and Pager only. Identifier of a conversation the message belongs to """
    
    id: Optional[str] = None
    """ Internal identifier of a conversation """
    
    uri: Optional[str] = None
    """ Deprecated. Link to a conversation resource """
    

class ReadMessageResponseDirection(Enum):
    """
    Message direction. Note that for some message types not all directions are allowed. For example
    voicemail messages can be only inbound
    
    Generated by Python OpenAPI Parser
    """
    
    Inbound = 'Inbound'
    Outbound = 'Outbound'

class ReadMessageResponseFaxResolution(Enum):
    """
    Fax only. Resolution of a fax message. 'High' for black and white image scanned at 200 dpi,
    'Low' for black and white image scanned at 100 dpi
    
    Generated by Python OpenAPI Parser
    """
    
    High = 'High'
    Low = 'Low'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadMessageResponseFrom(DataClassJsonMixin):
    """ Sender information """
    
    extension_number: Optional[str] = None
    """
    Extension short number (usually 3 or 4 digits). This property is filled when parties
    communicate by means of short internal numbers, for example when calling to other extension or
    sending/receiving Company Pager message
    """
    
    extension_id: Optional[str] = None
    """ Internal identifier of an extension """
    
    location: Optional[str] = None
    """
    Contains party location (city, state) if one can be determined from phoneNumber. This property
    is filled only when phoneNumber is not empty and server can calculate location information from
    it (for example, this information is unavailable for US toll-free numbers)
    """
    
    name: Optional[str] = None
    """
    Symbolic name associated with a party. If the phone does not belong to the known extension,
    only the location is returned, the name is not determined then
    """
    
    phone_number: Optional[str] = None
    """
    Phone number of a party. Usually it is a plain number including country and area code like
    18661234567. But sometimes it could be returned from database with some formatting applied, for
    example (866)123-4567. This property is filled in all cases where parties communicate by means
    of global phone numbers, for example when calling to direct numbers or sending/receiving SMS
    """
    

class ReadMessageResponseMessageStatus(Enum):
    """
    Message status. Different message types may have different allowed status values. For outbound
    faxes the aggregated message status is returned: If status for at least one recipient is
    'Queued', then 'Queued' value is returned If status for at least one recipient is
    'SendingFailed', then 'SendingFailed' value is returned In other cases Sent status is returned
    
    Generated by Python OpenAPI Parser
    """
    
    Queued = 'Queued'
    Sent = 'Sent'
    Delivered = 'Delivered'
    DeliveryFailed = 'DeliveryFailed'
    SendingFailed = 'SendingFailed'
    Received = 'Received'

class ReadMessageResponsePriority(Enum):
    """ Message priority """
    
    Normal = 'Normal'
    High = 'High'

class ReadMessageResponseReadStatus(Enum):
    """ Message read status """
    
    Read = 'Read'
    Unread = 'Unread'

class ReadMessageResponseToItemMessageStatus(Enum):
    """ Status of a message. Returned for outbound fax messages only """
    
    Queued = 'Queued'
    Sent = 'Sent'
    Delivered = 'Delivered'
    DeliveryFailed = 'DeliveryFailed'
    SendingFailed = 'SendingFailed'
    Received = 'Received'

class ReadMessageResponseToItemFaxErrorCode(Enum):
    """
    Error code returned in case of fax sending failure. Returned if messageStatus value is
    'SendingFailed'. Supported for fax messages only
    
    Generated by Python OpenAPI Parser
    """
    
    AllLinesInUse = 'AllLinesInUse'
    Undefined = 'Undefined'
    NoFaxSendPermission = 'NoFaxSendPermission'
    NoInternationalPermission = 'NoInternationalPermission'
    NoFaxMachine = 'NoFaxMachine'
    NoAnswer = 'NoAnswer'
    LineBusy = 'LineBusy'
    CallerHungUp = 'CallerHungUp'
    NotEnoughCredits = 'NotEnoughCredits'
    SentPartially = 'SentPartially'
    InternationalCallingDisabled = 'InternationalCallingDisabled'
    DestinationCountryDisabled = 'DestinationCountryDisabled'
    UnknownCountryCode = 'UnknownCountryCode'
    NotAccepted = 'NotAccepted'
    InvalidNumber = 'InvalidNumber'
    CallDeclined = 'CallDeclined'
    TooManyCallsPerLine = 'TooManyCallsPerLine'
    CallFailed = 'CallFailed'
    RenderingFailed = 'RenderingFailed'
    TooManyPages = 'TooManyPages'
    ReturnToDBQueue = 'ReturnToDBQueue'
    NoCallTime = 'NoCallTime'
    WrongNumber = 'WrongNumber'
    ProhibitedNumber = 'ProhibitedNumber'
    InternalError = 'InternalError'
    FaxSendingProhibited = 'FaxSendingProhibited'
    ThePhoneIsBlacklisted = 'ThePhoneIsBlacklisted'
    UserNotFound = 'UserNotFound'
    ConvertError = 'ConvertError'
    DBGeneralError = 'DBGeneralError'
    SkypeBillingFailed = 'SkypeBillingFailed'
    AccountSuspended = 'AccountSuspended'
    ProhibitedDestination = 'ProhibitedDestination'
    InternationalDisabled = 'InternationalDisabled'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadMessageResponseToItem(DataClassJsonMixin):
    extension_number: Optional[str] = None
    """
    Extension short number (usually 3 or 4 digits). This property is filled when parties
    communicate by means of short internal numbers, for example when calling to other extension or
    sending/receiving Company Pager message
    """
    
    extension_id: Optional[str] = None
    location: Optional[str] = None
    """
    Contains party location (city, state) if one can be determined from phoneNumber. This property
    is filled only when phoneNumber is not empty and server can calculate location information from
    it (for example, this information is unavailable for US toll-free numbers)
    """
    
    target: Optional[bool] = None
    """
    'True' specifies that message is sent exactly to this recipient. Returned in to field for group
    MMS. Useful if one extension has several phone numbers
    """
    
    message_status: Optional[ReadMessageResponseToItemMessageStatus] = None
    """ Status of a message. Returned for outbound fax messages only """
    
    fax_error_code: Optional[ReadMessageResponseToItemFaxErrorCode] = None
    """
    Error code returned in case of fax sending failure. Returned if messageStatus value is
    'SendingFailed'. Supported for fax messages only
    """
    
    name: Optional[str] = None
    """
    Symbolic name associated with a party. If the phone does not belong to the known extension,
    only the location is returned, the name is not determined then
    """
    
    phone_number: Optional[str] = None
    """
    Phone number of a party. Usually it is a plain number including country and area code like
    18661234567. But sometimes it could be returned from database with some formatting applied, for
    example (866)123-4567. This property is filled in all cases where parties communicate by means
    of global phone numbers, for example when calling to direct numbers or sending/receiving SMS
    """
    

class ReadMessageResponseType(Enum):
    """ Message type """
    
    Fax = 'Fax'
    SMS = 'SMS'
    VoiceMail = 'VoiceMail'
    Pager = 'Pager'
    Text = 'Text'

class ReadMessageResponseVmTranscriptionStatus(Enum):
    """
    Voicemail only. Status of voicemail to text transcription. If VoicemailToText feature is not
    activated for account, the 'NotAvailable' value is returned
    
    Generated by Python OpenAPI Parser
    """
    
    NotAvailable = 'NotAvailable'
    InProgress = 'InProgress'
    TimedOut = 'TimedOut'
    Completed = 'Completed'
    CompletedPartially = 'CompletedPartially'
    Failed = 'Failed'
    Unknown = 'Unknown'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadMessageResponse(DataClassJsonMixin):
    id: Optional[int] = None
    """ Internal identifier of a message """
    
    uri: Optional[str] = None
    """ Canonical URI of a message """
    
    attachments: Optional[List[ReadMessageResponseAttachmentsItem]] = None
    """ The list of message attachments """
    
    availability: Optional[ReadMessageResponseAvailability] = None
    """
    Message availability status. Message in 'Deleted' state is still preserved with all its
    attachments and can be restored. 'Purged' means that all attachments are already deleted and
    the message itself is about to be physically deleted shortly
    """
    
    conversation_id: Optional[int] = None
    """ SMS and Pager only. Identifier of a conversation the message belongs to """
    
    conversation: Optional[ReadMessageResponseConversation] = None
    """ SMS and Pager only. Identifier of a conversation the message belongs to """
    
    creation_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """
    Message creation datetime in ISO 8601 format including timezone, for example
    2016-03-10T18:07:52.534Z
    """
    
    delivery_error_code: Optional[str] = None
    """ SMS only. Delivery error code returned by gateway """
    
    direction: Optional[ReadMessageResponseDirection] = None
    """
    Message direction. Note that for some message types not all directions are allowed. For example
    voicemail messages can be only inbound
    """
    
    fax_page_count: Optional[int] = None
    """ Fax only. Page count in a fax message """
    
    fax_resolution: Optional[ReadMessageResponseFaxResolution] = None
    """
    Fax only. Resolution of a fax message. 'High' for black and white image scanned at 200 dpi,
    'Low' for black and white image scanned at 100 dpi
    """
    
    from_: Optional[ReadMessageResponseFrom] = field(metadata=config(field_name='from'), default=None)
    """ Sender information """
    
    last_modified_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """
    The datetime when the message was modified on server in ISO 8601 format including timezone, for
    example 2016-03-10T18:07:52.534Z
    """
    
    message_status: Optional[ReadMessageResponseMessageStatus] = None
    """
    Message status. Different message types may have different allowed status values. For outbound
    faxes the aggregated message status is returned: If status for at least one recipient is
    'Queued', then 'Queued' value is returned If status for at least one recipient is
    'SendingFailed', then 'SendingFailed' value is returned In other cases Sent status is returned
    """
    
    pg_to_department: Optional[bool] = None
    """ 'Pager' only. 'True' if at least one of the message recipients is 'Department' extension """
    
    priority: Optional[ReadMessageResponsePriority] = None
    """ Message priority """
    
    read_status: Optional[ReadMessageResponseReadStatus] = None
    """ Message read status """
    
    sms_delivery_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """
    SMS only. The datetime when outbound SMS was delivered to recipient's handset in ISO 8601
    format including timezone, for example 2016-03-10T18:07:52.534Z. It is filled only if the
    carrier sends a delivery receipt to RingCentral
    """
    
    sms_sending_attempts_count: Optional[int] = None
    """
    SMS only. Number of attempts made to send an outbound SMS to the gateway (if gateway is
    temporary unavailable)
    """
    
    subject: Optional[str] = None
    """
    Message subject. For SMS and Pager messages it replicates message text which is also returned
    as an attachment
    """
    
    to: Optional[List[ReadMessageResponseToItem]] = None
    """ Recipient information """
    
    type: Optional[ReadMessageResponseType] = None
    """ Message type """
    
    vm_transcription_status: Optional[ReadMessageResponseVmTranscriptionStatus] = None
    """
    Voicemail only. Status of voicemail to text transcription. If VoicemailToText feature is not
    activated for account, the 'NotAvailable' value is returned
    """
    
    cover_index: Optional[int] = None
    """
    Cover page identifier. For the list of available cover page identifiers please call the Fax
    Cover Pages method
    """
    
    cover_page_text: Optional[str] = None
    """
    Cover page text, entered by the fax sender and printed on the cover page. Maximum length is
    limited to 1024 symbols
    """
    

class ReadMessageResponseBodyAttachmentsItemType(Enum):
    """ Type of message attachment """
    
    AudioRecording = 'AudioRecording'
    AudioTranscription = 'AudioTranscription'
    Text = 'Text'
    SourceDocument = 'SourceDocument'
    RenderedDocument = 'RenderedDocument'
    MmsAttachment = 'MmsAttachment'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadMessageResponseBodyAttachmentsItem(DataClassJsonMixin):
    id: Optional[int] = None
    """ Internal identifier of a message attachment """
    
    uri: Optional[str] = None
    """ Canonical URI of a message attachment """
    
    type: Optional[ReadMessageResponseBodyAttachmentsItemType] = None
    """ Type of message attachment """
    
    content_type: Optional[str] = None
    """ MIME type for a given attachment, for instance 'audio/wav' """
    
    vm_duration: Optional[int] = None
    """ Supported for `Voicemail` only. Duration of a voicemail in seconds """
    
    file_name: Optional[str] = None
    """ Name of a file attached """
    
    size: Optional[int] = None
    """ Size of attachment in bytes """
    
    height: Optional[int] = None
    """ Attachment height in pixels if available """
    
    width: Optional[int] = None
    """ Attachment width in pixels if available """
    

class ReadMessageResponseBodyAvailability(Enum):
    """
    Message availability status. Message in 'Deleted' state is still preserved with all its
    attachments and can be restored. 'Purged' means that all attachments are already deleted and
    the message itself is about to be physically deleted shortly
    
    Generated by Python OpenAPI Parser
    """
    
    Alive = 'Alive'
    Deleted = 'Deleted'
    Purged = 'Purged'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadMessageResponseBodyConversation(DataClassJsonMixin):
    """ SMS and Pager only. Identifier of a conversation the message belongs to """
    
    id: Optional[str] = None
    """ Internal identifier of a conversation """
    
    uri: Optional[str] = None
    """ Deprecated. Link to a conversation resource """
    

class ReadMessageResponseBodyDirection(Enum):
    """
    Message direction. Note that for some message types not all directions are allowed. For example
    voicemail messages can be only inbound
    
    Generated by Python OpenAPI Parser
    """
    
    Inbound = 'Inbound'
    Outbound = 'Outbound'

class ReadMessageResponseBodyFaxResolution(Enum):
    """
    Fax only. Resolution of a fax message. 'High' for black and white image scanned at 200 dpi,
    'Low' for black and white image scanned at 100 dpi
    
    Generated by Python OpenAPI Parser
    """
    
    High = 'High'
    Low = 'Low'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadMessageResponseBodyFrom(DataClassJsonMixin):
    """ Sender information """
    
    extension_number: Optional[str] = None
    extension_id: Optional[str] = None
    name: Optional[str] = None

class ReadMessageResponseBodyMessageStatus(Enum):
    """
    Message status. Different message types may have different allowed status values.For outbound
    faxes the aggregated message status is returned: If status for at least one recipient is
    'Queued', then 'Queued' value is returned If status for at least one recipient is
    'SendingFailed', then 'SendingFailed' value is returned In other cases Sent status is returned
    
    Generated by Python OpenAPI Parser
    """
    
    Queued = 'Queued'
    Sent = 'Sent'
    Delivered = 'Delivered'
    DeliveryFailed = 'DeliveryFailed'
    SendingFailed = 'SendingFailed'
    Received = 'Received'

class ReadMessageResponseBodyPriority(Enum):
    """ Message priority """
    
    Normal = 'Normal'
    High = 'High'

class ReadMessageResponseBodyReadStatus(Enum):
    """ Message read status """
    
    Read = 'Read'
    Unread = 'Unread'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadMessageResponseBodyToItem(DataClassJsonMixin):
    extension_number: Optional[str] = None
    extension_id: Optional[str] = None
    name: Optional[str] = None

class ReadMessageResponseBodyType(Enum):
    """ Message type """
    
    Fax = 'Fax'
    SMS = 'SMS'
    VoiceMail = 'VoiceMail'
    Pager = 'Pager'
    Text = 'Text'

class ReadMessageResponseBodyVmTranscriptionStatus(Enum):
    """
    Voicemail only. Status of voicemail to text transcription. If VoicemailToText feature is not
    activated for account, the 'NotAvailable' value is returned
    
    Generated by Python OpenAPI Parser
    """
    
    NotAvailable = 'NotAvailable'
    InProgress = 'InProgress'
    TimedOut = 'TimedOut'
    Completed = 'Completed'
    CompletedPartially = 'CompletedPartially'
    Failed = 'Failed'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadMessageResponseBody(DataClassJsonMixin):
    uri: Optional[str] = None
    """ Canonical URI of a message """
    
    id: Optional[str] = None
    """ Internal identifier of a message """
    
    attachments: Optional[List[ReadMessageResponseBodyAttachmentsItem]] = None
    """ The list of message attachments """
    
    availability: Optional[ReadMessageResponseBodyAvailability] = None
    """
    Message availability status. Message in 'Deleted' state is still preserved with all its
    attachments and can be restored. 'Purged' means that all attachments are already deleted and
    the message itself is about to be physically deleted shortly
    """
    
    conversation_id: Optional[int] = None
    """ SMS and Pager only. Identifier of a conversation the message belongs to """
    
    conversation: Optional[ReadMessageResponseBodyConversation] = None
    """ SMS and Pager only. Identifier of a conversation the message belongs to """
    
    creation_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """
    Message creation datetime in ISO 8601 format including timezone, for example
    2016-03-10T18:07:52.534Z
    """
    
    delivery_error_code: Optional[str] = None
    """ SMS only. Delivery error code returned by gateway """
    
    direction: Optional[ReadMessageResponseBodyDirection] = None
    """
    Message direction. Note that for some message types not all directions are allowed. For example
    voicemail messages can be only inbound
    """
    
    fax_page_count: Optional[int] = None
    """ Fax only. Page count in a fax message """
    
    fax_resolution: Optional[ReadMessageResponseBodyFaxResolution] = None
    """
    Fax only. Resolution of a fax message. 'High' for black and white image scanned at 200 dpi,
    'Low' for black and white image scanned at 100 dpi
    """
    
    from_: Optional[ReadMessageResponseBodyFrom] = field(metadata=config(field_name='from'), default=None)
    """ Sender information """
    
    last_modified_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """
    The datetime when the message was modified on server in ISO 8601 format including timezone, for
    example 2016-03-10T18:07:52.534Z
    """
    
    message_status: Optional[ReadMessageResponseBodyMessageStatus] = None
    """
    Message status. Different message types may have different allowed status values.For outbound
    faxes the aggregated message status is returned: If status for at least one recipient is
    'Queued', then 'Queued' value is returned If status for at least one recipient is
    'SendingFailed', then 'SendingFailed' value is returned In other cases Sent status is returned
    """
    
    pg_to_department: Optional[bool] = None
    """ 'Pager' only. 'True' if at least one of the message recipients is 'Department' extension """
    
    priority: Optional[ReadMessageResponseBodyPriority] = None
    """ Message priority """
    
    read_status: Optional[ReadMessageResponseBodyReadStatus] = None
    """ Message read status """
    
    sms_delivery_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """
    SMS only. The datetime when outbound SMS was delivered to recipient's handset in ISO 8601
    format including timezone, for example 2016-03-10T18:07:52.534Z. It is filled only if the
    carrier sends a delivery receipt to RingCentral
    """
    
    sms_sending_attempts_count: Optional[int] = None
    """
    SMS only. Number of attempts made to send an outbound SMS to the gateway (if gateway is
    temporary unavailable)
    """
    
    subject: Optional[str] = None
    """
    Message subject. For SMS and Pager messages it replicates message text which is also returned
    as an attachment
    """
    
    to: Optional[List[ReadMessageResponseBodyToItem]] = None
    """ Recipient information """
    
    type: Optional[ReadMessageResponseBodyType] = None
    """ Message type """
    
    vm_transcription_status: Optional[ReadMessageResponseBodyVmTranscriptionStatus] = None
    """
    Voicemail only. Status of voicemail to text transcription. If VoicemailToText feature is not
    activated for account, the 'NotAvailable' value is returned
    """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadMessageResponse(DataClassJsonMixin):
    resource_id: Optional[str] = None
    """ Internal identifier of a resource """
    
    status: Optional[int] = None
    """ Status code of resource retrieval """
    
    body: Optional[ReadMessageResponseBody] = None

class UpdateMessageType(Enum):
    Fax = 'Fax'
    SMS = 'SMS'
    VoiceMail = 'VoiceMail'
    Pager = 'Pager'
    Text = 'Text'
    All = 'All'

class UpdateMessageRequestReadStatus(Enum):
    """ Read status of a message to be changed. Multiple values are accepted """
    
    Read = 'Read'
    Unread = 'Unread'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateMessageRequest(DataClassJsonMixin):
    read_status: Optional[UpdateMessageRequestReadStatus] = None
    """ Read status of a message to be changed. Multiple values are accepted """
    

class UpdateMessageResponseAttachmentsItemType(Enum):
    """ Type of message attachment """
    
    AudioRecording = 'AudioRecording'
    AudioTranscription = 'AudioTranscription'
    Text = 'Text'
    SourceDocument = 'SourceDocument'
    RenderedDocument = 'RenderedDocument'
    MmsAttachment = 'MmsAttachment'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateMessageResponseAttachmentsItem(DataClassJsonMixin):
    id: Optional[int] = None
    """ Internal identifier of a message attachment """
    
    uri: Optional[str] = None
    """ Canonical URI of a message attachment """
    
    type: Optional[UpdateMessageResponseAttachmentsItemType] = None
    """ Type of message attachment """
    
    content_type: Optional[str] = None
    """ MIME type for a given attachment, for instance 'audio/wav' """
    
    vm_duration: Optional[int] = None
    """ Supported for `Voicemail` only. Duration of a voicemail in seconds """
    
    file_name: Optional[str] = None
    """ Name of a file attached """
    
    size: Optional[int] = None
    """ Size of attachment in bytes """
    
    height: Optional[int] = None
    """ Attachment height in pixels if available """
    
    width: Optional[int] = None
    """ Attachment width in pixels if available """
    

class UpdateMessageResponseAvailability(Enum):
    """
    Message availability status. Message in 'Deleted' state is still preserved with all its
    attachments and can be restored. 'Purged' means that all attachments are already deleted and
    the message itself is about to be physically deleted shortly
    
    Generated by Python OpenAPI Parser
    """
    
    Alive = 'Alive'
    Deleted = 'Deleted'
    Purged = 'Purged'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateMessageResponseConversation(DataClassJsonMixin):
    """ SMS and Pager only. Identifier of a conversation the message belongs to """
    
    id: Optional[str] = None
    """ Internal identifier of a conversation """
    
    uri: Optional[str] = None
    """ Deprecated. Link to a conversation resource """
    

class UpdateMessageResponseDirection(Enum):
    """
    Message direction. Note that for some message types not all directions are allowed. For example
    voicemail messages can be only inbound
    
    Generated by Python OpenAPI Parser
    """
    
    Inbound = 'Inbound'
    Outbound = 'Outbound'

class UpdateMessageResponseFaxResolution(Enum):
    """
    Fax only. Resolution of a fax message. 'High' for black and white image scanned at 200 dpi,
    'Low' for black and white image scanned at 100 dpi
    
    Generated by Python OpenAPI Parser
    """
    
    High = 'High'
    Low = 'Low'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateMessageResponseFrom(DataClassJsonMixin):
    """ Sender information """
    
    extension_number: Optional[str] = None
    """
    Extension short number (usually 3 or 4 digits). This property is filled when parties
    communicate by means of short internal numbers, for example when calling to other extension or
    sending/receiving Company Pager message
    """
    
    extension_id: Optional[str] = None
    """ Internal identifier of an extension """
    
    location: Optional[str] = None
    """
    Contains party location (city, state) if one can be determined from phoneNumber. This property
    is filled only when phoneNumber is not empty and server can calculate location information from
    it (for example, this information is unavailable for US toll-free numbers)
    """
    
    name: Optional[str] = None
    """
    Symbolic name associated with a party. If the phone does not belong to the known extension,
    only the location is returned, the name is not determined then
    """
    
    phone_number: Optional[str] = None
    """
    Phone number of a party. Usually it is a plain number including country and area code like
    18661234567. But sometimes it could be returned from database with some formatting applied, for
    example (866)123-4567. This property is filled in all cases where parties communicate by means
    of global phone numbers, for example when calling to direct numbers or sending/receiving SMS
    """
    

class UpdateMessageResponseMessageStatus(Enum):
    """
    Message status. Different message types may have different allowed status values. For outbound
    faxes the aggregated message status is returned: If status for at least one recipient is
    'Queued', then 'Queued' value is returned If status for at least one recipient is
    'SendingFailed', then 'SendingFailed' value is returned In other cases Sent status is returned
    
    Generated by Python OpenAPI Parser
    """
    
    Queued = 'Queued'
    Sent = 'Sent'
    Delivered = 'Delivered'
    DeliveryFailed = 'DeliveryFailed'
    SendingFailed = 'SendingFailed'
    Received = 'Received'

class UpdateMessageResponsePriority(Enum):
    """ Message priority """
    
    Normal = 'Normal'
    High = 'High'

class UpdateMessageResponseReadStatus(Enum):
    """ Message read status """
    
    Read = 'Read'
    Unread = 'Unread'

class UpdateMessageResponseToItemMessageStatus(Enum):
    """ Status of a message. Returned for outbound fax messages only """
    
    Queued = 'Queued'
    Sent = 'Sent'
    Delivered = 'Delivered'
    DeliveryFailed = 'DeliveryFailed'
    SendingFailed = 'SendingFailed'
    Received = 'Received'

class UpdateMessageResponseToItemFaxErrorCode(Enum):
    """
    Error code returned in case of fax sending failure. Returned if messageStatus value is
    'SendingFailed'. Supported for fax messages only
    
    Generated by Python OpenAPI Parser
    """
    
    AllLinesInUse = 'AllLinesInUse'
    Undefined = 'Undefined'
    NoFaxSendPermission = 'NoFaxSendPermission'
    NoInternationalPermission = 'NoInternationalPermission'
    NoFaxMachine = 'NoFaxMachine'
    NoAnswer = 'NoAnswer'
    LineBusy = 'LineBusy'
    CallerHungUp = 'CallerHungUp'
    NotEnoughCredits = 'NotEnoughCredits'
    SentPartially = 'SentPartially'
    InternationalCallingDisabled = 'InternationalCallingDisabled'
    DestinationCountryDisabled = 'DestinationCountryDisabled'
    UnknownCountryCode = 'UnknownCountryCode'
    NotAccepted = 'NotAccepted'
    InvalidNumber = 'InvalidNumber'
    CallDeclined = 'CallDeclined'
    TooManyCallsPerLine = 'TooManyCallsPerLine'
    CallFailed = 'CallFailed'
    RenderingFailed = 'RenderingFailed'
    TooManyPages = 'TooManyPages'
    ReturnToDBQueue = 'ReturnToDBQueue'
    NoCallTime = 'NoCallTime'
    WrongNumber = 'WrongNumber'
    ProhibitedNumber = 'ProhibitedNumber'
    InternalError = 'InternalError'
    FaxSendingProhibited = 'FaxSendingProhibited'
    ThePhoneIsBlacklisted = 'ThePhoneIsBlacklisted'
    UserNotFound = 'UserNotFound'
    ConvertError = 'ConvertError'
    DBGeneralError = 'DBGeneralError'
    SkypeBillingFailed = 'SkypeBillingFailed'
    AccountSuspended = 'AccountSuspended'
    ProhibitedDestination = 'ProhibitedDestination'
    InternationalDisabled = 'InternationalDisabled'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateMessageResponseToItem(DataClassJsonMixin):
    extension_number: Optional[str] = None
    """
    Extension short number (usually 3 or 4 digits). This property is filled when parties
    communicate by means of short internal numbers, for example when calling to other extension or
    sending/receiving Company Pager message
    """
    
    extension_id: Optional[str] = None
    location: Optional[str] = None
    """
    Contains party location (city, state) if one can be determined from phoneNumber. This property
    is filled only when phoneNumber is not empty and server can calculate location information from
    it (for example, this information is unavailable for US toll-free numbers)
    """
    
    target: Optional[bool] = None
    """
    'True' specifies that message is sent exactly to this recipient. Returned in to field for group
    MMS. Useful if one extension has several phone numbers
    """
    
    message_status: Optional[UpdateMessageResponseToItemMessageStatus] = None
    """ Status of a message. Returned for outbound fax messages only """
    
    fax_error_code: Optional[UpdateMessageResponseToItemFaxErrorCode] = None
    """
    Error code returned in case of fax sending failure. Returned if messageStatus value is
    'SendingFailed'. Supported for fax messages only
    """
    
    name: Optional[str] = None
    """
    Symbolic name associated with a party. If the phone does not belong to the known extension,
    only the location is returned, the name is not determined then
    """
    
    phone_number: Optional[str] = None
    """
    Phone number of a party. Usually it is a plain number including country and area code like
    18661234567. But sometimes it could be returned from database with some formatting applied, for
    example (866)123-4567. This property is filled in all cases where parties communicate by means
    of global phone numbers, for example when calling to direct numbers or sending/receiving SMS
    """
    

class UpdateMessageResponseType(Enum):
    """ Message type """
    
    Fax = 'Fax'
    SMS = 'SMS'
    VoiceMail = 'VoiceMail'
    Pager = 'Pager'
    Text = 'Text'

class UpdateMessageResponseVmTranscriptionStatus(Enum):
    """
    Voicemail only. Status of voicemail to text transcription. If VoicemailToText feature is not
    activated for account, the 'NotAvailable' value is returned
    
    Generated by Python OpenAPI Parser
    """
    
    NotAvailable = 'NotAvailable'
    InProgress = 'InProgress'
    TimedOut = 'TimedOut'
    Completed = 'Completed'
    CompletedPartially = 'CompletedPartially'
    Failed = 'Failed'
    Unknown = 'Unknown'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateMessageResponse(DataClassJsonMixin):
    id: Optional[int] = None
    """ Internal identifier of a message """
    
    uri: Optional[str] = None
    """ Canonical URI of a message """
    
    attachments: Optional[List[UpdateMessageResponseAttachmentsItem]] = None
    """ The list of message attachments """
    
    availability: Optional[UpdateMessageResponseAvailability] = None
    """
    Message availability status. Message in 'Deleted' state is still preserved with all its
    attachments and can be restored. 'Purged' means that all attachments are already deleted and
    the message itself is about to be physically deleted shortly
    """
    
    conversation_id: Optional[int] = None
    """ SMS and Pager only. Identifier of a conversation the message belongs to """
    
    conversation: Optional[UpdateMessageResponseConversation] = None
    """ SMS and Pager only. Identifier of a conversation the message belongs to """
    
    creation_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """
    Message creation datetime in ISO 8601 format including timezone, for example
    2016-03-10T18:07:52.534Z
    """
    
    delivery_error_code: Optional[str] = None
    """ SMS only. Delivery error code returned by gateway """
    
    direction: Optional[UpdateMessageResponseDirection] = None
    """
    Message direction. Note that for some message types not all directions are allowed. For example
    voicemail messages can be only inbound
    """
    
    fax_page_count: Optional[int] = None
    """ Fax only. Page count in a fax message """
    
    fax_resolution: Optional[UpdateMessageResponseFaxResolution] = None
    """
    Fax only. Resolution of a fax message. 'High' for black and white image scanned at 200 dpi,
    'Low' for black and white image scanned at 100 dpi
    """
    
    from_: Optional[UpdateMessageResponseFrom] = field(metadata=config(field_name='from'), default=None)
    """ Sender information """
    
    last_modified_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """
    The datetime when the message was modified on server in ISO 8601 format including timezone, for
    example 2016-03-10T18:07:52.534Z
    """
    
    message_status: Optional[UpdateMessageResponseMessageStatus] = None
    """
    Message status. Different message types may have different allowed status values. For outbound
    faxes the aggregated message status is returned: If status for at least one recipient is
    'Queued', then 'Queued' value is returned If status for at least one recipient is
    'SendingFailed', then 'SendingFailed' value is returned In other cases Sent status is returned
    """
    
    pg_to_department: Optional[bool] = None
    """ 'Pager' only. 'True' if at least one of the message recipients is 'Department' extension """
    
    priority: Optional[UpdateMessageResponsePriority] = None
    """ Message priority """
    
    read_status: Optional[UpdateMessageResponseReadStatus] = None
    """ Message read status """
    
    sms_delivery_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """
    SMS only. The datetime when outbound SMS was delivered to recipient's handset in ISO 8601
    format including timezone, for example 2016-03-10T18:07:52.534Z. It is filled only if the
    carrier sends a delivery receipt to RingCentral
    """
    
    sms_sending_attempts_count: Optional[int] = None
    """
    SMS only. Number of attempts made to send an outbound SMS to the gateway (if gateway is
    temporary unavailable)
    """
    
    subject: Optional[str] = None
    """
    Message subject. For SMS and Pager messages it replicates message text which is also returned
    as an attachment
    """
    
    to: Optional[List[UpdateMessageResponseToItem]] = None
    """ Recipient information """
    
    type: Optional[UpdateMessageResponseType] = None
    """ Message type """
    
    vm_transcription_status: Optional[UpdateMessageResponseVmTranscriptionStatus] = None
    """
    Voicemail only. Status of voicemail to text transcription. If VoicemailToText feature is not
    activated for account, the 'NotAvailable' value is returned
    """
    
    cover_index: Optional[int] = None
    """
    Cover page identifier. For the list of available cover page identifiers please call the Fax
    Cover Pages method
    """
    
    cover_page_text: Optional[str] = None
    """
    Cover page text, entered by the fax sender and printed on the cover page. Maximum length is
    limited to 1024 symbols
    """
    

class UpdateMessageResponseBodyAttachmentsItemType(Enum):
    """ Type of message attachment """
    
    AudioRecording = 'AudioRecording'
    AudioTranscription = 'AudioTranscription'
    Text = 'Text'
    SourceDocument = 'SourceDocument'
    RenderedDocument = 'RenderedDocument'
    MmsAttachment = 'MmsAttachment'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateMessageResponseBodyAttachmentsItem(DataClassJsonMixin):
    id: Optional[int] = None
    """ Internal identifier of a message attachment """
    
    uri: Optional[str] = None
    """ Canonical URI of a message attachment """
    
    type: Optional[UpdateMessageResponseBodyAttachmentsItemType] = None
    """ Type of message attachment """
    
    content_type: Optional[str] = None
    """ MIME type for a given attachment, for instance 'audio/wav' """
    
    vm_duration: Optional[int] = None
    """ Supported for `Voicemail` only. Duration of a voicemail in seconds """
    
    file_name: Optional[str] = None
    """ Name of a file attached """
    
    size: Optional[int] = None
    """ Size of attachment in bytes """
    
    height: Optional[int] = None
    """ Attachment height in pixels if available """
    
    width: Optional[int] = None
    """ Attachment width in pixels if available """
    

class UpdateMessageResponseBodyAvailability(Enum):
    """
    Message availability status. Message in 'Deleted' state is still preserved with all its
    attachments and can be restored. 'Purged' means that all attachments are already deleted and
    the message itself is about to be physically deleted shortly
    
    Generated by Python OpenAPI Parser
    """
    
    Alive = 'Alive'
    Deleted = 'Deleted'
    Purged = 'Purged'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateMessageResponseBodyConversation(DataClassJsonMixin):
    """ SMS and Pager only. Identifier of a conversation the message belongs to """
    
    id: Optional[str] = None
    """ Internal identifier of a conversation """
    
    uri: Optional[str] = None
    """ Deprecated. Link to a conversation resource """
    

class UpdateMessageResponseBodyDirection(Enum):
    """
    Message direction. Note that for some message types not all directions are allowed. For example
    voicemail messages can be only inbound
    
    Generated by Python OpenAPI Parser
    """
    
    Inbound = 'Inbound'
    Outbound = 'Outbound'

class UpdateMessageResponseBodyFaxResolution(Enum):
    """
    Fax only. Resolution of a fax message. 'High' for black and white image scanned at 200 dpi,
    'Low' for black and white image scanned at 100 dpi
    
    Generated by Python OpenAPI Parser
    """
    
    High = 'High'
    Low = 'Low'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateMessageResponseBodyFrom(DataClassJsonMixin):
    """ Sender information """
    
    extension_number: Optional[str] = None
    extension_id: Optional[str] = None
    name: Optional[str] = None

class UpdateMessageResponseBodyMessageStatus(Enum):
    """
    Message status. Different message types may have different allowed status values.For outbound
    faxes the aggregated message status is returned: If status for at least one recipient is
    'Queued', then 'Queued' value is returned If status for at least one recipient is
    'SendingFailed', then 'SendingFailed' value is returned In other cases Sent status is returned
    
    Generated by Python OpenAPI Parser
    """
    
    Queued = 'Queued'
    Sent = 'Sent'
    Delivered = 'Delivered'
    DeliveryFailed = 'DeliveryFailed'
    SendingFailed = 'SendingFailed'
    Received = 'Received'

class UpdateMessageResponseBodyPriority(Enum):
    """ Message priority """
    
    Normal = 'Normal'
    High = 'High'

class UpdateMessageResponseBodyReadStatus(Enum):
    """ Message read status """
    
    Read = 'Read'
    Unread = 'Unread'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateMessageResponseBodyToItem(DataClassJsonMixin):
    extension_number: Optional[str] = None
    extension_id: Optional[str] = None
    name: Optional[str] = None

class UpdateMessageResponseBodyType(Enum):
    """ Message type """
    
    Fax = 'Fax'
    SMS = 'SMS'
    VoiceMail = 'VoiceMail'
    Pager = 'Pager'
    Text = 'Text'

class UpdateMessageResponseBodyVmTranscriptionStatus(Enum):
    """
    Voicemail only. Status of voicemail to text transcription. If VoicemailToText feature is not
    activated for account, the 'NotAvailable' value is returned
    
    Generated by Python OpenAPI Parser
    """
    
    NotAvailable = 'NotAvailable'
    InProgress = 'InProgress'
    TimedOut = 'TimedOut'
    Completed = 'Completed'
    CompletedPartially = 'CompletedPartially'
    Failed = 'Failed'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateMessageResponseBody(DataClassJsonMixin):
    uri: Optional[str] = None
    """ Canonical URI of a message """
    
    id: Optional[str] = None
    """ Internal identifier of a message """
    
    attachments: Optional[List[UpdateMessageResponseBodyAttachmentsItem]] = None
    """ The list of message attachments """
    
    availability: Optional[UpdateMessageResponseBodyAvailability] = None
    """
    Message availability status. Message in 'Deleted' state is still preserved with all its
    attachments and can be restored. 'Purged' means that all attachments are already deleted and
    the message itself is about to be physically deleted shortly
    """
    
    conversation_id: Optional[int] = None
    """ SMS and Pager only. Identifier of a conversation the message belongs to """
    
    conversation: Optional[UpdateMessageResponseBodyConversation] = None
    """ SMS and Pager only. Identifier of a conversation the message belongs to """
    
    creation_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """
    Message creation datetime in ISO 8601 format including timezone, for example
    2016-03-10T18:07:52.534Z
    """
    
    delivery_error_code: Optional[str] = None
    """ SMS only. Delivery error code returned by gateway """
    
    direction: Optional[UpdateMessageResponseBodyDirection] = None
    """
    Message direction. Note that for some message types not all directions are allowed. For example
    voicemail messages can be only inbound
    """
    
    fax_page_count: Optional[int] = None
    """ Fax only. Page count in a fax message """
    
    fax_resolution: Optional[UpdateMessageResponseBodyFaxResolution] = None
    """
    Fax only. Resolution of a fax message. 'High' for black and white image scanned at 200 dpi,
    'Low' for black and white image scanned at 100 dpi
    """
    
    from_: Optional[UpdateMessageResponseBodyFrom] = field(metadata=config(field_name='from'), default=None)
    """ Sender information """
    
    last_modified_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """
    The datetime when the message was modified on server in ISO 8601 format including timezone, for
    example 2016-03-10T18:07:52.534Z
    """
    
    message_status: Optional[UpdateMessageResponseBodyMessageStatus] = None
    """
    Message status. Different message types may have different allowed status values.For outbound
    faxes the aggregated message status is returned: If status for at least one recipient is
    'Queued', then 'Queued' value is returned If status for at least one recipient is
    'SendingFailed', then 'SendingFailed' value is returned In other cases Sent status is returned
    """
    
    pg_to_department: Optional[bool] = None
    """ 'Pager' only. 'True' if at least one of the message recipients is 'Department' extension """
    
    priority: Optional[UpdateMessageResponseBodyPriority] = None
    """ Message priority """
    
    read_status: Optional[UpdateMessageResponseBodyReadStatus] = None
    """ Message read status """
    
    sms_delivery_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """
    SMS only. The datetime when outbound SMS was delivered to recipient's handset in ISO 8601
    format including timezone, for example 2016-03-10T18:07:52.534Z. It is filled only if the
    carrier sends a delivery receipt to RingCentral
    """
    
    sms_sending_attempts_count: Optional[int] = None
    """
    SMS only. Number of attempts made to send an outbound SMS to the gateway (if gateway is
    temporary unavailable)
    """
    
    subject: Optional[str] = None
    """
    Message subject. For SMS and Pager messages it replicates message text which is also returned
    as an attachment
    """
    
    to: Optional[List[UpdateMessageResponseBodyToItem]] = None
    """ Recipient information """
    
    type: Optional[UpdateMessageResponseBodyType] = None
    """ Message type """
    
    vm_transcription_status: Optional[UpdateMessageResponseBodyVmTranscriptionStatus] = None
    """
    Voicemail only. Status of voicemail to text transcription. If VoicemailToText feature is not
    activated for account, the 'NotAvailable' value is returned
    """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateMessageResponse(DataClassJsonMixin):
    resource_id: Optional[str] = None
    """ Internal identifier of a resource """
    
    status: Optional[int] = None
    """ Status code of resource retrieval """
    
    body: Optional[UpdateMessageResponseBody] = None

class ReadMessageContentContentDisposition(Enum):
    Inline = 'Inline'
    Attachment = 'Attachment'

class SyncMessagesDirectionItem(Enum):
    Inbound = 'Inbound'
    Outbound = 'Outbound'

class SyncMessagesMessageTypeItem(Enum):
    Fax = 'Fax'
    SMS = 'SMS'
    VoiceMail = 'VoiceMail'
    Pager = 'Pager'
    Text = 'Text'

class SyncMessagesSyncTypeItem(Enum):
    FSync = 'FSync'
    ISync = 'ISync'

class SyncMessagesResponseRecordsItemAttachmentsItemType(Enum):
    """ Type of message attachment """
    
    AudioRecording = 'AudioRecording'
    AudioTranscription = 'AudioTranscription'
    Text = 'Text'
    SourceDocument = 'SourceDocument'
    RenderedDocument = 'RenderedDocument'
    MmsAttachment = 'MmsAttachment'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class SyncMessagesResponseRecordsItemAttachmentsItem(DataClassJsonMixin):
    id: Optional[int] = None
    """ Internal identifier of a message attachment """
    
    uri: Optional[str] = None
    """ Canonical URI of a message attachment """
    
    type: Optional[SyncMessagesResponseRecordsItemAttachmentsItemType] = None
    """ Type of message attachment """
    
    content_type: Optional[str] = None
    """ MIME type for a given attachment, for instance 'audio/wav' """
    
    vm_duration: Optional[int] = None
    """ Supported for `Voicemail` only. Duration of a voicemail in seconds """
    
    file_name: Optional[str] = None
    """ Name of a file attached """
    
    size: Optional[int] = None
    """ Size of attachment in bytes """
    
    height: Optional[int] = None
    """ Attachment height in pixels if available """
    
    width: Optional[int] = None
    """ Attachment width in pixels if available """
    

class SyncMessagesResponseRecordsItemAvailability(Enum):
    """
    Message availability status. Message in 'Deleted' state is still preserved with all its
    attachments and can be restored. 'Purged' means that all attachments are already deleted and
    the message itself is about to be physically deleted shortly
    
    Generated by Python OpenAPI Parser
    """
    
    Alive = 'Alive'
    Deleted = 'Deleted'
    Purged = 'Purged'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class SyncMessagesResponseRecordsItemConversation(DataClassJsonMixin):
    """ SMS and Pager only. Identifier of a conversation the message belongs to """
    
    id: Optional[str] = None
    """ Internal identifier of a conversation """
    
    uri: Optional[str] = None
    """ Deprecated. Link to a conversation resource """
    

class SyncMessagesResponseRecordsItemDirection(Enum):
    """
    Message direction. Note that for some message types not all directions are allowed. For example
    voicemail messages can be only inbound
    
    Generated by Python OpenAPI Parser
    """
    
    Inbound = 'Inbound'
    Outbound = 'Outbound'

class SyncMessagesResponseRecordsItemFaxResolution(Enum):
    """
    Fax only. Resolution of a fax message. 'High' for black and white image scanned at 200 dpi,
    'Low' for black and white image scanned at 100 dpi
    
    Generated by Python OpenAPI Parser
    """
    
    High = 'High'
    Low = 'Low'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class SyncMessagesResponseRecordsItemFrom(DataClassJsonMixin):
    """ Sender information """
    
    extension_number: Optional[str] = None
    """
    Extension short number (usually 3 or 4 digits). This property is filled when parties
    communicate by means of short internal numbers, for example when calling to other extension or
    sending/receiving Company Pager message
    """
    
    extension_id: Optional[str] = None
    """ Internal identifier of an extension """
    
    location: Optional[str] = None
    """
    Contains party location (city, state) if one can be determined from phoneNumber. This property
    is filled only when phoneNumber is not empty and server can calculate location information from
    it (for example, this information is unavailable for US toll-free numbers)
    """
    
    name: Optional[str] = None
    """
    Symbolic name associated with a party. If the phone does not belong to the known extension,
    only the location is returned, the name is not determined then
    """
    
    phone_number: Optional[str] = None
    """
    Phone number of a party. Usually it is a plain number including country and area code like
    18661234567. But sometimes it could be returned from database with some formatting applied, for
    example (866)123-4567. This property is filled in all cases where parties communicate by means
    of global phone numbers, for example when calling to direct numbers or sending/receiving SMS
    """
    

class SyncMessagesResponseRecordsItemMessageStatus(Enum):
    """
    Message status. Different message types may have different allowed status values. For outbound
    faxes the aggregated message status is returned: If status for at least one recipient is
    'Queued', then 'Queued' value is returned If status for at least one recipient is
    'SendingFailed', then 'SendingFailed' value is returned In other cases Sent status is returned
    
    Generated by Python OpenAPI Parser
    """
    
    Queued = 'Queued'
    Sent = 'Sent'
    Delivered = 'Delivered'
    DeliveryFailed = 'DeliveryFailed'
    SendingFailed = 'SendingFailed'
    Received = 'Received'

class SyncMessagesResponseRecordsItemPriority(Enum):
    """ Message priority """
    
    Normal = 'Normal'
    High = 'High'

class SyncMessagesResponseRecordsItemReadStatus(Enum):
    """ Message read status """
    
    Read = 'Read'
    Unread = 'Unread'

class SyncMessagesResponseRecordsItemToItemMessageStatus(Enum):
    """ Status of a message. Returned for outbound fax messages only """
    
    Queued = 'Queued'
    Sent = 'Sent'
    Delivered = 'Delivered'
    DeliveryFailed = 'DeliveryFailed'
    SendingFailed = 'SendingFailed'
    Received = 'Received'

class SyncMessagesResponseRecordsItemToItemFaxErrorCode(Enum):
    """
    Error code returned in case of fax sending failure. Returned if messageStatus value is
    'SendingFailed'. Supported for fax messages only
    
    Generated by Python OpenAPI Parser
    """
    
    AllLinesInUse = 'AllLinesInUse'
    Undefined = 'Undefined'
    NoFaxSendPermission = 'NoFaxSendPermission'
    NoInternationalPermission = 'NoInternationalPermission'
    NoFaxMachine = 'NoFaxMachine'
    NoAnswer = 'NoAnswer'
    LineBusy = 'LineBusy'
    CallerHungUp = 'CallerHungUp'
    NotEnoughCredits = 'NotEnoughCredits'
    SentPartially = 'SentPartially'
    InternationalCallingDisabled = 'InternationalCallingDisabled'
    DestinationCountryDisabled = 'DestinationCountryDisabled'
    UnknownCountryCode = 'UnknownCountryCode'
    NotAccepted = 'NotAccepted'
    InvalidNumber = 'InvalidNumber'
    CallDeclined = 'CallDeclined'
    TooManyCallsPerLine = 'TooManyCallsPerLine'
    CallFailed = 'CallFailed'
    RenderingFailed = 'RenderingFailed'
    TooManyPages = 'TooManyPages'
    ReturnToDBQueue = 'ReturnToDBQueue'
    NoCallTime = 'NoCallTime'
    WrongNumber = 'WrongNumber'
    ProhibitedNumber = 'ProhibitedNumber'
    InternalError = 'InternalError'
    FaxSendingProhibited = 'FaxSendingProhibited'
    ThePhoneIsBlacklisted = 'ThePhoneIsBlacklisted'
    UserNotFound = 'UserNotFound'
    ConvertError = 'ConvertError'
    DBGeneralError = 'DBGeneralError'
    SkypeBillingFailed = 'SkypeBillingFailed'
    AccountSuspended = 'AccountSuspended'
    ProhibitedDestination = 'ProhibitedDestination'
    InternationalDisabled = 'InternationalDisabled'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class SyncMessagesResponseRecordsItemToItem(DataClassJsonMixin):
    extension_number: Optional[str] = None
    """
    Extension short number (usually 3 or 4 digits). This property is filled when parties
    communicate by means of short internal numbers, for example when calling to other extension or
    sending/receiving Company Pager message
    """
    
    extension_id: Optional[str] = None
    location: Optional[str] = None
    """
    Contains party location (city, state) if one can be determined from phoneNumber. This property
    is filled only when phoneNumber is not empty and server can calculate location information from
    it (for example, this information is unavailable for US toll-free numbers)
    """
    
    target: Optional[bool] = None
    """
    'True' specifies that message is sent exactly to this recipient. Returned in to field for group
    MMS. Useful if one extension has several phone numbers
    """
    
    message_status: Optional[SyncMessagesResponseRecordsItemToItemMessageStatus] = None
    """ Status of a message. Returned for outbound fax messages only """
    
    fax_error_code: Optional[SyncMessagesResponseRecordsItemToItemFaxErrorCode] = None
    """
    Error code returned in case of fax sending failure. Returned if messageStatus value is
    'SendingFailed'. Supported for fax messages only
    """
    
    name: Optional[str] = None
    """
    Symbolic name associated with a party. If the phone does not belong to the known extension,
    only the location is returned, the name is not determined then
    """
    
    phone_number: Optional[str] = None
    """
    Phone number of a party. Usually it is a plain number including country and area code like
    18661234567. But sometimes it could be returned from database with some formatting applied, for
    example (866)123-4567. This property is filled in all cases where parties communicate by means
    of global phone numbers, for example when calling to direct numbers or sending/receiving SMS
    """
    

class SyncMessagesResponseRecordsItemType(Enum):
    """ Message type """
    
    Fax = 'Fax'
    SMS = 'SMS'
    VoiceMail = 'VoiceMail'
    Pager = 'Pager'
    Text = 'Text'

class SyncMessagesResponseRecordsItemVmTranscriptionStatus(Enum):
    """
    Voicemail only. Status of voicemail to text transcription. If VoicemailToText feature is not
    activated for account, the 'NotAvailable' value is returned
    
    Generated by Python OpenAPI Parser
    """
    
    NotAvailable = 'NotAvailable'
    InProgress = 'InProgress'
    TimedOut = 'TimedOut'
    Completed = 'Completed'
    CompletedPartially = 'CompletedPartially'
    Failed = 'Failed'
    Unknown = 'Unknown'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class SyncMessagesResponseRecordsItem(DataClassJsonMixin):
    id: Optional[int] = None
    """ Internal identifier of a message """
    
    uri: Optional[str] = None
    """ Canonical URI of a message """
    
    attachments: Optional[List[SyncMessagesResponseRecordsItemAttachmentsItem]] = None
    """ The list of message attachments """
    
    availability: Optional[SyncMessagesResponseRecordsItemAvailability] = None
    """
    Message availability status. Message in 'Deleted' state is still preserved with all its
    attachments and can be restored. 'Purged' means that all attachments are already deleted and
    the message itself is about to be physically deleted shortly
    """
    
    conversation_id: Optional[int] = None
    """ SMS and Pager only. Identifier of a conversation the message belongs to """
    
    conversation: Optional[SyncMessagesResponseRecordsItemConversation] = None
    """ SMS and Pager only. Identifier of a conversation the message belongs to """
    
    creation_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """
    Message creation datetime in ISO 8601 format including timezone, for example
    2016-03-10T18:07:52.534Z
    """
    
    delivery_error_code: Optional[str] = None
    """ SMS only. Delivery error code returned by gateway """
    
    direction: Optional[SyncMessagesResponseRecordsItemDirection] = None
    """
    Message direction. Note that for some message types not all directions are allowed. For example
    voicemail messages can be only inbound
    """
    
    fax_page_count: Optional[int] = None
    """ Fax only. Page count in a fax message """
    
    fax_resolution: Optional[SyncMessagesResponseRecordsItemFaxResolution] = None
    """
    Fax only. Resolution of a fax message. 'High' for black and white image scanned at 200 dpi,
    'Low' for black and white image scanned at 100 dpi
    """
    
    from_: Optional[SyncMessagesResponseRecordsItemFrom] = field(metadata=config(field_name='from'), default=None)
    """ Sender information """
    
    last_modified_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """
    The datetime when the message was modified on server in ISO 8601 format including timezone, for
    example 2016-03-10T18:07:52.534Z
    """
    
    message_status: Optional[SyncMessagesResponseRecordsItemMessageStatus] = None
    """
    Message status. Different message types may have different allowed status values. For outbound
    faxes the aggregated message status is returned: If status for at least one recipient is
    'Queued', then 'Queued' value is returned If status for at least one recipient is
    'SendingFailed', then 'SendingFailed' value is returned In other cases Sent status is returned
    """
    
    pg_to_department: Optional[bool] = None
    """ 'Pager' only. 'True' if at least one of the message recipients is 'Department' extension """
    
    priority: Optional[SyncMessagesResponseRecordsItemPriority] = None
    """ Message priority """
    
    read_status: Optional[SyncMessagesResponseRecordsItemReadStatus] = None
    """ Message read status """
    
    sms_delivery_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """
    SMS only. The datetime when outbound SMS was delivered to recipient's handset in ISO 8601
    format including timezone, for example 2016-03-10T18:07:52.534Z. It is filled only if the
    carrier sends a delivery receipt to RingCentral
    """
    
    sms_sending_attempts_count: Optional[int] = None
    """
    SMS only. Number of attempts made to send an outbound SMS to the gateway (if gateway is
    temporary unavailable)
    """
    
    subject: Optional[str] = None
    """
    Message subject. For SMS and Pager messages it replicates message text which is also returned
    as an attachment
    """
    
    to: Optional[List[SyncMessagesResponseRecordsItemToItem]] = None
    """ Recipient information """
    
    type: Optional[SyncMessagesResponseRecordsItemType] = None
    """ Message type """
    
    vm_transcription_status: Optional[SyncMessagesResponseRecordsItemVmTranscriptionStatus] = None
    """
    Voicemail only. Status of voicemail to text transcription. If VoicemailToText feature is not
    activated for account, the 'NotAvailable' value is returned
    """
    
    cover_index: Optional[int] = None
    """
    Cover page identifier. For the list of available cover page identifiers please call the Fax
    Cover Pages method
    """
    
    cover_page_text: Optional[str] = None
    """
    Cover page text, entered by the fax sender and printed on the cover page. Maximum length is
    limited to 1024 symbols
    """
    

class SyncMessagesResponseSyncInfoSyncType(Enum):
    """ Type of synchronization """
    
    FSync = 'FSync'
    ISync = 'ISync'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class SyncMessagesResponseSyncInfo(DataClassJsonMixin):
    """ Sync type, token and time """
    
    sync_type: Optional[SyncMessagesResponseSyncInfoSyncType] = None
    """ Type of synchronization """
    
    sync_token: Optional[str] = None
    """ Synchronization token """
    
    sync_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """
    Last synchronization datetime in ISO 8601 format including timezone, for example
    2016-03-10T18:07:52.534Z
    """
    
    older_records_exist: Optional[bool] = False

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class SyncMessagesResponse(DataClassJsonMixin):
    """
    Required Properties:
     - records
     - sync_info
    
    Generated by Python OpenAPI Parser
    """
    
    records: List[SyncMessagesResponseRecordsItem]
    """ List of message records with synchronization information """
    
    sync_info: SyncMessagesResponseSyncInfo
    """ Sync type, token and time """
    
    uri: Optional[str] = None
    """ Link to the message sync resource """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadMessageStoreConfigurationResponse(DataClassJsonMixin):
    retention_period: Optional[int] = None
    """
    Retention policy setting, specifying how long to keep messages; the supported value range is
    7-90 days
    """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateMessageStoreConfigurationRequest(DataClassJsonMixin):
    retention_period: Optional[int] = None
    """
    Retention policy setting, specifying how long to keep messages; the supported value range is
    7-90 days
    """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateMessageStoreConfigurationResponse(DataClassJsonMixin):
    retention_period: Optional[int] = None
    """
    Retention policy setting, specifying how long to keep messages; the supported value range is
    7-90 days
    """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateRingOutCallRequestFrom(DataClassJsonMixin):
    """
    Phone number of the caller. This number corresponds to the 1st leg of the RingOut call. This
    number can be one of user's configured forwarding numbers or arbitrary number
    
    Generated by Python OpenAPI Parser
    """
    
    phone_number: Optional[str] = None
    """ Phone number in E.164 format """
    
    forwarding_number_id: Optional[str] = None
    """
    Internal identifier of a forwarding number; returned in response as an 'id' field value. Can be
    specified instead of the phoneNumber attribute
    """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateRingOutCallRequestTo(DataClassJsonMixin):
    """ Phone number of the called party. This number corresponds to the 2nd leg of a RingOut call """
    
    phone_number: Optional[str] = None
    """ Phone number in E.164 format """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateRingOutCallRequestCallerId(DataClassJsonMixin):
    """ The number which will be displayed to the called party """
    
    phone_number: Optional[str] = None
    """ Phone number in E.164 format """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateRingOutCallRequestCountry(DataClassJsonMixin):
    """
    Optional. Dialing plan country data. If not specified, then extension home country is applied
    by default
    
    Generated by Python OpenAPI Parser
    """
    
    id: Optional[str] = None
    """ Dialing plan country identifier """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateRingOutCallRequest(DataClassJsonMixin):
    """
    Required Properties:
     - from_
     - to
    
    Generated by Python OpenAPI Parser
    """
    
    from_: CreateRingOutCallRequestFrom = field(metadata=config(field_name='from'))
    """
    Phone number of the caller. This number corresponds to the 1st leg of the RingOut call. This
    number can be one of user's configured forwarding numbers or arbitrary number
    """
    
    to: CreateRingOutCallRequestTo
    """ Phone number of the called party. This number corresponds to the 2nd leg of a RingOut call """
    
    caller_id: Optional[CreateRingOutCallRequestCallerId] = None
    """ The number which will be displayed to the called party """
    
    play_prompt: Optional[bool] = None
    """ The audio prompt that the calling party hears when the call is connected """
    
    country: Optional[CreateRingOutCallRequestCountry] = None
    """
    Optional. Dialing plan country data. If not specified, then extension home country is applied
    by default
    """
    

class CreateRingOutCallResponseStatusCallStatus(Enum):
    """ Status of a call """
    
    Invalid = 'Invalid'
    Success = 'Success'
    InProgress = 'InProgress'
    Busy = 'Busy'
    NoAnswer = 'NoAnswer'
    Rejected = 'Rejected'
    GenericError = 'GenericError'
    Finished = 'Finished'
    InternationalDisabled = 'InternationalDisabled'
    DestinationBlocked = 'DestinationBlocked'
    NotEnoughFunds = 'NotEnoughFunds'
    NoSuchUser = 'NoSuchUser'

class CreateRingOutCallResponseStatusCallerStatus(Enum):
    """ Status of a calling party """
    
    Invalid = 'Invalid'
    Success = 'Success'
    InProgress = 'InProgress'
    Busy = 'Busy'
    NoAnswer = 'NoAnswer'
    Rejected = 'Rejected'
    GenericError = 'GenericError'
    Finished = 'Finished'
    InternationalDisabled = 'InternationalDisabled'
    DestinationBlocked = 'DestinationBlocked'
    NotEnoughFunds = 'NotEnoughFunds'
    NoSuchUser = 'NoSuchUser'

class CreateRingOutCallResponseStatusCalleeStatus(Enum):
    """ Status of a called party """
    
    Invalid = 'Invalid'
    Success = 'Success'
    InProgress = 'InProgress'
    Busy = 'Busy'
    NoAnswer = 'NoAnswer'
    Rejected = 'Rejected'
    GenericError = 'GenericError'
    Finished = 'Finished'
    InternationalDisabled = 'InternationalDisabled'
    DestinationBlocked = 'DestinationBlocked'
    NotEnoughFunds = 'NotEnoughFunds'
    NoSuchUser = 'NoSuchUser'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateRingOutCallResponseStatus(DataClassJsonMixin):
    """ RingOut status information """
    
    call_status: Optional[CreateRingOutCallResponseStatusCallStatus] = None
    """ Status of a call """
    
    caller_status: Optional[CreateRingOutCallResponseStatusCallerStatus] = None
    """ Status of a calling party """
    
    callee_status: Optional[CreateRingOutCallResponseStatusCalleeStatus] = None
    """ Status of a called party """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateRingOutCallResponse(DataClassJsonMixin):
    id: Optional[int] = None
    """ Internal identifier of a RingOut call """
    
    uri: Optional[str] = None
    status: Optional[CreateRingOutCallResponseStatus] = None
    """ RingOut status information """
    

class ReadRingOutCallStatusResponseStatusCallStatus(Enum):
    """ Status of a call """
    
    Invalid = 'Invalid'
    Success = 'Success'
    InProgress = 'InProgress'
    Busy = 'Busy'
    NoAnswer = 'NoAnswer'
    Rejected = 'Rejected'
    GenericError = 'GenericError'
    Finished = 'Finished'
    InternationalDisabled = 'InternationalDisabled'
    DestinationBlocked = 'DestinationBlocked'
    NotEnoughFunds = 'NotEnoughFunds'
    NoSuchUser = 'NoSuchUser'

class ReadRingOutCallStatusResponseStatusCallerStatus(Enum):
    """ Status of a calling party """
    
    Invalid = 'Invalid'
    Success = 'Success'
    InProgress = 'InProgress'
    Busy = 'Busy'
    NoAnswer = 'NoAnswer'
    Rejected = 'Rejected'
    GenericError = 'GenericError'
    Finished = 'Finished'
    InternationalDisabled = 'InternationalDisabled'
    DestinationBlocked = 'DestinationBlocked'
    NotEnoughFunds = 'NotEnoughFunds'
    NoSuchUser = 'NoSuchUser'

class ReadRingOutCallStatusResponseStatusCalleeStatus(Enum):
    """ Status of a called party """
    
    Invalid = 'Invalid'
    Success = 'Success'
    InProgress = 'InProgress'
    Busy = 'Busy'
    NoAnswer = 'NoAnswer'
    Rejected = 'Rejected'
    GenericError = 'GenericError'
    Finished = 'Finished'
    InternationalDisabled = 'InternationalDisabled'
    DestinationBlocked = 'DestinationBlocked'
    NotEnoughFunds = 'NotEnoughFunds'
    NoSuchUser = 'NoSuchUser'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadRingOutCallStatusResponseStatus(DataClassJsonMixin):
    """ RingOut status information """
    
    call_status: Optional[ReadRingOutCallStatusResponseStatusCallStatus] = None
    """ Status of a call """
    
    caller_status: Optional[ReadRingOutCallStatusResponseStatusCallerStatus] = None
    """ Status of a calling party """
    
    callee_status: Optional[ReadRingOutCallStatusResponseStatusCalleeStatus] = None
    """ Status of a called party """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadRingOutCallStatusResponse(DataClassJsonMixin):
    id: Optional[int] = None
    """ Internal identifier of a RingOut call """
    
    uri: Optional[str] = None
    status: Optional[ReadRingOutCallStatusResponseStatus] = None
    """ RingOut status information """
    

class CreateRingOutCallDeprecatedResponseStatusCallStatus(Enum):
    """ Status of a call """
    
    Invalid = 'Invalid'
    Success = 'Success'
    InProgress = 'InProgress'
    Busy = 'Busy'
    NoAnswer = 'NoAnswer'
    Rejected = 'Rejected'
    GenericError = 'GenericError'
    Finished = 'Finished'
    InternationalDisabled = 'InternationalDisabled'
    DestinationBlocked = 'DestinationBlocked'
    NotEnoughFunds = 'NotEnoughFunds'
    NoSuchUser = 'NoSuchUser'

class CreateRingOutCallDeprecatedResponseStatusCallerStatus(Enum):
    """ Status of a calling party """
    
    Invalid = 'Invalid'
    Success = 'Success'
    InProgress = 'InProgress'
    Busy = 'Busy'
    NoAnswer = 'NoAnswer'
    Rejected = 'Rejected'
    GenericError = 'GenericError'
    Finished = 'Finished'
    InternationalDisabled = 'InternationalDisabled'
    DestinationBlocked = 'DestinationBlocked'
    NotEnoughFunds = 'NotEnoughFunds'
    NoSuchUser = 'NoSuchUser'

class CreateRingOutCallDeprecatedResponseStatusCalleeStatus(Enum):
    """ Status of a called party """
    
    Invalid = 'Invalid'
    Success = 'Success'
    InProgress = 'InProgress'
    Busy = 'Busy'
    NoAnswer = 'NoAnswer'
    Rejected = 'Rejected'
    GenericError = 'GenericError'
    Finished = 'Finished'
    InternationalDisabled = 'InternationalDisabled'
    DestinationBlocked = 'DestinationBlocked'
    NotEnoughFunds = 'NotEnoughFunds'
    NoSuchUser = 'NoSuchUser'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateRingOutCallDeprecatedResponseStatus(DataClassJsonMixin):
    """ RingOut status information """
    
    call_status: Optional[CreateRingOutCallDeprecatedResponseStatusCallStatus] = None
    """ Status of a call """
    
    caller_status: Optional[CreateRingOutCallDeprecatedResponseStatusCallerStatus] = None
    """ Status of a calling party """
    
    callee_status: Optional[CreateRingOutCallDeprecatedResponseStatusCalleeStatus] = None
    """ Status of a called party """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateRingOutCallDeprecatedResponse(DataClassJsonMixin):
    id: Optional[int] = None
    """ Internal identifier of a RingOut call """
    
    uri: Optional[str] = None
    status: Optional[CreateRingOutCallDeprecatedResponseStatus] = None
    """ RingOut status information """
    

class ReadRingOutCallStatusDeprecatedResponseStatusCallStatus(Enum):
    """ Status of a call """
    
    Invalid = 'Invalid'
    Success = 'Success'
    InProgress = 'InProgress'
    Busy = 'Busy'
    NoAnswer = 'NoAnswer'
    Rejected = 'Rejected'
    GenericError = 'GenericError'
    Finished = 'Finished'
    InternationalDisabled = 'InternationalDisabled'
    DestinationBlocked = 'DestinationBlocked'
    NotEnoughFunds = 'NotEnoughFunds'
    NoSuchUser = 'NoSuchUser'

class ReadRingOutCallStatusDeprecatedResponseStatusCallerStatus(Enum):
    """ Status of a calling party """
    
    Invalid = 'Invalid'
    Success = 'Success'
    InProgress = 'InProgress'
    Busy = 'Busy'
    NoAnswer = 'NoAnswer'
    Rejected = 'Rejected'
    GenericError = 'GenericError'
    Finished = 'Finished'
    InternationalDisabled = 'InternationalDisabled'
    DestinationBlocked = 'DestinationBlocked'
    NotEnoughFunds = 'NotEnoughFunds'
    NoSuchUser = 'NoSuchUser'

class ReadRingOutCallStatusDeprecatedResponseStatusCalleeStatus(Enum):
    """ Status of a called party """
    
    Invalid = 'Invalid'
    Success = 'Success'
    InProgress = 'InProgress'
    Busy = 'Busy'
    NoAnswer = 'NoAnswer'
    Rejected = 'Rejected'
    GenericError = 'GenericError'
    Finished = 'Finished'
    InternationalDisabled = 'InternationalDisabled'
    DestinationBlocked = 'DestinationBlocked'
    NotEnoughFunds = 'NotEnoughFunds'
    NoSuchUser = 'NoSuchUser'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadRingOutCallStatusDeprecatedResponseStatus(DataClassJsonMixin):
    """ RingOut status information """
    
    call_status: Optional[ReadRingOutCallStatusDeprecatedResponseStatusCallStatus] = None
    """ Status of a call """
    
    caller_status: Optional[ReadRingOutCallStatusDeprecatedResponseStatusCallerStatus] = None
    """ Status of a calling party """
    
    callee_status: Optional[ReadRingOutCallStatusDeprecatedResponseStatusCalleeStatus] = None
    """ Status of a called party """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadRingOutCallStatusDeprecatedResponse(DataClassJsonMixin):
    id: Optional[int] = None
    """ Internal identifier of a RingOut call """
    
    uri: Optional[str] = None
    status: Optional[ReadRingOutCallStatusDeprecatedResponseStatus] = None
    """ RingOut status information """
    
