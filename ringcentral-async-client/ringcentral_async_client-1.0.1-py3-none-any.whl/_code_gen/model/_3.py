from ._2 import *

class ExtensionCreationRequestSetupWizardState(Enum):
    """ Specifies extension configuration wizard state (web service setup). """
    
    NotStarted = 'NotStarted'
    Incomplete = 'Incomplete'
    Completed = 'Completed'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ExtensionCreationRequestSiteOperator(DataClassJsonMixin):
    """ Site Fax/SMS recipient (operator) reference. Multi-level IVR should be enabled """
    
    id: Optional[str] = None
    """ Internal identifier of an operator """
    
    uri: Optional[str] = None
    """ Link to an operator resource """
    
    extension_number: Optional[str] = None
    """ Extension number (pin) """
    
    name: Optional[str] = None
    """ Operator extension user full name """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ExtensionCreationRequestSite(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal idetifier of a site extension """
    
    uri: Optional[str] = None
    """ Link to a site resource """
    
    name: Optional[str] = None
    """ Extension user first name """
    
    extension_number: Optional[str] = None
    """ Extension number """
    
    caller_id_name: Optional[str] = None
    """
    Custom name of a caller. Max number of characters is 15 (only alphabetical symbols, numbers and
    commas are supported)
    """
    
    email: Optional[str] = None
    """ Exetnsion user email """
    
    business_address: Optional[dict] = None
    """ Extension user business address. The default is Company settings """
    
    regional_settings: Optional[dict] = None
    """ Information about regional settings. The default is Company settings """
    
    operator: Optional[ExtensionCreationRequestSiteOperator] = None
    """ Site Fax/SMS recipient (operator) reference. Multi-level IVR should be enabled """
    
    code: Optional[str] = None
    """ Site code value. Returned only if specified """
    

class ExtensionCreationRequestStatus(Enum):
    """ Extension current state """
    
    Enabled = 'Enabled'
    Disabled = 'Disabled'
    NotActivated = 'NotActivated'
    Unassigned = 'Unassigned'
    Frozen = 'Frozen'

class ExtensionCreationRequestStatusInfoReason(Enum):
    """ Type of suspension """
    
    Voluntarily = 'Voluntarily'
    Involuntarily = 'Involuntarily'
    SuspendedVoluntarily = 'SuspendedVoluntarily'
    SuspendedVoluntarily2 = 'SuspendedVoluntarily2'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ExtensionCreationRequestStatusInfo(DataClassJsonMixin):
    """ Status information (reason, comment). For 'Disabled' status only """
    
    comment: Optional[str] = None
    """ A free-form user comment, describing the status change reason """
    
    reason: Optional[ExtensionCreationRequestStatusInfoReason] = None
    """ Type of suspension """
    

class ExtensionCreationRequestType(Enum):
    """ Extension type """
    
    User = 'User'
    VirtualUser = 'VirtualUser'
    DigitalUser = 'DigitalUser'
    Department = 'Department'
    Announcement = 'Announcement'
    Voicemail = 'Voicemail'
    SharedLinesGroup = 'SharedLinesGroup'
    PagingOnly = 'PagingOnly'
    ParkLocation = 'ParkLocation'
    Limited = 'Limited'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ExtensionCreationRequest(DataClassJsonMixin):
    contact: Optional[ExtensionCreationRequestContact] = None
    """ Contact Information """
    
    extension_number: Optional[str] = None
    """ Number of extension """
    
    custom_fields: Optional[List[ExtensionCreationRequestCustomFieldsItem]] = None
    password: Optional[str] = None
    """ Password for extension. If not specified, the password is auto-generated """
    
    references: Optional[List[ExtensionCreationRequestReferencesItem]] = None
    """ List of non-RC internal identifiers assigned to an extension """
    
    regional_settings: Optional[ExtensionCreationRequestRegionalSettings] = None
    """ Extension region data (timezone, home country, language) """
    
    partner_id: Optional[str] = None
    """ Additional extension identifier, created by partner application and applied on client side """
    
    ivr_pin: Optional[str] = None
    """ IVR PIN """
    
    setup_wizard_state: Optional[ExtensionCreationRequestSetupWizardState] = 'NotStarted'
    """ Specifies extension configuration wizard state (web service setup). """
    
    site: Optional[ExtensionCreationRequestSite] = None
    status: Optional[ExtensionCreationRequestStatus] = None
    """ Extension current state """
    
    status_info: Optional[ExtensionCreationRequestStatusInfo] = None
    """ Status information (reason, comment). For 'Disabled' status only """
    
    type: Optional[ExtensionCreationRequestType] = None
    """ Extension type """
    
    hidden: Optional[bool] = None
    """
    Hides extension from showing in company directory. Supported for extensions of User type only.
    For unassigned extensions the value is set to 'True' by default. For assigned extensions the
    value is set to 'False' by default
    """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class SwitchInfoSite(DataClassJsonMixin):
    """ Site data """
    
    id: Optional[str] = None
    """ Internal identifier of a site. The company identifier value is 'main-site' """
    
    name: Optional[str] = None
    """ Name of a site """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class SwitchInfoEmergencyAddress(DataClassJsonMixin):
    """
    Emergency address assigned to the switch. Only one of a pair `emergencyAddress` or
    `emergencyLocationId` should be specified, otherwise the error is returned
    
    Generated by Python OpenAPI Parser
    """
    
    country: Optional[str] = None
    """ Country name """
    
    country_id: Optional[str] = None
    """ Internal identifier of a country """
    
    country_iso_code: Optional[str] = None
    """ ISO code of a country """
    
    country_name: Optional[str] = None
    """ Full name of a country """
    
    customer_name: Optional[str] = None
    """ Customer name """
    
    state: Optional[str] = None
    """ State/Province name. Mandatory for the USA, the UK and Canada """
    
    state_id: Optional[str] = None
    """ Internal identifier of a state """
    
    state_iso_code: Optional[str] = None
    """ ISO code of a state """
    
    state_name: Optional[str] = None
    """ Full name of a state """
    
    city: Optional[str] = None
    """ City name """
    
    street: Optional[str] = None
    """ First line address """
    
    street2: Optional[str] = None
    """ Second line address (apartment, suite, unit, building, floor, etc.) """
    
    zip: Optional[str] = None
    """ Postal (Zip) code """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class SwitchInfoEmergencyLocation(DataClassJsonMixin):
    """ Emergency response location information """
    
    id: Optional[str] = None
    """ Internal identifier of an emergency response location """
    
    name: Optional[str] = None
    """ Emergency response location name """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class SwitchInfo(DataClassJsonMixin):
    uri: Optional[str] = None
    """ Link to the network switch resource """
    
    id: Optional[str] = None
    """ Internal identifier of a network switch """
    
    chassis_id: Optional[str] = None
    """ Unique identifier of a network switch """
    
    name: Optional[str] = None
    """ Name of a network switch """
    
    site: Optional[SwitchInfoSite] = None
    """ Site data """
    
    emergency_address: Optional[SwitchInfoEmergencyAddress] = None
    """
    Emergency address assigned to the switch. Only one of a pair `emergencyAddress` or
    `emergencyLocationId` should be specified, otherwise the error is returned
    """
    
    emergency_location_id: Optional[str] = None
    """
    Deprecated. Emergency response location (address) internal identifier. Only one of a pair
    `emergencyAddress` or `emergencyLocationId` should be specified, otherwise the error is
    returned
    """
    
    emergency_location: Optional[SwitchInfoEmergencyLocation] = None
    """ Emergency response location information """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class EmergencyLocationInfoRequestAddress(DataClassJsonMixin):
    country: Optional[str] = None
    """ Country name """
    
    country_id: Optional[str] = None
    """ Internal identifier of a country """
    
    country_iso_code: Optional[str] = None
    """ ISO code of a country """
    
    country_name: Optional[str] = None
    """ Full name of a country """
    
    state: Optional[str] = None
    """ State/Province name. Mandatory for the USA, the UK and Canada """
    
    state_id: Optional[str] = None
    """ Internal identifier of a state """
    
    state_iso_code: Optional[str] = None
    """ ISO code of a state """
    
    state_name: Optional[str] = None
    """ Full name of a state """
    
    city: Optional[str] = None
    """ City name """
    
    street: Optional[str] = None
    """ First line address """
    
    street2: Optional[str] = None
    """ Second line address (apartment, suite, unit, building, floor, etc.) """
    
    zip: Optional[str] = None
    """ Postal (Zip) code """
    
    customer_name: Optional[str] = None
    """ Customer name """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class EmergencyLocationInfoRequestSite(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal idetifier of a site extension """
    
    name: Optional[str] = None
    """ Extension user first name """
    

class EmergencyLocationInfoRequestAddressStatus(Enum):
    """ Emergency address status """
    
    Valid = 'Valid'
    Invalid = 'Invalid'

class EmergencyLocationInfoRequestUsageStatus(Enum):
    """ Status of emergency response location usage. """
    
    Active = 'Active'
    Inactive = 'Inactive'

class EmergencyLocationInfoRequestVisibility(Enum):
    """
    Visibility of an emergency response location. If `Private` is set, then location is visible
    only for restricted number of users, specified in `owners` array
    
    Generated by Python OpenAPI Parser
    """
    
    Private = 'Private'
    Public = 'Public'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class EmergencyLocationInfoRequestOwnersItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a user - private location owner """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class EmergencyLocationInfoRequest(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of the emergency response location """
    
    address: Optional[EmergencyLocationInfoRequestAddress] = None
    name: Optional[str] = None
    """ Emergency response location name """
    
    site: Optional[EmergencyLocationInfoRequestSite] = None
    address_status: Optional[EmergencyLocationInfoRequestAddressStatus] = None
    """ Emergency address status """
    
    usage_status: Optional[EmergencyLocationInfoRequestUsageStatus] = None
    """ Status of emergency response location usage. """
    
    visibility: Optional[EmergencyLocationInfoRequestVisibility] = 'Public'
    """
    Visibility of an emergency response location. If `Private` is set, then location is visible
    only for restricted number of users, specified in `owners` array
    """
    
    owners: Optional[List[EmergencyLocationInfoRequestOwnersItem]] = None
    """ List of private location owners """
    

class CompanyPhoneNumberInfoPaymentType(Enum):
    """
    Payment type. 'External' is returned for forwarded numbers which are not terminated in the
    RingCentral phone system
    
    Generated by Python OpenAPI Parser
    """
    
    External = 'External'
    TollFree = 'TollFree'
    Local = 'Local'
    BusinessMobileNumberProvider = 'BusinessMobileNumberProvider'

class CompanyPhoneNumberInfoType(Enum):
    """ Phone number type """
    
    VoiceFax = 'VoiceFax'
    FaxOnly = 'FaxOnly'
    VoiceOnly = 'VoiceOnly'

class CompanyPhoneNumberInfoUsageType(Enum):
    """
    Usage type of a phone number. Usage type of a phone number. Numbers of 'NumberPool' type wont't
    be returned for phone number list requests
    
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
    MeetingsNumber = 'MeetingsNumber'
    NumberPool = 'NumberPool'
    BusinessMobileNumber = 'BusinessMobileNumber'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CompanyPhoneNumberInfoTemporaryNumber(DataClassJsonMixin):
    """ Temporary phone number, if any. Returned for phone numbers in `Pending` porting status only """
    
    id: Optional[str] = None
    """ Temporary phone number identifier """
    
    phone_number: Optional[str] = None
    """
    Temporary phone number in [E.164](https://www.itu.int/rec/T-REC-E.164-201011-I) (with '+' sign)
    format
    """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CompanyPhoneNumberInfo(DataClassJsonMixin):
    uri: Optional[str] = None
    """ Link to a company phone number resource """
    
    id: Optional[int] = None
    """ Internal identifier of a phone number """
    
    country: Optional[dict] = None
    """ Brief information on a phone number country """
    
    extension: Optional[dict] = None
    """
    Information on the extension, to which the phone number is assigned. Returned only for the
    request of Account phone number list
    """
    
    label: Optional[str] = None
    """ Custom user name of a phone number, if any """
    
    location: Optional[str] = None
    """ Location (City, State). Filled for local US numbers """
    
    payment_type: Optional[CompanyPhoneNumberInfoPaymentType] = None
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
    
    type: Optional[CompanyPhoneNumberInfoType] = None
    """ Phone number type """
    
    usage_type: Optional[CompanyPhoneNumberInfoUsageType] = None
    """
    Usage type of a phone number. Usage type of a phone number. Numbers of 'NumberPool' type wont't
    be returned for phone number list requests
    """
    
    temporary_number: Optional[CompanyPhoneNumberInfoTemporaryNumber] = None
    """ Temporary phone number, if any. Returned for phone numbers in `Pending` porting status only """
    
    contact_center_provider: Optional[dict] = None
    """
    CCRN (Contact Center Routing Number) provider. If not specified then the default value
    'InContact/North America' is used, its ID is '1'
    """
    
    vanity_pattern: Optional[str] = None
    """
    Vanity pattern for this number. Returned only when vanity search option is requested. Vanity
    pattern corresponds to request parameters nxx plus line or numberPattern
    """
    

class ExtensionUpdateRequestStatus(Enum):
    Disabled = 'Disabled'
    Enabled = 'Enabled'
    NotActivated = 'NotActivated'
    Frozen = 'Frozen'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ExtensionUpdateRequestContact(DataClassJsonMixin):
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
    
    email_as_login_name: Optional[bool] = None
    """
    If 'True' then contact email is enabled as login name for this user. Please note that email
    should be unique in this case. The default value is 'False'
    """
    
    department: Optional[str] = None
    """ Extension user department, if any """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ExtensionUpdateRequestRegionalSettingsHomeCountry(DataClassJsonMixin):
    id: Optional[str] = None
    """ internal Identifier of a country """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ExtensionUpdateRequestRegionalSettingsTimezone(DataClassJsonMixin):
    id: Optional[str] = None
    """ internal Identifier of a timezone """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ExtensionUpdateRequestRegionalSettingsLanguage(DataClassJsonMixin):
    id: Optional[str] = None
    """ internal Identifier of a language """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ExtensionUpdateRequestRegionalSettingsGreetingLanguage(DataClassJsonMixin):
    id: Optional[str] = None
    """ internal Identifier of a greeting language """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ExtensionUpdateRequestRegionalSettingsFormattingLocale(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal Identifier of a formatting language """
    

class ExtensionUpdateRequestRegionalSettingsTimeFormat(Enum):
    """ Time format setting """
    
    OBJECT_12h = '12h'
    OBJECT_24h = '24h'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ExtensionUpdateRequestRegionalSettings(DataClassJsonMixin):
    home_country: Optional[ExtensionUpdateRequestRegionalSettingsHomeCountry] = None
    timezone: Optional[ExtensionUpdateRequestRegionalSettingsTimezone] = None
    language: Optional[ExtensionUpdateRequestRegionalSettingsLanguage] = None
    greeting_language: Optional[ExtensionUpdateRequestRegionalSettingsGreetingLanguage] = None
    formatting_locale: Optional[ExtensionUpdateRequestRegionalSettingsFormattingLocale] = None
    time_format: Optional[ExtensionUpdateRequestRegionalSettingsTimeFormat] = '12h'
    """ Time format setting """
    

class ExtensionUpdateRequestSetupWizardState(Enum):
    NotStarted = 'NotStarted'
    Incomplete = 'Incomplete'
    Completed = 'Completed'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ExtensionUpdateRequestCallQueueInfo(DataClassJsonMixin):
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
class ExtensionUpdateRequestTransitionItem(DataClassJsonMixin):
    """ For NotActivated extensions only. Welcome email settings """
    
    send_welcome_emails_to_users: Optional[bool] = None
    """
    Specifies if an activation email is automatically sent to new users (Not Activated extensions)
    or not
    """
    
    send_welcome_email: Optional[bool] = None
    """ Supported for account confirmation. Specifies whether welcome email is sent """
    

class ExtensionUpdateRequestType(Enum):
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
class ExtensionUpdateRequest(DataClassJsonMixin):
    status: Optional[ExtensionUpdateRequestStatus] = None
    status_info: Optional[dict] = None
    reason: Optional[str] = None
    """ Type of suspension """
    
    comment: Optional[str] = None
    """ Free Form user comment """
    
    extension_number: Optional[str] = None
    """ Extension number available """
    
    contact: Optional[ExtensionUpdateRequestContact] = None
    regional_settings: Optional[ExtensionUpdateRequestRegionalSettings] = None
    setup_wizard_state: Optional[ExtensionUpdateRequestSetupWizardState] = None
    partner_id: Optional[str] = None
    """ Additional extension identifier, created by partner application and applied on client side """
    
    ivr_pin: Optional[str] = None
    """ IVR PIN """
    
    password: Optional[str] = None
    """ Password for extension """
    
    call_queue_info: Optional[ExtensionUpdateRequestCallQueueInfo] = None
    """ For Department extension type only. Call queue settings """
    
    transition: Optional[List[ExtensionUpdateRequestTransitionItem]] = None
    custom_fields: Optional[list] = None
    hidden: Optional[bool] = None
    """ Hides extension from showing in company directory. Supported for extensions of User type only """
    
    site: Optional[dict] = None
    """
    Site data. If multi-site feature is turned on for the account, then internal identifier of a
    site must be specified. To assign the wireless point to the main site (company) set site ID to
    `main-site`
    """
    
    type: Optional[ExtensionUpdateRequestType] = None
    """ Extension type """
    
    references: Optional[list] = None
    """ List of non-RC internal identifiers assigned to an extension """
    

class GetExtensionGrantListResponseRecordsItemExtensionType(Enum):
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
class GetExtensionGrantListResponseRecordsItemExtension(DataClassJsonMixin):
    """ Extension information """
    
    id: Optional[str] = None
    """ Internal identifier of an extension """
    
    uri: Optional[str] = None
    """ Canonical URI of an extension """
    
    extension_number: Optional[str] = None
    """ Extension short number (usually 3 or 4 digits) """
    
    name: Optional[str] = None
    """ Name of extension """
    
    type: Optional[GetExtensionGrantListResponseRecordsItemExtensionType] = None
    """ Extension type """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class GetExtensionGrantListResponseRecordsItem(DataClassJsonMixin):
    uri: Optional[str] = None
    """ Canonical URI of a grant """
    
    extension: Optional[GetExtensionGrantListResponseRecordsItemExtension] = None
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
class GetExtensionGrantListResponse(DataClassJsonMixin):
    """
    Required Properties:
     - navigation
     - paging
     - records
    
    Generated by Python OpenAPI Parser
    """
    
    records: List[GetExtensionGrantListResponseRecordsItem]
    """ List of extension grants with details """
    
    navigation: dict
    """ Information on navigation """
    
    paging: dict
    """ Information on paging """
    
    uri: Optional[str] = None
    """ Link to the list of extension grants """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateConferencingInfoRequestPhoneNumbersItem(DataClassJsonMixin):
    phone_number: Optional[str] = None
    """ Dial-in phone number to connect to a conference """
    
    default: Optional[bool] = None
    """
    'True' if the number is default for the conference. Default conference number is a domestic
    number that can be set by user (otherwise it is set by the system). Only one default number per
    country is allowed
    """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateConferencingInfoRequest(DataClassJsonMixin):
    phone_numbers: Optional[List[UpdateConferencingInfoRequestPhoneNumbersItem]] = None
    """
    Multiple dial-in phone numbers to connect to audio conference service, relevant for user's
    brand. Each number is given with the country and location information, in order to let the user
    choose the less expensive way to connect to a conference. The first number in the list is the
    primary conference number, that is default and domestic
    """
    
    allow_join_before_host: Optional[bool] = None
    """ Determines if host user allows conference participants to join before the host """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CallQueueMembersRecordsItem(DataClassJsonMixin):
    uri: Optional[str] = None
    """ Link to a call queue member """
    
    id: Optional[int] = None
    """ Internal identifier of a call queue member """
    
    extension_number: Optional[str] = None
    """ Extension number of a call queue member """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CallQueueMembers(DataClassJsonMixin):
    """
    Required Properties:
     - navigation
     - paging
     - records
     - uri
    
    Generated by Python OpenAPI Parser
    """
    
    uri: str
    """ Link to a call queue members resource """
    
    records: List[CallQueueMembersRecordsItem]
    """ List of call queue members """
    
    navigation: dict
    """ Information on navigation """
    
    paging: dict
    """ Information on paging """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateMultipleWirelessPointsRequestRecordsItemEmergencyAddress(DataClassJsonMixin):
    """
    Emergency address information. Only one of a pair `emergencyAddress` or `emergencyLocationId`
    should be specified, otherwise the error is returned
    
    Generated by Python OpenAPI Parser
    """
    
    country: Optional[str] = None
    """ Country name """
    
    country_id: Optional[str] = None
    """ Internal identifier of a country """
    
    country_iso_code: Optional[str] = None
    """ ISO code of a country """
    
    country_name: Optional[str] = None
    """ Full name of a country """
    
    customer_name: Optional[str] = None
    """ Customer name """
    
    state: Optional[str] = None
    """ State/Province name. Mandatory for the USA, the UK and Canada """
    
    state_id: Optional[str] = None
    """ Internal identifier of a state """
    
    state_iso_code: Optional[str] = None
    """ ISO code of a state """
    
    state_name: Optional[str] = None
    """ Full name of a state """
    
    city: Optional[str] = None
    """ City name """
    
    street: Optional[str] = None
    """ First line address """
    
    street2: Optional[str] = None
    """ Second line address (apartment, suite, unit, building, floor, etc.) """
    
    zip: Optional[str] = None
    """ Postal (Zip) code """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateMultipleWirelessPointsRequestRecordsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a wireless point """
    
    bssid: Optional[str] = None
    """
    Unique 48-bit identifier of wireless access point complying with MAC address conventions. Mask:
    XX:XX:XX:XX:XX:XX, where X can be a symbol in the range of 0-9 or A-F
    """
    
    name: Optional[str] = None
    """ Wireless access point name """
    
    site: Optional[dict] = None
    """
    Site data. If multi-site feature is turned on for the account, then internal identifier of a
    site must be specified. To assign the wireless point to the main site (company) set site ID to
    `main-site`
    """
    
    emergency_address: Optional[UpdateMultipleWirelessPointsRequestRecordsItemEmergencyAddress] = None
    """
    Emergency address information. Only one of a pair `emergencyAddress` or `emergencyLocationId`
    should be specified, otherwise the error is returned
    """
    
    emergency_location_id: Optional[str] = None
    """
    Deprecated. Internal identifier of the emergency response location (address). Only one of a
    pair `emergencyAddress` or `emergencyLocationId` should be specified, otherwise the error is
    returned
    """
    
    emergency_location: Optional[dict] = None
    """ Emergency response location information """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateMultipleWirelessPointsRequest(DataClassJsonMixin):
    records: Optional[List[UpdateMultipleWirelessPointsRequestRecordsItem]] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class AccountBusinessAddressResource(DataClassJsonMixin):
    uri: Optional[str] = None
    company: Optional[str] = None
    email: Optional[str] = None
    main_site_name: Optional[str] = None
    """ Custom site name """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ModifyAccountBusinessAddressRequestBusinessAddress(DataClassJsonMixin):
    """ Company business address """
    
    country: Optional[str] = None
    """ Name of a country """
    
    state: Optional[str] = None
    """ Name of a state/province """
    
    city: Optional[str] = None
    """ Name of a city """
    
    street: Optional[str] = None
    """ Street address """
    
    zip: Optional[str] = None
    """ Zip code """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ModifyAccountBusinessAddressRequest(DataClassJsonMixin):
    company: Optional[str] = None
    """ Company business name """
    
    email: Optional[str] = None
    """ Company business email address """
    
    business_address: Optional[ModifyAccountBusinessAddressRequestBusinessAddress] = None
    """ Company business address """
    
    main_site_name: Optional[str] = None
    """ Custom site name """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class EditPagingGroupRequest(DataClassJsonMixin):
    added_user_ids: Optional[List[str]] = None
    """ List of users that will be allowed to page a group specified """
    
    removed_user_ids: Optional[List[str]] = None
    """ List of users that will be unallowed to page a group specified """
    
    added_device_ids: Optional[List[str]] = None
    """ List of account devices that will be assigned to a paging group specified """
    
    removed_device_ids: Optional[List[str]] = None
    """ List of account devices that will be unassigned from a paging group specified """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateNetworkRequestPublicIpRangesItem(DataClassJsonMixin):
    id: Optional[str] = None
    start_ip: Optional[str] = None
    end_ip: Optional[str] = None
    matched: Optional[bool] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateNetworkRequestPrivateIpRangesItem(DataClassJsonMixin):
    id: Optional[str] = None
    start_ip: Optional[str] = None
    end_ip: Optional[str] = None
    name: Optional[str] = None
    """ Network name """
    
    emergency_address: Optional[dict] = None
    """
    Emergency address information. Only one of a pair `emergencyAddress` or `emergencyLocationId`
    should be specified, otherwise the error is returned
    """
    
    emergency_location_id: Optional[str] = None
    """
    Emergency response location (address) internal identifier. Only one of a pair
    `emergencyAddress` or `emergencyLocationId` should be specified, otherwise the error is
    returned
    """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateNetworkRequest(DataClassJsonMixin):
    name: Optional[str] = None
    site: Optional[dict] = None
    public_ip_ranges: Optional[List[CreateNetworkRequestPublicIpRangesItem]] = None
    private_ip_ranges: Optional[List[CreateNetworkRequestPrivateIpRangesItem]] = None
    emergency_location: Optional[dict] = None
    """ Emergency response location information """
    

class UpdateMultipleWirelessPointsResponseTaskStatus(Enum):
    """ Status of a task """
    
    Accepted = 'Accepted'
    Failed = 'Failed'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateMultipleWirelessPointsResponseTask(DataClassJsonMixin):
    """ Information on the task for multiple wireless points update """
    
    id: Optional[str] = None
    """ Internal identifier of a task for multiple switches creation """
    
    status: Optional[UpdateMultipleWirelessPointsResponseTaskStatus] = None
    """ Status of a task """
    
    creation_time: Optional[str] = None
    """ Task creation time """
    
    last_modified_time: Optional[str] = None
    """ Time of the task latest modification """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateMultipleWirelessPointsResponse(DataClassJsonMixin):
    task: Optional[UpdateMultipleWirelessPointsResponseTask] = None
    """ Information on the task for multiple wireless points update """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ExtensionCreationResponseContact(DataClassJsonMixin):
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
    
    business_address: Optional[dict] = None
    """ Business address of extension user company """
    
    email_as_login_name: Optional[bool] = 'False'
    """
    If 'True' then contact email is enabled as login name for this user. Please note that email
    should be unique in this case.
    """
    
    department: Optional[str] = None
    """ Extension user department, if any """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ExtensionCreationResponsePermissionsAdmin(DataClassJsonMixin):
    """ Admin permission """
    
    enabled: Optional[bool] = None
    """ Specifies if a permission is enabled or not """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ExtensionCreationResponsePermissions(DataClassJsonMixin):
    """
    Extension permissions, corresponding to the Service Web permissions 'Admin' and
    'InternationalCalling'
    
    Generated by Python OpenAPI Parser
    """
    
    admin: Optional[ExtensionCreationResponsePermissionsAdmin] = None
    """ Admin permission """
    
    international_calling: Optional[dict] = None
    """ International Calling permission """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ExtensionCreationResponseProfileImageScalesItem(DataClassJsonMixin):
    uri: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ExtensionCreationResponseProfileImage(DataClassJsonMixin):
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
    
    scales: Optional[List[ExtensionCreationResponseProfileImageScalesItem]] = None
    """ List of URIs to profile images in different dimensions """
    

class ExtensionCreationResponseServiceFeaturesItemFeatureName(Enum):
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
class ExtensionCreationResponseServiceFeaturesItem(DataClassJsonMixin):
    enabled: Optional[bool] = None
    """ Feature status; shows feature availability for an extension """
    
    feature_name: Optional[ExtensionCreationResponseServiceFeaturesItemFeatureName] = None
    """ Feature name """
    
    reason: Optional[str] = None
    """
    Reason for limitation of a particular service feature. Returned only if the enabled parameter
    value is 'False', see Service Feature Limitations and Reasons. When retrieving service features
    for an extension, the reasons for the limitations, if any, are returned in response
    """
    

class ExtensionCreationResponseSetupWizardState(Enum):
    """
    Specifies extension configuration wizard state (web service setup). The default value is
    'NotStarted'
    
    Generated by Python OpenAPI Parser
    """
    
    NotStarted = 'NotStarted'
    Incomplete = 'Incomplete'
    Completed = 'Completed'

class ExtensionCreationResponseStatus(Enum):
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

class ExtensionCreationResponseType(Enum):
    """ Extension type """
    
    User = 'User'
    VirtualUser = 'VirtualUser'
    DigitalUser = 'DigitalUser'
    Department = 'Department'
    Announcement = 'Announcement'
    Voicemail = 'Voicemail'
    SharedLinesGroup = 'SharedLinesGroup'
    PagingOnly = 'PagingOnly'
    ParkLocation = 'ParkLocation'
    Limited = 'Limited'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ExtensionCreationResponse(DataClassJsonMixin):
    id: Optional[int] = None
    """ Internal identifier of an extension """
    
    uri: Optional[str] = None
    """ Canonical URI of an extension """
    
    contact: Optional[ExtensionCreationResponseContact] = None
    """ Contact detailed information """
    
    custom_fields: Optional[list] = None
    extension_number: Optional[str] = None
    """ Number of department extension """
    
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
    
    permissions: Optional[ExtensionCreationResponsePermissions] = None
    """
    Extension permissions, corresponding to the Service Web permissions 'Admin' and
    'InternationalCalling'
    """
    
    profile_image: Optional[ExtensionCreationResponseProfileImage] = None
    """ Information on profile image """
    
    references: Optional[list] = None
    """ List of non-RC internal identifiers assigned to an extension """
    
    regional_settings: Optional[dict] = None
    """ Extension region data (timezone, home country, language) """
    
    service_features: Optional[List[ExtensionCreationResponseServiceFeaturesItem]] = None
    """
    Extension service features returned in response only when the logged-in user requests his/her
    own extension info, see also Extension Service Features
    """
    
    setup_wizard_state: Optional[ExtensionCreationResponseSetupWizardState] = None
    """
    Specifies extension configuration wizard state (web service setup). The default value is
    'NotStarted'
    """
    
    site: Optional[dict] = None
    """
    Site data. If multi-site feature is turned on for the account, then internal identifier of a
    site must be specified. To assign the wireless point to the main site (company) set site ID to
    `main-site`
    """
    
    status: Optional[ExtensionCreationResponseStatus] = None
    """
    Extension current state. If 'Unassigned' is specified, then extensions without
    ‘extensionNumber’ are returned. If not specified, then all extensions are returned
    """
    
    status_info: Optional[dict] = None
    """ Status information (reason, comment). Returned for 'Disabled' status only """
    
    type: Optional[ExtensionCreationResponseType] = None
    """ Extension type """
    
    hidden: Optional[bool] = None
    """ Hides extension from showing in company directory. Supported for extensions of User type only """
    

class UserTemplatesRecordsItemType(Enum):
    UserSettings = 'UserSettings'
    CallHandling = 'CallHandling'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UserTemplatesRecordsItem(DataClassJsonMixin):
    uri: Optional[str] = None
    """ Link to a template """
    
    id: Optional[str] = None
    """ Internal identifier of a template """
    
    type: Optional[UserTemplatesRecordsItemType] = None
    name: Optional[str] = None
    """ Name of a template """
    
    creation_time: Optional[str] = None
    """ Time of a template creation """
    
    last_modified_time: Optional[str] = None
    """ Time of the last template modification """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UserTemplates(DataClassJsonMixin):
    """
    Required Properties:
     - navigation
     - paging
     - records
    
    Generated by Python OpenAPI Parser
    """
    
    records: List[UserTemplatesRecordsItem]
    """ List of user templates """
    
    navigation: dict
    """ Information on navigation """
    
    paging: dict
    """ Information on paging """
    
    uri: Optional[str] = None
    """ Link to user templates resource """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CallQueueUpdateDetailsServiceLevelSettings(DataClassJsonMixin):
    """ Call queue service level settings """
    
    sla_goal: Optional[int] = None
    """
    Target percentage of calls that must be answered by agents within the service level time
    threshold
    """
    
    sla_threshold_seconds: Optional[int] = None
    """ The period of time in seconds that is considered to be an acceptable service level """
    
    include_abandoned_calls: Optional[bool] = None
    """
    Includes abandoned calls (when callers hang up prior to being served by an agent) into
    service-level calculation
    """
    
    abandoned_threshold_seconds: Optional[int] = None
    """
    Abandoned calls that are shorter than the defined period of time in seconds will not be
    included into the calculation of Service Level
    """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CallQueueUpdateDetails(DataClassJsonMixin):
    service_level_settings: Optional[CallQueueUpdateDetailsServiceLevelSettings] = None
    """ Call queue service level settings """
    
    editable_member_status: Optional[bool] = None
    """ Allows members to change their queue status """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class FeatureListRecordsItemParamsItem(DataClassJsonMixin):
    name: Optional[str] = None
    """ Parameter name """
    
    value: Optional[str] = None
    """ Parameter value """
    

class FeatureListRecordsItemReasonCode(Enum):
    """ Reason code """
    
    ServicePlanLimitation = 'ServicePlanLimitation'
    AccountLimitation = 'AccountLimitation'
    ExtensionTypeLimitation = 'ExtensionTypeLimitation'
    ExtensionLimitation = 'ExtensionLimitation'
    InsufficientPermissions = 'InsufficientPermissions'
    ConfigurationLimitation = 'ConfigurationLimitation'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class FeatureListRecordsItemReason(DataClassJsonMixin):
    """ Reason of the feature unavailability. Returned only if `available` is set to 'false' """
    
    code: Optional[FeatureListRecordsItemReasonCode] = None
    """ Reason code """
    
    message: Optional[str] = None
    """ Reason description """
    
    permission: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class FeatureListRecordsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a feature """
    
    available: Optional[bool] = None
    """
    Specifies if the feature is available for the current user according to services enabled for
    the account, type, entitlements and permissions of the extension. If the authorized user gets
    features of the other extension, only features that can be delegated are returned (such as
    configuration by administrators).
    """
    
    params: Optional[List[FeatureListRecordsItemParamsItem]] = None
    reason: Optional[FeatureListRecordsItemReason] = None
    """ Reason of the feature unavailability. Returned only if `available` is set to 'false' """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class FeatureList(DataClassJsonMixin):
    records: Optional[List[FeatureListRecordsItem]] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ExtensionCallerIdInfoByDeviceItemDevice(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a device """
    
    uri: Optional[str] = None
    """ Link to a device resource """
    
    name: Optional[str] = None
    """ Name of a device """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ExtensionCallerIdInfoByDeviceItemCallerIdPhoneInfo(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a phone number """
    
    uri: Optional[str] = None
    """ Link to a phone number resource """
    
    phone_number: Optional[str] = None
    """ Phone number in [E.164](https://www.itu.int/rec/T-REC-E.164-201011-I) (with '+' sign) format """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ExtensionCallerIdInfoByDeviceItemCallerId(DataClassJsonMixin):
    type: Optional[str] = None
    """
    If 'PhoneNumber' value is specified, then a certain phone number is shown as a caller ID when
    using this telephony feature. If 'Blocked' value is specified, then a caller ID is hidden. The
    value 'CurrentLocation' can be specified for 'RingOut' feature only. The default is
    'PhoneNumber' = ['PhoneNumber', 'Blocked', 'CurrentLocation']
    """
    
    phone_info: Optional[ExtensionCallerIdInfoByDeviceItemCallerIdPhoneInfo] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ExtensionCallerIdInfoByDeviceItem(DataClassJsonMixin):
    """ Caller ID settings by device """
    
    device: Optional[ExtensionCallerIdInfoByDeviceItemDevice] = None
    caller_id: Optional[ExtensionCallerIdInfoByDeviceItemCallerId] = None

class ExtensionCallerIdInfoByFeatureItemFeature(Enum):
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
class ExtensionCallerIdInfoByFeatureItemCallerId(DataClassJsonMixin):
    type: Optional[str] = None
    """
    If 'PhoneNumber' value is specified, then a certain phone number is shown as a caller ID when
    using this telephony feature. If 'Blocked' value is specified, then a caller ID is hidden. The
    value 'CurrentLocation' can be specified for 'RingOut' feature only. The default is
    'PhoneNumber' = ['PhoneNumber', 'Blocked', 'CurrentLocation']
    """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ExtensionCallerIdInfoByFeatureItem(DataClassJsonMixin):
    """ Caller ID settings by feature """
    
    feature: Optional[ExtensionCallerIdInfoByFeatureItemFeature] = None
    caller_id: Optional[ExtensionCallerIdInfoByFeatureItemCallerId] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ExtensionCallerIdInfo(DataClassJsonMixin):
    uri: Optional[str] = None
    """ Canonical URL of a caller ID resource """
    
    by_device: Optional[List[ExtensionCallerIdInfoByDeviceItem]] = None
    by_feature: Optional[List[ExtensionCallerIdInfoByFeatureItem]] = None
    extension_name_for_outbound_calls: Optional[bool] = None
    """
    If 'True', then user first name and last name will be used as caller ID when making outbound
    calls from extension
    """
    
    extension_number_for_internal_calls: Optional[bool] = None
    """ If 'True', then extension number will be used as caller ID when making internal calls """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class WirelessPointInfo(DataClassJsonMixin):
    uri: Optional[str] = None
    """ Link to the wireless point resource """
    
    id: Optional[str] = None
    """ Internal identifier of a wireless point """
    
    bssid: Optional[str] = None
    """ Unique 48-bit identifier of the wireless access point complying with MAC address conventions """
    
    name: Optional[str] = None
    """ Wireless access point name """
    
    site: Optional[dict] = None
    """ Site data (internal identifier and custom name of a site) """
    
    emergency_address: Optional[dict] = None
    """
    Emergency address assigned to the wireless point. Only one of a pair `emergencyAddress` or
    `emergencyLocationId` should be specified, otherwise the error is returned
    """
    
    emergency_location: Optional[dict] = None
    """ Emergency response location information """
    
    emergency_location_id: Optional[str] = None
    """
    Deprecated. Emergency response location (address) internal identifier. Only one of a pair
    `emergencyAddress` or `emergencyLocationId` should be specified, otherwise the error is
    returned
    """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class PagingOnlyGroupDevicesRecordsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a paging device """
    
    uri: Optional[str] = None
    """ Link to a paging device resource """
    
    name: Optional[str] = None
    """ Name of a paging device """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class PagingOnlyGroupDevices(DataClassJsonMixin):
    uri: Optional[str] = None
    """ Link to the list of devices assigned to the paging only group """
    
    records: Optional[List[PagingOnlyGroupDevicesRecordsItem]] = None
    """ List of paging devices assigned to this group """
    
    navigation: Optional[dict] = None
    """ Information on navigation """
    
    paging: Optional[dict] = None
    """ Information on paging """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CallMonitoringGroupsRecordsItem(DataClassJsonMixin):
    uri: Optional[str] = None
    """ Link to a call monitoring group resource """
    
    id: Optional[str] = None
    """ Internal identifier of a group """
    
    name: Optional[str] = None
    """ Name of a group """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CallMonitoringGroups(DataClassJsonMixin):
    """
    Required Properties:
     - navigation
     - paging
     - records
     - uri
    
    Generated by Python OpenAPI Parser
    """
    
    uri: str
    """ Link to a call monitoring groups resource """
    
    records: List[CallMonitoringGroupsRecordsItem]
    """ List of call monitoring group members """
    
    navigation: dict
    """ Information on navigation """
    
    paging: dict
    """ Information on paging """
    

class CallMonitoringGroupMemberListRecordsItemPermissionsItem(Enum):
    """
    Call monitoring permission; mltiple values are allowed: * `Monitoring` - User can monitor a
    group * `Monitored` - User can be monitored
    
    Generated by Python OpenAPI Parser
    """
    
    Monitoring = 'Monitoring'
    Monitored = 'Monitored'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CallMonitoringGroupMemberListRecordsItem(DataClassJsonMixin):
    uri: Optional[str] = None
    """ Link to a call monitoring group member """
    
    id: Optional[str] = None
    """ Internal identifier of a call monitoring group member """
    
    extension_number: Optional[str] = None
    """ Extension number of a call monitoring group member """
    
    permissions: Optional[List[CallMonitoringGroupMemberListRecordsItemPermissionsItem]] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CallMonitoringGroupMemberList(DataClassJsonMixin):
    """
    Required Properties:
     - navigation
     - paging
     - records
     - uri
    
    Generated by Python OpenAPI Parser
    """
    
    uri: str
    """ Link to a call monitoring group members resource """
    
    records: List[CallMonitoringGroupMemberListRecordsItem]
    """ List of a call monitoring group members """
    
    navigation: dict
    """ Information on navigation """
    
    paging: dict
    """ Information on paging """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateMultipleSwitchesRequestRecordsItem(DataClassJsonMixin):
    """
    Required Properties:
     - chassis_id
    
    Generated by Python OpenAPI Parser
    """
    
    chassis_id: str
    """
    Unique identifier of a network switch. The supported formats are: XX:XX:XX:XX:XX:XX (symbols
    0-9 and A-F) for MAC address and X.X.X.X for IP address (symbols 0-255)
    """
    
    name: Optional[str] = None
    """ Name of a network switch """
    
    site: Optional[dict] = None
    """ Site data """
    
    emergency_address: Optional[dict] = None
    """
    Emergency address assigned to the switch. Only one of a pair `emergencyAddress` or
    `emergencyLocationId` should be specified, otherwise the error is returned
    """
    
    emergency_location_id: Optional[str] = None
    """
    Deprecated. Emergency response location (address) internal identifier. Only one of a pair
    `emergencyAddress` or `emergencyLocationId` should be specified, otherwise the error is
    returned
    """
    
    emergency_location: Optional[dict] = None
    """ Emergency response location information """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateMultipleSwitchesRequest(DataClassJsonMixin):
    records: Optional[List[CreateMultipleSwitchesRequestRecordsItem]] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class GetServiceInfoResponseBrand(DataClassJsonMixin):
    """ Information on account brand """
    
    id: Optional[str] = None
    """ Internal identifier of a brand """
    
    name: Optional[str] = None
    """ Brand name, for example RingCentral UK , ClearFax """
    
    home_country: Optional[dict] = None
    """ Home country information """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class GetServiceInfoResponseContractedCountry(DataClassJsonMixin):
    """ Information on the contracted country of account """
    
    id: Optional[str] = None
    """ Identifier of a contracted country """
    
    uri: Optional[str] = None
    """ Canonical URI of a contracted country """
    

class GetServiceInfoResponseServicePlanFreemiumProductType(Enum):
    Freyja = 'Freyja'
    Phoenix = 'Phoenix'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class GetServiceInfoResponseServicePlan(DataClassJsonMixin):
    """ Information on account service plan """
    
    id: Optional[str] = None
    """ Internal identifier of a service plan """
    
    name: Optional[str] = None
    """ Name of a service plan """
    
    edition: Optional[str] = None
    """ Edition of a service plan """
    
    freemium_product_type: Optional[GetServiceInfoResponseServicePlanFreemiumProductType] = None

class GetServiceInfoResponseTargetServicePlanFreemiumProductType(Enum):
    Freyja = 'Freyja'
    Phoenix = 'Phoenix'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class GetServiceInfoResponseTargetServicePlan(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a target service plan """
    
    name: Optional[str] = None
    """ Name of a target service plan """
    
    edition: Optional[str] = None
    """ Edition of a service plan """
    
    freemium_product_type: Optional[GetServiceInfoResponseTargetServicePlanFreemiumProductType] = None

class GetServiceInfoResponseBillingPlanDurationUnit(Enum):
    """ Duration period """
    
    Month = 'Month'
    Day = 'Day'

class GetServiceInfoResponseBillingPlanType(Enum):
    """ Billing plan type """
    
    Initial = 'Initial'
    Regular = 'Regular'
    Suspended = 'Suspended'
    Trial = 'Trial'
    TrialNoCC = 'TrialNoCC'
    Free = 'Free'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class GetServiceInfoResponseBillingPlan(DataClassJsonMixin):
    """ Information on account billing plan """
    
    id: Optional[str] = None
    """ Internal identifier of a billing plan """
    
    name: Optional[str] = None
    """ Billing plan name """
    
    duration_unit: Optional[GetServiceInfoResponseBillingPlanDurationUnit] = None
    """ Duration period """
    
    duration: Optional[int] = None
    """ Number of duration units """
    
    type: Optional[GetServiceInfoResponseBillingPlanType] = None
    """ Billing plan type """
    
    included_phone_lines: Optional[int] = None
    """ Included digital lines count """
    

class GetServiceInfoResponseServiceFeaturesItemFeatureName(Enum):
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
class GetServiceInfoResponseServiceFeaturesItem(DataClassJsonMixin):
    feature_name: Optional[GetServiceInfoResponseServiceFeaturesItemFeatureName] = None
    """ Feature name """
    
    enabled: Optional[bool] = None
    """ Feature status, shows feature availability for the extension """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class GetServiceInfoResponseLimits(DataClassJsonMixin):
    """ Limits which are effective for the account """
    
    free_soft_phone_lines_per_extension: Optional[int] = None
    """ Max number of free softphone phone lines per user extension """
    
    meeting_size: Optional[int] = None
    """ Max number of participants in RingCentral meeting hosted by this account's user """
    
    cloud_recording_storage: Optional[int] = None
    """ Meetings recording cloud storage limitaion in Gb """
    
    max_monitored_extensions_per_user: Optional[int] = None
    """ Max number of extensions which can be included in the list of users monitored for Presence """
    
    max_extension_number_length: Optional[int] = 5
    """
    Max length of extension numbers of an account; the supported value is up to 8 symbols, depends
    on account type
    """
    
    site_code_length: Optional[int] = None
    """ Length of a site code """
    
    short_extension_number_length: Optional[int] = None
    """ Length of a short extension number """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class GetServiceInfoResponsePackage(DataClassJsonMixin):
    version: Optional[str] = None
    id: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class GetServiceInfoResponse(DataClassJsonMixin):
    uri: Optional[str] = None
    """ Canonical URI of the account Service Info resource """
    
    service_plan_name: Optional[str] = None
    """ Account Service Plan name """
    
    brand: Optional[GetServiceInfoResponseBrand] = None
    """ Information on account brand """
    
    contracted_country: Optional[GetServiceInfoResponseContractedCountry] = None
    """ Information on the contracted country of account """
    
    service_plan: Optional[GetServiceInfoResponseServicePlan] = None
    """ Information on account service plan """
    
    target_service_plan: Optional[GetServiceInfoResponseTargetServicePlan] = None
    billing_plan: Optional[GetServiceInfoResponseBillingPlan] = None
    """ Information on account billing plan """
    
    service_features: Optional[List[GetServiceInfoResponseServiceFeaturesItem]] = None
    """ Service features information, see Service Feature List """
    
    limits: Optional[GetServiceInfoResponseLimits] = None
    """ Limits which are effective for the account """
    
    package: Optional[GetServiceInfoResponsePackage] = None

class UserVideoConfigurationProvider(Enum):
    """ Video provider of the user """
    
    RCMeetings = 'RCMeetings'
    RCVideo = 'RCVideo'
    None_ = 'None'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UserVideoConfiguration(DataClassJsonMixin):
    provider: Optional[UserVideoConfigurationProvider] = None
    """ Video provider of the user """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateMultipleWirelessPointsRequestRecordsItem(DataClassJsonMixin):
    """
    Required Properties:
     - bssid
     - name
     - emergency_address
    
    Generated by Python OpenAPI Parser
    """
    
    bssid: str
    """
    Unique 48-bit identifier of wireless access point complying with MAC address conventions. The
    Mask is XX:XX:XX:XX:XX:XX, where X can be a symbol in the range of 0-9 or A-F
    """
    
    name: str
    """ Wireless access point name """
    
    emergency_address: dict
    """
    Emergency address information. Only one of a pair `emergencyAddress` or `emergencyLocationId`
    should be specified, otherwise the error is returned
    """
    
    site: Optional[dict] = None
    """
    Site data. If multi-site feature is turned on for the account, then internal identifier of a
    site must be specified. To assign the wireless point to the main site (company) set site ID to
    `main-site`
    """
    
    emergency_location_id: Optional[str] = None
    """
    Deprecated. Internal identifier of the emergency response location (address). Only one of a
    pair `emergencyAddress` or `emergencyLocationId` should be specified, otherwise the error is
    returned
    """
    
    emergency_location: Optional[dict] = None
    """ Emergency response location information """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateMultipleWirelessPointsRequest(DataClassJsonMixin):
    records: Optional[List[CreateMultipleWirelessPointsRequestRecordsItem]] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class GetLocationListResponseRecordsItemState(DataClassJsonMixin):
    """ Information on the state this location belongs to """
    
    id: Optional[str] = None
    """ Internal identifier of a state """
    
    uri: Optional[str] = None
    """ Link to a state resource """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class GetLocationListResponseRecordsItem(DataClassJsonMixin):
    uri: Optional[str] = None
    """ Canonical URI of a location """
    
    area_code: Optional[str] = None
    """ Area code of the location """
    
    city: Optional[str] = None
    """ Official name of the city, belonging to the certain state """
    
    npa: Optional[str] = None
    """
    Area code of the location (3-digit usually), according to the NANP number format, that can be
    summarized as NPA-NXX-xxxx and covers Canada, the United States, parts of the Caribbean Sea,
    and some Atlantic and Pacific islands. See for details North American Numbering Plan
    """
    
    nxx: Optional[str] = None
    """
    Central office code of the location, according to the NANP number format, that can be
    summarized as NPA-NXX-xxxx and covers Canada, the United States, parts of the Caribbean Sea,
    and some Atlantic and Pacific islands. See for details North American Numbering Plan
    """
    
    state: Optional[GetLocationListResponseRecordsItemState] = None
    """ Information on the state this location belongs to """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class GetLocationListResponse(DataClassJsonMixin):
    """
    Required Properties:
     - navigation
     - paging
    
    Generated by Python OpenAPI Parser
    """
    
    navigation: dict
    """ Information on navigation """
    
    paging: dict
    """ Information on paging """
    
    uri: Optional[str] = None
    """ Link to the location list resource """
    
    records: Optional[List[GetLocationListResponseRecordsItem]] = None
    """ List of locations """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class GetStateListResponseRecordsItemCountry(DataClassJsonMixin):
    """ Information on a country the state belongs to """
    
    id: Optional[str] = None
    """ Internal identifier of a state """
    
    uri: Optional[str] = None
    """ Canonical URI of a state """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class GetStateListResponseRecordsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a state """
    
    uri: Optional[str] = None
    """ Canonical URI of a state """
    
    country: Optional[GetStateListResponseRecordsItemCountry] = None
    """ Information on a country the state belongs to """
    
    iso_code: Optional[str] = None
    """ Short code for a state (2-letter usually) """
    
    name: Optional[str] = None
    """ Official name of a state """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class GetStateListResponse(DataClassJsonMixin):
    uri: Optional[str] = None
    """ Link to the states list resource """
    
    records: Optional[List[GetStateListResponseRecordsItem]] = None
    """ List of states """
    
    navigation: Optional[dict] = None
    """ Information on navigation """
    
    paging: Optional[dict] = None
    """ Information on paging """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CallQueueBulkAssignResource(DataClassJsonMixin):
    added_extension_ids: Optional[List[str]] = None
    removed_extension_ids: Optional[List[str]] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class NetworksListRecordsItemPrivateIpRangesItem(DataClassJsonMixin):
    id: Optional[str] = None
    start_ip: Optional[str] = None
    end_ip: Optional[str] = None
    name: Optional[str] = None
    """ Network name """
    
    emergency_address: Optional[dict] = None
    """
    Emergency address information. Only one of a pair `emergencyAddress` or `emergencyLocationId`
    should be specified, otherwise the error is returned
    """
    
    emergency_location_id: Optional[str] = None
    """
    Emergency response location (address) internal identifier. Only one of a pair
    `emergencyAddress` or `emergencyLocationId` should be specified, otherwise the error is
    returned
    """
    
    matched: Optional[bool] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class NetworksListRecordsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a network """
    
    uri: Optional[str] = None
    """ Link to a network resource """
    
    name: Optional[str] = None
    public_ip_ranges: Optional[list] = None
    private_ip_ranges: Optional[List[NetworksListRecordsItemPrivateIpRangesItem]] = None
    emergency_location: Optional[dict] = None
    """ Emergency response location information """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class NetworksList(DataClassJsonMixin):
    uri: Optional[str] = None
    """ Link to a networks resource """
    
    records: Optional[List[NetworksListRecordsItem]] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ValidateMultipleWirelessPointsRequestRecordsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a wireless point """
    
    bssid: Optional[str] = None
    """ Unique 48-bit identifier of the wireless access point complying with MAC address conventions """
    
    name: Optional[str] = None
    """ Wireless access point name """
    
    site: Optional[dict] = None
    """ Site data (internal identifier and custom name of a site) """
    
    emergency_address: Optional[dict] = None
    """
    Emergency address assigned to the wireless point. Only one of a pair `emergencyAddress` or
    `emergencyLocationId` should be specified, otherwise the error is returned
    """
    
    emergency_location_id: Optional[str] = None
    """
    Emergency response location (address) internal identifier. Only one of a pair
    `emergencyAddress` or `emergencyLocationId` should be specified, otherwise the error is
    returned
    """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ValidateMultipleWirelessPointsRequest(DataClassJsonMixin):
    records: Optional[List[ValidateMultipleWirelessPointsRequestRecordsItem]] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class GetExtensionListResponseRecordsItemAccount(DataClassJsonMixin):
    """ Account information """
    
    id: Optional[str] = None
    """ Internal identifier of an account """
    
    uri: Optional[str] = None
    """ Canonical URI of an account """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class GetExtensionListResponseRecordsItemDepartmentsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a department extension """
    
    uri: Optional[str] = None
    """ Canonical URI of a department extension """
    
    extension_number: Optional[str] = None
    """ Number of a department extension """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class GetExtensionListResponseRecordsItemRolesItem(DataClassJsonMixin):
    uri: Optional[str] = None
    id: Optional[str] = None
    """ Internal identifier of a role """
    

class GetExtensionListResponseRecordsItemSetupWizardState(Enum):
    """ Specifies extension configuration wizard state (web service setup). """
    
    NotStarted = 'NotStarted'
    Incomplete = 'Incomplete'
    Completed = 'Completed'

class GetExtensionListResponseRecordsItemStatus(Enum):
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

class GetExtensionListResponseRecordsItemType(Enum):
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
class GetExtensionListResponseRecordsItemCallQueueInfo(DataClassJsonMixin):
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
class GetExtensionListResponseRecordsItem(DataClassJsonMixin):
    id: Optional[int] = None
    """ Internal identifier of an extension """
    
    uri: Optional[str] = None
    """ Canonical URI of an extension """
    
    account: Optional[GetExtensionListResponseRecordsItemAccount] = None
    """ Account information """
    
    contact: Optional[dict] = None
    """ Contact detailed information """
    
    custom_fields: Optional[list] = None
    departments: Optional[List[GetExtensionListResponseRecordsItemDepartmentsItem]] = None
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
    
    profile_image: Optional[dict] = None
    """ Information on profile image """
    
    references: Optional[list] = None
    """ List of non-RC internal identifiers assigned to an extension """
    
    roles: Optional[List[GetExtensionListResponseRecordsItemRolesItem]] = None
    regional_settings: Optional[dict] = None
    """ Extension region data (timezone, home country, language) """
    
    service_features: Optional[list] = None
    """
    Extension service features returned in response only when the logged-in user requests his/her
    own extension info, see also Extension Service Features
    """
    
    setup_wizard_state: Optional[GetExtensionListResponseRecordsItemSetupWizardState] = 'NotStarted'
    """ Specifies extension configuration wizard state (web service setup). """
    
    status: Optional[GetExtensionListResponseRecordsItemStatus] = None
    """
    Extension current state. If 'Unassigned' is specified, then extensions without
    ‘extensionNumber’ are returned. If not specified, then all extensions are returned
    """
    
    status_info: Optional[dict] = None
    """ Status information (reason, comment). Returned for 'Disabled' status only """
    
    type: Optional[GetExtensionListResponseRecordsItemType] = None
    """ Extension type """
    
    call_queue_info: Optional[GetExtensionListResponseRecordsItemCallQueueInfo] = None
    """ For Department extension type only. Call queue settings """
    
    hidden: Optional[bool] = None
    """ Hides extension from showing in company directory. Supported for extensions of User type only """
    
    site: Optional[dict] = None
    """
    Site data. If multi-site feature is turned on for the account, then internal identifier of a
    site must be specified. To assign the wireless point to the main site (company) set site ID to
    `main-site`
    """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class GetExtensionListResponse(DataClassJsonMixin):
    """
    Required Properties:
     - records
    
    Generated by Python OpenAPI Parser
    """
    
    records: List[GetExtensionListResponseRecordsItem]
    """ List of extensions with extension information """
    
    uri: Optional[str] = None
    """ Link to the extension list resource """
    
    navigation: Optional[dict] = None
    """ Information on navigation """
    
    paging: Optional[dict] = None
    """ Information on paging """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CallQueues(DataClassJsonMixin):
    """
    Required Properties:
     - navigation
     - paging
     - records
     - uri
    
    Generated by Python OpenAPI Parser
    """
    
    uri: str
    """ Link to a call queues resource """
    
    records: list
    """ List of call queues """
    
    navigation: dict
    """ Information on navigation """
    
    paging: dict
    """ Information on paging """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class BulkAssignAutomaticLocationUpdatesUsers(DataClassJsonMixin):
    enabled_user_ids: Optional[List[str]] = None
    disabled_user_ids: Optional[List[str]] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateSwitchInfo(DataClassJsonMixin):
    id: Optional[str] = None
    """ internal identifier of a switch """
    
    chassis_id: Optional[str] = None
    """
    Unique identifier of a network switch. The supported formats are: XX:XX:XX:XX:XX:XX (symbols
    0-9 and A-F) for MAC address and X.X.X.X for IP address (symbols 0-255)
    """
    
    name: Optional[str] = None
    """ Name of a network switch """
    
    site: Optional[dict] = None
    """ Site data """
    
    emergency_address: Optional[dict] = None
    """
    Emergency address assigned to the switch. Only one of a pair `emergencyAddress` or
    `emergencyLocationId` should be specified, otherwise the error is returned
    """
    
    emergency_location_id: Optional[str] = None
    """
    Deprecated. Emergency response location (address) internal identifier. Only one of a pair
    `emergencyAddress` or `emergencyLocationId` should be specified, otherwise the error is
    returned
    """
    
    emergency_location: Optional[dict] = None
    """ Emergency response location information """
    

class AutomaticLocationUpdatesTaskInfoStatus(Enum):
    """ Status of a task """
    
    Accepted = 'Accepted'
    InProgress = 'InProgress'
    Completed = 'Completed'
    Failed = 'Failed'

class AutomaticLocationUpdatesTaskInfoType(Enum):
    """ Type of a task """
    
    WirelessPointsBulkCreate = 'WirelessPointsBulkCreate'
    WirelessPointsBulkUpdate = 'WirelessPointsBulkUpdate'
    SwitchesBulkCreate = 'SwitchesBulkCreate'
    SwitchesBulkUpdate = 'SwitchesBulkUpdate'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class AutomaticLocationUpdatesTaskInfoResultRecordsItemErrorsItem(DataClassJsonMixin):
    error_code: Optional[str] = None
    message: Optional[str] = None
    parameter_name: Optional[str] = None
    description: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class AutomaticLocationUpdatesTaskInfoResultRecordsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of the created/updated element - wireless point or network switch """
    
    bssid: Optional[str] = None
    """
    Unique 48-bit identifier of the wireless access point complying with MAC address conventions.
    Returned only for 'Wireless Points Bulk Create' tasks
    """
    
    chassis_id: Optional[str] = None
    """ Unique identifier of a network switch. Returned only for 'Switches Bulk Create' tasks """
    
    status: Optional[str] = None
    """ Operation status """
    
    errors: Optional[List[AutomaticLocationUpdatesTaskInfoResultRecordsItemErrorsItem]] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class AutomaticLocationUpdatesTaskInfoResult(DataClassJsonMixin):
    """ Task detailed result. Returned for failed and completed tasks """
    
    records: Optional[List[AutomaticLocationUpdatesTaskInfoResultRecordsItem]] = None
    """ Detailed task results by elements from initial request """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class AutomaticLocationUpdatesTaskInfo(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a task """
    
    status: Optional[AutomaticLocationUpdatesTaskInfoStatus] = None
    """ Status of a task """
    
    creation_time: Optional[str] = None
    """ Task creation time """
    
    last_modified_time: Optional[str] = None
    """ Time of the task latest modification """
    
    type: Optional[AutomaticLocationUpdatesTaskInfoType] = None
    """ Type of a task """
    
    result: Optional[AutomaticLocationUpdatesTaskInfoResult] = None
    """ Task detailed result. Returned for failed and completed tasks """
    

class EmergencyLocationListRecordsItemAddressStatus(Enum):
    """ Emergency address status """
    
    Valid = 'Valid'
    Invalid = 'Invalid'

class EmergencyLocationListRecordsItemUsageStatus(Enum):
    """ Status of emergency response location usage. """
    
    Active = 'Active'
    Inactive = 'Inactive'

class EmergencyLocationListRecordsItemSyncStatus(Enum):
    """
    Resulting status of emergency address synchronization. Returned if `syncEmergencyAddress`
    parameter is set to 'True'
    
    Generated by Python OpenAPI Parser
    """
    
    Verified = 'Verified'
    Updated = 'Updated'
    Deleted = 'Deleted'
    ActivationProcess = 'ActivationProcess'
    Unsupported = 'Unsupported'
    Failed = 'Failed'

class EmergencyLocationListRecordsItemVisibility(Enum):
    """
    Visibility of an emergency response location. If `Private` is set, then location is visible
    only for restricted number of users, specified in `owners` array
    
    Generated by Python OpenAPI Parser
    """
    
    Private = 'Private'
    Public = 'Public'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class EmergencyLocationListRecordsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of the emergency response location """
    
    address: Optional[dict] = None
    name: Optional[str] = None
    """ Emergency response location name """
    
    site: Optional[dict] = None
    address_status: Optional[EmergencyLocationListRecordsItemAddressStatus] = None
    """ Emergency address status """
    
    usage_status: Optional[EmergencyLocationListRecordsItemUsageStatus] = None
    """ Status of emergency response location usage. """
    
    sync_status: Optional[EmergencyLocationListRecordsItemSyncStatus] = None
    """
    Resulting status of emergency address synchronization. Returned if `syncEmergencyAddress`
    parameter is set to 'True'
    """
    
    visibility: Optional[EmergencyLocationListRecordsItemVisibility] = 'Public'
    """
    Visibility of an emergency response location. If `Private` is set, then location is visible
    only for restricted number of users, specified in `owners` array
    """
    
    owners: Optional[list] = None
    """ List of private location owners """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class EmergencyLocationList(DataClassJsonMixin):
    records: Optional[List[EmergencyLocationListRecordsItem]] = None
    navigation: Optional[dict] = None
    """ Information on navigation """
    
    paging: Optional[dict] = None
    """ Information on paging """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class NotificationSettingsUpdateRequestVoicemails(DataClassJsonMixin):
    notify_by_email: Optional[bool] = None
    """ Email notification flag """
    
    notify_by_sms: Optional[bool] = None
    """ SMS notification flag """
    
    advanced_email_addresses: Optional[List[str]] = None
    """
    List of recipient email addresses for voicemail notifications. Returned if specified, in both
    modes (advanced/basic). Applied in advanced mode only
    """
    
    advanced_sms_email_addresses: Optional[List[str]] = None
    """
    List of recipient phone numbers for voicemail notifications. Returned if specified, in both
    modes (advanced/basic). Applied in advanced mode only
    """
    
    include_attachment: Optional[bool] = None
    """ Indicates whether voicemail should be attached to email """
    
    include_transcription: Optional[bool] = None
    """ Specifies whether to add voicemail transcription or not """
    
    mark_as_read: Optional[bool] = None
    """ Indicates whether a voicemail should be automatically marked as read """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class NotificationSettingsUpdateRequestInboundFaxes(DataClassJsonMixin):
    notify_by_email: Optional[bool] = None
    """ Email notification flag """
    
    notify_by_sms: Optional[bool] = None
    """ SMS notification flag """
    
    advanced_email_addresses: Optional[List[str]] = None
    """
    List of recipient email addresses for inbound fax notifications. Returned if specified, in both
    modes (advanced/basic). Applied in advanced mode only
    """
    
    advanced_sms_email_addresses: Optional[List[str]] = None
    """
    List of recipient phone numbers for inbound fax notifications. Returned if specified, in both
    modes (advanced/basic). Applied in advanced mode only
    """
    
    include_attachment: Optional[bool] = None
    """ Indicates whether fax should be attached to email """
    
    mark_as_read: Optional[bool] = None
    """ Indicates whether email should be automatically marked as read """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class NotificationSettingsUpdateRequestOutboundFaxes(DataClassJsonMixin):
    notify_by_email: Optional[bool] = None
    """ Email notification flag """
    
    notify_by_sms: Optional[bool] = None
    """ SMS notification flag """
    
    advanced_email_addresses: Optional[List[str]] = None
    """
    List of recipient email addresses for outbound fax notifications. Returned if specified, in
    both modes (advanced/basic). Applied in advanced mode only
    """
    
    advanced_sms_email_addresses: Optional[List[str]] = None
    """
    List of recipient phone numbers for outbound fax notifications. Returned if specified, in both
    modes (advanced/basic). Applied in advanced mode only
    """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class NotificationSettingsUpdateRequestInboundTexts(DataClassJsonMixin):
    notify_by_email: Optional[bool] = None
    """ Email notification flag """
    
    notify_by_sms: Optional[bool] = None
    """ SMS notification flag """
    
    advanced_email_addresses: Optional[List[str]] = None
    """
    List of recipient email addresses for inbound text message notifications. Returned if
    specified, in both modes (advanced/basic). Applied in advanced mode only
    """
    
    advanced_sms_email_addresses: Optional[List[str]] = None
    """
    List of recipient phone numbers for inbound text message notifications. Returned if specified,
    in both modes (advanced/basic). Applied in advanced mode only
    """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class NotificationSettingsUpdateRequestMissedCalls(DataClassJsonMixin):
    notify_by_email: Optional[bool] = None
    """ Email notification flag """
    
    notify_by_sms: Optional[bool] = None
    """ SMS notification flag """
    
    advanced_email_addresses: Optional[List[str]] = None
    """
    List of recipient email addresses for missed call notifications. Returned if specified, in both
    modes (advanced/basic). Applied in advanced mode only
    """
    
    advanced_sms_email_addresses: Optional[List[str]] = None
    """
    List of recipient phone numbers for missed call notifications. Returned if specified, in both
    modes (advanced/basic). Applied in advanced mode only
    """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class NotificationSettingsUpdateRequest(DataClassJsonMixin):
    email_addresses: Optional[List[str]] = None
    """ List of notification recipient email addresses """
    
    sms_email_addresses: Optional[List[str]] = None
    """ List of notification recipient email addresses """
    
    advanced_mode: Optional[bool] = None
    """
    Specifies notifications settings mode. If 'True' then advanced mode is on, it allows using
    different emails and/or phone numbers for each notification type. If 'False' then basic mode is
    on. Advanced mode settings are returned in both modes, if specified once, but if basic mode is
    switched on, they are not applied
    """
    
    voicemails: Optional[NotificationSettingsUpdateRequestVoicemails] = None
    inbound_faxes: Optional[NotificationSettingsUpdateRequestInboundFaxes] = None
    outbound_faxes: Optional[NotificationSettingsUpdateRequestOutboundFaxes] = None
    inbound_texts: Optional[NotificationSettingsUpdateRequestInboundTexts] = None
    missed_calls: Optional[NotificationSettingsUpdateRequestMissedCalls] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateCallMonitoringGroupRequest(DataClassJsonMixin):
    """
    Required Properties:
     - name
    
    Generated by Python OpenAPI Parser
    """
    
    name: str
    """ Name of a group """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class SwitchesList(DataClassJsonMixin):
    uri: Optional[str] = None
    """ Link to the switches list resource """
    
    records: Optional[list] = None
    """ Switches map """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateMultipleSwitchesResponse(DataClassJsonMixin):
    """ Information on the task for multiple switches creation """
    
    task: Optional[dict] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateMultipleWirelessPointsResponse(DataClassJsonMixin):
    task: Optional[dict] = None
    """ Information on the task for multiple wireless points creation """
    

class NotificationSettingsEmailRecipientsItemStatus(Enum):
    """ Current state of an extension """
    
    Enabled = 'Enabled'
    Disable = 'Disable'
    NotActivated = 'NotActivated'
    Unassigned = 'Unassigned'

class NotificationSettingsEmailRecipientsItemPermission(Enum):
    """ Call queue manager permission """
    
    FullAccess = 'FullAccess'
    MembersOnly = 'MembersOnly'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class NotificationSettingsEmailRecipientsItem(DataClassJsonMixin):
    extension_id: Optional[str] = None
    """ Internal identifier of an extension """
    
    full_name: Optional[str] = None
    """ User full name """
    
    extension_number: Optional[str] = None
    """ User extension number """
    
    status: Optional[NotificationSettingsEmailRecipientsItemStatus] = None
    """ Current state of an extension """
    
    email_addresses: Optional[List[str]] = None
    """
    List of user email addresses from extension notification settings. By default main email
    address from contact information is returned
    """
    
    permission: Optional[NotificationSettingsEmailRecipientsItemPermission] = None
    """ Call queue manager permission """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class NotificationSettings(DataClassJsonMixin):
    uri: Optional[str] = None
    """ Canonical URI of notifications settings resource """
    
    email_recipients: Optional[List[NotificationSettingsEmailRecipientsItem]] = None
    """
    List of extensions specified as email notification recipients. Returned only for call queues
    where queue managers are assigned as user extensions.
    """
    
    email_addresses: Optional[List[str]] = None
    """ List of notification recipient email addresses """
    
    sms_email_addresses: Optional[List[str]] = None
    """ List of notification recipient email addresses """
    
    advanced_mode: Optional[bool] = None
    """
    Specifies notifications settings mode. If 'True' then advanced mode is on, it allows using
    different emails and/or phone numbers for each notification type. If 'False' then basic mode is
    on. Advanced mode settings are returned in both modes, if specified once, but if basic mode is
    switched on, they are not applied
    """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateMultipleSwitchesResponse(DataClassJsonMixin):
    task: Optional[dict] = None
    """ Information on the task for multiple switches update """
    

class ValidateMultipleWirelessPointsResponseRecordsItemStatus(Enum):
    """ Validation result status """
    
    Valid = 'Valid'
    Invalid = 'Invalid'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ValidateMultipleWirelessPointsResponseRecordsItemErrorsItem(DataClassJsonMixin):
    error_code: Optional[str] = None
    """ Error code """
    
    message: Optional[str] = None
    """ Error message """
    
    parameter_name: Optional[str] = None
    """ Name of invalid parameter """
    
    feature_name: Optional[str] = None
    parameter_value: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ValidateMultipleWirelessPointsResponseRecordsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a wireless point """
    
    bssid: Optional[str] = None
    """ Unique 48-bit identifier of the wireless access point complying with MAC address conventions """
    
    status: Optional[ValidateMultipleWirelessPointsResponseRecordsItemStatus] = None
    """ Validation result status """
    
    errors: Optional[List[ValidateMultipleWirelessPointsResponseRecordsItemErrorsItem]] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ValidateMultipleWirelessPointsResponse(DataClassJsonMixin):
    records: Optional[List[ValidateMultipleWirelessPointsResponseRecordsItem]] = None

class CallQueueDetailsStatus(Enum):
    """ Call queue status """
    
    Enabled = 'Enabled'
    Disabled = 'Disabled'
    NotActivated = 'NotActivated'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CallQueueDetails(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a call queue """
    
    name: Optional[str] = None
    """ Call queue name """
    
    extension_number: Optional[str] = None
    """ Call queue extension number """
    
    status: Optional[CallQueueDetailsStatus] = None
    """ Call queue status """
    
    service_level_settings: Optional[dict] = None
    """ Call queue service level settings """
    
    editable_member_status: Optional[bool] = None
    """ Allows members to change their queue status """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class DepartmentMemberList(DataClassJsonMixin):
    uri: Optional[str] = None
    """ Link to the list of department members """
    
    records: Optional[list] = None
    """ List of department members extensions """
    
    navigation: Optional[dict] = None
    """ Information on navigation """
    
    paging: Optional[dict] = None
    """ Information on paging """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class WirelessPointsList(DataClassJsonMixin):
    uri: Optional[str] = None
    """ Link to the wireless point list resource """
    
    records: Optional[list] = None
    """ List of wireless points with assigned emergency addresses """
    
    navigation: Optional[dict] = None
    """ Information on navigation """
    
    paging: Optional[dict] = None
    """ Information on paging """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateMultipleSwitchesRequest(DataClassJsonMixin):
    records: Optional[list] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateNetworkRequest(DataClassJsonMixin):
    name: Optional[str] = None
    public_ip_ranges: Optional[list] = None
    private_ip_ranges: Optional[list] = None
    emergency_location: Optional[dict] = None
    """ Emergency response location information """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ValidateMultipleSwitchesRequest(DataClassJsonMixin):
    records: Optional[list] = None

class ValidateMultipleSwitchesResponseRecordsItemStatus(Enum):
    """ Validation result status """
    
    Valid = 'Valid'
    Invalid = 'Invalid'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ValidateMultipleSwitchesResponseRecordsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a switch """
    
    chassis_id: Optional[str] = None
    """ Unique identifier of a network switch """
    
    status: Optional[ValidateMultipleSwitchesResponseRecordsItemStatus] = None
    """ Validation result status """
    
    errors: Optional[list] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ValidateMultipleSwitchesResponse(DataClassJsonMixin):
    records: Optional[List[ValidateMultipleSwitchesResponseRecordsItem]] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class GetAccountInfoResponseServiceInfo(DataClassJsonMixin):
    """ Account service information, including brand, service plan and billing plan """
    
    uri: Optional[str] = None
    """ Canonical URI of a service info resource """
    
    billing_plan: Optional[dict] = None
    """ Information on account billing plan """
    
    brand: Optional[dict] = None
    """ Information on account brand """
    
    service_plan: Optional[dict] = None
    """ Information on account service plan """
    
    target_service_plan: Optional[dict] = None
    """ Information on account target service plan """
    
    contracted_country: Optional[dict] = None
    """ Information on the contracted country of account """
    

class GetAccountInfoResponseSetupWizardState(Enum):
    """ Specifies account configuration wizard state (web service setup) """
    
    NotStarted = 'NotStarted'
    Incomplete = 'Incomplete'
    Completed = 'Completed'

class GetAccountInfoResponseSignupInfoSignupStateItem(Enum):
    AccountCreated = 'AccountCreated'
    BillingEntered = 'BillingEntered'
    CreditCardApproved = 'CreditCardApproved'
    AccountConfirmed = 'AccountConfirmed'
    PhoneVerificationRequired = 'PhoneVerificationRequired'
    PhoneVerificationPassed = 'PhoneVerificationPassed'

class GetAccountInfoResponseSignupInfoVerificationReason(Enum):
    CC_Failed = 'CC_Failed'
    Phone_Suspicious = 'Phone_Suspicious'
    CC_Phone_Not_Match = 'CC_Phone_Not_Match'
    AVS_Not_Available = 'AVS_Not_Available'
    MaxMind = 'MaxMind'
    CC_Blacklisted = 'CC_Blacklisted'
    Email_Blacklisted = 'Email_Blacklisted'
    Phone_Blacklisted = 'Phone_Blacklisted'
    Cookie_Blacklisted = 'Cookie_Blacklisted'
    Device_Blacklisted = 'Device_Blacklisted'
    IP_Blacklisted = 'IP_Blacklisted'
    Agent_Instance_Blacklisted = 'Agent_Instance_Blacklisted'
    Charge_Limit = 'Charge_Limit'
    Other_Country = 'Other_Country'
    Unknown = 'Unknown'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class GetAccountInfoResponseSignupInfo(DataClassJsonMixin):
    """ Account sign up data """
    
    tos_accepted: Optional[bool] = False
    signup_state: Optional[List[GetAccountInfoResponseSignupInfoSignupStateItem]] = None
    verification_reason: Optional[GetAccountInfoResponseSignupInfoVerificationReason] = None
    marketing_accepted: Optional[bool] = None
    """ Updates 'Send Marketing Information' flag on web interface """
    

class GetAccountInfoResponseStatus(Enum):
    """ Status of the current account """
    
    Initial = 'Initial'
    Confirmed = 'Confirmed'
    Unconfirmed = 'Unconfirmed'
    Disabled = 'Disabled'

class GetAccountInfoResponseStatusInfoReason(Enum):
    """ Type of suspension """
    
    SuspendedVoluntarily = 'SuspendedVoluntarily'
    SuspendedInvoluntarily = 'SuspendedInvoluntarily'
    UserResumed = 'UserResumed'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class GetAccountInfoResponseStatusInfo(DataClassJsonMixin):
    """ Status information (reason, comment, lifetime). Returned for 'Disabled' status only """
    
    comment: Optional[str] = None
    """ A free-form user comment, describing the status change reason """
    
    reason: Optional[GetAccountInfoResponseStatusInfoReason] = None
    """ Type of suspension """
    
    till: Optional[str] = None
    """ Date until which the account will get deleted. The default value is 30 days since current date """
    

class GetAccountInfoResponseRegionalSettingsTimeFormat(Enum):
    """ Time format setting. The default value is '12h' = ['12h', '24h'] """
    
    OBJECT_12h = '12h'
    OBJECT_24h = '24h'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class GetAccountInfoResponseRegionalSettingsCurrency(DataClassJsonMixin):
    """ Currency information """
    
    id: Optional[str] = None
    """ Internal identifier of a currency """
    
    code: Optional[str] = None
    """ Official code of a currency """
    
    name: Optional[str] = None
    """ Official name of a currency """
    
    symbol: Optional[str] = None
    """ Graphic symbol of a currency """
    
    minor_symbol: Optional[str] = None
    """ Minor graphic symbol of a currency """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class GetAccountInfoResponseRegionalSettings(DataClassJsonMixin):
    """ Account level region data (web service Auto-Receptionist settings) """
    
    home_country: Optional[dict] = None
    """ Extension country information """
    
    timezone: Optional[dict] = None
    """ Extension timezone information """
    
    language: Optional[dict] = None
    """ User interface language data """
    
    greeting_language: Optional[dict] = None
    """ Information on language used for telephony greetings """
    
    formatting_locale: Optional[dict] = None
    """ Formatting language preferences for numbers, dates and currencies """
    
    time_format: Optional[GetAccountInfoResponseRegionalSettingsTimeFormat] = None
    """ Time format setting. The default value is '12h' = ['12h', '24h'] """
    
    currency: Optional[GetAccountInfoResponseRegionalSettingsCurrency] = None
    """ Currency information """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class GetAccountInfoResponse(DataClassJsonMixin):
    id: Optional[int] = None
    """ Internal identifier of an account """
    
    uri: Optional[str] = None
    """ Canonical URI of an account """
    
    bsid: Optional[str] = None
    """ Internal identifier of an account in the billing system """
    
    main_number: Optional[str] = None
    """ Main phone number of the current account """
    
    operator: Optional[dict] = None
    """
    Operator's extension information. This extension will receive all calls and messages intended
    for the operator
    """
    
    partner_id: Optional[str] = None
    """ Additional account identifier, created by partner application and applied on client side """
    
    service_info: Optional[GetAccountInfoResponseServiceInfo] = None
    """ Account service information, including brand, service plan and billing plan """
    
    setup_wizard_state: Optional[GetAccountInfoResponseSetupWizardState] = 'NotStarted'
    """ Specifies account configuration wizard state (web service setup) """
    
    signup_info: Optional[GetAccountInfoResponseSignupInfo] = None
    """ Account sign up data """
    
    status: Optional[GetAccountInfoResponseStatus] = None
    """ Status of the current account """
    
    status_info: Optional[GetAccountInfoResponseStatusInfo] = None
    """ Status information (reason, comment, lifetime). Returned for 'Disabled' status only """
    
    regional_settings: Optional[GetAccountInfoResponseRegionalSettings] = None
    """ Account level region data (web service Auto-Receptionist settings) """
    
    federated: Optional[bool] = None
    """ Specifies whether an account is included into any federation of accounts or not """
    
    outbound_call_prefix: Optional[int] = None
    """
    If outbound call prefix is not specified, or set to null (0), then the parameter is not
    returned; the supported value range is 2-9
    """
    
    cfid: Optional[str] = None
    """
    Customer facing identifier. Returned for accounts with the turned off PBX features. Equals to
    main company number in [E.164](https://www.itu.int/rec/T-REC-E.164-201011-I) (without '+'
    sign)format
    """
    
    limits: Optional[dict] = None
    """ Limits which are effective for the account """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class GetCountryListResponseRecordsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a country """
    
    uri: Optional[str] = None
    """ Canonical URI of a country """
    
    calling_code: Optional[str] = None
    """
    Country calling code defined by ITU-T recommendations
    [E.123](https://www.itu.int/rec/T-REC-E.123-200102-I/en) and
    [E.164](https://www.itu.int/rec/T-REC-E.164-201011-I)
    """
    
    emergency_calling: Optional[bool] = None
    """ Emergency calling feature availability/emergency address requirement indicator """
    
    iso_code: Optional[str] = None
    """
    Country code according to the ISO standard, see [ISO
    3166](https://www.iso.org/iso-3166-country-codes.html)
    """
    
    name: Optional[str] = None
    """ Official name of a country """
    
    number_selling: Optional[bool] = None
    """ Determines whether phone numbers are available for a country """
    
    login_allowed: Optional[bool] = None
    """ Specifies whether login with the phone numbers of this country is enabled or not """
    
    signup_allowed: Optional[bool] = None
    """ Indicates whether signup/billing is allowed for a country """
    
    free_softphone_line: Optional[bool] = None
    """ Specifies if free phone line for softphone is available for a country or not """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class GetCountryListResponse(DataClassJsonMixin):
    """
    Required Properties:
     - navigation
     - paging
     - records
    
    Generated by Python OpenAPI Parser
    """
    
    records: List[GetCountryListResponseRecordsItem]
    """ List of countries with the country data """
    
    navigation: dict
    """ Information on navigation """
    
    paging: dict
    """ Information on paging """
    
    uri: Optional[str] = None
    """ Link to the list of countries supported """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class AssignMultipleDevicesAutomaticLocationUpdates(DataClassJsonMixin):
    enabled_device_ids: Optional[List[str]] = None
    disabled_device_ids: Optional[List[str]] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class AccountPhoneNumbers(DataClassJsonMixin):
    uri: Optional[str] = None
    """ Link to the list of account phone numbers """
    
    records: Optional[list] = None
    """ List of account phone numbers """
    
    navigation: Optional[dict] = None
    """ Information on navigation """
    
    paging: Optional[dict] = None
    """ Information on paging """
    

class CallMonitoringBulkAssignAddedExtensionsItemPermissionsItem(Enum):
    Monitoring = 'Monitoring'
    Monitored = 'Monitored'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CallMonitoringBulkAssignAddedExtensionsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """
    Internal identifier of an extension. Only the following extension types are allowed: User,
    DigitalUser, VirtualUser, FaxUser, Limited
    """
    
    permissions: Optional[List[CallMonitoringBulkAssignAddedExtensionsItemPermissionsItem]] = None
    """
    Set of call monitoring group permissions granted to the specified extension. In order to remove
    the specified extension from a call monitoring group use an empty value
    """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CallMonitoringBulkAssign(DataClassJsonMixin):
    added_extensions: Optional[List[CallMonitoringBulkAssignAddedExtensionsItem]] = None
    updated_extensions: Optional[list] = None
    removed_extensions: Optional[list] = None

class AutomaticLocationUpdatesUserListRecordsItemType(Enum):
    """ User extension type """
    
    User = 'User'
    Limited = 'Limited'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class AutomaticLocationUpdatesUserListRecordsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a device """
    
    full_name: Optional[str] = None
    """ User name """
    
    extension_number: Optional[str] = None
    feature_enabled: Optional[bool] = None
    """ Specifies if Automatic Location Updates feature is enabled """
    
    type: Optional[AutomaticLocationUpdatesUserListRecordsItemType] = None
    """ User extension type """
    
    site: Optional[str] = None
    """ Site data """
    
    department: Optional[str] = None
    """ Department name """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class AutomaticLocationUpdatesUserList(DataClassJsonMixin):
    uri: Optional[str] = None
    """ Link to the users list resource """
    
    records: Optional[List[AutomaticLocationUpdatesUserListRecordsItem]] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class LanguageList(DataClassJsonMixin):
    uri: Optional[str] = None
    """ Canonical URI of the language list resource """
    
    records: Optional[list] = None
    """ Language data """
    
    navigation: Optional[dict] = None
    """ Information on navigation """
    
    paging: Optional[dict] = None
    """ Information on paging """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ParsePhoneNumberRequest(DataClassJsonMixin):
    original_strings: Optional[List[str]] = None
    """
    Phone numbers passed in a string. The maximum value of phone numbers is limited to 64. The
    maximum number of symbols in each phone number in a string is 64
    """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ParsePhoneNumberResponseHomeCountry(DataClassJsonMixin):
    """ Information on a user home country """
    
    id: Optional[str] = None
    """ Internal identifier of a country """
    
    uri: Optional[str] = None
    """ Canonical URI of a country """
    
    calling_code: Optional[str] = None
    """ Country calling code defined by ITU-T recommendations E.123 and E.164, see Calling Codes """
    
    emergency_calling: Optional[bool] = None
    """ Emergency calling feature availability/emergency address requirement indicator """
    
    iso_code: Optional[str] = None
    """ Country code according to the ISO standard, see ISO 3166 """
    
    name: Optional[str] = None
    """ Official name of a country """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ParsePhoneNumberResponsePhoneNumbersItem(DataClassJsonMixin):
    area_code: Optional[str] = None
    """
    Area code of location. The portion of the [E.164](https://www.itu.int/rec/T-REC-E.164-201011-I)
    number that identifies a specific geographic region/numbering area of the national numbering
    plan (NANP); that can be summarized as `NPA-NXX-xxxx` and covers Canada, the United States,
    parts of the Caribbean Sea, and some Atlantic and Pacific islands. See [North American
    Numbering Plan] (https://en.wikipedia.org/wiki/North_American_Numbering_Plan) for details
    """
    
    country: Optional[dict] = None
    """ Information on a country the phone number belongs to """
    
    dialable: Optional[str] = None
    """ Dialing format of a phone number """
    
    e164: Optional[str] = None
    """ Phone number [E.164](https://www.itu.int/rec/T-REC-E.164-201011-I) format """
    
    formatted_international: Optional[str] = None
    """ International format of a phone number """
    
    formatted_national: Optional[str] = None
    """ Domestic format of a phone number """
    
    original_string: Optional[str] = None
    """ One of the numbers to be parsed, passed as a string in response """
    
    special: Optional[bool] = None
    """ 'True' if the number is in a special format (for example N11 code) """
    
    normalized: Optional[str] = None
    """
    Phone number [E.164](https://www.itu.int/rec/T-REC-E.164-201011-I) format without plus sign
    ('+')
    """
    
    toll_free: Optional[bool] = None
    """ Specifies if a phone number is toll free or not """
    
    sub_address: Optional[str] = None
    """
    Sub-Address. The portion of the number that identifies a subscriber into the subscriber
    internal (non-public) network.
    """
    
    subscriber_number: Optional[str] = None
    """
    Subscriber number. The portion of the [E.164](https://www.itu.int/rec/T-REC-E.164-201011-I)
    number that identifies a subscriber in a network or numbering area.
    """
    
    dtmf_postfix: Optional[str] = None
    """ DTMF (Dual Tone Multi-Frequency) postfix """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ParsePhoneNumberResponse(DataClassJsonMixin):
    """
    Required Properties:
     - home_country
     - phone_numbers
    
    Generated by Python OpenAPI Parser
    """
    
    home_country: ParsePhoneNumberResponseHomeCountry
    """ Information on a user home country """
    
    phone_numbers: List[ParsePhoneNumberResponsePhoneNumbersItem]
    """ Parsed phone numbers data """
    
    uri: Optional[str] = None
    """ Canonical URI of a resource """
    

class GetDeviceInfoResponseType(Enum):
    """ Device type """
    
    BLA = 'BLA'
    SoftPhone = 'SoftPhone'
    OtherPhone = 'OtherPhone'
    HardPhone = 'HardPhone'
    WebPhone = 'WebPhone'
    Paging = 'Paging'

class GetDeviceInfoResponseStatus(Enum):
    """ Device status """
    
    Offline = 'Offline'
    Online = 'Online'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class GetDeviceInfoResponseModelAddonsItem(DataClassJsonMixin):
    id: Optional[str] = None
    name: Optional[str] = None
    count: Optional[int] = None

class GetDeviceInfoResponseModelFeaturesItem(Enum):
    BLA = 'BLA'
    CommonPhone = 'CommonPhone'
    Intercom = 'Intercom'
    Paging = 'Paging'
    HELD = 'HELD'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class GetDeviceInfoResponseModel(DataClassJsonMixin):
    """ HardPhone model information """
    
    id: Optional[str] = None
    """ Internal identifier of a HardPhone device model """
    
    name: Optional[str] = None
    """ Device name """
    
    addons: Optional[List[GetDeviceInfoResponseModelAddonsItem]] = None
    """ Addons description """
    
    features: Optional[List[GetDeviceInfoResponseModelFeaturesItem]] = None
    """ Device feature or multiple features supported """
    
    line_count: Optional[int] = None
    """ Max supported count of phone lines """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class GetDeviceInfoResponseExtension(DataClassJsonMixin):
    """ This attribute can be omitted for unassigned devices """
    
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
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class GetDeviceInfoResponseEmergencyAddress(DataClassJsonMixin):
    customer_name: Optional[str] = None
    """ Name of a customer """
    
    street: Optional[str] = None
    """ Street address, line 1 - street address, P.O. box, company name, c/o """
    
    street2: Optional[str] = None
    """ Street address, line 2 - apartment, suite, unit, building, floor, etc. """
    
    city: Optional[str] = None
    """ City name """
    
    zip: Optional[str] = None
    """ Zip code """
    
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
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class GetDeviceInfoResponseEmergencyLocation(DataClassJsonMixin):
    """ Company emergency response location details """
    
    id: Optional[str] = None
    """ Internal identifier of the emergency response location """
    
    name: Optional[str] = None
    """ Location name """
    

class GetDeviceInfoResponseEmergencyAddressStatus(Enum):
    """ Emergency address status """
    
    Valid = 'Valid'
    Invalid = 'Invalid'

class GetDeviceInfoResponseEmergencySyncStatus(Enum):
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

class GetDeviceInfoResponseEmergencyAddressEditableStatus(Enum):
    """
    Ability to register new emergency address for a phone line using devices sharing this line or
    only main device (line owner)
    
    Generated by Python OpenAPI Parser
    """
    
    MainDevice = 'MainDevice'
    AnyDevice = 'AnyDevice'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class GetDeviceInfoResponseEmergency(DataClassJsonMixin):
    """ Device emergency settings """
    
    address: Optional[GetDeviceInfoResponseEmergencyAddress] = None
    location: Optional[GetDeviceInfoResponseEmergencyLocation] = None
    """ Company emergency response location details """
    
    out_of_country: Optional[bool] = None
    """ Specifies if emergency address is out of country """
    
    address_status: Optional[GetDeviceInfoResponseEmergencyAddressStatus] = None
    """ Emergency address status """
    
    sync_status: Optional[GetDeviceInfoResponseEmergencySyncStatus] = None
    """
    Resulting status of emergency address synchronization. Returned if `syncEmergencyAddress`
    parameter is set to 'True'
    """
    
    address_editable_status: Optional[GetDeviceInfoResponseEmergencyAddressEditableStatus] = None
    """
    Ability to register new emergency address for a phone line using devices sharing this line or
    only main device (line owner)
    """
    

class GetDeviceInfoResponseEmergencyServiceAddressSyncStatus(Enum):
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

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class GetDeviceInfoResponseEmergencyServiceAddress(DataClassJsonMixin):
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
    
    sync_status: Optional[GetDeviceInfoResponseEmergencyServiceAddressSyncStatus] = None
    """
    Resulting status of emergency address synchronization. Returned if `syncEmergencyAddress`
    parameter is set to 'True'
    """
    
    additional_customer_name: Optional[str] = None
    """
    Name of an additional contact person. Should be specified for countries except the US, Canada,
    the UK and Australia.
    """
    
    customer_email: Optional[str] = None
    """
    Email of a primary contact person (receiver). Should be specified for countries except the US,
    Canada, the UK and Australia.
    """
    
    additional_customer_email: Optional[str] = None
    """
    Email of an additional contact person. Should be specified for countries except the US, Canada,
    the UK and Australia.
    """
    
    customer_phone: Optional[str] = None
    """
    Phone number of a primary contact person (receiver). Should be specified for countries except
    the US, Canada, the UK and Australia
    """
    
    additional_customer_phone: Optional[str] = None
    """
    Phone number of an additional contact person. Should be specified for countries except the US,
    Canada, the UK & Australia.
    """
    
    tax_id: Optional[str] = None
    """ Internal identifier of a tax """
    

class GetDeviceInfoResponsePhoneLinesItemLineType(Enum):
    """ Type of phone line """
    
    Standalone = 'Standalone'
    StandaloneFree = 'StandaloneFree'
    BlaPrimary = 'BlaPrimary'
    BlaSecondary = 'BlaSecondary'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class GetDeviceInfoResponsePhoneLinesItemPhoneInfoCountry(DataClassJsonMixin):
    """ Brief information on a phone number country """
    
    id: Optional[str] = None
    """ Internal identifier of a home country """
    
    uri: Optional[str] = None
    """ Canonical URI of a home country """
    
    name: Optional[str] = None
    """ Official name of a home country """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class GetDeviceInfoResponsePhoneLinesItemPhoneInfoExtension(DataClassJsonMixin):
    """
    Information on the extension, to which the phone number is assigned. Returned only for the
    request of Account phone number list
    
    Generated by Python OpenAPI Parser
    """
    
    id: Optional[str] = None
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
    

class GetDeviceInfoResponsePhoneLinesItemPhoneInfoPaymentType(Enum):
    """
    Payment type. 'External' is returned for forwarded numbers which are not terminated in the
    RingCentral phone system
    
    Generated by Python OpenAPI Parser
    """
    
    External = 'External'
    TollFree = 'TollFree'
    Local = 'Local'

class GetDeviceInfoResponsePhoneLinesItemPhoneInfoType(Enum):
    """ Phone number type """
    
    VoiceFax = 'VoiceFax'
    FaxOnly = 'FaxOnly'
    VoiceOnly = 'VoiceOnly'

class GetDeviceInfoResponsePhoneLinesItemPhoneInfoUsageType(Enum):
    """ Usage type of the phone number """
    
    MainCompanyNumber = 'MainCompanyNumber'
    AdditionalCompanyNumber = 'AdditionalCompanyNumber'
    CompanyNumber = 'CompanyNumber'
    DirectNumber = 'DirectNumber'
    CompanyFaxNumber = 'CompanyFaxNumber'
    ForwardedNumber = 'ForwardedNumber'
    ForwardedCompanyNumber = 'ForwardedCompanyNumber'
    ContactCenterNumber = 'ContactCenterNumber'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class GetDeviceInfoResponsePhoneLinesItemPhoneInfo(DataClassJsonMixin):
    """ Phone number information """
    
    id: Optional[int] = None
    """ Internal identifier of a phone number """
    
    country: Optional[GetDeviceInfoResponsePhoneLinesItemPhoneInfoCountry] = None
    """ Brief information on a phone number country """
    
    extension: Optional[GetDeviceInfoResponsePhoneLinesItemPhoneInfoExtension] = None
    """
    Information on the extension, to which the phone number is assigned. Returned only for the
    request of Account phone number list
    """
    
    label: Optional[str] = None
    """ Custom user name of a phone number, if any """
    
    location: Optional[str] = None
    """ Location (City, State). Filled for local US numbers """
    
    payment_type: Optional[GetDeviceInfoResponsePhoneLinesItemPhoneInfoPaymentType] = None
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
    
    type: Optional[GetDeviceInfoResponsePhoneLinesItemPhoneInfoType] = None
    """ Phone number type """
    
    usage_type: Optional[GetDeviceInfoResponsePhoneLinesItemPhoneInfoUsageType] = None
    """ Usage type of the phone number """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class GetDeviceInfoResponsePhoneLinesItemEmergencyAddress(DataClassJsonMixin):
    required: Optional[bool] = None
    """ 'True' if specifying of emergency address is required """
    
    local_only: Optional[bool] = None
    """ 'True' if only local emergency address can be specified """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class GetDeviceInfoResponsePhoneLinesItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a phone line """
    
    line_type: Optional[GetDeviceInfoResponsePhoneLinesItemLineType] = None
    """ Type of phone line """
    
    phone_info: Optional[GetDeviceInfoResponsePhoneLinesItemPhoneInfo] = None
    """ Phone number information """
    
    emergency_address: Optional[GetDeviceInfoResponsePhoneLinesItemEmergencyAddress] = None

class GetDeviceInfoResponseShippingStatus(Enum):
    """
    Shipping status of the order item. It is set to 'Initial' when the order is submitted. Then it
    is changed to 'Accepted' when a distributor starts processing the order. Finally it is changed
    to Shipped which means that distributor has shipped the device.
    
    Generated by Python OpenAPI Parser
    """
    
    Initial = 'Initial'
    Accepted = 'Accepted'
    Shipped = 'Shipped'
    WonTShip = "Won't ship"

class GetDeviceInfoResponseShippingMethodId(Enum):
    """ Method identifier. The default value is 1 (Ground) """
    
    OBJECT_1 = '1'
    OBJECT_2 = '2'
    OBJECT_3 = '3'

class GetDeviceInfoResponseShippingMethodName(Enum):
    """ Method name, corresponding to the identifier """
    
    Ground = 'Ground'
    OBJECT_2_Day = '2 Day'
    Overnight = 'Overnight'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class GetDeviceInfoResponseShippingMethod(DataClassJsonMixin):
    """ Shipping method information """
    
    id: Optional[GetDeviceInfoResponseShippingMethodId] = None
    """ Method identifier. The default value is 1 (Ground) """
    
    name: Optional[GetDeviceInfoResponseShippingMethodName] = None
    """ Method name, corresponding to the identifier """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class GetDeviceInfoResponseShippingAddress(DataClassJsonMixin):
    """
    Shipping address for the order. If it coincides with the Emergency Service Address, then can be
    omitted. By default the same value as the emergencyServiceAddress. Multiple addresses can be
    specified; in case an order contains several devices, they can be delivered to different
    addresses
    
    Generated by Python OpenAPI Parser
    """
    
    customer_name: Optional[str] = None
    """ Name of a primary contact person (receiver) """
    
    additional_customer_name: Optional[str] = None
    """
    Name of an additional contact person. Should be specified for countries except the US, Canada,
    the UK and Australia.
    """
    
    customer_email: Optional[str] = None
    """
    Email of a primary contact person (receiver). Should be specified for countries except the US,
    Canada, the UK and Australia.
    """
    
    additional_customer_email: Optional[str] = None
    """
    Email of an additional contact person. Should be specified for countries except the US, Canada,
    the UK and Australia.
    """
    
    customer_phone: Optional[str] = None
    """
    Phone number of a primary contact person (receiver). Should be specified for countries except
    the US, Canada, the UK and Australia
    """
    
    additional_customer_phone: Optional[str] = None
    """
    Phone number of an additional contact person. Should be specified for countries except the US,
    Canada, the UK & Australia.
    """
    
    street: Optional[str] = None
    """ Street address, line 1 - street address, P.O. box, company name, c/o """
    
    street2: Optional[str] = None
    """ Street address, line 2 - apartment, suite, unit, building, floor, etc. """
    
    city: Optional[str] = None
    """ City name """
    
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
    
    zip: Optional[str] = None
    """ Zip code """
    
    tax_id: Optional[str] = None
    """
    National taxpayer identification number. Should be specified for Brazil (CNPJ/CPF number) and
    Argentina (CUIT number).
    """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class GetDeviceInfoResponseShipping(DataClassJsonMixin):
    """
    Shipping information, according to which devices (in case of HardPhone ) or e911 stickers (in
    case of SoftPhone and OtherPhone ) will be delivered to the customer
    
    Generated by Python OpenAPI Parser
    """
    
    status: Optional[GetDeviceInfoResponseShippingStatus] = None
    """
    Shipping status of the order item. It is set to 'Initial' when the order is submitted. Then it
    is changed to 'Accepted' when a distributor starts processing the order. Finally it is changed
    to Shipped which means that distributor has shipped the device.
    """
    
    carrier: Optional[str] = None
    """ Shipping carrier name. Appears only if the device status is 'Shipped' """
    
    tracking_number: Optional[str] = None
    """ Carrier-specific tracking number. Appears only if the device status is 'Shipped' """
    
    method: Optional[GetDeviceInfoResponseShippingMethod] = None
    """ Shipping method information """
    
    address: Optional[GetDeviceInfoResponseShippingAddress] = None
    """
    Shipping address for the order. If it coincides with the Emergency Service Address, then can be
    omitted. By default the same value as the emergencyServiceAddress. Multiple addresses can be
    specified; in case an order contains several devices, they can be delivered to different
    addresses
    """
    

class GetDeviceInfoResponseLinePooling(Enum):
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
class GetDeviceInfoResponseBillingStatementChargesItem(DataClassJsonMixin):
    description: Optional[str] = None
    amount: Optional[float] = None
    feature: Optional[str] = None
    free_service_credit: Optional[float] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class GetDeviceInfoResponseBillingStatementFeesItem(DataClassJsonMixin):
    description: Optional[str] = None
    amount: Optional[float] = None
    free_service_credit: Optional[float] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class GetDeviceInfoResponseBillingStatement(DataClassJsonMixin):
    """
    Billing information. Returned for device update request if `prestatement` query parameter is
    set to 'true'
    
    Generated by Python OpenAPI Parser
    """
    
    currency: Optional[str] = None
    """ Currency code complying with [ISO-4217](https://en.wikipedia.org/wiki/ISO_4217) standard """
    
    charges: Optional[List[GetDeviceInfoResponseBillingStatementChargesItem]] = None
    fees: Optional[List[GetDeviceInfoResponseBillingStatementFeesItem]] = None
    total_charged: Optional[float] = None
    total_charges: Optional[float] = None
    total_fees: Optional[float] = None
    subtotal: Optional[float] = None
    total_free_service_credit: Optional[float] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class GetDeviceInfoResponse(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a device """
    
    uri: Optional[str] = None
    """ Canonical URI of a device """
    
    sku: Optional[str] = None
    """
    Device identification number (stock keeping unit) in the format TP-ID [-AT-AC], where TP is
    device type (HP for RC HardPhone, DV for all other devices including softphone); ID - device
    model ID; AT -addon type ID; AC - addon count (if any). For example 'HP-56-2-2'
    """
    
    type: Optional[GetDeviceInfoResponseType] = 'HardPhone'
    """ Device type """
    
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
    
    status: Optional[GetDeviceInfoResponseStatus] = None
    """ Device status """
    
    computer_name: Optional[str] = None
    """ PC name for softphone """
    
    model: Optional[GetDeviceInfoResponseModel] = None
    """ HardPhone model information """
    
    extension: Optional[GetDeviceInfoResponseExtension] = None
    """ This attribute can be omitted for unassigned devices """
    
    emergency: Optional[GetDeviceInfoResponseEmergency] = None
    """ Device emergency settings """
    
    emergency_service_address: Optional[GetDeviceInfoResponseEmergencyServiceAddress] = None
    """
    Address for emergency cases. The same emergency address is assigned to all the numbers of one
    device
    """
    
    phone_lines: Optional[List[GetDeviceInfoResponsePhoneLinesItem]] = None
    """ Phone lines information """
    
    shipping: Optional[GetDeviceInfoResponseShipping] = None
    """
    Shipping information, according to which devices (in case of HardPhone ) or e911 stickers (in
    case of SoftPhone and OtherPhone ) will be delivered to the customer
    """
    
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
    
    in_company_net: Optional[bool] = None
    """
    Network location status. 'True' if the device is located in the configured corporate network
    (On-Net); 'False' for Off-Net location. Parameter is not returned if
    `EmergencyAddressAutoUpdate` feature is not enabled for the account/user, or if device network
    location is not determined
    """
    
    site: Optional[dict] = None
    """ Site data """
    
    last_location_report_time: Optional[str] = None
    """
    Datetime of receiving last location report in [ISO
    8601](https://en.wikipedia.org/wiki/ISO_8601) format including timezone, for example
    *2016-03-10T18:07:52.534Z
    """
    
    line_pooling: Optional[GetDeviceInfoResponseLinePooling] = None
    """
    Pooling type of a deviceHost - device with standalone paid phone line which can be linked to
    Glip/Softphone instanceGuest - device with a linked phone lineNone - device without a phone
    line or with specific line (free, BLA, etc.) = ['Host', 'Guest', 'None']
    """
    
    billing_statement: Optional[GetDeviceInfoResponseBillingStatement] = None
    """
    Billing information. Returned for device update request if `prestatement` query parameter is
    set to 'true'
    """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class AccountDeviceUpdateEmergencyServiceAddress(DataClassJsonMixin):
    """
    Address for emergency cases. The same emergency address is assigned to all numbers of a single
    device. If the emergency address is also specified in `emergency` resource, then this value is
    ignored
    
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
    
    country: Optional[str] = None
    """ Country name """
    
    country_id: Optional[str] = None
    """ Internal identifier of a country """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class AccountDeviceUpdateExtension(DataClassJsonMixin):
    """ Information on extension that the device is assigned to """
    
    id: Optional[str] = None
    """ Internal identifier of an extension """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class AccountDeviceUpdatePhoneLinesPhoneLinesItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a phone number """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class AccountDeviceUpdatePhoneLines(DataClassJsonMixin):
    """ Information on phone lines added to a device """
    
    phone_lines: Optional[List[AccountDeviceUpdatePhoneLinesPhoneLinesItem]] = None
    """ Information on phone lines added to a device """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class AccountDeviceUpdate(DataClassJsonMixin):
    emergency_service_address: Optional[AccountDeviceUpdateEmergencyServiceAddress] = None
    """
    Address for emergency cases. The same emergency address is assigned to all numbers of a single
    device. If the emergency address is also specified in `emergency` resource, then this value is
    ignored
    """
    
    emergency: Optional[dict] = None
    """ Device emergency settings """
    
    extension: Optional[AccountDeviceUpdateExtension] = None
    """ Information on extension that the device is assigned to """
    
    phone_lines: Optional[AccountDeviceUpdatePhoneLines] = None
    """ Information on phone lines added to a device """
    
    use_as_common_phone: Optional[bool] = None
    """
    Supported only for devices assigned to Limited extensions. If true, enables users to log in to
    this phone as a common phone.
    """
    

class GetExtensionDevicesResponseRecordsItemType(Enum):
    """ Device type """
    
    SoftPhone = 'SoftPhone'
    OtherPhone = 'OtherPhone'
    HardPhone = 'HardPhone'
    Paging = 'Paging'

class GetExtensionDevicesResponseRecordsItemStatus(Enum):
    """ Device status """
    
    Offline = 'Offline'
    Online = 'Online'

class GetExtensionDevicesResponseRecordsItemLinePooling(Enum):
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
class GetExtensionDevicesResponseRecordsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a device """
    
    uri: Optional[str] = None
    """ Canonical URI of a device """
    
    sku: Optional[str] = None
    """
    Device identification number (stock keeping unit) in the format TP-ID [-AT-AC], where TP is
    device type (HP for RC HardPhone, DV for all other devices including softphone); ID - device
    model ID; AT -addon type ID; AC - addon count (if any). For example 'HP-56-2-2'
    """
    
    type: Optional[GetExtensionDevicesResponseRecordsItemType] = 'HardPhone'
    """ Device type """
    
    name: Optional[str] = None
    """
    Device name. Mandatory if ordering SoftPhone or OtherPhone. Optional for HardPhone. If not
    specified for HardPhone, then device model name is used as device name
    """
    
    status: Optional[GetExtensionDevicesResponseRecordsItemStatus] = None
    """ Device status """
    
    serial: Optional[str] = None
    """
    Serial number for HardPhone (is returned only when the phone is shipped and provisioned);
    endpoint_id for softphone and mobile applications
    """
    
    computer_name: Optional[str] = None
    """ PC name for softphone """
    
    model: Optional[dict] = None
    """ HardPhone model information """
    
    extension: Optional[dict] = None
    """ This attribute can be omitted for unassigned devices """
    
    emergency_service_address: Optional[dict] = None
    """
    Address for emergency cases. The same emergency address is assigned to all the numbers of one
    device
    """
    
    emergency: Optional[dict] = None
    """ Device emergency settings """
    
    phone_lines: Optional[list] = None
    """ Phone lines information """
    
    shipping: Optional[dict] = None
    """
    Shipping information, according to which devices (in case of HardPhone ) or e911 stickers (in
    case of SoftPhone and OtherPhone ) will be delivered to the customer
    """
    
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
    
    line_pooling: Optional[GetExtensionDevicesResponseRecordsItemLinePooling] = None
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
    
    site: Optional[dict] = None
    """ Site data """
    
    last_location_report_time: Optional[str] = None
    """
    Datetime of receiving last location report in [ISO
    8601](https://en.wikipedia.org/wiki/ISO_8601) format including timezone, for example
    *2016-03-10T18:07:52.534Z
    """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class GetExtensionDevicesResponseNavigationFirstPage(DataClassJsonMixin):
    """ Canonical URI for the first page of the list """
    
    uri: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class GetExtensionDevicesResponseNavigation(DataClassJsonMixin):
    """ Information on navigation """
    
    first_page: Optional[GetExtensionDevicesResponseNavigationFirstPage] = None
    """ Canonical URI for the first page of the list """
    
    next_page: Optional[dict] = None
    """ Canonical URI for the next page of the list """
    
    previous_page: Optional[dict] = None
    """ Canonical URI for the previous page of the list """
    
    last_page: Optional[dict] = None
    """ Canonical URI for the last page of the list """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class GetExtensionDevicesResponsePaging(DataClassJsonMixin):
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
class GetExtensionDevicesResponse(DataClassJsonMixin):
    """
    Required Properties:
     - navigation
     - paging
     - records
    
    Generated by Python OpenAPI Parser
    """
    
    records: List[GetExtensionDevicesResponseRecordsItem]
    """ List of extension devices """
    
    navigation: GetExtensionDevicesResponseNavigation
    """ Information on navigation """
    
    paging: GetExtensionDevicesResponsePaging
    """ Information on paging """
    
    uri: Optional[str] = None
    """ Link to the list of extension devices """
    

class UserPatch_OperationsItemOp(Enum):
    Add = 'add'
    Replace = 'replace'
    Remove = 'remove'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UserPatch_OperationsItem(DataClassJsonMixin):
    """
    Required Properties:
     - op
    
    Generated by Python OpenAPI Parser
    """
    
    op: UserPatch_OperationsItemOp
    path: Optional[str] = None
    value: Optional[str] = None
    """ corresponding 'value' of that field specified by 'path' """
    

class UserPatchSchemasItem(Enum):
    UrnIetfParamsScimApiMessages_2_0_PatchOp = 'urn:ietf:params:scim:api:messages:2.0:PatchOp'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UserPatch(DataClassJsonMixin):
    """
    Required Properties:
     - operations
     - schemas
    
    Generated by Python OpenAPI Parser
    """
    
    operations: List[UserPatch_OperationsItem]
    """ patch operations list """
    
    schemas: List[UserPatchSchemasItem]

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ServiceProviderConfigAuthenticationSchemesItem(DataClassJsonMixin):
    description: Optional[str] = None
    documentation_uri: Optional[str] = None
    name: Optional[str] = None
    spec_uri: Optional[str] = None
    primary: Optional[bool] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ServiceProviderConfigBulk(DataClassJsonMixin):
    max_operations: Optional[int] = None
    max_payload_size: Optional[int] = None
    supported: Optional[bool] = False

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ServiceProviderConfigChangePassword(DataClassJsonMixin):
    supported: Optional[bool] = False

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ServiceProviderConfigFilter(DataClassJsonMixin):
    max_results: Optional[int] = None
    supported: Optional[bool] = False

class ServiceProviderConfigSchemasItem(Enum):
    UrnIetfParamsScimSchemasCore_2_0_ServiceProviderConfig = 'urn:ietf:params:scim:schemas:core:2.0:ServiceProviderConfig'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ServiceProviderConfig(DataClassJsonMixin):
    authentication_schemes: Optional[List[ServiceProviderConfigAuthenticationSchemesItem]] = None
    bulk: Optional[ServiceProviderConfigBulk] = None
    change_password: Optional[ServiceProviderConfigChangePassword] = None
    filter: Optional[ServiceProviderConfigFilter] = None
    schemas: Optional[List[ServiceProviderConfigSchemasItem]] = None

class UserSearchResponse_ResourcesItemAddressesItemType(Enum):
    Work = 'work'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UserSearchResponse_ResourcesItemAddressesItem(DataClassJsonMixin):
    """
    Required Properties:
     - type
    
    Generated by Python OpenAPI Parser
    """
    
    type: UserSearchResponse_ResourcesItemAddressesItemType
    country: Optional[str] = None
    locality: Optional[str] = None
    postal_code: Optional[str] = None
    region: Optional[str] = None
    street_address: Optional[str] = None

class UserSearchResponse_ResourcesItemEmailsItemType(Enum):
    Work = 'work'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UserSearchResponse_ResourcesItemEmailsItem(DataClassJsonMixin):
    """
    Required Properties:
     - type
     - value
    
    Generated by Python OpenAPI Parser
    """
    
    type: UserSearchResponse_ResourcesItemEmailsItemType
    value: str

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UserSearchResponse_ResourcesItemName(DataClassJsonMixin):
    """
    Required Properties:
     - family_name
     - given_name
    
    Generated by Python OpenAPI Parser
    """
    
    family_name: str
    given_name: str

class UserSearchResponse_ResourcesItemPhoneNumbersItemType(Enum):
    Work = 'work'
    Mobile = 'mobile'
    Other = 'other'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UserSearchResponse_ResourcesItemPhoneNumbersItem(DataClassJsonMixin):
    """
    Required Properties:
     - type
     - value
    
    Generated by Python OpenAPI Parser
    """
    
    type: UserSearchResponse_ResourcesItemPhoneNumbersItemType
    value: str

class UserSearchResponse_ResourcesItemPhotosItemType(Enum):
    Photo = 'photo'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UserSearchResponse_ResourcesItemPhotosItem(DataClassJsonMixin):
    """
    Required Properties:
     - type
     - value
    
    Generated by Python OpenAPI Parser
    """
    
    type: UserSearchResponse_ResourcesItemPhotosItemType
    value: str

class UserSearchResponse_ResourcesItemSchemasItem(Enum):
    UrnIetfParamsScimSchemasCore_2_0_User = 'urn:ietf:params:scim:schemas:core:2.0:User'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UserSearchResponse_ResourcesItemUrnIetfParamsScimSchemasExtensionEnterprise_2_0_User(DataClassJsonMixin):
    department: Optional[str] = None

class UserSearchResponse_ResourcesItemMetaResourceType(Enum):
    User = 'User'
    Group = 'Group'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UserSearchResponse_ResourcesItemMeta(DataClassJsonMixin):
    """ resource metadata """
    
    created: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    last_modified: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    location: Optional[str] = None
    """ resource location URI """
    
    resource_type: Optional[UserSearchResponse_ResourcesItemMetaResourceType] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UserSearchResponse_ResourcesItem(DataClassJsonMixin):
    """
    Required Properties:
     - emails
     - name
     - schemas
     - user_name
    
    Generated by Python OpenAPI Parser
    """
    
    emails: List[UserSearchResponse_ResourcesItemEmailsItem]
    name: UserSearchResponse_ResourcesItemName
    schemas: List[UserSearchResponse_ResourcesItemSchemasItem]
    user_name: str
    """ MUST be same as work type email address """
    
    active: Optional[bool] = False
    """ user status """
    
    addresses: Optional[List[UserSearchResponse_ResourcesItemAddressesItem]] = None
    external_id: Optional[str] = None
    """ external unique resource id defined by provisioning client """
    
    id: Optional[str] = None
    """ unique resource id defined by RingCentral """
    
    phone_numbers: Optional[List[UserSearchResponse_ResourcesItemPhoneNumbersItem]] = None
    photos: Optional[List[UserSearchResponse_ResourcesItemPhotosItem]] = None
    urn_ietf_params_scim_schemas_extension_enterprise_2_0_user: Optional[UserSearchResponse_ResourcesItemUrnIetfParamsScimSchemasExtensionEnterprise_2_0_User] = None
    meta: Optional[UserSearchResponse_ResourcesItemMeta] = None
    """ resource metadata """
    

class UserSearchResponseSchemasItem(Enum):
    UrnIetfParamsScimApiMessages_2_0_ListResponse = 'urn:ietf:params:scim:api:messages:2.0:ListResponse'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UserSearchResponse(DataClassJsonMixin):
    resources: Optional[List[UserSearchResponse_ResourcesItem]] = None
    """ user list """
    
    items_per_page: Optional[int] = None
    schemas: Optional[List[UserSearchResponseSchemasItem]] = None
    start_index: Optional[int] = None
    total_results: Optional[int] = None

class ScimErrorResponseSchemasItem(Enum):
    UrnIetfParamsScimApiMessages_2_0_Error = 'urn:ietf:params:scim:api:messages:2.0:Error'

class ScimErrorResponseScimType(Enum):
    """ bad request type when status code is 400 """
    
    Uniqueness = 'uniqueness'
    TooMany = 'tooMany'
    Mutability = 'mutability'
    Sensitive = 'sensitive'
    InvalidSyntax = 'invalidSyntax'
    InvalidFilter = 'invalidFilter'
    InvalidPath = 'invalidPath'
    InvalidValue = 'invalidValue'
    InvalidVers = 'invalidVers'
    NoTarget = 'noTarget'
