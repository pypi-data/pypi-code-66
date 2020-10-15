from ._15 import *

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CallParkPartyResponseOwner(DataClassJsonMixin):
    """ Data on a call owner """
    
    account_id: Optional[str] = None
    """ Internal identifier of an account that monitors a call """
    
    extension_id: Optional[str] = None
    """ Internal identifier of an extension that monitors a call """
    

class CallParkPartyResponseDirection(Enum):
    """ Direction of a call """
    
    Inbound = 'Inbound'
    Outbound = 'Outbound'

class CallParkPartyResponseConferenceRole(Enum):
    """ A party's role in the conference scenarios. For calls of 'Conference' type only """
    
    Host = 'Host'
    Participant = 'Participant'

class CallParkPartyResponseRingOutRole(Enum):
    """ A party's role in 'Ring Me'/'RingOut' scenarios. For calls of 'Ringout' type only """
    
    Initiator = 'Initiator'
    Target = 'Target'

class CallParkPartyResponseRingMeRole(Enum):
    """ A party's role in 'Ring Me'/'RingOut' scenarios. For calls of 'Ringme' type only """
    
    Initiator = 'Initiator'
    Target = 'Target'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CallParkPartyResponseRecordingsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a Recording resource """
    
    active: Optional[bool] = None
    """ True if the recording is active. False if the recording is paused. """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CallParkPartyResponse(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a party """
    
    status: Optional[CallParkPartyResponseStatus] = None
    """ Status data of a call session """
    
    muted: Optional[bool] = None
    """
    Specifies if a call participant is muted or not. **Note:** If a call is also controlled via
    Hard phone or RingCentral App (not only through the API by calling call control methods) then
    it cannot be fully muted/unmuted via API only, in this case the action should be duplicated via
    Hard phone/RC App interfaces
    """
    
    stand_alone: Optional[bool] = None
    """
    If 'True' then the party is not connected to a session voice conference, 'False' means the
    party is connected to other parties in a session
    """
    
    park: Optional[CallParkPartyResponsePark] = None
    """ Call park information """
    
    from_: Optional[CallParkPartyResponseFrom] = field(metadata=config(field_name='from'), default=None)
    """ Data on a calling party """
    
    to: Optional[CallParkPartyResponseTo] = None
    """ Data on a called party """
    
    owner: Optional[CallParkPartyResponseOwner] = None
    """ Data on a call owner """
    
    direction: Optional[CallParkPartyResponseDirection] = None
    """ Direction of a call """
    
    conference_role: Optional[CallParkPartyResponseConferenceRole] = None
    """ A party's role in the conference scenarios. For calls of 'Conference' type only """
    
    ring_out_role: Optional[CallParkPartyResponseRingOutRole] = None
    """ A party's role in 'Ring Me'/'RingOut' scenarios. For calls of 'Ringout' type only """
    
    ring_me_role: Optional[CallParkPartyResponseRingMeRole] = None
    """ A party's role in 'Ring Me'/'RingOut' scenarios. For calls of 'Ringme' type only """
    
    recordings: Optional[List[CallParkPartyResponseRecordingsItem]] = None
    """ Active recordings list """
    

class ReadCallPartyStatusResponseStatusCode(Enum):
    """ Status code of a call """
    
    Setup = 'Setup'
    Proceeding = 'Proceeding'
    Answered = 'Answered'
    Disconnected = 'Disconnected'
    Gone = 'Gone'
    Parked = 'Parked'
    Hold = 'Hold'
    VoiceMail = 'VoiceMail'
    FaxReceive = 'FaxReceive'
    VoiceMailScreening = 'VoiceMailScreening'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadCallPartyStatusResponseStatusPeerId(DataClassJsonMixin):
    """ Peer session / party data.'Gone'state only """
    
    session_id: Optional[str] = None
    telephony_session_id: Optional[str] = None
    party_id: Optional[str] = None

class ReadCallPartyStatusResponseStatusReason(Enum):
    """ Reason of call termination. For 'Disconnected' code only """
    
    Pickup = 'Pickup'
    Supervising = 'Supervising'
    TakeOver = 'TakeOver'
    Timeout = 'Timeout'
    BlindTransfer = 'BlindTransfer'
    RccTransfer = 'RccTransfer'
    AttendedTransfer = 'AttendedTransfer'
    CallerInputRedirect = 'CallerInputRedirect'
    CallFlip = 'CallFlip'
    ParkLocation = 'ParkLocation'
    DtmfTransfer = 'DtmfTransfer'
    AgentAnswered = 'AgentAnswered'
    AgentDropped = 'AgentDropped'
    Rejected = 'Rejected'
    Cancelled = 'Cancelled'
    InternalError = 'InternalError'
    NoAnswer = 'NoAnswer'
    TargetBusy = 'TargetBusy'
    InvalidNumber = 'InvalidNumber'
    InternationalDisabled = 'InternationalDisabled'
    DestinationBlocked = 'DestinationBlocked'
    NotEnoughFunds = 'NotEnoughFunds'
    NoSuchUser = 'NoSuchUser'
    CallPark = 'CallPark'
    CallRedirected = 'CallRedirected'
    CallReplied = 'CallReplied'
    CallSwitch = 'CallSwitch'
    CallFinished = 'CallFinished'
    CallDropped = 'CallDropped'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadCallPartyStatusResponseStatus(DataClassJsonMixin):
    """ Status data of a call session """
    
    code: Optional[ReadCallPartyStatusResponseStatusCode] = None
    """ Status code of a call """
    
    peer_id: Optional[ReadCallPartyStatusResponseStatusPeerId] = None
    """ Peer session / party data.'Gone'state only """
    
    reason: Optional[ReadCallPartyStatusResponseStatusReason] = None
    """ Reason of call termination. For 'Disconnected' code only """
    
    description: Optional[str] = None
    """ Optional message """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadCallPartyStatusResponsePark(DataClassJsonMixin):
    """ Call park information """
    
    id: Optional[str] = None
    """ Call park identifier """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadCallPartyStatusResponseFrom(DataClassJsonMixin):
    """ Data on a calling party """
    
    phone_number: Optional[str] = None
    """ Phone number of a party """
    
    name: Optional[str] = None
    """ Displayed name of a party """
    
    device_id: Optional[str] = None
    """ Internal identifier of a device """
    
    extension_id: Optional[str] = None
    """ Internal identifier of an extension """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadCallPartyStatusResponseTo(DataClassJsonMixin):
    """ Data on a called party """
    
    phone_number: Optional[str] = None
    """ Phone number of a party """
    
    name: Optional[str] = None
    """ Displayed name of a party """
    
    device_id: Optional[str] = None
    """ Internal identifier of a device """
    
    extension_id: Optional[str] = None
    """ Internal identifier of an extension """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadCallPartyStatusResponseOwner(DataClassJsonMixin):
    """ Data on a call owner """
    
    account_id: Optional[str] = None
    """ Internal identifier of an account that monitors a call """
    
    extension_id: Optional[str] = None
    """ Internal identifier of an extension that monitors a call """
    

class ReadCallPartyStatusResponseDirection(Enum):
    """ Direction of a call """
    
    Inbound = 'Inbound'
    Outbound = 'Outbound'

class ReadCallPartyStatusResponseConferenceRole(Enum):
    """ A party's role in the conference scenarios. For calls of 'Conference' type only """
    
    Host = 'Host'
    Participant = 'Participant'

class ReadCallPartyStatusResponseRingOutRole(Enum):
    """ A party's role in 'Ring Me'/'RingOut' scenarios. For calls of 'Ringout' type only """
    
    Initiator = 'Initiator'
    Target = 'Target'

class ReadCallPartyStatusResponseRingMeRole(Enum):
    """ A party's role in 'Ring Me'/'RingOut' scenarios. For calls of 'Ringme' type only """
    
    Initiator = 'Initiator'
    Target = 'Target'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadCallPartyStatusResponseRecordingsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a Recording resource """
    
    active: Optional[bool] = None
    """ True if the recording is active. False if the recording is paused. """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadCallPartyStatusResponse(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a party """
    
    status: Optional[ReadCallPartyStatusResponseStatus] = None
    """ Status data of a call session """
    
    muted: Optional[bool] = None
    """
    Specifies if a call participant is muted or not. **Note:** If a call is also controlled via
    Hard phone or RingCentral App (not only through the API by calling call control methods) then
    it cannot be fully muted/unmuted via API only, in this case the action should be duplicated via
    Hard phone/RC App interfaces
    """
    
    stand_alone: Optional[bool] = None
    """
    If 'True' then the party is not connected to a session voice conference, 'False' means the
    party is connected to other parties in a session
    """
    
    park: Optional[ReadCallPartyStatusResponsePark] = None
    """ Call park information """
    
    from_: Optional[ReadCallPartyStatusResponseFrom] = field(metadata=config(field_name='from'), default=None)
    """ Data on a calling party """
    
    to: Optional[ReadCallPartyStatusResponseTo] = None
    """ Data on a called party """
    
    owner: Optional[ReadCallPartyStatusResponseOwner] = None
    """ Data on a call owner """
    
    direction: Optional[ReadCallPartyStatusResponseDirection] = None
    """ Direction of a call """
    
    conference_role: Optional[ReadCallPartyStatusResponseConferenceRole] = None
    """ A party's role in the conference scenarios. For calls of 'Conference' type only """
    
    ring_out_role: Optional[ReadCallPartyStatusResponseRingOutRole] = None
    """ A party's role in 'Ring Me'/'RingOut' scenarios. For calls of 'Ringout' type only """
    
    ring_me_role: Optional[ReadCallPartyStatusResponseRingMeRole] = None
    """ A party's role in 'Ring Me'/'RingOut' scenarios. For calls of 'Ringme' type only """
    
    recordings: Optional[List[ReadCallPartyStatusResponseRecordingsItem]] = None
    """ Active recordings list """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateCallPartyRequestParty(DataClassJsonMixin):
    """ Party update data """
    
    muted: Optional[bool] = None
    """
    Specifies if a call participant is muted or not. **Note:** If a call is also controlled via
    Hard phone or RingCentral App (not only through the API by calling call control methods) then
    it cannot be fully muted/unmuted via API only, in this case the action should be duplicated via
    Hard phone/RC App interfaces
    """
    
    stand_alone: Optional[bool] = None
    """
    If 'True' then the party is not connected to a session voice conference, 'False' means the
    party is connected to other parties in a session
    """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateCallPartyRequest(DataClassJsonMixin):
    party: Optional[UpdateCallPartyRequestParty] = None
    """ Party update data """
    

class UpdateCallPartyResponseStatusCode(Enum):
    """ Status code of a call """
    
    Setup = 'Setup'
    Proceeding = 'Proceeding'
    Answered = 'Answered'
    Disconnected = 'Disconnected'
    Gone = 'Gone'
    Parked = 'Parked'
    Hold = 'Hold'
    VoiceMail = 'VoiceMail'
    FaxReceive = 'FaxReceive'
    VoiceMailScreening = 'VoiceMailScreening'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateCallPartyResponseStatusPeerId(DataClassJsonMixin):
    """ Peer session / party data.'Gone'state only """
    
    session_id: Optional[str] = None
    telephony_session_id: Optional[str] = None
    party_id: Optional[str] = None

class UpdateCallPartyResponseStatusReason(Enum):
    """ Reason of call termination. For 'Disconnected' code only """
    
    Pickup = 'Pickup'
    Supervising = 'Supervising'
    TakeOver = 'TakeOver'
    Timeout = 'Timeout'
    BlindTransfer = 'BlindTransfer'
    RccTransfer = 'RccTransfer'
    AttendedTransfer = 'AttendedTransfer'
    CallerInputRedirect = 'CallerInputRedirect'
    CallFlip = 'CallFlip'
    ParkLocation = 'ParkLocation'
    DtmfTransfer = 'DtmfTransfer'
    AgentAnswered = 'AgentAnswered'
    AgentDropped = 'AgentDropped'
    Rejected = 'Rejected'
    Cancelled = 'Cancelled'
    InternalError = 'InternalError'
    NoAnswer = 'NoAnswer'
    TargetBusy = 'TargetBusy'
    InvalidNumber = 'InvalidNumber'
    InternationalDisabled = 'InternationalDisabled'
    DestinationBlocked = 'DestinationBlocked'
    NotEnoughFunds = 'NotEnoughFunds'
    NoSuchUser = 'NoSuchUser'
    CallPark = 'CallPark'
    CallRedirected = 'CallRedirected'
    CallReplied = 'CallReplied'
    CallSwitch = 'CallSwitch'
    CallFinished = 'CallFinished'
    CallDropped = 'CallDropped'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateCallPartyResponseStatus(DataClassJsonMixin):
    """ Status data of a call session """
    
    code: Optional[UpdateCallPartyResponseStatusCode] = None
    """ Status code of a call """
    
    peer_id: Optional[UpdateCallPartyResponseStatusPeerId] = None
    """ Peer session / party data.'Gone'state only """
    
    reason: Optional[UpdateCallPartyResponseStatusReason] = None
    """ Reason of call termination. For 'Disconnected' code only """
    
    description: Optional[str] = None
    """ Optional message """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateCallPartyResponsePark(DataClassJsonMixin):
    """ Call park information """
    
    id: Optional[str] = None
    """ Call park identifier """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateCallPartyResponseFrom(DataClassJsonMixin):
    """ Data on a calling party """
    
    phone_number: Optional[str] = None
    """ Phone number of a party """
    
    name: Optional[str] = None
    """ Displayed name of a party """
    
    device_id: Optional[str] = None
    """ Internal identifier of a device """
    
    extension_id: Optional[str] = None
    """ Internal identifier of an extension """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateCallPartyResponseTo(DataClassJsonMixin):
    """ Data on a called party """
    
    phone_number: Optional[str] = None
    """ Phone number of a party """
    
    name: Optional[str] = None
    """ Displayed name of a party """
    
    device_id: Optional[str] = None
    """ Internal identifier of a device """
    
    extension_id: Optional[str] = None
    """ Internal identifier of an extension """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateCallPartyResponseOwner(DataClassJsonMixin):
    """ Data on a call owner """
    
    account_id: Optional[str] = None
    """ Internal identifier of an account that monitors a call """
    
    extension_id: Optional[str] = None
    """ Internal identifier of an extension that monitors a call """
    

class UpdateCallPartyResponseDirection(Enum):
    """ Direction of a call """
    
    Inbound = 'Inbound'
    Outbound = 'Outbound'

class UpdateCallPartyResponseConferenceRole(Enum):
    """ A party's role in the conference scenarios. For calls of 'Conference' type only """
    
    Host = 'Host'
    Participant = 'Participant'

class UpdateCallPartyResponseRingOutRole(Enum):
    """ A party's role in 'Ring Me'/'RingOut' scenarios. For calls of 'Ringout' type only """
    
    Initiator = 'Initiator'
    Target = 'Target'

