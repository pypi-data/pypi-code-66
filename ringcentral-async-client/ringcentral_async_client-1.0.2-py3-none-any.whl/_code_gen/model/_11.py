from ._10 import *

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListStandardGreetingsResponseRecordsItemNavigationNextPage(DataClassJsonMixin):
    """ Canonical URI for the next page of the list """
    
    uri: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListStandardGreetingsResponseRecordsItemNavigationPreviousPage(DataClassJsonMixin):
    """ Canonical URI for the previous page of the list """
    
    uri: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListStandardGreetingsResponseRecordsItemNavigationLastPage(DataClassJsonMixin):
    """ Canonical URI for the last page of the list """
    
    uri: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListStandardGreetingsResponseRecordsItemNavigation(DataClassJsonMixin):
    """ Information on navigation """
    
    first_page: Optional[ListStandardGreetingsResponseRecordsItemNavigationFirstPage] = None
    """ Canonical URI for the first page of the list """
    
    next_page: Optional[ListStandardGreetingsResponseRecordsItemNavigationNextPage] = None
    """ Canonical URI for the next page of the list """
    
    previous_page: Optional[ListStandardGreetingsResponseRecordsItemNavigationPreviousPage] = None
    """ Canonical URI for the previous page of the list """
    
    last_page: Optional[ListStandardGreetingsResponseRecordsItemNavigationLastPage] = None
    """ Canonical URI for the last page of the list """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListStandardGreetingsResponseRecordsItemPaging(DataClassJsonMixin):
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
class ListStandardGreetingsResponseRecordsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a greeting """
    
    uri: Optional[str] = None
    """ Link to a greeting """
    
    name: Optional[str] = None
    """ Name of a greeting """
    
    usage_type: Optional[ListStandardGreetingsResponseRecordsItemUsageType] = None
    """
    Usage type of a greeting, specifying if the greeting is applied for user extension or
    department extension.
    """
    
    text: Optional[str] = None
    """ Text of a greeting, if any """
    
    content_uri: Optional[str] = None
    """ Link to a greeting content (audio file), if any """
    
    type: Optional[ListStandardGreetingsResponseRecordsItemType] = None
    """ Type of a greeting, specifying the case when the greeting is played. """
    
    category: Optional[ListStandardGreetingsResponseRecordsItemCategory] = None
    """
    Category of a greeting, specifying data form. The category value 'None' specifies that
    greetings of a certain type ('Introductory', 'ConnectingAudio', etc.) are switched off for an
    extension = ['Music', 'Message', 'RingTones', 'None']
    """
    
    navigation: Optional[ListStandardGreetingsResponseRecordsItemNavigation] = None
    """ Information on navigation """
    
    paging: Optional[ListStandardGreetingsResponseRecordsItemPaging] = None
    """ Information on paging """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListStandardGreetingsResponseNavigationFirstPage(DataClassJsonMixin):
    """ Canonical URI for the first page of the list """
    
    uri: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListStandardGreetingsResponseNavigationNextPage(DataClassJsonMixin):
    """ Canonical URI for the next page of the list """
    
    uri: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListStandardGreetingsResponseNavigationPreviousPage(DataClassJsonMixin):
    """ Canonical URI for the previous page of the list """
    
    uri: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListStandardGreetingsResponseNavigationLastPage(DataClassJsonMixin):
    """ Canonical URI for the last page of the list """
    
    uri: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListStandardGreetingsResponseNavigation(DataClassJsonMixin):
    """ Information on navigation """
    
    first_page: Optional[ListStandardGreetingsResponseNavigationFirstPage] = None
    """ Canonical URI for the first page of the list """
    
    next_page: Optional[ListStandardGreetingsResponseNavigationNextPage] = None
    """ Canonical URI for the next page of the list """
    
    previous_page: Optional[ListStandardGreetingsResponseNavigationPreviousPage] = None
    """ Canonical URI for the previous page of the list """
    
    last_page: Optional[ListStandardGreetingsResponseNavigationLastPage] = None
    """ Canonical URI for the last page of the list """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListStandardGreetingsResponsePaging(DataClassJsonMixin):
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
class ListStandardGreetingsResponse(DataClassJsonMixin):
    uri: Optional[str] = None
    """ Canonical URI of greetings list resource """
    
    records: Optional[List[ListStandardGreetingsResponseRecordsItem]] = None
    """ List of greetings """
    
    navigation: Optional[ListStandardGreetingsResponseNavigation] = None
    """ Information on navigation """
    
    paging: Optional[ListStandardGreetingsResponsePaging] = None
    """ Information on paging """
    

class ReadStandardGreetingResponseUsageType(Enum):
    """
    Usage type of a greeting, specifying if the greeting is applied for user extension or
    department extension.
    
    Generated by Python OpenAPI Parser
    """
    
    UserExtensionAnsweringRule = 'UserExtensionAnsweringRule'
    ExtensionAnsweringRule = 'ExtensionAnsweringRule'
    DepartmentExtensionAnsweringRule = 'DepartmentExtensionAnsweringRule'
    BlockedCalls = 'BlockedCalls'
    CallRecording = 'CallRecording'
    CompanyAnsweringRule = 'CompanyAnsweringRule'
    CompanyAfterHoursAnsweringRule = 'CompanyAfterHoursAnsweringRule'
    LimitedExtensionAnsweringRule = 'LimitedExtensionAnsweringRule'
    VoicemailExtensionAnsweringRule = 'VoicemailExtensionAnsweringRule'
    AnnouncementExtensionAnsweringRule = 'AnnouncementExtensionAnsweringRule'
    SharedLinesGroupAnsweringRule = 'SharedLinesGroupAnsweringRule'

class ReadStandardGreetingResponseType(Enum):
    """ Type of a greeting, specifying the case when the greeting is played. """
    
    Introductory = 'Introductory'
    Announcement = 'Announcement'
    AutomaticRecording = 'AutomaticRecording'
    BlockedCallersAll = 'BlockedCallersAll'
    BlockedCallersSpecific = 'BlockedCallersSpecific'
    BlockedNoCallerId = 'BlockedNoCallerId'
    BlockedPayPhones = 'BlockedPayPhones'
    ConnectingMessage = 'ConnectingMessage'
    ConnectingAudio = 'ConnectingAudio'
    StartRecording = 'StartRecording'
    StopRecording = 'StopRecording'
    Voicemail = 'Voicemail'
    Unavailable = 'Unavailable'
    InterruptPrompt = 'InterruptPrompt'
    HoldMusic = 'HoldMusic'
    Company = 'Company'

class ReadStandardGreetingResponseCategory(Enum):
    """
    Category of a greeting, specifying data form. The category value 'None' specifies that
    greetings of a certain type ('Introductory', 'ConnectingAudio', etc.) are switched off for an
    extension = ['Music', 'Message', 'RingTones', 'None']
    
    Generated by Python OpenAPI Parser
    """
    
    Music = 'Music'
    Message = 'Message'
    RingTones = 'RingTones'
    None_ = 'None'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadStandardGreetingResponseNavigationFirstPage(DataClassJsonMixin):
    """ Canonical URI for the first page of the list """
    
    uri: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadStandardGreetingResponseNavigationNextPage(DataClassJsonMixin):
    """ Canonical URI for the next page of the list """
    
    uri: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadStandardGreetingResponseNavigationPreviousPage(DataClassJsonMixin):
    """ Canonical URI for the previous page of the list """
    
    uri: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadStandardGreetingResponseNavigationLastPage(DataClassJsonMixin):
    """ Canonical URI for the last page of the list """
    
    uri: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadStandardGreetingResponseNavigation(DataClassJsonMixin):
    """ Information on navigation """
    
    first_page: Optional[ReadStandardGreetingResponseNavigationFirstPage] = None
    """ Canonical URI for the first page of the list """
    
    next_page: Optional[ReadStandardGreetingResponseNavigationNextPage] = None
    """ Canonical URI for the next page of the list """
    
    previous_page: Optional[ReadStandardGreetingResponseNavigationPreviousPage] = None
    """ Canonical URI for the previous page of the list """
    
    last_page: Optional[ReadStandardGreetingResponseNavigationLastPage] = None
    """ Canonical URI for the last page of the list """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadStandardGreetingResponsePaging(DataClassJsonMixin):
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
class ReadStandardGreetingResponse(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a greeting """
    
    uri: Optional[str] = None
    """ Link to a greeting """
    
    name: Optional[str] = None
    """ Name of a greeting """
    
    usage_type: Optional[ReadStandardGreetingResponseUsageType] = None
    """
    Usage type of a greeting, specifying if the greeting is applied for user extension or
    department extension.
    """
    
    text: Optional[str] = None
    """ Text of a greeting, if any """
    
    content_uri: Optional[str] = None
    """ Link to a greeting content (audio file), if any """
    
    type: Optional[ReadStandardGreetingResponseType] = None
    """ Type of a greeting, specifying the case when the greeting is played. """
    
    category: Optional[ReadStandardGreetingResponseCategory] = None
    """
    Category of a greeting, specifying data form. The category value 'None' specifies that
    greetings of a certain type ('Introductory', 'ConnectingAudio', etc.) are switched off for an
    extension = ['Music', 'Message', 'RingTones', 'None']
    """
    
    navigation: Optional[ReadStandardGreetingResponseNavigation] = None
    """ Information on navigation """
    
    paging: Optional[ReadStandardGreetingResponsePaging] = None
    """ Information on paging """
    

class CreateCompanyGreetingRequestType(Enum):
    """ Type of a greeting, specifying the case when the greeting is played. """
    
    Company = 'Company'
    StartRecording = 'StartRecording'
    StopRecording = 'StopRecording'
    AutomaticRecording = 'AutomaticRecording'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateCompanyGreetingRequest(DataClassJsonMixin):
    """
    Required Properties:
     - type
     - binary
    
    Generated by Python OpenAPI Parser
    """
    
    type: CreateCompanyGreetingRequestType
    """ Type of a greeting, specifying the case when the greeting is played. """
    
    binary: bytes
    """ Meida file to upload """
    
    answering_rule_id: Optional[str] = None
    """ Internal identifier of an answering rule """
    
    language_id: Optional[str] = None
    """ Internal identifier of a language. See Get Language List """
    

class CreateCompanyGreetingResponseType(Enum):
    """ Type of a company greeting """
    
    Company = 'Company'
    StartRecording = 'StartRecording'
    StopRecording = 'StopRecording'
    AutomaticRecording = 'AutomaticRecording'

class CreateCompanyGreetingResponseContentType(Enum):
    """ Content media type """
    
    AudioMpeg = 'audio/mpeg'
    AudioWav = 'audio/wav'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateCompanyGreetingResponseAnsweringRule(DataClassJsonMixin):
    """ Information on an answering rule that the greeting is applied to """
    
    uri: Optional[str] = None
    """ Canonical URI of an answering rule """
    
    id: Optional[str] = None
    """ Internal identifier of an answering rule """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateCompanyGreetingResponseLanguage(DataClassJsonMixin):
    """
    Information on a greeting language. Supported for types 'StopRecording', 'StartRecording',
    'AutomaticRecording'
    
    Generated by Python OpenAPI Parser
    """
    
    id: Optional[str] = None
    """ Internal identifier of a greeting language """
    
    uri: Optional[str] = None
    """ Link to a greeting language """
    
    name: Optional[str] = None
    """ Name of a greeting language """
    
    locale_code: Optional[str] = None
    """ Locale code of a greeting language """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateCompanyGreetingResponse(DataClassJsonMixin):
    uri: Optional[str] = None
    """ Link to an extension custom greeting """
    
    id: Optional[str] = None
    """ Internal identifier of an answering rule """
    
    type: Optional[CreateCompanyGreetingResponseType] = None
    """ Type of a company greeting """
    
    content_type: Optional[CreateCompanyGreetingResponseContentType] = None
    """ Content media type """
    
    content_uri: Optional[str] = None
    """ Link to a greeting content (audio file) """
    
    answering_rule: Optional[CreateCompanyGreetingResponseAnsweringRule] = None
    """ Information on an answering rule that the greeting is applied to """
    
    language: Optional[CreateCompanyGreetingResponseLanguage] = None
    """
    Information on a greeting language. Supported for types 'StopRecording', 'StartRecording',
    'AutomaticRecording'
    """
    

class CreateCustomUserGreetingRequestType(Enum):
    """ Type of a greeting, specifying the case when the greeting is played. """
    
    Introductory = 'Introductory'
    Announcement = 'Announcement'
    ConnectingMessage = 'ConnectingMessage'
    ConnectingAudio = 'ConnectingAudio'
    Voicemail = 'Voicemail'
    Unavailable = 'Unavailable'
    HoldMusic = 'HoldMusic'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateCustomUserGreetingRequest(DataClassJsonMixin):
    """
    Required Properties:
     - type
     - answering_rule_id
     - binary
    
    Generated by Python OpenAPI Parser
    """
    
    type: CreateCustomUserGreetingRequestType
    """ Type of a greeting, specifying the case when the greeting is played. """
    
    answering_rule_id: str
    """ Internal identifier of an answering rule """
    
    binary: bytes
    """ Meida file to upload """
    

class CreateCustomUserGreetingResponseType(Enum):
    """ Type of a custom user greeting """
    
    Introductory = 'Introductory'
    Announcement = 'Announcement'
    InterruptPrompt = 'InterruptPrompt'
    ConnectingAudio = 'ConnectingAudio'
    ConnectingMessage = 'ConnectingMessage'
    Voicemail = 'Voicemail'
    Unavailable = 'Unavailable'
    HoldMusic = 'HoldMusic'
    PronouncedName = 'PronouncedName'

class CreateCustomUserGreetingResponseContentType(Enum):
    """ Content media type """
    
    AudioMpeg = 'audio/mpeg'
    AudioWav = 'audio/wav'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateCustomUserGreetingResponseAnsweringRule(DataClassJsonMixin):
    """ Information on an answering rule that the greeting is applied to """
    
    uri: Optional[str] = None
    """ Canonical URI of an answering rule """
    
    id: Optional[str] = None
    """ Internal identifier of an answering rule """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateCustomUserGreetingResponse(DataClassJsonMixin):
    uri: Optional[str] = None
    """ Link to a custom user greeting """
    
    id: Optional[str] = None
    """ Internal identifier of a custom user greeting """
    
    type: Optional[CreateCustomUserGreetingResponseType] = None
    """ Type of a custom user greeting """
    
    content_type: Optional[CreateCustomUserGreetingResponseContentType] = None
    """ Content media type """
    
    content_uri: Optional[str] = None
    """ Link to a greeting content (audio file) """
    
    answering_rule: Optional[CreateCustomUserGreetingResponseAnsweringRule] = None
    """ Information on an answering rule that the greeting is applied to """
    

class ReadCustomGreetingResponseType(Enum):
    """ Type of a custom user greeting """
    
    Introductory = 'Introductory'
    Announcement = 'Announcement'
    InterruptPrompt = 'InterruptPrompt'
    ConnectingAudio = 'ConnectingAudio'
    ConnectingMessage = 'ConnectingMessage'
    Voicemail = 'Voicemail'
    Unavailable = 'Unavailable'
    HoldMusic = 'HoldMusic'
    PronouncedName = 'PronouncedName'

class ReadCustomGreetingResponseContentType(Enum):
    """ Content media type """
    
    AudioMpeg = 'audio/mpeg'
    AudioWav = 'audio/wav'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadCustomGreetingResponseAnsweringRule(DataClassJsonMixin):
    """ Information on an answering rule that the greeting is applied to """
    
    uri: Optional[str] = None
    """ Canonical URI of an answering rule """
    
    id: Optional[str] = None
    """ Internal identifier of an answering rule """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadCustomGreetingResponse(DataClassJsonMixin):
    uri: Optional[str] = None
    """ Link to a custom user greeting """
    
    id: Optional[str] = None
    """ Internal identifier of a custom user greeting """
    
    type: Optional[ReadCustomGreetingResponseType] = None
    """ Type of a custom user greeting """
    
    content_type: Optional[ReadCustomGreetingResponseContentType] = None
    """ Content media type """
    
    content_uri: Optional[str] = None
    """ Link to a greeting content (audio file) """
    
    answering_rule: Optional[ReadCustomGreetingResponseAnsweringRule] = None
    """ Information on an answering rule that the greeting is applied to """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListIVRPromptsResponseRecordsItem(DataClassJsonMixin):
    uri: Optional[str] = None
    """ Internal identifier of a prompt """
    
    id: Optional[str] = None
    """ Link to a prompt metadata """
    
    content_type: Optional[str] = None
    """ Type of a prompt media content """
    
    content_uri: Optional[str] = None
    """ Link to a prompt media content """
    
    filename: Optional[str] = None
    """ Name of a prompt """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListIVRPromptsResponseNavigationFirstPage(DataClassJsonMixin):
    """ Canonical URI for the first page of the list """
    
    uri: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListIVRPromptsResponseNavigationNextPage(DataClassJsonMixin):
    """ Canonical URI for the next page of the list """
    
    uri: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListIVRPromptsResponseNavigationPreviousPage(DataClassJsonMixin):
    """ Canonical URI for the previous page of the list """
    
    uri: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListIVRPromptsResponseNavigationLastPage(DataClassJsonMixin):
    """ Canonical URI for the last page of the list """
    
    uri: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListIVRPromptsResponseNavigation(DataClassJsonMixin):
    """ Information on navigation """
    
    first_page: Optional[ListIVRPromptsResponseNavigationFirstPage] = None
    """ Canonical URI for the first page of the list """
    
    next_page: Optional[ListIVRPromptsResponseNavigationNextPage] = None
    """ Canonical URI for the next page of the list """
    
    previous_page: Optional[ListIVRPromptsResponseNavigationPreviousPage] = None
    """ Canonical URI for the previous page of the list """
    
    last_page: Optional[ListIVRPromptsResponseNavigationLastPage] = None
    """ Canonical URI for the last page of the list """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListIVRPromptsResponsePaging(DataClassJsonMixin):
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
class ListIVRPromptsResponse(DataClassJsonMixin):
    uri: Optional[str] = None
    """ Link to prompts library resource """
    
    records: Optional[List[ListIVRPromptsResponseRecordsItem]] = None
    """ List of Prompts """
    
    navigation: Optional[ListIVRPromptsResponseNavigation] = None
    """ Information on navigation """
    
    paging: Optional[ListIVRPromptsResponsePaging] = None
    """ Information on paging """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateIVRPromptRequest(DataClassJsonMixin):
    """
    Required Properties:
     - attachment
    
    Generated by Python OpenAPI Parser
    """
    
    attachment: bytes
    """
    Audio file that will be used as a prompt. Attachment cannot be empty, only audio files are
    supported
    """
    
    name: Optional[str] = None
    """ Description of file contents. """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateIVRPromptResponse(DataClassJsonMixin):
    uri: Optional[str] = None
    """ Internal identifier of a prompt """
    
    id: Optional[str] = None
    """ Link to a prompt metadata """
    
    content_type: Optional[str] = None
    """ Type of a prompt media content """
    
    content_uri: Optional[str] = None
    """ Link to a prompt media content """
    
    filename: Optional[str] = None
    """ Name of a prompt """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadIVRPromptResponse(DataClassJsonMixin):
    uri: Optional[str] = None
    """ Internal identifier of a prompt """
    
    id: Optional[str] = None
    """ Link to a prompt metadata """
    
    content_type: Optional[str] = None
    """ Type of a prompt media content """
    
    content_uri: Optional[str] = None
    """ Link to a prompt media content """
    
    filename: Optional[str] = None
    """ Name of a prompt """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateIVRPromptRequest(DataClassJsonMixin):
    filename: Optional[str] = None
    """ Name of a file to be uploaded as a prompt """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateIVRPromptResponse(DataClassJsonMixin):
    uri: Optional[str] = None
    """ Internal identifier of a prompt """
    
    id: Optional[str] = None
    """ Link to a prompt metadata """
    
    content_type: Optional[str] = None
    """ Type of a prompt media content """
    
    content_uri: Optional[str] = None
    """ Link to a prompt media content """
    
    filename: Optional[str] = None
    """ Name of a prompt """
    

class CreateIVRMenuRequestPromptMode(Enum):
    """ Prompt mode: custom media or text """
    
    Audio = 'Audio'
    TextToSpeech = 'TextToSpeech'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateIVRMenuRequestPromptAudio(DataClassJsonMixin):
    """ For 'Audio' mode only. Prompt media reference """
    
    uri: Optional[str] = None
    """ Link to a prompt audio file """
    
    id: Optional[str] = None
    """ Internal identifier of a prompt """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateIVRMenuRequestPromptLanguage(DataClassJsonMixin):
    """ For 'TextToSpeech' mode only. Prompt language metadata """
    
    uri: Optional[str] = None
    """ Link to a prompt language """
    
    id: Optional[str] = None
    """ Internal identifier of a language """
    
    name: Optional[str] = None
    """ Language name """
    
    locale_code: Optional[str] = None
    """ Language locale code """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateIVRMenuRequestPrompt(DataClassJsonMixin):
    """ Prompt metadata """
    
    mode: Optional[CreateIVRMenuRequestPromptMode] = None
    """ Prompt mode: custom media or text """
    
    audio: Optional[CreateIVRMenuRequestPromptAudio] = None
    """ For 'Audio' mode only. Prompt media reference """
    
    text: Optional[str] = None
    """ For 'TextToSpeech' mode only. Prompt text """
    
    language: Optional[CreateIVRMenuRequestPromptLanguage] = None
    """ For 'TextToSpeech' mode only. Prompt language metadata """
    