class UpdateCallPartyResponseRingMeRole(Enum):
    """ A party's role in 'Ring Me'/'RingOut' scenarios. For calls of 'Ringme' type only """
    
    Initiator = 'Initiator'
    Target = 'Target'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateCallPartyResponseRecordingsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a Recording resource """
    
    active: Optional[bool] = None
    """ True if the recording is active. False if the recording is paused. """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateCallPartyResponse(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a party """
    
    status: Optional[UpdateCallPartyResponseStatus] = None
    """ Status data of a call session """
    
    muted: Optional[bool] = None
    """
    Specifies if a call participant is muted or not. **Note:** If a call is also controlled via
    Hard phone or RingCentral App (not only through the API by calling call control methods) then
    it cannot be fully muted/unmuted via API only, in this case the action should be duplicated via
    Hard phone/RC App interfaces
    """
    
    stand_alone: Optional[bool] = None
    """
    If 'True' then the party is not connected to a session voice conference, 'False' means the
    party is connected to other parties in a session
    """
    
    park: Optional[UpdateCallPartyResponsePark] = None
    """ Call park information """
    
    from_: Optional[UpdateCallPartyResponseFrom] = field(metadata=config(field_name='from'), default=None)
    """ Data on a calling party """
    
    to: Optional[UpdateCallPartyResponseTo] = None
    """ Data on a called party """
    
    owner: Optional[UpdateCallPartyResponseOwner] = None
    """ Data on a call owner """
    
    direction: Optional[UpdateCallPartyResponseDirection] = None
    """ Direction of a call """
    
    conference_role: Optional[UpdateCallPartyResponseConferenceRole] = None
    """ A party's role in the conference scenarios. For calls of 'Conference' type only """
    
    ring_out_role: Optional[UpdateCallPartyResponseRingOutRole] = None
    """ A party's role in 'Ring Me'/'RingOut' scenarios. For calls of 'Ringout' type only """
    
    ring_me_role: Optional[UpdateCallPartyResponseRingMeRole] = None
    """ A party's role in 'Ring Me'/'RingOut' scenarios. For calls of 'Ringme' type only """
    
    recordings: Optional[List[UpdateCallPartyResponseRecordingsItem]] = None
    """ Active recordings list """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class PauseResumeCallRecordingRequest(DataClassJsonMixin):
    active: Optional[bool] = None
    """ Recording status """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class PauseResumeCallRecordingResponse(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a call recording """
    
    active: Optional[bool] = None
    """ Call recording status """
    

class SuperviseCallSessionRequestMode(Enum):
    """
    Supervising mode
    
    Example: `Listen`
    Generated by Python OpenAPI Parser
    """
    
    Listen = 'Listen'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class SuperviseCallSessionRequest(DataClassJsonMixin):
    """
    Required Properties:
     - mode
     - supervisor_device_id
    
    Generated by Python OpenAPI Parser
    """
    
    mode: SuperviseCallSessionRequestMode
    """
    Supervising mode
    
    Example: `Listen`
    """
    
    supervisor_device_id: str
    """
    Internal identifier of a supervisor's device which will be used for call session monitoring
    
    Example: `191888004`
    """
    
    agent_extension_number: Optional[str] = None
    """
    Extension number of the user that will be monitored
    
    Example: `105`
    """
    
    agent_extension_id: Optional[str] = None
    """
    Extension identifier of the user that will be monitored
    
    Example: `400378008008`
    """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class SuperviseCallSessionResponseFrom(DataClassJsonMixin):
    """ Information about a call party that monitors a call """
    
    phone_number: Optional[str] = None
    """ Phone number of a party """
    
    name: Optional[str] = None
    """ Displayed name of a party """
    
    device_id: Optional[str] = None
    """ Internal identifier of a device """
    
    extension_id: Optional[str] = None
    """ Internal identifier of an extension """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class SuperviseCallSessionResponseTo(DataClassJsonMixin):
    """ Information about a call party that is monitored """
    
    phone_number: Optional[str] = None
    """ Phone number of a party """
    
    name: Optional[str] = None
    """ Displayed name of a party """
    
    device_id: Optional[str] = None
    """ Internal identifier of a device """
    
    extension_id: Optional[str] = None
    """ Internal identifier of an extension """
    

class SuperviseCallSessionResponseDirection(Enum):
    """ Direction of a call """
    
    Outbound = 'Outbound'
    Inbound = 'Inbound'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class SuperviseCallSessionResponseOwner(DataClassJsonMixin):
    """ Data on a call owner """
    
    account_id: Optional[str] = None
    """ Internal identifier of an account that monitors a call """
    
    extension_id: Optional[str] = None
    """ Internal identifier of an extension that monitors a call """
    

class SuperviseCallSessionResponseStatusCode(Enum):
    """ Status code of a call """
    
    Setup = 'Setup'
    Proceeding = 'Proceeding'
    Answered = 'Answered'
    Disconnected = 'Disconnected'
    Gone = 'Gone'
    Parked = 'Parked'
    Hold = 'Hold'
    VoiceMail = 'VoiceMail'
    FaxReceive = 'FaxReceive'
    VoiceMailScreening = 'VoiceMailScreening'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class SuperviseCallSessionResponseStatusPeerId(DataClassJsonMixin):
    """ Peer session / party data.'Gone'state only """
    
    session_id: Optional[str] = None
    telephony_session_id: Optional[str] = None
    party_id: Optional[str] = None

class SuperviseCallSessionResponseStatusReason(Enum):
    """ Reason of call termination. For 'Disconnected' code only """
    
    Pickup = 'Pickup'
    Supervising = 'Supervising'
    TakeOver = 'TakeOver'
    Timeout = 'Timeout'
    BlindTransfer = 'BlindTransfer'
    RccTransfer = 'RccTransfer'
    AttendedTransfer = 'AttendedTransfer'
    CallerInputRedirect = 'CallerInputRedirect'
    CallFlip = 'CallFlip'
    ParkLocation = 'ParkLocation'
    DtmfTransfer = 'DtmfTransfer'
    AgentAnswered = 'AgentAnswered'
    AgentDropped = 'AgentDropped'
    Rejected = 'Rejected'
    Cancelled = 'Cancelled'
    InternalError = 'InternalError'
    NoAnswer = 'NoAnswer'
    TargetBusy = 'TargetBusy'
    InvalidNumber = 'InvalidNumber'
    InternationalDisabled = 'InternationalDisabled'
    DestinationBlocked = 'DestinationBlocked'
    NotEnoughFunds = 'NotEnoughFunds'
    NoSuchUser = 'NoSuchUser'
    CallPark = 'CallPark'
    CallRedirected = 'CallRedirected'
    CallReplied = 'CallReplied'
    CallSwitch = 'CallSwitch'
    CallFinished = 'CallFinished'
    CallDropped = 'CallDropped'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class SuperviseCallSessionResponseStatus(DataClassJsonMixin):
    code: Optional[SuperviseCallSessionResponseStatusCode] = None
    """ Status code of a call """
    
    peer_id: Optional[SuperviseCallSessionResponseStatusPeerId] = None
    """ Peer session / party data.'Gone'state only """
    
    reason: Optional[SuperviseCallSessionResponseStatusReason] = None
    """ Reason of call termination. For 'Disconnected' code only """
    
    description: Optional[str] = None
    """ Optional message """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class SuperviseCallSessionResponse(DataClassJsonMixin):
    from_: Optional[SuperviseCallSessionResponseFrom] = field(metadata=config(field_name='from'), default=None)
    """ Information about a call party that monitors a call """
    
    to: Optional[SuperviseCallSessionResponseTo] = None
    """ Information about a call party that is monitored """
    
    direction: Optional[SuperviseCallSessionResponseDirection] = None
    """ Direction of a call """
    
    id: Optional[str] = None
    """ Internal identifier of a party that monitors a call """
    
    account_id: Optional[str] = None
    """ Internal identifier of an account that monitors a call """
    
    extension_id: Optional[str] = None
    """ Internal identifier of an extension that monitors a call """
    
    muted: Optional[bool] = None
    """
    Specifies if a call participant is muted or not. **Note:** If a call is also controlled via
    Hard phone or RingCentral App (not only through the API by calling call control methods) then
    it cannot be fully muted/unmuted via API only, in this case the action should be duplicated via
    Hard phone/RC App interfaces
    """
    
    owner: Optional[SuperviseCallSessionResponseOwner] = None
    """ Data on a call owner """
    
    stand_alone: Optional[bool] = None
    """
    If 'True' then the party is not connected to a session voice conference, 'False' means the
    party is connected to other parties in a session
    """
    
    status: Optional[SuperviseCallSessionResponseStatus] = None

class SuperviseCallPartyRequestMode(Enum):
    """
    Supervising mode
    
    Example: `Listen`
    Generated by Python OpenAPI Parser
    """
    
    Listen = 'Listen'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class SuperviseCallPartyRequest(DataClassJsonMixin):
    """
    Required Properties:
     - mode
     - supervisor_device_id
     - agent_extension_id
    
    Generated by Python OpenAPI Parser
    """
    
    mode: SuperviseCallPartyRequestMode
    """
    Supervising mode
    
    Example: `Listen`
    """
    
    supervisor_device_id: str
    """
    Internal identifier of a supervisor's device
    
    Example: `191888004`
    """
    
    agent_extension_id: str
    """
    Mailbox ID of a user that will be monitored
    
    Example: `400378008008`
    """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class SuperviseCallPartyResponseFrom(DataClassJsonMixin):
    """ Information about a call party that monitors a call """
    
    phone_number: Optional[str] = None
    """ Phone number of a party """
    
    name: Optional[str] = None
    """ Displayed name of a party """
    
    device_id: Optional[str] = None
    """ Internal identifier of a device """
    
    extension_id: Optional[str] = None
    """ Internal identifier of an extension """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class SuperviseCallPartyResponseTo(DataClassJsonMixin):
    """ Information about a call party that is monitored """
    
    phone_number: Optional[str] = None
    """ Phone number of a party """
    
    name: Optional[str] = None
    """ Displayed name of a party """
    
    device_id: Optional[str] = None
    """ Internal identifier of a device """
    
    extension_id: Optional[str] = None
    """ Internal identifier of an extension """
    

class SuperviseCallPartyResponseDirection(Enum):
    """ Direction of a call """
    
    Outbound = 'Outbound'
    Inbound = 'Inbound'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class SuperviseCallPartyResponseOwner(DataClassJsonMixin):
    """ Deprecated. Infromation a call owner """
    
    account_id: Optional[str] = None
    """ Internal identifier of an account that monitors a call """
    
    extension_id: Optional[str] = None
    """ Internal identifier of an extension that monitors a call """
    

class SuperviseCallPartyResponseStatusCode(Enum):
    """ Status code of a call """
    
    Setup = 'Setup'
    Proceeding = 'Proceeding'
    Answered = 'Answered'
    Disconnected = 'Disconnected'
    Gone = 'Gone'
    Parked = 'Parked'
    Hold = 'Hold'
    VoiceMail = 'VoiceMail'
    FaxReceive = 'FaxReceive'
    VoiceMailScreening = 'VoiceMailScreening'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class SuperviseCallPartyResponseStatusPeerId(DataClassJsonMixin):
    """ Peer session / party data.'Gone'state only """
    
    session_id: Optional[str] = None
    telephony_session_id: Optional[str] = None
    party_id: Optional[str] = None

class SuperviseCallPartyResponseStatusReason(Enum):
    """ Reason of call termination. For 'Disconnected' code only """
    
    Pickup = 'Pickup'
    Supervising = 'Supervising'
    TakeOver = 'TakeOver'
    Timeout = 'Timeout'
    BlindTransfer = 'BlindTransfer'
    RccTransfer = 'RccTransfer'
    AttendedTransfer = 'AttendedTransfer'
    CallerInputRedirect = 'CallerInputRedirect'
    CallFlip = 'CallFlip'
    ParkLocation = 'ParkLocation'
    DtmfTransfer = 'DtmfTransfer'
    AgentAnswered = 'AgentAnswered'
    AgentDropped = 'AgentDropped'
    Rejected = 'Rejected'
    Cancelled = 'Cancelled'
    InternalError = 'InternalError'
    NoAnswer = 'NoAnswer'
    TargetBusy = 'TargetBusy'
    InvalidNumber = 'InvalidNumber'
    InternationalDisabled = 'InternationalDisabled'
    DestinationBlocked = 'DestinationBlocked'
    NotEnoughFunds = 'NotEnoughFunds'
    NoSuchUser = 'NoSuchUser'
    CallPark = 'CallPark'
    CallRedirected = 'CallRedirected'
    CallReplied = 'CallReplied'
    CallSwitch = 'CallSwitch'
    CallFinished = 'CallFinished'
    CallDropped = 'CallDropped'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class SuperviseCallPartyResponseStatus(DataClassJsonMixin):
    code: Optional[SuperviseCallPartyResponseStatusCode] = None
    """ Status code of a call """
    
    peer_id: Optional[SuperviseCallPartyResponseStatusPeerId] = None
    """ Peer session / party data.'Gone'state only """
    
    reason: Optional[SuperviseCallPartyResponseStatusReason] = None
    """ Reason of call termination. For 'Disconnected' code only """
    
    description: Optional[str] = None
    """ Optional message """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class SuperviseCallPartyResponse(DataClassJsonMixin):
    from_: Optional[SuperviseCallPartyResponseFrom] = field(metadata=config(field_name='from'), default=None)
    """ Information about a call party that monitors a call """
    
    to: Optional[SuperviseCallPartyResponseTo] = None
    """ Information about a call party that is monitored """
    
    direction: Optional[SuperviseCallPartyResponseDirection] = None
    """ Direction of a call """
    
    id: Optional[str] = None
    """ Internal identifier of a party that monitors a call """
    
    account_id: Optional[str] = None
    """ Internal identifier of an account that monitors a call """
    
    extension_id: Optional[str] = None
    """ Internal identifier of an extension that monitors a call """
    
    muted: Optional[bool] = None
    """ Specifies if a call party is muted """
    
    owner: Optional[SuperviseCallPartyResponseOwner] = None
    """ Deprecated. Infromation a call owner """
    
    stand_alone: Optional[bool] = None
    """ Specifies if a device is stand-alone """
    
    status: Optional[SuperviseCallPartyResponseStatus] = None

class ListDataExportTasksStatus(Enum):
    Accepted = 'Accepted'
    InProgress = 'InProgress'
    Completed = 'Completed'
    Failed = 'Failed'
    Expired = 'Expired'

class ListDataExportTasksResponseTasksItemStatus(Enum):
    """ Task status """
    
    Accepted = 'Accepted'
    InProgress = 'InProgress'
    Completed = 'Completed'
    Failed = 'Failed'
    Expired = 'Expired'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListDataExportTasksResponseTasksItemCreator(DataClassJsonMixin):
    """ Task creator information """
    
    id: Optional[str] = None
    """ Internal identifier of a user who created a note/task """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListDataExportTasksResponseTasksItemSpecificContactsItem(DataClassJsonMixin):
    """
    List of users whose data is collected. The following data is exported: posts, tasks, events,
    etc. posted by the user(s); posts addressing the user(s) via direct and @Mentions; tasks
    assigned to the listed user(s)
    
    Generated by Python OpenAPI Parser
    """
    
    id: Optional[str] = None
    """ Internal identifier of a contact """
    
    email: Optional[str] = None
    """ Email address of a contact """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListDataExportTasksResponseTasksItemSpecific(DataClassJsonMixin):
    """ Information specififed in request """
    
    time_from: Optional[str] = None
    """ Starting time for data collection """
    
    time_to: Optional[str] = None
    """ Ending time for data collection """
    
    contacts: Optional[List[ListDataExportTasksResponseTasksItemSpecificContactsItem]] = None
    chat_ids: Optional[List[str]] = None
    """ List of chats from which the data (posts, files, tasks, events, notes, etc.) will be collected """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListDataExportTasksResponseTasksItemDatasetsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a dataset """
    
    uri: Optional[str] = None
    """ Link for downloading a dataset """
    
    size: Optional[int] = None
    """ Size of ta dataset in bytes """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListDataExportTasksResponseTasksItem(DataClassJsonMixin):
    uri: Optional[str] = None
    """ Canonical URI of a task """
    
    id: Optional[str] = None
    """ Internal identifier of a task """
    
    creation_time: Optional[str] = None
    """ Task creation datetime """
    
    last_modified_time: Optional[str] = None
    """ Task last modification datetime """
    
    status: Optional[ListDataExportTasksResponseTasksItemStatus] = None
    """ Task status """
    
    creator: Optional[ListDataExportTasksResponseTasksItemCreator] = None
    """ Task creator information """
    
    specific: Optional[ListDataExportTasksResponseTasksItemSpecific] = None
    """ Information specififed in request """
    
    datasets: Optional[List[ListDataExportTasksResponseTasksItemDatasetsItem]] = None
    """ Data collection sets. Returned by task ID """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListDataExportTasksResponseNavigationFirstPage(DataClassJsonMixin):
    """ Canonical URI for the first page of the list """
    
    uri: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListDataExportTasksResponseNavigationNextPage(DataClassJsonMixin):
    """ Canonical URI for the next page of the list """
    
    uri: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListDataExportTasksResponseNavigationPreviousPage(DataClassJsonMixin):
    """ Canonical URI for the previous page of the list """
    
    uri: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListDataExportTasksResponseNavigationLastPage(DataClassJsonMixin):
    """ Canonical URI for the last page of the list """
    
    uri: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListDataExportTasksResponseNavigation(DataClassJsonMixin):
    first_page: Optional[ListDataExportTasksResponseNavigationFirstPage] = None
    """ Canonical URI for the first page of the list """
    
    next_page: Optional[ListDataExportTasksResponseNavigationNextPage] = None
    """ Canonical URI for the next page of the list """
    
    previous_page: Optional[ListDataExportTasksResponseNavigationPreviousPage] = None
    """ Canonical URI for the previous page of the list """
    
    last_page: Optional[ListDataExportTasksResponseNavigationLastPage] = None
    """ Canonical URI for the last page of the list """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListDataExportTasksResponsePaging(DataClassJsonMixin):
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
class ListDataExportTasksResponse(DataClassJsonMixin):
    tasks: Optional[List[ListDataExportTasksResponseTasksItem]] = None
    navigation: Optional[ListDataExportTasksResponseNavigation] = None
    paging: Optional[ListDataExportTasksResponsePaging] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateDataExportTaskRequestContactsItem(DataClassJsonMixin):
    """
    List of users whose data is collected. The following data will be exported: posts, tasks,
    events, etc. posted by the user(s); posts addressing the user(s) via direct and @Mentions;
    tasks assigned to the listed user(s). The list of 10 users per request is supported.
    
    Generated by Python OpenAPI Parser
    """
    
    id: Optional[str] = None
    """ Internal identifier of a contact """
    
    email: Optional[str] = None
    """ Email address of a contact """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateDataExportTaskRequest(DataClassJsonMixin):
    time_from: Optional[str] = None
    """
    Starting time for data collection. The default value is `timeTo` minus 24 hours. Max allowed
    time frame between `timeFrom` and `timeTo` is 6 months
    """
    
    time_to: Optional[str] = None
    """
    Ending time for data collection. The default value is current time. Max allowed time frame
    between `timeFrom` and `timeTo` is 6 months
    """
    
    contacts: Optional[List[CreateDataExportTaskRequestContactsItem]] = None
    chat_ids: Optional[List[str]] = None
    """
    List of chats from which the data (posts, files, tasks, events, notes, etc.) will be collected.
    Maximum number of chats supported is 10
    """
    

class CreateDataExportTaskResponseStatus(Enum):
    """ Task status """
    
    Accepted = 'Accepted'
    InProgress = 'InProgress'
    Completed = 'Completed'
    Failed = 'Failed'
    Expired = 'Expired'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateDataExportTaskResponseCreator(DataClassJsonMixin):
    """ Task creator information """
    
    id: Optional[str] = None
    """ Internal identifier of a user who created a note/task """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateDataExportTaskResponseSpecificContactsItem(DataClassJsonMixin):
    """
    List of users whose data is collected. The following data is exported: posts, tasks, events,
    etc. posted by the user(s); posts addressing the user(s) via direct and @Mentions; tasks
    assigned to the listed user(s)
    
    Generated by Python OpenAPI Parser
    """
    
    id: Optional[str] = None
    """ Internal identifier of a contact """
    
    email: Optional[str] = None
    """ Email address of a contact """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateDataExportTaskResponseSpecific(DataClassJsonMixin):
    """ Information specififed in request """
    
    time_from: Optional[str] = None
    """ Starting time for data collection """
    
    time_to: Optional[str] = None
    """ Ending time for data collection """
    
    contacts: Optional[List[CreateDataExportTaskResponseSpecificContactsItem]] = None
    chat_ids: Optional[List[str]] = None
    """ List of chats from which the data (posts, files, tasks, events, notes, etc.) will be collected """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateDataExportTaskResponseDatasetsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a dataset """
    
    uri: Optional[str] = None
    """ Link for downloading a dataset """
    
    size: Optional[int] = None
    """ Size of ta dataset in bytes """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateDataExportTaskResponse(DataClassJsonMixin):
    uri: Optional[str] = None
    """ Canonical URI of a task """
    
    id: Optional[str] = None
    """ Internal identifier of a task """
    
    creation_time: Optional[str] = None
    """ Task creation datetime """
    
    last_modified_time: Optional[str] = None
    """ Task last modification datetime """
    
    status: Optional[CreateDataExportTaskResponseStatus] = None
    """ Task status """
    
    creator: Optional[CreateDataExportTaskResponseCreator] = None
    """ Task creator information """
    
    specific: Optional[CreateDataExportTaskResponseSpecific] = None
    """ Information specififed in request """
    
    datasets: Optional[List[CreateDataExportTaskResponseDatasetsItem]] = None
    """ Data collection sets. Returned by task ID """
    

class ReadDataExportTaskResponseStatus(Enum):
    """ Task status """
    
    Accepted = 'Accepted'
    InProgress = 'InProgress'
    Completed = 'Completed'
    Failed = 'Failed'
    Expired = 'Expired'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadDataExportTaskResponseCreator(DataClassJsonMixin):
    """ Task creator information """
    
    id: Optional[str] = None
    """ Internal identifier of a user who created a note/task """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadDataExportTaskResponseSpecificContactsItem(DataClassJsonMixin):
    """
    List of users whose data is collected. The following data is exported: posts, tasks, events,
    etc. posted by the user(s); posts addressing the user(s) via direct and @Mentions; tasks
    assigned to the listed user(s)
    
    Generated by Python OpenAPI Parser
    """
    
    id: Optional[str] = None
    """ Internal identifier of a contact """
    
    email: Optional[str] = None
    """ Email address of a contact """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadDataExportTaskResponseSpecific(DataClassJsonMixin):
    """ Information specififed in request """
    
    time_from: Optional[str] = None
    """ Starting time for data collection """
    
    time_to: Optional[str] = None
    """ Ending time for data collection """
    
    contacts: Optional[List[ReadDataExportTaskResponseSpecificContactsItem]] = None
    chat_ids: Optional[List[str]] = None
    """ List of chats from which the data (posts, files, tasks, events, notes, etc.) will be collected """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadDataExportTaskResponseDatasetsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a dataset """
    
    uri: Optional[str] = None
    """ Link for downloading a dataset """
    
    size: Optional[int] = None
    """ Size of ta dataset in bytes """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadDataExportTaskResponse(DataClassJsonMixin):
    uri: Optional[str] = None
    """ Canonical URI of a task """
    
    id: Optional[str] = None
    """ Internal identifier of a task """
    
    creation_time: Optional[str] = None
    """ Task creation datetime """
    
    last_modified_time: Optional[str] = None
    """ Task last modification datetime """
    
    status: Optional[ReadDataExportTaskResponseStatus] = None
    """ Task status """
    
    creator: Optional[ReadDataExportTaskResponseCreator] = None
    """ Task creator information """
    
    specific: Optional[ReadDataExportTaskResponseSpecific] = None
    """ Information specififed in request """
    
    datasets: Optional[List[ReadDataExportTaskResponseDatasetsItem]] = None
    """ Data collection sets. Returned by task ID """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateMessageStoreReportRequest(DataClassJsonMixin):
    date_from: Optional[str] = None
    """
    Starting time for collecting messages. The default value equals to the current time minus 24
    hours
    """
    
    date_to: Optional[str] = None
    """ Ending time for collecting messages. The default value is the current time """
    

class CreateMessageStoreReportResponseStatus(Enum):
    """ Status of a message store report task """
    
    Accepted = 'Accepted'
    Pending = 'Pending'
    InProgress = 'InProgress'
    AttemptFailed = 'AttemptFailed'
    Failed = 'Failed'
    Completed = 'Completed'
    Cancelled = 'Cancelled'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateMessageStoreReportResponse(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a message store report task """
    
    uri: Optional[str] = None
    """ Link to a task """
    
    status: Optional[CreateMessageStoreReportResponseStatus] = None
    """ Status of a message store report task """
    
    account_id: Optional[str] = None
    """ Internal identifier of an account """
    
    extension_id: Optional[str] = None
    """ Internal identifier of an extension """
    
    creation_time: Optional[str] = None
    """ Task creation time """
    
    last_modified_time: Optional[str] = None
    """ Time of the last task modification """
    
    date_to: Optional[str] = None
    """ Ending time for collecting messages """
    
    date_from: Optional[str] = None
    """ Starting time for collecting messages """
    

class ReadMessageStoreReportTaskResponseStatus(Enum):
    """ Status of a message store report task """
    
    Accepted = 'Accepted'
    Pending = 'Pending'
    InProgress = 'InProgress'
    AttemptFailed = 'AttemptFailed'
    Failed = 'Failed'
    Completed = 'Completed'
    Cancelled = 'Cancelled'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadMessageStoreReportTaskResponse(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a message store report task """
    
    uri: Optional[str] = None
    """ Link to a task """
    
    status: Optional[ReadMessageStoreReportTaskResponseStatus] = None
    """ Status of a message store report task """
    
    account_id: Optional[str] = None
    """ Internal identifier of an account """
    
    extension_id: Optional[str] = None
    """ Internal identifier of an extension """
    
    creation_time: Optional[str] = None
    """ Task creation time """
    
    last_modified_time: Optional[str] = None
    """ Time of the last task modification """
    
    date_to: Optional[str] = None
    """ Ending time for collecting messages """
    
    date_from: Optional[str] = None
    """ Starting time for collecting messages """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadMessageStoreReportArchiveResponseRecordsItem(DataClassJsonMixin):
    size: Optional[int] = None
    """ Archive size in bytes """
    
    uri: Optional[str] = None
    """ Link for archive download """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadMessageStoreReportArchiveResponse(DataClassJsonMixin):
    records: Optional[List[ReadMessageStoreReportArchiveResponseRecordsItem]] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListAccountMeetingRecordingsResponseRecordsItemMeeting(DataClassJsonMixin):
    id: Optional[str] = None
    topic: Optional[str] = None
    start_time: Optional[str] = None

class ListAccountMeetingRecordingsResponseRecordsItemRecordingItemContentType(Enum):
    VideoMp4 = 'video/mp4'
    AudioM4a = 'audio/m4a'
    TextVtt = 'text/vtt'

class ListAccountMeetingRecordingsResponseRecordsItemRecordingItemStatus(Enum):
    Completed = 'Completed'
    Processing = 'Processing'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListAccountMeetingRecordingsResponseRecordsItemRecordingItem(DataClassJsonMixin):
    id: Optional[str] = None
    content_download_uri: Optional[str] = None
    content_type: Optional[ListAccountMeetingRecordingsResponseRecordsItemRecordingItemContentType] = None
    size: Optional[int] = None
    start_time: Optional[str] = None
    """ Starting time of a recording """
    
    end_time: Optional[str] = None
    """ Ending time of a recording """
    
    status: Optional[ListAccountMeetingRecordingsResponseRecordsItemRecordingItemStatus] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListAccountMeetingRecordingsResponseRecordsItem(DataClassJsonMixin):
    meeting: Optional[ListAccountMeetingRecordingsResponseRecordsItemMeeting] = None
    recording: Optional[List[ListAccountMeetingRecordingsResponseRecordsItemRecordingItem]] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListAccountMeetingRecordingsResponsePaging(DataClassJsonMixin):
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
class ListAccountMeetingRecordingsResponseNavigationFirstPage(DataClassJsonMixin):
    """ Canonical URI for the first page of the list """
    
    uri: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListAccountMeetingRecordingsResponseNavigationNextPage(DataClassJsonMixin):
    """ Canonical URI for the next page of the list """
    
    uri: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListAccountMeetingRecordingsResponseNavigationPreviousPage(DataClassJsonMixin):
    """ Canonical URI for the previous page of the list """
    
    uri: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListAccountMeetingRecordingsResponseNavigationLastPage(DataClassJsonMixin):
    """ Canonical URI for the last page of the list """
    
    uri: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListAccountMeetingRecordingsResponseNavigation(DataClassJsonMixin):
    first_page: Optional[ListAccountMeetingRecordingsResponseNavigationFirstPage] = None
    """ Canonical URI for the first page of the list """
    
    next_page: Optional[ListAccountMeetingRecordingsResponseNavigationNextPage] = None
    """ Canonical URI for the next page of the list """
    
    previous_page: Optional[ListAccountMeetingRecordingsResponseNavigationPreviousPage] = None
    """ Canonical URI for the previous page of the list """
    
    last_page: Optional[ListAccountMeetingRecordingsResponseNavigationLastPage] = None
    """ Canonical URI for the last page of the list """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListAccountMeetingRecordingsResponse(DataClassJsonMixin):
    records: Optional[List[ListAccountMeetingRecordingsResponseRecordsItem]] = None
    paging: Optional[ListAccountMeetingRecordingsResponsePaging] = None
    navigation: Optional[ListAccountMeetingRecordingsResponseNavigation] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListUserMeetingRecordingsResponseRecordsItemMeeting(DataClassJsonMixin):
    id: Optional[str] = None
    topic: Optional[str] = None
    start_time: Optional[str] = None

class ListUserMeetingRecordingsResponseRecordsItemRecordingItemContentType(Enum):
    VideoMp4 = 'video/mp4'
    AudioM4a = 'audio/m4a'
    TextVtt = 'text/vtt'

class ListUserMeetingRecordingsResponseRecordsItemRecordingItemStatus(Enum):
    Completed = 'Completed'
    Processing = 'Processing'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListUserMeetingRecordingsResponseRecordsItemRecordingItem(DataClassJsonMixin):
    id: Optional[str] = None
    content_download_uri: Optional[str] = None
    content_type: Optional[ListUserMeetingRecordingsResponseRecordsItemRecordingItemContentType] = None
    size: Optional[int] = None
    start_time: Optional[str] = None
    """ Starting time of a recording """
    
    end_time: Optional[str] = None
    """ Ending time of a recording """
    
    status: Optional[ListUserMeetingRecordingsResponseRecordsItemRecordingItemStatus] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListUserMeetingRecordingsResponseRecordsItem(DataClassJsonMixin):
    meeting: Optional[ListUserMeetingRecordingsResponseRecordsItemMeeting] = None
    recording: Optional[List[ListUserMeetingRecordingsResponseRecordsItemRecordingItem]] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListUserMeetingRecordingsResponsePaging(DataClassJsonMixin):
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
class ListUserMeetingRecordingsResponseNavigationFirstPage(DataClassJsonMixin):
    """ Canonical URI for the first page of the list """
    
    uri: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListUserMeetingRecordingsResponseNavigationNextPage(DataClassJsonMixin):
    """ Canonical URI for the next page of the list """
    
    uri: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListUserMeetingRecordingsResponseNavigationPreviousPage(DataClassJsonMixin):
    """ Canonical URI for the previous page of the list """
    
    uri: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListUserMeetingRecordingsResponseNavigationLastPage(DataClassJsonMixin):
    """ Canonical URI for the last page of the list """
    
    uri: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListUserMeetingRecordingsResponseNavigation(DataClassJsonMixin):
    first_page: Optional[ListUserMeetingRecordingsResponseNavigationFirstPage] = None
    """ Canonical URI for the first page of the list """
    
    next_page: Optional[ListUserMeetingRecordingsResponseNavigationNextPage] = None
    """ Canonical URI for the next page of the list """
    
    previous_page: Optional[ListUserMeetingRecordingsResponseNavigationPreviousPage] = None
    """ Canonical URI for the previous page of the list """
    
    last_page: Optional[ListUserMeetingRecordingsResponseNavigationLastPage] = None
    """ Canonical URI for the last page of the list """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListUserMeetingRecordingsResponse(DataClassJsonMixin):
    records: Optional[List[ListUserMeetingRecordingsResponseRecordsItem]] = None
    paging: Optional[ListUserMeetingRecordingsResponsePaging] = None
    navigation: Optional[ListUserMeetingRecordingsResponseNavigation] = None

class ListCustomFieldsResponseRecordsItemCategory(Enum):
    """ Object category to attach custom fields """
    
    User = 'User'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListCustomFieldsResponseRecordsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Custom field identifier """
    
    category: Optional[ListCustomFieldsResponseRecordsItemCategory] = None
    """ Object category to attach custom fields """
    
    display_name: Optional[str] = None
    """ Custom field display name """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListCustomFieldsResponse(DataClassJsonMixin):
    records: Optional[List[ListCustomFieldsResponseRecordsItem]] = None

class CreateCustomFieldRequestCategory(Enum):
    """ Object category to attach custom fields """
    
    User = 'User'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateCustomFieldRequest(DataClassJsonMixin):
    category: Optional[CreateCustomFieldRequestCategory] = None
    """ Object category to attach custom fields """
    
    display_name: Optional[str] = None
    """ Custom field display name """
    

class CreateCustomFieldResponseCategory(Enum):
    """ Object category to attach custom fields """
    
    User = 'User'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateCustomFieldResponse(DataClassJsonMixin):
    id: Optional[str] = None
    """ Custom field identifier """
    
    category: Optional[CreateCustomFieldResponseCategory] = None
    """ Object category to attach custom fields """
    
    display_name: Optional[str] = None
    """ Custom field display name """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateCustomFieldRequest(DataClassJsonMixin):
    display_name: Optional[str] = None
    """ Custom field display name """
    

class UpdateCustomFieldResponseCategory(Enum):
    """ Object category to attach custom fields """
    
    User = 'User'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateCustomFieldResponse(DataClassJsonMixin):
    id: Optional[str] = None
    """ Custom field identifier """
    
    category: Optional[UpdateCustomFieldResponseCategory] = None
    """ Object category to attach custom fields """
    
    display_name: Optional[str] = None
    """ Custom field display name """
    


__all__ = \
[
    'AccountBusinessAddressResource',
    'AccountCallLogResponse',
    'AccountCallLogSyncResponse',
    'AccountCallLogSyncResponseSyncInfo',
    'AccountCallLogSyncResponseSyncInfoSyncType',
    'AccountDeviceUpdate',
    'AccountDeviceUpdateEmergencyServiceAddress',
    'AccountDeviceUpdateExtension',
    'AccountDeviceUpdatePhoneLines',
    'AccountDeviceUpdatePhoneLinesPhoneLinesItem',
    'AccountLockedSettingResponse',
    'AccountPhoneNumbers',
    'AccountPresenceInfo',
    'AccountPresenceInfoNavigation',
    'AccountPresenceInfoNavigationFirstPage',
    'AccountPresenceInfoPaging',
    'AddBlockedAllowedPhoneNumber',
    'AddBlockedAllowedPhoneNumberStatus',
    'AddGlipTeamMembersRequest',
    'AddGlipTeamMembersRequestMembersItem',
    'AddressBookSync',
    'AddressBookSyncSyncInfo',
    'AddressBookSyncSyncInfoSyncType',
    'AnswerCallPartyRequest',
    'AnswerCallPartyResponse',
    'AnswerCallPartyResponseConferenceRole',
    'AnswerCallPartyResponseDirection',
    'AnswerCallPartyResponseFrom',
    'AnswerCallPartyResponseOwner',
    'AnswerCallPartyResponsePark',
    'AnswerCallPartyResponseRecordingsItem',
    'AnswerCallPartyResponseRingMeRole',
    'AnswerCallPartyResponseRingOutRole',
    'AnswerCallPartyResponseStatus',
    'AnswerCallPartyResponseStatusCode',
    'AnswerCallPartyResponseStatusPeerId',
    'AnswerCallPartyResponseStatusReason',
    'AnswerCallPartyResponseTo',
    'AnswerTarget',
    'AnsweringRuleInfo',
    'AnsweringRuleInfoCallHandlingAction',
    'AnsweringRuleInfoCalledNumbersItem',
    'AnsweringRuleInfoCallersItem',
    'AnsweringRuleInfoForwarding',
    'AnsweringRuleInfoForwardingRingingMode',
    'AnsweringRuleInfoForwardingRulesItem',
    'AnsweringRuleInfoForwardingRulesItemForwardingNumbersItem',
    'AnsweringRuleInfoForwardingRulesItemForwardingNumbersItemLabel',
    'AnsweringRuleInfoForwardingRulesItemForwardingNumbersItemType',
    'AnsweringRuleInfoGreetingsItem',
    'AnsweringRuleInfoGreetingsItemCustom',
    'AnsweringRuleInfoGreetingsItemPreset',
    'AnsweringRuleInfoGreetingsItemType',
    'AnsweringRuleInfoGreetingsItemUsageType',
    'AnsweringRuleInfoQueue',
    'AnsweringRuleInfoQueueFixedOrderAgentsItem',
    'AnsweringRuleInfoQueueFixedOrderAgentsItemExtension',
    'AnsweringRuleInfoQueueHoldAudioInterruptionMode',
    'AnsweringRuleInfoQueueHoldTimeExpirationAction',
    'AnsweringRuleInfoQueueMaxCallersAction',
    'AnsweringRuleInfoQueueNoAnswerAction',
    'AnsweringRuleInfoQueueTransferItem',
    'AnsweringRuleInfoQueueTransferItemAction',
    'AnsweringRuleInfoQueueTransferItemExtension',
    'AnsweringRuleInfoQueueTransferMode',
    'AnsweringRuleInfoSchedule',
    'AnsweringRuleInfoScheduleRangesItem',
    'AnsweringRuleInfoScheduleRef',
    'AnsweringRuleInfoScheduleWeeklyRanges',
    'AnsweringRuleInfoScheduleWeeklyRangesMondayItem',
    'AnsweringRuleInfoScreening',
    'AnsweringRuleInfoSharedLines',
    'AnsweringRuleInfoTransfer',
    'AnsweringRuleInfoTransferExtension',
    'AnsweringRuleInfoType',
    'AnsweringRuleInfoUnconditionalForwarding',
    'AnsweringRuleInfoUnconditionalForwardingAction',
    'AnsweringRuleInfoVoicemail',
    'AnsweringRuleInfoVoicemailRecipient',
    'AssignGlipGroupMembersRequest',
    'AssignGlipGroupMembersResponse',
    'AssignGlipGroupMembersResponseType',
    'AssignMultipleAutomaticaLocationUpdatesUsersRequest',
    'AssignMultipleCallQueueMembersRequest',
    'AssignMultipleDepartmentMembersRequest',
    'AssignMultipleDepartmentMembersRequestItemsItem',
    'AssignMultipleDevicesAutomaticLocationUpdates',
    'AssignMultipleDevicesAutomaticLocationUpdatesRequest',
    'AssignMultiplePagingGroupUsersDevicesRequest',
    'AssistantsResource',
    'AssistantsResourceRecordsItem',
    'AssistedUsersResource',
    'AssistedUsersResourceRecordsItem',
    'AuthProfileCheckResource',
    'AuthProfileResource',
    'AuthProfileResourcePermissionsItem',
    'AuthProfileResourcePermissionsItemEffectiveRole',
    'AuthProfileResourcePermissionsItemPermission',
    'AuthProfileResourcePermissionsItemPermissionSiteCompatible',
    'AuthProfileResourcePermissionsItemScopesItem',
    'AutomaticLocationUpdatesTaskInfo',
    'AutomaticLocationUpdatesTaskInfoResult',
    'AutomaticLocationUpdatesTaskInfoResultRecordsItem',
    'AutomaticLocationUpdatesTaskInfoResultRecordsItemErrorsItem',
    'AutomaticLocationUpdatesTaskInfoStatus',
    'AutomaticLocationUpdatesTaskInfoType',
    'AutomaticLocationUpdatesUserList',
    'AutomaticLocationUpdatesUserListRecordsItem',
    'AutomaticLocationUpdatesUserListRecordsItemType',
    'BlockedAllowedPhoneNumbersList',
    'BlockedAllowedPhoneNumbersListRecordsItem',
    'BlockedAllowedPhoneNumbersListRecordsItemStatus',
    'BridgeCallPartyRequest',
    'BridgeCallPartyResponse',
    'BridgeCallPartyResponseConferenceRole',
    'BridgeCallPartyResponseDirection',
    'BridgeCallPartyResponseFrom',
    'BridgeCallPartyResponseOwner',
    'BridgeCallPartyResponsePark',
    'BridgeCallPartyResponseRecordingsItem',
    'BridgeCallPartyResponseRingMeRole',
    'BridgeCallPartyResponseRingOutRole',
    'BridgeCallPartyResponseStatus',
    'BridgeCallPartyResponseStatusCode',
    'BridgeCallPartyResponseStatusPeerId',
    'BridgeCallPartyResponseStatusReason',
    'BridgeCallPartyResponseTo',
    'BridgeTargetRequest',
    'BulkAccountCallRecordingsResource',
    'BulkAccountCallRecordingsResourceAddedExtensionsItem',
    'BulkAccountCallRecordingsResourceAddedExtensionsItemCallDirection',
    'BulkAssignAutomaticLocationUpdatesUsers',
    'CallFlipPartyRequest',
    'CallLogSync',
    'CallLogSyncSyncInfo',
    'CallLogSyncSyncInfoSyncType',
    'CallMonitoringBulkAssign',
    'CallMonitoringBulkAssignAddedExtensionsItem',
    'CallMonitoringBulkAssignAddedExtensionsItemPermissionsItem',
    'CallMonitoringGroupMemberList',
    'CallMonitoringGroupMemberListRecordsItem',
    'CallMonitoringGroupMemberListRecordsItemPermissionsItem',
    'CallMonitoringGroups',
    'CallMonitoringGroupsRecordsItem',
    'CallParkPartyResponse',
    'CallParkPartyResponseConferenceRole',
    'CallParkPartyResponseDirection',
    'CallParkPartyResponseFrom',
    'CallParkPartyResponseOwner',
    'CallParkPartyResponsePark',
    'CallParkPartyResponseRecordingsItem',
    'CallParkPartyResponseRingMeRole',
    'CallParkPartyResponseRingOutRole',
    'CallParkPartyResponseStatus',
    'CallParkPartyResponseStatusCode',
    'CallParkPartyResponseStatusPeerId',
    'CallParkPartyResponseStatusReason',
    'CallParkPartyResponseTo',
    'CallPartyFlip',
    'CallPartyReply',
    'CallPartyReplyReplyWithPattern',
    'CallPartyReplyReplyWithPatternPattern',
    'CallPartyReplyReplyWithPatternTimeUnit',
    'CallQueueBulkAssignResource',
    'CallQueueDetails',
    'CallQueueDetailsStatus',
    'CallQueueMembers',
    'CallQueueMembersRecordsItem',
    'CallQueuePresence',
    'CallQueuePresenceRecordsItem',
    'CallQueuePresenceRecordsItemMember',
    'CallQueuePresenceRecordsItemMemberSite',
    'CallQueueUpdateDetails',
    'CallQueueUpdateDetailsServiceLevelSettings',
    'CallQueueUpdatePresence',
    'CallQueueUpdatePresenceRecordsItem',
    'CallQueueUpdatePresenceRecordsItemMember',
    'CallQueues',
    'CallRecording',
    'CallRecordingCustomGreetings',
    'CallRecordingCustomGreetingsRecordsItem',
    'CallRecordingCustomGreetingsRecordsItemCustom',
    'CallRecordingCustomGreetingsRecordsItemLanguage',
    'CallRecordingCustomGreetingsRecordsItemType',
    'CallRecordingExtensions',
    'CallRecordingExtensionsRecordsItem',
    'CallRecordingSettingsResource',
    'CallRecordingSettingsResourceAutomatic',
    'CallRecordingSettingsResourceGreetingsItem',
    'CallRecordingSettingsResourceGreetingsItemMode',
    'CallRecordingSettingsResourceGreetingsItemType',
    'CallRecordingSettingsResourceOnDemand',
    'CallRecordingUpdate',
    'CallSession',
    'CallSessionSession',
    'CallSessionSessionOrigin',
    'CallSessionSessionOriginType',
    'CallSessionSessionPartiesItem',
    'CallSessionSessionPartiesItemConferenceRole',
    'CallSessionSessionPartiesItemDirection',
    'CallSessionSessionPartiesItemPark',
    'CallSessionSessionPartiesItemRecordingsItem',
    'CallSessionSessionPartiesItemRingMeRole',
    'CallSessionSessionPartiesItemRingOutRole',
    'CallerBlockingSettings',
    'CallerBlockingSettingsMode',
    'CallerBlockingSettingsNoCallerId',
    'CallerBlockingSettingsPayPhones',
    'CallerBlockingSettingsUpdate',
    'CallerBlockingSettingsUpdateGreetingsItem',
    'CallerBlockingSettingsUpdateMode',
    'CallerBlockingSettingsUpdateNoCallerId',
    'CallerBlockingSettingsUpdatePayPhones',
    'CheckUserPermissionResponse',
    'CheckUserPermissionResponseDetails',
    'CheckUserPermissionResponseDetailsEffectiveRole',
    'CheckUserPermissionResponseDetailsPermission',
    'CheckUserPermissionResponseDetailsPermissionSiteCompatible',
    'CheckUserPermissionResponseDetailsScopesItem',
    'CompanyActiveCallsResponse',
    'CompanyAnsweringRuleInfo',
    'CompanyAnsweringRuleInfoCallHandlingAction',
    'CompanyAnsweringRuleInfoCalledNumbersItem',
    'CompanyAnsweringRuleInfoExtension',
    'CompanyAnsweringRuleInfoSchedule',
    'CompanyAnsweringRuleInfoScheduleRef',
    'CompanyAnsweringRuleInfoType',
    'CompanyAnsweringRuleList',
    'CompanyAnsweringRuleListRecordsItem',
    'CompanyAnsweringRuleListRecordsItemExtension',
    'CompanyAnsweringRuleListRecordsItemType',
    'CompanyAnsweringRuleRequest',
    'CompanyAnsweringRuleRequestCallHandlingAction',
    'CompanyAnsweringRuleRequestCalledNumbersItem',
    'CompanyAnsweringRuleRequestCallersItem',
    'CompanyAnsweringRuleRequestSchedule',
    'CompanyAnsweringRuleRequestScheduleRef',
    'CompanyAnsweringRuleRequestScheduleWeeklyRanges',
    'CompanyAnsweringRuleRequestScheduleWeeklyRangesMondayItem',
    'CompanyAnsweringRuleRequestType',
    'CompanyAnsweringRuleUpdate',
    'CompanyAnsweringRuleUpdateCallHandlingAction',
    'CompanyAnsweringRuleUpdateType',
    'CompanyBusinessHours',
    'CompanyBusinessHoursSchedule',
    'CompanyBusinessHoursUpdateRequest',
    'CompanyCallLogRecord',
    'CompanyCallLogRecordAction',
    'CompanyCallLogRecordDirection',
    'CompanyCallLogRecordReason',
    'CompanyCallLogRecordResult',
    'CompanyCallLogRecordTransport',
    'CompanyCallLogRecordType',
    'CompanyPhoneNumberInfo',
    'CompanyPhoneNumberInfoPaymentType',
    'CompanyPhoneNumberInfoTemporaryNumber',
    'CompanyPhoneNumberInfoType',
    'CompanyPhoneNumberInfoUsageType',
    'CompleteTaskRequest',
    'CompleteTaskRequestAssigneesItem',
    'CompleteTaskRequestStatus',
    'ContactList',
    'ContactListGroups',
    'ContactListNavigation',
    'ContactListNavigationFirstPage',
    'ContactListPaging',
    'ContactListRecordsItem',
    'ContactListRecordsItemAvailability',
    'ContactListRecordsItemBusinessAddress',
    'CreateAnsweringRuleRequest',
    'CreateAnsweringRuleRequest',
    'CreateAnsweringRuleRequestCallHandlingAction',
    'CreateAnsweringRuleRequestCallHandlingAction',
    'CreateAnsweringRuleRequestCalledNumbersItem',
    'CreateAnsweringRuleRequestCallersItem',
    'CreateAnsweringRuleRequestCallersItem',
    'CreateAnsweringRuleRequestForwarding',
    'CreateAnsweringRuleRequestForwardingRingingMode',
    'CreateAnsweringRuleRequestForwardingRulesItem',
    'CreateAnsweringRuleRequestForwardingRulesItemForwardingNumbersItem',
    'CreateAnsweringRuleRequestForwardingRulesItemForwardingNumbersItemLabel',
    'CreateAnsweringRuleRequestForwardingRulesItemForwardingNumbersItemType',
    'CreateAnsweringRuleRequestGreetingsItem',
    'CreateAnsweringRuleRequestGreetingsItemCustom',
    'CreateAnsweringRuleRequestGreetingsItemPreset',
    'CreateAnsweringRuleRequestGreetingsItemType',
    'CreateAnsweringRuleRequestGreetingsItemUsageType',
    'CreateAnsweringRuleRequestQueue',
    'CreateAnsweringRuleRequestQueueFixedOrderAgentsItem',
    'CreateAnsweringRuleRequestQueueFixedOrderAgentsItemExtension',
    'CreateAnsweringRuleRequestQueueHoldAudioInterruptionMode',
    'CreateAnsweringRuleRequestQueueHoldTimeExpirationAction',
    'CreateAnsweringRuleRequestQueueMaxCallersAction',
    'CreateAnsweringRuleRequestQueueNoAnswerAction',
    'CreateAnsweringRuleRequestQueueTransferItem',
    'CreateAnsweringRuleRequestQueueTransferItemAction',
    'CreateAnsweringRuleRequestQueueTransferItemExtension',
    'CreateAnsweringRuleRequestQueueTransferMode',
    'CreateAnsweringRuleRequestQueueUnconditionalForwardingItem',
    'CreateAnsweringRuleRequestQueueUnconditionalForwardingItemAction',
    'CreateAnsweringRuleRequestSchedule',
    'CreateAnsweringRuleRequestScheduleRangesItem',
    'CreateAnsweringRuleRequestScheduleRef',
    'CreateAnsweringRuleRequestScheduleWeeklyRanges',
    'CreateAnsweringRuleRequestScheduleWeeklyRangesFridayItem',
    'CreateAnsweringRuleRequestScheduleWeeklyRangesMondayItem',
    'CreateAnsweringRuleRequestScheduleWeeklyRangesSaturdayItem',
    'CreateAnsweringRuleRequestScheduleWeeklyRangesSundayItem',
    'CreateAnsweringRuleRequestScheduleWeeklyRangesThursdayItem',
    'CreateAnsweringRuleRequestScheduleWeeklyRangesTuesdayItem',
    'CreateAnsweringRuleRequestScheduleWeeklyRangesWednesdayItem',
    'CreateAnsweringRuleRequestScreening',
    'CreateAnsweringRuleRequestScreening',
    'CreateAnsweringRuleRequestTransfer',
    'CreateAnsweringRuleRequestTransferExtension',
    'CreateAnsweringRuleRequestUnconditionalForwarding',
    'CreateAnsweringRuleRequestUnconditionalForwardingAction',
    'CreateAnsweringRuleRequestVoicemail',
    'CreateAnsweringRuleRequestVoicemailRecipient',
    'CreateAnsweringRuleResponse',
    'CreateAnsweringRuleResponseCallHandlingAction',
    'CreateAnsweringRuleResponseCalledNumbersItem',
    'CreateAnsweringRuleResponseCallersItem',
    'CreateAnsweringRuleResponseForwarding',
    'CreateAnsweringRuleResponseForwardingRingingMode',
    'CreateAnsweringRuleResponseForwardingRulesItem',
    'CreateAnsweringRuleResponseForwardingRulesItemForwardingNumbersItem',
    'CreateAnsweringRuleResponseForwardingRulesItemForwardingNumbersItemLabel',
    'CreateAnsweringRuleResponseForwardingRulesItemForwardingNumbersItemType',
    'CreateAnsweringRuleResponseGreetingsItem',
    'CreateAnsweringRuleResponseGreetingsItemCustom',
    'CreateAnsweringRuleResponseGreetingsItemPreset',
    'CreateAnsweringRuleResponseGreetingsItemType',
    'CreateAnsweringRuleResponseGreetingsItemUsageType',
    'CreateAnsweringRuleResponseQueue',
    'CreateAnsweringRuleResponseQueueFixedOrderAgentsItem',
    'CreateAnsweringRuleResponseQueueFixedOrderAgentsItemExtension',
    'CreateAnsweringRuleResponseQueueHoldAudioInterruptionMode',
    'CreateAnsweringRuleResponseQueueHoldTimeExpirationAction',
    'CreateAnsweringRuleResponseQueueMaxCallersAction',
    'CreateAnsweringRuleResponseQueueNoAnswerAction',
    'CreateAnsweringRuleResponseQueueTransferItem',
    'CreateAnsweringRuleResponseQueueTransferItemAction',
    'CreateAnsweringRuleResponseQueueTransferItemExtension',
    'CreateAnsweringRuleResponseQueueTransferMode',
    'CreateAnsweringRuleResponseQueueUnconditionalForwardingItem',
    'CreateAnsweringRuleResponseQueueUnconditionalForwardingItemAction',
    'CreateAnsweringRuleResponseSchedule',
    'CreateAnsweringRuleResponseScheduleRangesItem',
    'CreateAnsweringRuleResponseScheduleRef',
    'CreateAnsweringRuleResponseScheduleWeeklyRanges',
    'CreateAnsweringRuleResponseScheduleWeeklyRangesFridayItem',
    'CreateAnsweringRuleResponseScheduleWeeklyRangesMondayItem',
    'CreateAnsweringRuleResponseScheduleWeeklyRangesSaturdayItem',
    'CreateAnsweringRuleResponseScheduleWeeklyRangesSundayItem',
    'CreateAnsweringRuleResponseScheduleWeeklyRangesThursdayItem',
    'CreateAnsweringRuleResponseScheduleWeeklyRangesTuesdayItem',
    'CreateAnsweringRuleResponseScheduleWeeklyRangesWednesdayItem',
    'CreateAnsweringRuleResponseScreening',
    'CreateAnsweringRuleResponseSharedLines',
    'CreateAnsweringRuleResponseTransfer',
    'CreateAnsweringRuleResponseTransferExtension',
    'CreateAnsweringRuleResponseType',
    'CreateAnsweringRuleResponseUnconditionalForwarding',
    'CreateAnsweringRuleResponseUnconditionalForwardingAction',
    'CreateAnsweringRuleResponseVoicemail',
    'CreateAnsweringRuleResponseVoicemailRecipient',
    'CreateBlockedAllowedNumberRequest',
    'CreateBlockedAllowedNumberRequestStatus',
    'CreateBlockedAllowedNumberResponse',
    'CreateBlockedAllowedNumberResponseStatus',
    'CreateCallMonitoringGroupRequest',
    'CreateCallMonitoringGroupRequest',
    'CreateCallMonitoringGroupResponse',
    'CreateCallOutCallSessionRequest',
    'CreateCallOutCallSessionRequestFrom',
    'CreateCallOutCallSessionRequestTo',
    'CreateCallOutCallSessionResponse',
    'CreateCallOutCallSessionResponseSession',
    'CreateCallOutCallSessionResponseSessionOrigin',
    'CreateCallOutCallSessionResponseSessionOriginType',
    'CreateCallOutCallSessionResponseSessionPartiesItem',
    'CreateCallOutCallSessionResponseSessionPartiesItemConferenceRole',
    'CreateCallOutCallSessionResponseSessionPartiesItemDirection',
    'CreateCallOutCallSessionResponseSessionPartiesItemFrom',
    'CreateCallOutCallSessionResponseSessionPartiesItemOwner',
    'CreateCallOutCallSessionResponseSessionPartiesItemPark',
    'CreateCallOutCallSessionResponseSessionPartiesItemRecordingsItem',
    'CreateCallOutCallSessionResponseSessionPartiesItemRingMeRole',
    'CreateCallOutCallSessionResponseSessionPartiesItemRingOutRole',
    'CreateCallOutCallSessionResponseSessionPartiesItemStatus',
    'CreateCallOutCallSessionResponseSessionPartiesItemStatusCode',
    'CreateCallOutCallSessionResponseSessionPartiesItemStatusPeerId',
    'CreateCallOutCallSessionResponseSessionPartiesItemStatusReason',
    'CreateCallOutCallSessionResponseSessionPartiesItemTo',
    'CreateChatNoteRequest',
    'CreateChatNoteResponse',
    'CreateChatNoteResponseCreator',
    'CreateChatNoteResponseLastModifiedBy',
    'CreateChatNoteResponseLockedBy',
    'CreateChatNoteResponseStatus',
    'CreateChatNoteResponseType',
    'CreateCompanyAnsweringRuleRequest',
    'CreateCompanyAnsweringRuleRequestCallHandlingAction',
    'CreateCompanyAnsweringRuleRequestCalledNumbersItem',
    'CreateCompanyAnsweringRuleRequestCallersItem',
    'CreateCompanyAnsweringRuleRequestGreetingsItem',
    'CreateCompanyAnsweringRuleRequestGreetingsItemCustom',
    'CreateCompanyAnsweringRuleRequestGreetingsItemPreset',
    'CreateCompanyAnsweringRuleRequestGreetingsItemType',
    'CreateCompanyAnsweringRuleRequestGreetingsItemUsageType',
    'CreateCompanyAnsweringRuleRequestSchedule',
    'CreateCompanyAnsweringRuleRequestScheduleRangesItem',
    'CreateCompanyAnsweringRuleRequestScheduleRef',
    'CreateCompanyAnsweringRuleRequestScheduleWeeklyRanges',
    'CreateCompanyAnsweringRuleRequestScheduleWeeklyRangesFridayItem',
    'CreateCompanyAnsweringRuleRequestScheduleWeeklyRangesMondayItem',
    'CreateCompanyAnsweringRuleRequestScheduleWeeklyRangesSaturdayItem',
    'CreateCompanyAnsweringRuleRequestScheduleWeeklyRangesSundayItem',
    'CreateCompanyAnsweringRuleRequestScheduleWeeklyRangesThursdayItem',
    'CreateCompanyAnsweringRuleRequestScheduleWeeklyRangesTuesdayItem',
    'CreateCompanyAnsweringRuleRequestScheduleWeeklyRangesWednesdayItem',
    'CreateCompanyAnsweringRuleRequestType',
    'CreateCompanyAnsweringRuleResponse',
    'CreateCompanyAnsweringRuleResponseCallHandlingAction',
    'CreateCompanyAnsweringRuleResponseCalledNumbersItem',
    'CreateCompanyAnsweringRuleResponseCallersItem',
    'CreateCompanyAnsweringRuleResponseExtension',
    'CreateCompanyAnsweringRuleResponseGreetingsItem',
    'CreateCompanyAnsweringRuleResponseGreetingsItemCustom',
    'CreateCompanyAnsweringRuleResponseGreetingsItemPreset',
    'CreateCompanyAnsweringRuleResponseGreetingsItemType',
    'CreateCompanyAnsweringRuleResponseGreetingsItemUsageType',
    'CreateCompanyAnsweringRuleResponseSchedule',
    'CreateCompanyAnsweringRuleResponseScheduleRangesItem',
    'CreateCompanyAnsweringRuleResponseScheduleRef',
    'CreateCompanyAnsweringRuleResponseScheduleWeeklyRanges',
    'CreateCompanyAnsweringRuleResponseScheduleWeeklyRangesFridayItem',
    'CreateCompanyAnsweringRuleResponseScheduleWeeklyRangesMondayItem',
    'CreateCompanyAnsweringRuleResponseScheduleWeeklyRangesSaturdayItem',
    'CreateCompanyAnsweringRuleResponseScheduleWeeklyRangesSundayItem',
    'CreateCompanyAnsweringRuleResponseScheduleWeeklyRangesThursdayItem',
    'CreateCompanyAnsweringRuleResponseScheduleWeeklyRangesTuesdayItem',
    'CreateCompanyAnsweringRuleResponseScheduleWeeklyRangesWednesdayItem',
    'CreateCompanyAnsweringRuleResponseType',
    'CreateCompanyGreetingRequest',
    'CreateCompanyGreetingRequestType',
    'CreateCompanyGreetingResponse',
    'CreateCompanyGreetingResponseAnsweringRule',
    'CreateCompanyGreetingResponseContentType',
    'CreateCompanyGreetingResponseLanguage',
    'CreateCompanyGreetingResponseType',
    'CreateContactRequest',
    'CreateContactRequestBusinessAddress',
    'CreateContactRequestHomeAddress',
    'CreateContactRequestOtherAddress',
    'CreateContactResponse',
    'CreateContactResponseAvailability',
    'CreateContactResponseBusinessAddress',
    'CreateContactResponseHomeAddress',
    'CreateContactResponseOtherAddress',
    'CreateCustomFieldRequest',
    'CreateCustomFieldRequestCategory',
    'CreateCustomFieldResponse',
    'CreateCustomFieldResponseCategory',
    'CreateCustomUserGreetingRequest',
    'CreateCustomUserGreetingRequestType',
    'CreateCustomUserGreetingResponse',
    'CreateCustomUserGreetingResponseAnsweringRule',
    'CreateCustomUserGreetingResponseContentType',
    'CreateCustomUserGreetingResponseType',
    'CreateDataExportTaskRequest',
    'CreateDataExportTaskRequest',
    'CreateDataExportTaskRequestContactsItem',
    'CreateDataExportTaskResponse',
    'CreateDataExportTaskResponseCreator',
    'CreateDataExportTaskResponseDatasetsItem',
    'CreateDataExportTaskResponseSpecific',
    'CreateDataExportTaskResponseSpecificContactsItem',
    'CreateDataExportTaskResponseStatus',
    'CreateEmergencyLocationRequest',
    'CreateEmergencyLocationRequestAddress',
    'CreateEmergencyLocationRequestAddressStatus',
    'CreateEmergencyLocationRequestOwnersItem',
    'CreateEmergencyLocationRequestSite',
    'CreateEmergencyLocationRequestUsageStatus',
    'CreateEmergencyLocationRequestVisibility',
    'CreateEventRequest',
    'CreateEventRequestColor',
    'CreateEventRequestEndingOn',
    'CreateEventRequestRecurrence',
    'CreateEventResponse',
    'CreateEventResponseColor',
    'CreateEventResponseEndingOn',
    'CreateEventResponseRecurrence',
    'CreateEventbyGroupIdResponse',
    'CreateEventbyGroupIdResponseColor',
    'CreateEventbyGroupIdResponseEndingOn',
    'CreateEventbyGroupIdResponseRecurrence',
    'CreateExtensionRequest',
    'CreateExtensionRequestContact',
    'CreateExtensionRequestContactBusinessAddress',
    'CreateExtensionRequestContactPronouncedName',
    'CreateExtensionRequestContactPronouncedNamePrompt',
    'CreateExtensionRequestContactPronouncedNamePromptContentType',
    'CreateExtensionRequestContactPronouncedNameType',
    'CreateExtensionRequestCustomFieldsItem',
    'CreateExtensionRequestReferencesItem',
    'CreateExtensionRequestReferencesItemType',
    'CreateExtensionRequestRegionalSettings',
    'CreateExtensionRequestRegionalSettingsFormattingLocale',
    'CreateExtensionRequestRegionalSettingsGreetingLanguage',
    'CreateExtensionRequestRegionalSettingsHomeCountry',
    'CreateExtensionRequestRegionalSettingsLanguage',
    'CreateExtensionRequestRegionalSettingsTimeFormat',
    'CreateExtensionRequestRegionalSettingsTimezone',
    'CreateExtensionRequestSetupWizardState',
    'CreateExtensionRequestSite',
    'CreateExtensionRequestSiteBusinessAddress',
    'CreateExtensionRequestSiteOperator',
    'CreateExtensionRequestSiteRegionalSettings',
    'CreateExtensionRequestSiteRegionalSettingsFormattingLocale',
    'CreateExtensionRequestSiteRegionalSettingsGreetingLanguage',
    'CreateExtensionRequestSiteRegionalSettingsHomeCountry',
    'CreateExtensionRequestSiteRegionalSettingsLanguage',
    'CreateExtensionRequestSiteRegionalSettingsTimeFormat',
    'CreateExtensionRequestSiteRegionalSettingsTimezone',
    'CreateExtensionRequestStatus',
    'CreateExtensionRequestStatusInfo',
    'CreateExtensionRequestStatusInfoReason',
    'CreateExtensionRequestType',
    'CreateExtensionResponse',
    'CreateExtensionResponseContact',
    'CreateExtensionResponseContactBusinessAddress',
    'CreateExtensionResponseContactPronouncedName',
    'CreateExtensionResponseContactPronouncedNamePrompt',
    'CreateExtensionResponseContactPronouncedNamePromptContentType',
    'CreateExtensionResponseContactPronouncedNameType',
    'CreateExtensionResponseCustomFieldsItem',
    'CreateExtensionResponsePermissions',
    'CreateExtensionResponsePermissionsAdmin',
    'CreateExtensionResponsePermissionsInternationalCalling',
    'CreateExtensionResponseProfileImage',
    'CreateExtensionResponseProfileImageScalesItem',
    'CreateExtensionResponseReferencesItem',
    'CreateExtensionResponseReferencesItemType',
    'CreateExtensionResponseRegionalSettings',
    'CreateExtensionResponseRegionalSettingsFormattingLocale',
    'CreateExtensionResponseRegionalSettingsGreetingLanguage',
    'CreateExtensionResponseRegionalSettingsHomeCountry',
    'CreateExtensionResponseRegionalSettingsLanguage',
    'CreateExtensionResponseRegionalSettingsTimeFormat',
    'CreateExtensionResponseRegionalSettingsTimezone',
    'CreateExtensionResponseServiceFeaturesItem',
    'CreateExtensionResponseServiceFeaturesItemFeatureName',
    'CreateExtensionResponseSetupWizardState',
    'CreateExtensionResponseSite',
    'CreateExtensionResponseStatus',
    'CreateExtensionResponseStatusInfo',
    'CreateExtensionResponseStatusInfoReason',
    'CreateExtensionResponseType',
    'CreateFaxMessageRequest',
    'CreateFaxMessageRequestFaxResolution',
    'CreateFaxMessageResponse',
    'CreateFaxMessageResponseAttachmentsItem',
    'CreateFaxMessageResponseAttachmentsItemType',
    'CreateFaxMessageResponseAvailability',
    'CreateFaxMessageResponseDirection',
    'CreateFaxMessageResponseFaxResolution',
    'CreateFaxMessageResponseFrom',
    'CreateFaxMessageResponseMessageStatus',
    'CreateFaxMessageResponsePriority',
    'CreateFaxMessageResponseReadStatus',
    'CreateFaxMessageResponseToItem',
    'CreateFaxMessageResponseToItemFaxErrorCode',
    'CreateFaxMessageResponseToItemMessageStatus',
    'CreateForwardingNumberRequest',
    'CreateForwardingNumberRequest',
    'CreateForwardingNumberRequestDevice',
    'CreateForwardingNumberRequestType',
    'CreateForwardingNumberRequestType',
    'CreateForwardingNumberResponse',
    'CreateForwardingNumberResponseDevice',
    'CreateForwardingNumberResponseFeaturesItem',
    'CreateForwardingNumberResponseLabel',
    'CreateForwardingNumberResponseType',
    'CreateGlipCardRequest',
    'CreateGlipCardRequestAuthor',
    'CreateGlipCardRequestFieldsItem',
    'CreateGlipCardRequestFieldsItemStyle',
    'CreateGlipCardRequestFootnote',
    'CreateGlipCardRequestRecurrence',
    'CreateGlipCardRequestType',
    'CreateGlipCardResponse',
    'CreateGlipCardResponseAuthor',
    'CreateGlipCardResponseColor',
    'CreateGlipCardResponseEndingOn',
    'CreateGlipCardResponseFieldsItem',
    'CreateGlipCardResponseFieldsItemStyle',
    'CreateGlipCardResponseFootnote',
    'CreateGlipCardResponseRecurrence',
    'CreateGlipCardResponseType',
    'CreateGlipConversationRequest',
    'CreateGlipConversationRequest',
    'CreateGlipConversationRequestMembersItem',
    'CreateGlipConversationResponse',
    'CreateGlipConversationResponse',
    'CreateGlipConversationResponseMembersItem',
    'CreateGlipConversationResponseMembersItem',
    'CreateGlipConversationResponseType',
    'CreateGlipConversationResponseType',
    'CreateGlipGroupPostRequest',
    'CreateGlipGroupPostRequestAttachmentsItem',
    'CreateGlipGroupPostRequestAttachmentsItemAuthor',
    'CreateGlipGroupPostRequestAttachmentsItemFieldsItem',
    'CreateGlipGroupPostRequestAttachmentsItemFieldsItemStyle',
    'CreateGlipGroupPostRequestAttachmentsItemFootnote',
    'CreateGlipGroupPostRequestAttachmentsItemRecurrence',
    'CreateGlipGroupPostRequestAttachmentsItemType',
    'CreateGlipGroupPostResponse',
    'CreateGlipGroupPostResponseAttachmentsItem',
    'CreateGlipGroupPostResponseAttachmentsItemAuthor',
    'CreateGlipGroupPostResponseAttachmentsItemColor',
    'CreateGlipGroupPostResponseAttachmentsItemEndingOn',
    'CreateGlipGroupPostResponseAttachmentsItemFieldsItem',
    'CreateGlipGroupPostResponseAttachmentsItemFieldsItemStyle',
    'CreateGlipGroupPostResponseAttachmentsItemFootnote',
    'CreateGlipGroupPostResponseAttachmentsItemRecurrence',
    'CreateGlipGroupPostResponseAttachmentsItemType',
    'CreateGlipGroupPostResponseMentionsItem',
    'CreateGlipGroupPostResponseMentionsItemType',
    'CreateGlipGroupPostResponseType',
    'CreateGlipGroupRequest',
    'CreateGlipGroupRequestMembersItem',
    'CreateGlipGroupRequestType',
    'CreateGlipGroupResponse',
    'CreateGlipGroupResponseType',
    'CreateGlipGroupWebhookResponse',
    'CreateGlipGroupWebhookResponseStatus',
    'CreateGlipPostRequest',
    'CreateGlipPostRequestAttachmentsItem',
    'CreateGlipPostRequestAttachmentsItemType',
    'CreateGlipPostResponse',
    'CreateGlipPostResponseAttachmentsItem',
    'CreateGlipPostResponseAttachmentsItemAuthor',
    'CreateGlipPostResponseAttachmentsItemColor',
    'CreateGlipPostResponseAttachmentsItemEndingOn',
    'CreateGlipPostResponseAttachmentsItemFieldsItem',
    'CreateGlipPostResponseAttachmentsItemFieldsItemStyle',
    'CreateGlipPostResponseAttachmentsItemFootnote',
    'CreateGlipPostResponseAttachmentsItemRecurrence',
    'CreateGlipPostResponseAttachmentsItemType',
    'CreateGlipPostResponseMentionsItem',
    'CreateGlipPostResponseMentionsItemType',
    'CreateGlipPostResponseType',
    'CreateGlipTeamRequest',
    'CreateGlipTeamRequestMembersItem',
    'CreateGlipTeamResponse',
    'CreateGlipTeamResponseStatus',
    'CreateGlipTeamResponseType',
    'CreateIVRMenuRequest',
    'CreateIVRMenuRequestActionsItem',
    'CreateIVRMenuRequestActionsItemAction',
    'CreateIVRMenuRequestActionsItemExtension',
    'CreateIVRMenuRequestPrompt',
    'CreateIVRMenuRequestPromptAudio',
    'CreateIVRMenuRequestPromptLanguage',
    'CreateIVRMenuRequestPromptMode',
    'CreateIVRMenuResponse',
    'CreateIVRMenuResponseActionsItem',
    'CreateIVRMenuResponseActionsItemAction',
    'CreateIVRMenuResponseActionsItemExtension',
    'CreateIVRMenuResponsePrompt',
    'CreateIVRMenuResponsePromptAudio',
    'CreateIVRMenuResponsePromptLanguage',
    'CreateIVRMenuResponsePromptMode',
    'CreateIVRPromptRequest',
    'CreateIVRPromptResponse',
    'CreateInternalTextMessageRequest',
    'CreateInternalTextMessageRequest',
    'CreateInternalTextMessageRequestFrom',
    'CreateInternalTextMessageRequestFrom',
    'CreateInternalTextMessageRequestToItem',
    'CreateInternalTextMessageResponse',
    'CreateInternalTextMessageResponseAttachmentsItem',
    'CreateInternalTextMessageResponseAttachmentsItemType',
    'CreateInternalTextMessageResponseAvailability',
    'CreateInternalTextMessageResponseConversation',
    'CreateInternalTextMessageResponseDirection',
    'CreateInternalTextMessageResponseFaxResolution',
    'CreateInternalTextMessageResponseFrom',
    'CreateInternalTextMessageResponseMessageStatus',
    'CreateInternalTextMessageResponsePriority',
    'CreateInternalTextMessageResponseReadStatus',
    'CreateInternalTextMessageResponseToItem',
    'CreateInternalTextMessageResponseToItemFaxErrorCode',
    'CreateInternalTextMessageResponseToItemMessageStatus',
    'CreateInternalTextMessageResponseType',
    'CreateInternalTextMessageResponseVmTranscriptionStatus',
    'CreateMMSRequest',
    'CreateMMSResponse',
    'CreateMMSResponseAttachmentsItem',
    'CreateMMSResponseAttachmentsItemType',
    'CreateMMSResponseAvailability',
    'CreateMMSResponseConversation',
    'CreateMMSResponseDirection',
    'CreateMMSResponseFaxResolution',
    'CreateMMSResponseFrom',
    'CreateMMSResponseMessageStatus',
    'CreateMMSResponsePriority',
    'CreateMMSResponseReadStatus',
    'CreateMMSResponseToItem',
    'CreateMMSResponseToItemFaxErrorCode',
    'CreateMMSResponseToItemMessageStatus',
    'CreateMMSResponseType',
    'CreateMMSResponseVmTranscriptionStatus',
    'CreateMeetingRequest',
    'CreateMeetingRequestAutoRecordType',
    'CreateMeetingRequestHost',
    'CreateMeetingRequestMeetingType',
    'CreateMeetingRequestRecurrence',
    'CreateMeetingRequestRecurrenceFrequency',
    'CreateMeetingRequestRecurrenceMonthlyByWeek',
    'CreateMeetingRequestRecurrenceWeeklyByDay',
    'CreateMeetingRequestRecurrenceWeeklyByDays',
    'CreateMeetingRequestSchedule',
    'CreateMeetingRequestScheduleTimeZone',
    'CreateMeetingResponse',
    'CreateMeetingResponseHost',
    'CreateMeetingResponseLinks',
    'CreateMeetingResponseMeetingType',
    'CreateMeetingResponseOccurrencesItem',
    'CreateMeetingResponseSchedule',
    'CreateMeetingResponseScheduleTimeZone',
    'CreateMessageStoreReportRequest',
    'CreateMessageStoreReportRequest',
    'CreateMessageStoreReportResponse',
    'CreateMessageStoreReportResponseStatus',
    'CreateMultipleSwitchesRequest',
    'CreateMultipleSwitchesRequest',
    'CreateMultipleSwitchesRequestRecordsItem',
    'CreateMultipleSwitchesRequestRecordsItem',
    'CreateMultipleSwitchesRequestRecordsItemEmergencyAddress',
    'CreateMultipleSwitchesRequestRecordsItemEmergencyLocation',
    'CreateMultipleSwitchesRequestRecordsItemSite',
    'CreateMultipleSwitchesResponse',
    'CreateMultipleSwitchesResponse',
    'CreateMultipleSwitchesResponseTask',
    'CreateMultipleSwitchesResponseTaskStatus',
    'CreateMultipleWirelessPointsRequest',
    'CreateMultipleWirelessPointsRequest',
    'CreateMultipleWirelessPointsRequestRecordsItem',
    'CreateMultipleWirelessPointsRequestRecordsItem',
    'CreateMultipleWirelessPointsRequestRecordsItemEmergencyAddress',
    'CreateMultipleWirelessPointsRequestRecordsItemEmergencyLocation',
    'CreateMultipleWirelessPointsRequestRecordsItemSite',
    'CreateMultipleWirelessPointsResponse',
    'CreateMultipleWirelessPointsResponse',
    'CreateMultipleWirelessPointsResponseTask',
    'CreateMultipleWirelessPointsResponseTaskStatus',
    'CreateNetworkRequest',
    'CreateNetworkRequest',
    'CreateNetworkRequestEmergencyLocation',
    'CreateNetworkRequestPrivateIpRangesItem',
    'CreateNetworkRequestPrivateIpRangesItem',
    'CreateNetworkRequestPrivateIpRangesItemEmergencyAddress',
    'CreateNetworkRequestPublicIpRangesItem',
    'CreateNetworkRequestPublicIpRangesItem',
    'CreateNetworkRequestSite',
    'CreateNetworkResponse',
    'CreateNetworkResponseEmergencyLocation',
    'CreateNetworkResponsePrivateIpRangesItem',
    'CreateNetworkResponsePrivateIpRangesItemEmergencyAddress',
    'CreateNetworkResponsePublicIpRangesItem',
    'CreateNetworkResponseSite',
    'CreatePostRequest',
    'CreatePostRequestAttachmentsItem',
    'CreatePostRequestAttachmentsItemAuthor',
    'CreatePostRequestAttachmentsItemFieldsItem',
    'CreatePostRequestAttachmentsItemFieldsItemStyle',
    'CreatePostRequestAttachmentsItemFootnote',
    'CreatePostRequestAttachmentsItemRecurrence',
    'CreatePostRequestAttachmentsItemType',
    'CreatePostResponse',
    'CreatePostResponseAttachmentsItem',
    'CreatePostResponseAttachmentsItemAuthor',
    'CreatePostResponseAttachmentsItemColor',
    'CreatePostResponseAttachmentsItemEndingOn',
    'CreatePostResponseAttachmentsItemFieldsItem',
    'CreatePostResponseAttachmentsItemFieldsItemStyle',
    'CreatePostResponseAttachmentsItemFootnote',
    'CreatePostResponseAttachmentsItemRecurrence',
    'CreatePostResponseAttachmentsItemType',
    'CreatePostResponseMentionsItem',
    'CreatePostResponseMentionsItemType',
    'CreatePostResponseType',
    'CreateRingOutCallDeprecatedResponse',
    'CreateRingOutCallDeprecatedResponseStatus',
    'CreateRingOutCallDeprecatedResponseStatusCallStatus',
    'CreateRingOutCallDeprecatedResponseStatusCalleeStatus',
    'CreateRingOutCallDeprecatedResponseStatusCallerStatus',
    'CreateRingOutCallRequest',
    'CreateRingOutCallRequestCallerId',
    'CreateRingOutCallRequestCountry',
    'CreateRingOutCallRequestFrom',
    'CreateRingOutCallRequestTo',
    'CreateRingOutCallResponse',
    'CreateRingOutCallResponseStatus',
    'CreateRingOutCallResponseStatusCallStatus',
    'CreateRingOutCallResponseStatusCalleeStatus',
    'CreateRingOutCallResponseStatusCallerStatus',
    'CreateSIPRegistrationRequest',
    'CreateSIPRegistrationRequestDevice',
    'CreateSIPRegistrationRequestSipInfoItem',
    'CreateSIPRegistrationRequestSipInfoItemTransport',
    'CreateSIPRegistrationResponse',
    'CreateSIPRegistrationResponseDevice',
    'CreateSIPRegistrationResponseDeviceEmergency',
    'CreateSIPRegistrationResponseDeviceEmergencyAddress',
    'CreateSIPRegistrationResponseDeviceEmergencyAddressEditableStatus',
    'CreateSIPRegistrationResponseDeviceEmergencyAddressStatus',
    'CreateSIPRegistrationResponseDeviceEmergencyLocation',
    'CreateSIPRegistrationResponseDeviceEmergencyServiceAddress',
    'CreateSIPRegistrationResponseDeviceEmergencySyncStatus',
    'CreateSIPRegistrationResponseDeviceExtension',
    'CreateSIPRegistrationResponseDeviceLinePooling',
    'CreateSIPRegistrationResponseDeviceModel',
    'CreateSIPRegistrationResponseDeviceModelAddonsItem',
    'CreateSIPRegistrationResponseDeviceModelFeaturesItem',
    'CreateSIPRegistrationResponseDevicePhoneLinesItem',
    'CreateSIPRegistrationResponseDevicePhoneLinesItemEmergencyAddress',
    'CreateSIPRegistrationResponseDevicePhoneLinesItemLineType',
    'CreateSIPRegistrationResponseDevicePhoneLinesItemPhoneInfo',
    'CreateSIPRegistrationResponseDevicePhoneLinesItemPhoneInfoCountry',
    'CreateSIPRegistrationResponseDevicePhoneLinesItemPhoneInfoPaymentType',
    'CreateSIPRegistrationResponseDevicePhoneLinesItemPhoneInfoType',
    'CreateSIPRegistrationResponseDevicePhoneLinesItemPhoneInfoUsageType',
    'CreateSIPRegistrationResponseDeviceShipping',
    'CreateSIPRegistrationResponseDeviceShippingAddress',
    'CreateSIPRegistrationResponseDeviceShippingMethod',
    'CreateSIPRegistrationResponseDeviceSite',
    'CreateSIPRegistrationResponseDeviceStatus',
    'CreateSIPRegistrationResponseDeviceType',
    'CreateSIPRegistrationResponseSipFlags',
    'CreateSIPRegistrationResponseSipFlagsOutboundCallsEnabled',
    'CreateSIPRegistrationResponseSipFlagsVoipCountryBlocked',
    'CreateSIPRegistrationResponseSipFlagsVoipFeatureEnabled',
    'CreateSIPRegistrationResponseSipInfoItem',
    'CreateSIPRegistrationResponseSipInfoItemTransport',
    'CreateSIPRegistrationResponseSipInfoPstnItem',
    'CreateSIPRegistrationResponseSipInfoPstnItemTransport',
    'CreateSMSMessageRequest',
    'CreateSMSMessageRequest',
    'CreateSMSMessageRequestCountry',
    'CreateSMSMessageRequestCountry',
    'CreateSMSMessageRequestFrom',
    'CreateSMSMessageRequestFrom',
    'CreateSMSMessageRequestToItem',
    'CreateSMSMessageResponse',
    'CreateSMSMessageResponseAttachmentsItem',
    'CreateSMSMessageResponseAttachmentsItemType',
    'CreateSMSMessageResponseAvailability',
    'CreateSMSMessageResponseConversation',
    'CreateSMSMessageResponseDirection',
    'CreateSMSMessageResponseFaxResolution',
    'CreateSMSMessageResponseFrom',
    'CreateSMSMessageResponseMessageStatus',
    'CreateSMSMessageResponsePriority',
    'CreateSMSMessageResponseReadStatus',
    'CreateSMSMessageResponseToItem',
    'CreateSMSMessageResponseToItemFaxErrorCode',
    'CreateSMSMessageResponseToItemMessageStatus',
    'CreateSMSMessageResponseType',
    'CreateSMSMessageResponseVmTranscriptionStatus',
    'CreateSipRegistrationRequest',
    'CreateSipRegistrationRequestDevice',
    'CreateSipRegistrationRequestSipInfoItem',
    'CreateSipRegistrationRequestSipInfoItemTransport',
    'CreateSipRegistrationResponse',
    'CreateSipRegistrationResponseDevice',
    'CreateSipRegistrationResponseDeviceEmergency',
    'CreateSipRegistrationResponseDeviceEmergencyAddressEditableStatus',
    'CreateSipRegistrationResponseDeviceEmergencyAddressStatus',
    'CreateSipRegistrationResponseDeviceEmergencyLocation',
    'CreateSipRegistrationResponseDeviceEmergencyServiceAddress',
    'CreateSipRegistrationResponseDeviceEmergencySyncStatus',
    'CreateSipRegistrationResponseDeviceExtension',
    'CreateSipRegistrationResponseDeviceLinePooling',
    'CreateSipRegistrationResponseDeviceModel',
    'CreateSipRegistrationResponseDeviceModelAddonsItem',
    'CreateSipRegistrationResponseDeviceModelFeaturesItem',
    'CreateSipRegistrationResponseDevicePhoneLinesItem',
    'CreateSipRegistrationResponseDevicePhoneLinesItemEmergencyAddress',
    'CreateSipRegistrationResponseDevicePhoneLinesItemLineType',
    'CreateSipRegistrationResponseDevicePhoneLinesItemPhoneInfo',
    'CreateSipRegistrationResponseDevicePhoneLinesItemPhoneInfoCountry',
    'CreateSipRegistrationResponseDevicePhoneLinesItemPhoneInfoPaymentType',
    'CreateSipRegistrationResponseDevicePhoneLinesItemPhoneInfoType',
    'CreateSipRegistrationResponseDevicePhoneLinesItemPhoneInfoUsageType',
    'CreateSipRegistrationResponseDeviceShipping',
    'CreateSipRegistrationResponseDeviceShippingMethod',
    'CreateSipRegistrationResponseDeviceSite',
    'CreateSipRegistrationResponseDeviceStatus',
    'CreateSipRegistrationResponseDeviceType',
    'CreateSipRegistrationResponseSipFlags',
    'CreateSipRegistrationResponseSipFlagsOutboundCallsEnabled',
    'CreateSipRegistrationResponseSipFlagsVoipCountryBlocked',
    'CreateSipRegistrationResponseSipFlagsVoipFeatureEnabled',
    'CreateSipRegistrationResponseSipInfoItem',
    'CreateSipRegistrationResponseSipInfoItemTransport',
    'CreateSubscriptionRequest',
    'CreateSubscriptionRequest',
    'CreateSubscriptionRequestDeliveryMode',
    'CreateSubscriptionRequestDeliveryMode',
    'CreateSubscriptionRequestDeliveryModeTransportType',
    'CreateSubscriptionRequestDeliveryModeTransportType',
    'CreateSubscriptionResponse',
    'CreateSubscriptionResponseBlacklistedData',
    'CreateSubscriptionResponseDeliveryMode',
    'CreateSubscriptionResponseDeliveryModeTransportType',
    'CreateSubscriptionResponseDisabledFiltersItem',
    'CreateSubscriptionResponseStatus',
    'CreateSubscriptionResponseTransportType',
    'CreateSwitchRequest',
    'CreateSwitchRequestEmergencyAddress',
    'CreateSwitchRequestEmergencyLocation',
    'CreateSwitchRequestSite',
    'CreateSwitchResponse',
    'CreateSwitchResponseEmergencyAddress',
    'CreateSwitchResponseEmergencyLocation',
    'CreateSwitchResponseSite',
    'CreateTaskRequest',
    'CreateTaskRequestAssigneesItem',
    'CreateTaskRequestAttachmentsItem',
    'CreateTaskRequestAttachmentsItemType',
    'CreateTaskRequestColor',
    'CreateTaskRequestCompletenessCondition',
    'CreateTaskRequestRecurrence',
    'CreateTaskRequestRecurrenceEndingCondition',
    'CreateTaskRequestRecurrenceSchedule',
    'CreateTaskResponse',
    'CreateTaskResponseAssigneesItem',
    'CreateTaskResponseAssigneesItemStatus',
    'CreateTaskResponseAttachmentsItem',
    'CreateTaskResponseAttachmentsItemType',
    'CreateTaskResponseColor',
    'CreateTaskResponseCompletenessCondition',
    'CreateTaskResponseCreator',
    'CreateTaskResponseRecurrence',
    'CreateTaskResponseRecurrenceEndingCondition',
    'CreateTaskResponseRecurrenceSchedule',
    'CreateTaskResponseStatus',
    'CreateTaskResponseType',
    'CreateUser',
    'CreateUser2Request',
    'CreateUser2RequestAddressesItem',
    'CreateUser2RequestAddressesItemType',
    'CreateUser2RequestEmailsItem',
    'CreateUser2RequestEmailsItemType',
    'CreateUser2RequestName',
    'CreateUser2RequestPhoneNumbersItem',
    'CreateUser2RequestPhoneNumbersItemType',
    'CreateUser2RequestPhotosItem',
    'CreateUser2RequestPhotosItemType',
    'CreateUser2RequestSchemasItem',
    'CreateUser2RequestUrnIetfParamsScimSchemasExtensionEnterprise_2_0_User',
    'CreateUser2Response',
    'CreateUser2Response',
    'CreateUser2Response',
    'CreateUser2Response',
    'CreateUser2Response',
    'CreateUser2Response',
    'CreateUser2Response',
    'CreateUser2Response',
    'CreateUser2ResponseAddressesItem',
    'CreateUser2ResponseAddressesItemType',
    'CreateUser2ResponseEmailsItem',
    'CreateUser2ResponseEmailsItemType',
    'CreateUser2ResponseMeta',
    'CreateUser2ResponseMetaResourceType',
    'CreateUser2ResponseName',
    'CreateUser2ResponsePhoneNumbersItem',
    'CreateUser2ResponsePhoneNumbersItemType',
    'CreateUser2ResponsePhotosItem',
    'CreateUser2ResponsePhotosItemType',
    'CreateUser2ResponseSchemasItem',
    'CreateUser2ResponseSchemasItem',
    'CreateUser2ResponseSchemasItem',
    'CreateUser2ResponseSchemasItem',
    'CreateUser2ResponseSchemasItem',
    'CreateUser2ResponseSchemasItem',
    'CreateUser2ResponseSchemasItem',
    'CreateUser2ResponseSchemasItem',
    'CreateUser2ResponseScimType',
    'CreateUser2ResponseScimType',
    'CreateUser2ResponseScimType',
    'CreateUser2ResponseScimType',
    'CreateUser2ResponseScimType',
    'CreateUser2ResponseScimType',
    'CreateUser2ResponseScimType',
    'CreateUser2ResponseUrnIetfParamsScimSchemasExtensionEnterprise_2_0_User',
    'CreateUserProfileImageRequest',
    'CreateUserRequest',
    'CreateUserRequestAddressesItem',
    'CreateUserRequestAddressesItemType',
    'CreateUserRequestEmailsItem',
    'CreateUserRequestEmailsItemType',
    'CreateUserRequestName',
    'CreateUserRequestPhoneNumbersItem',
    'CreateUserRequestPhoneNumbersItemType',
    'CreateUserRequestPhotosItem',
    'CreateUserRequestPhotosItemType',
    'CreateUserRequestSchemasItem',
    'CreateUserRequestUrnIetfParamsScimSchemasExtensionEnterprise_2_0_User',
    'CreateUserResponse',
    'CreateUserResponse',
    'CreateUserResponse',
    'CreateUserResponse',
    'CreateUserResponse',
    'CreateUserResponse',
    'CreateUserResponse',
    'CreateUserResponse',
    'CreateUserResponseAddressesItem',
    'CreateUserResponseAddressesItemType',
    'CreateUserResponseEmailsItem',
    'CreateUserResponseEmailsItemType',
    'CreateUserResponseMeta',
    'CreateUserResponseMetaResourceType',
    'CreateUserResponseName',
    'CreateUserResponsePhoneNumbersItem',
    'CreateUserResponsePhoneNumbersItemType',
    'CreateUserResponsePhotosItem',
    'CreateUserResponsePhotosItemType',
    'CreateUserResponseSchemasItem',
    'CreateUserResponseSchemasItem',
    'CreateUserResponseSchemasItem',
    'CreateUserResponseSchemasItem',
    'CreateUserResponseSchemasItem',
    'CreateUserResponseSchemasItem',
    'CreateUserResponseSchemasItem',
    'CreateUserResponseSchemasItem',
    'CreateUserResponseScimType',
    'CreateUserResponseScimType',
    'CreateUserResponseScimType',
    'CreateUserResponseScimType',
    'CreateUserResponseScimType',
    'CreateUserResponseScimType',
    'CreateUserResponseScimType',
    'CreateUserResponseUrnIetfParamsScimSchemasExtensionEnterprise_2_0_User',
    'CreateUserSchemasItem',
    'CreateWirelessPointRequest',
    'CreateWirelessPointRequestEmergencyAddress',
    'CreateWirelessPointRequestEmergencyLocation',
    'CreateWirelessPointRequestSite',
    'CreateWirelessPointResponse',
    'CreateWirelessPointResponseEmergencyAddress',
    'CreateWirelessPointResponseEmergencyLocation',
    'CreateWirelessPointResponseSite',
    'CustomAnsweringRuleInfo',
    'CustomAnsweringRuleInfoCallHandlingAction',
    'CustomAnsweringRuleInfoScreening',
    'CustomAnsweringRuleInfoType',
    'CustomCompanyGreetingInfo',
    'CustomCompanyGreetingInfoAnsweringRule',
    'CustomCompanyGreetingInfoContentType',
    'CustomCompanyGreetingInfoLanguage',
    'CustomCompanyGreetingInfoType',
    'CustomFieldCreateRequest',
    'CustomFieldCreateRequestCategory',
    'CustomFieldUpdateRequest',
    'CustomFieldsResource',
    'CustomFieldsResourceRecordsItem',
    'CustomFieldsResourceRecordsItemCategory',
    'CustomUserGreetingInfo',
    'CustomUserGreetingInfoContentType',
    'CustomUserGreetingInfoType',
    'DataExportTask',
    'DataExportTaskDatasetsItem',
    'DataExportTaskList',
    'DataExportTaskListNavigation',
    'DataExportTaskListNavigationFirstPage',
    'DataExportTaskListPaging',
    'DataExportTaskSpecific',
    'DataExportTaskSpecificContactsItem',
    'DataExportTaskStatus',
    'DeleteMessageByFilterType',
    'DeleteUser2Response',
    'DeleteUser2Response',
    'DeleteUser2Response',
    'DeleteUser2Response',
    'DeleteUser2Response',
    'DeleteUser2ResponseSchemasItem',
    'DeleteUser2ResponseSchemasItem',
    'DeleteUser2ResponseSchemasItem',
    'DeleteUser2ResponseSchemasItem',
    'DeleteUser2ResponseSchemasItem',
    'DeleteUser2ResponseScimType',
    'DeleteUser2ResponseScimType',
    'DeleteUser2ResponseScimType',
    'DeleteUser2ResponseScimType',
    'DeleteUser2ResponseScimType',
    'DeleteUserCallLogDirectionItem',
    'DeleteUserCallLogTypeItem',
    'DepartmentBulkAssignResource',
    'DepartmentBulkAssignResourceItemsItem',
    'DepartmentMemberList',
    'DictionaryGreetingList',
    'DictionaryGreetingListRecordsItem',
    'DictionaryGreetingListRecordsItemCategory',
    'DictionaryGreetingListRecordsItemType',
    'DictionaryGreetingListRecordsItemUsageType',
    'DirectoryResource',
    'DirectoryResourcePaging',
    'DirectoryResourceRecordsItem',
    'DirectoryResourceRecordsItemAccount',
    'DirectoryResourceRecordsItemAccountMainNumber',
    'DirectoryResourceRecordsItemAccountMainNumberUsageType',
    'DirectoryResourceRecordsItemProfileImage',
    'DirectoryResourceRecordsItemSite',
    'EditGroupRequest',
    'EditPagingGroupRequest',
    'EmergencyLocationInfoRequest',
    'EmergencyLocationInfoRequestAddress',
    'EmergencyLocationInfoRequestAddressStatus',
    'EmergencyLocationInfoRequestOwnersItem',
    'EmergencyLocationInfoRequestSite',
    'EmergencyLocationInfoRequestUsageStatus',
    'EmergencyLocationInfoRequestVisibility',
    'EmergencyLocationList',
    'EmergencyLocationListRecordsItem',
    'EmergencyLocationListRecordsItemAddressStatus',
    'EmergencyLocationListRecordsItemSyncStatus',
    'EmergencyLocationListRecordsItemUsageStatus',
    'EmergencyLocationListRecordsItemVisibility',
    'ErrorResponse',
    'ErrorResponseErrorsItem',
    'ErrorResponseErrorsItemErrorCode',
    'ExtensionCallQueuePresenceList',
    'ExtensionCallQueuePresenceListRecordsItem',
    'ExtensionCallQueuePresenceListRecordsItemCallQueue',
    'ExtensionCallQueueUpdatePresenceList',
    'ExtensionCallQueueUpdatePresenceListRecordsItem',
    'ExtensionCallQueueUpdatePresenceListRecordsItemCallQueue',
    'ExtensionCallerIdInfo',
    'ExtensionCallerIdInfoByDeviceItem',
    'ExtensionCallerIdInfoByDeviceItemCallerId',
    'ExtensionCallerIdInfoByDeviceItemCallerIdPhoneInfo',
    'ExtensionCallerIdInfoByDeviceItemDevice',
    'ExtensionCallerIdInfoByFeatureItem',
    'ExtensionCallerIdInfoByFeatureItemCallerId',
    'ExtensionCallerIdInfoByFeatureItemFeature',
    'ExtensionCreationRequest',
    'ExtensionCreationRequestContact',
    'ExtensionCreationRequestContactBusinessAddress',
    'ExtensionCreationRequestContactPronouncedName',
    'ExtensionCreationRequestContactPronouncedNamePrompt',
    'ExtensionCreationRequestContactPronouncedNamePromptContentType',
    'ExtensionCreationRequestContactPronouncedNameType',
    'ExtensionCreationRequestCustomFieldsItem',
    'ExtensionCreationRequestReferencesItem',
    'ExtensionCreationRequestReferencesItemType',
    'ExtensionCreationRequestRegionalSettings',
    'ExtensionCreationRequestRegionalSettingsFormattingLocale',
    'ExtensionCreationRequestRegionalSettingsGreetingLanguage',
    'ExtensionCreationRequestRegionalSettingsLanguage',
    'ExtensionCreationRequestRegionalSettingsTimeFormat',
    'ExtensionCreationRequestRegionalSettingsTimezone',
    'ExtensionCreationRequestSetupWizardState',
    'ExtensionCreationRequestSite',
    'ExtensionCreationRequestSiteOperator',
    'ExtensionCreationRequestStatus',
    'ExtensionCreationRequestStatusInfo',
    'ExtensionCreationRequestStatusInfoReason',
    'ExtensionCreationRequestType',
    'ExtensionCreationResponse',
    'ExtensionCreationResponseContact',
    'ExtensionCreationResponsePermissions',
    'ExtensionCreationResponsePermissionsAdmin',
    'ExtensionCreationResponseProfileImage',
    'ExtensionCreationResponseProfileImageScalesItem',
    'ExtensionCreationResponseServiceFeaturesItem',
    'ExtensionCreationResponseServiceFeaturesItemFeatureName',
    'ExtensionCreationResponseSetupWizardState',
    'ExtensionCreationResponseStatus',
    'ExtensionCreationResponseType',
    'ExtensionUpdateRequest',
    'ExtensionUpdateRequestCallQueueInfo',
    'ExtensionUpdateRequestContact',
    'ExtensionUpdateRequestRegionalSettings',
    'ExtensionUpdateRequestRegionalSettingsFormattingLocale',
    'ExtensionUpdateRequestRegionalSettingsGreetingLanguage',
    'ExtensionUpdateRequestRegionalSettingsHomeCountry',
    'ExtensionUpdateRequestRegionalSettingsLanguage',
    'ExtensionUpdateRequestRegionalSettingsTimeFormat',
    'ExtensionUpdateRequestRegionalSettingsTimezone',
    'ExtensionUpdateRequestSetupWizardState',
    'ExtensionUpdateRequestStatus',
    'ExtensionUpdateRequestTransitionItem',
    'ExtensionUpdateRequestType',
    'FavoriteCollection',
    'FavoriteCollectionRecordsItem',
    'FavoriteContactList',
    'FaxResponse',
    'FaxResponseAttachmentsItem',
    'FaxResponseAttachmentsItemType',
    'FaxResponseAvailability',
    'FaxResponseDirection',
    'FaxResponseFaxResolution',
    'FaxResponseFrom',
    'FaxResponseMessageStatus',
    'FaxResponsePriority',
    'FaxResponseReadStatus',
    'FaxResponseToItem',
    'FaxResponseToItemFaxErrorCode',
    'FaxResponseToItemMessageStatus',
    'FeatureList',
    'FeatureListRecordsItem',
    'FeatureListRecordsItemParamsItem',
    'FeatureListRecordsItemReason',
    'FeatureListRecordsItemReasonCode',
    'FederationResource',
    'FederationResourceAccountsItem',
    'ForwardCallPartyRequest',
    'ForwardCallPartyResponse',
    'ForwardCallPartyResponseConferenceRole',
    'ForwardCallPartyResponseDirection',
    'ForwardCallPartyResponseFrom',
    'ForwardCallPartyResponseOwner',
    'ForwardCallPartyResponsePark',
    'ForwardCallPartyResponseRecordingsItem',
    'ForwardCallPartyResponseRingMeRole',
    'ForwardCallPartyResponseRingOutRole',
    'ForwardCallPartyResponseStatus',
    'ForwardCallPartyResponseStatusCode',
    'ForwardCallPartyResponseStatusPeerId',
    'ForwardCallPartyResponseStatusReason',
    'ForwardCallPartyResponseTo',
    'ForwardTarget',
    'GetAccountInfoResponse',
    'GetAccountInfoResponseRegionalSettings',
    'GetAccountInfoResponseRegionalSettingsCurrency',
    'GetAccountInfoResponseRegionalSettingsTimeFormat',
    'GetAccountInfoResponseServiceInfo',
    'GetAccountInfoResponseSetupWizardState',
    'GetAccountInfoResponseSignupInfo',
    'GetAccountInfoResponseSignupInfoSignupStateItem',
    'GetAccountInfoResponseSignupInfoVerificationReason',
    'GetAccountInfoResponseStatus',
    'GetAccountInfoResponseStatusInfo',
    'GetAccountInfoResponseStatusInfoReason',
    'GetAccountLockedSettingResponse',
    'GetAccountLockedSettingResponseRecording',
    'GetAccountLockedSettingResponseRecordingAutoRecording',
    'GetAccountLockedSettingResponseScheduleMeeting',
    'GetAccountLockedSettingResponseScheduleMeetingAudioOptionsItem',
    'GetAccountLockedSettingResponseScheduleMeetingRequirePasswordForPmiMeetings',
    'GetCallRecordingResponse',
    'GetConferencingInfoResponse',
    'GetConferencingInfoResponsePhoneNumbersItem',
    'GetConferencingInfoResponsePhoneNumbersItemCountry',
    'GetCountryListResponse',
    'GetCountryListResponseRecordsItem',
    'GetDeviceInfoResponse',
    'GetDeviceInfoResponseBillingStatement',
    'GetDeviceInfoResponseBillingStatementChargesItem',
    'GetDeviceInfoResponseBillingStatementFeesItem',
    'GetDeviceInfoResponseEmergency',
    'GetDeviceInfoResponseEmergencyAddress',
    'GetDeviceInfoResponseEmergencyAddressEditableStatus',
    'GetDeviceInfoResponseEmergencyAddressStatus',
    'GetDeviceInfoResponseEmergencyLocation',
    'GetDeviceInfoResponseEmergencyServiceAddress',
    'GetDeviceInfoResponseEmergencyServiceAddressSyncStatus',
    'GetDeviceInfoResponseEmergencySyncStatus',
    'GetDeviceInfoResponseExtension',
    'GetDeviceInfoResponseLinePooling',
    'GetDeviceInfoResponseModel',
    'GetDeviceInfoResponseModelAddonsItem',
    'GetDeviceInfoResponseModelFeaturesItem',
    'GetDeviceInfoResponsePhoneLinesItem',
    'GetDeviceInfoResponsePhoneLinesItemEmergencyAddress',
    'GetDeviceInfoResponsePhoneLinesItemLineType',
    'GetDeviceInfoResponsePhoneLinesItemPhoneInfo',
    'GetDeviceInfoResponsePhoneLinesItemPhoneInfoCountry',
    'GetDeviceInfoResponsePhoneLinesItemPhoneInfoExtension',
    'GetDeviceInfoResponsePhoneLinesItemPhoneInfoPaymentType',
    'GetDeviceInfoResponsePhoneLinesItemPhoneInfoType',
    'GetDeviceInfoResponsePhoneLinesItemPhoneInfoUsageType',
    'GetDeviceInfoResponseShipping',
    'GetDeviceInfoResponseShippingAddress',
    'GetDeviceInfoResponseShippingMethod',
    'GetDeviceInfoResponseShippingMethodId',
    'GetDeviceInfoResponseShippingMethodName',
    'GetDeviceInfoResponseShippingStatus',
    'GetDeviceInfoResponseStatus',
    'GetDeviceInfoResponseType',
    'GetExtensionDevicesResponse',
    'GetExtensionDevicesResponseNavigation',
    'GetExtensionDevicesResponseNavigationFirstPage',
    'GetExtensionDevicesResponsePaging',
    'GetExtensionDevicesResponseRecordsItem',
    'GetExtensionDevicesResponseRecordsItemLinePooling',
    'GetExtensionDevicesResponseRecordsItemStatus',
    'GetExtensionDevicesResponseRecordsItemType',
    'GetExtensionForwardingNumberListResponse',
    'GetExtensionForwardingNumberListResponseNavigation',
    'GetExtensionForwardingNumberListResponseNavigationFirstPage',
    'GetExtensionForwardingNumberListResponsePaging',
    'GetExtensionForwardingNumberListResponseRecordsItem',
    'GetExtensionForwardingNumberListResponseRecordsItemDevice',
    'GetExtensionForwardingNumberListResponseRecordsItemFeaturesItem',
    'GetExtensionForwardingNumberListResponseRecordsItemLabel',
    'GetExtensionForwardingNumberListResponseRecordsItemType',
    'GetExtensionGrantListResponse',
    'GetExtensionGrantListResponseRecordsItem',
    'GetExtensionGrantListResponseRecordsItemExtension',
    'GetExtensionGrantListResponseRecordsItemExtensionType',
    'GetExtensionListResponse',
    'GetExtensionListResponseRecordsItem',
    'GetExtensionListResponseRecordsItemAccount',
    'GetExtensionListResponseRecordsItemCallQueueInfo',
    'GetExtensionListResponseRecordsItemDepartmentsItem',
    'GetExtensionListResponseRecordsItemRolesItem',
    'GetExtensionListResponseRecordsItemSetupWizardState',
    'GetExtensionListResponseRecordsItemStatus',
    'GetExtensionListResponseRecordsItemType',
    'GetExtensionPhoneNumbersResponse',
    'GetExtensionPhoneNumbersResponseRecordsItem',
    'GetExtensionPhoneNumbersResponseRecordsItemContactCenterProvider',
    'GetExtensionPhoneNumbersResponseRecordsItemCountry',
    'GetExtensionPhoneNumbersResponseRecordsItemExtension',
    'GetExtensionPhoneNumbersResponseRecordsItemExtensionType',
    'GetExtensionPhoneNumbersResponseRecordsItemFeaturesItem',
    'GetExtensionPhoneNumbersResponseRecordsItemPaymentType',
    'GetExtensionPhoneNumbersResponseRecordsItemType',
    'GetExtensionPhoneNumbersResponseRecordsItemUsageType',
    'GetGlipNoteInfo',
    'GetGlipNoteInfoStatus',
    'GetGlipNoteInfoType',
    'GetLocationListResponse',
    'GetLocationListResponseRecordsItem',
    'GetLocationListResponseRecordsItemState',
    'GetMessageInfoResponse',
    'GetMessageInfoResponseAvailability',
    'GetMessageInfoResponseDirection',
    'GetMessageInfoResponseFaxResolution',
    'GetMessageInfoResponseFrom',
    'GetMessageInfoResponseMessageStatus',
    'GetMessageInfoResponsePriority',
    'GetMessageInfoResponseReadStatus',
    'GetMessageInfoResponseToItem',
    'GetMessageInfoResponseToItemFaxErrorCode',
    'GetMessageInfoResponseToItemMessageStatus',
    'GetMessageInfoResponseType',
    'GetMessageInfoResponseVmTranscriptionStatus',
    'GetMessageList',
    'GetMessageMultiResponseItem',
    'GetMessageMultiResponseItemBody',
    'GetMessageMultiResponseItemBodyAvailability',
    'GetMessageMultiResponseItemBodyDirection',
    'GetMessageMultiResponseItemBodyFaxResolution',
    'GetMessageMultiResponseItemBodyFrom',
    'GetMessageMultiResponseItemBodyMessageStatus',
    'GetMessageMultiResponseItemBodyPriority',
    'GetMessageMultiResponseItemBodyReadStatus',
    'GetMessageMultiResponseItemBodyToItem',
    'GetMessageMultiResponseItemBodyType',
    'GetMessageMultiResponseItemBodyVmTranscriptionStatus',
    'GetMessageSyncResponse',
    'GetMessageSyncResponseSyncInfo',
    'GetMessageSyncResponseSyncInfoSyncType',
    'GetPresenceInfo',
    'GetPresenceInfoDndStatus',
    'GetPresenceInfoExtension',
    'GetPresenceInfoMeetingStatus',
    'GetPresenceInfoPresenceStatus',
    'GetPresenceInfoTelephonyStatus',
    'GetPresenceInfoUserStatus',
    'GetRingOutStatusResponse',
    'GetRingOutStatusResponseIntId',
    'GetRingOutStatusResponseStatus',
    'GetRingOutStatusResponseStatusCallStatus',
    'GetRingOutStatusResponseStatusCalleeStatus',
    'GetRingOutStatusResponseStatusCallerStatus',
    'GetServiceInfoResponse',
    'GetServiceInfoResponseBillingPlan',
    'GetServiceInfoResponseBillingPlanDurationUnit',
    'GetServiceInfoResponseBillingPlanType',
    'GetServiceInfoResponseBrand',
    'GetServiceInfoResponseContractedCountry',
    'GetServiceInfoResponseLimits',
    'GetServiceInfoResponsePackage',
    'GetServiceInfoResponseServiceFeaturesItem',
    'GetServiceInfoResponseServiceFeaturesItemFeatureName',
    'GetServiceInfoResponseServicePlan',
    'GetServiceInfoResponseServicePlanFreemiumProductType',
    'GetServiceInfoResponseTargetServicePlan',
    'GetServiceInfoResponseTargetServicePlanFreemiumProductType',
    'GetStateListResponse',
    'GetStateListResponseRecordsItem',
    'GetStateListResponseRecordsItemCountry',
    'GetTimezoneListResponse',
    'GetTimezoneListResponseNavigation',
    'GetTimezoneListResponseNavigationFirstPage',
    'GetTimezoneListResponsePaging',
    'GetTimezoneListResponseRecordsItem',
    'GetUserBusinessHoursResponse',
    'GetUserBusinessHoursResponseSchedule',
    'GetUserSettingResponse',
    'GetUserSettingResponseRecording',
    'GetUserSettingResponseRecordingAutoRecording',
    'GetUserSettingResponseScheduleMeeting',
    'GetUserSettingResponseScheduleMeetingAudioOptionsItem',
    'GetUserSettingResponseScheduleMeetingRequirePasswordForPmiMeetings',
    'GetVersionResponse',
    'GetVersionsResponse',
    'GetVersionsResponseApiVersionsItem',
    'GlipChatsList',
    'GlipChatsListWithoutNavigation',
    'GlipChatsListWithoutNavigationRecordsItem',
    'GlipChatsListWithoutNavigationRecordsItemStatus',
    'GlipChatsListWithoutNavigationRecordsItemType',
    'GlipCompleteTask',
    'GlipCompleteTaskStatus',
    'GlipConversationInfo',
    'GlipConversationInfoMembersItem',
    'GlipConversationInfoType',
    'GlipConversationsList',
    'GlipCreateGroup',
    'GlipCreateGroupType',
    'GlipCreatePost',
    'GlipCreatePostAttachmentsItem',
    'GlipCreatePostAttachmentsItemRecurrence',
    'GlipCreatePostAttachmentsItemType',
    'GlipCreateTask',
    'GlipCreateTaskColor',
    'GlipCreateTaskCompletenessCondition',
    'GlipEventCreate',
    'GlipEventCreateColor',
    'GlipEventCreateEndingOn',
    'GlipEventCreateRecurrence',
    'GlipEveryoneInfo',
    'GlipEveryoneInfoType',
    'GlipGroupList',
    'GlipNoteCreate',
    'GlipNoteInfo',
    'GlipNoteInfoLastModifiedBy',
    'GlipNoteInfoLockedBy',
    'GlipNoteInfoStatus',
    'GlipNoteInfoType',
    'GlipNotesInfo',
    'GlipPatchPostBody',
    'GlipPatchTeamBody',
    'GlipPersonInfo',
    'GlipPostMembersIdsListBody',
    'GlipPostMembersListBody',
    'GlipPostPostBody',
    'GlipPostPostBodyAttachmentsItem',
    'GlipPostPostBodyAttachmentsItemType',
    'GlipPostTeamBody',
    'GlipPosts',
    'GlipPostsList',
    'GlipPostsRecordsItem',
    'GlipPostsRecordsItemType',
    'GlipPreferencesInfo',
    'GlipPreferencesInfoChats',
    'GlipPreferencesInfoChatsLeftRailMode',
    'GlipTaskInfo',
    'GlipTaskInfoAssigneesItem',
    'GlipTaskInfoAssigneesItemStatus',
    'GlipTaskInfoAttachmentsItem',
    'GlipTaskInfoAttachmentsItemType',
    'GlipTaskInfoColor',
    'GlipTaskInfoCompletenessCondition',
    'GlipTaskInfoCreator',
    'GlipTaskInfoRecurrence',
    'GlipTaskInfoRecurrenceEndingCondition',
    'GlipTaskInfoRecurrenceSchedule',
    'GlipTaskInfoStatus',
    'GlipTaskInfoType',
    'GlipTaskList',
    'GlipTeamInfo',
    'GlipTeamInfoStatus',
    'GlipTeamInfoType',
    'GlipTeamsList',
    'GlipUpdateTask',
    'GlipUpdateTaskAssigneesItem',
    'GlipUpdateTaskColor',
    'GlipUpdateTaskCompletenessCondition',
    'HoldCallPartyResponse',
    'HoldCallPartyResponseConferenceRole',
    'HoldCallPartyResponseDirection',
    'HoldCallPartyResponseFrom',
    'HoldCallPartyResponseOwner',
    'HoldCallPartyResponsePark',
    'HoldCallPartyResponseRecordingsItem',
    'HoldCallPartyResponseRingMeRole',
    'HoldCallPartyResponseRingOutRole',
    'HoldCallPartyResponseStatus',
    'HoldCallPartyResponseStatusCode',
    'HoldCallPartyResponseStatusPeerId',
    'HoldCallPartyResponseStatusReason',
    'HoldCallPartyResponseTo',
    'IVRMenuInfo',
    'IVRMenuInfoActionsItem',
    'IVRMenuInfoActionsItemAction',
    'IVRMenuInfoActionsItemExtension',
    'IVRMenuInfoPrompt',
    'IVRMenuInfoPromptAudio',
    'IVRMenuInfoPromptLanguage',
    'IVRMenuInfoPromptMode',
    'IVRPrompts',
    'IgnoreCallInQueueRequest',
    'IgnoreRequestBody',
    'LanguageList',
    'ListAccountMeetingRecordingsResponse',
    'ListAccountMeetingRecordingsResponseNavigation',
    'ListAccountMeetingRecordingsResponseNavigationFirstPage',
    'ListAccountMeetingRecordingsResponseNavigationLastPage',
    'ListAccountMeetingRecordingsResponseNavigationNextPage',
    'ListAccountMeetingRecordingsResponseNavigationPreviousPage',
    'ListAccountMeetingRecordingsResponsePaging',
    'ListAccountMeetingRecordingsResponseRecordsItem',
    'ListAccountMeetingRecordingsResponseRecordsItemMeeting',
    'ListAccountMeetingRecordingsResponseRecordsItemRecordingItem',
    'ListAccountMeetingRecordingsResponseRecordsItemRecordingItemContentType',
    'ListAccountMeetingRecordingsResponseRecordsItemRecordingItemStatus',
    'ListAccountPhoneNumbersResponse',
    'ListAccountPhoneNumbersResponseNavigation',
    'ListAccountPhoneNumbersResponseNavigationFirstPage',
    'ListAccountPhoneNumbersResponseNavigationLastPage',
    'ListAccountPhoneNumbersResponseNavigationNextPage',
    'ListAccountPhoneNumbersResponseNavigationPreviousPage',
    'ListAccountPhoneNumbersResponsePaging',
    'ListAccountPhoneNumbersResponseRecordsItem',
    'ListAccountPhoneNumbersResponseRecordsItemContactCenterProvider',
    'ListAccountPhoneNumbersResponseRecordsItemCountry',
    'ListAccountPhoneNumbersResponseRecordsItemExtension',
    'ListAccountPhoneNumbersResponseRecordsItemPaymentType',
    'ListAccountPhoneNumbersResponseRecordsItemTemporaryNumber',
    'ListAccountPhoneNumbersResponseRecordsItemType',
    'ListAccountPhoneNumbersResponseRecordsItemUsageType',
    'ListAccountPhoneNumbersStatus',
    'ListAccountPhoneNumbersUsageTypeItem',
    'ListAccountSwitchesResponse',
    'ListAccountSwitchesResponseNavigation',
    'ListAccountSwitchesResponseNavigationFirstPage',
    'ListAccountSwitchesResponseNavigationLastPage',
    'ListAccountSwitchesResponseNavigationNextPage',
    'ListAccountSwitchesResponseNavigationPreviousPage',
    'ListAccountSwitchesResponsePaging',
    'ListAccountSwitchesResponseRecordsItem',
    'ListAccountSwitchesResponseRecordsItemEmergencyAddress',
    'ListAccountSwitchesResponseRecordsItemEmergencyLocation',
    'ListAccountSwitchesResponseRecordsItemSite',
    'ListAnsweringRulesResponse',
    'ListAnsweringRulesResponseNavigation',
    'ListAnsweringRulesResponseNavigationFirstPage',
    'ListAnsweringRulesResponseNavigationLastPage',
    'ListAnsweringRulesResponseNavigationNextPage',
    'ListAnsweringRulesResponseNavigationPreviousPage',
    'ListAnsweringRulesResponsePaging',
    'ListAnsweringRulesResponseRecordsItem',
    'ListAnsweringRulesResponseRecordsItemSharedLines',
    'ListAnsweringRulesResponseRecordsItemType',
    'ListAnsweringRulesView',
    'ListAutomaticLocationUpdatesUsersResponse',
    'ListAutomaticLocationUpdatesUsersResponseNavigation',
    'ListAutomaticLocationUpdatesUsersResponseNavigationFirstPage',
    'ListAutomaticLocationUpdatesUsersResponseNavigationLastPage',
    'ListAutomaticLocationUpdatesUsersResponseNavigationNextPage',
    'ListAutomaticLocationUpdatesUsersResponseNavigationPreviousPage',
    'ListAutomaticLocationUpdatesUsersResponsePaging',
    'ListAutomaticLocationUpdatesUsersResponseRecordsItem',
    'ListAutomaticLocationUpdatesUsersResponseRecordsItemType',
    'ListAutomaticLocationUpdatesUsersType',
    'ListBlockedAllowedNumbersResponse',
    'ListBlockedAllowedNumbersResponseNavigation',
    'ListBlockedAllowedNumbersResponseNavigationFirstPage',
    'ListBlockedAllowedNumbersResponseNavigationLastPage',
    'ListBlockedAllowedNumbersResponseNavigationNextPage',
    'ListBlockedAllowedNumbersResponseNavigationPreviousPage',
    'ListBlockedAllowedNumbersResponsePaging',
    'ListBlockedAllowedNumbersResponseRecordsItem',
    'ListBlockedAllowedNumbersResponseRecordsItemStatus',
    'ListBlockedAllowedNumbersStatus',
    'ListCallMonitoringGroupMembersResponse',
    'ListCallMonitoringGroupMembersResponseNavigation',
    'ListCallMonitoringGroupMembersResponseNavigationFirstPage',
    'ListCallMonitoringGroupMembersResponseNavigationLastPage',
    'ListCallMonitoringGroupMembersResponseNavigationNextPage',
    'ListCallMonitoringGroupMembersResponseNavigationPreviousPage',
    'ListCallMonitoringGroupMembersResponsePaging',
    'ListCallMonitoringGroupMembersResponseRecordsItem',
    'ListCallMonitoringGroupMembersResponseRecordsItemPermissionsItem',
    'ListCallMonitoringGroupsResponse',
    'ListCallMonitoringGroupsResponseNavigation',
    'ListCallMonitoringGroupsResponseNavigationFirstPage',
    'ListCallMonitoringGroupsResponseNavigationLastPage',
    'ListCallMonitoringGroupsResponseNavigationNextPage',
    'ListCallMonitoringGroupsResponseNavigationPreviousPage',
    'ListCallMonitoringGroupsResponsePaging',
    'ListCallMonitoringGroupsResponseRecordsItem',
    'ListCallQueueMembersResponse',
    'ListCallQueueMembersResponseNavigation',
    'ListCallQueueMembersResponseNavigationFirstPage',
    'ListCallQueueMembersResponseNavigationLastPage',
    'ListCallQueueMembersResponseNavigationNextPage',
    'ListCallQueueMembersResponseNavigationPreviousPage',
    'ListCallQueueMembersResponsePaging',
    'ListCallQueueMembersResponseRecordsItem',
    'ListCallQueuesResponse',
    'ListCallQueuesResponseNavigation',
    'ListCallQueuesResponseNavigationFirstPage',
    'ListCallQueuesResponseNavigationLastPage',
    'ListCallQueuesResponseNavigationNextPage',
    'ListCallQueuesResponseNavigationPreviousPage',
    'ListCallQueuesResponsePaging',
    'ListCallQueuesResponseRecordsItem',
    'ListCallRecordingCustomGreetingsResponse',
    'ListCallRecordingCustomGreetingsResponseRecordsItem',
    'ListCallRecordingCustomGreetingsResponseRecordsItemCustom',
    'ListCallRecordingCustomGreetingsResponseRecordsItemLanguage',
    'ListCallRecordingCustomGreetingsResponseRecordsItemType',
    'ListCallRecordingCustomGreetingsType',
    'ListCallRecordingExtensionsResponse',
    'ListCallRecordingExtensionsResponseNavigation',
    'ListCallRecordingExtensionsResponseNavigationFirstPage',
    'ListCallRecordingExtensionsResponseNavigationLastPage',
    'ListCallRecordingExtensionsResponseNavigationNextPage',
    'ListCallRecordingExtensionsResponseNavigationPreviousPage',
    'ListCallRecordingExtensionsResponsePaging',
    'ListCallRecordingExtensionsResponseRecordsItem',
    'ListChatNotesResponse',
    'ListChatNotesResponseNavigation',
    'ListChatNotesResponseRecordsItem',
    'ListChatNotesResponseRecordsItemCreator',
    'ListChatNotesResponseRecordsItemLastModifiedBy',
    'ListChatNotesResponseRecordsItemLockedBy',
    'ListChatNotesResponseRecordsItemStatus',
    'ListChatNotesResponseRecordsItemType',
    'ListChatNotesStatus',
    'ListChatTasksAssigneeStatus',
    'ListChatTasksAssignmentStatus',
    'ListChatTasksResponse',
    'ListChatTasksResponseRecordsItem',
    'ListChatTasksResponseRecordsItemAssigneesItem',
    'ListChatTasksResponseRecordsItemAssigneesItemStatus',
    'ListChatTasksResponseRecordsItemAttachmentsItem',
    'ListChatTasksResponseRecordsItemAttachmentsItemType',
    'ListChatTasksResponseRecordsItemColor',
    'ListChatTasksResponseRecordsItemCompletenessCondition',
    'ListChatTasksResponseRecordsItemCreator',
    'ListChatTasksResponseRecordsItemRecurrence',
    'ListChatTasksResponseRecordsItemRecurrenceEndingCondition',
    'ListChatTasksResponseRecordsItemRecurrenceSchedule',
    'ListChatTasksResponseRecordsItemStatus',
    'ListChatTasksResponseRecordsItemType',
    'ListChatTasksStatusItem',
    'ListCompanyActiveCallsDirectionItem',
    'ListCompanyActiveCallsResponse',
    'ListCompanyActiveCallsResponseNavigation',
    'ListCompanyActiveCallsResponseNavigationFirstPage',
    'ListCompanyActiveCallsResponseNavigationLastPage',
    'ListCompanyActiveCallsResponseNavigationNextPage',
    'ListCompanyActiveCallsResponseNavigationPreviousPage',
    'ListCompanyActiveCallsResponsePaging',
    'ListCompanyActiveCallsResponseRecordsItem',
    'ListCompanyActiveCallsResponseRecordsItemAction',
    'ListCompanyActiveCallsResponseRecordsItemBilling',
    'ListCompanyActiveCallsResponseRecordsItemDelegate',
    'ListCompanyActiveCallsResponseRecordsItemDirection',
    'ListCompanyActiveCallsResponseRecordsItemExtension',
    'ListCompanyActiveCallsResponseRecordsItemFrom',
    'ListCompanyActiveCallsResponseRecordsItemFromDevice',
    'ListCompanyActiveCallsResponseRecordsItemLegsItem',
    'ListCompanyActiveCallsResponseRecordsItemLegsItemAction',
    'ListCompanyActiveCallsResponseRecordsItemLegsItemBilling',
    'ListCompanyActiveCallsResponseRecordsItemLegsItemDelegate',
    'ListCompanyActiveCallsResponseRecordsItemLegsItemDirection',
    'ListCompanyActiveCallsResponseRecordsItemLegsItemExtension',
    'ListCompanyActiveCallsResponseRecordsItemLegsItemFrom',
    'ListCompanyActiveCallsResponseRecordsItemLegsItemFromDevice',
    'ListCompanyActiveCallsResponseRecordsItemLegsItemLegType',
    'ListCompanyActiveCallsResponseRecordsItemLegsItemMessage',
    'ListCompanyActiveCallsResponseRecordsItemLegsItemReason',
    'ListCompanyActiveCallsResponseRecordsItemLegsItemRecording',
    'ListCompanyActiveCallsResponseRecordsItemLegsItemRecordingType',
    'ListCompanyActiveCallsResponseRecordsItemLegsItemResult',
    'ListCompanyActiveCallsResponseRecordsItemLegsItemTo',
    'ListCompanyActiveCallsResponseRecordsItemLegsItemToDevice',
    'ListCompanyActiveCallsResponseRecordsItemLegsItemTransport',
    'ListCompanyActiveCallsResponseRecordsItemLegsItemType',
    'ListCompanyActiveCallsResponseRecordsItemMessage',
    'ListCompanyActiveCallsResponseRecordsItemReason',
    'ListCompanyActiveCallsResponseRecordsItemRecording',
    'ListCompanyActiveCallsResponseRecordsItemRecordingType',
    'ListCompanyActiveCallsResponseRecordsItemResult',
    'ListCompanyActiveCallsResponseRecordsItemTo',
    'ListCompanyActiveCallsResponseRecordsItemToDevice',
    'ListCompanyActiveCallsResponseRecordsItemTransport',
    'ListCompanyActiveCallsResponseRecordsItemType',
    'ListCompanyActiveCallsTransportItem',
    'ListCompanyActiveCallsTypeItem',
    'ListCompanyActiveCallsView',
    'ListCompanyAnsweringRulesResponse',
    'ListCompanyAnsweringRulesResponseNavigation',
    'ListCompanyAnsweringRulesResponseNavigationFirstPage',
    'ListCompanyAnsweringRulesResponseNavigationLastPage',
    'ListCompanyAnsweringRulesResponseNavigationNextPage',
    'ListCompanyAnsweringRulesResponseNavigationPreviousPage',
    'ListCompanyAnsweringRulesResponsePaging',
    'ListCompanyAnsweringRulesResponseRecordsItem',
    'ListCompanyAnsweringRulesResponseRecordsItemCalledNumbersItem',
    'ListCompanyAnsweringRulesResponseRecordsItemExtension',
    'ListCompanyAnsweringRulesResponseRecordsItemType',
    'ListContactsResponse',
    'ListContactsResponseGroups',
    'ListContactsResponseNavigation',
    'ListContactsResponseNavigationFirstPage',
    'ListContactsResponseNavigationLastPage',
    'ListContactsResponseNavigationNextPage',
    'ListContactsResponseNavigationPreviousPage',
    'ListContactsResponsePaging',
    'ListContactsResponseRecordsItem',
    'ListContactsResponseRecordsItemAvailability',
    'ListContactsResponseRecordsItemBusinessAddress',
    'ListContactsResponseRecordsItemHomeAddress',
    'ListContactsResponseRecordsItemOtherAddress',
    'ListContactsSortByItem',
    'ListCountriesResponse',
    'ListCountriesResponseNavigation',
    'ListCountriesResponseNavigationFirstPage',
    'ListCountriesResponseNavigationLastPage',
    'ListCountriesResponseNavigationNextPage',
    'ListCountriesResponseNavigationPreviousPage',
    'ListCountriesResponsePaging',
    'ListCountriesResponseRecordsItem',
    'ListCustomFieldsResponse',
    'ListCustomFieldsResponseRecordsItem',
    'ListCustomFieldsResponseRecordsItemCategory',
    'ListDataExportTasksResponse',
    'ListDataExportTasksResponseNavigation',
    'ListDataExportTasksResponseNavigationFirstPage',
    'ListDataExportTasksResponseNavigationLastPage',
    'ListDataExportTasksResponseNavigationNextPage',
    'ListDataExportTasksResponseNavigationPreviousPage',
    'ListDataExportTasksResponsePaging',
    'ListDataExportTasksResponseTasksItem',
    'ListDataExportTasksResponseTasksItemCreator',
    'ListDataExportTasksResponseTasksItemDatasetsItem',
    'ListDataExportTasksResponseTasksItemSpecific',
    'ListDataExportTasksResponseTasksItemSpecificContactsItem',
    'ListDataExportTasksResponseTasksItemStatus',
    'ListDataExportTasksStatus',
    'ListDepartmentMembersResponse',
    'ListDepartmentMembersResponseNavigation',
    'ListDepartmentMembersResponseNavigationFirstPage',
    'ListDepartmentMembersResponseNavigationLastPage',
    'ListDepartmentMembersResponseNavigationNextPage',
    'ListDepartmentMembersResponseNavigationPreviousPage',
    'ListDepartmentMembersResponsePaging',
    'ListDepartmentMembersResponseRecordsItem',
    'ListDevicesAutomaticLocationUpdates',
    'ListDevicesAutomaticLocationUpdatesRecordsItem',
    'ListDevicesAutomaticLocationUpdatesRecordsItemModel',
    'ListDevicesAutomaticLocationUpdatesRecordsItemModelFeaturesItem',
    'ListDevicesAutomaticLocationUpdatesRecordsItemPhoneLinesItem',
    'ListDevicesAutomaticLocationUpdatesRecordsItemPhoneLinesItemLineType',
    'ListDevicesAutomaticLocationUpdatesRecordsItemPhoneLinesItemPhoneInfo',
    'ListDevicesAutomaticLocationUpdatesRecordsItemType',
    'ListDevicesAutomaticLocationUpdatesResponse',
    'ListDevicesAutomaticLocationUpdatesResponseNavigation',
    'ListDevicesAutomaticLocationUpdatesResponseNavigationFirstPage',
    'ListDevicesAutomaticLocationUpdatesResponseNavigationLastPage',
    'ListDevicesAutomaticLocationUpdatesResponseNavigationNextPage',
    'ListDevicesAutomaticLocationUpdatesResponseNavigationPreviousPage',
    'ListDevicesAutomaticLocationUpdatesResponsePaging',
    'ListDevicesAutomaticLocationUpdatesResponseRecordsItem',
    'ListDevicesAutomaticLocationUpdatesResponseRecordsItemModel',
    'ListDevicesAutomaticLocationUpdatesResponseRecordsItemModelFeaturesItem',
    'ListDevicesAutomaticLocationUpdatesResponseRecordsItemPhoneLinesItem',
    'ListDevicesAutomaticLocationUpdatesResponseRecordsItemPhoneLinesItemLineType',
    'ListDevicesAutomaticLocationUpdatesResponseRecordsItemPhoneLinesItemPhoneInfo',
    'ListDevicesAutomaticLocationUpdatesResponseRecordsItemType',
    'ListDirectoryEntriesResponse',
    'ListDirectoryEntriesResponse',
    'ListDirectoryEntriesResponse',
    'ListDirectoryEntriesResponse',
    'ListDirectoryEntriesResponseErrorsItem',
    'ListDirectoryEntriesResponseErrorsItem',
    'ListDirectoryEntriesResponseErrorsItem',
    'ListDirectoryEntriesResponseErrorsItemErrorCode',
    'ListDirectoryEntriesResponseErrorsItemErrorCode',
    'ListDirectoryEntriesResponseErrorsItemErrorCode',
    'ListDirectoryEntriesResponsePaging',
    'ListDirectoryEntriesResponseRecordsItem',
    'ListDirectoryEntriesResponseRecordsItemAccount',
    'ListDirectoryEntriesResponseRecordsItemAccountMainNumber',
    'ListDirectoryEntriesResponseRecordsItemAccountMainNumberUsageType',
    'ListDirectoryEntriesResponseRecordsItemPhoneNumbersItem',
    'ListDirectoryEntriesResponseRecordsItemPhoneNumbersItemUsageType',
    'ListDirectoryEntriesResponseRecordsItemProfileImage',
    'ListDirectoryEntriesResponseRecordsItemSite',
    'ListDirectoryEntriesType',
    'ListEmergencyLocationsAddressStatus',
    'ListEmergencyLocationsResponse',
    'ListEmergencyLocationsResponseNavigation',
    'ListEmergencyLocationsResponseNavigationFirstPage',
    'ListEmergencyLocationsResponseNavigationLastPage',
    'ListEmergencyLocationsResponseNavigationNextPage',
    'ListEmergencyLocationsResponseNavigationPreviousPage',
    'ListEmergencyLocationsResponsePaging',
    'ListEmergencyLocationsResponseRecordsItem',
    'ListEmergencyLocationsResponseRecordsItemAddress',
    'ListEmergencyLocationsResponseRecordsItemAddressStatus',
    'ListEmergencyLocationsResponseRecordsItemOwnersItem',
    'ListEmergencyLocationsResponseRecordsItemSite',
    'ListEmergencyLocationsResponseRecordsItemSyncStatus',
    'ListEmergencyLocationsResponseRecordsItemUsageStatus',
    'ListEmergencyLocationsResponseRecordsItemVisibility',
    'ListEmergencyLocationsUsageStatus',
    'ListExtensionActiveCallsDirectionItem',
    'ListExtensionActiveCallsResponse',
    'ListExtensionActiveCallsResponseNavigation',
    'ListExtensionActiveCallsResponseNavigationFirstPage',
    'ListExtensionActiveCallsResponseNavigationLastPage',
    'ListExtensionActiveCallsResponseNavigationNextPage',
    'ListExtensionActiveCallsResponseNavigationPreviousPage',
    'ListExtensionActiveCallsResponsePaging',
    'ListExtensionActiveCallsResponseRecordsItem',
    'ListExtensionActiveCallsResponseRecordsItemAction',
    'ListExtensionActiveCallsResponseRecordsItemBilling',
    'ListExtensionActiveCallsResponseRecordsItemDelegate',
    'ListExtensionActiveCallsResponseRecordsItemDirection',
    'ListExtensionActiveCallsResponseRecordsItemExtension',
    'ListExtensionActiveCallsResponseRecordsItemFrom',
    'ListExtensionActiveCallsResponseRecordsItemFromDevice',
    'ListExtensionActiveCallsResponseRecordsItemLegsItem',
    'ListExtensionActiveCallsResponseRecordsItemLegsItemAction',
    'ListExtensionActiveCallsResponseRecordsItemLegsItemBilling',
    'ListExtensionActiveCallsResponseRecordsItemLegsItemDelegate',
    'ListExtensionActiveCallsResponseRecordsItemLegsItemDirection',
    'ListExtensionActiveCallsResponseRecordsItemLegsItemExtension',
    'ListExtensionActiveCallsResponseRecordsItemLegsItemFrom',
    'ListExtensionActiveCallsResponseRecordsItemLegsItemFromDevice',
    'ListExtensionActiveCallsResponseRecordsItemLegsItemLegType',
    'ListExtensionActiveCallsResponseRecordsItemLegsItemMessage',
    'ListExtensionActiveCallsResponseRecordsItemLegsItemReason',
    'ListExtensionActiveCallsResponseRecordsItemLegsItemRecording',
    'ListExtensionActiveCallsResponseRecordsItemLegsItemRecordingType',
    'ListExtensionActiveCallsResponseRecordsItemLegsItemResult',
    'ListExtensionActiveCallsResponseRecordsItemLegsItemTo',
    'ListExtensionActiveCallsResponseRecordsItemLegsItemToDevice',
    'ListExtensionActiveCallsResponseRecordsItemLegsItemTransport',
    'ListExtensionActiveCallsResponseRecordsItemLegsItemType',
    'ListExtensionActiveCallsResponseRecordsItemMessage',
    'ListExtensionActiveCallsResponseRecordsItemReason',
    'ListExtensionActiveCallsResponseRecordsItemRecording',
    'ListExtensionActiveCallsResponseRecordsItemRecordingType',
    'ListExtensionActiveCallsResponseRecordsItemResult',
    'ListExtensionActiveCallsResponseRecordsItemTo',
    'ListExtensionActiveCallsResponseRecordsItemToDevice',
    'ListExtensionActiveCallsResponseRecordsItemTransport',
    'ListExtensionActiveCallsResponseRecordsItemType',
    'ListExtensionActiveCallsTypeItem',
    'ListExtensionActiveCallsView',
    'ListExtensionDevicesFeature',
    'ListExtensionDevicesLinePooling',
    'ListExtensionDevicesResponse',
    'ListExtensionDevicesResponseNavigation',
    'ListExtensionDevicesResponseNavigationFirstPage',
    'ListExtensionDevicesResponseNavigationLastPage',
    'ListExtensionDevicesResponseNavigationNextPage',
    'ListExtensionDevicesResponseNavigationPreviousPage',
    'ListExtensionDevicesResponsePaging',
    'ListExtensionDevicesResponseRecordsItem',
    'ListExtensionDevicesResponseRecordsItemEmergency',
    'ListExtensionDevicesResponseRecordsItemEmergencyAddress',
    'ListExtensionDevicesResponseRecordsItemEmergencyAddressEditableStatus',
    'ListExtensionDevicesResponseRecordsItemEmergencyAddressStatus',
    'ListExtensionDevicesResponseRecordsItemEmergencyLocation',
    'ListExtensionDevicesResponseRecordsItemEmergencyServiceAddress',
    'ListExtensionDevicesResponseRecordsItemEmergencyServiceAddressSyncStatus',
    'ListExtensionDevicesResponseRecordsItemEmergencySyncStatus',
    'ListExtensionDevicesResponseRecordsItemExtension',
    'ListExtensionDevicesResponseRecordsItemLinePooling',
    'ListExtensionDevicesResponseRecordsItemModel',
    'ListExtensionDevicesResponseRecordsItemModelAddonsItem',
    'ListExtensionDevicesResponseRecordsItemModelFeaturesItem',
    'ListExtensionDevicesResponseRecordsItemPhoneLinesItem',
    'ListExtensionDevicesResponseRecordsItemPhoneLinesItemEmergencyAddress',
    'ListExtensionDevicesResponseRecordsItemPhoneLinesItemLineType',
    'ListExtensionDevicesResponseRecordsItemPhoneLinesItemPhoneInfo',
    'ListExtensionDevicesResponseRecordsItemPhoneLinesItemPhoneInfoCountry',
    'ListExtensionDevicesResponseRecordsItemPhoneLinesItemPhoneInfoExtension',
    'ListExtensionDevicesResponseRecordsItemPhoneLinesItemPhoneInfoPaymentType',
    'ListExtensionDevicesResponseRecordsItemPhoneLinesItemPhoneInfoType',
    'ListExtensionDevicesResponseRecordsItemPhoneLinesItemPhoneInfoUsageType',
    'ListExtensionDevicesResponseRecordsItemShipping',
    'ListExtensionDevicesResponseRecordsItemShippingAddress',
    'ListExtensionDevicesResponseRecordsItemShippingMethod',
    'ListExtensionDevicesResponseRecordsItemShippingMethodId',
    'ListExtensionDevicesResponseRecordsItemShippingMethodName',
    'ListExtensionDevicesResponseRecordsItemShippingStatus',
    'ListExtensionDevicesResponseRecordsItemSite',
    'ListExtensionDevicesResponseRecordsItemStatus',
    'ListExtensionDevicesResponseRecordsItemType',
    'ListExtensionGrantsExtensionType',
    'ListExtensionGrantsResponse',
    'ListExtensionGrantsResponseNavigation',
    'ListExtensionGrantsResponseNavigationFirstPage',
    'ListExtensionGrantsResponseNavigationLastPage',
    'ListExtensionGrantsResponseNavigationNextPage',
    'ListExtensionGrantsResponseNavigationPreviousPage',
    'ListExtensionGrantsResponsePaging',
    'ListExtensionGrantsResponseRecordsItem',
    'ListExtensionGrantsResponseRecordsItemExtension',
    'ListExtensionGrantsResponseRecordsItemExtensionType',
    'ListExtensionPhoneNumbersResponse',
    'ListExtensionPhoneNumbersResponseNavigation',
    'ListExtensionPhoneNumbersResponseNavigationFirstPage',
    'ListExtensionPhoneNumbersResponseNavigationLastPage',
    'ListExtensionPhoneNumbersResponseNavigationNextPage',
    'ListExtensionPhoneNumbersResponseNavigationPreviousPage',
    'ListExtensionPhoneNumbersResponsePaging',
    'ListExtensionPhoneNumbersResponseRecordsItem',
    'ListExtensionPhoneNumbersResponseRecordsItemContactCenterProvider',
    'ListExtensionPhoneNumbersResponseRecordsItemCountry',
    'ListExtensionPhoneNumbersResponseRecordsItemExtension',
    'ListExtensionPhoneNumbersResponseRecordsItemExtensionContactCenterProvider',
    'ListExtensionPhoneNumbersResponseRecordsItemExtensionType',
    'ListExtensionPhoneNumbersResponseRecordsItemFeaturesItem',
    'ListExtensionPhoneNumbersResponseRecordsItemPaymentType',
    'ListExtensionPhoneNumbersResponseRecordsItemType',
    'ListExtensionPhoneNumbersResponseRecordsItemUsageType',
    'ListExtensionPhoneNumbersStatus',
    'ListExtensionPhoneNumbersUsageTypeItem',
    'ListExtensionsResponse',
    'ListExtensionsResponseNavigation',
    'ListExtensionsResponseNavigationFirstPage',
    'ListExtensionsResponseNavigationLastPage',
    'ListExtensionsResponseNavigationNextPage',
    'ListExtensionsResponseNavigationPreviousPage',
    'ListExtensionsResponsePaging',
    'ListExtensionsResponseRecordsItem',
    'ListExtensionsResponseRecordsItemAccount',
    'ListExtensionsResponseRecordsItemCallQueueInfo',
    'ListExtensionsResponseRecordsItemContact',
    'ListExtensionsResponseRecordsItemContactBusinessAddress',
    'ListExtensionsResponseRecordsItemContactPronouncedName',
    'ListExtensionsResponseRecordsItemContactPronouncedNamePrompt',
    'ListExtensionsResponseRecordsItemContactPronouncedNamePromptContentType',
    'ListExtensionsResponseRecordsItemContactPronouncedNameType',
    'ListExtensionsResponseRecordsItemCustomFieldsItem',
    'ListExtensionsResponseRecordsItemDepartmentsItem',
    'ListExtensionsResponseRecordsItemPermissions',
    'ListExtensionsResponseRecordsItemPermissionsAdmin',
    'ListExtensionsResponseRecordsItemPermissionsInternationalCalling',
    'ListExtensionsResponseRecordsItemProfileImage',
    'ListExtensionsResponseRecordsItemProfileImageScalesItem',
    'ListExtensionsResponseRecordsItemReferencesItem',
    'ListExtensionsResponseRecordsItemReferencesItemType',
    'ListExtensionsResponseRecordsItemRegionalSettings',
    'ListExtensionsResponseRecordsItemRegionalSettingsFormattingLocale',
    'ListExtensionsResponseRecordsItemRegionalSettingsGreetingLanguage',
    'ListExtensionsResponseRecordsItemRegionalSettingsHomeCountry',
    'ListExtensionsResponseRecordsItemRegionalSettingsLanguage',
    'ListExtensionsResponseRecordsItemRegionalSettingsTimeFormat',
    'ListExtensionsResponseRecordsItemRegionalSettingsTimezone',
    'ListExtensionsResponseRecordsItemRolesItem',
    'ListExtensionsResponseRecordsItemServiceFeaturesItem',
    'ListExtensionsResponseRecordsItemServiceFeaturesItemFeatureName',
    'ListExtensionsResponseRecordsItemSetupWizardState',
    'ListExtensionsResponseRecordsItemSite',
    'ListExtensionsResponseRecordsItemStatus',
    'ListExtensionsResponseRecordsItemStatusInfo',
    'ListExtensionsResponseRecordsItemStatusInfoReason',
    'ListExtensionsResponseRecordsItemType',
    'ListExtensionsStatusItem',
    'ListExtensionsTypeItem',
    'ListFavoriteChatsResponse',
    'ListFavoriteChatsResponseRecordsItem',
    'ListFavoriteChatsResponseRecordsItemMembersItem',
    'ListFavoriteChatsResponseRecordsItemStatus',
    'ListFavoriteChatsResponseRecordsItemType',
    'ListFavoriteContactsResponse',
    'ListFavoriteContactsResponseRecordsItem',
    'ListFaxCoverPagesResponse',
    'ListFaxCoverPagesResponse',
    'ListFaxCoverPagesResponseNavigation',
    'ListFaxCoverPagesResponseNavigation',
    'ListFaxCoverPagesResponseNavigationFirstPage',
    'ListFaxCoverPagesResponseNavigationFirstPage',
    'ListFaxCoverPagesResponseNavigationLastPage',
    'ListFaxCoverPagesResponseNavigationNextPage',
    'ListFaxCoverPagesResponseNavigationPreviousPage',
    'ListFaxCoverPagesResponsePaging',
    'ListFaxCoverPagesResponsePaging',
    'ListFaxCoverPagesResponseRecordsItem',
    'ListFaxCoverPagesResponseRecordsItem',
    'ListForwardingNumbersResponse',
    'ListForwardingNumbersResponseNavigation',
    'ListForwardingNumbersResponseNavigationFirstPage',
    'ListForwardingNumbersResponseNavigationLastPage',
    'ListForwardingNumbersResponseNavigationNextPage',
    'ListForwardingNumbersResponseNavigationPreviousPage',
    'ListForwardingNumbersResponsePaging',
    'ListForwardingNumbersResponseRecordsItem',
    'ListForwardingNumbersResponseRecordsItemDevice',
    'ListForwardingNumbersResponseRecordsItemFeaturesItem',
    'ListForwardingNumbersResponseRecordsItemLabel',
    'ListForwardingNumbersResponseRecordsItemType',
    'ListGlipChatsResponse',
    'ListGlipChatsResponseNavigation',
    'ListGlipChatsResponseRecordsItem',
    'ListGlipChatsResponseRecordsItemMembersItem',
    'ListGlipChatsResponseRecordsItemStatus',
    'ListGlipChatsResponseRecordsItemType',
    'ListGlipChatsTypeItem',
    'ListGlipConversationsResponse',
    'ListGlipConversationsResponseNavigation',
    'ListGlipConversationsResponseRecordsItem',
    'ListGlipConversationsResponseRecordsItemMembersItem',
    'ListGlipConversationsResponseRecordsItemType',
    'ListGlipGroupPostsResponse',
    'ListGlipGroupPostsResponseNavigation',
    'ListGlipGroupPostsResponseRecordsItem',
    'ListGlipGroupPostsResponseRecordsItemAttachmentsItem',
    'ListGlipGroupPostsResponseRecordsItemAttachmentsItemAuthor',
    'ListGlipGroupPostsResponseRecordsItemAttachmentsItemColor',
    'ListGlipGroupPostsResponseRecordsItemAttachmentsItemEndingOn',
    'ListGlipGroupPostsResponseRecordsItemAttachmentsItemFieldsItem',
    'ListGlipGroupPostsResponseRecordsItemAttachmentsItemFieldsItemStyle',
    'ListGlipGroupPostsResponseRecordsItemAttachmentsItemFootnote',
    'ListGlipGroupPostsResponseRecordsItemAttachmentsItemRecurrence',
    'ListGlipGroupPostsResponseRecordsItemAttachmentsItemType',
    'ListGlipGroupPostsResponseRecordsItemMentionsItem',
    'ListGlipGroupPostsResponseRecordsItemMentionsItemType',
    'ListGlipGroupPostsResponseRecordsItemType',
    'ListGlipGroupWebhooksResponse',
    'ListGlipGroupWebhooksResponseRecordsItem',
    'ListGlipGroupWebhooksResponseRecordsItemStatus',
    'ListGlipGroupsResponse',
    'ListGlipGroupsResponseNavigation',
    'ListGlipGroupsResponseRecordsItem',
    'ListGlipGroupsResponseRecordsItemType',
    'ListGlipGroupsType',
    'ListGlipPostsResponse',
    'ListGlipPostsResponseNavigation',
    'ListGlipPostsResponseRecordsItem',
    'ListGlipPostsResponseRecordsItemAttachmentsItem',
    'ListGlipPostsResponseRecordsItemAttachmentsItemAuthor',
    'ListGlipPostsResponseRecordsItemAttachmentsItemColor',
    'ListGlipPostsResponseRecordsItemAttachmentsItemEndingOn',
    'ListGlipPostsResponseRecordsItemAttachmentsItemFieldsItem',
    'ListGlipPostsResponseRecordsItemAttachmentsItemFieldsItemStyle',
    'ListGlipPostsResponseRecordsItemAttachmentsItemFootnote',
    'ListGlipPostsResponseRecordsItemAttachmentsItemRecurrence',
    'ListGlipPostsResponseRecordsItemAttachmentsItemType',
    'ListGlipPostsResponseRecordsItemMentionsItem',
    'ListGlipPostsResponseRecordsItemMentionsItemType',
    'ListGlipPostsResponseRecordsItemType',
    'ListGlipTeamsResponse',
    'ListGlipTeamsResponseNavigation',
    'ListGlipTeamsResponseRecordsItem',
    'ListGlipTeamsResponseRecordsItemStatus',
    'ListGlipTeamsResponseRecordsItemType',
    'ListGlipWebhooksResponse',
    'ListGlipWebhooksResponse',
    'ListGlipWebhooksResponseRecordsItem',
    'ListGlipWebhooksResponseRecordsItem',
    'ListGlipWebhooksResponseRecordsItemStatus',
    'ListGlipWebhooksResponseRecordsItemStatus',
    'ListGroupEventsResponse',
    'ListGroupEventsResponseColor',
    'ListGroupEventsResponseEndingOn',
    'ListGroupEventsResponseRecurrence',
    'ListIVRPromptsResponse',
    'ListIVRPromptsResponseNavigation',
    'ListIVRPromptsResponseNavigationFirstPage',
    'ListIVRPromptsResponseNavigationLastPage',
    'ListIVRPromptsResponseNavigationNextPage',
    'ListIVRPromptsResponseNavigationPreviousPage',
    'ListIVRPromptsResponsePaging',
    'ListIVRPromptsResponseRecordsItem',
    'ListLanguagesResponse',
    'ListLanguagesResponseNavigation',
    'ListLanguagesResponseNavigationFirstPage',
    'ListLanguagesResponseNavigationLastPage',
    'ListLanguagesResponseNavigationNextPage',
    'ListLanguagesResponseNavigationPreviousPage',
    'ListLanguagesResponsePaging',
    'ListLanguagesResponseRecordsItem',
    'ListLocationsOrderBy',
    'ListLocationsResponse',
    'ListLocationsResponseNavigation',
    'ListLocationsResponseNavigationFirstPage',
    'ListLocationsResponseNavigationLastPage',
    'ListLocationsResponseNavigationNextPage',
    'ListLocationsResponseNavigationPreviousPage',
    'ListLocationsResponsePaging',
    'ListLocationsResponseRecordsItem',
    'ListLocationsResponseRecordsItemState',
    'ListMeetingRecordingsResponse',
    'ListMeetingRecordingsResponseNavigation',
    'ListMeetingRecordingsResponseNavigationFirstPage',
    'ListMeetingRecordingsResponsePaging',
    'ListMeetingRecordingsResponseRecordsItem',
    'ListMeetingRecordingsResponseRecordsItemMeeting',
    'ListMeetingRecordingsResponseRecordsItemRecordingItem',
    'ListMeetingRecordingsResponseRecordsItemRecordingItemContentType',
    'ListMeetingRecordingsResponseRecordsItemRecordingItemStatus',
    'ListMeetingsResponse',
    'ListMeetingsResponseNavigation',
    'ListMeetingsResponseNavigationFirstPage',
    'ListMeetingsResponseNavigationLastPage',
    'ListMeetingsResponseNavigationNextPage',
    'ListMeetingsResponseNavigationPreviousPage',
    'ListMeetingsResponsePaging',
    'ListMeetingsResponseRecordsItem',
    'ListMeetingsResponseRecordsItemHost',
    'ListMeetingsResponseRecordsItemLinks',
    'ListMeetingsResponseRecordsItemMeetingType',
    'ListMeetingsResponseRecordsItemOccurrencesItem',
    'ListMeetingsResponseRecordsItemSchedule',
    'ListMeetingsResponseRecordsItemScheduleTimeZone',
    'ListMessagesAvailabilityItem',
    'ListMessagesDirectionItem',
    'ListMessagesMessageTypeItem',
    'ListMessagesReadStatusItem',
    'ListMessagesResponse',
    'ListMessagesResponseNavigation',
    'ListMessagesResponseNavigationFirstPage',
    'ListMessagesResponseNavigationLastPage',
    'ListMessagesResponseNavigationNextPage',
    'ListMessagesResponseNavigationPreviousPage',
    'ListMessagesResponsePaging',
    'ListMessagesResponseRecordsItem',
    'ListMessagesResponseRecordsItemAttachmentsItem',
    'ListMessagesResponseRecordsItemAttachmentsItemType',
    'ListMessagesResponseRecordsItemAvailability',
    'ListMessagesResponseRecordsItemConversation',
    'ListMessagesResponseRecordsItemDirection',
    'ListMessagesResponseRecordsItemFaxResolution',
    'ListMessagesResponseRecordsItemFrom',
    'ListMessagesResponseRecordsItemMessageStatus',
    'ListMessagesResponseRecordsItemPriority',
    'ListMessagesResponseRecordsItemReadStatus',
    'ListMessagesResponseRecordsItemToItem',
    'ListMessagesResponseRecordsItemToItemFaxErrorCode',
    'ListMessagesResponseRecordsItemToItemMessageStatus',
    'ListMessagesResponseRecordsItemType',
    'ListMessagesResponseRecordsItemVmTranscriptionStatus',
    'ListNetworksResponse',
    'ListNetworksResponseNavigation',
    'ListNetworksResponseNavigationFirstPage',
    'ListNetworksResponseNavigationLastPage',
    'ListNetworksResponseNavigationNextPage',
    'ListNetworksResponseNavigationPreviousPage',
    'ListNetworksResponsePaging',
    'ListNetworksResponseRecordsItem',
    'ListNetworksResponseRecordsItemEmergencyLocation',
    'ListNetworksResponseRecordsItemPrivateIpRangesItem',
    'ListNetworksResponseRecordsItemPrivateIpRangesItemEmergencyAddress',
    'ListNetworksResponseRecordsItemPublicIpRangesItem',
    'ListNetworksResponseRecordsItemSite',
    'ListPagingGroupDevicesResponse',
    'ListPagingGroupDevicesResponseNavigation',
    'ListPagingGroupDevicesResponseNavigationFirstPage',
    'ListPagingGroupDevicesResponseNavigationLastPage',
    'ListPagingGroupDevicesResponseNavigationNextPage',
    'ListPagingGroupDevicesResponseNavigationPreviousPage',
    'ListPagingGroupDevicesResponsePaging',
    'ListPagingGroupDevicesResponseRecordsItem',
    'ListPagingGroupUsersResponse',
    'ListPagingGroupUsersResponseNavigation',
    'ListPagingGroupUsersResponseNavigationFirstPage',
    'ListPagingGroupUsersResponseNavigationLastPage',
    'ListPagingGroupUsersResponseNavigationNextPage',
    'ListPagingGroupUsersResponseNavigationPreviousPage',
    'ListPagingGroupUsersResponsePaging',
    'ListPagingGroupUsersResponseRecordsItem',
    'ListRecentChatsResponse',
    'ListRecentChatsResponseRecordsItem',
    'ListRecentChatsResponseRecordsItemMembersItem',
    'ListRecentChatsResponseRecordsItemStatus',
    'ListRecentChatsResponseRecordsItemType',
    'ListRecentChatsTypeItem',
    'ListStandardGreetingsResponse',
    'ListStandardGreetingsResponseNavigation',
    'ListStandardGreetingsResponseNavigationFirstPage',
    'ListStandardGreetingsResponseNavigationLastPage',
    'ListStandardGreetingsResponseNavigationNextPage',
    'ListStandardGreetingsResponseNavigationPreviousPage',
    'ListStandardGreetingsResponsePaging',
    'ListStandardGreetingsResponseRecordsItem',
    'ListStandardGreetingsResponseRecordsItemCategory',
    'ListStandardGreetingsResponseRecordsItemNavigation',
    'ListStandardGreetingsResponseRecordsItemNavigationFirstPage',
    'ListStandardGreetingsResponseRecordsItemNavigationLastPage',
    'ListStandardGreetingsResponseRecordsItemNavigationNextPage',
    'ListStandardGreetingsResponseRecordsItemNavigationPreviousPage',
    'ListStandardGreetingsResponseRecordsItemPaging',
    'ListStandardGreetingsResponseRecordsItemType',
    'ListStandardGreetingsResponseRecordsItemUsageType',
    'ListStandardGreetingsType',
    'ListStandardGreetingsUsageType',
    'ListStatesResponse',
    'ListStatesResponseNavigation',
    'ListStatesResponseNavigationFirstPage',
    'ListStatesResponseNavigationLastPage',
    'ListStatesResponseNavigationNextPage',
    'ListStatesResponseNavigationPreviousPage',
    'ListStatesResponsePaging',
    'ListStatesResponseRecordsItem',
    'ListStatesResponseRecordsItemCountry',
    'ListSubscriptionsResponse',
    'ListSubscriptionsResponseRecordsItem',
    'ListSubscriptionsResponseRecordsItemBlacklistedData',
    'ListSubscriptionsResponseRecordsItemDeliveryMode',
    'ListSubscriptionsResponseRecordsItemDeliveryModeTransportType',
    'ListSubscriptionsResponseRecordsItemDisabledFiltersItem',
    'ListSubscriptionsResponseRecordsItemStatus',
    'ListSubscriptionsResponseRecordsItemTransportType',
    'ListTimezonesResponse',
    'ListTimezonesResponseNavigation',
    'ListTimezonesResponseNavigationFirstPage',
    'ListTimezonesResponseNavigationLastPage',
    'ListTimezonesResponseNavigationNextPage',
    'ListTimezonesResponseNavigationPreviousPage',
    'ListTimezonesResponsePaging',
    'ListTimezonesResponseRecordsItem',
    'ListUserMeetingRecordingsResponse',
    'ListUserMeetingRecordingsResponseNavigation',
    'ListUserMeetingRecordingsResponseNavigationFirstPage',
    'ListUserMeetingRecordingsResponseNavigationLastPage',
    'ListUserMeetingRecordingsResponseNavigationNextPage',
    'ListUserMeetingRecordingsResponseNavigationPreviousPage',
    'ListUserMeetingRecordingsResponsePaging',
    'ListUserMeetingRecordingsResponseRecordsItem',
    'ListUserMeetingRecordingsResponseRecordsItemMeeting',
    'ListUserMeetingRecordingsResponseRecordsItemRecordingItem',
    'ListUserMeetingRecordingsResponseRecordsItemRecordingItemContentType',
    'ListUserMeetingRecordingsResponseRecordsItemRecordingItemStatus',
    'ListUserTemplatesResponse',
    'ListUserTemplatesResponseNavigation',
    'ListUserTemplatesResponseNavigationFirstPage',
    'ListUserTemplatesResponseNavigationLastPage',
    'ListUserTemplatesResponseNavigationNextPage',
    'ListUserTemplatesResponseNavigationPreviousPage',
    'ListUserTemplatesResponsePaging',
    'ListUserTemplatesResponseRecordsItem',
    'ListUserTemplatesResponseRecordsItemType',
    'ListUserTemplatesType',
    'ListWirelessPointsResponse',
    'ListWirelessPointsResponseNavigation',
    'ListWirelessPointsResponseNavigationFirstPage',
    'ListWirelessPointsResponseNavigationLastPage',
    'ListWirelessPointsResponseNavigationNextPage',
    'ListWirelessPointsResponseNavigationPreviousPage',
    'ListWirelessPointsResponsePaging',
    'ListWirelessPointsResponseRecordsItem',
    'ListWirelessPointsResponseRecordsItemEmergencyAddress',
    'ListWirelessPointsResponseRecordsItemEmergencyLocation',
    'ListWirelessPointsResponseRecordsItemSite',
    'MakeCallOutRequest',
    'MakeCallOutRequestFrom',
    'MakeCallOutRequestTo',
    'MakeRingOutRequest',
    'MakeRingOutRequestCountry',
    'MakeRingOutRequestFrom',
    'MakeRingOutRequestTo',
    'MeetingRequestResource',
    'MeetingRequestResourceAutoRecordType',
    'MeetingRequestResourceMeetingType',
    'MeetingRequestResourceRecurrence',
    'MeetingRequestResourceRecurrenceFrequency',
    'MeetingRequestResourceRecurrenceMonthlyByWeek',
    'MeetingRequestResourceRecurrenceWeeklyByDay',
    'MeetingRequestResourceRecurrenceWeeklyByDays',
    'MeetingResponseResource',
    'MeetingResponseResourceHost',
    'MeetingResponseResourceLinks',
    'MeetingResponseResourceMeetingType',
    'MeetingResponseResourceOccurrencesItem',
    'MeetingResponseResourceSchedule',
    'MeetingResponseResourceScheduleTimeZone',
    'MeetingServiceInfoRequest',
    'MeetingServiceInfoRequestExternalUserInfo',
    'MeetingServiceInfoResource',
    'MeetingServiceInfoResourceDialInNumbersItem',
    'MeetingServiceInfoResourceDialInNumbersItemCountry',
    'MeetingUserSettingsResponse',
    'MeetingUserSettingsResponseRecording',
    'MeetingUserSettingsResponseRecordingAutoRecording',
    'MeetingUserSettingsResponseScheduleMeeting',
    'MeetingUserSettingsResponseScheduleMeetingAudioOptionsItem',
    'MeetingUserSettingsResponseScheduleMeetingRequirePasswordForPmiMeetings',
    'MeetingsResource',
    'MeetingsResourceNavigation',
    'MeetingsResourceNavigationNextPage',
    'MeetingsResourcePaging',
    'MessageStoreConfiguration',
    'MessageStoreReport',
    'MessageStoreReportArchive',
    'MessageStoreReportArchiveRecordsItem',
    'MessageStoreReportStatus',
    'ModifyAccountBusinessAddressRequest',
    'ModifyAccountBusinessAddressRequestBusinessAddress',
    'ModifySubscriptionRequest',
    'NetworksList',
    'NetworksListRecordsItem',
    'NetworksListRecordsItemPrivateIpRangesItem',
    'NotificationSettings',
    'NotificationSettingsEmailRecipientsItem',
    'NotificationSettingsEmailRecipientsItemPermission',
    'NotificationSettingsEmailRecipientsItemStatus',
    'NotificationSettingsUpdateRequest',
    'NotificationSettingsUpdateRequestInboundFaxes',
    'NotificationSettingsUpdateRequestInboundTexts',
    'NotificationSettingsUpdateRequestMissedCalls',
    'NotificationSettingsUpdateRequestOutboundFaxes',
    'NotificationSettingsUpdateRequestVoicemails',
    'PagingOnlyGroupDevices',
    'PagingOnlyGroupDevicesRecordsItem',
    'PagingOnlyGroupUsers',
    'PagingOnlyGroupUsersRecordsItem',
    'ParsePhoneNumberRequest',
    'ParsePhoneNumberRequest',
    'ParsePhoneNumberResponse',
    'ParsePhoneNumberResponse',
    'ParsePhoneNumberResponseHomeCountry',
    'ParsePhoneNumberResponseHomeCountry',
    'ParsePhoneNumberResponsePhoneNumbersItem',
    'ParsePhoneNumberResponsePhoneNumbersItem',
    'ParsePhoneNumberResponsePhoneNumbersItemCountry',
    'PartySuperviseRequest',
    'PartySuperviseRequestMode',
    'PartySuperviseResponse',
    'PartySuperviseResponseDirection',
    'PartyUpdateRequest',
    'PartyUpdateRequestParty',
    'PatchGlipEveryoneRequest',
    'PatchGlipEveryoneResponse',
    'PatchGlipEveryoneResponseType',
    'PatchGlipPostRequest',
    'PatchGlipPostResponse',
    'PatchGlipPostResponseAttachmentsItem',
    'PatchGlipPostResponseAttachmentsItemAuthor',
    'PatchGlipPostResponseAttachmentsItemColor',
    'PatchGlipPostResponseAttachmentsItemEndingOn',
    'PatchGlipPostResponseAttachmentsItemFieldsItem',
    'PatchGlipPostResponseAttachmentsItemFieldsItemStyle',
    'PatchGlipPostResponseAttachmentsItemFootnote',
    'PatchGlipPostResponseAttachmentsItemRecurrence',
    'PatchGlipPostResponseAttachmentsItemType',
    'PatchGlipPostResponseMentionsItem',
    'PatchGlipPostResponseMentionsItemType',
    'PatchGlipPostResponseType',
    'PatchGlipTeamRequest',
    'PatchGlipTeamResponse',
    'PatchGlipTeamResponseStatus',
    'PatchGlipTeamResponseType',
    'PatchNoteResponse',
    'PatchNoteResponseCreator',
    'PatchNoteResponseLastModifiedBy',
    'PatchNoteResponseLockedBy',
    'PatchNoteResponseStatus',
    'PatchNoteResponseType',
    'PatchTaskRequest',
    'PatchTaskRequestAssigneesItem',
    'PatchTaskRequestAttachmentsItem',
    'PatchTaskRequestAttachmentsItemType',
    'PatchTaskRequestColor',
    'PatchTaskRequestCompletenessCondition',
    'PatchTaskRequestRecurrence',
    'PatchTaskRequestRecurrenceEndingCondition',
    'PatchTaskRequestRecurrenceSchedule',
    'PatchTaskResponse',
    'PatchTaskResponseRecordsItem',
    'PatchTaskResponseRecordsItemAssigneesItem',
    'PatchTaskResponseRecordsItemAssigneesItemStatus',
    'PatchTaskResponseRecordsItemAttachmentsItem',
    'PatchTaskResponseRecordsItemAttachmentsItemType',
    'PatchTaskResponseRecordsItemColor',
    'PatchTaskResponseRecordsItemCompletenessCondition',
    'PatchTaskResponseRecordsItemCreator',
    'PatchTaskResponseRecordsItemRecurrence',
    'PatchTaskResponseRecordsItemRecurrenceEndingCondition',
    'PatchTaskResponseRecordsItemRecurrenceSchedule',
    'PatchTaskResponseRecordsItemStatus',
    'PatchTaskResponseRecordsItemType',
    'PatchUser2Request',
    'PatchUser2RequestSchemasItem',
    'PatchUser2Request_OperationsItem',
    'PatchUser2Request_OperationsItemOp',
    'PatchUser2Response',
    'PatchUser2Response',
    'PatchUser2Response',
    'PatchUser2Response',
    'PatchUser2Response',
    'PatchUser2Response',
    'PatchUser2Response',
    'PatchUser2Response',
    'PatchUser2ResponseAddressesItem',
    'PatchUser2ResponseAddressesItemType',
    'PatchUser2ResponseEmailsItem',
    'PatchUser2ResponseEmailsItemType',
    'PatchUser2ResponseMeta',
    'PatchUser2ResponseMetaResourceType',
    'PatchUser2ResponseName',
    'PatchUser2ResponsePhoneNumbersItem',
    'PatchUser2ResponsePhoneNumbersItemType',
    'PatchUser2ResponsePhotosItem',
    'PatchUser2ResponsePhotosItemType',
    'PatchUser2ResponseSchemasItem',
    'PatchUser2ResponseSchemasItem',
    'PatchUser2ResponseSchemasItem',
    'PatchUser2ResponseSchemasItem',
    'PatchUser2ResponseSchemasItem',
    'PatchUser2ResponseSchemasItem',
    'PatchUser2ResponseSchemasItem',
    'PatchUser2ResponseSchemasItem',
    'PatchUser2ResponseScimType',
    'PatchUser2ResponseScimType',
    'PatchUser2ResponseScimType',
    'PatchUser2ResponseScimType',
    'PatchUser2ResponseScimType',
    'PatchUser2ResponseScimType',
    'PatchUser2ResponseScimType',
    'PatchUser2ResponseUrnIetfParamsScimSchemasExtensionEnterprise_2_0_User',
    'PauseResumeCallRecordingRequest',
    'PauseResumeCallRecordingResponse',
    'PersonalContactRequest',
    'PickupCallPartyRequest',
    'PickupCallPartyResponse',
    'PickupCallPartyResponseConferenceRole',
    'PickupCallPartyResponseDirection',
    'PickupCallPartyResponseFrom',
    'PickupCallPartyResponseOwner',
    'PickupCallPartyResponsePark',
    'PickupCallPartyResponseRecordingsItem',
    'PickupCallPartyResponseRingMeRole',
    'PickupCallPartyResponseRingOutRole',
    'PickupCallPartyResponseStatus',
    'PickupCallPartyResponseStatusCode',
    'PickupCallPartyResponseStatusPeerId',
    'PickupCallPartyResponseStatusReason',
    'PickupCallPartyResponseTo',
    'PickupTarget',
    'PresenceInfoResource',
    'PresenceInfoResourceDndStatus',
    'PresenceInfoResourceUserStatus',
    'PresenceInfoResponse',
    'PresenceInfoResponseDndStatus',
    'PresenceInfoResponseMeetingStatus',
    'PresenceInfoResponsePresenceStatus',
    'PresenceInfoResponseTelephonyStatus',
    'PresenceInfoResponseUserStatus',
    'PromptInfo',
    'PublicMeetingInvitationResponse',
    'ReadAPIVersionResponse',
    'ReadAPIVersionsResponse',
    'ReadAPIVersionsResponseApiVersionsItem',
    'ReadAccountBusinessAddressResponse',
    'ReadAccountBusinessAddressResponseBusinessAddress',
    'ReadAccountFederationResponse',
    'ReadAccountFederationResponse',
    'ReadAccountFederationResponse',
    'ReadAccountFederationResponse',
    'ReadAccountFederationResponseAccountsItem',
    'ReadAccountFederationResponseAccountsItemMainNumber',
    'ReadAccountFederationResponseAccountsItemMainNumberUsageType',
    'ReadAccountFederationResponseErrorsItem',
    'ReadAccountFederationResponseErrorsItem',
    'ReadAccountFederationResponseErrorsItem',
    'ReadAccountFederationResponseErrorsItemErrorCode',
    'ReadAccountFederationResponseErrorsItemErrorCode',
    'ReadAccountFederationResponseErrorsItemErrorCode',
    'ReadAccountInfoResponse',
    'ReadAccountInfoResponseLimits',
    'ReadAccountInfoResponseOperator',
    'ReadAccountInfoResponseOperatorAccount',
    'ReadAccountInfoResponseOperatorCallQueueInfo',
    'ReadAccountInfoResponseOperatorContact',
    'ReadAccountInfoResponseOperatorContactBusinessAddress',
    'ReadAccountInfoResponseOperatorContactPronouncedName',
    'ReadAccountInfoResponseOperatorContactPronouncedNamePrompt',
    'ReadAccountInfoResponseOperatorContactPronouncedNamePromptContentType',
    'ReadAccountInfoResponseOperatorContactPronouncedNameType',
    'ReadAccountInfoResponseOperatorCustomFieldsItem',
    'ReadAccountInfoResponseOperatorDepartmentsItem',
    'ReadAccountInfoResponseOperatorPermissions',
    'ReadAccountInfoResponseOperatorPermissionsAdmin',
    'ReadAccountInfoResponseOperatorPermissionsInternationalCalling',
    'ReadAccountInfoResponseOperatorProfileImage',
    'ReadAccountInfoResponseOperatorProfileImageScalesItem',
    'ReadAccountInfoResponseOperatorReferencesItem',
    'ReadAccountInfoResponseOperatorReferencesItemType',
    'ReadAccountInfoResponseOperatorRegionalSettings',
    'ReadAccountInfoResponseOperatorRegionalSettingsFormattingLocale',
    'ReadAccountInfoResponseOperatorRegionalSettingsGreetingLanguage',
    'ReadAccountInfoResponseOperatorRegionalSettingsHomeCountry',
    'ReadAccountInfoResponseOperatorRegionalSettingsLanguage',
    'ReadAccountInfoResponseOperatorRegionalSettingsTimeFormat',
    'ReadAccountInfoResponseOperatorRegionalSettingsTimezone',
    'ReadAccountInfoResponseOperatorRolesItem',
    'ReadAccountInfoResponseOperatorServiceFeaturesItem',
    'ReadAccountInfoResponseOperatorServiceFeaturesItemFeatureName',
    'ReadAccountInfoResponseOperatorSetupWizardState',
    'ReadAccountInfoResponseOperatorSite',
    'ReadAccountInfoResponseOperatorStatus',
    'ReadAccountInfoResponseOperatorStatusInfo',
    'ReadAccountInfoResponseOperatorStatusInfoReason',
    'ReadAccountInfoResponseOperatorType',
    'ReadAccountInfoResponseRegionalSettings',
    'ReadAccountInfoResponseRegionalSettingsCurrency',
    'ReadAccountInfoResponseRegionalSettingsFormattingLocale',
    'ReadAccountInfoResponseRegionalSettingsGreetingLanguage',
    'ReadAccountInfoResponseRegionalSettingsHomeCountry',
    'ReadAccountInfoResponseRegionalSettingsLanguage',
    'ReadAccountInfoResponseRegionalSettingsTimeFormat',
    'ReadAccountInfoResponseRegionalSettingsTimezone',
    'ReadAccountInfoResponseServiceInfo',
    'ReadAccountInfoResponseServiceInfoBillingPlan',
    'ReadAccountInfoResponseServiceInfoBillingPlanDurationUnit',
    'ReadAccountInfoResponseServiceInfoBillingPlanType',
    'ReadAccountInfoResponseServiceInfoBrand',
    'ReadAccountInfoResponseServiceInfoBrandHomeCountry',
    'ReadAccountInfoResponseServiceInfoContractedCountry',
    'ReadAccountInfoResponseServiceInfoServicePlan',
    'ReadAccountInfoResponseServiceInfoServicePlanFreemiumProductType',
    'ReadAccountInfoResponseServiceInfoTargetServicePlan',
    'ReadAccountInfoResponseServiceInfoTargetServicePlanFreemiumProductType',
    'ReadAccountInfoResponseSetupWizardState',
    'ReadAccountInfoResponseSignupInfo',
    'ReadAccountInfoResponseSignupInfoSignupStateItem',
    'ReadAccountInfoResponseSignupInfoVerificationReason',
    'ReadAccountInfoResponseStatus',
    'ReadAccountInfoResponseStatusInfo',
    'ReadAccountInfoResponseStatusInfoReason',
    'ReadAccountPhoneNumberResponse',
    'ReadAccountPhoneNumberResponseContactCenterProvider',
    'ReadAccountPhoneNumberResponseCountry',
    'ReadAccountPhoneNumberResponseExtension',
    'ReadAccountPhoneNumberResponsePaymentType',
    'ReadAccountPhoneNumberResponseTemporaryNumber',
    'ReadAccountPhoneNumberResponseType',
    'ReadAccountPhoneNumberResponseUsageType',
    'ReadAccountPresenceResponse',
    'ReadAccountPresenceResponseNavigation',
    'ReadAccountPresenceResponseNavigationFirstPage',
    'ReadAccountPresenceResponseNavigationLastPage',
    'ReadAccountPresenceResponseNavigationNextPage',
    'ReadAccountPresenceResponseNavigationPreviousPage',
    'ReadAccountPresenceResponsePaging',
    'ReadAccountPresenceResponseRecordsItem',
    'ReadAccountPresenceResponseRecordsItemActiveCallsItem',
    'ReadAccountPresenceResponseRecordsItemActiveCallsItemAdditional',
    'ReadAccountPresenceResponseRecordsItemActiveCallsItemAdditionalType',
    'ReadAccountPresenceResponseRecordsItemActiveCallsItemDirection',
    'ReadAccountPresenceResponseRecordsItemActiveCallsItemPrimary',
    'ReadAccountPresenceResponseRecordsItemActiveCallsItemPrimaryType',
    'ReadAccountPresenceResponseRecordsItemActiveCallsItemSipData',
    'ReadAccountPresenceResponseRecordsItemActiveCallsItemTelephonyStatus',
    'ReadAccountPresenceResponseRecordsItemDndStatus',
    'ReadAccountPresenceResponseRecordsItemExtension',
    'ReadAccountPresenceResponseRecordsItemMeetingStatus',
    'ReadAccountPresenceResponseRecordsItemPresenceStatus',
    'ReadAccountPresenceResponseRecordsItemTelephonyStatus',
    'ReadAccountPresenceResponseRecordsItemUserStatus',
    'ReadAccountServiceInfoResponse',
    'ReadAccountServiceInfoResponseBillingPlan',
    'ReadAccountServiceInfoResponseBillingPlanDurationUnit',
    'ReadAccountServiceInfoResponseBillingPlanType',
    'ReadAccountServiceInfoResponseBrand',
    'ReadAccountServiceInfoResponseBrandHomeCountry',
    'ReadAccountServiceInfoResponseContractedCountry',
    'ReadAccountServiceInfoResponseLimits',
    'ReadAccountServiceInfoResponsePackage',
    'ReadAccountServiceInfoResponseServiceFeaturesItem',
    'ReadAccountServiceInfoResponseServiceFeaturesItemFeatureName',
    'ReadAccountServiceInfoResponseServicePlan',
    'ReadAccountServiceInfoResponseServicePlanFreemiumProductType',
    'ReadAccountServiceInfoResponseTargetServicePlan',
    'ReadAccountServiceInfoResponseTargetServicePlanFreemiumProductType',
    'ReadAnsweringRuleResponse',
    'ReadAnsweringRuleResponseCallHandlingAction',
    'ReadAnsweringRuleResponseCalledNumbersItem',
    'ReadAnsweringRuleResponseCallersItem',
    'ReadAnsweringRuleResponseForwarding',
    'ReadAnsweringRuleResponseForwardingRingingMode',
    'ReadAnsweringRuleResponseForwardingRulesItem',
    'ReadAnsweringRuleResponseForwardingRulesItemForwardingNumbersItem',
    'ReadAnsweringRuleResponseForwardingRulesItemForwardingNumbersItemLabel',
    'ReadAnsweringRuleResponseForwardingRulesItemForwardingNumbersItemType',
    'ReadAnsweringRuleResponseGreetingsItem',
    'ReadAnsweringRuleResponseGreetingsItemCustom',
    'ReadAnsweringRuleResponseGreetingsItemPreset',
    'ReadAnsweringRuleResponseGreetingsItemType',
    'ReadAnsweringRuleResponseGreetingsItemUsageType',
    'ReadAnsweringRuleResponseQueue',
    'ReadAnsweringRuleResponseQueueFixedOrderAgentsItem',
    'ReadAnsweringRuleResponseQueueFixedOrderAgentsItemExtension',
    'ReadAnsweringRuleResponseQueueHoldAudioInterruptionMode',
    'ReadAnsweringRuleResponseQueueHoldTimeExpirationAction',
    'ReadAnsweringRuleResponseQueueMaxCallersAction',
    'ReadAnsweringRuleResponseQueueNoAnswerAction',
    'ReadAnsweringRuleResponseQueueTransferItem',
    'ReadAnsweringRuleResponseQueueTransferItemAction',
    'ReadAnsweringRuleResponseQueueTransferItemExtension',
    'ReadAnsweringRuleResponseQueueTransferMode',
    'ReadAnsweringRuleResponseQueueUnconditionalForwardingItem',
    'ReadAnsweringRuleResponseQueueUnconditionalForwardingItemAction',
    'ReadAnsweringRuleResponseSchedule',
    'ReadAnsweringRuleResponseScheduleRangesItem',
    'ReadAnsweringRuleResponseScheduleRef',
    'ReadAnsweringRuleResponseScheduleWeeklyRanges',
    'ReadAnsweringRuleResponseScheduleWeeklyRangesFridayItem',
    'ReadAnsweringRuleResponseScheduleWeeklyRangesMondayItem',
    'ReadAnsweringRuleResponseScheduleWeeklyRangesSaturdayItem',
    'ReadAnsweringRuleResponseScheduleWeeklyRangesSundayItem',
    'ReadAnsweringRuleResponseScheduleWeeklyRangesThursdayItem',
    'ReadAnsweringRuleResponseScheduleWeeklyRangesTuesdayItem',
    'ReadAnsweringRuleResponseScheduleWeeklyRangesWednesdayItem',
    'ReadAnsweringRuleResponseScreening',
    'ReadAnsweringRuleResponseSharedLines',
    'ReadAnsweringRuleResponseTransfer',
    'ReadAnsweringRuleResponseTransferExtension',
    'ReadAnsweringRuleResponseType',
    'ReadAnsweringRuleResponseUnconditionalForwarding',
    'ReadAnsweringRuleResponseUnconditionalForwardingAction',
    'ReadAnsweringRuleResponseVoicemail',
    'ReadAnsweringRuleResponseVoicemailRecipient',
    'ReadAssistantsResponse',
    'ReadAssistantsResponseRecordsItem',
    'ReadAssistedUsersResponse',
    'ReadAssistedUsersResponseRecordsItem',
    'ReadAuthorizationProfileResponse',
    'ReadAuthorizationProfileResponsePermissionsItem',
    'ReadAuthorizationProfileResponsePermissionsItemEffectiveRole',
    'ReadAuthorizationProfileResponsePermissionsItemPermission',
    'ReadAuthorizationProfileResponsePermissionsItemPermissionSiteCompatible',
    'ReadAuthorizationProfileResponsePermissionsItemScopesItem',
    'ReadAutomaticLocationUpdatesTaskResponse',
    'ReadAutomaticLocationUpdatesTaskResponseResult',
    'ReadAutomaticLocationUpdatesTaskResponseResultRecordsItem',
    'ReadAutomaticLocationUpdatesTaskResponseResultRecordsItemErrorsItem',
    'ReadAutomaticLocationUpdatesTaskResponseStatus',
    'ReadAutomaticLocationUpdatesTaskResponseType',
    'ReadBlockedAllowedNumberResponse',
    'ReadBlockedAllowedNumberResponseStatus',
    'ReadCallPartyStatusResponse',
    'ReadCallPartyStatusResponseConferenceRole',
    'ReadCallPartyStatusResponseDirection',
    'ReadCallPartyStatusResponseFrom',
    'ReadCallPartyStatusResponseOwner',
    'ReadCallPartyStatusResponsePark',
    'ReadCallPartyStatusResponseRecordingsItem',
    'ReadCallPartyStatusResponseRingMeRole',
    'ReadCallPartyStatusResponseRingOutRole',
    'ReadCallPartyStatusResponseStatus',
    'ReadCallPartyStatusResponseStatusCode',
    'ReadCallPartyStatusResponseStatusPeerId',
    'ReadCallPartyStatusResponseStatusReason',
    'ReadCallPartyStatusResponseTo',
    'ReadCallQueueInfoResponse',
    'ReadCallQueueInfoResponseServiceLevelSettings',
    'ReadCallQueueInfoResponseStatus',
    'ReadCallQueuePresenceResponse',
    'ReadCallQueuePresenceResponseRecordsItem',
    'ReadCallQueuePresenceResponseRecordsItemMember',
    'ReadCallQueuePresenceResponseRecordsItemMemberSite',
    'ReadCallRecordingResponse',
    'ReadCallRecordingSettingsResponse',
    'ReadCallRecordingSettingsResponseAutomatic',
    'ReadCallRecordingSettingsResponseGreetingsItem',
    'ReadCallRecordingSettingsResponseGreetingsItemMode',
    'ReadCallRecordingSettingsResponseGreetingsItemType',
    'ReadCallRecordingSettingsResponseOnDemand',
    'ReadCallSessionStatusResponse',
    'ReadCallSessionStatusResponseSession',
    'ReadCallSessionStatusResponseSessionOrigin',
    'ReadCallSessionStatusResponseSessionOriginType',
    'ReadCallSessionStatusResponseSessionPartiesItem',
    'ReadCallSessionStatusResponseSessionPartiesItemConferenceRole',
    'ReadCallSessionStatusResponseSessionPartiesItemDirection',
    'ReadCallSessionStatusResponseSessionPartiesItemFrom',
    'ReadCallSessionStatusResponseSessionPartiesItemOwner',
    'ReadCallSessionStatusResponseSessionPartiesItemPark',
    'ReadCallSessionStatusResponseSessionPartiesItemRecordingsItem',
    'ReadCallSessionStatusResponseSessionPartiesItemRingMeRole',
    'ReadCallSessionStatusResponseSessionPartiesItemRingOutRole',
    'ReadCallSessionStatusResponseSessionPartiesItemStatus',
    'ReadCallSessionStatusResponseSessionPartiesItemStatusCode',
    'ReadCallSessionStatusResponseSessionPartiesItemStatusPeerId',
    'ReadCallSessionStatusResponseSessionPartiesItemStatusReason',
    'ReadCallSessionStatusResponseSessionPartiesItemTo',
    'ReadCallerBlockingSettingsResponse',
    'ReadCallerBlockingSettingsResponseGreetingsItem',
    'ReadCallerBlockingSettingsResponseGreetingsItemPreset',
    'ReadCallerBlockingSettingsResponseMode',
    'ReadCallerBlockingSettingsResponseNoCallerId',
    'ReadCallerBlockingSettingsResponsePayPhones',
    'ReadCompanyAnsweringRuleResponse',
    'ReadCompanyAnsweringRuleResponseCallHandlingAction',
    'ReadCompanyAnsweringRuleResponseCalledNumbersItem',
    'ReadCompanyAnsweringRuleResponseCallersItem',
    'ReadCompanyAnsweringRuleResponseExtension',
    'ReadCompanyAnsweringRuleResponseGreetingsItem',
    'ReadCompanyAnsweringRuleResponseGreetingsItemCustom',
    'ReadCompanyAnsweringRuleResponseGreetingsItemPreset',
    'ReadCompanyAnsweringRuleResponseGreetingsItemType',
    'ReadCompanyAnsweringRuleResponseGreetingsItemUsageType',
    'ReadCompanyAnsweringRuleResponseSchedule',
    'ReadCompanyAnsweringRuleResponseScheduleRangesItem',
    'ReadCompanyAnsweringRuleResponseScheduleRef',
    'ReadCompanyAnsweringRuleResponseScheduleWeeklyRanges',
    'ReadCompanyAnsweringRuleResponseScheduleWeeklyRangesFridayItem',
    'ReadCompanyAnsweringRuleResponseScheduleWeeklyRangesMondayItem',
    'ReadCompanyAnsweringRuleResponseScheduleWeeklyRangesSaturdayItem',
    'ReadCompanyAnsweringRuleResponseScheduleWeeklyRangesSundayItem',
    'ReadCompanyAnsweringRuleResponseScheduleWeeklyRangesThursdayItem',
    'ReadCompanyAnsweringRuleResponseScheduleWeeklyRangesTuesdayItem',
    'ReadCompanyAnsweringRuleResponseScheduleWeeklyRangesWednesdayItem',
    'ReadCompanyAnsweringRuleResponseType',
    'ReadCompanyBusinessHoursResponse',
    'ReadCompanyBusinessHoursResponseSchedule',
    'ReadCompanyBusinessHoursResponseScheduleWeeklyRanges',
    'ReadCompanyBusinessHoursResponseScheduleWeeklyRangesFridayItem',
    'ReadCompanyBusinessHoursResponseScheduleWeeklyRangesMondayItem',
    'ReadCompanyBusinessHoursResponseScheduleWeeklyRangesSaturdayItem',
    'ReadCompanyBusinessHoursResponseScheduleWeeklyRangesSundayItem',
    'ReadCompanyBusinessHoursResponseScheduleWeeklyRangesThursdayItem',
    'ReadCompanyBusinessHoursResponseScheduleWeeklyRangesTuesdayItem',
    'ReadCompanyBusinessHoursResponseScheduleWeeklyRangesWednesdayItem',
    'ReadCompanyCallLogDirectionItem',
    'ReadCompanyCallLogRecordingType',
    'ReadCompanyCallLogResponse',
    'ReadCompanyCallLogResponseNavigation',
    'ReadCompanyCallLogResponseNavigationFirstPage',
    'ReadCompanyCallLogResponseNavigationLastPage',
    'ReadCompanyCallLogResponseNavigationNextPage',
    'ReadCompanyCallLogResponseNavigationPreviousPage',
    'ReadCompanyCallLogResponsePaging',
    'ReadCompanyCallLogResponseRecordsItem',
    'ReadCompanyCallLogResponseRecordsItemAction',
    'ReadCompanyCallLogResponseRecordsItemBilling',
    'ReadCompanyCallLogResponseRecordsItemDelegate',
    'ReadCompanyCallLogResponseRecordsItemDirection',
    'ReadCompanyCallLogResponseRecordsItemExtension',
    'ReadCompanyCallLogResponseRecordsItemFrom',
    'ReadCompanyCallLogResponseRecordsItemFromDevice',
    'ReadCompanyCallLogResponseRecordsItemLegsItem',
    'ReadCompanyCallLogResponseRecordsItemLegsItemAction',
    'ReadCompanyCallLogResponseRecordsItemLegsItemBilling',
    'ReadCompanyCallLogResponseRecordsItemLegsItemDelegate',
    'ReadCompanyCallLogResponseRecordsItemLegsItemDirection',
    'ReadCompanyCallLogResponseRecordsItemLegsItemExtension',
    'ReadCompanyCallLogResponseRecordsItemLegsItemFrom',
    'ReadCompanyCallLogResponseRecordsItemLegsItemFromDevice',
    'ReadCompanyCallLogResponseRecordsItemLegsItemLegType',
    'ReadCompanyCallLogResponseRecordsItemLegsItemMessage',
    'ReadCompanyCallLogResponseRecordsItemLegsItemReason',
    'ReadCompanyCallLogResponseRecordsItemLegsItemRecording',
    'ReadCompanyCallLogResponseRecordsItemLegsItemRecordingType',
    'ReadCompanyCallLogResponseRecordsItemLegsItemResult',
    'ReadCompanyCallLogResponseRecordsItemLegsItemTo',
    'ReadCompanyCallLogResponseRecordsItemLegsItemToDevice',
    'ReadCompanyCallLogResponseRecordsItemLegsItemTransport',
    'ReadCompanyCallLogResponseRecordsItemLegsItemType',
    'ReadCompanyCallLogResponseRecordsItemMessage',
    'ReadCompanyCallLogResponseRecordsItemReason',
    'ReadCompanyCallLogResponseRecordsItemRecording',
    'ReadCompanyCallLogResponseRecordsItemRecordingType',
    'ReadCompanyCallLogResponseRecordsItemResult',
    'ReadCompanyCallLogResponseRecordsItemTo',
    'ReadCompanyCallLogResponseRecordsItemToDevice',
    'ReadCompanyCallLogResponseRecordsItemTransport',
    'ReadCompanyCallLogResponseRecordsItemType',
    'ReadCompanyCallLogTypeItem',
    'ReadCompanyCallLogView',
    'ReadCompanyCallRecordResponse',
    'ReadCompanyCallRecordResponseAction',
    'ReadCompanyCallRecordResponseBilling',
    'ReadCompanyCallRecordResponseDelegate',
    'ReadCompanyCallRecordResponseDirection',
    'ReadCompanyCallRecordResponseExtension',
    'ReadCompanyCallRecordResponseFrom',
    'ReadCompanyCallRecordResponseFromDevice',
    'ReadCompanyCallRecordResponseLegsItem',
    'ReadCompanyCallRecordResponseLegsItemAction',
    'ReadCompanyCallRecordResponseLegsItemBilling',
    'ReadCompanyCallRecordResponseLegsItemDelegate',
    'ReadCompanyCallRecordResponseLegsItemDirection',
    'ReadCompanyCallRecordResponseLegsItemExtension',
    'ReadCompanyCallRecordResponseLegsItemFrom',
    'ReadCompanyCallRecordResponseLegsItemFromDevice',
    'ReadCompanyCallRecordResponseLegsItemLegType',
    'ReadCompanyCallRecordResponseLegsItemMessage',
    'ReadCompanyCallRecordResponseLegsItemReason',
    'ReadCompanyCallRecordResponseLegsItemRecording',
    'ReadCompanyCallRecordResponseLegsItemRecordingType',
    'ReadCompanyCallRecordResponseLegsItemResult',
    'ReadCompanyCallRecordResponseLegsItemTo',
    'ReadCompanyCallRecordResponseLegsItemToDevice',
    'ReadCompanyCallRecordResponseLegsItemTransport',
    'ReadCompanyCallRecordResponseLegsItemType',
    'ReadCompanyCallRecordResponseMessage',
    'ReadCompanyCallRecordResponseReason',
    'ReadCompanyCallRecordResponseRecording',
    'ReadCompanyCallRecordResponseRecordingType',
    'ReadCompanyCallRecordResponseResult',
    'ReadCompanyCallRecordResponseTo',
    'ReadCompanyCallRecordResponseToDevice',
    'ReadCompanyCallRecordResponseTransport',
    'ReadCompanyCallRecordResponseType',
    'ReadCompanyCallRecordView',
    'ReadConferencingSettingsResponse',
    'ReadConferencingSettingsResponsePhoneNumbersItem',
    'ReadConferencingSettingsResponsePhoneNumbersItemCountry',
    'ReadContactResponse',
    'ReadContactResponseAvailability',
    'ReadContactResponseBusinessAddress',
    'ReadContactResponseHomeAddress',
    'ReadContactResponseOtherAddress',
    'ReadCountryResponse',
    'ReadCustomGreetingResponse',
    'ReadCustomGreetingResponseAnsweringRule',
    'ReadCustomGreetingResponseContentType',
    'ReadCustomGreetingResponseType',
    'ReadDataExportTaskResponse',
    'ReadDataExportTaskResponseCreator',
    'ReadDataExportTaskResponseDatasetsItem',
    'ReadDataExportTaskResponseSpecific',
    'ReadDataExportTaskResponseSpecificContactsItem',
    'ReadDataExportTaskResponseStatus',
    'ReadDeviceResponse',
    'ReadDeviceResponseBillingStatement',
    'ReadDeviceResponseBillingStatementChargesItem',
    'ReadDeviceResponseBillingStatementFeesItem',
    'ReadDeviceResponseEmergency',
    'ReadDeviceResponseEmergencyAddress',
    'ReadDeviceResponseEmergencyAddressEditableStatus',
    'ReadDeviceResponseEmergencyAddressStatus',
    'ReadDeviceResponseEmergencyLocation',
    'ReadDeviceResponseEmergencyServiceAddress',
    'ReadDeviceResponseEmergencyServiceAddressSyncStatus',
    'ReadDeviceResponseEmergencySyncStatus',
    'ReadDeviceResponseExtension',
    'ReadDeviceResponseLinePooling',
    'ReadDeviceResponseModel',
    'ReadDeviceResponseModelAddonsItem',
    'ReadDeviceResponseModelFeaturesItem',
    'ReadDeviceResponsePhoneLinesItem',
    'ReadDeviceResponsePhoneLinesItemEmergencyAddress',
    'ReadDeviceResponsePhoneLinesItemLineType',
    'ReadDeviceResponsePhoneLinesItemPhoneInfo',
    'ReadDeviceResponsePhoneLinesItemPhoneInfoCountry',
    'ReadDeviceResponsePhoneLinesItemPhoneInfoExtension',
    'ReadDeviceResponsePhoneLinesItemPhoneInfoPaymentType',
    'ReadDeviceResponsePhoneLinesItemPhoneInfoType',
    'ReadDeviceResponsePhoneLinesItemPhoneInfoUsageType',
    'ReadDeviceResponseShipping',
    'ReadDeviceResponseShippingAddress',
    'ReadDeviceResponseShippingMethod',
    'ReadDeviceResponseShippingMethodId',
    'ReadDeviceResponseShippingMethodName',
    'ReadDeviceResponseShippingStatus',
    'ReadDeviceResponseSite',
    'ReadDeviceResponseStatus',
    'ReadDeviceResponseType',
    'ReadDirectoryEntryResponse',
    'ReadDirectoryEntryResponse',
    'ReadDirectoryEntryResponse',
    'ReadDirectoryEntryResponse',
    'ReadDirectoryEntryResponseAccount',
    'ReadDirectoryEntryResponseAccountMainNumber',
    'ReadDirectoryEntryResponseAccountMainNumberUsageType',
    'ReadDirectoryEntryResponseErrorsItem',
    'ReadDirectoryEntryResponseErrorsItem',
    'ReadDirectoryEntryResponseErrorsItem',
    'ReadDirectoryEntryResponseErrorsItemErrorCode',
    'ReadDirectoryEntryResponseErrorsItemErrorCode',
    'ReadDirectoryEntryResponseErrorsItemErrorCode',
    'ReadDirectoryEntryResponsePhoneNumbersItem',
    'ReadDirectoryEntryResponsePhoneNumbersItemUsageType',
    'ReadDirectoryEntryResponseProfileImage',
    'ReadDirectoryEntryResponseSite',
    'ReadEmergencyLocationResponse',
    'ReadEmergencyLocationResponseAddress',
    'ReadEmergencyLocationResponseAddressStatus',
    'ReadEmergencyLocationResponseOwnersItem',
    'ReadEmergencyLocationResponseSite',
    'ReadEmergencyLocationResponseSyncStatus',
    'ReadEmergencyLocationResponseUsageStatus',
    'ReadEmergencyLocationResponseVisibility',
    'ReadEventResponse',
    'ReadEventResponseColor',
    'ReadEventResponseEndingOn',
    'ReadEventResponseRecurrence',
    'ReadExtensionCallQueuePresenceResponse',
    'ReadExtensionCallQueuePresenceResponseRecordsItem',
    'ReadExtensionCallQueuePresenceResponseRecordsItemCallQueue',
    'ReadExtensionCallerIdResponse',
    'ReadExtensionCallerIdResponseByDeviceItem',
    'ReadExtensionCallerIdResponseByDeviceItemCallerId',
    'ReadExtensionCallerIdResponseByDeviceItemCallerIdPhoneInfo',
    'ReadExtensionCallerIdResponseByDeviceItemDevice',
    'ReadExtensionCallerIdResponseByFeatureItem',
    'ReadExtensionCallerIdResponseByFeatureItemCallerId',
    'ReadExtensionCallerIdResponseByFeatureItemCallerIdPhoneInfo',
    'ReadExtensionCallerIdResponseByFeatureItemFeature',
    'ReadExtensionResponse',
    'ReadExtensionResponseAccount',
    'ReadExtensionResponseCallQueueInfo',
    'ReadExtensionResponseContact',
    'ReadExtensionResponseContactBusinessAddress',
    'ReadExtensionResponseContactPronouncedName',
    'ReadExtensionResponseContactPronouncedNamePrompt',
    'ReadExtensionResponseContactPronouncedNamePromptContentType',
    'ReadExtensionResponseContactPronouncedNameType',
    'ReadExtensionResponseCustomFieldsItem',
    'ReadExtensionResponseDepartmentsItem',
    'ReadExtensionResponsePermissions',
    'ReadExtensionResponsePermissionsAdmin',
    'ReadExtensionResponsePermissionsInternationalCalling',
    'ReadExtensionResponseProfileImage',
    'ReadExtensionResponseProfileImageScalesItem',
    'ReadExtensionResponseReferencesItem',
    'ReadExtensionResponseReferencesItemType',
    'ReadExtensionResponseRegionalSettings',
    'ReadExtensionResponseRegionalSettingsFormattingLocale',
    'ReadExtensionResponseRegionalSettingsGreetingLanguage',
    'ReadExtensionResponseRegionalSettingsHomeCountry',
    'ReadExtensionResponseRegionalSettingsLanguage',
    'ReadExtensionResponseRegionalSettingsTimeFormat',
    'ReadExtensionResponseRegionalSettingsTimezone',
    'ReadExtensionResponseRolesItem',
    'ReadExtensionResponseServiceFeaturesItem',
    'ReadExtensionResponseServiceFeaturesItemFeatureName',
    'ReadExtensionResponseSetupWizardState',
    'ReadExtensionResponseSite',
    'ReadExtensionResponseStatus',
    'ReadExtensionResponseStatusInfo',
    'ReadExtensionResponseStatusInfoReason',
    'ReadExtensionResponseType',
    'ReadForwardingNumberResponse',
    'ReadForwardingNumberResponseDevice',
    'ReadForwardingNumberResponseFeaturesItem',
    'ReadForwardingNumberResponseLabel',
    'ReadForwardingNumberResponseType',
    'ReadGlipCardResponse',
    'ReadGlipCardResponse',
    'ReadGlipCardResponseAuthor',
    'ReadGlipCardResponseAuthor',
    'ReadGlipCardResponseColor',
    'ReadGlipCardResponseColor',
    'ReadGlipCardResponseEndingOn',
    'ReadGlipCardResponseEndingOn',
    'ReadGlipCardResponseFieldsItem',
    'ReadGlipCardResponseFieldsItem',
    'ReadGlipCardResponseFieldsItemStyle',
    'ReadGlipCardResponseFieldsItemStyle',
    'ReadGlipCardResponseFootnote',
    'ReadGlipCardResponseFootnote',
    'ReadGlipCardResponseRecurrence',
    'ReadGlipCardResponseRecurrence',
    'ReadGlipCardResponseType',
    'ReadGlipCardResponseType',
    'ReadGlipChatResponse',
    'ReadGlipChatResponseMembersItem',
    'ReadGlipChatResponseStatus',
    'ReadGlipChatResponseType',
    'ReadGlipCompanyResponse',
    'ReadGlipCompanyResponse',
    'ReadGlipConversationResponse',
    'ReadGlipConversationResponseMembersItem',
    'ReadGlipConversationResponseType',
    'ReadGlipEventsResponse',
    'ReadGlipEventsResponse',
    'ReadGlipEventsResponseNavigation',
    'ReadGlipEventsResponseNavigation',
    'ReadGlipEventsResponseRecordsItem',
    'ReadGlipEventsResponseRecordsItem',
    'ReadGlipEventsResponseRecordsItemColor',
    'ReadGlipEventsResponseRecordsItemColor',
    'ReadGlipEventsResponseRecordsItemEndingOn',
    'ReadGlipEventsResponseRecordsItemEndingOn',
    'ReadGlipEventsResponseRecordsItemRecurrence',
    'ReadGlipEventsResponseRecordsItemRecurrence',
    'ReadGlipEveryoneResponse',
    'ReadGlipEveryoneResponseType',
    'ReadGlipGroupResponse',
    'ReadGlipGroupResponse',
    'ReadGlipGroupResponseType',
    'ReadGlipGroupResponseType',
    'ReadGlipPersonResponse',
    'ReadGlipPostResponse',
    'ReadGlipPostResponseAttachmentsItem',
    'ReadGlipPostResponseAttachmentsItemAuthor',
    'ReadGlipPostResponseAttachmentsItemColor',
    'ReadGlipPostResponseAttachmentsItemEndingOn',
    'ReadGlipPostResponseAttachmentsItemFieldsItem',
    'ReadGlipPostResponseAttachmentsItemFieldsItemStyle',
    'ReadGlipPostResponseAttachmentsItemFootnote',
    'ReadGlipPostResponseAttachmentsItemRecurrence',
    'ReadGlipPostResponseAttachmentsItemType',
    'ReadGlipPostResponseMentionsItem',
    'ReadGlipPostResponseMentionsItemType',
    'ReadGlipPostResponseType',
    'ReadGlipPostsResponse',
    'ReadGlipPostsResponseNavigation',
    'ReadGlipPostsResponseRecordsItem',
    'ReadGlipPostsResponseRecordsItemAttachmentsItem',
    'ReadGlipPostsResponseRecordsItemAttachmentsItemAuthor',
    'ReadGlipPostsResponseRecordsItemAttachmentsItemColor',
    'ReadGlipPostsResponseRecordsItemAttachmentsItemEndingOn',
    'ReadGlipPostsResponseRecordsItemAttachmentsItemFieldsItem',
    'ReadGlipPostsResponseRecordsItemAttachmentsItemFieldsItemStyle',
    'ReadGlipPostsResponseRecordsItemAttachmentsItemFootnote',
    'ReadGlipPostsResponseRecordsItemAttachmentsItemRecurrence',
    'ReadGlipPostsResponseRecordsItemAttachmentsItemType',
    'ReadGlipPostsResponseRecordsItemMentionsItem',
    'ReadGlipPostsResponseRecordsItemMentionsItemType',
    'ReadGlipPostsResponseRecordsItemType',
    'ReadGlipPreferencesResponse',
    'ReadGlipPreferencesResponseChats',
    'ReadGlipPreferencesResponseChatsLeftRailMode',
    'ReadGlipTeamResponse',
    'ReadGlipTeamResponseStatus',
    'ReadGlipTeamResponseType',
    'ReadGlipWebhookResponse',
    'ReadGlipWebhookResponseRecordsItem',
    'ReadGlipWebhookResponseRecordsItemStatus',
    'ReadIVRMenuResponse',
    'ReadIVRMenuResponseActionsItem',
    'ReadIVRMenuResponseActionsItemAction',
    'ReadIVRMenuResponseActionsItemExtension',
    'ReadIVRMenuResponsePrompt',
    'ReadIVRMenuResponsePromptAudio',
    'ReadIVRMenuResponsePromptLanguage',
    'ReadIVRMenuResponsePromptMode',
    'ReadIVRPromptResponse',
    'ReadLanguageResponse',
    'ReadMeetingInvitationResponse',
    'ReadMeetingResponse',
    'ReadMeetingResponseHost',
    'ReadMeetingResponseLinks',
    'ReadMeetingResponseMeetingType',
    'ReadMeetingResponseOccurrencesItem',
    'ReadMeetingResponseSchedule',
    'ReadMeetingResponseScheduleTimeZone',
    'ReadMeetingServiceInfoResponse',
    'ReadMeetingServiceInfoResponseDialInNumbersItem',
    'ReadMeetingServiceInfoResponseDialInNumbersItemCountry',
    'ReadMeetingServiceInfoResponseExternalUserInfo',
    'ReadMessageContentContentDisposition',
    'ReadMessageResponse',
    'ReadMessageResponse',
    'ReadMessageResponseAttachmentsItem',
    'ReadMessageResponseAttachmentsItemType',
    'ReadMessageResponseAvailability',
    'ReadMessageResponseBody',
    'ReadMessageResponseBodyAttachmentsItem',
    'ReadMessageResponseBodyAttachmentsItemType',
    'ReadMessageResponseBodyAvailability',
    'ReadMessageResponseBodyConversation',
    'ReadMessageResponseBodyDirection',
    'ReadMessageResponseBodyFaxResolution',
    'ReadMessageResponseBodyFrom',
    'ReadMessageResponseBodyMessageStatus',
    'ReadMessageResponseBodyPriority',
    'ReadMessageResponseBodyReadStatus',
    'ReadMessageResponseBodyToItem',
    'ReadMessageResponseBodyType',
    'ReadMessageResponseBodyVmTranscriptionStatus',
    'ReadMessageResponseConversation',
    'ReadMessageResponseDirection',
    'ReadMessageResponseFaxResolution',
    'ReadMessageResponseFrom',
    'ReadMessageResponseMessageStatus',
    'ReadMessageResponsePriority',
    'ReadMessageResponseReadStatus',
    'ReadMessageResponseToItem',
    'ReadMessageResponseToItemFaxErrorCode',
    'ReadMessageResponseToItemMessageStatus',
    'ReadMessageResponseType',
    'ReadMessageResponseVmTranscriptionStatus',
    'ReadMessageStoreConfigurationResponse',
    'ReadMessageStoreReportArchiveResponse',
    'ReadMessageStoreReportArchiveResponseRecordsItem',
    'ReadMessageStoreReportTaskResponse',
    'ReadMessageStoreReportTaskResponseStatus',
    'ReadNetworkResponse',
    'ReadNetworkResponseEmergencyLocation',
    'ReadNetworkResponsePrivateIpRangesItem',
    'ReadNetworkResponsePrivateIpRangesItemEmergencyAddress',
    'ReadNetworkResponsePublicIpRangesItem',
    'ReadNetworkResponseSite',
    'ReadNotificationSettingsResponse',
    'ReadNotificationSettingsResponseEmailRecipientsItem',
    'ReadNotificationSettingsResponseEmailRecipientsItemPermission',
    'ReadNotificationSettingsResponseEmailRecipientsItemStatus',
    'ReadNotificationSettingsResponseInboundFaxes',
    'ReadNotificationSettingsResponseInboundTexts',
    'ReadNotificationSettingsResponseMissedCalls',
    'ReadNotificationSettingsResponseOutboundFaxes',
    'ReadNotificationSettingsResponseVoicemails',
    'ReadRingOutCallStatusDeprecatedResponse',
    'ReadRingOutCallStatusDeprecatedResponseStatus',
    'ReadRingOutCallStatusDeprecatedResponseStatusCallStatus',
    'ReadRingOutCallStatusDeprecatedResponseStatusCalleeStatus',
    'ReadRingOutCallStatusDeprecatedResponseStatusCallerStatus',
    'ReadRingOutCallStatusResponse',
    'ReadRingOutCallStatusResponseStatus',
    'ReadRingOutCallStatusResponseStatusCallStatus',
    'ReadRingOutCallStatusResponseStatusCalleeStatus',
    'ReadRingOutCallStatusResponseStatusCallerStatus',
    'ReadServiceProviderConfig2Response',
    'ReadServiceProviderConfig2ResponseAuthenticationSchemesItem',
    'ReadServiceProviderConfig2ResponseBulk',
    'ReadServiceProviderConfig2ResponseChangePassword',
    'ReadServiceProviderConfig2ResponseEtag',
    'ReadServiceProviderConfig2ResponseFilter',
    'ReadServiceProviderConfig2ResponsePatch',
    'ReadServiceProviderConfig2ResponseSchemasItem',
    'ReadServiceProviderConfig2ResponseSort',
    'ReadServiceProviderConfig2ResponseXmlDataFormat',
    'ReadServiceProviderConfigResponse',
    'ReadServiceProviderConfigResponseAuthenticationSchemesItem',
    'ReadServiceProviderConfigResponseBulk',
    'ReadServiceProviderConfigResponseChangePassword',
    'ReadServiceProviderConfigResponseEtag',
    'ReadServiceProviderConfigResponseFilter',
    'ReadServiceProviderConfigResponsePatch',
    'ReadServiceProviderConfigResponseSchemasItem',
    'ReadServiceProviderConfigResponseSort',
    'ReadServiceProviderConfigResponseXmlDataFormat',
    'ReadStandardGreetingResponse',
    'ReadStandardGreetingResponseCategory',
    'ReadStandardGreetingResponseNavigation',
    'ReadStandardGreetingResponseNavigationFirstPage',
    'ReadStandardGreetingResponseNavigationLastPage',
    'ReadStandardGreetingResponseNavigationNextPage',
    'ReadStandardGreetingResponseNavigationPreviousPage',
    'ReadStandardGreetingResponsePaging',
    'ReadStandardGreetingResponseType',
    'ReadStandardGreetingResponseUsageType',
    'ReadStateResponse',
    'ReadStateResponseCountry',
    'ReadSubscriptionResponse',
    'ReadSubscriptionResponseBlacklistedData',
    'ReadSubscriptionResponseDeliveryMode',
    'ReadSubscriptionResponseDeliveryModeTransportType',
    'ReadSubscriptionResponseDisabledFiltersItem',
    'ReadSubscriptionResponseStatus',
    'ReadSubscriptionResponseTransportType',
    'ReadSwitchResponse',
    'ReadSwitchResponseEmergencyAddress',
    'ReadSwitchResponseEmergencyLocation',
    'ReadSwitchResponseSite',
    'ReadTaskResponse',
    'ReadTaskResponseAssigneesItem',
    'ReadTaskResponseAssigneesItemStatus',
    'ReadTaskResponseAttachmentsItem',
    'ReadTaskResponseAttachmentsItemType',
    'ReadTaskResponseColor',
    'ReadTaskResponseCompletenessCondition',
    'ReadTaskResponseCreator',
    'ReadTaskResponseRecurrence',
    'ReadTaskResponseRecurrenceEndingCondition',
    'ReadTaskResponseRecurrenceSchedule',
    'ReadTaskResponseStatus',
    'ReadTaskResponseType',
    'ReadTimezoneResponse',
    'ReadUnifiedPresenceResponse',
    'ReadUnifiedPresenceResponse',
    'ReadUnifiedPresenceResponseBody',
    'ReadUnifiedPresenceResponseBodyGlip',
    'ReadUnifiedPresenceResponseBodyGlipAvailability',
    'ReadUnifiedPresenceResponseBodyGlipStatus',
    'ReadUnifiedPresenceResponseBodyGlipVisibility',
    'ReadUnifiedPresenceResponseBodyMeeting',
    'ReadUnifiedPresenceResponseBodyMeetingStatus',
    'ReadUnifiedPresenceResponseBodyStatus',
    'ReadUnifiedPresenceResponseBodyTelephony',
    'ReadUnifiedPresenceResponseBodyTelephonyAvailability',
    'ReadUnifiedPresenceResponseBodyTelephonyStatus',
    'ReadUnifiedPresenceResponseBodyTelephonyVisibility',
    'ReadUnifiedPresenceResponseGlip',
    'ReadUnifiedPresenceResponseGlipAvailability',
    'ReadUnifiedPresenceResponseGlipStatus',
    'ReadUnifiedPresenceResponseGlipVisibility',
    'ReadUnifiedPresenceResponseMeeting',
    'ReadUnifiedPresenceResponseMeetingStatus',
    'ReadUnifiedPresenceResponseStatus',
    'ReadUnifiedPresenceResponseTelephony',
    'ReadUnifiedPresenceResponseTelephonyAvailability',
    'ReadUnifiedPresenceResponseTelephonyStatus',
    'ReadUnifiedPresenceResponseTelephonyVisibility',
    'ReadUser2Response',
    'ReadUser2Response',
    'ReadUser2Response',
    'ReadUser2Response',
    'ReadUser2Response',
    'ReadUser2Response',
    'ReadUser2ResponseAddressesItem',
    'ReadUser2ResponseAddressesItemType',
    'ReadUser2ResponseEmailsItem',
    'ReadUser2ResponseEmailsItemType',
    'ReadUser2ResponseMeta',
    'ReadUser2ResponseMetaResourceType',
    'ReadUser2ResponseName',
    'ReadUser2ResponsePhoneNumbersItem',
    'ReadUser2ResponsePhoneNumbersItemType',
    'ReadUser2ResponsePhotosItem',
    'ReadUser2ResponsePhotosItemType',
    'ReadUser2ResponseSchemasItem',
    'ReadUser2ResponseSchemasItem',
    'ReadUser2ResponseSchemasItem',
    'ReadUser2ResponseSchemasItem',
    'ReadUser2ResponseSchemasItem',
    'ReadUser2ResponseSchemasItem',
    'ReadUser2ResponseScimType',
    'ReadUser2ResponseScimType',
    'ReadUser2ResponseScimType',
    'ReadUser2ResponseScimType',
    'ReadUser2ResponseScimType',
    'ReadUser2ResponseUrnIetfParamsScimSchemasExtensionEnterprise_2_0_User',
    'ReadUserBusinessHoursResponse',
    'ReadUserBusinessHoursResponseSchedule',
    'ReadUserBusinessHoursResponseScheduleWeeklyRanges',
    'ReadUserBusinessHoursResponseScheduleWeeklyRangesFridayItem',
    'ReadUserBusinessHoursResponseScheduleWeeklyRangesMondayItem',
    'ReadUserBusinessHoursResponseScheduleWeeklyRangesSaturdayItem',
    'ReadUserBusinessHoursResponseScheduleWeeklyRangesSundayItem',
    'ReadUserBusinessHoursResponseScheduleWeeklyRangesThursdayItem',
    'ReadUserBusinessHoursResponseScheduleWeeklyRangesTuesdayItem',
    'ReadUserBusinessHoursResponseScheduleWeeklyRangesWednesdayItem',
    'ReadUserCallLogDirectionItem',
    'ReadUserCallLogRecordingType',
    'ReadUserCallLogResponse',
    'ReadUserCallLogResponseNavigation',
    'ReadUserCallLogResponseNavigationFirstPage',
    'ReadUserCallLogResponseNavigationLastPage',
    'ReadUserCallLogResponseNavigationNextPage',
    'ReadUserCallLogResponseNavigationPreviousPage',
    'ReadUserCallLogResponsePaging',
    'ReadUserCallLogResponseRecordsItem',
    'ReadUserCallLogResponseRecordsItemAction',
    'ReadUserCallLogResponseRecordsItemBilling',
    'ReadUserCallLogResponseRecordsItemDelegate',
    'ReadUserCallLogResponseRecordsItemDirection',
    'ReadUserCallLogResponseRecordsItemExtension',
    'ReadUserCallLogResponseRecordsItemFrom',
    'ReadUserCallLogResponseRecordsItemFromDevice',
    'ReadUserCallLogResponseRecordsItemLegsItem',
    'ReadUserCallLogResponseRecordsItemLegsItemAction',
    'ReadUserCallLogResponseRecordsItemLegsItemBilling',
    'ReadUserCallLogResponseRecordsItemLegsItemDelegate',
    'ReadUserCallLogResponseRecordsItemLegsItemDirection',
    'ReadUserCallLogResponseRecordsItemLegsItemExtension',
    'ReadUserCallLogResponseRecordsItemLegsItemFrom',
    'ReadUserCallLogResponseRecordsItemLegsItemFromDevice',
    'ReadUserCallLogResponseRecordsItemLegsItemLegType',
    'ReadUserCallLogResponseRecordsItemLegsItemMessage',
    'ReadUserCallLogResponseRecordsItemLegsItemReason',
    'ReadUserCallLogResponseRecordsItemLegsItemRecording',
    'ReadUserCallLogResponseRecordsItemLegsItemRecordingType',
    'ReadUserCallLogResponseRecordsItemLegsItemResult',
    'ReadUserCallLogResponseRecordsItemLegsItemTo',
    'ReadUserCallLogResponseRecordsItemLegsItemToDevice',
    'ReadUserCallLogResponseRecordsItemLegsItemTransport',
    'ReadUserCallLogResponseRecordsItemLegsItemType',
    'ReadUserCallLogResponseRecordsItemMessage',
    'ReadUserCallLogResponseRecordsItemReason',
    'ReadUserCallLogResponseRecordsItemRecording',
    'ReadUserCallLogResponseRecordsItemRecordingType',
    'ReadUserCallLogResponseRecordsItemResult',
    'ReadUserCallLogResponseRecordsItemTo',
    'ReadUserCallLogResponseRecordsItemToDevice',
    'ReadUserCallLogResponseRecordsItemTransport',
    'ReadUserCallLogResponseRecordsItemType',
    'ReadUserCallLogTransportItem',
    'ReadUserCallLogTypeItem',
    'ReadUserCallLogView',
    'ReadUserCallRecordResponse',
    'ReadUserCallRecordResponseAction',
    'ReadUserCallRecordResponseBilling',
    'ReadUserCallRecordResponseDelegate',
    'ReadUserCallRecordResponseDirection',
    'ReadUserCallRecordResponseExtension',
    'ReadUserCallRecordResponseFrom',
    'ReadUserCallRecordResponseFromDevice',
    'ReadUserCallRecordResponseLegsItem',
    'ReadUserCallRecordResponseLegsItemAction',
    'ReadUserCallRecordResponseLegsItemBilling',
    'ReadUserCallRecordResponseLegsItemDelegate',
    'ReadUserCallRecordResponseLegsItemDirection',
    'ReadUserCallRecordResponseLegsItemExtension',
    'ReadUserCallRecordResponseLegsItemFrom',
    'ReadUserCallRecordResponseLegsItemFromDevice',
    'ReadUserCallRecordResponseLegsItemLegType',
    'ReadUserCallRecordResponseLegsItemMessage',
    'ReadUserCallRecordResponseLegsItemReason',
    'ReadUserCallRecordResponseLegsItemRecording',
    'ReadUserCallRecordResponseLegsItemRecordingType',
    'ReadUserCallRecordResponseLegsItemResult',
    'ReadUserCallRecordResponseLegsItemTo',
    'ReadUserCallRecordResponseLegsItemToDevice',
    'ReadUserCallRecordResponseLegsItemTransport',
    'ReadUserCallRecordResponseLegsItemType',
    'ReadUserCallRecordResponseMessage',
    'ReadUserCallRecordResponseReason',
    'ReadUserCallRecordResponseRecording',
    'ReadUserCallRecordResponseRecordingType',
    'ReadUserCallRecordResponseResult',
    'ReadUserCallRecordResponseTo',
    'ReadUserCallRecordResponseToDevice',
    'ReadUserCallRecordResponseTransport',
    'ReadUserCallRecordResponseType',
    'ReadUserCallRecordView',
    'ReadUserFeaturesResponse',
    'ReadUserFeaturesResponseRecordsItem',
    'ReadUserFeaturesResponseRecordsItemParamsItem',
    'ReadUserFeaturesResponseRecordsItemReason',
    'ReadUserFeaturesResponseRecordsItemReasonCode',
    'ReadUserNoteResponse',
    'ReadUserNoteResponseCreator',
    'ReadUserNoteResponseLastModifiedBy',
    'ReadUserNoteResponseLockedBy',
    'ReadUserNoteResponseStatus',
    'ReadUserNoteResponseType',
    'ReadUserPresenceStatusResponse',
    'ReadUserPresenceStatusResponseActiveCallsItem',
    'ReadUserPresenceStatusResponseActiveCallsItemAdditional',
    'ReadUserPresenceStatusResponseActiveCallsItemAdditionalType',
    'ReadUserPresenceStatusResponseActiveCallsItemDirection',
    'ReadUserPresenceStatusResponseActiveCallsItemPrimary',
    'ReadUserPresenceStatusResponseActiveCallsItemPrimaryType',
    'ReadUserPresenceStatusResponseActiveCallsItemSipData',
    'ReadUserPresenceStatusResponseActiveCallsItemTelephonyStatus',
    'ReadUserPresenceStatusResponseDndStatus',
    'ReadUserPresenceStatusResponseExtension',
    'ReadUserPresenceStatusResponseMeetingStatus',
    'ReadUserPresenceStatusResponsePresenceStatus',
    'ReadUserPresenceStatusResponseTelephonyStatus',
    'ReadUserPresenceStatusResponseUserStatus',
    'ReadUserTemplateResponse',
    'ReadUserTemplateResponseType',
    'ReadUserVideoConfigurationResponse',
    'ReadUserVideoConfigurationResponseProvider',
    'ReadWirelessPointResponse',
    'ReadWirelessPointResponseEmergencyAddress',
    'ReadWirelessPointResponseEmergencyLocation',
    'ReadWirelessPointResponseSite',
    'RecordsCollectionResourceSubscriptionResponse',
    'RecordsCollectionResourceSubscriptionResponseRecordsItem',
    'RecordsCollectionResourceSubscriptionResponseRecordsItemBlacklistedData',
    'RecordsCollectionResourceSubscriptionResponseRecordsItemDeliveryMode',
    'RecordsCollectionResourceSubscriptionResponseRecordsItemDeliveryModeTransportType',
    'RecordsCollectionResourceSubscriptionResponseRecordsItemDisabledFiltersItem',
    'RecordsCollectionResourceSubscriptionResponseRecordsItemStatus',
    'RecordsCollectionResourceSubscriptionResponseRecordsItemTransportType',
    'RemoveGlipTeamMembersRequest',
    'RemoveGlipTeamMembersRequestMembersItem',
    'RenewSubscriptionResponse',
    'RenewSubscriptionResponseBlacklistedData',
    'RenewSubscriptionResponseDeliveryMode',
    'RenewSubscriptionResponseDeliveryModeTransportType',
    'RenewSubscriptionResponseDisabledFiltersItem',
    'RenewSubscriptionResponseStatus',
    'RenewSubscriptionResponseTransportType',
    'ReplaceUser2Request',
    'ReplaceUser2RequestAddressesItem',
    'ReplaceUser2RequestAddressesItemType',
    'ReplaceUser2RequestEmailsItem',
    'ReplaceUser2RequestEmailsItemType',
    'ReplaceUser2RequestName',
    'ReplaceUser2RequestPhoneNumbersItem',
    'ReplaceUser2RequestPhoneNumbersItemType',
    'ReplaceUser2RequestPhotosItem',
    'ReplaceUser2RequestPhotosItemType',
    'ReplaceUser2RequestSchemasItem',
    'ReplaceUser2RequestUrnIetfParamsScimSchemasExtensionEnterprise_2_0_User',
    'ReplaceUser2Response',
    'ReplaceUser2Response',
    'ReplaceUser2Response',
    'ReplaceUser2Response',
    'ReplaceUser2Response',
    'ReplaceUser2Response',
    'ReplaceUser2Response',
    'ReplaceUser2Response',
    'ReplaceUser2ResponseAddressesItem',
    'ReplaceUser2ResponseAddressesItemType',
    'ReplaceUser2ResponseEmailsItem',
    'ReplaceUser2ResponseEmailsItemType',
    'ReplaceUser2ResponseMeta',
    'ReplaceUser2ResponseMetaResourceType',
    'ReplaceUser2ResponseName',
    'ReplaceUser2ResponsePhoneNumbersItem',
    'ReplaceUser2ResponsePhoneNumbersItemType',
    'ReplaceUser2ResponsePhotosItem',
    'ReplaceUser2ResponsePhotosItemType',
    'ReplaceUser2ResponseSchemasItem',
    'ReplaceUser2ResponseSchemasItem',
    'ReplaceUser2ResponseSchemasItem',
    'ReplaceUser2ResponseSchemasItem',
    'ReplaceUser2ResponseSchemasItem',
    'ReplaceUser2ResponseSchemasItem',
    'ReplaceUser2ResponseSchemasItem',
    'ReplaceUser2ResponseSchemasItem',
    'ReplaceUser2ResponseScimType',
    'ReplaceUser2ResponseScimType',
    'ReplaceUser2ResponseScimType',
    'ReplaceUser2ResponseScimType',
    'ReplaceUser2ResponseScimType',
    'ReplaceUser2ResponseScimType',
    'ReplaceUser2ResponseScimType',
    'ReplaceUser2ResponseUrnIetfParamsScimSchemasExtensionEnterprise_2_0_User',
    'ReplyParty',
    'ReplyPartyDirection',
    'ReplyPartyRequest',
    'ReplyPartyRequestReplyWithPattern',
    'ReplyPartyRequestReplyWithPatternPattern',
    'ReplyPartyRequestReplyWithPatternTimeUnit',
    'ReplyPartyResponse',
    'ReplyPartyResponseDirection',
    'ReplyPartyResponseFrom',
    'ReplyPartyResponseOwner',
    'ReplyPartyResponsePark',
    'ReplyPartyResponseStatus',
    'ReplyPartyResponseStatusCode',
    'ReplyPartyResponseStatusPeerId',
    'ReplyPartyResponseStatusReason',
    'ReplyPartyResponseTo',
    'ScimErrorResponse',
    'ScimErrorResponseSchemasItem',
    'ScimErrorResponseScimType',
    'SearchDirectoryEntriesRequest',
    'SearchDirectoryEntriesRequest',
    'SearchDirectoryEntriesRequestExtensionType',
    'SearchDirectoryEntriesRequestExtensionType',
    'SearchDirectoryEntriesRequestOrderByItem',
    'SearchDirectoryEntriesRequestOrderByItem',
    'SearchDirectoryEntriesRequestOrderByItemDirection',
    'SearchDirectoryEntriesRequestOrderByItemDirection',
    'SearchDirectoryEntriesRequestOrderByItemFieldName',
    'SearchDirectoryEntriesRequestOrderByItemFieldName',
    'SearchDirectoryEntriesRequestSearchFieldsItem',
    'SearchDirectoryEntriesRequestSearchFieldsItem',
    'SearchDirectoryEntriesResponse',
    'SearchDirectoryEntriesResponse',
    'SearchDirectoryEntriesResponse',
    'SearchDirectoryEntriesResponse',
    'SearchDirectoryEntriesResponseErrorsItem',
    'SearchDirectoryEntriesResponseErrorsItem',
    'SearchDirectoryEntriesResponseErrorsItem',
    'SearchDirectoryEntriesResponseErrorsItemErrorCode',
    'SearchDirectoryEntriesResponseErrorsItemErrorCode',
    'SearchDirectoryEntriesResponseErrorsItemErrorCode',
    'SearchDirectoryEntriesResponsePaging',
    'SearchDirectoryEntriesResponseRecordsItem',
    'SearchDirectoryEntriesResponseRecordsItemAccount',
    'SearchDirectoryEntriesResponseRecordsItemAccountMainNumber',
    'SearchDirectoryEntriesResponseRecordsItemAccountMainNumberUsageType',
    'SearchDirectoryEntriesResponseRecordsItemPhoneNumbersItem',
    'SearchDirectoryEntriesResponseRecordsItemPhoneNumbersItemUsageType',
    'SearchDirectoryEntriesResponseRecordsItemProfileImage',
    'SearchDirectoryEntriesResponseRecordsItemSite',
    'SearchRequest',
    'SearchRequestSchemasItem',
    'SearchViaGet2Response',
    'SearchViaGet2Response',
    'SearchViaGet2Response',
    'SearchViaGet2Response',
    'SearchViaGet2Response',
    'SearchViaGet2Response',
    'SearchViaGet2ResponseSchemasItem',
    'SearchViaGet2ResponseSchemasItem',
    'SearchViaGet2ResponseSchemasItem',
    'SearchViaGet2ResponseSchemasItem',
    'SearchViaGet2ResponseSchemasItem',
    'SearchViaGet2ResponseSchemasItem',
    'SearchViaGet2ResponseScimType',
    'SearchViaGet2ResponseScimType',
    'SearchViaGet2ResponseScimType',
    'SearchViaGet2ResponseScimType',
    'SearchViaGet2ResponseScimType',
    'SearchViaGet2Response_ResourcesItem',
    'SearchViaGet2Response_ResourcesItemAddressesItem',
    'SearchViaGet2Response_ResourcesItemAddressesItemType',
    'SearchViaGet2Response_ResourcesItemEmailsItem',
    'SearchViaGet2Response_ResourcesItemEmailsItemType',
    'SearchViaGet2Response_ResourcesItemMeta',
    'SearchViaGet2Response_ResourcesItemMetaResourceType',
    'SearchViaGet2Response_ResourcesItemName',
    'SearchViaGet2Response_ResourcesItemPhoneNumbersItem',
    'SearchViaGet2Response_ResourcesItemPhoneNumbersItemType',
    'SearchViaGet2Response_ResourcesItemPhotosItem',
    'SearchViaGet2Response_ResourcesItemPhotosItemType',
    'SearchViaGet2Response_ResourcesItemSchemasItem',
    'SearchViaGet2Response_ResourcesItemUrnIetfParamsScimSchemasExtensionEnterprise_2_0_User',
    'SearchViaGetResponse',
    'SearchViaGetResponse',
    'SearchViaGetResponse',
    'SearchViaGetResponse',
    'SearchViaGetResponse',
    'SearchViaGetResponse',
    'SearchViaGetResponseSchemasItem',
    'SearchViaGetResponseSchemasItem',
    'SearchViaGetResponseSchemasItem',
    'SearchViaGetResponseSchemasItem',
    'SearchViaGetResponseSchemasItem',
    'SearchViaGetResponseSchemasItem',
    'SearchViaGetResponseScimType',
    'SearchViaGetResponseScimType',
    'SearchViaGetResponseScimType',
    'SearchViaGetResponseScimType',
    'SearchViaGetResponseScimType',
    'SearchViaGetResponse_ResourcesItem',
    'SearchViaGetResponse_ResourcesItemAddressesItem',
    'SearchViaGetResponse_ResourcesItemAddressesItemType',
    'SearchViaGetResponse_ResourcesItemEmailsItem',
    'SearchViaGetResponse_ResourcesItemEmailsItemType',
    'SearchViaGetResponse_ResourcesItemMeta',
    'SearchViaGetResponse_ResourcesItemMetaResourceType',
    'SearchViaGetResponse_ResourcesItemName',
    'SearchViaGetResponse_ResourcesItemPhoneNumbersItem',
    'SearchViaGetResponse_ResourcesItemPhoneNumbersItemType',
    'SearchViaGetResponse_ResourcesItemPhotosItem',
    'SearchViaGetResponse_ResourcesItemPhotosItemType',
    'SearchViaGetResponse_ResourcesItemSchemasItem',
    'SearchViaGetResponse_ResourcesItemUrnIetfParamsScimSchemasExtensionEnterprise_2_0_User',
    'SearchViaPost2Request',
    'SearchViaPost2RequestSchemasItem',
    'SearchViaPost2Response',
    'SearchViaPost2Response',
    'SearchViaPost2Response',
    'SearchViaPost2Response',
    'SearchViaPost2Response',
    'SearchViaPost2Response',
    'SearchViaPost2ResponseSchemasItem',
    'SearchViaPost2ResponseSchemasItem',
    'SearchViaPost2ResponseSchemasItem',
    'SearchViaPost2ResponseSchemasItem',
    'SearchViaPost2ResponseSchemasItem',
    'SearchViaPost2ResponseSchemasItem',
    'SearchViaPost2ResponseScimType',
    'SearchViaPost2ResponseScimType',
    'SearchViaPost2ResponseScimType',
    'SearchViaPost2ResponseScimType',
    'SearchViaPost2ResponseScimType',
    'SearchViaPost2Response_ResourcesItem',
    'SearchViaPost2Response_ResourcesItemAddressesItem',
    'SearchViaPost2Response_ResourcesItemAddressesItemType',
    'SearchViaPost2Response_ResourcesItemEmailsItem',
    'SearchViaPost2Response_ResourcesItemEmailsItemType',
    'SearchViaPost2Response_ResourcesItemMeta',
    'SearchViaPost2Response_ResourcesItemMetaResourceType',
    'SearchViaPost2Response_ResourcesItemName',
    'SearchViaPost2Response_ResourcesItemPhoneNumbersItem',
    'SearchViaPost2Response_ResourcesItemPhoneNumbersItemType',
    'SearchViaPost2Response_ResourcesItemPhotosItem',
    'SearchViaPost2Response_ResourcesItemPhotosItemType',
    'SearchViaPost2Response_ResourcesItemSchemasItem',
    'SearchViaPost2Response_ResourcesItemUrnIetfParamsScimSchemasExtensionEnterprise_2_0_User',
    'ServiceProviderConfig',
    'ServiceProviderConfigAuthenticationSchemesItem',
    'ServiceProviderConfigBulk',
    'ServiceProviderConfigChangePassword',
    'ServiceProviderConfigFilter',
    'ServiceProviderConfigSchemasItem',
    'SuperviseCallPartyRequest',
    'SuperviseCallPartyRequestMode',
    'SuperviseCallPartyResponse',
    'SuperviseCallPartyResponseDirection',
    'SuperviseCallPartyResponseFrom',
    'SuperviseCallPartyResponseOwner',
    'SuperviseCallPartyResponseStatus',
    'SuperviseCallPartyResponseStatusCode',
    'SuperviseCallPartyResponseStatusPeerId',
    'SuperviseCallPartyResponseStatusReason',
    'SuperviseCallPartyResponseTo',
    'SuperviseCallSession',
    'SuperviseCallSessionDirection',
    'SuperviseCallSessionFrom',
    'SuperviseCallSessionOwner',
    'SuperviseCallSessionRequest',
    'SuperviseCallSessionRequest',
    'SuperviseCallSessionRequestMode',
    'SuperviseCallSessionRequestMode',
    'SuperviseCallSessionResponse',
    'SuperviseCallSessionResponseDirection',
    'SuperviseCallSessionResponseFrom',
    'SuperviseCallSessionResponseOwner',
    'SuperviseCallSessionResponseStatus',
    'SuperviseCallSessionResponseStatusCode',
    'SuperviseCallSessionResponseStatusPeerId',
    'SuperviseCallSessionResponseStatusReason',
    'SuperviseCallSessionResponseTo',
    'SuperviseCallSessionStatus',
    'SuperviseCallSessionStatusCode',
    'SuperviseCallSessionStatusPeerId',
    'SuperviseCallSessionStatusReason',
    'SwitchInfo',
    'SwitchInfoEmergencyAddress',
    'SwitchInfoEmergencyLocation',
    'SwitchInfoSite',
    'SwitchesList',
    'SyncAccountCallLogResponse',
    'SyncAccountCallLogResponseRecordsItem',
    'SyncAccountCallLogResponseRecordsItemAction',
    'SyncAccountCallLogResponseRecordsItemBilling',
    'SyncAccountCallLogResponseRecordsItemDelegate',
    'SyncAccountCallLogResponseRecordsItemDirection',
    'SyncAccountCallLogResponseRecordsItemExtension',
    'SyncAccountCallLogResponseRecordsItemFrom',
    'SyncAccountCallLogResponseRecordsItemFromDevice',
    'SyncAccountCallLogResponseRecordsItemLegsItem',
    'SyncAccountCallLogResponseRecordsItemLegsItemAction',
    'SyncAccountCallLogResponseRecordsItemLegsItemBilling',
    'SyncAccountCallLogResponseRecordsItemLegsItemDelegate',
    'SyncAccountCallLogResponseRecordsItemLegsItemDirection',
    'SyncAccountCallLogResponseRecordsItemLegsItemExtension',
    'SyncAccountCallLogResponseRecordsItemLegsItemFrom',
    'SyncAccountCallLogResponseRecordsItemLegsItemFromDevice',
    'SyncAccountCallLogResponseRecordsItemLegsItemLegType',
    'SyncAccountCallLogResponseRecordsItemLegsItemMessage',
    'SyncAccountCallLogResponseRecordsItemLegsItemReason',
    'SyncAccountCallLogResponseRecordsItemLegsItemRecording',
    'SyncAccountCallLogResponseRecordsItemLegsItemRecordingType',
    'SyncAccountCallLogResponseRecordsItemLegsItemResult',
    'SyncAccountCallLogResponseRecordsItemLegsItemTo',
    'SyncAccountCallLogResponseRecordsItemLegsItemToDevice',
    'SyncAccountCallLogResponseRecordsItemLegsItemTransport',
    'SyncAccountCallLogResponseRecordsItemLegsItemType',
    'SyncAccountCallLogResponseRecordsItemMessage',
    'SyncAccountCallLogResponseRecordsItemReason',
    'SyncAccountCallLogResponseRecordsItemRecording',
    'SyncAccountCallLogResponseRecordsItemRecordingType',
    'SyncAccountCallLogResponseRecordsItemResult',
    'SyncAccountCallLogResponseRecordsItemTo',
    'SyncAccountCallLogResponseRecordsItemToDevice',
    'SyncAccountCallLogResponseRecordsItemTransport',
    'SyncAccountCallLogResponseRecordsItemType',
    'SyncAccountCallLogResponseSyncInfo',
    'SyncAccountCallLogResponseSyncInfoSyncType',
    'SyncAccountCallLogStatusGroup',
    'SyncAccountCallLogSyncType',
    'SyncAccountCallLogView',
    'SyncAddressBookResponse',
    'SyncAddressBookResponseRecordsItem',
    'SyncAddressBookResponseRecordsItemAvailability',
    'SyncAddressBookResponseRecordsItemBusinessAddress',
    'SyncAddressBookResponseRecordsItemHomeAddress',
    'SyncAddressBookResponseRecordsItemOtherAddress',
    'SyncAddressBookResponseSyncInfo',
    'SyncAddressBookResponseSyncInfoSyncType',
    'SyncAddressBookSyncTypeItem',
    'SyncMessagesDirectionItem',
    'SyncMessagesMessageTypeItem',
    'SyncMessagesResponse',
    'SyncMessagesResponseRecordsItem',
    'SyncMessagesResponseRecordsItemAttachmentsItem',
    'SyncMessagesResponseRecordsItemAttachmentsItemType',
    'SyncMessagesResponseRecordsItemAvailability',
    'SyncMessagesResponseRecordsItemConversation',
    'SyncMessagesResponseRecordsItemDirection',
    'SyncMessagesResponseRecordsItemFaxResolution',
    'SyncMessagesResponseRecordsItemFrom',
    'SyncMessagesResponseRecordsItemMessageStatus',
    'SyncMessagesResponseRecordsItemPriority',
    'SyncMessagesResponseRecordsItemReadStatus',
    'SyncMessagesResponseRecordsItemToItem',
    'SyncMessagesResponseRecordsItemToItemFaxErrorCode',
    'SyncMessagesResponseRecordsItemToItemMessageStatus',
    'SyncMessagesResponseRecordsItemType',
    'SyncMessagesResponseRecordsItemVmTranscriptionStatus',
    'SyncMessagesResponseSyncInfo',
    'SyncMessagesResponseSyncInfoSyncType',
    'SyncMessagesSyncTypeItem',
    'SyncUserCallLogResponse',
    'SyncUserCallLogResponseRecordsItem',
    'SyncUserCallLogResponseRecordsItemAction',
    'SyncUserCallLogResponseRecordsItemBilling',
    'SyncUserCallLogResponseRecordsItemDelegate',
    'SyncUserCallLogResponseRecordsItemDirection',
    'SyncUserCallLogResponseRecordsItemExtension',
    'SyncUserCallLogResponseRecordsItemFrom',
    'SyncUserCallLogResponseRecordsItemFromDevice',
    'SyncUserCallLogResponseRecordsItemLegsItem',
    'SyncUserCallLogResponseRecordsItemLegsItemAction',
    'SyncUserCallLogResponseRecordsItemLegsItemBilling',
    'SyncUserCallLogResponseRecordsItemLegsItemDelegate',
    'SyncUserCallLogResponseRecordsItemLegsItemDirection',
    'SyncUserCallLogResponseRecordsItemLegsItemExtension',
    'SyncUserCallLogResponseRecordsItemLegsItemFrom',
    'SyncUserCallLogResponseRecordsItemLegsItemFromDevice',
    'SyncUserCallLogResponseRecordsItemLegsItemLegType',
    'SyncUserCallLogResponseRecordsItemLegsItemMessage',
    'SyncUserCallLogResponseRecordsItemLegsItemReason',
    'SyncUserCallLogResponseRecordsItemLegsItemRecording',
    'SyncUserCallLogResponseRecordsItemLegsItemRecordingType',
    'SyncUserCallLogResponseRecordsItemLegsItemResult',
    'SyncUserCallLogResponseRecordsItemLegsItemTo',
    'SyncUserCallLogResponseRecordsItemLegsItemToDevice',
    'SyncUserCallLogResponseRecordsItemLegsItemTransport',
    'SyncUserCallLogResponseRecordsItemLegsItemType',
    'SyncUserCallLogResponseRecordsItemMessage',
    'SyncUserCallLogResponseRecordsItemReason',
    'SyncUserCallLogResponseRecordsItemRecording',
    'SyncUserCallLogResponseRecordsItemRecordingType',
    'SyncUserCallLogResponseRecordsItemResult',
    'SyncUserCallLogResponseRecordsItemTo',
    'SyncUserCallLogResponseRecordsItemToDevice',
    'SyncUserCallLogResponseRecordsItemTransport',
    'SyncUserCallLogResponseRecordsItemType',
    'SyncUserCallLogResponseSyncInfo',
    'SyncUserCallLogResponseSyncInfoSyncType',
    'SyncUserCallLogStatusGroupItem',
    'SyncUserCallLogSyncTypeItem',
    'SyncUserCallLogView',
    'TransferCallPartyRequest',
    'TransferCallPartyResponse',
    'TransferCallPartyResponseConferenceRole',
    'TransferCallPartyResponseDirection',
    'TransferCallPartyResponseFrom',
    'TransferCallPartyResponseOwner',
    'TransferCallPartyResponsePark',
    'TransferCallPartyResponseRecordingsItem',
    'TransferCallPartyResponseRingMeRole',
    'TransferCallPartyResponseRingOutRole',
    'TransferCallPartyResponseStatus',
    'TransferCallPartyResponseStatusCode',
    'TransferCallPartyResponseStatusPeerId',
    'TransferCallPartyResponseStatusReason',
    'TransferCallPartyResponseTo',
    'TransferTarget',
    'UnholdCallPartyResponse',
    'UnholdCallPartyResponseConferenceRole',
    'UnholdCallPartyResponseDirection',
    'UnholdCallPartyResponseFrom',
    'UnholdCallPartyResponseOwner',
    'UnholdCallPartyResponsePark',
    'UnholdCallPartyResponseRecordingsItem',
    'UnholdCallPartyResponseRingMeRole',
    'UnholdCallPartyResponseRingOutRole',
    'UnholdCallPartyResponseStatus',
    'UnholdCallPartyResponseStatusCode',
    'UnholdCallPartyResponseStatusPeerId',
    'UnholdCallPartyResponseStatusReason',
    'UnholdCallPartyResponseTo',
    'UnifiedPresence',
    'UnifiedPresenceGlip',
    'UnifiedPresenceGlipAvailability',
    'UnifiedPresenceGlipStatus',
    'UnifiedPresenceGlipVisibility',
    'UnifiedPresenceListItem',
    'UnifiedPresenceMeeting',
    'UnifiedPresenceMeetingStatus',
    'UnifiedPresenceStatus',
    'UnifiedPresenceTelephony',
    'UnifiedPresenceTelephonyAvailability',
    'UnifiedPresenceTelephonyStatus',
    'UnifiedPresenceTelephonyVisibility',
    'UpdateAccountBusinessAddressRequest',
    'UpdateAccountBusinessAddressRequestBusinessAddress',
    'UpdateAccountBusinessAddressResponse',
    'UpdateAccountBusinessAddressResponseBusinessAddress',
    'UpdateAnsweringRuleRequest',
    'UpdateAnsweringRuleRequest',
    'UpdateAnsweringRuleRequestCallHandlingAction',
    'UpdateAnsweringRuleRequestCallHandlingAction',
    'UpdateAnsweringRuleRequestCalledNumbersItem',
    'UpdateAnsweringRuleRequestCallersItem',
    'UpdateAnsweringRuleRequestForwarding',
    'UpdateAnsweringRuleRequestForwarding',
    'UpdateAnsweringRuleRequestForwardingRingingMode',
    'UpdateAnsweringRuleRequestForwardingRingingMode',
    'UpdateAnsweringRuleRequestForwardingRulesItem',
    'UpdateAnsweringRuleRequestForwardingRulesItem',
    'UpdateAnsweringRuleRequestForwardingRulesItemForwardingNumbersItem',
    'UpdateAnsweringRuleRequestForwardingRulesItemForwardingNumbersItem',
    'UpdateAnsweringRuleRequestForwardingRulesItemForwardingNumbersItemLabel',
    'UpdateAnsweringRuleRequestForwardingRulesItemForwardingNumbersItemLabel',
    'UpdateAnsweringRuleRequestForwardingRulesItemForwardingNumbersItemType',
    'UpdateAnsweringRuleRequestForwardingRulesItemForwardingNumbersItemType',
    'UpdateAnsweringRuleRequestGreetingsItem',
    'UpdateAnsweringRuleRequestGreetingsItemCustom',
    'UpdateAnsweringRuleRequestGreetingsItemPreset',
    'UpdateAnsweringRuleRequestGreetingsItemType',
    'UpdateAnsweringRuleRequestGreetingsItemUsageType',
    'UpdateAnsweringRuleRequestQueue',
    'UpdateAnsweringRuleRequestQueueFixedOrderAgentsItem',
    'UpdateAnsweringRuleRequestQueueFixedOrderAgentsItemExtension',
    'UpdateAnsweringRuleRequestQueueHoldAudioInterruptionMode',
    'UpdateAnsweringRuleRequestQueueHoldTimeExpirationAction',
    'UpdateAnsweringRuleRequestQueueMaxCallersAction',
    'UpdateAnsweringRuleRequestQueueNoAnswerAction',
    'UpdateAnsweringRuleRequestQueueTransferItem',
    'UpdateAnsweringRuleRequestQueueTransferItemAction',
    'UpdateAnsweringRuleRequestQueueTransferItemExtension',
    'UpdateAnsweringRuleRequestQueueTransferMode',
    'UpdateAnsweringRuleRequestQueueUnconditionalForwardingItem',
    'UpdateAnsweringRuleRequestQueueUnconditionalForwardingItemAction',
    'UpdateAnsweringRuleRequestSchedule',
    'UpdateAnsweringRuleRequestScheduleRangesItem',
    'UpdateAnsweringRuleRequestScheduleRef',
    'UpdateAnsweringRuleRequestScheduleWeeklyRanges',
    'UpdateAnsweringRuleRequestScheduleWeeklyRangesFridayItem',
    'UpdateAnsweringRuleRequestScheduleWeeklyRangesMondayItem',
    'UpdateAnsweringRuleRequestScheduleWeeklyRangesSaturdayItem',
    'UpdateAnsweringRuleRequestScheduleWeeklyRangesSundayItem',
    'UpdateAnsweringRuleRequestScheduleWeeklyRangesThursdayItem',
    'UpdateAnsweringRuleRequestScheduleWeeklyRangesTuesdayItem',
    'UpdateAnsweringRuleRequestScheduleWeeklyRangesWednesdayItem',
    'UpdateAnsweringRuleRequestScreening',
    'UpdateAnsweringRuleRequestScreening',
    'UpdateAnsweringRuleRequestTransfer',
    'UpdateAnsweringRuleRequestTransferExtension',
    'UpdateAnsweringRuleRequestType',
    'UpdateAnsweringRuleRequestType',
    'UpdateAnsweringRuleRequestUnconditionalForwarding',
    'UpdateAnsweringRuleRequestUnconditionalForwardingAction',
    'UpdateAnsweringRuleRequestVoicemail',
    'UpdateAnsweringRuleRequestVoicemailRecipient',
    'UpdateAnsweringRuleResponse',
    'UpdateAnsweringRuleResponseCallHandlingAction',
    'UpdateAnsweringRuleResponseCalledNumbersItem',
    'UpdateAnsweringRuleResponseCallersItem',
    'UpdateAnsweringRuleResponseForwarding',
    'UpdateAnsweringRuleResponseForwardingRingingMode',
    'UpdateAnsweringRuleResponseForwardingRulesItem',
    'UpdateAnsweringRuleResponseForwardingRulesItemForwardingNumbersItem',
    'UpdateAnsweringRuleResponseForwardingRulesItemForwardingNumbersItemLabel',
    'UpdateAnsweringRuleResponseForwardingRulesItemForwardingNumbersItemType',
    'UpdateAnsweringRuleResponseGreetingsItem',
    'UpdateAnsweringRuleResponseGreetingsItemCustom',
    'UpdateAnsweringRuleResponseGreetingsItemPreset',
    'UpdateAnsweringRuleResponseGreetingsItemType',
    'UpdateAnsweringRuleResponseGreetingsItemUsageType',
    'UpdateAnsweringRuleResponseQueue',
    'UpdateAnsweringRuleResponseQueueFixedOrderAgentsItem',
    'UpdateAnsweringRuleResponseQueueFixedOrderAgentsItemExtension',
    'UpdateAnsweringRuleResponseQueueHoldAudioInterruptionMode',
    'UpdateAnsweringRuleResponseQueueHoldTimeExpirationAction',
    'UpdateAnsweringRuleResponseQueueMaxCallersAction',
    'UpdateAnsweringRuleResponseQueueNoAnswerAction',
    'UpdateAnsweringRuleResponseQueueTransferItem',
    'UpdateAnsweringRuleResponseQueueTransferItemAction',
    'UpdateAnsweringRuleResponseQueueTransferItemExtension',
    'UpdateAnsweringRuleResponseQueueTransferMode',
    'UpdateAnsweringRuleResponseQueueUnconditionalForwardingItem',
    'UpdateAnsweringRuleResponseQueueUnconditionalForwardingItemAction',
    'UpdateAnsweringRuleResponseSchedule',
    'UpdateAnsweringRuleResponseScheduleRangesItem',
    'UpdateAnsweringRuleResponseScheduleRef',
    'UpdateAnsweringRuleResponseScheduleWeeklyRanges',
    'UpdateAnsweringRuleResponseScheduleWeeklyRangesFridayItem',
    'UpdateAnsweringRuleResponseScheduleWeeklyRangesMondayItem',
    'UpdateAnsweringRuleResponseScheduleWeeklyRangesSaturdayItem',
    'UpdateAnsweringRuleResponseScheduleWeeklyRangesSundayItem',
    'UpdateAnsweringRuleResponseScheduleWeeklyRangesThursdayItem',
    'UpdateAnsweringRuleResponseScheduleWeeklyRangesTuesdayItem',
    'UpdateAnsweringRuleResponseScheduleWeeklyRangesWednesdayItem',
    'UpdateAnsweringRuleResponseScreening',
    'UpdateAnsweringRuleResponseSharedLines',
    'UpdateAnsweringRuleResponseTransfer',
    'UpdateAnsweringRuleResponseTransferExtension',
    'UpdateAnsweringRuleResponseType',
    'UpdateAnsweringRuleResponseUnconditionalForwarding',
    'UpdateAnsweringRuleResponseUnconditionalForwardingAction',
    'UpdateAnsweringRuleResponseVoicemail',
    'UpdateAnsweringRuleResponseVoicemailRecipient',
    'UpdateBlockedAllowedNumberRequest',
    'UpdateBlockedAllowedNumberRequestStatus',
    'UpdateBlockedAllowedNumberResponse',
    'UpdateBlockedAllowedNumberResponseStatus',
    'UpdateCallMonitoringGroupListRequest',
    'UpdateCallMonitoringGroupListRequestAddedExtensionsItem',
    'UpdateCallMonitoringGroupListRequestAddedExtensionsItemPermissionsItem',
    'UpdateCallMonitoringGroupListRequestRemovedExtensionsItem',
    'UpdateCallMonitoringGroupListRequestRemovedExtensionsItemPermissionsItem',
    'UpdateCallMonitoringGroupListRequestUpdatedExtensionsItem',
    'UpdateCallMonitoringGroupListRequestUpdatedExtensionsItemPermissionsItem',
    'UpdateCallMonitoringGroupRequest',
    'UpdateCallMonitoringGroupResponse',
    'UpdateCallPartyRequest',
    'UpdateCallPartyRequestParty',
    'UpdateCallPartyResponse',
    'UpdateCallPartyResponseConferenceRole',
    'UpdateCallPartyResponseDirection',
    'UpdateCallPartyResponseFrom',
    'UpdateCallPartyResponseOwner',
    'UpdateCallPartyResponsePark',
    'UpdateCallPartyResponseRecordingsItem',
    'UpdateCallPartyResponseRingMeRole',
    'UpdateCallPartyResponseRingOutRole',
    'UpdateCallPartyResponseStatus',
    'UpdateCallPartyResponseStatusCode',
    'UpdateCallPartyResponseStatusPeerId',
    'UpdateCallPartyResponseStatusReason',
    'UpdateCallPartyResponseTo',
    'UpdateCallQueueInfoRequest',
    'UpdateCallQueueInfoRequestServiceLevelSettings',
    'UpdateCallQueueInfoResponse',
    'UpdateCallQueueInfoResponseServiceLevelSettings',
    'UpdateCallQueueInfoResponseStatus',
    'UpdateCallQueuePresenceRequest',
    'UpdateCallQueuePresenceRequestRecordsItem',
    'UpdateCallQueuePresenceRequestRecordsItemMember',
    'UpdateCallQueuePresenceResponse',
    'UpdateCallQueuePresenceResponseRecordsItem',
    'UpdateCallQueuePresenceResponseRecordsItemMember',
    'UpdateCallQueuePresenceResponseRecordsItemMemberSite',
    'UpdateCallRecordingExtensionListRequest',
    'UpdateCallRecordingExtensionListRequestAddedExtensionsItem',
    'UpdateCallRecordingExtensionListRequestAddedExtensionsItemCallDirection',
    'UpdateCallRecordingExtensionListRequestRemovedExtensionsItem',
    'UpdateCallRecordingExtensionListRequestRemovedExtensionsItemCallDirection',
    'UpdateCallRecordingExtensionListRequestUpdatedExtensionsItem',
    'UpdateCallRecordingExtensionListRequestUpdatedExtensionsItemCallDirection',
    'UpdateCallRecordingSettingsRequest',
    'UpdateCallRecordingSettingsRequestAutomatic',
    'UpdateCallRecordingSettingsRequestGreetingsItem',
    'UpdateCallRecordingSettingsRequestGreetingsItemMode',
    'UpdateCallRecordingSettingsRequestGreetingsItemType',
    'UpdateCallRecordingSettingsRequestOnDemand',
    'UpdateCallRecordingSettingsResponse',
    'UpdateCallRecordingSettingsResponseAutomatic',
    'UpdateCallRecordingSettingsResponseGreetingsItem',
    'UpdateCallRecordingSettingsResponseGreetingsItemMode',
    'UpdateCallRecordingSettingsResponseGreetingsItemType',
    'UpdateCallRecordingSettingsResponseOnDemand',
    'UpdateCallerBlockingSettingsRequest',
    'UpdateCallerBlockingSettingsRequestGreetingsItem',
    'UpdateCallerBlockingSettingsRequestGreetingsItemPreset',
    'UpdateCallerBlockingSettingsRequestMode',
    'UpdateCallerBlockingSettingsRequestNoCallerId',
    'UpdateCallerBlockingSettingsRequestPayPhones',
    'UpdateCallerBlockingSettingsResponse',
    'UpdateCallerBlockingSettingsResponseGreetingsItem',
    'UpdateCallerBlockingSettingsResponseGreetingsItemPreset',
    'UpdateCallerBlockingSettingsResponseMode',
    'UpdateCallerBlockingSettingsResponseNoCallerId',
    'UpdateCallerBlockingSettingsResponsePayPhones',
    'UpdateCompanyAnsweringRuleRequest',
    'UpdateCompanyAnsweringRuleRequestCallHandlingAction',
    'UpdateCompanyAnsweringRuleRequestCalledNumbersItem',
    'UpdateCompanyAnsweringRuleRequestCallersItem',
    'UpdateCompanyAnsweringRuleRequestGreetingsItem',
    'UpdateCompanyAnsweringRuleRequestGreetingsItemCustom',
    'UpdateCompanyAnsweringRuleRequestGreetingsItemPreset',
    'UpdateCompanyAnsweringRuleRequestGreetingsItemType',
    'UpdateCompanyAnsweringRuleRequestGreetingsItemUsageType',
    'UpdateCompanyAnsweringRuleRequestSchedule',
    'UpdateCompanyAnsweringRuleRequestScheduleRangesItem',
    'UpdateCompanyAnsweringRuleRequestScheduleRef',
    'UpdateCompanyAnsweringRuleRequestScheduleWeeklyRanges',
    'UpdateCompanyAnsweringRuleRequestScheduleWeeklyRangesFridayItem',
    'UpdateCompanyAnsweringRuleRequestScheduleWeeklyRangesMondayItem',
    'UpdateCompanyAnsweringRuleRequestScheduleWeeklyRangesSaturdayItem',
    'UpdateCompanyAnsweringRuleRequestScheduleWeeklyRangesSundayItem',
    'UpdateCompanyAnsweringRuleRequestScheduleWeeklyRangesThursdayItem',
    'UpdateCompanyAnsweringRuleRequestScheduleWeeklyRangesTuesdayItem',
    'UpdateCompanyAnsweringRuleRequestScheduleWeeklyRangesWednesdayItem',
    'UpdateCompanyAnsweringRuleRequestType',
    'UpdateCompanyAnsweringRuleResponse',
    'UpdateCompanyAnsweringRuleResponseCallHandlingAction',
    'UpdateCompanyAnsweringRuleResponseCalledNumbersItem',
    'UpdateCompanyAnsweringRuleResponseCallersItem',
    'UpdateCompanyAnsweringRuleResponseExtension',
    'UpdateCompanyAnsweringRuleResponseGreetingsItem',
    'UpdateCompanyAnsweringRuleResponseGreetingsItemCustom',
    'UpdateCompanyAnsweringRuleResponseGreetingsItemPreset',
    'UpdateCompanyAnsweringRuleResponseGreetingsItemType',
    'UpdateCompanyAnsweringRuleResponseGreetingsItemUsageType',
    'UpdateCompanyAnsweringRuleResponseSchedule',
    'UpdateCompanyAnsweringRuleResponseScheduleRangesItem',
    'UpdateCompanyAnsweringRuleResponseScheduleRef',
    'UpdateCompanyAnsweringRuleResponseScheduleWeeklyRanges',
    'UpdateCompanyAnsweringRuleResponseScheduleWeeklyRangesFridayItem',
    'UpdateCompanyAnsweringRuleResponseScheduleWeeklyRangesMondayItem',
    'UpdateCompanyAnsweringRuleResponseScheduleWeeklyRangesSaturdayItem',
    'UpdateCompanyAnsweringRuleResponseScheduleWeeklyRangesSundayItem',
    'UpdateCompanyAnsweringRuleResponseScheduleWeeklyRangesThursdayItem',
    'UpdateCompanyAnsweringRuleResponseScheduleWeeklyRangesTuesdayItem',
    'UpdateCompanyAnsweringRuleResponseScheduleWeeklyRangesWednesdayItem',
    'UpdateCompanyAnsweringRuleResponseType',
    'UpdateCompanyBusinessHoursRequest',
    'UpdateCompanyBusinessHoursRequestSchedule',
    'UpdateCompanyBusinessHoursRequestScheduleWeeklyRanges',
    'UpdateCompanyBusinessHoursRequestScheduleWeeklyRangesFridayItem',
    'UpdateCompanyBusinessHoursRequestScheduleWeeklyRangesMondayItem',
    'UpdateCompanyBusinessHoursRequestScheduleWeeklyRangesSaturdayItem',
    'UpdateCompanyBusinessHoursRequestScheduleWeeklyRangesSundayItem',
    'UpdateCompanyBusinessHoursRequestScheduleWeeklyRangesThursdayItem',
    'UpdateCompanyBusinessHoursRequestScheduleWeeklyRangesTuesdayItem',
    'UpdateCompanyBusinessHoursRequestScheduleWeeklyRangesWednesdayItem',
    'UpdateCompanyBusinessHoursResponse',
    'UpdateCompanyBusinessHoursResponseSchedule',
    'UpdateCompanyBusinessHoursResponseScheduleWeeklyRanges',
    'UpdateCompanyBusinessHoursResponseScheduleWeeklyRangesFridayItem',
    'UpdateCompanyBusinessHoursResponseScheduleWeeklyRangesMondayItem',
    'UpdateCompanyBusinessHoursResponseScheduleWeeklyRangesSaturdayItem',
    'UpdateCompanyBusinessHoursResponseScheduleWeeklyRangesSundayItem',
    'UpdateCompanyBusinessHoursResponseScheduleWeeklyRangesThursdayItem',
    'UpdateCompanyBusinessHoursResponseScheduleWeeklyRangesTuesdayItem',
    'UpdateCompanyBusinessHoursResponseScheduleWeeklyRangesWednesdayItem',
    'UpdateConferencingInfoRequest',
    'UpdateConferencingInfoRequestPhoneNumbersItem',
    'UpdateConferencingSettingsRequest',
    'UpdateConferencingSettingsRequestPhoneNumbersItem',
    'UpdateConferencingSettingsResponse',
    'UpdateConferencingSettingsResponsePhoneNumbersItem',
    'UpdateConferencingSettingsResponsePhoneNumbersItemCountry',
    'UpdateContactResponse',
    'UpdateContactResponseAvailability',
    'UpdateContactResponseBusinessAddress',
    'UpdateContactResponseHomeAddress',
    'UpdateContactResponseOtherAddress',
    'UpdateCustomFieldRequest',
    'UpdateCustomFieldResponse',
    'UpdateCustomFieldResponseCategory',
    'UpdateDeviceRequest',
    'UpdateDeviceRequestEmergency',
    'UpdateDeviceRequestEmergencyAddress',
    'UpdateDeviceRequestEmergencyAddressEditableStatus',
    'UpdateDeviceRequestEmergencyAddressStatus',
    'UpdateDeviceRequestEmergencyLocation',
    'UpdateDeviceRequestEmergencyServiceAddress',
    'UpdateDeviceRequestEmergencySyncStatus',
    'UpdateDeviceRequestExtension',
    'UpdateDeviceRequestPhoneLines',
    'UpdateDeviceRequestPhoneLinesPhoneLinesItem',
    'UpdateDeviceResponse',
    'UpdateDeviceResponseBillingStatement',
    'UpdateDeviceResponseBillingStatementChargesItem',
    'UpdateDeviceResponseBillingStatementFeesItem',
    'UpdateDeviceResponseEmergency',
    'UpdateDeviceResponseEmergencyAddress',
    'UpdateDeviceResponseEmergencyAddressEditableStatus',
    'UpdateDeviceResponseEmergencyAddressStatus',
    'UpdateDeviceResponseEmergencyLocation',
    'UpdateDeviceResponseEmergencyServiceAddress',
    'UpdateDeviceResponseEmergencyServiceAddressSyncStatus',
    'UpdateDeviceResponseEmergencySyncStatus',
    'UpdateDeviceResponseExtension',
    'UpdateDeviceResponseLinePooling',
    'UpdateDeviceResponseModel',
    'UpdateDeviceResponseModelAddonsItem',
    'UpdateDeviceResponseModelFeaturesItem',
    'UpdateDeviceResponsePhoneLinesItem',
    'UpdateDeviceResponsePhoneLinesItemEmergencyAddress',
    'UpdateDeviceResponsePhoneLinesItemLineType',
    'UpdateDeviceResponsePhoneLinesItemPhoneInfo',
    'UpdateDeviceResponsePhoneLinesItemPhoneInfoCountry',
    'UpdateDeviceResponsePhoneLinesItemPhoneInfoExtension',
    'UpdateDeviceResponsePhoneLinesItemPhoneInfoPaymentType',
    'UpdateDeviceResponsePhoneLinesItemPhoneInfoType',
    'UpdateDeviceResponsePhoneLinesItemPhoneInfoUsageType',
    'UpdateDeviceResponseShipping',
    'UpdateDeviceResponseShippingAddress',
    'UpdateDeviceResponseShippingMethod',
    'UpdateDeviceResponseShippingMethodId',
    'UpdateDeviceResponseShippingMethodName',
    'UpdateDeviceResponseShippingStatus',
    'UpdateDeviceResponseSite',
    'UpdateDeviceResponseStatus',
    'UpdateDeviceResponseType',
    'UpdateEmergencyLocationResponse',
    'UpdateEmergencyLocationResponseAddress',
    'UpdateEmergencyLocationResponseAddressStatus',
    'UpdateEmergencyLocationResponseOwnersItem',
    'UpdateEmergencyLocationResponseSite',
    'UpdateEmergencyLocationResponseSyncStatus',
    'UpdateEmergencyLocationResponseUsageStatus',
    'UpdateEmergencyLocationResponseVisibility',
    'UpdateEventResponse',
    'UpdateEventResponseColor',
    'UpdateEventResponseEndingOn',
    'UpdateEventResponseRecurrence',
    'UpdateExtensionCallQueuePresenceRequest',
    'UpdateExtensionCallQueuePresenceRequestRecordsItem',
    'UpdateExtensionCallQueuePresenceRequestRecordsItemCallQueue',
    'UpdateExtensionCallQueuePresenceResponse',
    'UpdateExtensionCallQueuePresenceResponseRecordsItem',
    'UpdateExtensionCallQueuePresenceResponseRecordsItemCallQueue',
    'UpdateExtensionCallerIdRequest',
    'UpdateExtensionCallerIdRequestByDeviceItem',
    'UpdateExtensionCallerIdRequestByDeviceItemCallerId',
    'UpdateExtensionCallerIdRequestByDeviceItemCallerIdPhoneInfo',
    'UpdateExtensionCallerIdRequestByDeviceItemDevice',
    'UpdateExtensionCallerIdRequestByFeatureItem',
    'UpdateExtensionCallerIdRequestByFeatureItemCallerId',
    'UpdateExtensionCallerIdRequestByFeatureItemCallerIdPhoneInfo',
    'UpdateExtensionCallerIdRequestByFeatureItemFeature',
    'UpdateExtensionCallerIdResponse',
    'UpdateExtensionCallerIdResponseByDeviceItem',
    'UpdateExtensionCallerIdResponseByDeviceItemCallerId',
    'UpdateExtensionCallerIdResponseByDeviceItemCallerIdPhoneInfo',
    'UpdateExtensionCallerIdResponseByDeviceItemDevice',
    'UpdateExtensionCallerIdResponseByFeatureItem',
    'UpdateExtensionCallerIdResponseByFeatureItemCallerId',
    'UpdateExtensionCallerIdResponseByFeatureItemCallerIdPhoneInfo',
    'UpdateExtensionCallerIdResponseByFeatureItemFeature',
    'UpdateExtensionRequest',
    'UpdateExtensionRequestCallQueueInfo',
    'UpdateExtensionRequestContact',
    'UpdateExtensionRequestContactBusinessAddress',
    'UpdateExtensionRequestContactPronouncedName',
    'UpdateExtensionRequestContactPronouncedNamePrompt',
    'UpdateExtensionRequestContactPronouncedNamePromptContentType',
    'UpdateExtensionRequestContactPronouncedNameType',
    'UpdateExtensionRequestCustomFieldsItem',
    'UpdateExtensionRequestReferencesItem',
    'UpdateExtensionRequestReferencesItemType',
    'UpdateExtensionRequestRegionalSettings',
    'UpdateExtensionRequestRegionalSettingsFormattingLocale',
    'UpdateExtensionRequestRegionalSettingsGreetingLanguage',
    'UpdateExtensionRequestRegionalSettingsHomeCountry',
    'UpdateExtensionRequestRegionalSettingsLanguage',
    'UpdateExtensionRequestRegionalSettingsTimeFormat',
    'UpdateExtensionRequestRegionalSettingsTimezone',
    'UpdateExtensionRequestSetupWizardState',
    'UpdateExtensionRequestSite',
    'UpdateExtensionRequestStatus',
    'UpdateExtensionRequestStatusInfo',
    'UpdateExtensionRequestStatusInfoReason',
    'UpdateExtensionRequestTransitionItem',
    'UpdateExtensionRequestType',
    'UpdateExtensionResponse',
    'UpdateExtensionResponseAccount',
    'UpdateExtensionResponseCallQueueInfo',
    'UpdateExtensionResponseContact',
    'UpdateExtensionResponseContactBusinessAddress',
    'UpdateExtensionResponseContactPronouncedName',
    'UpdateExtensionResponseContactPronouncedNamePrompt',
    'UpdateExtensionResponseContactPronouncedNamePromptContentType',
    'UpdateExtensionResponseContactPronouncedNameType',
    'UpdateExtensionResponseCustomFieldsItem',
    'UpdateExtensionResponseDepartmentsItem',
    'UpdateExtensionResponsePermissions',
    'UpdateExtensionResponsePermissionsAdmin',
    'UpdateExtensionResponsePermissionsInternationalCalling',
    'UpdateExtensionResponseProfileImage',
    'UpdateExtensionResponseProfileImageScalesItem',
    'UpdateExtensionResponseReferencesItem',
    'UpdateExtensionResponseReferencesItemType',
    'UpdateExtensionResponseRegionalSettings',
    'UpdateExtensionResponseRegionalSettingsFormattingLocale',
    'UpdateExtensionResponseRegionalSettingsGreetingLanguage',
    'UpdateExtensionResponseRegionalSettingsHomeCountry',
    'UpdateExtensionResponseRegionalSettingsLanguage',
    'UpdateExtensionResponseRegionalSettingsTimeFormat',
    'UpdateExtensionResponseRegionalSettingsTimezone',
    'UpdateExtensionResponseRolesItem',
    'UpdateExtensionResponseServiceFeaturesItem',
    'UpdateExtensionResponseServiceFeaturesItemFeatureName',
    'UpdateExtensionResponseSetupWizardState',
    'UpdateExtensionResponseSite',
    'UpdateExtensionResponseStatus',
    'UpdateExtensionResponseStatusInfo',
    'UpdateExtensionResponseStatusInfoReason',
    'UpdateExtensionResponseType',
    'UpdateFavoriteContactListRequest',
    'UpdateFavoriteContactListRequestRecordsItem',
    'UpdateFavoriteContactListResponse',
    'UpdateFavoriteContactListResponseRecordsItem',
    'UpdateForwardingNumberRequest',
    'UpdateForwardingNumberRequest',
    'UpdateForwardingNumberRequestLabel',
    'UpdateForwardingNumberRequestLabel',
    'UpdateForwardingNumberRequestType',
    'UpdateForwardingNumberRequestType',
    'UpdateForwardingNumberResponse',
    'UpdateForwardingNumberResponseDevice',
    'UpdateForwardingNumberResponseFeaturesItem',
    'UpdateForwardingNumberResponseLabel',
    'UpdateForwardingNumberResponseType',
    'UpdateGlipEveryoneRequest',
    'UpdateIVRMenuResponse',
    'UpdateIVRMenuResponseActionsItem',
    'UpdateIVRMenuResponseActionsItemAction',
    'UpdateIVRMenuResponseActionsItemExtension',
    'UpdateIVRMenuResponsePrompt',
    'UpdateIVRMenuResponsePromptAudio',
    'UpdateIVRMenuResponsePromptLanguage',
    'UpdateIVRMenuResponsePromptMode',
    'UpdateIVRPromptRequest',
    'UpdateIVRPromptRequest',
    'UpdateIVRPromptResponse',
    'UpdateMeetingResponse',
    'UpdateMeetingResponseHost',
    'UpdateMeetingResponseLinks',
    'UpdateMeetingResponseMeetingType',
    'UpdateMeetingResponseOccurrencesItem',
    'UpdateMeetingResponseSchedule',
    'UpdateMeetingResponseScheduleTimeZone',
    'UpdateMeetingServiceInfoRequest',
    'UpdateMeetingServiceInfoRequestExternalUserInfo',
    'UpdateMeetingServiceInfoResponse',
    'UpdateMeetingServiceInfoResponseDialInNumbersItem',
    'UpdateMeetingServiceInfoResponseDialInNumbersItemCountry',
    'UpdateMeetingServiceInfoResponseExternalUserInfo',
    'UpdateMessageRequest',
    'UpdateMessageRequest',
    'UpdateMessageRequestReadStatus',
    'UpdateMessageRequestReadStatus',
    'UpdateMessageResponse',
    'UpdateMessageResponse',
    'UpdateMessageResponseAttachmentsItem',
    'UpdateMessageResponseAttachmentsItemType',
    'UpdateMessageResponseAvailability',
    'UpdateMessageResponseBody',
    'UpdateMessageResponseBodyAttachmentsItem',
    'UpdateMessageResponseBodyAttachmentsItemType',
    'UpdateMessageResponseBodyAvailability',
    'UpdateMessageResponseBodyConversation',
    'UpdateMessageResponseBodyDirection',
    'UpdateMessageResponseBodyFaxResolution',
    'UpdateMessageResponseBodyFrom',
    'UpdateMessageResponseBodyMessageStatus',
    'UpdateMessageResponseBodyPriority',
    'UpdateMessageResponseBodyReadStatus',
    'UpdateMessageResponseBodyToItem',
    'UpdateMessageResponseBodyType',
    'UpdateMessageResponseBodyVmTranscriptionStatus',
    'UpdateMessageResponseConversation',
    'UpdateMessageResponseDirection',
    'UpdateMessageResponseFaxResolution',
    'UpdateMessageResponseFrom',
    'UpdateMessageResponseMessageStatus',
    'UpdateMessageResponsePriority',
    'UpdateMessageResponseReadStatus',
    'UpdateMessageResponseToItem',
    'UpdateMessageResponseToItemFaxErrorCode',
    'UpdateMessageResponseToItemMessageStatus',
    'UpdateMessageResponseType',
    'UpdateMessageResponseVmTranscriptionStatus',
    'UpdateMessageStoreConfigurationRequest',
    'UpdateMessageStoreConfigurationResponse',
    'UpdateMessageType',
    'UpdateMultipleSwitchesRequest',
    'UpdateMultipleSwitchesRequest',
    'UpdateMultipleSwitchesRequestRecordsItem',
    'UpdateMultipleSwitchesRequestRecordsItemEmergencyAddress',
    'UpdateMultipleSwitchesRequestRecordsItemEmergencyLocation',
    'UpdateMultipleSwitchesRequestRecordsItemSite',
    'UpdateMultipleSwitchesResponse',
    'UpdateMultipleSwitchesResponse',
    'UpdateMultipleSwitchesResponseTask',
    'UpdateMultipleSwitchesResponseTaskStatus',
    'UpdateMultipleWirelessPointsRequest',
    'UpdateMultipleWirelessPointsRequest',
    'UpdateMultipleWirelessPointsRequestRecordsItem',
    'UpdateMultipleWirelessPointsRequestRecordsItem',
    'UpdateMultipleWirelessPointsRequestRecordsItemEmergencyAddress',
    'UpdateMultipleWirelessPointsRequestRecordsItemEmergencyAddress',
    'UpdateMultipleWirelessPointsRequestRecordsItemEmergencyLocation',
    'UpdateMultipleWirelessPointsRequestRecordsItemSite',
    'UpdateMultipleWirelessPointsResponse',
    'UpdateMultipleWirelessPointsResponse',
    'UpdateMultipleWirelessPointsResponseTask',
    'UpdateMultipleWirelessPointsResponseTask',
    'UpdateMultipleWirelessPointsResponseTaskStatus',
    'UpdateMultipleWirelessPointsResponseTaskStatus',
    'UpdateNetworkRequest',
    'UpdateNetworkRequest',
    'UpdateNetworkRequestEmergencyLocation',
    'UpdateNetworkRequestPrivateIpRangesItem',
    'UpdateNetworkRequestPrivateIpRangesItemEmergencyAddress',
    'UpdateNetworkRequestPublicIpRangesItem',
    'UpdateNetworkRequestSite',
    'UpdateNotificationSettingsRequest',
    'UpdateNotificationSettingsRequestInboundFaxes',
    'UpdateNotificationSettingsRequestInboundTexts',
    'UpdateNotificationSettingsRequestMissedCalls',
    'UpdateNotificationSettingsRequestOutboundFaxes',
    'UpdateNotificationSettingsRequestVoicemails',
    'UpdateNotificationSettingsResponse',
    'UpdateNotificationSettingsResponseEmailRecipientsItem',
    'UpdateNotificationSettingsResponseEmailRecipientsItemPermission',
    'UpdateNotificationSettingsResponseEmailRecipientsItemStatus',
    'UpdateNotificationSettingsResponseInboundFaxes',
    'UpdateNotificationSettingsResponseInboundTexts',
    'UpdateNotificationSettingsResponseMissedCalls',
    'UpdateNotificationSettingsResponseOutboundFaxes',
    'UpdateNotificationSettingsResponseVoicemails',
    'UpdateSubscriptionRequest',
    'UpdateSubscriptionRequestDeliveryMode',
    'UpdateSubscriptionRequestDeliveryModeTransportType',
    'UpdateSubscriptionResponse',
    'UpdateSubscriptionResponseBlacklistedData',
    'UpdateSubscriptionResponseDeliveryMode',
    'UpdateSubscriptionResponseDeliveryModeTransportType',
    'UpdateSubscriptionResponseDisabledFiltersItem',
    'UpdateSubscriptionResponseStatus',
    'UpdateSubscriptionResponseTransportType',
    'UpdateSwitchInfo',
    'UpdateSwitchRequest',
    'UpdateSwitchRequestEmergencyAddress',
    'UpdateSwitchRequestEmergencyLocation',
    'UpdateSwitchRequestSite',
    'UpdateSwitchResponse',
    'UpdateSwitchResponseEmergencyAddress',
    'UpdateSwitchResponseEmergencyLocation',
    'UpdateSwitchResponseSite',
    'UpdateUnifiedPresence',
    'UpdateUnifiedPresenceGlip',
    'UpdateUnifiedPresenceGlipAvailability',
    'UpdateUnifiedPresenceGlipVisibility',
    'UpdateUnifiedPresenceRequest',
    'UpdateUnifiedPresenceRequestGlip',
    'UpdateUnifiedPresenceRequestGlipAvailability',
    'UpdateUnifiedPresenceRequestGlipVisibility',
    'UpdateUnifiedPresenceRequestTelephony',
    'UpdateUnifiedPresenceRequestTelephonyAvailability',
    'UpdateUnifiedPresenceResponse',
    'UpdateUnifiedPresenceResponseGlip',
    'UpdateUnifiedPresenceResponseGlipAvailability',
    'UpdateUnifiedPresenceResponseGlipStatus',
    'UpdateUnifiedPresenceResponseGlipVisibility',
    'UpdateUnifiedPresenceResponseMeeting',
    'UpdateUnifiedPresenceResponseMeetingStatus',
    'UpdateUnifiedPresenceResponseStatus',
    'UpdateUnifiedPresenceResponseTelephony',
    'UpdateUnifiedPresenceResponseTelephonyAvailability',
    'UpdateUnifiedPresenceResponseTelephonyStatus',
    'UpdateUnifiedPresenceResponseTelephonyVisibility',
    'UpdateUnifiedPresenceTelephony',
    'UpdateUnifiedPresenceTelephonyAvailability',
    'UpdateUserBusinessHoursRequest',
    'UpdateUserBusinessHoursRequestSchedule',
    'UpdateUserBusinessHoursRequestScheduleWeeklyRanges',
    'UpdateUserBusinessHoursRequestScheduleWeeklyRangesFridayItem',
    'UpdateUserBusinessHoursRequestScheduleWeeklyRangesMondayItem',
    'UpdateUserBusinessHoursRequestScheduleWeeklyRangesSaturdayItem',
    'UpdateUserBusinessHoursRequestScheduleWeeklyRangesSundayItem',
    'UpdateUserBusinessHoursRequestScheduleWeeklyRangesThursdayItem',
    'UpdateUserBusinessHoursRequestScheduleWeeklyRangesTuesdayItem',
    'UpdateUserBusinessHoursRequestScheduleWeeklyRangesWednesdayItem',
    'UpdateUserBusinessHoursResponse',
    'UpdateUserBusinessHoursResponseSchedule',
    'UpdateUserBusinessHoursResponseScheduleWeeklyRanges',
    'UpdateUserBusinessHoursResponseScheduleWeeklyRangesFridayItem',
    'UpdateUserBusinessHoursResponseScheduleWeeklyRangesMondayItem',
    'UpdateUserBusinessHoursResponseScheduleWeeklyRangesSaturdayItem',
    'UpdateUserBusinessHoursResponseScheduleWeeklyRangesSundayItem',
    'UpdateUserBusinessHoursResponseScheduleWeeklyRangesThursdayItem',
    'UpdateUserBusinessHoursResponseScheduleWeeklyRangesTuesdayItem',
    'UpdateUserBusinessHoursResponseScheduleWeeklyRangesWednesdayItem',
    'UpdateUserCallQueuesRequest',
    'UpdateUserCallQueuesRequestRecordsItem',
    'UpdateUserCallQueuesResponse',
    'UpdateUserCallQueuesResponseRecordsItem',
    'UpdateUserPresenceStatusRequest',
    'UpdateUserPresenceStatusRequestActiveCallsItem',
    'UpdateUserPresenceStatusRequestActiveCallsItemAdditional',
    'UpdateUserPresenceStatusRequestActiveCallsItemAdditionalType',
    'UpdateUserPresenceStatusRequestActiveCallsItemDirection',
    'UpdateUserPresenceStatusRequestActiveCallsItemPrimary',
    'UpdateUserPresenceStatusRequestActiveCallsItemPrimaryType',
    'UpdateUserPresenceStatusRequestActiveCallsItemSipData',
    'UpdateUserPresenceStatusRequestActiveCallsItemTelephonyStatus',
    'UpdateUserPresenceStatusRequestDndStatus',
    'UpdateUserPresenceStatusRequestUserStatus',
    'UpdateUserPresenceStatusResponse',
    'UpdateUserPresenceStatusResponseActiveCallsItem',
    'UpdateUserPresenceStatusResponseActiveCallsItemAdditional',
    'UpdateUserPresenceStatusResponseActiveCallsItemAdditionalType',
    'UpdateUserPresenceStatusResponseActiveCallsItemDirection',
    'UpdateUserPresenceStatusResponseActiveCallsItemPrimary',
    'UpdateUserPresenceStatusResponseActiveCallsItemPrimaryType',
    'UpdateUserPresenceStatusResponseActiveCallsItemSipData',
    'UpdateUserPresenceStatusResponseActiveCallsItemTelephonyStatus',
    'UpdateUserPresenceStatusResponseDndStatus',
    'UpdateUserPresenceStatusResponseExtension',
    'UpdateUserPresenceStatusResponseMeetingStatus',
    'UpdateUserPresenceStatusResponsePresenceStatus',
    'UpdateUserPresenceStatusResponseTelephonyStatus',
    'UpdateUserPresenceStatusResponseUserStatus',
    'UpdateUserProfileImageRequest',
    'UpdateUserVideoConfigurationRequest',
    'UpdateUserVideoConfigurationRequestProvider',
    'UpdateUserVideoConfigurationResponse',
    'UpdateUserVideoConfigurationResponseProvider',
    'UpdateWirelessPointRequest',
    'UpdateWirelessPointRequestEmergencyAddress',
    'UpdateWirelessPointRequestEmergencyLocation',
    'UpdateWirelessPointRequestSite',
    'UpdateWirelessPointResponse',
    'UpdateWirelessPointResponseEmergencyAddress',
    'UpdateWirelessPointResponseEmergencyLocation',
    'UpdateWirelessPointResponseSite',
    'User',
    'UserActiveCallsResponse',
    'UserAnsweringRuleList',
    'UserAnsweringRuleListNavigation',
    'UserAnsweringRuleListNavigationFirstPage',
    'UserAnsweringRuleListPaging',
    'UserAnsweringRuleListRecordsItem',
    'UserAnsweringRuleListRecordsItemType',
    'UserBusinessHoursUpdateRequest',
    'UserBusinessHoursUpdateResponse',
    'UserBusinessHoursUpdateResponseSchedule',
    'UserCallLogResponse',
    'UserCallLogResponseNavigation',
    'UserCallLogResponseNavigationFirstPage',
    'UserCallLogResponsePaging',
    'UserCallLogResponseRecordsItem',
    'UserCallLogResponseRecordsItemAction',
    'UserCallLogResponseRecordsItemDirection',
    'UserCallLogResponseRecordsItemExtension',
    'UserCallLogResponseRecordsItemFrom',
    'UserCallLogResponseRecordsItemFromDevice',
    'UserCallLogResponseRecordsItemLegsItem',
    'UserCallLogResponseRecordsItemLegsItemAction',
    'UserCallLogResponseRecordsItemLegsItemBilling',
    'UserCallLogResponseRecordsItemLegsItemDelegate',
    'UserCallLogResponseRecordsItemLegsItemDirection',
    'UserCallLogResponseRecordsItemLegsItemLegType',
    'UserCallLogResponseRecordsItemLegsItemMessage',
    'UserCallLogResponseRecordsItemLegsItemReason',
    'UserCallLogResponseRecordsItemLegsItemRecording',
    'UserCallLogResponseRecordsItemLegsItemRecordingType',
    'UserCallLogResponseRecordsItemLegsItemResult',
    'UserCallLogResponseRecordsItemLegsItemTransport',
    'UserCallLogResponseRecordsItemLegsItemType',
    'UserCallLogResponseRecordsItemReason',
    'UserCallLogResponseRecordsItemResult',
    'UserCallLogResponseRecordsItemTransport',
    'UserCallLogResponseRecordsItemType',
    'UserCallQueues',
    'UserCallQueuesRecordsItem',
    'UserPatch',
    'UserPatchSchemasItem',
    'UserPatch_OperationsItem',
    'UserPatch_OperationsItemOp',
    'UserSchemasItem',
    'UserSearchResponse',
    'UserSearchResponseSchemasItem',
    'UserSearchResponse_ResourcesItem',
    'UserSearchResponse_ResourcesItemAddressesItem',
    'UserSearchResponse_ResourcesItemAddressesItemType',
    'UserSearchResponse_ResourcesItemEmailsItem',
    'UserSearchResponse_ResourcesItemEmailsItemType',
    'UserSearchResponse_ResourcesItemMeta',
    'UserSearchResponse_ResourcesItemMetaResourceType',
    'UserSearchResponse_ResourcesItemName',
    'UserSearchResponse_ResourcesItemPhoneNumbersItem',
    'UserSearchResponse_ResourcesItemPhoneNumbersItemType',
    'UserSearchResponse_ResourcesItemPhotosItem',
    'UserSearchResponse_ResourcesItemPhotosItemType',
    'UserSearchResponse_ResourcesItemSchemasItem',
    'UserSearchResponse_ResourcesItemUrnIetfParamsScimSchemasExtensionEnterprise_2_0_User',
    'UserTemplates',
    'UserTemplatesRecordsItem',
    'UserTemplatesRecordsItemType',
    'UserVideoConfiguration',
    'UserVideoConfigurationProvider',
    'ValidateMultipleSwitchesRequest',
    'ValidateMultipleSwitchesRequest',
    'ValidateMultipleSwitchesRequestRecordsItem',
    'ValidateMultipleSwitchesRequestRecordsItemEmergencyAddress',
    'ValidateMultipleSwitchesRequestRecordsItemEmergencyLocation',
    'ValidateMultipleSwitchesRequestRecordsItemSite',
    'ValidateMultipleSwitchesResponse',
    'ValidateMultipleSwitchesResponse',
    'ValidateMultipleSwitchesResponseRecordsItem',
    'ValidateMultipleSwitchesResponseRecordsItem',
    'ValidateMultipleSwitchesResponseRecordsItemErrorsItem',
    'ValidateMultipleSwitchesResponseRecordsItemStatus',
    'ValidateMultipleSwitchesResponseRecordsItemStatus',
    'ValidateMultipleWirelessPointsRequest',
    'ValidateMultipleWirelessPointsRequest',
    'ValidateMultipleWirelessPointsRequestRecordsItem',
    'ValidateMultipleWirelessPointsRequestRecordsItem',
    'ValidateMultipleWirelessPointsRequestRecordsItemEmergencyAddress',
    'ValidateMultipleWirelessPointsRequestRecordsItemSite',
    'ValidateMultipleWirelessPointsResponse',
    'ValidateMultipleWirelessPointsResponse',
    'ValidateMultipleWirelessPointsResponseRecordsItem',
    'ValidateMultipleWirelessPointsResponseRecordsItem',
    'ValidateMultipleWirelessPointsResponseRecordsItemErrorsItem',
    'ValidateMultipleWirelessPointsResponseRecordsItemErrorsItem',
    'ValidateMultipleWirelessPointsResponseRecordsItemStatus',
    'ValidateMultipleWirelessPointsResponseRecordsItemStatus',
    'WirelessPointInfo',
    'WirelessPointsList',
]