class CreateIVRMenuRequestActionsItemAction(Enum):
    """ Internal identifier of an answering rule """
    
    Connect = 'Connect'
    Voicemail = 'Voicemail'
    DialByName = 'DialByName'
    Transfer = 'Transfer'
    Repeat = 'Repeat'
    ReturnToRoot = 'ReturnToRoot'
    ReturnToPrevious = 'ReturnToPrevious'
    Disconnect = 'Disconnect'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateIVRMenuRequestActionsItemExtension(DataClassJsonMixin):
    """ For 'Connect' or 'Voicemail' actions only. Extension reference """
    
    uri: Optional[str] = None
    """ Link to an extension resource """
    
    id: Optional[str] = None
    """ Internal identifier of an extension """
    
    name: Optional[str] = None
    """ Name of an extension """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateIVRMenuRequestActionsItem(DataClassJsonMixin):
    input: Optional[str] = None
    """ Key. The following values are supported: numeric: '1' to '9' Star Hash NoInput """
    
    action: Optional[CreateIVRMenuRequestActionsItemAction] = None
    """ Internal identifier of an answering rule """
    
    extension: Optional[CreateIVRMenuRequestActionsItemExtension] = None
    """ For 'Connect' or 'Voicemail' actions only. Extension reference """
    
    phone_number: Optional[str] = None
    """ For 'Transfer' action only. PSTN number in E.164 format """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateIVRMenuRequest(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of an IVR Menu extension """
    
    uri: Optional[str] = None
    """ Link to an IVR Menu extension resource """
    
    name: Optional[str] = None
    """ First name of an IVR Menu user """
    
    extension_number: Optional[str] = None
    """ Number of an IVR Menu extension """
    
    site: Optional[str] = None
    """ Site data """
    
    prompt: Optional[CreateIVRMenuRequestPrompt] = None
    """ Prompt metadata """
    
    actions: Optional[List[CreateIVRMenuRequestActionsItem]] = None
    """ Keys handling settings """
    

class CreateIVRMenuResponsePromptMode(Enum):
    """ Prompt mode: custom media or text """
    
    Audio = 'Audio'
    TextToSpeech = 'TextToSpeech'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateIVRMenuResponsePromptAudio(DataClassJsonMixin):
    """ For 'Audio' mode only. Prompt media reference """
    
    uri: Optional[str] = None
    """ Link to a prompt audio file """
    
    id: Optional[str] = None
    """ Internal identifier of a prompt """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateIVRMenuResponsePromptLanguage(DataClassJsonMixin):
    """ For 'TextToSpeech' mode only. Prompt language metadata """
    
    uri: Optional[str] = None
    """ Link to a prompt language """
    
    id: Optional[str] = None
    """ Internal identifier of a language """
    
    name: Optional[str] = None
    """ Language name """
    
    locale_code: Optional[str] = None
    """ Language locale code """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateIVRMenuResponsePrompt(DataClassJsonMixin):
    """ Prompt metadata """
    
    mode: Optional[CreateIVRMenuResponsePromptMode] = None
    """ Prompt mode: custom media or text """
    
    audio: Optional[CreateIVRMenuResponsePromptAudio] = None
    """ For 'Audio' mode only. Prompt media reference """
    
    text: Optional[str] = None
    """ For 'TextToSpeech' mode only. Prompt text """
    
    language: Optional[CreateIVRMenuResponsePromptLanguage] = None
    """ For 'TextToSpeech' mode only. Prompt language metadata """
    

class CreateIVRMenuResponseActionsItemAction(Enum):
    """ Internal identifier of an answering rule """
    
    Connect = 'Connect'
    Voicemail = 'Voicemail'
    DialByName = 'DialByName'
    Transfer = 'Transfer'
    Repeat = 'Repeat'
    ReturnToRoot = 'ReturnToRoot'
    ReturnToPrevious = 'ReturnToPrevious'
    Disconnect = 'Disconnect'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateIVRMenuResponseActionsItemExtension(DataClassJsonMixin):
    """ For 'Connect' or 'Voicemail' actions only. Extension reference """
    
    uri: Optional[str] = None
    """ Link to an extension resource """
    
    id: Optional[str] = None
    """ Internal identifier of an extension """
    
    name: Optional[str] = None
    """ Name of an extension """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateIVRMenuResponseActionsItem(DataClassJsonMixin):
    input: Optional[str] = None
    """ Key. The following values are supported: numeric: '1' to '9' Star Hash NoInput """
    
    action: Optional[CreateIVRMenuResponseActionsItemAction] = None
    """ Internal identifier of an answering rule """
    
    extension: Optional[CreateIVRMenuResponseActionsItemExtension] = None
    """ For 'Connect' or 'Voicemail' actions only. Extension reference """
    
    phone_number: Optional[str] = None
    """ For 'Transfer' action only. PSTN number in E.164 format """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateIVRMenuResponse(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of an IVR Menu extension """
    
    uri: Optional[str] = None
    """ Link to an IVR Menu extension resource """
    
    name: Optional[str] = None
    """ First name of an IVR Menu user """
    
    extension_number: Optional[str] = None
    """ Number of an IVR Menu extension """
    
    site: Optional[str] = None
    """ Site data """
    
    prompt: Optional[CreateIVRMenuResponsePrompt] = None
    """ Prompt metadata """
    
    actions: Optional[List[CreateIVRMenuResponseActionsItem]] = None
    """ Keys handling settings """
    

class ReadIVRMenuResponsePromptMode(Enum):
    """ Prompt mode: custom media or text """
    
    Audio = 'Audio'
    TextToSpeech = 'TextToSpeech'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadIVRMenuResponsePromptAudio(DataClassJsonMixin):
    """ For 'Audio' mode only. Prompt media reference """
    
    uri: Optional[str] = None
    """ Link to a prompt audio file """
    
    id: Optional[str] = None
    """ Internal identifier of a prompt """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadIVRMenuResponsePromptLanguage(DataClassJsonMixin):
    """ For 'TextToSpeech' mode only. Prompt language metadata """
    
    uri: Optional[str] = None
    """ Link to a prompt language """
    
    id: Optional[str] = None
    """ Internal identifier of a language """
    
    name: Optional[str] = None
    """ Language name """
    
    locale_code: Optional[str] = None
    """ Language locale code """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadIVRMenuResponsePrompt(DataClassJsonMixin):
    """ Prompt metadata """
    
    mode: Optional[ReadIVRMenuResponsePromptMode] = None
    """ Prompt mode: custom media or text """
    
    audio: Optional[ReadIVRMenuResponsePromptAudio] = None
    """ For 'Audio' mode only. Prompt media reference """
    
    text: Optional[str] = None
    """ For 'TextToSpeech' mode only. Prompt text """
    
    language: Optional[ReadIVRMenuResponsePromptLanguage] = None
    """ For 'TextToSpeech' mode only. Prompt language metadata """
    

class ReadIVRMenuResponseActionsItemAction(Enum):
    """ Internal identifier of an answering rule """
    
    Connect = 'Connect'
    Voicemail = 'Voicemail'
    DialByName = 'DialByName'
    Transfer = 'Transfer'
    Repeat = 'Repeat'
    ReturnToRoot = 'ReturnToRoot'
    ReturnToPrevious = 'ReturnToPrevious'
    Disconnect = 'Disconnect'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadIVRMenuResponseActionsItemExtension(DataClassJsonMixin):
    """ For 'Connect' or 'Voicemail' actions only. Extension reference """
    
    uri: Optional[str] = None
    """ Link to an extension resource """
    
    id: Optional[str] = None
    """ Internal identifier of an extension """
    
    name: Optional[str] = None
    """ Name of an extension """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadIVRMenuResponseActionsItem(DataClassJsonMixin):
    input: Optional[str] = None
    """ Key. The following values are supported: numeric: '1' to '9' Star Hash NoInput """
    
    action: Optional[ReadIVRMenuResponseActionsItemAction] = None
    """ Internal identifier of an answering rule """
    
    extension: Optional[ReadIVRMenuResponseActionsItemExtension] = None
    """ For 'Connect' or 'Voicemail' actions only. Extension reference """
    
    phone_number: Optional[str] = None
    """ For 'Transfer' action only. PSTN number in E.164 format """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadIVRMenuResponse(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of an IVR Menu extension """
    
    uri: Optional[str] = None
    """ Link to an IVR Menu extension resource """
    
    name: Optional[str] = None
    """ First name of an IVR Menu user """
    
    extension_number: Optional[str] = None
    """ Number of an IVR Menu extension """
    
    site: Optional[str] = None
    """ Site data """
    
    prompt: Optional[ReadIVRMenuResponsePrompt] = None
    """ Prompt metadata """
    
    actions: Optional[List[ReadIVRMenuResponseActionsItem]] = None
    """ Keys handling settings """
    

class UpdateIVRMenuResponsePromptMode(Enum):
    """ Prompt mode: custom media or text """
    
    Audio = 'Audio'
    TextToSpeech = 'TextToSpeech'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateIVRMenuResponsePromptAudio(DataClassJsonMixin):
    """ For 'Audio' mode only. Prompt media reference """
    
    uri: Optional[str] = None
    """ Link to a prompt audio file """
    
    id: Optional[str] = None
    """ Internal identifier of a prompt """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateIVRMenuResponsePromptLanguage(DataClassJsonMixin):
    """ For 'TextToSpeech' mode only. Prompt language metadata """
    
    uri: Optional[str] = None
    """ Link to a prompt language """
    
    id: Optional[str] = None
    """ Internal identifier of a language """
    
    name: Optional[str] = None
    """ Language name """
    
    locale_code: Optional[str] = None
    """ Language locale code """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateIVRMenuResponsePrompt(DataClassJsonMixin):
    """ Prompt metadata """
    
    mode: Optional[UpdateIVRMenuResponsePromptMode] = None
    """ Prompt mode: custom media or text """
    
    audio: Optional[UpdateIVRMenuResponsePromptAudio] = None
    """ For 'Audio' mode only. Prompt media reference """
    
    text: Optional[str] = None
    """ For 'TextToSpeech' mode only. Prompt text """
    
    language: Optional[UpdateIVRMenuResponsePromptLanguage] = None
    """ For 'TextToSpeech' mode only. Prompt language metadata """
    

class UpdateIVRMenuResponseActionsItemAction(Enum):
    """ Internal identifier of an answering rule """
    
    Connect = 'Connect'
    Voicemail = 'Voicemail'
    DialByName = 'DialByName'
    Transfer = 'Transfer'
    Repeat = 'Repeat'
    ReturnToRoot = 'ReturnToRoot'
    ReturnToPrevious = 'ReturnToPrevious'
    Disconnect = 'Disconnect'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateIVRMenuResponseActionsItemExtension(DataClassJsonMixin):
    """ For 'Connect' or 'Voicemail' actions only. Extension reference """
    
    uri: Optional[str] = None
    """ Link to an extension resource """
    
    id: Optional[str] = None
    """ Internal identifier of an extension """
    
    name: Optional[str] = None
    """ Name of an extension """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateIVRMenuResponseActionsItem(DataClassJsonMixin):
    input: Optional[str] = None
    """ Key. The following values are supported: numeric: '1' to '9' Star Hash NoInput """
    
    action: Optional[UpdateIVRMenuResponseActionsItemAction] = None
    """ Internal identifier of an answering rule """
    
    extension: Optional[UpdateIVRMenuResponseActionsItemExtension] = None
    """ For 'Connect' or 'Voicemail' actions only. Extension reference """
    
    phone_number: Optional[str] = None
    """ For 'Transfer' action only. PSTN number in E.164 format """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateIVRMenuResponse(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of an IVR Menu extension """
    
    uri: Optional[str] = None
    """ Link to an IVR Menu extension resource """
    
    name: Optional[str] = None
    """ First name of an IVR Menu user """
    
    extension_number: Optional[str] = None
    """ Number of an IVR Menu extension """
    
    site: Optional[str] = None
    """ Site data """
    
    prompt: Optional[UpdateIVRMenuResponsePrompt] = None
    """ Prompt metadata """
    
    actions: Optional[List[UpdateIVRMenuResponseActionsItem]] = None
    """ Keys handling settings """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadCallRecordingSettingsResponseOnDemand(DataClassJsonMixin):
    enabled: Optional[bool] = None
    """ Flag for controlling OnDemand Call Recording settings """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadCallRecordingSettingsResponseAutomatic(DataClassJsonMixin):
    enabled: Optional[bool] = None
    """ Flag for controling Automatic Call Recording settings """
    
    outbound_call_tones: Optional[bool] = None
    """ Flag for controlling 'Play Call Recording Announcement for Outbound Calls' settings """
    
    outbound_call_announcement: Optional[bool] = None
    """ Flag for controlling 'Play periodic tones for outbound calls' settings """
    
    allow_mute: Optional[bool] = None
    """ Flag for controlling 'Allow mute in auto call recording' settings """
    
    extension_count: Optional[int] = None
    """ Total amount of extension that are used in call recordings """
    

class ReadCallRecordingSettingsResponseGreetingsItemType(Enum):
    StartRecording = 'StartRecording'
    StopRecording = 'StopRecording'
    AutomaticRecording = 'AutomaticRecording'

class ReadCallRecordingSettingsResponseGreetingsItemMode(Enum):
    """
    'Default' value specifies that all greetings of that type (in all languages) are default, if at
    least one greeting (in any language) of the specified type is custom, then 'Custom' value is
    returned.
    
    Generated by Python OpenAPI Parser
    """
    
    Default = 'Default'
    Custom = 'Custom'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadCallRecordingSettingsResponseGreetingsItem(DataClassJsonMixin):
    type: Optional[ReadCallRecordingSettingsResponseGreetingsItemType] = None
    mode: Optional[ReadCallRecordingSettingsResponseGreetingsItemMode] = None
    """
    'Default' value specifies that all greetings of that type (in all languages) are default, if at
    least one greeting (in any language) of the specified type is custom, then 'Custom' value is
    returned.
    """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadCallRecordingSettingsResponse(DataClassJsonMixin):
    on_demand: Optional[ReadCallRecordingSettingsResponseOnDemand] = None
    automatic: Optional[ReadCallRecordingSettingsResponseAutomatic] = None
    greetings: Optional[List[ReadCallRecordingSettingsResponseGreetingsItem]] = None
    """ Collection of Greeting Info """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateCallRecordingSettingsRequestOnDemand(DataClassJsonMixin):
    enabled: Optional[bool] = None
    """ Flag for controlling OnDemand Call Recording settings """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateCallRecordingSettingsRequestAutomatic(DataClassJsonMixin):
    enabled: Optional[bool] = None
    """ Flag for controling Automatic Call Recording settings """
    
    outbound_call_tones: Optional[bool] = None
    """ Flag for controlling 'Play Call Recording Announcement for Outbound Calls' settings """
    
    outbound_call_announcement: Optional[bool] = None
    """ Flag for controlling 'Play periodic tones for outbound calls' settings """
    
    allow_mute: Optional[bool] = None
    """ Flag for controlling 'Allow mute in auto call recording' settings """
    
    extension_count: Optional[int] = None
    """ Total amount of extension that are used in call recordings """
    

class UpdateCallRecordingSettingsRequestGreetingsItemType(Enum):
    StartRecording = 'StartRecording'
    StopRecording = 'StopRecording'
    AutomaticRecording = 'AutomaticRecording'

class UpdateCallRecordingSettingsRequestGreetingsItemMode(Enum):
    """
    'Default' value specifies that all greetings of that type (in all languages) are default, if at
    least one greeting (in any language) of the specified type is custom, then 'Custom' value is
    returned.
    
    Generated by Python OpenAPI Parser
    """
    
    Default = 'Default'
    Custom = 'Custom'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateCallRecordingSettingsRequestGreetingsItem(DataClassJsonMixin):
    type: Optional[UpdateCallRecordingSettingsRequestGreetingsItemType] = None
    mode: Optional[UpdateCallRecordingSettingsRequestGreetingsItemMode] = None
    """
    'Default' value specifies that all greetings of that type (in all languages) are default, if at
    least one greeting (in any language) of the specified type is custom, then 'Custom' value is
    returned.
    """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateCallRecordingSettingsRequest(DataClassJsonMixin):
    on_demand: Optional[UpdateCallRecordingSettingsRequestOnDemand] = None
    automatic: Optional[UpdateCallRecordingSettingsRequestAutomatic] = None
    greetings: Optional[List[UpdateCallRecordingSettingsRequestGreetingsItem]] = None
    """ Collection of Greeting Info """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateCallRecordingSettingsResponseOnDemand(DataClassJsonMixin):
    enabled: Optional[bool] = None
    """ Flag for controlling OnDemand Call Recording settings """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateCallRecordingSettingsResponseAutomatic(DataClassJsonMixin):
    enabled: Optional[bool] = None
    """ Flag for controling Automatic Call Recording settings """
    
    outbound_call_tones: Optional[bool] = None
    """ Flag for controlling 'Play Call Recording Announcement for Outbound Calls' settings """
    
    outbound_call_announcement: Optional[bool] = None
    """ Flag for controlling 'Play periodic tones for outbound calls' settings """
    
    allow_mute: Optional[bool] = None
    """ Flag for controlling 'Allow mute in auto call recording' settings """
    
    extension_count: Optional[int] = None
    """ Total amount of extension that are used in call recordings """
    

class UpdateCallRecordingSettingsResponseGreetingsItemType(Enum):
    StartRecording = 'StartRecording'
    StopRecording = 'StopRecording'
    AutomaticRecording = 'AutomaticRecording'

class UpdateCallRecordingSettingsResponseGreetingsItemMode(Enum):
    """
    'Default' value specifies that all greetings of that type (in all languages) are default, if at
    least one greeting (in any language) of the specified type is custom, then 'Custom' value is
    returned.
    
    Generated by Python OpenAPI Parser
    """
    
    Default = 'Default'
    Custom = 'Custom'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateCallRecordingSettingsResponseGreetingsItem(DataClassJsonMixin):
    type: Optional[UpdateCallRecordingSettingsResponseGreetingsItemType] = None
    mode: Optional[UpdateCallRecordingSettingsResponseGreetingsItemMode] = None
    """
    'Default' value specifies that all greetings of that type (in all languages) are default, if at
    least one greeting (in any language) of the specified type is custom, then 'Custom' value is
    returned.
    """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateCallRecordingSettingsResponse(DataClassJsonMixin):
    on_demand: Optional[UpdateCallRecordingSettingsResponseOnDemand] = None
    automatic: Optional[UpdateCallRecordingSettingsResponseAutomatic] = None
    greetings: Optional[List[UpdateCallRecordingSettingsResponseGreetingsItem]] = None
    """ Collection of Greeting Info """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListCallRecordingExtensionsResponseRecordsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of an extension """
    
    uri: Optional[str] = None
    """ Link to an extension resource """
    
    extension_number: Optional[str] = None
    """ Number of an extension """
    
    name: Optional[str] = None
    """ Name of an extension """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListCallRecordingExtensionsResponseNavigationFirstPage(DataClassJsonMixin):
    """ Canonical URI for the first page of the list """
    
    uri: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListCallRecordingExtensionsResponseNavigationNextPage(DataClassJsonMixin):
    """ Canonical URI for the next page of the list """
    
    uri: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListCallRecordingExtensionsResponseNavigationPreviousPage(DataClassJsonMixin):
    """ Canonical URI for the previous page of the list """
    
    uri: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListCallRecordingExtensionsResponseNavigationLastPage(DataClassJsonMixin):
    """ Canonical URI for the last page of the list """
    
    uri: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListCallRecordingExtensionsResponseNavigation(DataClassJsonMixin):
    """ Information on navigation """
    
    first_page: Optional[ListCallRecordingExtensionsResponseNavigationFirstPage] = None
    """ Canonical URI for the first page of the list """
    
    next_page: Optional[ListCallRecordingExtensionsResponseNavigationNextPage] = None
    """ Canonical URI for the next page of the list """
    
    previous_page: Optional[ListCallRecordingExtensionsResponseNavigationPreviousPage] = None
    """ Canonical URI for the previous page of the list """
    
    last_page: Optional[ListCallRecordingExtensionsResponseNavigationLastPage] = None
    """ Canonical URI for the last page of the list """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListCallRecordingExtensionsResponsePaging(DataClassJsonMixin):
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
class ListCallRecordingExtensionsResponse(DataClassJsonMixin):
    uri: Optional[str] = None
    """ Link to call recording extension list resource """
    
    records: Optional[List[ListCallRecordingExtensionsResponseRecordsItem]] = None
    navigation: Optional[ListCallRecordingExtensionsResponseNavigation] = None
    """ Information on navigation """
    
    paging: Optional[ListCallRecordingExtensionsResponsePaging] = None
    """ Information on paging """
    

class UpdateCallRecordingExtensionListRequestAddedExtensionsItemCallDirection(Enum):
    """ Direction of call """
    
    Outbound = 'Outbound'
    Inbound = 'Inbound'
    All = 'All'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateCallRecordingExtensionListRequestAddedExtensionsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of an extension """
    
    uri: Optional[str] = None
    extension_number: Optional[str] = None
    type: Optional[str] = None
    call_direction: Optional[UpdateCallRecordingExtensionListRequestAddedExtensionsItemCallDirection] = None
    """ Direction of call """
    

class UpdateCallRecordingExtensionListRequestUpdatedExtensionsItemCallDirection(Enum):
    """ Direction of call """
    
    Outbound = 'Outbound'
    Inbound = 'Inbound'
    All = 'All'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateCallRecordingExtensionListRequestUpdatedExtensionsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of an extension """
    
    uri: Optional[str] = None
    extension_number: Optional[str] = None
    type: Optional[str] = None
    call_direction: Optional[UpdateCallRecordingExtensionListRequestUpdatedExtensionsItemCallDirection] = None
    """ Direction of call """
    

class UpdateCallRecordingExtensionListRequestRemovedExtensionsItemCallDirection(Enum):
    """ Direction of call """
    
    Outbound = 'Outbound'
    Inbound = 'Inbound'
    All = 'All'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateCallRecordingExtensionListRequestRemovedExtensionsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of an extension """
    
    uri: Optional[str] = None
    extension_number: Optional[str] = None
    type: Optional[str] = None
    call_direction: Optional[UpdateCallRecordingExtensionListRequestRemovedExtensionsItemCallDirection] = None
    """ Direction of call """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateCallRecordingExtensionListRequest(DataClassJsonMixin):
    added_extensions: Optional[List[UpdateCallRecordingExtensionListRequestAddedExtensionsItem]] = None
    updated_extensions: Optional[List[UpdateCallRecordingExtensionListRequestUpdatedExtensionsItem]] = None
    removed_extensions: Optional[List[UpdateCallRecordingExtensionListRequestRemovedExtensionsItem]] = None

class ListCallRecordingCustomGreetingsType(Enum):
    StartRecording = 'StartRecording'
    StopRecording = 'StopRecording'
    AutomaticRecording = 'AutomaticRecording'

class ListCallRecordingCustomGreetingsResponseRecordsItemType(Enum):
    StartRecording = 'StartRecording'
    StopRecording = 'StopRecording'
    AutomaticRecording = 'AutomaticRecording'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListCallRecordingCustomGreetingsResponseRecordsItemCustom(DataClassJsonMixin):
    """ Custom greeting data """
    
    uri: Optional[str] = None
    """ Link to a custom company greeting """
    
    id: Optional[str] = None
    """ Internal identifier of a custom company greeting """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListCallRecordingCustomGreetingsResponseRecordsItemLanguage(DataClassJsonMixin):
    """ Custom greeting language """
    
    uri: Optional[str] = None
    """ Link to a language """
    
    id: Optional[str] = None
    """ Internal identifier of a language """
    
    name: Optional[str] = None
    """ Language name """
    
    locale_code: Optional[str] = None
    """ Language locale code """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListCallRecordingCustomGreetingsResponseRecordsItem(DataClassJsonMixin):
    type: Optional[ListCallRecordingCustomGreetingsResponseRecordsItemType] = None
    custom: Optional[ListCallRecordingCustomGreetingsResponseRecordsItemCustom] = None
    """ Custom greeting data """
    
    language: Optional[ListCallRecordingCustomGreetingsResponseRecordsItemLanguage] = None
    """ Custom greeting language """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListCallRecordingCustomGreetingsResponse(DataClassJsonMixin):
    """ Returns data on call recording custom greetings. """
    
    records: Optional[List[ListCallRecordingCustomGreetingsResponseRecordsItem]] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateSIPRegistrationRequestDevice(DataClassJsonMixin):
    """ Device unique description """
    
    id: Optional[str] = None
    """ Device unique identifier, retrieved on previous session (if any) """
    
    app_external_id: Optional[str] = None
    """
    Supported for iOS devices only. Certificate name (used by iOS applications for APNS
    subscription)
    """
    
    computer_name: Optional[str] = None
    """ Supported for SoftPhone only. Computer name """
    
    serial: Optional[str] = None
    """
    Serial number for HardPhone; endpoint_id for softphone and mobile applications. Returned only
    when the phone is shipped and provisioned
    """
    

class CreateSIPRegistrationRequestSipInfoItemTransport(Enum):
    """ Supported transport. SIP info will be returned for this transport if supported """
    
    UDP = 'UDP'
    TCP = 'TCP'
    TLS = 'TLS'
    WS = 'WS'
    WSS = 'WSS'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateSIPRegistrationRequestSipInfoItem(DataClassJsonMixin):
    transport: Optional[CreateSIPRegistrationRequestSipInfoItemTransport] = None
    """ Supported transport. SIP info will be returned for this transport if supported """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateSIPRegistrationRequest(DataClassJsonMixin):
    device: Optional[CreateSIPRegistrationRequestDevice] = None
    """ Device unique description """
    
    sip_info: Optional[List[CreateSIPRegistrationRequestSipInfoItem]] = None
    """ SIP settings for device """
    

class CreateSIPRegistrationResponseDeviceType(Enum):
    """ Device type """
    
    HardPhone = 'HardPhone'
    SoftPhone = 'SoftPhone'
    OtherPhone = 'OtherPhone'
    Paging = 'Paging'
    WebPhone = 'WebPhone'

class CreateSIPRegistrationResponseDeviceStatus(Enum):
    Online = 'Online'
    Offline = 'Offline'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateSIPRegistrationResponseDeviceModelAddonsItem(DataClassJsonMixin):
    id: Optional[str] = None
    name: Optional[str] = None
    count: Optional[str] = None

class CreateSIPRegistrationResponseDeviceModelFeaturesItem(Enum):
    BLA = 'BLA'
    Intercom = 'Intercom'
    Paging = 'Paging'
    HELD = 'HELD'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateSIPRegistrationResponseDeviceModel(DataClassJsonMixin):
    """
    HardPhone model information
    
    Required Properties:
     - addons
    
    Generated by Python OpenAPI Parser
    """
    
    addons: List[CreateSIPRegistrationResponseDeviceModelAddonsItem]
    """ Addons description """
    
    id: Optional[str] = None
    """
    Addon identifier. For HardPhones of certain types, which are compatible with this addon
    identifier
    """
    
    name: Optional[str] = None
    """ Device name """
    
    features: Optional[List[CreateSIPRegistrationResponseDeviceModelFeaturesItem]] = None
    """ Device feature or multiple features supported """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateSIPRegistrationResponseDeviceExtension(DataClassJsonMixin):
    """ Internal identifier of an extension the device should be assigned to """
    
    id: Optional[int] = None
    """ Internal identifier of an extension """
    
    uri: Optional[str] = None
    """ Link to an extension resource """
    
    extension_number: Optional[str] = None
    """ Number of extension """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateSIPRegistrationResponseDeviceEmergencyServiceAddress(DataClassJsonMixin):
    """
    Address for emergency cases. The same emergency address is assigned to all the numbers of one
    device
    
    Generated by Python OpenAPI Parser
    """
    
    street: Optional[str] = None
    street2: Optional[str] = None
    city: Optional[str] = None
    zip: Optional[str] = None
    customer_name: Optional[str] = None
    state: Optional[str] = None
    """ State/province name """
    
    state_id: Optional[str] = None
    """ Internal identifier of a state """
    
    state_iso_code: Optional[str] = None
    """ ISO code of a state """
    
    state_name: Optional[str] = None
    """ Full name of a state """
    
    country_id: Optional[str] = None
    """ Internal identifier of a country """
    
    country_iso_code: Optional[str] = None
    """ ISO code of a country """
    
    country: Optional[str] = None
    """ Country name """
    
    country_name: Optional[str] = None
    """ Full name of a country """
    
    out_of_country: Optional[bool] = None
    """ Specifies if emergency address is out of country """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateSIPRegistrationResponseDeviceEmergencyAddress(DataClassJsonMixin):
    street: Optional[str] = None
    street2: Optional[str] = None
    city: Optional[str] = None
    zip: Optional[str] = None
    customer_name: Optional[str] = None
    state: Optional[str] = None
    """ State/province name """
    
    state_id: Optional[str] = None
    """ Internal identifier of a state """
    
    state_iso_code: Optional[str] = None
    """ ISO code of a state """
    
    state_name: Optional[str] = None
    """ Full name of a state """
    
    country_id: Optional[str] = None
    """ Internal identifier of a country """
    
    country_iso_code: Optional[str] = None
    """ ISO code of a country """
    
    country: Optional[str] = None
    """ Country name """
    
    country_name: Optional[str] = None
    """ Full name of a country """
    
    out_of_country: Optional[bool] = None
    """ Specifies if emergency address is out of country """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateSIPRegistrationResponseDeviceEmergencyLocation(DataClassJsonMixin):
    """ Company emergency response location details """
    
    id: Optional[str] = None
    """ Internal identifier of an emergency response location """
    
    name: Optional[str] = None
    """ Emergency response location name """
    

class CreateSIPRegistrationResponseDeviceEmergencyAddressStatus(Enum):
    """ Emergency address status """
    
    Valid = 'Valid'
    Invalid = 'Invalid'

class CreateSIPRegistrationResponseDeviceEmergencySyncStatus(Enum):
    """
    Resulting status of emergency address synchronization. Returned if `syncEmergencyAddress`
    parameter is set to 'True'
    
    Generated by Python OpenAPI Parser
    """
    
    Verified = 'Verified'
    Updated = 'Updated'
    Deleted = 'Deleted'
    NotRequired = 'NotRequired'
    Unsupported = 'Unsupported'
    Failed = 'Failed'

class CreateSIPRegistrationResponseDeviceEmergencyAddressEditableStatus(Enum):
    """
    Ability to register new emergency address for a phone line using devices sharing this line or
    only main device (line owner)
    
    Generated by Python OpenAPI Parser
    """
    
    MainDevice = 'MainDevice'
    AnyDevice = 'AnyDevice'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateSIPRegistrationResponseDeviceEmergency(DataClassJsonMixin):
    """ Emergency response location settings of a device """
    
    address: Optional[CreateSIPRegistrationResponseDeviceEmergencyAddress] = None
    location: Optional[CreateSIPRegistrationResponseDeviceEmergencyLocation] = None
    """ Company emergency response location details """
    
    out_of_country: Optional[bool] = None
    """ Specifies if emergency address is out of country """
    
    address_status: Optional[CreateSIPRegistrationResponseDeviceEmergencyAddressStatus] = None
    """ Emergency address status """
    
    sync_status: Optional[CreateSIPRegistrationResponseDeviceEmergencySyncStatus] = None
    """
    Resulting status of emergency address synchronization. Returned if `syncEmergencyAddress`
    parameter is set to 'True'
    """
    
    address_editable_status: Optional[CreateSIPRegistrationResponseDeviceEmergencyAddressEditableStatus] = None
    """
    Ability to register new emergency address for a phone line using devices sharing this line or
    only main device (line owner)
    """
    
    address_required: Optional[bool] = None
    """ 'True' if emergency address is required for the country of a phone line """
    
    address_location_only: Optional[bool] = None
    """ 'True' if out of country emergency address is not allowed for the country of a phone line """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateSIPRegistrationResponseDeviceShippingAddress(DataClassJsonMixin):
    street: Optional[str] = None
    street2: Optional[str] = None
    city: Optional[str] = None
    zip: Optional[str] = None
    customer_name: Optional[str] = None
    state: Optional[str] = None
    """ State/province name """
    
    state_id: Optional[str] = None
    """ Internal identifier of a state """
    
    state_iso_code: Optional[str] = None
    """ ISO code of a state """
    
    state_name: Optional[str] = None
    """ Full name of a state """
    
    country_id: Optional[str] = None
    """ Internal identifier of a country """
    
    country_iso_code: Optional[str] = None
    """ ISO code of a country """
    
    country: Optional[str] = None
    """ Country name """
    
    country_name: Optional[str] = None
    """ Full name of a country """
    
    out_of_country: Optional[bool] = None
    """ Specifies if emergency address is out of country """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateSIPRegistrationResponseDeviceShippingMethod(DataClassJsonMixin):
    id: Optional[str] = None
    name: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateSIPRegistrationResponseDeviceShipping(DataClassJsonMixin):
    """
    Shipping information, according to which devices (in case of HardPhone ) or e911 stickers (in
    case of SoftPhone and OtherPhone ) will be delivered to the customer
    
    Generated by Python OpenAPI Parser
    """
    
    address: Optional[CreateSIPRegistrationResponseDeviceShippingAddress] = None
    method: Optional[CreateSIPRegistrationResponseDeviceShippingMethod] = None
    status: Optional[str] = None
    carrier: Optional[str] = None
    tracking_number: Optional[str] = None

class CreateSIPRegistrationResponseDevicePhoneLinesItemLineType(Enum):
    """ Type of phone line """
    
    Standalone = 'Standalone'
    StandaloneFree = 'StandaloneFree'
    BlaPrimary = 'BlaPrimary'
    BlaSecondary = 'BlaSecondary'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateSIPRegistrationResponseDevicePhoneLinesItemEmergencyAddress(DataClassJsonMixin):
    required: Optional[bool] = None
    """ 'True' if specifying of emergency address is required """
    
    local_only: Optional[bool] = None
    """ 'True' if only local emergency address can be specified """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateSIPRegistrationResponseDevicePhoneLinesItemPhoneInfoCountry(DataClassJsonMixin):
    """ Brief information on a phone number country """
    
    id: Optional[str] = None
    """ Internal identifier of a home country """
    
    uri: Optional[str] = None
    """ Canonical URI of a home country """
    
    name: Optional[str] = None
    """ Official name of a home country """
    

class CreateSIPRegistrationResponseDevicePhoneLinesItemPhoneInfoPaymentType(Enum):
    """
    Payment type. 'External' is returned for forwarded numbers which are not terminated in the
    RingCentral phone system = ['External', 'TollFree', 'Local'],
    
    Generated by Python OpenAPI Parser
    """
    
    External = 'External'
    TollFree = 'TollFree'
    Local = 'Local'

class CreateSIPRegistrationResponseDevicePhoneLinesItemPhoneInfoUsageType(Enum):
    CompanyNumber = 'CompanyNumber'
    MainCompanyNumber = 'MainCompanyNumber'
    AdditionalCompanyNumber = 'AdditionalCompanyNumber'
    DirectNumber = 'DirectNumber'
    CompanyFaxNumber = 'CompanyFaxNumber'
    ForwardedNumber = 'ForwardedNumber'
    ForwardedCompanyNumber = 'ForwardedCompanyNumber'
    ContactCenterNumber = 'ContactCenterNumber'

class CreateSIPRegistrationResponseDevicePhoneLinesItemPhoneInfoType(Enum):
    """ Type of a phone number """
    
    VoiceFax = 'VoiceFax'
    FaxOnly = 'FaxOnly'
    VoiceOnly = 'VoiceOnly'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateSIPRegistrationResponseDevicePhoneLinesItemPhoneInfo(DataClassJsonMixin):
    """ Phone number information """
    
    id: Optional[int] = None
    """ Internal identifier of a phone number """
    
    country: Optional[CreateSIPRegistrationResponseDevicePhoneLinesItemPhoneInfoCountry] = None
    """ Brief information on a phone number country """
    
    payment_type: Optional[CreateSIPRegistrationResponseDevicePhoneLinesItemPhoneInfoPaymentType] = None
    """
    Payment type. 'External' is returned for forwarded numbers which are not terminated in the
    RingCentral phone system = ['External', 'TollFree', 'Local'],
    """
    
    phone_number: Optional[str] = None
    """ Phone number """
    
    usage_type: Optional[CreateSIPRegistrationResponseDevicePhoneLinesItemPhoneInfoUsageType] = None
    type: Optional[CreateSIPRegistrationResponseDevicePhoneLinesItemPhoneInfoType] = None
    """ Type of a phone number """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateSIPRegistrationResponseDevicePhoneLinesItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a phone line """
    
    line_type: Optional[CreateSIPRegistrationResponseDevicePhoneLinesItemLineType] = None
    """ Type of phone line """
    
    emergency_address: Optional[CreateSIPRegistrationResponseDevicePhoneLinesItemEmergencyAddress] = None
    phone_info: Optional[CreateSIPRegistrationResponseDevicePhoneLinesItemPhoneInfo] = None
    """ Phone number information """
    

class CreateSIPRegistrationResponseDeviceLinePooling(Enum):
    """
    Pooling type of a deviceHost - device with standalone paid phone line which can be linked to
    Glip/Softphone instanceGuest - device with a linked phone lineNone - device without a phone
    line or with specific line (free, BLA, etc.) = ['Host', 'Guest', 'None']
    
    Generated by Python OpenAPI Parser
    """
    
    Host = 'Host'
    Guest = 'Guest'
    None_ = 'None'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateSIPRegistrationResponseDeviceSite(DataClassJsonMixin):
    """ Site data """
    
    id: Optional[str] = None
    """ Internal identifier of a site """
    
    name: Optional[str] = None
    """ Name of a site """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateSIPRegistrationResponseDevice(DataClassJsonMixin):
    uri: Optional[str] = None
    """ Link to a device resource """
    
    id: Optional[str] = None
    """ Internal identifier of a Device """
    
    type: Optional[CreateSIPRegistrationResponseDeviceType] = None
    """ Device type """
    
    sku: Optional[str] = None
    """
    Device identification number (stock keeping unit) in the format TP-ID [-AT-AC], where TP is
    device type (HP for RC HardPhone, DV for all other devices including softphone); ID - device
    model ID; AT -addon type ID; AC - addon count (if any). For example 'HP-56-2-2'
    """
    
    status: Optional[CreateSIPRegistrationResponseDeviceStatus] = None
    name: Optional[str] = None
    """
    Device name. Mandatory if ordering SoftPhone or OtherPhone. Optional for HardPhone. If not
    specified for HardPhone, then device model name is used as device name
    """
    
    serial: Optional[str] = None
    """
    Serial number for HardPhone (is returned only when the phone is shipped and provisioned);
    endpoint_id for softphone and mobile applications
    """
    
    computer_name: Optional[str] = None
    """ PC name for softphone """
    
    model: Optional[CreateSIPRegistrationResponseDeviceModel] = None
    """ HardPhone model information """
    
    extension: Optional[CreateSIPRegistrationResponseDeviceExtension] = None
    """ Internal identifier of an extension the device should be assigned to """
    
    emergency_service_address: Optional[CreateSIPRegistrationResponseDeviceEmergencyServiceAddress] = None
    """
    Address for emergency cases. The same emergency address is assigned to all the numbers of one
    device
    """
    
    emergency: Optional[CreateSIPRegistrationResponseDeviceEmergency] = None
    """ Emergency response location settings of a device """
    
    shipping: Optional[CreateSIPRegistrationResponseDeviceShipping] = None
    """
    Shipping information, according to which devices (in case of HardPhone ) or e911 stickers (in
    case of SoftPhone and OtherPhone ) will be delivered to the customer
    """
    
    phone_lines: Optional[List[CreateSIPRegistrationResponseDevicePhoneLinesItem]] = None
    """ Phone lines information """
    
    box_billing_id: Optional[int] = None
    """
    Box billing identifier of a device. Applicable only for HardPhones. It is an alternative way to
    identify the device to be ordered. EitherT? model structure, or boxBillingId must be specified
    forT?HardPhone
    """
    
    use_as_common_phone: Optional[bool] = None
    """
    Supported only for devices assigned to Limited extensions. If true, enables users to log in to
    this phone as a common phone.
    """
    
    line_pooling: Optional[CreateSIPRegistrationResponseDeviceLinePooling] = None
    """
    Pooling type of a deviceHost - device with standalone paid phone line which can be linked to
    Glip/Softphone instanceGuest - device with a linked phone lineNone - device without a phone
    line or with specific line (free, BLA, etc.) = ['Host', 'Guest', 'None']
    """
    
    in_company_net: Optional[bool] = None
    """
    Network location status. 'True' if the device is located in the configured corporate network
    (On-Net); 'False' for Off-Net location. Parameter is not returned if
    `EmergencyAddressAutoUpdate` feature is not enabled for the account/user, or if device network
    location is not determined
    """
    
    site: Optional[CreateSIPRegistrationResponseDeviceSite] = None
    """ Site data """
    
    last_location_report_time: Optional[str] = None
    """
    Datetime of receiving last location report in [ISO
    8601](https://en.wikipedia.org/wiki/ISO_8601) format including timezone, for example
    *2016-03-10T18:07:52.534Z
    """
    

class CreateSIPRegistrationResponseSipInfoItemTransport(Enum):
    """ Preferred transport. SIP info will be returned for this transport if supported """
    
    UDP = 'UDP'
    TCP = 'TCP'
    TLS = 'TLS'
    WS = 'WS'
    WSS = 'WSS'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateSIPRegistrationResponseSipInfoItem(DataClassJsonMixin):
    username: Optional[str] = None
    """ User credentials """
    
    password: Optional[str] = None
    """ User password """
    
    authorization_id: Optional[str] = None
    """ Identifier for SIP authorization """
    
    omain: Optional[str] = None
    """ SIP domain """
    
    outbound_proxy: Optional[str] = None
    """ SIP outbound proxy """
    
    outbound_proxy_i_pv6: Optional[str] = None
    """ SIP outbound IPv6 proxy """
    
    outbound_proxy_backup: Optional[str] = None
    """ SIP outbound proxy backup """
    
    outbound_proxy_i_pv6_backup: Optional[str] = None
    """ SIP outbound IPv6 proxy backup """
    
    transport: Optional[CreateSIPRegistrationResponseSipInfoItemTransport] = None
    """ Preferred transport. SIP info will be returned for this transport if supported """
    
    certificate: Optional[str] = None
    """ For TLS transport only Base64 encoded certificate """
    
    switch_back_interval: Optional[int] = None
    """
    The interval in seconds after which the app must try to switch back to primary proxy if it was
    previously switched to backup. If this parameter is not returned, the app must stay on backup
    proxy and try to switch to primary proxy after the next SIP-provision call.
    """
    

class CreateSIPRegistrationResponseSipInfoPstnItemTransport(Enum):
    """ Preferred transport. SIP info will be returned for this transport if supported """
    
    UDP = 'UDP'
    TCP = 'TCP'
    TLS = 'TLS'
    WS = 'WS'
    WSS = 'WSS'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateSIPRegistrationResponseSipInfoPstnItem(DataClassJsonMixin):
    username: Optional[str] = None
    """ User credentials """
    
    password: Optional[str] = None
    """ User password """
    
    authorization_id: Optional[str] = None
    """ Identifier for SIP authorization """
    
    omain: Optional[str] = None
    """ SIP domain """
    
    outbound_proxy: Optional[str] = None
    """ SIP outbound proxy """
    
    outbound_proxy_i_pv6: Optional[str] = None
    """ SIP outbound IPv6 proxy """
    
    outbound_proxy_backup: Optional[str] = None
    """ SIP outbound proxy backup """
    
    outbound_proxy_i_pv6_backup: Optional[str] = None
    """ SIP outbound IPv6 proxy backup """
    
    transport: Optional[CreateSIPRegistrationResponseSipInfoPstnItemTransport] = None
    """ Preferred transport. SIP info will be returned for this transport if supported """
    
    certificate: Optional[str] = None
    """ For TLS transport only Base64 encoded certificate """
    
    switch_back_interval: Optional[int] = None
    """
    The interval in seconds after which the app must try to switch back to primary proxy if it was
    previously switched to backup. If this parameter is not returned, the app must stay on backup
    proxy and try to switch to primary proxy after the next SIP-provision call.
    """
    

class CreateSIPRegistrationResponseSipFlagsVoipFeatureEnabled(Enum):
    """ If 'True' VoIP calling feature is enabled """
    
    True_ = 'True'
    False_ = 'False'

class CreateSIPRegistrationResponseSipFlagsVoipCountryBlocked(Enum):
    """ If 'True' the request is sent from IP address of a country blocked for VoIP calling """
    
    True_ = 'True'
    False_ = 'False'

class CreateSIPRegistrationResponseSipFlagsOutboundCallsEnabled(Enum):
    """ If 'True' outbound calls are enabled """
    
    True_ = 'True'
    False_ = 'False'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateSIPRegistrationResponseSipFlags(DataClassJsonMixin):
    """ SIP flags data """
    
    voip_feature_enabled: Optional[CreateSIPRegistrationResponseSipFlagsVoipFeatureEnabled] = None
    """ If 'True' VoIP calling feature is enabled """
    
    voip_country_blocked: Optional[CreateSIPRegistrationResponseSipFlagsVoipCountryBlocked] = None
    """ If 'True' the request is sent from IP address of a country blocked for VoIP calling """
    
    outbound_calls_enabled: Optional[CreateSIPRegistrationResponseSipFlagsOutboundCallsEnabled] = None
    """ If 'True' outbound calls are enabled """
    
    dscp_enabled: Optional[bool] = None
    dscp_signaling: Optional[int] = None
    dscp_voice: Optional[int] = None
    dscp_video: Optional[int] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateSIPRegistrationResponse(DataClassJsonMixin):
    """
    Required Properties:
     - sip_flags
     - sip_info
    
    Generated by Python OpenAPI Parser
    """
    
    sip_info: List[CreateSIPRegistrationResponseSipInfoItem]
    """ SIP settings for device """
    
    sip_flags: CreateSIPRegistrationResponseSipFlags
    """ SIP flags data """
    
    device: Optional[CreateSIPRegistrationResponseDevice] = None
    sip_info_pstn: Optional[List[CreateSIPRegistrationResponseSipInfoPstnItem]] = None
    """ SIP PSTN settings for device """
    
    sip_error_codes: Optional[List[str]] = None

class ListExtensionPhoneNumbersStatus(Enum):
    Normal = 'Normal'
    Pending = 'Pending'
    PortedIn = 'PortedIn'
    Temporary = 'Temporary'

class ListExtensionPhoneNumbersUsageTypeItem(Enum):
    MainCompanyNumber = 'MainCompanyNumber'
    AdditionalCompanyNumber = 'AdditionalCompanyNumber'
    CompanyNumber = 'CompanyNumber'
    DirectNumber = 'DirectNumber'
    CompanyFaxNumber = 'CompanyFaxNumber'
    ForwardedNumber = 'ForwardedNumber'
    ForwardedCompanyNumber = 'ForwardedCompanyNumber'
    BusinessMobileNumber = 'BusinessMobileNumber'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListExtensionPhoneNumbersResponseRecordsItemCountry(DataClassJsonMixin):
    """ Brief information on a phone number country """
    
    id: Optional[str] = None
    """ Internal identifier of a home country """
    
    uri: Optional[str] = None
    """ Canonical URI of a home country """
    
    name: Optional[str] = None
    """ Official name of a home country """
    
    iso_code: Optional[str] = None
    """ ISO code of a country """
    
    calling_code: Optional[str] = None
    """ Calling code of a country """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListExtensionPhoneNumbersResponseRecordsItemContactCenterProvider(DataClassJsonMixin):
    """
    CCRN (Contact Center Routing Number) provider. If not specified then the default value
    'InContact/North America' is used, its ID is '1'
    
    Generated by Python OpenAPI Parser
    """
    
    id: Optional[str] = None
    """ Internal identifier of the provider """
    
    name: Optional[str] = None
    """ Provider's name """
    

class ListExtensionPhoneNumbersResponseRecordsItemExtensionType(Enum):
    """ Extension type """
    
    User = 'User'
    FaxUser = 'FaxUser'
    VirtualUser = 'VirtualUser'
    DigitalUser = 'DigitalUser'
    Department = 'Department'
    Announcement = 'Announcement'
    Voicemail = 'Voicemail'
    SharedLinesGroup = 'SharedLinesGroup'
    PagingOnly = 'PagingOnly'
    IvrMenu = 'IvrMenu'
    ApplicationExtension = 'ApplicationExtension'
    ParkLocation = 'ParkLocation'
    Site = 'Site'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListExtensionPhoneNumbersResponseRecordsItemExtensionContactCenterProvider(DataClassJsonMixin):
    """
    CCRN (Contact Center Routing Number) provider. If not specified then the default value
    'InContact/North America' is used, its ID is '1'
    
    Generated by Python OpenAPI Parser
    """
    
    id: Optional[str] = None
    """ Internal identifier of the provider """
    
    name: Optional[str] = None
    """ Provider's name """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListExtensionPhoneNumbersResponseRecordsItemExtension(DataClassJsonMixin):
    """
    Information on the extension, to which the phone number is assigned. Returned only for the
    request of Account phone number list
    
    Generated by Python OpenAPI Parser
    """
    
    id: Optional[int] = None
    """ Internal identifier of an extension """
    
    uri: Optional[str] = None
    """ Canonical URI of an extension """
    
    extension_number: Optional[str] = None
    """ Number of department extension """
    
    partner_id: Optional[str] = None
    """
    For Partner Applications Internal identifier of an extension created by partner. The
    RingCentral supports the mapping of accounts and stores the corresponding account ID/extension
    ID for each partner ID of a client application. In request URIs partner IDs are accepted
    instead of regular RingCentral native IDs as path parameters using pid = XXX clause. Though in
    response URIs contain the corresponding account IDs and extension IDs. In all request and
    response bodies these values are reflected via partnerId attributes of account and extension
    """
    
    type: Optional[ListExtensionPhoneNumbersResponseRecordsItemExtensionType] = None
    """ Extension type """
    
    contact_center_provider: Optional[ListExtensionPhoneNumbersResponseRecordsItemExtensionContactCenterProvider] = None
    """
    CCRN (Contact Center Routing Number) provider. If not specified then the default value
    'InContact/North America' is used, its ID is '1'
    """
    
    name: Optional[str] = None
    """
    Extension name. For user extension types the value is a combination of the specified first name
    and last name
    """
    

class ListExtensionPhoneNumbersResponseRecordsItemPaymentType(Enum):
    """
    Payment type. 'External' is returned for forwarded numbers which are not terminated in the
    RingCentral phone system
    
    Generated by Python OpenAPI Parser
    """
    
    External = 'External'
    TollFree = 'TollFree'
    Local = 'Local'
    BusinessMobileNumberProvider = 'BusinessMobileNumberProvider'

class ListExtensionPhoneNumbersResponseRecordsItemType(Enum):
    """ Phone number type """
    
    VoiceFax = 'VoiceFax'
    FaxOnly = 'FaxOnly'
    VoiceOnly = 'VoiceOnly'

class ListExtensionPhoneNumbersResponseRecordsItemUsageType(Enum):
    """
    Usage type of a phone number. Numbers of 'NumberPool' type wont't be returned for phone number
    list requests
    
    Generated by Python OpenAPI Parser
    """
    
    MainCompanyNumber = 'MainCompanyNumber'
    AdditionalCompanyNumber = 'AdditionalCompanyNumber'
    CompanyNumber = 'CompanyNumber'
    DirectNumber = 'DirectNumber'
    CompanyFaxNumber = 'CompanyFaxNumber'
    ForwardedNumber = 'ForwardedNumber'
    ForwardedCompanyNumber = 'ForwardedCompanyNumber'
    ContactCenterNumber = 'ContactCenterNumber'
    ConferencingNumber = 'ConferencingNumber'
    NumberPool = 'NumberPool'
    BusinessMobileNumber = 'BusinessMobileNumber'

class ListExtensionPhoneNumbersResponseRecordsItemFeaturesItem(Enum):
    CallerId = 'CallerId'
    SmsSender = 'SmsSender'
    A2PSmsSender = 'A2PSmsSender'
    MmsSender = 'MmsSender'
    InternationalSmsSender = 'InternationalSmsSender'
    Delegated = 'Delegated'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListExtensionPhoneNumbersResponseRecordsItem(DataClassJsonMixin):
    uri: Optional[str] = None
    """ Link to the user's phone number resource """
    
    id: Optional[int] = None
    """ Internal identifier of a phone number """
    
    country: Optional[ListExtensionPhoneNumbersResponseRecordsItemCountry] = None
    """ Brief information on a phone number country """
    
    contact_center_provider: Optional[ListExtensionPhoneNumbersResponseRecordsItemContactCenterProvider] = None
    """
    CCRN (Contact Center Routing Number) provider. If not specified then the default value
    'InContact/North America' is used, its ID is '1'
    """
    
    extension: Optional[ListExtensionPhoneNumbersResponseRecordsItemExtension] = None
    """
    Information on the extension, to which the phone number is assigned. Returned only for the
    request of Account phone number list
    """
    
    label: Optional[str] = None
    """ Custom user name of a phone number, if any """
    
    location: Optional[str] = None
    """ Location (City, State). Filled for local US numbers """
    
    payment_type: Optional[ListExtensionPhoneNumbersResponseRecordsItemPaymentType] = None
    """
    Payment type. 'External' is returned for forwarded numbers which are not terminated in the
    RingCentral phone system
    """
    
    phone_number: Optional[str] = None
    """ Phone number """
    
    status: Optional[str] = None
    """
    Status of a phone number. If the value is 'Normal', the phone number is ready to be used.
    Otherwise it is an external number not yet ported to RingCentral
    """
    
    type: Optional[ListExtensionPhoneNumbersResponseRecordsItemType] = None
    """ Phone number type """
    
    usage_type: Optional[ListExtensionPhoneNumbersResponseRecordsItemUsageType] = None
    """
    Usage type of a phone number. Numbers of 'NumberPool' type wont't be returned for phone number
    list requests
    """
    
    features: Optional[List[ListExtensionPhoneNumbersResponseRecordsItemFeaturesItem]] = None
    """ List of features of a phone number """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListExtensionPhoneNumbersResponseNavigationFirstPage(DataClassJsonMixin):
    """ Canonical URI for the first page of the list """
    
    uri: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListExtensionPhoneNumbersResponseNavigationNextPage(DataClassJsonMixin):
    """ Canonical URI for the next page of the list """
    
    uri: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListExtensionPhoneNumbersResponseNavigationPreviousPage(DataClassJsonMixin):
    """ Canonical URI for the previous page of the list """
    
    uri: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListExtensionPhoneNumbersResponseNavigationLastPage(DataClassJsonMixin):
    """ Canonical URI for the last page of the list """
    
    uri: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListExtensionPhoneNumbersResponseNavigation(DataClassJsonMixin):
    """ Information on navigation """
    
    first_page: Optional[ListExtensionPhoneNumbersResponseNavigationFirstPage] = None
    """ Canonical URI for the first page of the list """
    
    next_page: Optional[ListExtensionPhoneNumbersResponseNavigationNextPage] = None
    """ Canonical URI for the next page of the list """
    
    previous_page: Optional[ListExtensionPhoneNumbersResponseNavigationPreviousPage] = None
    """ Canonical URI for the previous page of the list """
    
    last_page: Optional[ListExtensionPhoneNumbersResponseNavigationLastPage] = None
    """ Canonical URI for the last page of the list """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListExtensionPhoneNumbersResponsePaging(DataClassJsonMixin):
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
class ListExtensionPhoneNumbersResponse(DataClassJsonMixin):
    """
    Required Properties:
     - navigation
     - paging
     - records
    
    Generated by Python OpenAPI Parser
    """
    
    records: List[ListExtensionPhoneNumbersResponseRecordsItem]
    """ List of phone numbers """
    
    navigation: ListExtensionPhoneNumbersResponseNavigation
    """ Information on navigation """
    
    paging: ListExtensionPhoneNumbersResponsePaging
    """ Information on paging """
    
    uri: Optional[str] = None
    """ Link to the user's phone number list resource """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadExtensionResponseAccount(DataClassJsonMixin):
    """ Account information """
    
    id: Optional[str] = None
    """ Internal identifier of an account """
    
    uri: Optional[str] = None
    """ Canonical URI of an account """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadExtensionResponseContactBusinessAddress(DataClassJsonMixin):
    """ Business address of extension user company """
    
    country: Optional[str] = None
    """ Country name of an extension user company """
    
    state: Optional[str] = None
    """ State/province name of an extension user company. Mandatory for the USA, UK and Canada """
    
    city: Optional[str] = None
    """ City name of an extension user company """
    
    street: Optional[str] = None
    """ Street address of an extension user company """
    
    zip: Optional[str] = None
    """ Zip code of an extension user company """
    

class ReadExtensionResponseContactPronouncedNameType(Enum):
    """
    Voice name type. 'Default' - default extension name; first name and last name specified in user
    profile; 'TextToSpeech' - custom text; user name spelled the way it sounds and specified by
    user; 'Recorded' - custom audio, user name recorded in user's own voice (supported only for
    extension retrieval)
    
    Generated by Python OpenAPI Parser
    """
    
    Default = 'Default'
    TextToSpeech = 'TextToSpeech'
    Recorded = 'Recorded'

class ReadExtensionResponseContactPronouncedNamePromptContentType(Enum):
    """ Content media type """
    
    AudioMpeg = 'audio/mpeg'
    AudioWav = 'audio/wav'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadExtensionResponseContactPronouncedNamePrompt(DataClassJsonMixin):
    id: Optional[str] = None
    content_uri: Optional[str] = None
    """ Link to a prompt resource """
    
    content_type: Optional[ReadExtensionResponseContactPronouncedNamePromptContentType] = None
    """ Content media type """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadExtensionResponseContactPronouncedName(DataClassJsonMixin):
    type: Optional[ReadExtensionResponseContactPronouncedNameType] = None
    """
    Voice name type. 'Default' - default extension name; first name and last name specified in user
    profile; 'TextToSpeech' - custom text; user name spelled the way it sounds and specified by
    user; 'Recorded' - custom audio, user name recorded in user's own voice (supported only for
    extension retrieval)
    """
    
    text: Optional[str] = None
    """ Custom text """
    
    prompt: Optional[ReadExtensionResponseContactPronouncedNamePrompt] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadExtensionResponseContact(DataClassJsonMixin):
    """ Contact detailed information """
    
    first_name: Optional[str] = None
    """ For User extension type only. Extension user first name """
    
    last_name: Optional[str] = None
    """ For User extension type only. Extension user last name """
    
    company: Optional[str] = None
    """ Extension user company name """
    
    job_title: Optional[str] = None
    email: Optional[str] = None
    """ Email of extension user """
    
    business_phone: Optional[str] = None
    """
    Extension user contact phone number in [E.164](https://www.itu.int/rec/T-REC-E.164-201011-I)
    (with '+' sign) format
    """
    
    mobile_phone: Optional[str] = None
    """
    Extension user mobile (**non** Toll Free) phone number in
    [E.164](https://www.itu.int/rec/T-REC-E.164-201011-I) (with '+' sign) format
    """
    
    business_address: Optional[ReadExtensionResponseContactBusinessAddress] = None
    """ Business address of extension user company """
    
    email_as_login_name: Optional[bool] = 'False'
    """
    If 'True' then contact email is enabled as login name for this user. Please note that email
    should be unique in this case.
    """
    
    pronounced_name: Optional[ReadExtensionResponseContactPronouncedName] = None
    department: Optional[str] = None
    """ Extension user department, if any """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadExtensionResponseCustomFieldsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a custom field """
    
    value: Optional[str] = None
    """ Custom field value """
    
    display_name: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadExtensionResponseDepartmentsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a department extension """
    
    uri: Optional[str] = None
    """ Canonical URI of a department extension """
    
    extension_number: Optional[str] = None
    """ Number of a department extension """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadExtensionResponsePermissionsAdmin(DataClassJsonMixin):
    """ Admin permission """
    
    enabled: Optional[bool] = None
    """ Specifies if a permission is enabled or not """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadExtensionResponsePermissionsInternationalCalling(DataClassJsonMixin):
    """ International Calling permission """
    
    enabled: Optional[bool] = None
    """ Specifies if a permission is enabled or not """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadExtensionResponsePermissions(DataClassJsonMixin):
    """
    Extension permissions, corresponding to the Service Web permissions 'Admin' and
    'InternationalCalling'
    
    Generated by Python OpenAPI Parser
    """
    
    admin: Optional[ReadExtensionResponsePermissionsAdmin] = None
    """ Admin permission """
    
    international_calling: Optional[ReadExtensionResponsePermissionsInternationalCalling] = None
    """ International Calling permission """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadExtensionResponseProfileImageScalesItem(DataClassJsonMixin):
    uri: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadExtensionResponseProfileImage(DataClassJsonMixin):
    """
    Information on profile image
    
    Required Properties:
     - uri
    
    Generated by Python OpenAPI Parser
    """
    
    uri: str
    """ Link to a profile image. If an image is not uploaded for an extension, only uri is returned """
    
    etag: Optional[str] = None
    """ Identifier of an image """
    
    last_modified: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """
    The datetime when an image was last updated in ISO 8601 format, for example
    2016-03-10T18:07:52.534Z
    """
    
    content_type: Optional[str] = None
    """ The type of an image """
    
    scales: Optional[List[ReadExtensionResponseProfileImageScalesItem]] = None
    """ List of URIs to profile images in different dimensions """
    

class ReadExtensionResponseReferencesItemType(Enum):
    """ Type of external identifier """
    
    PartnerId = 'PartnerId'
    CustomerDirectoryId = 'CustomerDirectoryId'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadExtensionResponseReferencesItem(DataClassJsonMixin):
    ref: Optional[str] = None
    """ Non-RC identifier of an extension """
    
    type: Optional[ReadExtensionResponseReferencesItemType] = None
    """ Type of external identifier """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadExtensionResponseRolesItem(DataClassJsonMixin):
    uri: Optional[str] = None
    id: Optional[str] = None
    """ Internal identifier of a role """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadExtensionResponseRegionalSettingsHomeCountry(DataClassJsonMixin):
    """ Extension country information """
    
    id: Optional[str] = None
    """ Internal identifier of a home country """
    
    uri: Optional[str] = None
    """ Canonical URI of a home country """
    
    name: Optional[str] = None
    """ Official name of a home country """
    
    iso_code: Optional[str] = None
    """ ISO code of a country """
    
    calling_code: Optional[str] = None
    """ Calling code of a country """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadExtensionResponseRegionalSettingsTimezone(DataClassJsonMixin):
    """ Extension timezone information """
    
    id: Optional[str] = None
    """ Internal identifier of a timezone """
    
    uri: Optional[str] = None
    """ Canonical URI of a timezone """
    
    name: Optional[str] = None
    """ Short name of a timezone """
    
    description: Optional[str] = None
    """ Meaningful description of the timezone """
    
    bias: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadExtensionResponseRegionalSettingsLanguage(DataClassJsonMixin):
    """ User interface language data """
    
    id: Optional[str] = None
    """ Internal identifier of a language """
    
    uri: Optional[str] = None
    """ Canonical URI of a language """
    
    greeting: Optional[bool] = None
    """ Indicates whether a language is available as greeting language """
    
    formatting_locale: Optional[bool] = None
    """ Indicates whether a language is available as formatting locale """
    
    locale_code: Optional[str] = None
    """ Localization code of a language """
    
    iso_code: Optional[str] = None
    """
    Country code according to the ISO standard, see [ISO
    3166](https://www.iso.org/iso-3166-country-codes.html)
    """
    
    name: Optional[str] = None
    """ Official name of a language """
    
    ui: Optional[bool] = None
    """ Indicates whether a language is available as UI language """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadExtensionResponseRegionalSettingsGreetingLanguage(DataClassJsonMixin):
    """ Information on language used for telephony greetings """
    
    id: Optional[str] = None
    """ Internal identifier of a greeting language """
    
    locale_code: Optional[str] = None
    """ Localization code of a greeting language """
    
    name: Optional[str] = None
    """ Official name of a greeting language """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadExtensionResponseRegionalSettingsFormattingLocale(DataClassJsonMixin):
    """ Formatting language preferences for numbers, dates and currencies """
    
    id: Optional[str] = None
    """ Internal identifier of a formatting language """
    
    locale_code: Optional[str] = None
    """ Localization code of a formatting language """
    
    name: Optional[str] = None

class ReadExtensionResponseRegionalSettingsTimeFormat(Enum):
    """ Time format setting. The default value is '12h' = ['12h', '24h'] """
    
    OBJECT_12h = '12h'
    OBJECT_24h = '24h'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadExtensionResponseRegionalSettings(DataClassJsonMixin):
    """ Extension region data (timezone, home country, language) """
    
    home_country: Optional[ReadExtensionResponseRegionalSettingsHomeCountry] = None
    """ Extension country information """
    
    timezone: Optional[ReadExtensionResponseRegionalSettingsTimezone] = None
    """ Extension timezone information """
    
    language: Optional[ReadExtensionResponseRegionalSettingsLanguage] = None
    """ User interface language data """
    
    greeting_language: Optional[ReadExtensionResponseRegionalSettingsGreetingLanguage] = None
    """ Information on language used for telephony greetings """
    
    formatting_locale: Optional[ReadExtensionResponseRegionalSettingsFormattingLocale] = None
    """ Formatting language preferences for numbers, dates and currencies """
    
    time_format: Optional[ReadExtensionResponseRegionalSettingsTimeFormat] = None
    """ Time format setting. The default value is '12h' = ['12h', '24h'] """
    

class ReadExtensionResponseServiceFeaturesItemFeatureName(Enum):
    """ Feature name """
    
    AccountFederation = 'AccountFederation'
    Archiver = 'Archiver'
    AutomaticCallRecordingMute = 'AutomaticCallRecordingMute'
    AutomaticInboundCallRecording = 'AutomaticInboundCallRecording'
    AutomaticOutboundCallRecording = 'AutomaticOutboundCallRecording'
    BlockedMessageForwarding = 'BlockedMessageForwarding'
    Calendar = 'Calendar'
    CallerIdControl = 'CallerIdControl'
    CallForwarding = 'CallForwarding'
    CallPark = 'CallPark'
    CallParkLocations = 'CallParkLocations'
    CallSupervision = 'CallSupervision'
    CallSwitch = 'CallSwitch'
    CallQualitySurvey = 'CallQualitySurvey'
    Conferencing = 'Conferencing'
    ConferencingNumber = 'ConferencingNumber'
    ConfigureDelegates = 'ConfigureDelegates'
    DeveloperPortal = 'DeveloperPortal'
    DND = 'DND'
    DynamicConference = 'DynamicConference'
    EmergencyAddressAutoUpdate = 'EmergencyAddressAutoUpdate'
    EmergencyCalling = 'EmergencyCalling'
    EncryptionAtRest = 'EncryptionAtRest'
    ExternalDirectoryIntegration = 'ExternalDirectoryIntegration'
    Fax = 'Fax'
    FaxReceiving = 'FaxReceiving'
    FreeSoftPhoneLines = 'FreeSoftPhoneLines'
    HDVoice = 'HDVoice'
    HipaaCompliance = 'HipaaCompliance'
    Intercom = 'Intercom'
    InternationalCalling = 'InternationalCalling'
    InternationalSMS = 'InternationalSMS'
    LinkedSoftphoneLines = 'LinkedSoftphoneLines'
    MMS = 'MMS'
    MobileVoipEmergencyCalling = 'MobileVoipEmergencyCalling'
    OnDemandCallRecording = 'OnDemandCallRecording'
    Pager = 'Pager'
    PagerReceiving = 'PagerReceiving'
    Paging = 'Paging'
    PasswordAuth = 'PasswordAuth'
    PromoMessage = 'PromoMessage'
    Reports = 'Reports'
    Presence = 'Presence'
    RCTeams = 'RCTeams'
    RingOut = 'RingOut'
    SalesForce = 'SalesForce'
    SharedLines = 'SharedLines'
    SingleExtensionUI = 'SingleExtensionUI'
    SiteCodes = 'SiteCodes'
    SMS = 'SMS'
    SMSReceiving = 'SMSReceiving'
    SoftPhoneUpdate = 'SoftPhoneUpdate'
    TelephonySessions = 'TelephonySessions'
    UserManagement = 'UserManagement'
    VideoConferencing = 'VideoConferencing'
    VoipCalling = 'VoipCalling'
    VoipCallingOnMobile = 'VoipCallingOnMobile'
    Voicemail = 'Voicemail'
    VoicemailToText = 'VoicemailToText'
    WebPhone = 'WebPhone'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadExtensionResponseServiceFeaturesItem(DataClassJsonMixin):
    enabled: Optional[bool] = None
    """ Feature status; shows feature availability for an extension """
    
    feature_name: Optional[ReadExtensionResponseServiceFeaturesItemFeatureName] = None
    """ Feature name """
    
    reason: Optional[str] = None
    """
    Reason for limitation of a particular service feature. Returned only if the enabled parameter
    value is 'False', see Service Feature Limitations and Reasons. When retrieving service features
    for an extension, the reasons for the limitations, if any, are returned in response
    """
    

class ReadExtensionResponseSetupWizardState(Enum):
    """ Specifies extension configuration wizard state (web service setup). """
    
    NotStarted = 'NotStarted'
    Incomplete = 'Incomplete'
    Completed = 'Completed'

class ReadExtensionResponseStatus(Enum):
    """
    Extension current state. If 'Unassigned' is specified, then extensions without
    ‘extensionNumber’ are returned. If not specified, then all extensions are returned
    
    Generated by Python OpenAPI Parser
    """
    
    Enabled = 'Enabled'
    Disabled = 'Disabled'
    Frozen = 'Frozen'
    NotActivated = 'NotActivated'
    Unassigned = 'Unassigned'

class ReadExtensionResponseStatusInfoReason(Enum):
    """ Type of suspension """
    
    Voluntarily = 'Voluntarily'
    Involuntarily = 'Involuntarily'
    SuspendedVoluntarily = 'SuspendedVoluntarily'
    SuspendedVoluntarily2 = 'SuspendedVoluntarily2'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadExtensionResponseStatusInfo(DataClassJsonMixin):
    """ Status information (reason, comment). Returned for 'Disabled' status only """
    
    comment: Optional[str] = None
    """ A free-form user comment, describing the status change reason """
    
    reason: Optional[ReadExtensionResponseStatusInfoReason] = None
    """ Type of suspension """
    

class ReadExtensionResponseType(Enum):
    """ Extension type """
    
    User = 'User'
    FaxUser = 'FaxUser'
    VirtualUser = 'VirtualUser'
    DigitalUser = 'DigitalUser'
    Department = 'Department'
    Announcement = 'Announcement'
    Voicemail = 'Voicemail'
    SharedLinesGroup = 'SharedLinesGroup'
    PagingOnly = 'PagingOnly'
    IvrMenu = 'IvrMenu'
    ApplicationExtension = 'ApplicationExtension'
    ParkLocation = 'ParkLocation'
    Bot = 'Bot'
    Room = 'Room'
    Limited = 'Limited'
    Site = 'Site'
    ProxyAdmin = 'ProxyAdmin'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadExtensionResponseCallQueueInfo(DataClassJsonMixin):
    """ For Department extension type only. Call queue settings """
    
    sla_goal: Optional[int] = None
    """
    Target percentage of calls that must be answered by agents within the service level time
    threshold
    """
    
    sla_threshold_seconds: Optional[int] = None
    """ Period of time in seconds that is considered to be an acceptable service level """
    
    include_abandoned_calls: Optional[bool] = None
    """
    If 'True' abandoned calls (hanged up prior to being served) are included into service level
    calculation
    """
    
    abandoned_threshold_seconds: Optional[int] = None
    """
    Period of time in seconds specifying abandoned calls duration - calls that are shorter will not
    be included into the calculation of service level.; zero value means that abandoned calls of
    any duration will be included into calculation
    """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadExtensionResponseSite(DataClassJsonMixin):
    """
    Site data. If multi-site feature is turned on for the account, then internal identifier of a
    site must be specified. To assign the wireless point to the main site (company) set site ID to
    `main-site`
    
    Generated by Python OpenAPI Parser
    """
    
    id: Optional[str] = None
    """ Internal identifier of a site """
    
    uri: Optional[str] = None
    """ Link to a site resource """
    
    name: Optional[str] = None
    """ Name of a site """
    
    code: Optional[str] = None
    """ Site code value. Returned only if specified """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadExtensionResponse(DataClassJsonMixin):
    id: Optional[int] = None
    """ Internal identifier of an extension """
    
    uri: Optional[str] = None
    """ Canonical URI of an extension """
    
    account: Optional[ReadExtensionResponseAccount] = None
    """ Account information """
    
    contact: Optional[ReadExtensionResponseContact] = None
    """ Contact detailed information """
    
    custom_fields: Optional[List[ReadExtensionResponseCustomFieldsItem]] = None
    departments: Optional[List[ReadExtensionResponseDepartmentsItem]] = None
    """
    Information on department extension(s), to which the requested extension belongs. Returned only
    for user extensions, members of department, requested by single extensionId
    """
    
    extension_number: Optional[str] = None
    """ Number of department extension """
    
    extension_numbers: Optional[List[str]] = None
    name: Optional[str] = None
    """
    Extension name. For user extension types the value is a combination of the specified first name
    and last name
    """
    
    partner_id: Optional[str] = None
    """
    For Partner Applications Internal identifier of an extension created by partner. The
    RingCentral supports the mapping of accounts and stores the corresponding account ID/extension
    ID for each partner ID of a client application. In request URIs partner IDs are accepted
    instead of regular RingCentral native IDs as path parameters using pid = XXX clause. Though in
    response URIs contain the corresponding account IDs and extension IDs. In all request and
    response bodies these values are reflected via partnerId attributes of account and extension
    """
    
    permissions: Optional[ReadExtensionResponsePermissions] = None
    """
    Extension permissions, corresponding to the Service Web permissions 'Admin' and
    'InternationalCalling'
    """
    
    profile_image: Optional[ReadExtensionResponseProfileImage] = None
    """ Information on profile image """
    
    references: Optional[List[ReadExtensionResponseReferencesItem]] = None
    """ List of non-RC internal identifiers assigned to an extension """
    
    roles: Optional[List[ReadExtensionResponseRolesItem]] = None
    regional_settings: Optional[ReadExtensionResponseRegionalSettings] = None
    """ Extension region data (timezone, home country, language) """
    
    service_features: Optional[List[ReadExtensionResponseServiceFeaturesItem]] = None
    """
    Extension service features returned in response only when the logged-in user requests his/her
    own extension info, see also Extension Service Features
    """
    
    setup_wizard_state: Optional[ReadExtensionResponseSetupWizardState] = 'NotStarted'
    """ Specifies extension configuration wizard state (web service setup). """
    
    status: Optional[ReadExtensionResponseStatus] = None
    """
    Extension current state. If 'Unassigned' is specified, then extensions without
    ‘extensionNumber’ are returned. If not specified, then all extensions are returned
    """
    
    status_info: Optional[ReadExtensionResponseStatusInfo] = None
    """ Status information (reason, comment). Returned for 'Disabled' status only """
    
    type: Optional[ReadExtensionResponseType] = None
    """ Extension type """
    
    call_queue_info: Optional[ReadExtensionResponseCallQueueInfo] = None
    """ For Department extension type only. Call queue settings """
    
    hidden: Optional[bool] = None
    """ Hides extension from showing in company directory. Supported for extensions of User type only """
    
    site: Optional[ReadExtensionResponseSite] = None
    """
    Site data. If multi-site feature is turned on for the account, then internal identifier of a
    site must be specified. To assign the wireless point to the main site (company) set site ID to
    `main-site`
    """
    

class UpdateExtensionRequestStatus(Enum):
    Disabled = 'Disabled'
    Enabled = 'Enabled'
    NotActivated = 'NotActivated'
    Frozen = 'Frozen'

class UpdateExtensionRequestStatusInfoReason(Enum):
    """ Type of suspension """
    
    Voluntarily = 'Voluntarily'
    Involuntarily = 'Involuntarily'
    SuspendedVoluntarily = 'SuspendedVoluntarily'
    SuspendedVoluntarily2 = 'SuspendedVoluntarily2'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateExtensionRequestStatusInfo(DataClassJsonMixin):
    comment: Optional[str] = None
    """ A free-form user comment, describing the status change reason """
    
    reason: Optional[UpdateExtensionRequestStatusInfoReason] = None
    """ Type of suspension """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateExtensionRequestContactBusinessAddress(DataClassJsonMixin):
    country: Optional[str] = None
    """ Country name of an extension user company """
    
    state: Optional[str] = None
    """ State/province name of an extension user company. Mandatory for the USA, UK and Canada """
    
    city: Optional[str] = None
    """ City name of an extension user company """
    
    street: Optional[str] = None
    """ Street address of an extension user company """
    
    zip: Optional[str] = None
    """ Zip code of an extension user company """
    

class UpdateExtensionRequestContactPronouncedNameType(Enum):
    """
    Voice name type. 'Default' - default extension name; first name and last name specified in user
    profile; 'TextToSpeech' - custom text; user name spelled the way it sounds and specified by
    user; 'Recorded' - custom audio, user name recorded in user's own voice (supported only for
    extension retrieval)
    
    Generated by Python OpenAPI Parser
    """
    
    Default = 'Default'
    TextToSpeech = 'TextToSpeech'
    Recorded = 'Recorded'

class UpdateExtensionRequestContactPronouncedNamePromptContentType(Enum):
    """ Content media type """
    
    AudioMpeg = 'audio/mpeg'
    AudioWav = 'audio/wav'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateExtensionRequestContactPronouncedNamePrompt(DataClassJsonMixin):
    id: Optional[str] = None
    content_uri: Optional[str] = None
    """ Link to a prompt resource """
    
    content_type: Optional[UpdateExtensionRequestContactPronouncedNamePromptContentType] = None
    """ Content media type """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateExtensionRequestContactPronouncedName(DataClassJsonMixin):
    type: Optional[UpdateExtensionRequestContactPronouncedNameType] = None
    """
    Voice name type. 'Default' - default extension name; first name and last name specified in user
    profile; 'TextToSpeech' - custom text; user name spelled the way it sounds and specified by
    user; 'Recorded' - custom audio, user name recorded in user's own voice (supported only for
    extension retrieval)
    """
    
    text: Optional[str] = None
    """ Custom text """
    
    prompt: Optional[UpdateExtensionRequestContactPronouncedNamePrompt] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateExtensionRequestContact(DataClassJsonMixin):
    first_name: Optional[str] = None
    """ For User extension type only. Extension user first name """
    
    last_name: Optional[str] = None
    """ For User extension type only. Extension user last name """
    
    company: Optional[str] = None
    """ Extension user company name """
    
    job_title: Optional[str] = None
    email: Optional[str] = None
    """ Email of extension user """
    
    business_phone: Optional[str] = None
    """
    Extension user contact phone number in [E.164](https://www.itu.int/rec/T-REC-E.164-201011-I)
    format
    """
    
    mobile_phone: Optional[str] = None
    """
    Extension user mobile (**non** Toll Free) phone number in
    [E.164](https://www.itu.int/rec/T-REC-E.164-201011-I) (with '+' sign) format
    """
    
    business_address: Optional[UpdateExtensionRequestContactBusinessAddress] = None
    email_as_login_name: Optional[bool] = None
    """
    If 'True' then contact email is enabled as login name for this user. Please note that email
    should be unique in this case. The default value is 'False'
    """
    
    pronounced_name: Optional[UpdateExtensionRequestContactPronouncedName] = None
    department: Optional[str] = None
    """ Extension user department, if any """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateExtensionRequestRegionalSettingsHomeCountry(DataClassJsonMixin):
    id: Optional[str] = None
    """ internal Identifier of a country """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateExtensionRequestRegionalSettingsTimezone(DataClassJsonMixin):
    id: Optional[str] = None
    """ internal Identifier of a timezone """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateExtensionRequestRegionalSettingsLanguage(DataClassJsonMixin):
    id: Optional[str] = None
    """ internal Identifier of a language """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateExtensionRequestRegionalSettingsGreetingLanguage(DataClassJsonMixin):
    id: Optional[str] = None
    """ internal Identifier of a greeting language """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateExtensionRequestRegionalSettingsFormattingLocale(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal Identifier of a formatting language """
    

class UpdateExtensionRequestRegionalSettingsTimeFormat(Enum):
    """ Time format setting """
    
    OBJECT_12h = '12h'
    OBJECT_24h = '24h'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateExtensionRequestRegionalSettings(DataClassJsonMixin):
    home_country: Optional[UpdateExtensionRequestRegionalSettingsHomeCountry] = None
    timezone: Optional[UpdateExtensionRequestRegionalSettingsTimezone] = None
    language: Optional[UpdateExtensionRequestRegionalSettingsLanguage] = None
    greeting_language: Optional[UpdateExtensionRequestRegionalSettingsGreetingLanguage] = None
    formatting_locale: Optional[UpdateExtensionRequestRegionalSettingsFormattingLocale] = None
    time_format: Optional[UpdateExtensionRequestRegionalSettingsTimeFormat] = '12h'
    """ Time format setting """
    

class UpdateExtensionRequestSetupWizardState(Enum):
    NotStarted = 'NotStarted'
    Incomplete = 'Incomplete'
    Completed = 'Completed'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateExtensionRequestCallQueueInfo(DataClassJsonMixin):
    """ For Department extension type only. Call queue settings """
    
    sla_goal: Optional[int] = None
    """
    Target percentage of calls that must be answered by agents within the service level time
    threshold
    """
    
    sla_threshold_seconds: Optional[int] = None
    include_abandoned_calls: Optional[bool] = None
    abandoned_threshold_seconds: Optional[int] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateExtensionRequestTransitionItem(DataClassJsonMixin):
    """ For NotActivated extensions only. Welcome email settings """
    
    send_welcome_emails_to_users: Optional[bool] = None
    """
    Specifies if an activation email is automatically sent to new users (Not Activated extensions)
    or not
    """
    
    send_welcome_email: Optional[bool] = None
    """ Supported for account confirmation. Specifies whether welcome email is sent """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateExtensionRequestCustomFieldsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a custom field """
    
    value: Optional[str] = None
    """ Custom field value """
    
    display_name: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateExtensionRequestSite(DataClassJsonMixin):
    """
    Site data. If multi-site feature is turned on for the account, then internal identifier of a
    site must be specified. To assign the wireless point to the main site (company) set site ID to
    `main-site`
    
    Generated by Python OpenAPI Parser
    """
    
    id: Optional[str] = None
    """ Internal identifier of a site """
    
    uri: Optional[str] = None
    """ Link to a site resource """
    
    name: Optional[str] = None
    """ Name of a site """
    
    code: Optional[str] = None
    """ Site code value. Returned only if specified """
    

class UpdateExtensionRequestType(Enum):
    """ Extension type """
    
    User = 'User'
    Fax_User = 'Fax User'
    VirtualUser = 'VirtualUser'
    DigitalUser = 'DigitalUser'
    Department = 'Department'
    Announcement = 'Announcement'
    Voicemail = 'Voicemail'
    SharedLinesGroup = 'SharedLinesGroup'
    PagingOnly = 'PagingOnly'
    IvrMenu = 'IvrMenu'
    ApplicationExtension = 'ApplicationExtension'
    ParkLocation = 'ParkLocation'

class UpdateExtensionRequestReferencesItemType(Enum):
    """ Type of external identifier """
    
    PartnerId = 'PartnerId'
    CustomerDirectoryId = 'CustomerDirectoryId'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateExtensionRequestReferencesItem(DataClassJsonMixin):
    ref: Optional[str] = None
    """ Non-RC identifier of an extension """
    
    type: Optional[UpdateExtensionRequestReferencesItemType] = None
    """ Type of external identifier """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateExtensionRequest(DataClassJsonMixin):
    status: Optional[UpdateExtensionRequestStatus] = None
    status_info: Optional[UpdateExtensionRequestStatusInfo] = None
    reason: Optional[str] = None
    """ Type of suspension """
    
    comment: Optional[str] = None
    """ Free Form user comment """
    
    extension_number: Optional[str] = None
    """ Extension number available """
    
    contact: Optional[UpdateExtensionRequestContact] = None
    regional_settings: Optional[UpdateExtensionRequestRegionalSettings] = None
    setup_wizard_state: Optional[UpdateExtensionRequestSetupWizardState] = None
    partner_id: Optional[str] = None
    """ Additional extension identifier, created by partner application and applied on client side """
    
    ivr_pin: Optional[str] = None
    """ IVR PIN """
    
    password: Optional[str] = None
    """ Password for extension """
    
    call_queue_info: Optional[UpdateExtensionRequestCallQueueInfo] = None
    """ For Department extension type only. Call queue settings """
    
    transition: Optional[List[UpdateExtensionRequestTransitionItem]] = None
    custom_fields: Optional[List[UpdateExtensionRequestCustomFieldsItem]] = None
    hidden: Optional[bool] = None
    """ Hides extension from showing in company directory. Supported for extensions of User type only """
    
    site: Optional[UpdateExtensionRequestSite] = None
    """
    Site data. If multi-site feature is turned on for the account, then internal identifier of a
    site must be specified. To assign the wireless point to the main site (company) set site ID to
    `main-site`
    """
    
    type: Optional[UpdateExtensionRequestType] = None
    """ Extension type """
    
    references: Optional[List[UpdateExtensionRequestReferencesItem]] = None
    """ List of non-RC internal identifiers assigned to an extension """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateExtensionResponseAccount(DataClassJsonMixin):
    """ Account information """
    
    id: Optional[str] = None
    """ Internal identifier of an account """
    
    uri: Optional[str] = None
    """ Canonical URI of an account """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateExtensionResponseContactBusinessAddress(DataClassJsonMixin):
    """ Business address of extension user company """
    
    country: Optional[str] = None
    """ Country name of an extension user company """
    
    state: Optional[str] = None
    """ State/province name of an extension user company. Mandatory for the USA, UK and Canada """
    
    city: Optional[str] = None
    """ City name of an extension user company """
    
    street: Optional[str] = None
    """ Street address of an extension user company """
    
    zip: Optional[str] = None
    """ Zip code of an extension user company """
    

class UpdateExtensionResponseContactPronouncedNameType(Enum):
    """
    Voice name type. 'Default' - default extension name; first name and last name specified in user
    profile; 'TextToSpeech' - custom text; user name spelled the way it sounds and specified by
    user; 'Recorded' - custom audio, user name recorded in user's own voice (supported only for
    extension retrieval)
    
    Generated by Python OpenAPI Parser
    """
    
    Default = 'Default'
    TextToSpeech = 'TextToSpeech'
    Recorded = 'Recorded'

class UpdateExtensionResponseContactPronouncedNamePromptContentType(Enum):
    """ Content media type """
    
    AudioMpeg = 'audio/mpeg'
    AudioWav = 'audio/wav'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateExtensionResponseContactPronouncedNamePrompt(DataClassJsonMixin):
    id: Optional[str] = None
    content_uri: Optional[str] = None
    """ Link to a prompt resource """
    
    content_type: Optional[UpdateExtensionResponseContactPronouncedNamePromptContentType] = None
    """ Content media type """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateExtensionResponseContactPronouncedName(DataClassJsonMixin):
    type: Optional[UpdateExtensionResponseContactPronouncedNameType] = None
    """
    Voice name type. 'Default' - default extension name; first name and last name specified in user
    profile; 'TextToSpeech' - custom text; user name spelled the way it sounds and specified by
    user; 'Recorded' - custom audio, user name recorded in user's own voice (supported only for
    extension retrieval)
    """
    
    text: Optional[str] = None
    """ Custom text """
    
    prompt: Optional[UpdateExtensionResponseContactPronouncedNamePrompt] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateExtensionResponseContact(DataClassJsonMixin):
    """ Contact detailed information """
    
    first_name: Optional[str] = None
    """ For User extension type only. Extension user first name """
    
    last_name: Optional[str] = None
    """ For User extension type only. Extension user last name """
    
    company: Optional[str] = None
    """ Extension user company name """
    
    job_title: Optional[str] = None
    email: Optional[str] = None
    """ Email of extension user """
    
    business_phone: Optional[str] = None
    """
    Extension user contact phone number in [E.164](https://www.itu.int/rec/T-REC-E.164-201011-I)
    (with '+' sign) format
    """
    
    mobile_phone: Optional[str] = None
    """
    Extension user mobile (**non** Toll Free) phone number in
    [E.164](https://www.itu.int/rec/T-REC-E.164-201011-I) (with '+' sign) format
    """
    
    business_address: Optional[UpdateExtensionResponseContactBusinessAddress] = None
    """ Business address of extension user company """
    
    email_as_login_name: Optional[bool] = 'False'
    """
    If 'True' then contact email is enabled as login name for this user. Please note that email
    should be unique in this case.
    """
    
    pronounced_name: Optional[UpdateExtensionResponseContactPronouncedName] = None
    department: Optional[str] = None
    """ Extension user department, if any """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateExtensionResponseCustomFieldsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a custom field """
    
    value: Optional[str] = None
    """ Custom field value """
    
    display_name: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateExtensionResponseDepartmentsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a department extension """
    
    uri: Optional[str] = None
    """ Canonical URI of a department extension """
    
    extension_number: Optional[str] = None
    """ Number of a department extension """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateExtensionResponsePermissionsAdmin(DataClassJsonMixin):
    """ Admin permission """
    
    enabled: Optional[bool] = None
    """ Specifies if a permission is enabled or not """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateExtensionResponsePermissionsInternationalCalling(DataClassJsonMixin):
    """ International Calling permission """
    
    enabled: Optional[bool] = None
    """ Specifies if a permission is enabled or not """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateExtensionResponsePermissions(DataClassJsonMixin):
    """
    Extension permissions, corresponding to the Service Web permissions 'Admin' and
    'InternationalCalling'
    
    Generated by Python OpenAPI Parser
    """
    
    admin: Optional[UpdateExtensionResponsePermissionsAdmin] = None
    """ Admin permission """
    
    international_calling: Optional[UpdateExtensionResponsePermissionsInternationalCalling] = None
    """ International Calling permission """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateExtensionResponseProfileImageScalesItem(DataClassJsonMixin):
    uri: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateExtensionResponseProfileImage(DataClassJsonMixin):
    """
    Information on profile image
    
    Required Properties:
     - uri
    
    Generated by Python OpenAPI Parser
    """
    
    uri: str
    """ Link to a profile image. If an image is not uploaded for an extension, only uri is returned """
    
    etag: Optional[str] = None
    """ Identifier of an image """
    
    last_modified: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """
    The datetime when an image was last updated in ISO 8601 format, for example
    2016-03-10T18:07:52.534Z
    """
    
    content_type: Optional[str] = None
    """ The type of an image """
    
    scales: Optional[List[UpdateExtensionResponseProfileImageScalesItem]] = None
    """ List of URIs to profile images in different dimensions """
    

class UpdateExtensionResponseReferencesItemType(Enum):
    """ Type of external identifier """
    
    PartnerId = 'PartnerId'
    CustomerDirectoryId = 'CustomerDirectoryId'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateExtensionResponseReferencesItem(DataClassJsonMixin):
    ref: Optional[str] = None
    """ Non-RC identifier of an extension """
    
    type: Optional[UpdateExtensionResponseReferencesItemType] = None
    """ Type of external identifier """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateExtensionResponseRolesItem(DataClassJsonMixin):
    uri: Optional[str] = None
    id: Optional[str] = None
    """ Internal identifier of a role """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateExtensionResponseRegionalSettingsHomeCountry(DataClassJsonMixin):
    """ Extension country information """
    
    id: Optional[str] = None
    """ Internal identifier of a home country """
    
    uri: Optional[str] = None
    """ Canonical URI of a home country """
    
    name: Optional[str] = None
    """ Official name of a home country """
    
    iso_code: Optional[str] = None
    """ ISO code of a country """
    
    calling_code: Optional[str] = None
    """ Calling code of a country """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateExtensionResponseRegionalSettingsTimezone(DataClassJsonMixin):
    """ Extension timezone information """
    
    id: Optional[str] = None
    """ Internal identifier of a timezone """
    
    uri: Optional[str] = None
    """ Canonical URI of a timezone """
    
    name: Optional[str] = None
    """ Short name of a timezone """
    
    description: Optional[str] = None
    """ Meaningful description of the timezone """
    
    bias: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateExtensionResponseRegionalSettingsLanguage(DataClassJsonMixin):
    """ User interface language data """
    
    id: Optional[str] = None
    """ Internal identifier of a language """
    
    uri: Optional[str] = None
    """ Canonical URI of a language """
    
    greeting: Optional[bool] = None
    """ Indicates whether a language is available as greeting language """
    
    formatting_locale: Optional[bool] = None
    """ Indicates whether a language is available as formatting locale """
    
    locale_code: Optional[str] = None
    """ Localization code of a language """
    
    iso_code: Optional[str] = None
    """
    Country code according to the ISO standard, see [ISO
    3166](https://www.iso.org/iso-3166-country-codes.html)
    """
    
    name: Optional[str] = None
    """ Official name of a language """
    
    ui: Optional[bool] = None
    """ Indicates whether a language is available as UI language """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateExtensionResponseRegionalSettingsGreetingLanguage(DataClassJsonMixin):
    """ Information on language used for telephony greetings """
    
    id: Optional[str] = None
    """ Internal identifier of a greeting language """
    
    locale_code: Optional[str] = None
    """ Localization code of a greeting language """
    
    name: Optional[str] = None
    """ Official name of a greeting language """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateExtensionResponseRegionalSettingsFormattingLocale(DataClassJsonMixin):
    """ Formatting language preferences for numbers, dates and currencies """
    
    id: Optional[str] = None
    """ Internal identifier of a formatting language """
    
    locale_code: Optional[str] = None
    """ Localization code of a formatting language """
    
    name: Optional[str] = None

class UpdateExtensionResponseRegionalSettingsTimeFormat(Enum):
    """ Time format setting. The default value is '12h' = ['12h', '24h'] """
    
    OBJECT_12h = '12h'
    OBJECT_24h = '24h'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateExtensionResponseRegionalSettings(DataClassJsonMixin):
    """ Extension region data (timezone, home country, language) """
    
    home_country: Optional[UpdateExtensionResponseRegionalSettingsHomeCountry] = None
    """ Extension country information """
    
    timezone: Optional[UpdateExtensionResponseRegionalSettingsTimezone] = None
    """ Extension timezone information """
    
    language: Optional[UpdateExtensionResponseRegionalSettingsLanguage] = None
    """ User interface language data """
    
    greeting_language: Optional[UpdateExtensionResponseRegionalSettingsGreetingLanguage] = None
    """ Information on language used for telephony greetings """
    
    formatting_locale: Optional[UpdateExtensionResponseRegionalSettingsFormattingLocale] = None
    """ Formatting language preferences for numbers, dates and currencies """
    
    time_format: Optional[UpdateExtensionResponseRegionalSettingsTimeFormat] = None
    """ Time format setting. The default value is '12h' = ['12h', '24h'] """
    

class UpdateExtensionResponseServiceFeaturesItemFeatureName(Enum):
    """ Feature name """
    
    AccountFederation = 'AccountFederation'
    Archiver = 'Archiver'
    AutomaticCallRecordingMute = 'AutomaticCallRecordingMute'
    AutomaticInboundCallRecording = 'AutomaticInboundCallRecording'
    AutomaticOutboundCallRecording = 'AutomaticOutboundCallRecording'
    BlockedMessageForwarding = 'BlockedMessageForwarding'
    Calendar = 'Calendar'
    CallerIdControl = 'CallerIdControl'
    CallForwarding = 'CallForwarding'
    CallPark = 'CallPark'
    CallParkLocations = 'CallParkLocations'
    CallSupervision = 'CallSupervision'
    CallSwitch = 'CallSwitch'
    CallQualitySurvey = 'CallQualitySurvey'
    Conferencing = 'Conferencing'
    ConferencingNumber = 'ConferencingNumber'
    ConfigureDelegates = 'ConfigureDelegates'
    DeveloperPortal = 'DeveloperPortal'
    DND = 'DND'
    DynamicConference = 'DynamicConference'
    EmergencyAddressAutoUpdate = 'EmergencyAddressAutoUpdate'
    EmergencyCalling = 'EmergencyCalling'
    EncryptionAtRest = 'EncryptionAtRest'
    ExternalDirectoryIntegration = 'ExternalDirectoryIntegration'
    Fax = 'Fax'
    FaxReceiving = 'FaxReceiving'
    FreeSoftPhoneLines = 'FreeSoftPhoneLines'
    HDVoice = 'HDVoice'
    HipaaCompliance = 'HipaaCompliance'
    Intercom = 'Intercom'
    InternationalCalling = 'InternationalCalling'
    InternationalSMS = 'InternationalSMS'
    LinkedSoftphoneLines = 'LinkedSoftphoneLines'
    MMS = 'MMS'
    MobileVoipEmergencyCalling = 'MobileVoipEmergencyCalling'
    OnDemandCallRecording = 'OnDemandCallRecording'
    Pager = 'Pager'
    PagerReceiving = 'PagerReceiving'
    Paging = 'Paging'
    PasswordAuth = 'PasswordAuth'
    PromoMessage = 'PromoMessage'
    Reports = 'Reports'
    Presence = 'Presence'
    RCTeams = 'RCTeams'
    RingOut = 'RingOut'
    SalesForce = 'SalesForce'
    SharedLines = 'SharedLines'
    SingleExtensionUI = 'SingleExtensionUI'
    SiteCodes = 'SiteCodes'
    SMS = 'SMS'
    SMSReceiving = 'SMSReceiving'
    SoftPhoneUpdate = 'SoftPhoneUpdate'
    TelephonySessions = 'TelephonySessions'
    UserManagement = 'UserManagement'
    VideoConferencing = 'VideoConferencing'
    VoipCalling = 'VoipCalling'
    VoipCallingOnMobile = 'VoipCallingOnMobile'
    Voicemail = 'Voicemail'
    VoicemailToText = 'VoicemailToText'
    WebPhone = 'WebPhone'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateExtensionResponseServiceFeaturesItem(DataClassJsonMixin):
    enabled: Optional[bool] = None
    """ Feature status; shows feature availability for an extension """
    
    feature_name: Optional[UpdateExtensionResponseServiceFeaturesItemFeatureName] = None
    """ Feature name """
    
    reason: Optional[str] = None
    """
    Reason for limitation of a particular service feature. Returned only if the enabled parameter
    value is 'False', see Service Feature Limitations and Reasons. When retrieving service features
    for an extension, the reasons for the limitations, if any, are returned in response
    """
    

class UpdateExtensionResponseSetupWizardState(Enum):
    """ Specifies extension configuration wizard state (web service setup). """
    
    NotStarted = 'NotStarted'
    Incomplete = 'Incomplete'
    Completed = 'Completed'

class UpdateExtensionResponseStatus(Enum):
    """
    Extension current state. If 'Unassigned' is specified, then extensions without
    ‘extensionNumber’ are returned. If not specified, then all extensions are returned
    
    Generated by Python OpenAPI Parser
    """
    
    Enabled = 'Enabled'
    Disabled = 'Disabled'
    Frozen = 'Frozen'
    NotActivated = 'NotActivated'
    Unassigned = 'Unassigned'

class UpdateExtensionResponseStatusInfoReason(Enum):
    """ Type of suspension """
    
    Voluntarily = 'Voluntarily'
    Involuntarily = 'Involuntarily'
    SuspendedVoluntarily = 'SuspendedVoluntarily'
    SuspendedVoluntarily2 = 'SuspendedVoluntarily2'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateExtensionResponseStatusInfo(DataClassJsonMixin):
    """ Status information (reason, comment). Returned for 'Disabled' status only """
    
    comment: Optional[str] = None
    """ A free-form user comment, describing the status change reason """
    
    reason: Optional[UpdateExtensionResponseStatusInfoReason] = None
    """ Type of suspension """
    

class UpdateExtensionResponseType(Enum):
    """ Extension type """
    
    User = 'User'
    FaxUser = 'FaxUser'
    VirtualUser = 'VirtualUser'
    DigitalUser = 'DigitalUser'
    Department = 'Department'
    Announcement = 'Announcement'
    Voicemail = 'Voicemail'
    SharedLinesGroup = 'SharedLinesGroup'
    PagingOnly = 'PagingOnly'
    IvrMenu = 'IvrMenu'
    ApplicationExtension = 'ApplicationExtension'
    ParkLocation = 'ParkLocation'
    Bot = 'Bot'
    Room = 'Room'
    Limited = 'Limited'
    Site = 'Site'
    ProxyAdmin = 'ProxyAdmin'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateExtensionResponseCallQueueInfo(DataClassJsonMixin):
    """ For Department extension type only. Call queue settings """
    
    sla_goal: Optional[int] = None
    """
    Target percentage of calls that must be answered by agents within the service level time
    threshold
    """
    
    sla_threshold_seconds: Optional[int] = None
    """ Period of time in seconds that is considered to be an acceptable service level """
    
    include_abandoned_calls: Optional[bool] = None
    """
    If 'True' abandoned calls (hanged up prior to being served) are included into service level
    calculation
    """
    
    abandoned_threshold_seconds: Optional[int] = None
    """
    Period of time in seconds specifying abandoned calls duration - calls that are shorter will not
    be included into the calculation of service level.; zero value means that abandoned calls of
    any duration will be included into calculation
    """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateExtensionResponseSite(DataClassJsonMixin):
    """
    Site data. If multi-site feature is turned on for the account, then internal identifier of a
    site must be specified. To assign the wireless point to the main site (company) set site ID to
    `main-site`
    
    Generated by Python OpenAPI Parser
    """
    
    id: Optional[str] = None
    """ Internal identifier of a site """
    
    uri: Optional[str] = None
    """ Link to a site resource """
    
    name: Optional[str] = None
    """ Name of a site """
    
    code: Optional[str] = None
    """ Site code value. Returned only if specified """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateExtensionResponse(DataClassJsonMixin):
    id: Optional[int] = None
    """ Internal identifier of an extension """
    
    uri: Optional[str] = None
    """ Canonical URI of an extension """
    
    account: Optional[UpdateExtensionResponseAccount] = None
    """ Account information """
    
    contact: Optional[UpdateExtensionResponseContact] = None
    """ Contact detailed information """
    
    custom_fields: Optional[List[UpdateExtensionResponseCustomFieldsItem]] = None
    departments: Optional[List[UpdateExtensionResponseDepartmentsItem]] = None
    """
    Information on department extension(s), to which the requested extension belongs. Returned only
    for user extensions, members of department, requested by single extensionId
    """
    
    extension_number: Optional[str] = None
    """ Number of department extension """
    
    extension_numbers: Optional[List[str]] = None
    name: Optional[str] = None
    """
    Extension name. For user extension types the value is a combination of the specified first name
    and last name
    """
    
    partner_id: Optional[str] = None
    """
    For Partner Applications Internal identifier of an extension created by partner. The
    RingCentral supports the mapping of accounts and stores the corresponding account ID/extension
    ID for each partner ID of a client application. In request URIs partner IDs are accepted
    instead of regular RingCentral native IDs as path parameters using pid = XXX clause. Though in
    response URIs contain the corresponding account IDs and extension IDs. In all request and
    response bodies these values are reflected via partnerId attributes of account and extension
    """
    
    permissions: Optional[UpdateExtensionResponsePermissions] = None
    """
    Extension permissions, corresponding to the Service Web permissions 'Admin' and
    'InternationalCalling'
    """
    
    profile_image: Optional[UpdateExtensionResponseProfileImage] = None
    """ Information on profile image """
    
    references: Optional[List[UpdateExtensionResponseReferencesItem]] = None
    """ List of non-RC internal identifiers assigned to an extension """
    
    roles: Optional[List[UpdateExtensionResponseRolesItem]] = None
    regional_settings: Optional[UpdateExtensionResponseRegionalSettings] = None
    """ Extension region data (timezone, home country, language) """
    
    service_features: Optional[List[UpdateExtensionResponseServiceFeaturesItem]] = None
    """
    Extension service features returned in response only when the logged-in user requests his/her
    own extension info, see also Extension Service Features
    """
    
    setup_wizard_state: Optional[UpdateExtensionResponseSetupWizardState] = 'NotStarted'
    """ Specifies extension configuration wizard state (web service setup). """
    
    status: Optional[UpdateExtensionResponseStatus] = None
    """
    Extension current state. If 'Unassigned' is specified, then extensions without
    ‘extensionNumber’ are returned. If not specified, then all extensions are returned
    """
    
    status_info: Optional[UpdateExtensionResponseStatusInfo] = None
    """ Status information (reason, comment). Returned for 'Disabled' status only """
    
    type: Optional[UpdateExtensionResponseType] = None
    """ Extension type """
    
    call_queue_info: Optional[UpdateExtensionResponseCallQueueInfo] = None
    """ For Department extension type only. Call queue settings """
    
    hidden: Optional[bool] = None
    """ Hides extension from showing in company directory. Supported for extensions of User type only """
    
    site: Optional[UpdateExtensionResponseSite] = None
    """
    Site data. If multi-site feature is turned on for the account, then internal identifier of a
    site must be specified. To assign the wireless point to the main site (company) set site ID to
    `main-site`
    """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadExtensionCallerIdResponseByDeviceItemDevice(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a device """
    
    uri: Optional[str] = None
    """ Link to a device resource """
    
    name: Optional[str] = None
    """ Name of a device """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadExtensionCallerIdResponseByDeviceItemCallerIdPhoneInfo(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a phone number """
    
    uri: Optional[str] = None
    """ Link to a phone number resource """
    
    phone_number: Optional[str] = None
    """ Phone number in [E.164](https://www.itu.int/rec/T-REC-E.164-201011-I) (with '+' sign) format """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadExtensionCallerIdResponseByDeviceItemCallerId(DataClassJsonMixin):
    type: Optional[str] = None
    """
    If 'PhoneNumber' value is specified, then a certain phone number is shown as a caller ID when
    using this telephony feature. If 'Blocked' value is specified, then a caller ID is hidden. The
    value 'CurrentLocation' can be specified for 'RingOut' feature only. The default is
    'PhoneNumber' = ['PhoneNumber', 'Blocked', 'CurrentLocation']
    """
    
    phone_info: Optional[ReadExtensionCallerIdResponseByDeviceItemCallerIdPhoneInfo] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadExtensionCallerIdResponseByDeviceItem(DataClassJsonMixin):
    """ Caller ID settings by device """
    
    device: Optional[ReadExtensionCallerIdResponseByDeviceItemDevice] = None
    caller_id: Optional[ReadExtensionCallerIdResponseByDeviceItemCallerId] = None

class ReadExtensionCallerIdResponseByFeatureItemFeature(Enum):
    RingOut = 'RingOut'
    RingMe = 'RingMe'
    CallFlip = 'CallFlip'
    FaxNumber = 'FaxNumber'
    AdditionalSoftphone = 'AdditionalSoftphone'
    Alternate = 'Alternate'
    CommonPhone = 'CommonPhone'
    MobileApp = 'MobileApp'
    Delegated = 'Delegated'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadExtensionCallerIdResponseByFeatureItemCallerIdPhoneInfo(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a phone number """
    
    uri: Optional[str] = None
    """ Link to a phone number resource """
    
    phone_number: Optional[str] = None
    """ Phone number in [E.164](https://www.itu.int/rec/T-REC-E.164-201011-I) (with '+' sign) format """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadExtensionCallerIdResponseByFeatureItemCallerId(DataClassJsonMixin):
    type: Optional[str] = None
    """
    If 'PhoneNumber' value is specified, then a certain phone number is shown as a caller ID when
    using this telephony feature. If 'Blocked' value is specified, then a caller ID is hidden. The
    value 'CurrentLocation' can be specified for 'RingOut' feature only. The default is
    'PhoneNumber' = ['PhoneNumber', 'Blocked', 'CurrentLocation']
    """
    
    phone_info: Optional[ReadExtensionCallerIdResponseByFeatureItemCallerIdPhoneInfo] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadExtensionCallerIdResponseByFeatureItem(DataClassJsonMixin):
    """ Caller ID settings by feature """
    
    feature: Optional[ReadExtensionCallerIdResponseByFeatureItemFeature] = None
    caller_id: Optional[ReadExtensionCallerIdResponseByFeatureItemCallerId] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadExtensionCallerIdResponse(DataClassJsonMixin):
    uri: Optional[str] = None
    """ Canonical URL of a caller ID resource """
    
    by_device: Optional[List[ReadExtensionCallerIdResponseByDeviceItem]] = None
    by_feature: Optional[List[ReadExtensionCallerIdResponseByFeatureItem]] = None
    extension_name_for_outbound_calls: Optional[bool] = None
    """
    If 'True', then user first name and last name will be used as caller ID when making outbound
    calls from extension
    """
    
    extension_number_for_internal_calls: Optional[bool] = None
    """ If 'True', then extension number will be used as caller ID when making internal calls """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateExtensionCallerIdRequestByDeviceItemDevice(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a device """
    
    uri: Optional[str] = None
    """ Link to a device resource """
    
    name: Optional[str] = None
    """ Name of a device """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateExtensionCallerIdRequestByDeviceItemCallerIdPhoneInfo(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a phone number """
    
    uri: Optional[str] = None
    """ Link to a phone number resource """
    
    phone_number: Optional[str] = None
    """ Phone number in [E.164](https://www.itu.int/rec/T-REC-E.164-201011-I) (with '+' sign) format """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateExtensionCallerIdRequestByDeviceItemCallerId(DataClassJsonMixin):
    type: Optional[str] = None
    """
    If 'PhoneNumber' value is specified, then a certain phone number is shown as a caller ID when
    using this telephony feature. If 'Blocked' value is specified, then a caller ID is hidden. The
    value 'CurrentLocation' can be specified for 'RingOut' feature only. The default is
    'PhoneNumber' = ['PhoneNumber', 'Blocked', 'CurrentLocation']
    """
    
    phone_info: Optional[UpdateExtensionCallerIdRequestByDeviceItemCallerIdPhoneInfo] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateExtensionCallerIdRequestByDeviceItem(DataClassJsonMixin):
    """ Caller ID settings by device """
    
    device: Optional[UpdateExtensionCallerIdRequestByDeviceItemDevice] = None
    caller_id: Optional[UpdateExtensionCallerIdRequestByDeviceItemCallerId] = None

class UpdateExtensionCallerIdRequestByFeatureItemFeature(Enum):
    RingOut = 'RingOut'
    RingMe = 'RingMe'
    CallFlip = 'CallFlip'
    FaxNumber = 'FaxNumber'
    AdditionalSoftphone = 'AdditionalSoftphone'
    Alternate = 'Alternate'
    CommonPhone = 'CommonPhone'
    MobileApp = 'MobileApp'
    Delegated = 'Delegated'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateExtensionCallerIdRequestByFeatureItemCallerIdPhoneInfo(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a phone number """
    
    uri: Optional[str] = None
    """ Link to a phone number resource """
    
    phone_number: Optional[str] = None
    """ Phone number in [E.164](https://www.itu.int/rec/T-REC-E.164-201011-I) (with '+' sign) format """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateExtensionCallerIdRequestByFeatureItemCallerId(DataClassJsonMixin):
    type: Optional[str] = None
    """
    If 'PhoneNumber' value is specified, then a certain phone number is shown as a caller ID when
    using this telephony feature. If 'Blocked' value is specified, then a caller ID is hidden. The
    value 'CurrentLocation' can be specified for 'RingOut' feature only. The default is
    'PhoneNumber' = ['PhoneNumber', 'Blocked', 'CurrentLocation']
    """
    
    phone_info: Optional[UpdateExtensionCallerIdRequestByFeatureItemCallerIdPhoneInfo] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateExtensionCallerIdRequestByFeatureItem(DataClassJsonMixin):
    """ Caller ID settings by feature """
    
    feature: Optional[UpdateExtensionCallerIdRequestByFeatureItemFeature] = None
    caller_id: Optional[UpdateExtensionCallerIdRequestByFeatureItemCallerId] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateExtensionCallerIdRequest(DataClassJsonMixin):
    uri: Optional[str] = None
    """ Canonical URL of a caller ID resource """
    
    by_device: Optional[List[UpdateExtensionCallerIdRequestByDeviceItem]] = None
    by_feature: Optional[List[UpdateExtensionCallerIdRequestByFeatureItem]] = None
    extension_name_for_outbound_calls: Optional[bool] = None
    """
    If 'True', then user first name and last name will be used as caller ID when making outbound
    calls from extension
    """
    
    extension_number_for_internal_calls: Optional[bool] = None
    """ If 'True', then extension number will be used as caller ID when making internal calls """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateExtensionCallerIdResponseByDeviceItemDevice(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a device """
    
    uri: Optional[str] = None
    """ Link to a device resource """
    
    name: Optional[str] = None
    """ Name of a device """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateExtensionCallerIdResponseByDeviceItemCallerIdPhoneInfo(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a phone number """
    
    uri: Optional[str] = None
    """ Link to a phone number resource """
    
    phone_number: Optional[str] = None
    """ Phone number in [E.164](https://www.itu.int/rec/T-REC-E.164-201011-I) (with '+' sign) format """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateExtensionCallerIdResponseByDeviceItemCallerId(DataClassJsonMixin):
    type: Optional[str] = None
    """
    If 'PhoneNumber' value is specified, then a certain phone number is shown as a caller ID when
    using this telephony feature. If 'Blocked' value is specified, then a caller ID is hidden. The
    value 'CurrentLocation' can be specified for 'RingOut' feature only. The default is
    'PhoneNumber' = ['PhoneNumber', 'Blocked', 'CurrentLocation']
    """
    
    phone_info: Optional[UpdateExtensionCallerIdResponseByDeviceItemCallerIdPhoneInfo] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateExtensionCallerIdResponseByDeviceItem(DataClassJsonMixin):
    """ Caller ID settings by device """
    
    device: Optional[UpdateExtensionCallerIdResponseByDeviceItemDevice] = None
    caller_id: Optional[UpdateExtensionCallerIdResponseByDeviceItemCallerId] = None

class UpdateExtensionCallerIdResponseByFeatureItemFeature(Enum):
    RingOut = 'RingOut'
    RingMe = 'RingMe'
    CallFlip = 'CallFlip'
    FaxNumber = 'FaxNumber'
    AdditionalSoftphone = 'AdditionalSoftphone'
    Alternate = 'Alternate'
    CommonPhone = 'CommonPhone'
    MobileApp = 'MobileApp'
    Delegated = 'Delegated'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateExtensionCallerIdResponseByFeatureItemCallerIdPhoneInfo(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a phone number """
    
    uri: Optional[str] = None
    """ Link to a phone number resource """
    
    phone_number: Optional[str] = None
    """ Phone number in [E.164](https://www.itu.int/rec/T-REC-E.164-201011-I) (with '+' sign) format """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateExtensionCallerIdResponseByFeatureItemCallerId(DataClassJsonMixin):
    type: Optional[str] = None
    """
    If 'PhoneNumber' value is specified, then a certain phone number is shown as a caller ID when
    using this telephony feature. If 'Blocked' value is specified, then a caller ID is hidden. The
    value 'CurrentLocation' can be specified for 'RingOut' feature only. The default is
    'PhoneNumber' = ['PhoneNumber', 'Blocked', 'CurrentLocation']
    """
    
    phone_info: Optional[UpdateExtensionCallerIdResponseByFeatureItemCallerIdPhoneInfo] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateExtensionCallerIdResponseByFeatureItem(DataClassJsonMixin):
    """ Caller ID settings by feature """
    
    feature: Optional[UpdateExtensionCallerIdResponseByFeatureItemFeature] = None
    caller_id: Optional[UpdateExtensionCallerIdResponseByFeatureItemCallerId] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateExtensionCallerIdResponse(DataClassJsonMixin):
    uri: Optional[str] = None
    """ Canonical URL of a caller ID resource """
    
    by_device: Optional[List[UpdateExtensionCallerIdResponseByDeviceItem]] = None
    by_feature: Optional[List[UpdateExtensionCallerIdResponseByFeatureItem]] = None
    extension_name_for_outbound_calls: Optional[bool] = None
    """
    If 'True', then user first name and last name will be used as caller ID when making outbound
    calls from extension
    """
    
    extension_number_for_internal_calls: Optional[bool] = None
    """ If 'True', then extension number will be used as caller ID when making internal calls """
    

class ListExtensionGrantsExtensionType(Enum):
    User = 'User'
    FaxUser = 'FaxUser'
    VirtualUser = 'VirtualUser'
    DigitalUser = 'DigitalUser'
    Department = 'Department'
    Announcement = 'Announcement'
    Voicemail = 'Voicemail'
    SharedLinesGroup = 'SharedLinesGroup'
    PagingOnly = 'PagingOnly'
    IvrMenu = 'IvrMenu'
    ApplicationExtension = 'ApplicationExtension'
    ParkLocation = 'ParkLocation'
    Limited = 'Limited'
    Bot = 'Bot'

class ListExtensionGrantsResponseRecordsItemExtensionType(Enum):
    """ Extension type """
    
    User = 'User'
    Fax_User = 'Fax User'
    VirtualUser = 'VirtualUser'
    DigitalUser = 'DigitalUser'
    Department = 'Department'
    Announcement = 'Announcement'
    Voicemail = 'Voicemail'
    SharedLinesGroup = 'SharedLinesGroup'
    PagingOnly = 'PagingOnly'
    IvrMenu = 'IvrMenu'
    ApplicationExtension = 'ApplicationExtension'
    ParkLocation = 'ParkLocation'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListExtensionGrantsResponseRecordsItemExtension(DataClassJsonMixin):
    """ Extension information """
    
    id: Optional[str] = None
    """ Internal identifier of an extension """
    
    uri: Optional[str] = None
    """ Canonical URI of an extension """
    
    extension_number: Optional[str] = None
    """ Extension short number (usually 3 or 4 digits) """
    
    name: Optional[str] = None
    """ Name of extension """
    
    type: Optional[ListExtensionGrantsResponseRecordsItemExtensionType] = None
    """ Extension type """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListExtensionGrantsResponseRecordsItem(DataClassJsonMixin):
    uri: Optional[str] = None
    """ Canonical URI of a grant """
    
    extension: Optional[ListExtensionGrantsResponseRecordsItemExtension] = None
    """ Extension information """
    
    call_pickup: Optional[bool] = None
    """
    Specifies if picking up of other extensions' calls is allowed for the extension. If 'Presence'
    feature is disabled for the given extension, the flag is not returned
    """
    
    call_monitoring: Optional[bool] = None
    """
    Specifies if monitoring of other extensions' calls is allowed for the extension. If
    'CallMonitoring' feature is disabled for the given extension, the flag is not returned
    """
    
    call_on_behalf_of: Optional[bool] = None
    """
    Specifies whether the current extension is able to make or receive calls on behalf of the user
    referenced in extension object
    """
    
    call_delegation: Optional[bool] = None
    """
    Specifies whether the current extension can delegate a call to the user referenced in extension
    object
    """
    
    group_paging: Optional[bool] = None
    """
    Specifies whether the current extension is allowed to call Paging Only group referenced to in
    extension object
    """
    
    call_queue_setup: Optional[bool] = None
    """
    Specifies whether the current extension is assigned as a Full-Access manager in the call queue
    referenced in extension object
    """
    
    call_queue_members_setup: Optional[bool] = None
    """
    Specifies whether the current extension is assigned as a Members-Only manager in the call queue
    referenced in extension object
    """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListExtensionGrantsResponseNavigationFirstPage(DataClassJsonMixin):
    """ Canonical URI for the first page of the list """
    
    uri: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListExtensionGrantsResponseNavigationNextPage(DataClassJsonMixin):
    """ Canonical URI for the next page of the list """
    
    uri: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListExtensionGrantsResponseNavigationPreviousPage(DataClassJsonMixin):
    """ Canonical URI for the previous page of the list """
    
    uri: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListExtensionGrantsResponseNavigationLastPage(DataClassJsonMixin):
    """ Canonical URI for the last page of the list """
    
    uri: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListExtensionGrantsResponseNavigation(DataClassJsonMixin):
    """ Information on navigation """
    
    first_page: Optional[ListExtensionGrantsResponseNavigationFirstPage] = None
    """ Canonical URI for the first page of the list """
    
    next_page: Optional[ListExtensionGrantsResponseNavigationNextPage] = None
    """ Canonical URI for the next page of the list """
    
    previous_page: Optional[ListExtensionGrantsResponseNavigationPreviousPage] = None
    """ Canonical URI for the previous page of the list """
    
    last_page: Optional[ListExtensionGrantsResponseNavigationLastPage] = None
    """ Canonical URI for the last page of the list """
    
