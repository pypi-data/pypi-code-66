from ._7 import *

class ReadGlipPostResponseMentionsItemType(Enum):
    """ Type of mentions """
    
    Person = 'Person'
    Team = 'Team'
    File = 'File'
    Link = 'Link'
    Event = 'Event'
    Task = 'Task'
    Note = 'Note'
    Card = 'Card'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadGlipPostResponseMentionsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a user """
    
    type: Optional[ReadGlipPostResponseMentionsItemType] = None
    """ Type of mentions """
    
    name: Optional[str] = None
    """ Name of a user """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadGlipPostResponse(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a post """
    
    group_id: Optional[str] = None
    """ Internal identifier of a group a post belongs to """
    
    type: Optional[ReadGlipPostResponseType] = None
    """ Type of a post """
    
    text: Optional[str] = None
    """ For 'TextMessage' post type only. Text of a message """
    
    creator_id: Optional[str] = None
    """ Internal identifier of a user - author of a post """
    
    added_person_ids: Optional[List[str]] = None
    """ For 'PersonsAdded' post type only. Identifiers of persons added to a group """
    
    creation_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """ Post creation datetime in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format """
    
    last_modified_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """ Post last modification datetime in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format """
    
    attachments: Optional[List[ReadGlipPostResponseAttachmentsItem]] = None
    """ List of posted attachments """
    
    mentions: Optional[List[ReadGlipPostResponseMentionsItem]] = None
    activity: Optional[str] = None
    """ Label of activity type """
    
    title: Optional[str] = None
    """ Title of a message. (Can be set for bot's messages only) """
    
    icon_uri: Optional[str] = None
    """ Link to an image used as an icon for this message """
    
    icon_emoji: Optional[str] = None
    """ Emoji used as an icon for this message """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class PatchGlipPostRequest(DataClassJsonMixin):
    text: Optional[str] = None
    """ Post text. """
    

class PatchGlipPostResponseType(Enum):
    """ Type of a post """
    
    TextMessage = 'TextMessage'
    PersonJoined = 'PersonJoined'
    PersonsAdded = 'PersonsAdded'

class PatchGlipPostResponseAttachmentsItemType(Enum):
    """ Type of an attachment """
    
    Card = 'Card'
    Event = 'Event'
    Note = 'Note'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class PatchGlipPostResponseAttachmentsItemAuthor(DataClassJsonMixin):
    """ Information about the author """
    
    name: Optional[str] = None
    """ Name of a message author """
    
    uri: Optional[str] = None
    """ Link to an author's name """
    
    icon_uri: Optional[str] = None
    """ Link to an image displayed to the left of an author's name; sized 82x82px """
    

class PatchGlipPostResponseAttachmentsItemFieldsItemStyle(Enum):
    """ Style of width span applied to a field """
    
    Short = 'Short'
    Long = 'Long'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class PatchGlipPostResponseAttachmentsItemFieldsItem(DataClassJsonMixin):
    title: Optional[str] = None
    """ Title of an individual field """
    
    value: Optional[str] = None
    """ Value of an individual field (supports Markdown) """
    
    style: Optional[PatchGlipPostResponseAttachmentsItemFieldsItemStyle] = 'Short'
    """ Style of width span applied to a field """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class PatchGlipPostResponseAttachmentsItemFootnote(DataClassJsonMixin):
    """ Message Footer """
    
    text: Optional[str] = None
    """ Text of a footer """
    
    icon_uri: Optional[str] = None
    """ Link to an icon displayed to the left of a footer; sized 32x32px """
    
    time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """
    Message creation datetime in ISO 8601 format including timezone, for example
    *2016-03-10T18:07:52.534Z*
    """
    

class PatchGlipPostResponseAttachmentsItemRecurrence(Enum):
    """ Event recurrence settings. """
    
    None_ = 'None'
    Day = 'Day'
    Weekday = 'Weekday'
    Week = 'Week'
    Month = 'Month'
    Year = 'Year'

class PatchGlipPostResponseAttachmentsItemEndingOn(Enum):
    """ Iterations end datetime for periodic events """
    
    None_ = 'None'
    Count = 'Count'
    Date = 'Date'

class PatchGlipPostResponseAttachmentsItemColor(Enum):
    """
    Color of Event title, including its presentation in Calendar; or the color of the side border
    of an interactive message of a Card
    
    Generated by Python OpenAPI Parser
    """
    
    Black = 'Black'
    Red = 'Red'
    Orange = 'Orange'
    Yellow = 'Yellow'
    Green = 'Green'
    Blue = 'Blue'
    Purple = 'Purple'
    Magenta = 'Magenta'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class PatchGlipPostResponseAttachmentsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of an attachment """
    
    type: Optional[PatchGlipPostResponseAttachmentsItemType] = 'Card'
    """ Type of an attachment """
    
    fallback: Optional[str] = None
    """
    A string of default text that will be rendered in the case that the client does not support
    Interactive Messages
    """
    
    intro: Optional[str] = None
    """ A pretext to the message """
    
    author: Optional[PatchGlipPostResponseAttachmentsItemAuthor] = None
    """ Information about the author """
    
    title: Optional[str] = None
    """ Message title """
    
    text: Optional[str] = None
    """
    A large string field (up to 1000 chars) to be displayed as the body of a message (Supports
    GlipDown)
    """
    
    image_uri: Optional[str] = None
    """ Link to an image displayed at the bottom of a message """
    
    thumbnail_uri: Optional[str] = None
    """ Link to an image preview displayed to the right of a message (82x82) """
    
    fields: Optional[List[PatchGlipPostResponseAttachmentsItemFieldsItem]] = None
    """ Information on navigation """
    
    footnote: Optional[PatchGlipPostResponseAttachmentsItemFootnote] = None
    """ Message Footer """
    
    creator_id: Optional[str] = None
    """ Internal identifier of a person created an event """
    
    start_time: Optional[str] = None
    """ Datetime of starting an event """
    
    end_time: Optional[str] = None
    """ Datetime of ending an event """
    
    all_day: Optional[bool] = False
    """ Indicates whether an event has some specific time slot or lasts for the whole day(s) """
    
    recurrence: Optional[PatchGlipPostResponseAttachmentsItemRecurrence] = None
    """ Event recurrence settings. """
    
    ending_condition: Optional[str] = None
    """ Condition of ending """
    
    ending_after: Optional[int] = None
    """ Count of iterations. For periodic events only """
    
    ending_on: Optional[PatchGlipPostResponseAttachmentsItemEndingOn] = 'None'
    """ Iterations end datetime for periodic events """
    
    color: Optional[PatchGlipPostResponseAttachmentsItemColor] = 'Black'
    """
    Color of Event title, including its presentation in Calendar; or the color of the side border
    of an interactive message of a Card
    """
    
    location: Optional[str] = None
    """ Event location """
    
    description: Optional[str] = None
    """ Event details """
    

class PatchGlipPostResponseMentionsItemType(Enum):
    """ Type of mentions """
    
    Person = 'Person'
    Team = 'Team'
    File = 'File'
    Link = 'Link'
    Event = 'Event'
    Task = 'Task'
    Note = 'Note'
    Card = 'Card'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class PatchGlipPostResponseMentionsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a user """
    
    type: Optional[PatchGlipPostResponseMentionsItemType] = None
    """ Type of mentions """
    
    name: Optional[str] = None
    """ Name of a user """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class PatchGlipPostResponse(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a post """
    
    group_id: Optional[str] = None
    """ Internal identifier of a group a post belongs to """
    
    type: Optional[PatchGlipPostResponseType] = None
    """ Type of a post """
    
    text: Optional[str] = None
    """ For 'TextMessage' post type only. Text of a message """
    
    creator_id: Optional[str] = None
    """ Internal identifier of a user - author of a post """
    
    added_person_ids: Optional[List[str]] = None
    """ For 'PersonsAdded' post type only. Identifiers of persons added to a group """
    
    creation_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """ Post creation datetime in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format """
    
    last_modified_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """ Post last modification datetime in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format """
    
    attachments: Optional[List[PatchGlipPostResponseAttachmentsItem]] = None
    """ List of posted attachments """
    
    mentions: Optional[List[PatchGlipPostResponseMentionsItem]] = None
    activity: Optional[str] = None
    """ Label of activity type """
    
    title: Optional[str] = None
    """ Title of a message. (Can be set for bot's messages only) """
    
    icon_uri: Optional[str] = None
    """ Link to an image used as an icon for this message """
    
    icon_emoji: Optional[str] = None
    """ Emoji used as an icon for this message """
    

class ReadGlipPostsResponseRecordsItemType(Enum):
    """ Type of a post """
    
    TextMessage = 'TextMessage'
    PersonJoined = 'PersonJoined'
    PersonsAdded = 'PersonsAdded'

class ReadGlipPostsResponseRecordsItemAttachmentsItemType(Enum):
    """ Type of an attachment """
    
    Card = 'Card'
    Event = 'Event'
    Note = 'Note'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadGlipPostsResponseRecordsItemAttachmentsItemAuthor(DataClassJsonMixin):
    """ Information about the author """
    
    name: Optional[str] = None
    """ Name of a message author """
    
    uri: Optional[str] = None
    """ Link to an author's name """
    
    icon_uri: Optional[str] = None
    """ Link to an image displayed to the left of an author's name; sized 82x82px """
    

class ReadGlipPostsResponseRecordsItemAttachmentsItemFieldsItemStyle(Enum):
    """ Style of width span applied to a field """
    
    Short = 'Short'
    Long = 'Long'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadGlipPostsResponseRecordsItemAttachmentsItemFieldsItem(DataClassJsonMixin):
    title: Optional[str] = None
    """ Title of an individual field """
    
    value: Optional[str] = None
    """ Value of an individual field (supports Markdown) """
    
    style: Optional[ReadGlipPostsResponseRecordsItemAttachmentsItemFieldsItemStyle] = 'Short'
    """ Style of width span applied to a field """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadGlipPostsResponseRecordsItemAttachmentsItemFootnote(DataClassJsonMixin):
    """ Message Footer """
    
    text: Optional[str] = None
    """ Text of a footer """
    
    icon_uri: Optional[str] = None
    """ Link to an icon displayed to the left of a footer; sized 32x32px """
    
    time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """
    Message creation datetime in ISO 8601 format including timezone, for example
    *2016-03-10T18:07:52.534Z*
    """
    

class ReadGlipPostsResponseRecordsItemAttachmentsItemRecurrence(Enum):
    """ Event recurrence settings. """
    
    None_ = 'None'
    Day = 'Day'
    Weekday = 'Weekday'
    Week = 'Week'
    Month = 'Month'
    Year = 'Year'

class ReadGlipPostsResponseRecordsItemAttachmentsItemEndingOn(Enum):
    """ Iterations end datetime for periodic events """
    
    None_ = 'None'
    Count = 'Count'
    Date = 'Date'

class ReadGlipPostsResponseRecordsItemAttachmentsItemColor(Enum):
    """
    Color of Event title, including its presentation in Calendar; or the color of the side border
    of an interactive message of a Card
    
    Generated by Python OpenAPI Parser
    """
    
    Black = 'Black'
    Red = 'Red'
    Orange = 'Orange'
    Yellow = 'Yellow'
    Green = 'Green'
    Blue = 'Blue'
    Purple = 'Purple'
    Magenta = 'Magenta'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadGlipPostsResponseRecordsItemAttachmentsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of an attachment """
    
    type: Optional[ReadGlipPostsResponseRecordsItemAttachmentsItemType] = 'Card'
    """ Type of an attachment """
    
    fallback: Optional[str] = None
    """
    A string of default text that will be rendered in the case that the client does not support
    Interactive Messages
    """
    
    intro: Optional[str] = None
    """ A pretext to the message """
    
    author: Optional[ReadGlipPostsResponseRecordsItemAttachmentsItemAuthor] = None
    """ Information about the author """
    
    title: Optional[str] = None
    """ Message title """
    
    text: Optional[str] = None
    """
    A large string field (up to 1000 chars) to be displayed as the body of a message (Supports
    GlipDown)
    """
    
    image_uri: Optional[str] = None
    """ Link to an image displayed at the bottom of a message """
    
    thumbnail_uri: Optional[str] = None
    """ Link to an image preview displayed to the right of a message (82x82) """
    
    fields: Optional[List[ReadGlipPostsResponseRecordsItemAttachmentsItemFieldsItem]] = None
    """ Information on navigation """
    
    footnote: Optional[ReadGlipPostsResponseRecordsItemAttachmentsItemFootnote] = None
    """ Message Footer """
    
    creator_id: Optional[str] = None
    """ Internal identifier of a person created an event """
    
    start_time: Optional[str] = None
    """ Datetime of starting an event """
    
    end_time: Optional[str] = None
    """ Datetime of ending an event """
    
    all_day: Optional[bool] = False
    """ Indicates whether an event has some specific time slot or lasts for the whole day(s) """
    
    recurrence: Optional[ReadGlipPostsResponseRecordsItemAttachmentsItemRecurrence] = None
    """ Event recurrence settings. """
    
    ending_condition: Optional[str] = None
    """ Condition of ending """
    
    ending_after: Optional[int] = None
    """ Count of iterations. For periodic events only """
    
    ending_on: Optional[ReadGlipPostsResponseRecordsItemAttachmentsItemEndingOn] = 'None'
    """ Iterations end datetime for periodic events """
    
    color: Optional[ReadGlipPostsResponseRecordsItemAttachmentsItemColor] = 'Black'
    """
    Color of Event title, including its presentation in Calendar; or the color of the side border
    of an interactive message of a Card
    """
    
    location: Optional[str] = None
    """ Event location """
    
    description: Optional[str] = None
    """ Event details """
    

class ReadGlipPostsResponseRecordsItemMentionsItemType(Enum):
    """ Type of mentions """
    
    Person = 'Person'
    Team = 'Team'
    File = 'File'
    Link = 'Link'
    Event = 'Event'
    Task = 'Task'
    Note = 'Note'
    Card = 'Card'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadGlipPostsResponseRecordsItemMentionsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a user """
    
    type: Optional[ReadGlipPostsResponseRecordsItemMentionsItemType] = None
    """ Type of mentions """
    
    name: Optional[str] = None
    """ Name of a user """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadGlipPostsResponseRecordsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a post """
    
    group_id: Optional[str] = None
    """ Internal identifier of a group a post belongs to """
    
    type: Optional[ReadGlipPostsResponseRecordsItemType] = None
    """ Type of a post """
    
    text: Optional[str] = None
    """ For 'TextMessage' post type only. Text of a message """
    
    creator_id: Optional[str] = None
    """ Internal identifier of a user - author of a post """
    
    added_person_ids: Optional[List[str]] = None
    """ For 'PersonsAdded' post type only. Identifiers of persons added to a group """
    
    creation_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """ Post creation datetime in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format """
    
    last_modified_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """ Post last modification datetime in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format """
    
    attachments: Optional[List[ReadGlipPostsResponseRecordsItemAttachmentsItem]] = None
    """ List of posted attachments """
    
    mentions: Optional[List[ReadGlipPostsResponseRecordsItemMentionsItem]] = None
    activity: Optional[str] = None
    """ Label of activity type """
    
    title: Optional[str] = None
    """ Title of a message. (Can be set for bot's messages only) """
    
    icon_uri: Optional[str] = None
    """ Link to an image used as an icon for this message """
    
    icon_emoji: Optional[str] = None
    """ Emoji used as an icon for this message """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadGlipPostsResponseNavigation(DataClassJsonMixin):
    prev_page_token: Optional[str] = None
    """
    Previous page token. To get previous page, user should pass one of returned token in next
    request and, in turn, required page will be returned with new tokens
    """
    
    next_page_token: Optional[str] = None
    """
    Next page token. To get next page, user should pass one of returned token in next request and,
    in turn, required page will be returned with new tokens
    """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadGlipPostsResponse(DataClassJsonMixin):
    """
    Required Properties:
     - records
    
    Generated by Python OpenAPI Parser
    """
    
    records: List[ReadGlipPostsResponseRecordsItem]
    """ List of posts """
    
    navigation: Optional[ReadGlipPostsResponseNavigation] = None

class CreateGlipPostRequestAttachmentsItemType(Enum):
    """ Type of an attachment """
    
    Event = 'Event'
    File = 'File'
    Note = 'Note'
    Task = 'Task'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateGlipPostRequestAttachmentsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of an attachment """
    
    type: Optional[CreateGlipPostRequestAttachmentsItemType] = None
    """ Type of an attachment """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateGlipPostRequest(DataClassJsonMixin):
    """
    Required Properties:
     - text
    
    Generated by Python OpenAPI Parser
    """
    
    text: str
    """ Post text. """
    
    attachments: Optional[List[CreateGlipPostRequestAttachmentsItem]] = None
    """ Identifier(s) of attachments. """
    

class CreateGlipPostResponseType(Enum):
    """ Type of a post """
    
    TextMessage = 'TextMessage'
    PersonJoined = 'PersonJoined'
    PersonsAdded = 'PersonsAdded'

class CreateGlipPostResponseAttachmentsItemType(Enum):
    """ Type of an attachment """
    
    Card = 'Card'
    Event = 'Event'
    Note = 'Note'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateGlipPostResponseAttachmentsItemAuthor(DataClassJsonMixin):
    """ Information about the author """
    
    name: Optional[str] = None
    """ Name of a message author """
    
    uri: Optional[str] = None
    """ Link to an author's name """
    
    icon_uri: Optional[str] = None
    """ Link to an image displayed to the left of an author's name; sized 82x82px """
    

class CreateGlipPostResponseAttachmentsItemFieldsItemStyle(Enum):
    """ Style of width span applied to a field """
    
    Short = 'Short'
    Long = 'Long'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateGlipPostResponseAttachmentsItemFieldsItem(DataClassJsonMixin):
    title: Optional[str] = None
    """ Title of an individual field """
    
    value: Optional[str] = None
    """ Value of an individual field (supports Markdown) """
    
    style: Optional[CreateGlipPostResponseAttachmentsItemFieldsItemStyle] = 'Short'
    """ Style of width span applied to a field """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateGlipPostResponseAttachmentsItemFootnote(DataClassJsonMixin):
    """ Message Footer """
    
    text: Optional[str] = None
    """ Text of a footer """
    
    icon_uri: Optional[str] = None
    """ Link to an icon displayed to the left of a footer; sized 32x32px """
    
    time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """
    Message creation datetime in ISO 8601 format including timezone, for example
    *2016-03-10T18:07:52.534Z*
    """
    

class CreateGlipPostResponseAttachmentsItemRecurrence(Enum):
    """ Event recurrence settings. """
    
    None_ = 'None'
    Day = 'Day'
    Weekday = 'Weekday'
    Week = 'Week'
    Month = 'Month'
    Year = 'Year'

class CreateGlipPostResponseAttachmentsItemEndingOn(Enum):
    """ Iterations end datetime for periodic events """
    
    None_ = 'None'
    Count = 'Count'
    Date = 'Date'

class CreateGlipPostResponseAttachmentsItemColor(Enum):
    """
    Color of Event title, including its presentation in Calendar; or the color of the side border
    of an interactive message of a Card
    
    Generated by Python OpenAPI Parser
    """
    
    Black = 'Black'
    Red = 'Red'
    Orange = 'Orange'
    Yellow = 'Yellow'
    Green = 'Green'
    Blue = 'Blue'
    Purple = 'Purple'
    Magenta = 'Magenta'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateGlipPostResponseAttachmentsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of an attachment """
    
    type: Optional[CreateGlipPostResponseAttachmentsItemType] = 'Card'
    """ Type of an attachment """
    
    fallback: Optional[str] = None
    """
    A string of default text that will be rendered in the case that the client does not support
    Interactive Messages
    """
    
    intro: Optional[str] = None
    """ A pretext to the message """
    
    author: Optional[CreateGlipPostResponseAttachmentsItemAuthor] = None
    """ Information about the author """
    
    title: Optional[str] = None
    """ Message title """
    
    text: Optional[str] = None
    """
    A large string field (up to 1000 chars) to be displayed as the body of a message (Supports
    GlipDown)
    """
    
    image_uri: Optional[str] = None
    """ Link to an image displayed at the bottom of a message """
    
    thumbnail_uri: Optional[str] = None
    """ Link to an image preview displayed to the right of a message (82x82) """
    
    fields: Optional[List[CreateGlipPostResponseAttachmentsItemFieldsItem]] = None
    """ Information on navigation """
    
    footnote: Optional[CreateGlipPostResponseAttachmentsItemFootnote] = None
    """ Message Footer """
    
    creator_id: Optional[str] = None
    """ Internal identifier of a person created an event """
    
    start_time: Optional[str] = None
    """ Datetime of starting an event """
    
    end_time: Optional[str] = None
    """ Datetime of ending an event """
    
    all_day: Optional[bool] = False
    """ Indicates whether an event has some specific time slot or lasts for the whole day(s) """
    
    recurrence: Optional[CreateGlipPostResponseAttachmentsItemRecurrence] = None
    """ Event recurrence settings. """
    
    ending_condition: Optional[str] = None
    """ Condition of ending """
    
    ending_after: Optional[int] = None
    """ Count of iterations. For periodic events only """
    
    ending_on: Optional[CreateGlipPostResponseAttachmentsItemEndingOn] = 'None'
    """ Iterations end datetime for periodic events """
    
    color: Optional[CreateGlipPostResponseAttachmentsItemColor] = 'Black'
    """
    Color of Event title, including its presentation in Calendar; or the color of the side border
    of an interactive message of a Card
    """
    
    location: Optional[str] = None
    """ Event location """
    
    description: Optional[str] = None
    """ Event details """
    

class CreateGlipPostResponseMentionsItemType(Enum):
    """ Type of mentions """
    
    Person = 'Person'
    Team = 'Team'
    File = 'File'
    Link = 'Link'
    Event = 'Event'
    Task = 'Task'
    Note = 'Note'
    Card = 'Card'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateGlipPostResponseMentionsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a user """
    
    type: Optional[CreateGlipPostResponseMentionsItemType] = None
    """ Type of mentions """
    
    name: Optional[str] = None
    """ Name of a user """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateGlipPostResponse(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a post """
    
    group_id: Optional[str] = None
    """ Internal identifier of a group a post belongs to """
    
    type: Optional[CreateGlipPostResponseType] = None
    """ Type of a post """
    
    text: Optional[str] = None
    """ For 'TextMessage' post type only. Text of a message """
    
    creator_id: Optional[str] = None
    """ Internal identifier of a user - author of a post """
    
    added_person_ids: Optional[List[str]] = None
    """ For 'PersonsAdded' post type only. Identifiers of persons added to a group """
    
    creation_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """ Post creation datetime in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format """
    
    last_modified_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """ Post last modification datetime in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format """
    
    attachments: Optional[List[CreateGlipPostResponseAttachmentsItem]] = None
    """ List of posted attachments """
    
    mentions: Optional[List[CreateGlipPostResponseMentionsItem]] = None
    activity: Optional[str] = None
    """ Label of activity type """
    
    title: Optional[str] = None
    """ Title of a message. (Can be set for bot's messages only) """
    
    icon_uri: Optional[str] = None
    """ Link to an image used as an icon for this message """
    
    icon_emoji: Optional[str] = None
    """ Emoji used as an icon for this message """
    

class ListGlipGroupPostsResponseRecordsItemType(Enum):
    """ Type of a post """
    
    TextMessage = 'TextMessage'
    PersonJoined = 'PersonJoined'
    PersonsAdded = 'PersonsAdded'

class ListGlipGroupPostsResponseRecordsItemAttachmentsItemType(Enum):
    """ Type of an attachment """
    
    Card = 'Card'
    Event = 'Event'
    Note = 'Note'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListGlipGroupPostsResponseRecordsItemAttachmentsItemAuthor(DataClassJsonMixin):
    """ Information about the author """
    
    name: Optional[str] = None
    """ Name of a message author """
    
    uri: Optional[str] = None
    """ Link to an author's name """
    
    icon_uri: Optional[str] = None
    """ Link to an image displayed to the left of an author's name; sized 82x82px """
    

class ListGlipGroupPostsResponseRecordsItemAttachmentsItemFieldsItemStyle(Enum):
    """ Style of width span applied to a field """
    
    Short = 'Short'
    Long = 'Long'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListGlipGroupPostsResponseRecordsItemAttachmentsItemFieldsItem(DataClassJsonMixin):
    title: Optional[str] = None
    """ Title of an individual field """
    
    value: Optional[str] = None
    """ Value of an individual field (supports Markdown) """
    
    style: Optional[ListGlipGroupPostsResponseRecordsItemAttachmentsItemFieldsItemStyle] = 'Short'
    """ Style of width span applied to a field """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListGlipGroupPostsResponseRecordsItemAttachmentsItemFootnote(DataClassJsonMixin):
    """ Message Footer """
    
    text: Optional[str] = None
    """ Text of a footer """
    
    icon_uri: Optional[str] = None
    """ Link to an icon displayed to the left of a footer; sized 32x32px """
    
    time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """
    Message creation datetime in ISO 8601 format including timezone, for example
    *2016-03-10T18:07:52.534Z*
    """
    

class ListGlipGroupPostsResponseRecordsItemAttachmentsItemRecurrence(Enum):
    """ Event recurrence settings. """
    
    None_ = 'None'
    Day = 'Day'
    Weekday = 'Weekday'
    Week = 'Week'
    Month = 'Month'
    Year = 'Year'

class ListGlipGroupPostsResponseRecordsItemAttachmentsItemEndingOn(Enum):
    """ Iterations end datetime for periodic events """
    
    None_ = 'None'
    Count = 'Count'
    Date = 'Date'

class ListGlipGroupPostsResponseRecordsItemAttachmentsItemColor(Enum):
    """
    Color of Event title, including its presentation in Calendar; or the color of the side border
    of an interactive message of a Card
    
    Generated by Python OpenAPI Parser
    """
    
    Black = 'Black'
    Red = 'Red'
    Orange = 'Orange'
    Yellow = 'Yellow'
    Green = 'Green'
    Blue = 'Blue'
    Purple = 'Purple'
    Magenta = 'Magenta'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListGlipGroupPostsResponseRecordsItemAttachmentsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of an attachment """
    
    type: Optional[ListGlipGroupPostsResponseRecordsItemAttachmentsItemType] = 'Card'
    """ Type of an attachment """
    
    fallback: Optional[str] = None
    """
    A string of default text that will be rendered in the case that the client does not support
    Interactive Messages
    """
    
    intro: Optional[str] = None
    """ A pretext to the message """
    
    author: Optional[ListGlipGroupPostsResponseRecordsItemAttachmentsItemAuthor] = None
    """ Information about the author """
    
    title: Optional[str] = None
    """ Message title """
    
    text: Optional[str] = None
    """
    A large string field (up to 1000 chars) to be displayed as the body of a message (Supports
    GlipDown)
    """
    
    image_uri: Optional[str] = None
    """ Link to an image displayed at the bottom of a message """
    
    thumbnail_uri: Optional[str] = None
    """ Link to an image preview displayed to the right of a message (82x82) """
    
    fields: Optional[List[ListGlipGroupPostsResponseRecordsItemAttachmentsItemFieldsItem]] = None
    """ Information on navigation """
    
    footnote: Optional[ListGlipGroupPostsResponseRecordsItemAttachmentsItemFootnote] = None
    """ Message Footer """
    
    creator_id: Optional[str] = None
    """ Internal identifier of a person created an event """
    
    start_time: Optional[str] = None
    """ Datetime of starting an event """
    
    end_time: Optional[str] = None
    """ Datetime of ending an event """
    
    all_day: Optional[bool] = False
    """ Indicates whether an event has some specific time slot or lasts for the whole day(s) """
    
    recurrence: Optional[ListGlipGroupPostsResponseRecordsItemAttachmentsItemRecurrence] = None
    """ Event recurrence settings. """
    
    ending_condition: Optional[str] = None
    """ Condition of ending """
    
    ending_after: Optional[int] = None
    """ Count of iterations. For periodic events only """
    
    ending_on: Optional[ListGlipGroupPostsResponseRecordsItemAttachmentsItemEndingOn] = 'None'
    """ Iterations end datetime for periodic events """
    
    color: Optional[ListGlipGroupPostsResponseRecordsItemAttachmentsItemColor] = 'Black'
    """
    Color of Event title, including its presentation in Calendar; or the color of the side border
    of an interactive message of a Card
    """
    
    location: Optional[str] = None
    """ Event location """
    
    description: Optional[str] = None
    """ Event details """
    

class ListGlipGroupPostsResponseRecordsItemMentionsItemType(Enum):
    """ Type of mentions """
    
    Person = 'Person'
    Team = 'Team'
    File = 'File'
    Link = 'Link'
    Event = 'Event'
    Task = 'Task'
    Note = 'Note'
    Card = 'Card'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListGlipGroupPostsResponseRecordsItemMentionsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a user """
    
    type: Optional[ListGlipGroupPostsResponseRecordsItemMentionsItemType] = None
    """ Type of mentions """
    
    name: Optional[str] = None
    """ Name of a user """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListGlipGroupPostsResponseRecordsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a post """
    
    group_id: Optional[str] = None
    """ Internal identifier of a group a post belongs to """
    
    type: Optional[ListGlipGroupPostsResponseRecordsItemType] = None
    """ Type of a post """
    
    text: Optional[str] = None
    """ For 'TextMessage' post type only. Text of a message """
    
    creator_id: Optional[str] = None
    """ Internal identifier of a user - author of a post """
    
    added_person_ids: Optional[List[str]] = None
    """ For 'PersonsAdded' post type only. Identifiers of persons added to a group """
    
    creation_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """ Post creation datetime in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format """
    
    last_modified_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """ Post last modification datetime in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format """
    
    attachments: Optional[List[ListGlipGroupPostsResponseRecordsItemAttachmentsItem]] = None
    """ List of posted attachments """
    
    mentions: Optional[List[ListGlipGroupPostsResponseRecordsItemMentionsItem]] = None
    activity: Optional[str] = None
    """ Label of activity type """
    
    title: Optional[str] = None
    """ Title of a message. (Can be set for bot's messages only) """
    
    icon_uri: Optional[str] = None
    """ Link to an image used as an icon for this message """
    
    icon_emoji: Optional[str] = None
    """ Emoji used as an icon for this message """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListGlipGroupPostsResponseNavigation(DataClassJsonMixin):
    prev_page_token: Optional[str] = None
    """
    Previous page token. To get previous page, user should pass one of returned token in next
    request and, in turn, required page will be returned with new tokens
    """
    
    next_page_token: Optional[str] = None
    """
    Next page token. To get next page, user should pass one of returned token in next request and,
    in turn, required page will be returned with new tokens
    """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListGlipGroupPostsResponse(DataClassJsonMixin):
    """
    Required Properties:
     - records
    
    Generated by Python OpenAPI Parser
    """
    
    records: List[ListGlipGroupPostsResponseRecordsItem]
    """ List of posts """
    
    navigation: Optional[ListGlipGroupPostsResponseNavigation] = None

class CreateGlipGroupPostRequestAttachmentsItemType(Enum):
    """ Type of attachment """
    
    Card = 'Card'
    Event = 'Event'
    Note = 'Note'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateGlipGroupPostRequestAttachmentsItemAuthor(DataClassJsonMixin):
    """ Information about the author """
    
    name: Optional[str] = None
    """ Name of a message author """
    
    uri: Optional[str] = None
    """ Link to an author's name """
    
    icon_uri: Optional[str] = None
    """ Link to an image displayed to the left of an author's name; sized 82x82px """
    

class CreateGlipGroupPostRequestAttachmentsItemFieldsItemStyle(Enum):
    """ Style of width span applied to a field """
    
    Short = 'Short'
    Long = 'Long'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateGlipGroupPostRequestAttachmentsItemFieldsItem(DataClassJsonMixin):
    title: Optional[str] = None
    """ Title of an individual field """
    
    value: Optional[str] = None
    """ Value of an individual field (supports Markdown) """
    
    style: Optional[CreateGlipGroupPostRequestAttachmentsItemFieldsItemStyle] = 'Short'
    """ Style of width span applied to a field """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateGlipGroupPostRequestAttachmentsItemFootnote(DataClassJsonMixin):
    """ Message footer information """
    
    text: Optional[str] = None
    """ Text of a footer """
    
    icon_uri: Optional[str] = None
    """ Link to an icon displayed to the left of a footer; sized 32x32px """
    
    time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """
    Message creation datetime in ISO 8601 format including timezone, for example
    *2016-03-10T18:07:52.534Z*
    """
    

class CreateGlipGroupPostRequestAttachmentsItemRecurrence(Enum):
    """
    Event recurrence settings. For non-periodic events the value is 'None'. Must be greater or
    equal to event duration: 1- Day/Weekday; 7 - Week; 28 - Month; 365 - Year
    
    Generated by Python OpenAPI Parser
    """
    
    None_ = 'None'
    Day = 'Day'
    Weekday = 'Weekday'
    Week = 'Week'
    Month = 'Month'
    Year = 'Year'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateGlipGroupPostRequestAttachmentsItem(DataClassJsonMixin):
    type: Optional[CreateGlipGroupPostRequestAttachmentsItemType] = 'Card'
    """ Type of attachment """
    
    title: Optional[str] = None
    """ Attachment title """
    
    fallback: Optional[str] = None
    """ Default message returned in case the client does not support interactive messages """
    
    color: Optional[str] = None
    """
    Color of Event title, including its presentation in Calendar; or the color of the side border
    of an interactive message of a Card. The default color is 'Black'
    """
    
    intro: Optional[str] = None
    """ Introductory text displayed directly above a message """
    
    author: Optional[CreateGlipGroupPostRequestAttachmentsItemAuthor] = None
    """ Information about the author """
    
    text: Optional[str] = None
    """ Text of attachment (up to 1000 chars), supports GlipDown """
    
    image_uri: Optional[str] = None
    """ Link to an image displayed at the bottom of a message """
    
    thumbnail_uri: Optional[str] = None
    """ Link to an image preview displayed to the right of a message (82x82) """
    
    fields: Optional[List[CreateGlipGroupPostRequestAttachmentsItemFieldsItem]] = None
    """ Individual subsections within a message """
    
    footnote: Optional[CreateGlipGroupPostRequestAttachmentsItemFootnote] = None
    """ Message footer information """
    
    start_time: Optional[str] = None
    """ Datetime of starting an event """
    
    end_time: Optional[str] = None
    """ Datetime of ending an event """
    
    all_day: Optional[bool] = False
    """ Indicates whether an event has some specific time slot or lasts for the whole day(s) """
    
    recurrence: Optional[CreateGlipGroupPostRequestAttachmentsItemRecurrence] = None
    """
    Event recurrence settings. For non-periodic events the value is 'None'. Must be greater or
    equal to event duration: 1- Day/Weekday; 7 - Week; 28 - Month; 365 - Year
    """
    
    ending_condition: Optional[str] = None
    """ Condition of ending an event """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateGlipGroupPostRequest(DataClassJsonMixin):
    activity: Optional[str] = None
    title: Optional[str] = None
    """ Title of a message. (Can be set for bot's messages only). """
    
    text: Optional[str] = None
    """ Text of a post """
    
    group_id: Optional[str] = None
    """ Internal identifier of a group """
    
    attachments: Optional[List[CreateGlipGroupPostRequestAttachmentsItem]] = None
    """ List of attachments to be posted """
    
    person_ids: Optional[List[str]] = None
    system: Optional[bool] = None

class CreateGlipGroupPostResponseType(Enum):
    """ Type of a post """
    
    TextMessage = 'TextMessage'
    PersonJoined = 'PersonJoined'
    PersonsAdded = 'PersonsAdded'

class CreateGlipGroupPostResponseAttachmentsItemType(Enum):
    """ Type of an attachment """
    
    Card = 'Card'
    Event = 'Event'
    Note = 'Note'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateGlipGroupPostResponseAttachmentsItemAuthor(DataClassJsonMixin):
    """ Information about the author """
    
    name: Optional[str] = None
    """ Name of a message author """
    
    uri: Optional[str] = None
    """ Link to an author's name """
    
    icon_uri: Optional[str] = None
    """ Link to an image displayed to the left of an author's name; sized 82x82px """
    

class CreateGlipGroupPostResponseAttachmentsItemFieldsItemStyle(Enum):
    """ Style of width span applied to a field """
    
    Short = 'Short'
    Long = 'Long'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateGlipGroupPostResponseAttachmentsItemFieldsItem(DataClassJsonMixin):
    title: Optional[str] = None
    """ Title of an individual field """
    
    value: Optional[str] = None
    """ Value of an individual field (supports Markdown) """
    
    style: Optional[CreateGlipGroupPostResponseAttachmentsItemFieldsItemStyle] = 'Short'
    """ Style of width span applied to a field """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateGlipGroupPostResponseAttachmentsItemFootnote(DataClassJsonMixin):
    """ Message Footer """
    
    text: Optional[str] = None
    """ Text of a footer """
    
    icon_uri: Optional[str] = None
    """ Link to an icon displayed to the left of a footer; sized 32x32px """
    
    time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """
    Message creation datetime in ISO 8601 format including timezone, for example
    *2016-03-10T18:07:52.534Z*
    """
    

class CreateGlipGroupPostResponseAttachmentsItemRecurrence(Enum):
    """ Event recurrence settings. """
    
    None_ = 'None'
    Day = 'Day'
    Weekday = 'Weekday'
    Week = 'Week'
    Month = 'Month'
    Year = 'Year'

class CreateGlipGroupPostResponseAttachmentsItemEndingOn(Enum):
    """ Iterations end datetime for periodic events """
    
    None_ = 'None'
    Count = 'Count'
    Date = 'Date'

class CreateGlipGroupPostResponseAttachmentsItemColor(Enum):
    """
    Color of Event title, including its presentation in Calendar; or the color of the side border
    of an interactive message of a Card
    
    Generated by Python OpenAPI Parser
    """
    
    Black = 'Black'
    Red = 'Red'
    Orange = 'Orange'
    Yellow = 'Yellow'
    Green = 'Green'
    Blue = 'Blue'
    Purple = 'Purple'
    Magenta = 'Magenta'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateGlipGroupPostResponseAttachmentsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of an attachment """
    
    type: Optional[CreateGlipGroupPostResponseAttachmentsItemType] = 'Card'
    """ Type of an attachment """
    
    fallback: Optional[str] = None
    """
    A string of default text that will be rendered in the case that the client does not support
    Interactive Messages
    """
    
    intro: Optional[str] = None
    """ A pretext to the message """
    
    author: Optional[CreateGlipGroupPostResponseAttachmentsItemAuthor] = None
    """ Information about the author """
    
    title: Optional[str] = None
    """ Message title """
    
    text: Optional[str] = None
    """
    A large string field (up to 1000 chars) to be displayed as the body of a message (Supports
    GlipDown)
    """
    
    image_uri: Optional[str] = None
    """ Link to an image displayed at the bottom of a message """
    
    thumbnail_uri: Optional[str] = None
    """ Link to an image preview displayed to the right of a message (82x82) """
    
    fields: Optional[List[CreateGlipGroupPostResponseAttachmentsItemFieldsItem]] = None
    """ Information on navigation """
    
    footnote: Optional[CreateGlipGroupPostResponseAttachmentsItemFootnote] = None
    """ Message Footer """
    
    creator_id: Optional[str] = None
    """ Internal identifier of a person created an event """
    
    start_time: Optional[str] = None
    """ Datetime of starting an event """
    
    end_time: Optional[str] = None
    """ Datetime of ending an event """
    
    all_day: Optional[bool] = False
    """ Indicates whether an event has some specific time slot or lasts for the whole day(s) """
    
    recurrence: Optional[CreateGlipGroupPostResponseAttachmentsItemRecurrence] = None
    """ Event recurrence settings. """
    
    ending_condition: Optional[str] = None
    """ Condition of ending """
    
    ending_after: Optional[int] = None
    """ Count of iterations. For periodic events only """
    
    ending_on: Optional[CreateGlipGroupPostResponseAttachmentsItemEndingOn] = 'None'
    """ Iterations end datetime for periodic events """
    
    color: Optional[CreateGlipGroupPostResponseAttachmentsItemColor] = 'Black'
    """
    Color of Event title, including its presentation in Calendar; or the color of the side border
    of an interactive message of a Card
    """
    
    location: Optional[str] = None
    """ Event location """
    
    description: Optional[str] = None
    """ Event details """
    

class CreateGlipGroupPostResponseMentionsItemType(Enum):
    """ Type of mentions """
    
    Person = 'Person'
    Team = 'Team'
    File = 'File'
    Link = 'Link'
    Event = 'Event'
    Task = 'Task'
    Note = 'Note'
    Card = 'Card'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateGlipGroupPostResponseMentionsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a user """
    
    type: Optional[CreateGlipGroupPostResponseMentionsItemType] = None
    """ Type of mentions """
    
    name: Optional[str] = None
    """ Name of a user """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateGlipGroupPostResponse(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a post """
    
    group_id: Optional[str] = None
    """ Internal identifier of a group a post belongs to """
    
    type: Optional[CreateGlipGroupPostResponseType] = None
    """ Type of a post """
    
    text: Optional[str] = None
    """ For 'TextMessage' post type only. Text of a message """
    
    creator_id: Optional[str] = None
    """ Internal identifier of a user - author of a post """
    
    added_person_ids: Optional[List[str]] = None
    """ For 'PersonsAdded' post type only. Identifiers of persons added to a group """
    
    creation_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """ Post creation datetime in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format """
    
    last_modified_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """ Post last modification datetime in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format """
    
    attachments: Optional[List[CreateGlipGroupPostResponseAttachmentsItem]] = None
    """ List of posted attachments """
    
    mentions: Optional[List[CreateGlipGroupPostResponseMentionsItem]] = None
    activity: Optional[str] = None
    """ Label of activity type """
    
    title: Optional[str] = None
    """ Title of a message. (Can be set for bot's messages only) """
    
    icon_uri: Optional[str] = None
    """ Link to an image used as an icon for this message """
    
    icon_emoji: Optional[str] = None
    """ Emoji used as an icon for this message """
    

class CreateGlipCardRequestType(Enum):
    """ Type of attachment """
    
    Card = 'Card'
    Event = 'Event'
    Note = 'Note'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateGlipCardRequestAuthor(DataClassJsonMixin):
    """ Information about the author """
    
    name: Optional[str] = None
    """ Name of a message author """
    
    uri: Optional[str] = None
    """ Link to an author's name """
    
    icon_uri: Optional[str] = None
    """ Link to an image displayed to the left of an author's name; sized 82x82px """
    

class CreateGlipCardRequestFieldsItemStyle(Enum):
    """ Style of width span applied to a field """
    
    Short = 'Short'
    Long = 'Long'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateGlipCardRequestFieldsItem(DataClassJsonMixin):
    title: Optional[str] = None
    """ Title of an individual field """
    
    value: Optional[str] = None
    """ Value of an individual field (supports Markdown) """
    
    style: Optional[CreateGlipCardRequestFieldsItemStyle] = 'Short'
    """ Style of width span applied to a field """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateGlipCardRequestFootnote(DataClassJsonMixin):
    """ Message footer information """
    
    text: Optional[str] = None
    """ Text of a footer """
    
    icon_uri: Optional[str] = None
    """ Link to an icon displayed to the left of a footer; sized 32x32px """
    
    time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """
    Message creation datetime in ISO 8601 format including timezone, for example
    *2016-03-10T18:07:52.534Z*
    """
    

class CreateGlipCardRequestRecurrence(Enum):
    """
    Event recurrence settings. For non-periodic events the value is 'None'. Must be greater or
    equal to event duration: 1- Day/Weekday; 7 - Week; 28 - Month; 365 - Year
    
    Generated by Python OpenAPI Parser
    """
    
    None_ = 'None'
    Day = 'Day'
    Weekday = 'Weekday'
    Week = 'Week'
    Month = 'Month'
    Year = 'Year'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateGlipCardRequest(DataClassJsonMixin):
    type: Optional[CreateGlipCardRequestType] = 'Card'
    """ Type of attachment """
    
    title: Optional[str] = None
    """ Attachment title """
    
    fallback: Optional[str] = None
    """ Default message returned in case the client does not support interactive messages """
    
    color: Optional[str] = None
    """
    Color of Event title, including its presentation in Calendar; or the color of the side border
    of an interactive message of a Card. The default color is 'Black'
    """
    
    intro: Optional[str] = None
    """ Introductory text displayed directly above a message """
    
    author: Optional[CreateGlipCardRequestAuthor] = None
    """ Information about the author """
    
    text: Optional[str] = None
    """ Text of attachment (up to 1000 chars), supports GlipDown """
    
    image_uri: Optional[str] = None
    """ Link to an image displayed at the bottom of a message """
    
    thumbnail_uri: Optional[str] = None
    """ Link to an image preview displayed to the right of a message (82x82) """
    
    fields: Optional[List[CreateGlipCardRequestFieldsItem]] = None
    """ Individual subsections within a message """
    
    footnote: Optional[CreateGlipCardRequestFootnote] = None
    """ Message footer information """
    
    start_time: Optional[str] = None
    """ Datetime of starting an event """
    
    end_time: Optional[str] = None
    """ Datetime of ending an event """
    
    all_day: Optional[bool] = False
    """ Indicates whether an event has some specific time slot or lasts for the whole day(s) """
    
    recurrence: Optional[CreateGlipCardRequestRecurrence] = None
    """
    Event recurrence settings. For non-periodic events the value is 'None'. Must be greater or
    equal to event duration: 1- Day/Weekday; 7 - Week; 28 - Month; 365 - Year
    """
    
    ending_condition: Optional[str] = None
    """ Condition of ending an event """
    

class CreateGlipCardResponseType(Enum):
    """ Type of an attachment """
    
    Card = 'Card'
    Event = 'Event'
    Note = 'Note'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateGlipCardResponseAuthor(DataClassJsonMixin):
    """ Information about the author """
    
    name: Optional[str] = None
    """ Name of a message author """
    
    uri: Optional[str] = None
    """ Link to an author's name """
    
    icon_uri: Optional[str] = None
    """ Link to an image displayed to the left of an author's name; sized 82x82px """
    

class CreateGlipCardResponseFieldsItemStyle(Enum):
    """ Style of width span applied to a field """
    
    Short = 'Short'
    Long = 'Long'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateGlipCardResponseFieldsItem(DataClassJsonMixin):
    title: Optional[str] = None
    """ Title of an individual field """
    
    value: Optional[str] = None
    """ Value of an individual field (supports Markdown) """
    
    style: Optional[CreateGlipCardResponseFieldsItemStyle] = 'Short'
    """ Style of width span applied to a field """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateGlipCardResponseFootnote(DataClassJsonMixin):
    """ Message Footer """
    
    text: Optional[str] = None
    """ Text of a footer """
    
    icon_uri: Optional[str] = None
    """ Link to an icon displayed to the left of a footer; sized 32x32px """
    
    time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """
    Message creation datetime in ISO 8601 format including timezone, for example
    *2016-03-10T18:07:52.534Z*
    """
    

class CreateGlipCardResponseRecurrence(Enum):
    """ Event recurrence settings. """
    
    None_ = 'None'
    Day = 'Day'
    Weekday = 'Weekday'
    Week = 'Week'
    Month = 'Month'
    Year = 'Year'

class CreateGlipCardResponseEndingOn(Enum):
    """ Iterations end datetime for periodic events """
    
    None_ = 'None'
    Count = 'Count'
    Date = 'Date'

class CreateGlipCardResponseColor(Enum):
    """
    Color of Event title, including its presentation in Calendar; or the color of the side border
    of an interactive message of a Card
    
    Generated by Python OpenAPI Parser
    """
    
    Black = 'Black'
    Red = 'Red'
    Orange = 'Orange'
    Yellow = 'Yellow'
    Green = 'Green'
    Blue = 'Blue'
    Purple = 'Purple'
    Magenta = 'Magenta'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateGlipCardResponse(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of an attachment """
    
    type: Optional[CreateGlipCardResponseType] = 'Card'
    """ Type of an attachment """
    
    fallback: Optional[str] = None
    """
    A string of default text that will be rendered in the case that the client does not support
    Interactive Messages
    """
    
    intro: Optional[str] = None
    """ A pretext to the message """
    
    author: Optional[CreateGlipCardResponseAuthor] = None
    """ Information about the author """
    
    title: Optional[str] = None
    """ Message title """
    
    text: Optional[str] = None
    """
    A large string field (up to 1000 chars) to be displayed as the body of a message (Supports
    GlipDown)
    """
    
    image_uri: Optional[str] = None
    """ Link to an image displayed at the bottom of a message """
    
    thumbnail_uri: Optional[str] = None
    """ Link to an image preview displayed to the right of a message (82x82) """
    
    fields: Optional[List[CreateGlipCardResponseFieldsItem]] = None
    """ Information on navigation """
    
    footnote: Optional[CreateGlipCardResponseFootnote] = None
    """ Message Footer """
    
    creator_id: Optional[str] = None
    """ Internal identifier of a person created an event """
    
    start_time: Optional[str] = None
    """ Datetime of starting an event """
    
    end_time: Optional[str] = None
    """ Datetime of ending an event """
    
    all_day: Optional[bool] = False
    """ Indicates whether an event has some specific time slot or lasts for the whole day(s) """
    
    recurrence: Optional[CreateGlipCardResponseRecurrence] = None
    """ Event recurrence settings. """
    
    ending_condition: Optional[str] = None
    """ Condition of ending """
    
    ending_after: Optional[int] = None
    """ Count of iterations. For periodic events only """
    
    ending_on: Optional[CreateGlipCardResponseEndingOn] = 'None'
    """ Iterations end datetime for periodic events """
    
    color: Optional[CreateGlipCardResponseColor] = 'Black'
    """
    Color of Event title, including its presentation in Calendar; or the color of the side border
    of an interactive message of a Card
    """
    
    location: Optional[str] = None
    """ Event location """
    
    description: Optional[str] = None
    """ Event details """
    

class ReadGlipCardResponseType(Enum):
    """ Type of an attachment """
    
    Card = 'Card'
    Event = 'Event'
    Note = 'Note'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadGlipCardResponseAuthor(DataClassJsonMixin):
    """ Information about the author """
    
    name: Optional[str] = None
    """ Name of a message author """
    
    uri: Optional[str] = None
    """ Link to an author's name """
    
    icon_uri: Optional[str] = None
    """ Link to an image displayed to the left of an author's name; sized 82x82px """
    

class ReadGlipCardResponseFieldsItemStyle(Enum):
    """ Style of width span applied to a field """
    
    Short = 'Short'
    Long = 'Long'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadGlipCardResponseFieldsItem(DataClassJsonMixin):
    title: Optional[str] = None
    """ Title of an individual field """
    
    value: Optional[str] = None
    """ Value of an individual field (supports Markdown) """
    
    style: Optional[ReadGlipCardResponseFieldsItemStyle] = 'Short'
    """ Style of width span applied to a field """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadGlipCardResponseFootnote(DataClassJsonMixin):
    """ Message Footer """
    
    text: Optional[str] = None
    """ Text of a footer """
    
    icon_uri: Optional[str] = None
    """ Link to an icon displayed to the left of a footer; sized 32x32px """
    
    time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """
    Message creation datetime in ISO 8601 format including timezone, for example
    *2016-03-10T18:07:52.534Z*
    """
    

class ReadGlipCardResponseRecurrence(Enum):
    """ Event recurrence settings. """
    
    None_ = 'None'
    Day = 'Day'
    Weekday = 'Weekday'
    Week = 'Week'
    Month = 'Month'
    Year = 'Year'

class ReadGlipCardResponseEndingOn(Enum):
    """ Iterations end datetime for periodic events """
    
    None_ = 'None'
    Count = 'Count'
    Date = 'Date'

class ReadGlipCardResponseColor(Enum):
    """
    Color of Event title, including its presentation in Calendar; or the color of the side border
    of an interactive message of a Card
    
    Generated by Python OpenAPI Parser
    """
    
    Black = 'Black'
    Red = 'Red'
    Orange = 'Orange'
    Yellow = 'Yellow'
    Green = 'Green'
    Blue = 'Blue'
    Purple = 'Purple'
    Magenta = 'Magenta'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadGlipCardResponse(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of an attachment """
    
    type: Optional[ReadGlipCardResponseType] = 'Card'
    """ Type of an attachment """
    
    fallback: Optional[str] = None
    """
    A string of default text that will be rendered in the case that the client does not support
    Interactive Messages
    """
    
    intro: Optional[str] = None
    """ A pretext to the message """
    
    author: Optional[ReadGlipCardResponseAuthor] = None
    """ Information about the author """
    
    title: Optional[str] = None
    """ Message title """
    
    text: Optional[str] = None
    """
    A large string field (up to 1000 chars) to be displayed as the body of a message (Supports
    GlipDown)
    """
    
    image_uri: Optional[str] = None
    """ Link to an image displayed at the bottom of a message """
    
    thumbnail_uri: Optional[str] = None
    """ Link to an image preview displayed to the right of a message (82x82) """
    
    fields: Optional[List[ReadGlipCardResponseFieldsItem]] = None
    """ Information on navigation """
    
    footnote: Optional[ReadGlipCardResponseFootnote] = None
    """ Message Footer """
    
    creator_id: Optional[str] = None
    """ Internal identifier of a person created an event """
    
    start_time: Optional[str] = None
    """ Datetime of starting an event """
    
    end_time: Optional[str] = None
    """ Datetime of ending an event """
    
    all_day: Optional[bool] = False
    """ Indicates whether an event has some specific time slot or lasts for the whole day(s) """
    
    recurrence: Optional[ReadGlipCardResponseRecurrence] = None
    """ Event recurrence settings. """
    
    ending_condition: Optional[str] = None
    """ Condition of ending """
    
    ending_after: Optional[int] = None
    """ Count of iterations. For periodic events only """
    
    ending_on: Optional[ReadGlipCardResponseEndingOn] = 'None'
    """ Iterations end datetime for periodic events """
    
    color: Optional[ReadGlipCardResponseColor] = 'Black'
    """
    Color of Event title, including its presentation in Calendar; or the color of the side border
    of an interactive message of a Card
    """
    
    location: Optional[str] = None
    """ Event location """
    
    description: Optional[str] = None
    """ Event details """
    

class ReadGlipCardResponseType(Enum):
    """ Type of an attachment """
    
    Card = 'Card'
    Event = 'Event'
    Note = 'Note'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadGlipCardResponseAuthor(DataClassJsonMixin):
    """ Information about the author """
    
    name: Optional[str] = None
    """ Name of a message author """
    
    uri: Optional[str] = None
    """ Link to an author's name """
    
    icon_uri: Optional[str] = None
    """ Link to an image displayed to the left of an author's name; sized 82x82px """
    

class ReadGlipCardResponseFieldsItemStyle(Enum):
    """ Style of width span applied to a field """
    
    Short = 'Short'
    Long = 'Long'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadGlipCardResponseFieldsItem(DataClassJsonMixin):
    title: Optional[str] = None
    """ Title of an individual field """
    
    value: Optional[str] = None
    """ Value of an individual field (supports Markdown) """
    
    style: Optional[ReadGlipCardResponseFieldsItemStyle] = 'Short'
    """ Style of width span applied to a field """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadGlipCardResponseFootnote(DataClassJsonMixin):
    """ Message Footer """
    
    text: Optional[str] = None
    """ Text of a footer """
    
    icon_uri: Optional[str] = None
    """ Link to an icon displayed to the left of a footer; sized 32x32px """
    
    time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """
    Message creation datetime in ISO 8601 format including timezone, for example
    *2016-03-10T18:07:52.534Z*
    """
    

class ReadGlipCardResponseRecurrence(Enum):
    """ Event recurrence settings. """
    
    None_ = 'None'
    Day = 'Day'
    Weekday = 'Weekday'
    Week = 'Week'
    Month = 'Month'
    Year = 'Year'

class ReadGlipCardResponseEndingOn(Enum):
    """ Iterations end datetime for periodic events """
    
    None_ = 'None'
    Count = 'Count'
    Date = 'Date'

class ReadGlipCardResponseColor(Enum):
    """
    Color of Event title, including its presentation in Calendar; or the color of the side border
    of an interactive message of a Card
    
    Generated by Python OpenAPI Parser
    """
    
    Black = 'Black'
    Red = 'Red'
    Orange = 'Orange'
    Yellow = 'Yellow'
    Green = 'Green'
    Blue = 'Blue'
    Purple = 'Purple'
    Magenta = 'Magenta'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadGlipCardResponse(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of an attachment """
    
    type: Optional[ReadGlipCardResponseType] = 'Card'
    """ Type of an attachment """
    
    fallback: Optional[str] = None
    """
    A string of default text that will be rendered in the case that the client does not support
    Interactive Messages
    """
    
    intro: Optional[str] = None
    """ A pretext to the message """
    
    author: Optional[ReadGlipCardResponseAuthor] = None
    """ Information about the author """
    
    title: Optional[str] = None
    """ Message title """
    
    text: Optional[str] = None
    """
    A large string field (up to 1000 chars) to be displayed as the body of a message (Supports
    GlipDown)
    """
    
    image_uri: Optional[str] = None
    """ Link to an image displayed at the bottom of a message """
    
    thumbnail_uri: Optional[str] = None
    """ Link to an image preview displayed to the right of a message (82x82) """
    
    fields: Optional[List[ReadGlipCardResponseFieldsItem]] = None
    """ Information on navigation """
    
    footnote: Optional[ReadGlipCardResponseFootnote] = None
    """ Message Footer """
    
    creator_id: Optional[str] = None
    """ Internal identifier of a person created an event """
    
    start_time: Optional[str] = None
    """ Datetime of starting an event """
    
    end_time: Optional[str] = None
    """ Datetime of ending an event """
    
    all_day: Optional[bool] = False
    """ Indicates whether an event has some specific time slot or lasts for the whole day(s) """
    
    recurrence: Optional[ReadGlipCardResponseRecurrence] = None
    """ Event recurrence settings. """
    
    ending_condition: Optional[str] = None
    """ Condition of ending """
    
    ending_after: Optional[int] = None
    """ Count of iterations. For periodic events only """
    
    ending_on: Optional[ReadGlipCardResponseEndingOn] = 'None'
    """ Iterations end datetime for periodic events """
    
    color: Optional[ReadGlipCardResponseColor] = 'Black'
    """
    Color of Event title, including its presentation in Calendar; or the color of the side border
    of an interactive message of a Card
    """
    
    location: Optional[str] = None
    """ Event location """
    
    description: Optional[str] = None
    """ Event details """
    

class ReadGlipEventsResponseRecordsItemRecurrence(Enum):
    """ Event recurrence settings """
    
    None_ = 'None'
    Day = 'Day'
    Weekday = 'Weekday'
    Week = 'Week'
    Month = 'Month'
    Year = 'Year'

class ReadGlipEventsResponseRecordsItemEndingOn(Enum):
    """ Iterations end datetime for periodic events """
    
    None_ = 'None'
    Count = 'Count'
    Date = 'Date'

class ReadGlipEventsResponseRecordsItemColor(Enum):
    """ Color of Event title (including its presentation in Calendar) """
    
    Black = 'Black'
    Red = 'Red'
    Orange = 'Orange'
    Yellow = 'Yellow'
    Green = 'Green'
    Blue = 'Blue'
    Purple = 'Purple'
    Magenta = 'Magenta'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadGlipEventsResponseRecordsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of an event """
    
    creator_id: Optional[str] = None
    """ Internal identifier of a person created an event """
    
    title: Optional[str] = None
    """ Event title """
    
    start_time: Optional[str] = None
    """ Datetime of starting an event """
    
    end_time: Optional[str] = None
    """ Datetime of ending an event """
    
    all_day: Optional[bool] = False
    """ Indicates whether an event has some specific time slot or lasts for the whole day(s) """
    
    recurrence: Optional[ReadGlipEventsResponseRecordsItemRecurrence] = None
    """ Event recurrence settings """
    
    ending_condition: Optional[str] = None
    """ Condition of ending """
    
    ending_after: Optional[int] = None
    """ Count of iterations. For periodic events only """
    
    ending_on: Optional[ReadGlipEventsResponseRecordsItemEndingOn] = 'None'
    """ Iterations end datetime for periodic events """
    
    color: Optional[ReadGlipEventsResponseRecordsItemColor] = 'Black'
    """ Color of Event title (including its presentation in Calendar) """
    
    location: Optional[str] = None
    """ Event location """
    
    description: Optional[str] = None
    """ Event details """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadGlipEventsResponseNavigation(DataClassJsonMixin):
    prev_page_token: Optional[str] = None
    """
    Previous page token. To get previous page, user should pass one of returned token in next
    request and, in turn, required page will be returned with new tokens
    """
    
    next_page_token: Optional[str] = None
    """
    Next page token. To get next page, user should pass one of returned token in next request and,
    in turn, required page will be returned with new tokens
    """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadGlipEventsResponse(DataClassJsonMixin):
    records: Optional[List[ReadGlipEventsResponseRecordsItem]] = None
    """ List of events created by the current user """
    
    navigation: Optional[ReadGlipEventsResponseNavigation] = None

class ReadGlipEventsResponseRecordsItemRecurrence(Enum):
    """ Event recurrence settings """
    
    None_ = 'None'
    Day = 'Day'
    Weekday = 'Weekday'
    Week = 'Week'
    Month = 'Month'
    Year = 'Year'

class ReadGlipEventsResponseRecordsItemEndingOn(Enum):
    """ Iterations end datetime for periodic events """
    
    None_ = 'None'
    Count = 'Count'
    Date = 'Date'

class ReadGlipEventsResponseRecordsItemColor(Enum):
    """ Color of Event title (including its presentation in Calendar) """
    
    Black = 'Black'
    Red = 'Red'
    Orange = 'Orange'
    Yellow = 'Yellow'
    Green = 'Green'
    Blue = 'Blue'
    Purple = 'Purple'
    Magenta = 'Magenta'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadGlipEventsResponseRecordsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of an event """
    
    creator_id: Optional[str] = None
    """ Internal identifier of a person created an event """
    
    title: Optional[str] = None
    """ Event title """
    
    start_time: Optional[str] = None
    """ Datetime of starting an event """
    
    end_time: Optional[str] = None
    """ Datetime of ending an event """
    
    all_day: Optional[bool] = False
    """ Indicates whether an event has some specific time slot or lasts for the whole day(s) """
    
    recurrence: Optional[ReadGlipEventsResponseRecordsItemRecurrence] = None
    """ Event recurrence settings """
    
    ending_condition: Optional[str] = None
    """ Condition of ending """
    
    ending_after: Optional[int] = None
    """ Count of iterations. For periodic events only """
    
    ending_on: Optional[ReadGlipEventsResponseRecordsItemEndingOn] = 'None'
    """ Iterations end datetime for periodic events """
    
    color: Optional[ReadGlipEventsResponseRecordsItemColor] = 'Black'
    """ Color of Event title (including its presentation in Calendar) """
    
    location: Optional[str] = None
    """ Event location """
    
    description: Optional[str] = None
    """ Event details """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadGlipEventsResponseNavigation(DataClassJsonMixin):
    prev_page_token: Optional[str] = None
    """
    Previous page token. To get previous page, user should pass one of returned token in next
    request and, in turn, required page will be returned with new tokens
    """
    
    next_page_token: Optional[str] = None
    """
    Next page token. To get next page, user should pass one of returned token in next request and,
    in turn, required page will be returned with new tokens
    """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadGlipEventsResponse(DataClassJsonMixin):
    records: Optional[List[ReadGlipEventsResponseRecordsItem]] = None
    """ List of events created by the current user """
    
    navigation: Optional[ReadGlipEventsResponseNavigation] = None

class CreateEventRequestRecurrence(Enum):
    """
    Event recurrence settings. For non-periodic events the value is 'None'. Must be greater or
    equal to event duration: 1- Day/Weekday; 7 - Week; 28 - Month; 365 - Year
    
    Generated by Python OpenAPI Parser
    """
    
    None_ = 'None'
    Day = 'Day'
    Weekday = 'Weekday'
    Week = 'Week'
    Month = 'Month'
    Year = 'Year'

class CreateEventRequestEndingOn(Enum):
    """ Iterations end datetime for periodic events. """
    
    None_ = 'None'
    Count = 'Count'
    Date = 'Date'

class CreateEventRequestColor(Enum):
    """ Color of Event title (including its presentation in Calendar) """
    
    Black = 'Black'
    Red = 'Red'
    Orange = 'Orange'
    Yellow = 'Yellow'
    Green = 'Green'
    Blue = 'Blue'
    Purple = 'Purple'
    Magenta = 'Magenta'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateEventRequest(DataClassJsonMixin):
    """
    Required Properties:
     - title
     - start_time
     - end_time
    
    Generated by Python OpenAPI Parser
    """
    
    title: str
    """ Event title """
    
    start_time: str
    """ Datetime of starting an event """
    
    end_time: str
    """ Datetime of ending an event """
    
    id: Optional[str] = None
    """ Internal identifier of an event """
    
    creator_id: Optional[str] = None
    """ Internal identifier of a person created an event """
    
    all_day: Optional[bool] = False
    """ Indicates whether event has some specific time slot or lasts for whole day(s) """
    
    recurrence: Optional[CreateEventRequestRecurrence] = None
    """
    Event recurrence settings. For non-periodic events the value is 'None'. Must be greater or
    equal to event duration: 1- Day/Weekday; 7 - Week; 28 - Month; 365 - Year
    """
    
    ending_condition: Optional[str] = None
    """ Condition of ending """
    
    ending_after: Optional[int] = None
    """
    Count of iterations. For periodic events only. Value range is 1 - 10. Must be specified if
    'endingCondition' is 'Count'
    """
    
    ending_on: Optional[CreateEventRequestEndingOn] = 'None'
    """ Iterations end datetime for periodic events. """
    
    color: Optional[CreateEventRequestColor] = 'Black'
    """ Color of Event title (including its presentation in Calendar) """
    
    location: Optional[str] = None
    """ Event location """
    
    description: Optional[str] = None
    """ Event details """
    

class CreateEventResponseRecurrence(Enum):
    """ Event recurrence settings """
    
    None_ = 'None'
    Day = 'Day'
    Weekday = 'Weekday'
    Week = 'Week'
    Month = 'Month'
    Year = 'Year'

class CreateEventResponseEndingOn(Enum):
    """ Iterations end datetime for periodic events """
    
    None_ = 'None'
    Count = 'Count'
    Date = 'Date'

class CreateEventResponseColor(Enum):
    """ Color of Event title (including its presentation in Calendar) """
    
    Black = 'Black'
    Red = 'Red'
    Orange = 'Orange'
    Yellow = 'Yellow'
    Green = 'Green'
    Blue = 'Blue'
    Purple = 'Purple'
    Magenta = 'Magenta'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateEventResponse(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of an event """
    
    creator_id: Optional[str] = None
    """ Internal identifier of a person created an event """
    
    title: Optional[str] = None
    """ Event title """
    
    start_time: Optional[str] = None
    """ Datetime of starting an event """
    
    end_time: Optional[str] = None
    """ Datetime of ending an event """
    
    all_day: Optional[bool] = False
    """ Indicates whether an event has some specific time slot or lasts for the whole day(s) """
    
    recurrence: Optional[CreateEventResponseRecurrence] = None
    """ Event recurrence settings """
    
    ending_condition: Optional[str] = None
    """ Condition of ending """
    
    ending_after: Optional[int] = None
    """ Count of iterations. For periodic events only """
    
    ending_on: Optional[CreateEventResponseEndingOn] = 'None'
    """ Iterations end datetime for periodic events """
    
    color: Optional[CreateEventResponseColor] = 'Black'
    """ Color of Event title (including its presentation in Calendar) """
    
    location: Optional[str] = None
    """ Event location """
    
    description: Optional[str] = None
    """ Event details """
    

class ReadEventResponseRecurrence(Enum):
    """ Event recurrence settings """
    
    None_ = 'None'
    Day = 'Day'
    Weekday = 'Weekday'
    Week = 'Week'
    Month = 'Month'
    Year = 'Year'

class ReadEventResponseEndingOn(Enum):
    """ Iterations end datetime for periodic events """
    
    None_ = 'None'
    Count = 'Count'
    Date = 'Date'

class ReadEventResponseColor(Enum):
    """ Color of Event title (including its presentation in Calendar) """
    
    Black = 'Black'
    Red = 'Red'
    Orange = 'Orange'
    Yellow = 'Yellow'
    Green = 'Green'
    Blue = 'Blue'
    Purple = 'Purple'
    Magenta = 'Magenta'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadEventResponse(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of an event """
    
    creator_id: Optional[str] = None
    """ Internal identifier of a person created an event """
    
    title: Optional[str] = None
    """ Event title """
    
    start_time: Optional[str] = None
    """ Datetime of starting an event """
    
    end_time: Optional[str] = None
    """ Datetime of ending an event """
    
    all_day: Optional[bool] = False
    """ Indicates whether an event has some specific time slot or lasts for the whole day(s) """
    
    recurrence: Optional[ReadEventResponseRecurrence] = None
    """ Event recurrence settings """
    
    ending_condition: Optional[str] = None
    """ Condition of ending """
    
    ending_after: Optional[int] = None
    """ Count of iterations. For periodic events only """
    
    ending_on: Optional[ReadEventResponseEndingOn] = 'None'
    """ Iterations end datetime for periodic events """
    
    color: Optional[ReadEventResponseColor] = 'Black'
    """ Color of Event title (including its presentation in Calendar) """
    
    location: Optional[str] = None
    """ Event location """
    
    description: Optional[str] = None
    """ Event details """
    

class UpdateEventResponseRecurrence(Enum):
    """ Event recurrence settings """
    
    None_ = 'None'
    Day = 'Day'
    Weekday = 'Weekday'
    Week = 'Week'
    Month = 'Month'
    Year = 'Year'

class UpdateEventResponseEndingOn(Enum):
    """ Iterations end datetime for periodic events """
    
    None_ = 'None'
    Count = 'Count'
    Date = 'Date'

class UpdateEventResponseColor(Enum):
    """ Color of Event title (including its presentation in Calendar) """
    
    Black = 'Black'
    Red = 'Red'
    Orange = 'Orange'
    Yellow = 'Yellow'
    Green = 'Green'
    Blue = 'Blue'
    Purple = 'Purple'
    Magenta = 'Magenta'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateEventResponse(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of an event """
    
    creator_id: Optional[str] = None
    """ Internal identifier of a person created an event """
    
    title: Optional[str] = None
    """ Event title """
    
    start_time: Optional[str] = None
    """ Datetime of starting an event """
    
    end_time: Optional[str] = None
    """ Datetime of ending an event """
    
    all_day: Optional[bool] = False
    """ Indicates whether an event has some specific time slot or lasts for the whole day(s) """
    
    recurrence: Optional[UpdateEventResponseRecurrence] = None
    """ Event recurrence settings """
    
    ending_condition: Optional[str] = None
    """ Condition of ending """
    
    ending_after: Optional[int] = None
    """ Count of iterations. For periodic events only """
    
    ending_on: Optional[UpdateEventResponseEndingOn] = 'None'
    """ Iterations end datetime for periodic events """
    
    color: Optional[UpdateEventResponseColor] = 'Black'
    """ Color of Event title (including its presentation in Calendar) """
    
    location: Optional[str] = None
    """ Event location """
    
    description: Optional[str] = None
    """ Event details """
    

class ListGroupEventsResponseRecurrence(Enum):
    """ Event recurrence settings """
    
    None_ = 'None'
    Day = 'Day'
    Weekday = 'Weekday'
    Week = 'Week'
    Month = 'Month'
    Year = 'Year'

class ListGroupEventsResponseEndingOn(Enum):
    """ Iterations end datetime for periodic events """
    
    None_ = 'None'
    Count = 'Count'
    Date = 'Date'

class ListGroupEventsResponseColor(Enum):
    """ Color of Event title (including its presentation in Calendar) """
    
    Black = 'Black'
    Red = 'Red'
    Orange = 'Orange'
    Yellow = 'Yellow'
    Green = 'Green'
    Blue = 'Blue'
    Purple = 'Purple'
    Magenta = 'Magenta'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListGroupEventsResponse(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of an event """
    
    creator_id: Optional[str] = None
    """ Internal identifier of a person created an event """
    
    title: Optional[str] = None
    """ Event title """
    
    start_time: Optional[str] = None
    """ Datetime of starting an event """
    
    end_time: Optional[str] = None
    """ Datetime of ending an event """
    
    all_day: Optional[bool] = False
    """ Indicates whether an event has some specific time slot or lasts for the whole day(s) """
    
    recurrence: Optional[ListGroupEventsResponseRecurrence] = None
    """ Event recurrence settings """
    
    ending_condition: Optional[str] = None
    """ Condition of ending """
    
    ending_after: Optional[int] = None
    """ Count of iterations. For periodic events only """
    
    ending_on: Optional[ListGroupEventsResponseEndingOn] = 'None'
    """ Iterations end datetime for periodic events """
    
    color: Optional[ListGroupEventsResponseColor] = 'Black'
    """ Color of Event title (including its presentation in Calendar) """
    
    location: Optional[str] = None
    """ Event location """
    
    description: Optional[str] = None
    """ Event details """
    

class CreateEventbyGroupIdResponseRecurrence(Enum):
    """ Event recurrence settings """
    
    None_ = 'None'
    Day = 'Day'
    Weekday = 'Weekday'
    Week = 'Week'
    Month = 'Month'
    Year = 'Year'

class CreateEventbyGroupIdResponseEndingOn(Enum):
    """ Iterations end datetime for periodic events """
    
    None_ = 'None'
    Count = 'Count'
    Date = 'Date'

class CreateEventbyGroupIdResponseColor(Enum):
    """ Color of Event title (including its presentation in Calendar) """
    
    Black = 'Black'
    Red = 'Red'
    Orange = 'Orange'
    Yellow = 'Yellow'
    Green = 'Green'
    Blue = 'Blue'
    Purple = 'Purple'
    Magenta = 'Magenta'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateEventbyGroupIdResponse(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of an event """
    
    creator_id: Optional[str] = None
    """ Internal identifier of a person created an event """
    
    title: Optional[str] = None
    """ Event title """
    
    start_time: Optional[str] = None
    """ Datetime of starting an event """
    
    end_time: Optional[str] = None
    """ Datetime of ending an event """
    
    all_day: Optional[bool] = False
    """ Indicates whether an event has some specific time slot or lasts for the whole day(s) """
    
    recurrence: Optional[CreateEventbyGroupIdResponseRecurrence] = None
    """ Event recurrence settings """
    
    ending_condition: Optional[str] = None
    """ Condition of ending """
    
    ending_after: Optional[int] = None
    """ Count of iterations. For periodic events only """
    
    ending_on: Optional[CreateEventbyGroupIdResponseEndingOn] = 'None'
    """ Iterations end datetime for periodic events """
    
    color: Optional[CreateEventbyGroupIdResponseColor] = 'Black'
    """ Color of Event title (including its presentation in Calendar) """
    
    location: Optional[str] = None
    """ Event location """
    
    description: Optional[str] = None
    """ Event details """
    

class ListChatNotesStatus(Enum):
    Active = 'Active'
    Draft = 'Draft'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListChatNotesResponseRecordsItemCreator(DataClassJsonMixin):
    """ Note creator information """
    
    id: Optional[str] = None
    """ Internal identifier of a user who created a note/task """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListChatNotesResponseRecordsItemLastModifiedBy(DataClassJsonMixin):
    """ Note last modification information """
    
    id: Optional[str] = None
    """ Internal identifier of the user who last updated the note """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListChatNotesResponseRecordsItemLockedBy(DataClassJsonMixin):
    """
    Returned for the note being edited (locked) at the current moment. Information on the user
    editing the note
    
    Generated by Python OpenAPI Parser
    """
    
    id: Optional[str] = None
    """ Internal identifier of the user editing the note """
    

class ListChatNotesResponseRecordsItemStatus(Enum):
    """
    Note publishing status. Any note is created in 'Draft' status. After it is posted it becomes
    'Active'
    
    Generated by Python OpenAPI Parser
    """
    
    Active = 'Active'
    Draft = 'Draft'

class ListChatNotesResponseRecordsItemType(Enum):
    Note = 'Note'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListChatNotesResponseRecordsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a note """
    
    title: Optional[str] = None
    """ Title of a note """
    
    chat_ids: Optional[List[str]] = None
    """ Internal identifiers of the chat(s) where the note is posted or shared. """
    
    preview: Optional[str] = None
    """ Preview of a note (first 150 characters of a body) """
    
    creator: Optional[ListChatNotesResponseRecordsItemCreator] = None
    """ Note creator information """
    
    last_modified_by: Optional[ListChatNotesResponseRecordsItemLastModifiedBy] = None
    """ Note last modification information """
    
    locked_by: Optional[ListChatNotesResponseRecordsItemLockedBy] = None
    """
    Returned for the note being edited (locked) at the current moment. Information on the user
    editing the note
    """
    
    status: Optional[ListChatNotesResponseRecordsItemStatus] = None
    """
    Note publishing status. Any note is created in 'Draft' status. After it is posted it becomes
    'Active'
    """
    
    creation_time: Optional[str] = None
    """ Creation time """
    
    last_modified_time: Optional[str] = None
    """ Datetime of the note last update """
    
    type: Optional[ListChatNotesResponseRecordsItemType] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListChatNotesResponseNavigation(DataClassJsonMixin):
    prev_page_token: Optional[str] = None
    """
    Previous page token. To get previous page, user should pass one of returned token in next
    request and, in turn, required page will be returned with new tokens
    """
    
    next_page_token: Optional[str] = None
    """
    Next page token. To get next page, user should pass one of returned token in next request and,
    in turn, required page will be returned with new tokens
    """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListChatNotesResponse(DataClassJsonMixin):
    records: Optional[List[ListChatNotesResponseRecordsItem]] = None
    navigation: Optional[ListChatNotesResponseNavigation] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateChatNoteRequest(DataClassJsonMixin):
    """
    Required Properties:
     - title
    
    Generated by Python OpenAPI Parser
    """
    
    title: str
    """ Title of a note. Max allowed legth is 250 characters """
    
    body: Optional[str] = None
    """ Contents of a note; HTML-markuped text. Max allowed length is 1048576 characters (1 Mb). """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateChatNoteResponseCreator(DataClassJsonMixin):
    """ Note creator information """
    
    id: Optional[str] = None
    """ Internal identifier of a user who created a note/task """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateChatNoteResponseLastModifiedBy(DataClassJsonMixin):
    """ Note last modification information """
    
    id: Optional[str] = None
    """ Internal identifier of the user who last updated the note """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateChatNoteResponseLockedBy(DataClassJsonMixin):
    """
    Returned for the note being edited (locked) at the current moment. Information on the user
    editing the note
    
    Generated by Python OpenAPI Parser
    """
    
    id: Optional[str] = None
    """ Internal identifier of the user editing the note """
    

class CreateChatNoteResponseStatus(Enum):
    """
    Note publishing status. Any note is created in 'Draft' status. After it is posted it becomes
    'Active'
    
    Generated by Python OpenAPI Parser
    """
    
    Active = 'Active'
    Draft = 'Draft'

class CreateChatNoteResponseType(Enum):
    Note = 'Note'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateChatNoteResponse(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a note """
    
    title: Optional[str] = None
    """ Title of a note """
    
    chat_ids: Optional[List[str]] = None
    """ Internal identifiers of the chat(s) where the note is posted or shared. """
    
    preview: Optional[str] = None
    """ Preview of a note (first 150 characters of a body) """
    
    creator: Optional[CreateChatNoteResponseCreator] = None
    """ Note creator information """
    
    last_modified_by: Optional[CreateChatNoteResponseLastModifiedBy] = None
    """ Note last modification information """
    
    locked_by: Optional[CreateChatNoteResponseLockedBy] = None
    """
    Returned for the note being edited (locked) at the current moment. Information on the user
    editing the note
    """
    
    status: Optional[CreateChatNoteResponseStatus] = None
    """
    Note publishing status. Any note is created in 'Draft' status. After it is posted it becomes
    'Active'
    """
    
    creation_time: Optional[str] = None
    """ Creation time """
    
    last_modified_time: Optional[str] = None
    """ Datetime of the note last update """
    
    type: Optional[CreateChatNoteResponseType] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadUserNoteResponseCreator(DataClassJsonMixin):
    """ Note creator information """
    
    id: Optional[str] = None
    """ Internal identifier of a user who created a note/task """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadUserNoteResponseLastModifiedBy(DataClassJsonMixin):
    """ Note last modification information """
    
    id: Optional[str] = None
    """ Internal identifier of the user who last updated the note """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadUserNoteResponseLockedBy(DataClassJsonMixin):
    """
    Returned for the note being edited (locked) at the current moment. Information on the user
    editing the note
    
    Generated by Python OpenAPI Parser
    """
    
    id: Optional[str] = None
    """ Internal identifier of the user editing the note """
    

class ReadUserNoteResponseStatus(Enum):
    """
    Note publishing status. Any note is created in 'Draft' status. After it is posted it becomes
    'Active'
    
    Generated by Python OpenAPI Parser
    """
    
    Active = 'Active'
    Draft = 'Draft'

class ReadUserNoteResponseType(Enum):
    Note = 'Note'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadUserNoteResponse(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a note """
    
    title: Optional[str] = None
    """ Title of a note """
    
    chat_ids: Optional[List[str]] = None
    """ Internal identifiers of the chat(s) where the note is posted or shared. """
    
    preview: Optional[str] = None
    """ Preview of a note (first 150 characters of a body) """
    
    body: Optional[str] = None
    """ Text of a note """
    
    creator: Optional[ReadUserNoteResponseCreator] = None
    """ Note creator information """
    
    last_modified_by: Optional[ReadUserNoteResponseLastModifiedBy] = None
    """ Note last modification information """
    
    locked_by: Optional[ReadUserNoteResponseLockedBy] = None
    """
    Returned for the note being edited (locked) at the current moment. Information on the user
    editing the note
    """
    
    status: Optional[ReadUserNoteResponseStatus] = None
    """
    Note publishing status. Any note is created in 'Draft' status. After it is posted it becomes
    'Active'
    """
    
    creation_time: Optional[str] = None
    """ Creation time """
    
    last_modified_time: Optional[str] = None
    """ Datetime of the note last update """
    
    type: Optional[ReadUserNoteResponseType] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class PatchNoteResponseCreator(DataClassJsonMixin):
    """ Note creator information """
    
    id: Optional[str] = None
    """ Internal identifier of a user who created a note/task """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class PatchNoteResponseLastModifiedBy(DataClassJsonMixin):
    """ Note last modification information """
    
    id: Optional[str] = None
    """ Internal identifier of the user who last updated the note """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class PatchNoteResponseLockedBy(DataClassJsonMixin):
    """
    Returned for the note being edited (locked) at the current moment. Information on the user
    editing the note
    
    Generated by Python OpenAPI Parser
    """
    
    id: Optional[str] = None
    """ Internal identifier of the user editing the note """
    

class PatchNoteResponseStatus(Enum):
    """
    Note publishing status. Any note is created in 'Draft' status. After it is posted it becomes
    'Active'
    
    Generated by Python OpenAPI Parser
    """
    
    Active = 'Active'
    Draft = 'Draft'

class PatchNoteResponseType(Enum):
    Note = 'Note'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class PatchNoteResponse(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a note """
    
    title: Optional[str] = None
    """ Title of a note """
    
    chat_ids: Optional[List[str]] = None
    """ Internal identifiers of the chat(s) where the note is posted or shared. """
    
    preview: Optional[str] = None
    """ Preview of a note (first 150 characters of a body) """
    
    creator: Optional[PatchNoteResponseCreator] = None
    """ Note creator information """
    
    last_modified_by: Optional[PatchNoteResponseLastModifiedBy] = None
    """ Note last modification information """
    
    locked_by: Optional[PatchNoteResponseLockedBy] = None
    """
    Returned for the note being edited (locked) at the current moment. Information on the user
    editing the note
    """
    
    status: Optional[PatchNoteResponseStatus] = None
    """
    Note publishing status. Any note is created in 'Draft' status. After it is posted it becomes
    'Active'
    """
    
    creation_time: Optional[str] = None
    """ Creation time """
    
    last_modified_time: Optional[str] = None
    """ Datetime of the note last update """
    
    type: Optional[PatchNoteResponseType] = None

class ListChatTasksStatusItem(Enum):
    Pending = 'Pending'
    InProgress = 'InProgress'
    Completed = 'Completed'

class ListChatTasksAssignmentStatus(Enum):
    Unassigned = 'Unassigned'
    Assigned = 'Assigned'

class ListChatTasksAssigneeStatus(Enum):
    Pending = 'Pending'
    Completed = 'Completed'

class ListChatTasksResponseRecordsItemType(Enum):
    """ Type of a task """
    
    Task = 'Task'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListChatTasksResponseRecordsItemCreator(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a user who created a note/task """
    

class ListChatTasksResponseRecordsItemStatus(Enum):
    """ Status of task execution """
    
    Pending = 'Pending'
    InProgress = 'InProgress'
    Completed = 'Completed'

class ListChatTasksResponseRecordsItemAssigneesItemStatus(Enum):
    """ Status of the task execution by assignee """
    
    Pending = 'Pending'
    Completed = 'Completed'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListChatTasksResponseRecordsItemAssigneesItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of an assignee """
    
    status: Optional[ListChatTasksResponseRecordsItemAssigneesItemStatus] = None
    """ Status of the task execution by assignee """
    

class ListChatTasksResponseRecordsItemCompletenessCondition(Enum):
    """ Specifies how to determine task completeness """
    
    Simple = 'Simple'
    AllAssignees = 'AllAssignees'
    Percentage = 'Percentage'

class ListChatTasksResponseRecordsItemColor(Enum):
    """ Font color of a post with the current task """
    
    Black = 'Black'
    Red = 'Red'
    Orange = 'Orange'
    Yellow = 'Yellow'
    Green = 'Green'
    Blue = 'Blue'
    Purple = 'Purple'
    Magenta = 'Magenta'

class ListChatTasksResponseRecordsItemRecurrenceSchedule(Enum):
    """ Task recurrence settings. For non-periodic tasks the value is 'None' """
    
    None_ = 'None'
    Daily = 'Daily'
    Weekdays = 'Weekdays'
    Weekly = 'Weekly'
    Monthly = 'Monthly'
    Yearly = 'Yearly'

class ListChatTasksResponseRecordsItemRecurrenceEndingCondition(Enum):
    """ Task ending condition """
    
    None_ = 'None'
    Count = 'Count'
    Date = 'Date'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListChatTasksResponseRecordsItemRecurrence(DataClassJsonMixin):
    schedule: Optional[ListChatTasksResponseRecordsItemRecurrenceSchedule] = None
    """ Task recurrence settings. For non-periodic tasks the value is 'None' """
    
    ending_condition: Optional[ListChatTasksResponseRecordsItemRecurrenceEndingCondition] = None
    """ Task ending condition """
    
    ending_after: Optional[int] = None
    """ Count of iterations of periodic tasks """
    
    ending_on: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """ End date of periodic task """
    

class ListChatTasksResponseRecordsItemAttachmentsItemType(Enum):
    """ Attachment type (currently only `File` value is supported). """
    
    File = 'File'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListChatTasksResponseRecordsItemAttachmentsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a file """
    
    type: Optional[ListChatTasksResponseRecordsItemAttachmentsItemType] = None
    """ Attachment type (currently only `File` value is supported). """
    
    name: Optional[str] = None
    """ Name of the attached file (including extension name). """
    
    content_uri: Optional[str] = None
    """ Link to an attachment content """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListChatTasksResponseRecordsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a task """
    
    creation_time: Optional[str] = None
    """ Datetime of the task creation in UTC time zone. """
    
    last_modified_time: Optional[str] = None
    """ Datetime of the last modification of the task in UTC time zone. """
    
    type: Optional[ListChatTasksResponseRecordsItemType] = None
    """ Type of a task """
    
    creator: Optional[ListChatTasksResponseRecordsItemCreator] = None
    chat_ids: Optional[List[str]] = None
    """ Chat IDs where the task is posted or shared. """
    
    status: Optional[ListChatTasksResponseRecordsItemStatus] = None
    """ Status of task execution """
    
    subject: Optional[str] = None
    """ Name/subject of a task """
    
    assignees: Optional[List[ListChatTasksResponseRecordsItemAssigneesItem]] = None
    completeness_condition: Optional[ListChatTasksResponseRecordsItemCompletenessCondition] = None
    """ Specifies how to determine task completeness """
    
    completeness_percentage: Optional[int] = None
    """
    Current completeness percentage of the task with the specified percentage completeness
    condition
    """
    
    start_date: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """ Task start date """
    
    due_date: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """ Task due date/time """
    
    color: Optional[ListChatTasksResponseRecordsItemColor] = None
    """ Font color of a post with the current task """
    
    section: Optional[str] = None
    """ Task section to group/search by """
    
    description: Optional[str] = None
    """ Task details """
    
    recurrence: Optional[ListChatTasksResponseRecordsItemRecurrence] = None
    attachments: Optional[List[ListChatTasksResponseRecordsItemAttachmentsItem]] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListChatTasksResponse(DataClassJsonMixin):
    records: Optional[List[ListChatTasksResponseRecordsItem]] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateTaskRequestAssigneesItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of an assignee """
    

class CreateTaskRequestCompletenessCondition(Enum):
    Simple = 'Simple'
    AllAssignees = 'AllAssignees'
    Percentage = 'Percentage'

class CreateTaskRequestColor(Enum):
    Black = 'Black'
    Red = 'Red'
    Orange = 'Orange'
    Yellow = 'Yellow'
    Green = 'Green'
    Blue = 'Blue'
    Purple = 'Purple'
    Magenta = 'Magenta'

class CreateTaskRequestRecurrenceSchedule(Enum):
    """ Task recurrence settings. For non-periodic tasks the value is 'None' """
    
    None_ = 'None'
    Daily = 'Daily'
    Weekdays = 'Weekdays'
    Weekly = 'Weekly'
    Monthly = 'Monthly'
    Yearly = 'Yearly'

class CreateTaskRequestRecurrenceEndingCondition(Enum):
    """ Task ending condition """
    
    None_ = 'None'
    Count = 'Count'
    Date = 'Date'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateTaskRequestRecurrence(DataClassJsonMixin):
    schedule: Optional[CreateTaskRequestRecurrenceSchedule] = None
    """ Task recurrence settings. For non-periodic tasks the value is 'None' """
    
    ending_condition: Optional[CreateTaskRequestRecurrenceEndingCondition] = None
    """ Task ending condition """
    
    ending_after: Optional[int] = None
    """ Count of iterations of periodic tasks """
    
    ending_on: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """ End date of periodic task """
    

class CreateTaskRequestAttachmentsItemType(Enum):
    """ Type of an attachment """
    
    Event = 'Event'
    File = 'File'
    Note = 'Note'
    Task = 'Task'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateTaskRequestAttachmentsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of an attachment """
    
    type: Optional[CreateTaskRequestAttachmentsItemType] = None
    """ Type of an attachment """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateTaskRequest(DataClassJsonMixin):
    """
    Required Properties:
     - subject
     - assignees
    
    Generated by Python OpenAPI Parser
    """
    
    subject: str
    """ Task name/subject. Max allowed length is 250 characters. """
    
    assignees: List[CreateTaskRequestAssigneesItem]
    completeness_condition: Optional[CreateTaskRequestCompletenessCondition] = 'Simple'
    start_date: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """ Task start date in UTC time zone. """
    
    due_date: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """ Task due date/time in UTC time zone. """
    
    color: Optional[CreateTaskRequestColor] = 'Black'
    section: Optional[str] = None
    """ Task section to group / search by. Max allowed legth is 100 characters. """
    
    description: Optional[str] = None
    """ Task details. Max allowed legth is 102400 characters (100kB). """
    
    recurrence: Optional[CreateTaskRequestRecurrence] = None
    attachments: Optional[List[CreateTaskRequestAttachmentsItem]] = None

class CreateTaskResponseType(Enum):
    """ Type of a task """
    
    Task = 'Task'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateTaskResponseCreator(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a user who created a note/task """
    

class CreateTaskResponseStatus(Enum):
    """ Status of task execution """
    
    Pending = 'Pending'
    InProgress = 'InProgress'
    Completed = 'Completed'

class CreateTaskResponseAssigneesItemStatus(Enum):
    """ Status of the task execution by assignee """
    
    Pending = 'Pending'
    Completed = 'Completed'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateTaskResponseAssigneesItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of an assignee """
    
    status: Optional[CreateTaskResponseAssigneesItemStatus] = None
    """ Status of the task execution by assignee """
    

class CreateTaskResponseCompletenessCondition(Enum):
    """ Specifies how to determine task completeness """
    
    Simple = 'Simple'
    AllAssignees = 'AllAssignees'
    Percentage = 'Percentage'

class CreateTaskResponseColor(Enum):
    """ Font color of a post with the current task """
    
    Black = 'Black'
    Red = 'Red'
    Orange = 'Orange'
    Yellow = 'Yellow'
    Green = 'Green'
    Blue = 'Blue'
    Purple = 'Purple'
    Magenta = 'Magenta'

class CreateTaskResponseRecurrenceSchedule(Enum):
    """ Task recurrence settings. For non-periodic tasks the value is 'None' """
    
    None_ = 'None'
    Daily = 'Daily'
    Weekdays = 'Weekdays'
    Weekly = 'Weekly'
    Monthly = 'Monthly'
    Yearly = 'Yearly'

class CreateTaskResponseRecurrenceEndingCondition(Enum):
    """ Task ending condition """
    
    None_ = 'None'
    Count = 'Count'
    Date = 'Date'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateTaskResponseRecurrence(DataClassJsonMixin):
    schedule: Optional[CreateTaskResponseRecurrenceSchedule] = None
    """ Task recurrence settings. For non-periodic tasks the value is 'None' """
    
    ending_condition: Optional[CreateTaskResponseRecurrenceEndingCondition] = None
    """ Task ending condition """
    
    ending_after: Optional[int] = None
    """ Count of iterations of periodic tasks """
    
    ending_on: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """ End date of periodic task """
    

class CreateTaskResponseAttachmentsItemType(Enum):
    """ Attachment type (currently only `File` value is supported). """
    
    File = 'File'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateTaskResponseAttachmentsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a file """
    
    type: Optional[CreateTaskResponseAttachmentsItemType] = None
    """ Attachment type (currently only `File` value is supported). """
    
    name: Optional[str] = None
    """ Name of the attached file (including extension name). """
    
    content_uri: Optional[str] = None
    """ Link to an attachment content """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateTaskResponse(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a task """
    
    creation_time: Optional[str] = None
    """ Datetime of the task creation in UTC time zone. """
    
    last_modified_time: Optional[str] = None
    """ Datetime of the last modification of the task in UTC time zone. """
    
    type: Optional[CreateTaskResponseType] = None
    """ Type of a task """
    
    creator: Optional[CreateTaskResponseCreator] = None
    chat_ids: Optional[List[str]] = None
    """ Chat IDs where the task is posted or shared. """
    
    status: Optional[CreateTaskResponseStatus] = None
    """ Status of task execution """
    
    subject: Optional[str] = None
    """ Name/subject of a task """
    
    assignees: Optional[List[CreateTaskResponseAssigneesItem]] = None
    completeness_condition: Optional[CreateTaskResponseCompletenessCondition] = None
    """ Specifies how to determine task completeness """
    
    completeness_percentage: Optional[int] = None
    """
    Current completeness percentage of the task with the specified percentage completeness
    condition
    """
    
    start_date: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """ Task start date """
    
    due_date: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """ Task due date/time """
    
    color: Optional[CreateTaskResponseColor] = None
    """ Font color of a post with the current task """
    
    section: Optional[str] = None
    """ Task section to group/search by """
    
    description: Optional[str] = None
    """ Task details """
    
    recurrence: Optional[CreateTaskResponseRecurrence] = None
    attachments: Optional[List[CreateTaskResponseAttachmentsItem]] = None

class ReadTaskResponseType(Enum):
    """ Type of a task """
    
    Task = 'Task'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadTaskResponseCreator(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a user who created a note/task """
    

class ReadTaskResponseStatus(Enum):
    """ Status of task execution """
    
    Pending = 'Pending'
    InProgress = 'InProgress'
    Completed = 'Completed'

class ReadTaskResponseAssigneesItemStatus(Enum):
    """ Status of the task execution by assignee """
    
    Pending = 'Pending'
    Completed = 'Completed'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadTaskResponseAssigneesItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of an assignee """
    
    status: Optional[ReadTaskResponseAssigneesItemStatus] = None
    """ Status of the task execution by assignee """
    

class ReadTaskResponseCompletenessCondition(Enum):
    """ Specifies how to determine task completeness """
    
    Simple = 'Simple'
    AllAssignees = 'AllAssignees'
    Percentage = 'Percentage'

class ReadTaskResponseColor(Enum):
    """ Font color of a post with the current task """
    
    Black = 'Black'
    Red = 'Red'
    Orange = 'Orange'
    Yellow = 'Yellow'
    Green = 'Green'
    Blue = 'Blue'
    Purple = 'Purple'
    Magenta = 'Magenta'

class ReadTaskResponseRecurrenceSchedule(Enum):
    """ Task recurrence settings. For non-periodic tasks the value is 'None' """
    
    None_ = 'None'
    Daily = 'Daily'
    Weekdays = 'Weekdays'
    Weekly = 'Weekly'
    Monthly = 'Monthly'
    Yearly = 'Yearly'

class ReadTaskResponseRecurrenceEndingCondition(Enum):
    """ Task ending condition """
    
    None_ = 'None'
    Count = 'Count'
    Date = 'Date'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadTaskResponseRecurrence(DataClassJsonMixin):
    schedule: Optional[ReadTaskResponseRecurrenceSchedule] = None
    """ Task recurrence settings. For non-periodic tasks the value is 'None' """
    
    ending_condition: Optional[ReadTaskResponseRecurrenceEndingCondition] = None
    """ Task ending condition """
    
    ending_after: Optional[int] = None
    """ Count of iterations of periodic tasks """
    
    ending_on: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """ End date of periodic task """
    

class ReadTaskResponseAttachmentsItemType(Enum):
    """ Attachment type (currently only `File` value is supported). """
    
    File = 'File'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadTaskResponseAttachmentsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a file """
    
    type: Optional[ReadTaskResponseAttachmentsItemType] = None
    """ Attachment type (currently only `File` value is supported). """
    
    name: Optional[str] = None
    """ Name of the attached file (including extension name). """
    
    content_uri: Optional[str] = None
    """ Link to an attachment content """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadTaskResponse(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a task """
    
    creation_time: Optional[str] = None
    """ Datetime of the task creation in UTC time zone. """
    
    last_modified_time: Optional[str] = None
    """ Datetime of the last modification of the task in UTC time zone. """
    
    type: Optional[ReadTaskResponseType] = None
    """ Type of a task """
    
    creator: Optional[ReadTaskResponseCreator] = None
    chat_ids: Optional[List[str]] = None
    """ Chat IDs where the task is posted or shared. """
    
    status: Optional[ReadTaskResponseStatus] = None
    """ Status of task execution """
    
    subject: Optional[str] = None
    """ Name/subject of a task """
    
    assignees: Optional[List[ReadTaskResponseAssigneesItem]] = None
    completeness_condition: Optional[ReadTaskResponseCompletenessCondition] = None
    """ Specifies how to determine task completeness """
    
    completeness_percentage: Optional[int] = None
    """
    Current completeness percentage of the task with the specified percentage completeness
    condition
    """
    
    start_date: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """ Task start date """
    
    due_date: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """ Task due date/time """
    
    color: Optional[ReadTaskResponseColor] = None
    """ Font color of a post with the current task """
    
    section: Optional[str] = None
    """ Task section to group/search by """
    
    description: Optional[str] = None
    """ Task details """
    
    recurrence: Optional[ReadTaskResponseRecurrence] = None
    attachments: Optional[List[ReadTaskResponseAttachmentsItem]] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class PatchTaskRequestAssigneesItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of an assignee """
    

class PatchTaskRequestCompletenessCondition(Enum):
    Simple = 'Simple'
    AllAssignees = 'AllAssignees'
    Percentage = 'Percentage'

class PatchTaskRequestColor(Enum):
    Black = 'Black'
    Red = 'Red'
    Orange = 'Orange'
    Yellow = 'Yellow'
    Green = 'Green'
    Blue = 'Blue'
    Purple = 'Purple'
    Magenta = 'Magenta'

class PatchTaskRequestRecurrenceSchedule(Enum):
    """ Task recurrence settings. For non-periodic tasks the value is 'None' """
    
    None_ = 'None'
    Daily = 'Daily'
    Weekdays = 'Weekdays'
    Weekly = 'Weekly'
    Monthly = 'Monthly'
    Yearly = 'Yearly'

class PatchTaskRequestRecurrenceEndingCondition(Enum):
    """ Task ending condition """
    
    None_ = 'None'
    Count = 'Count'
    Date = 'Date'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class PatchTaskRequestRecurrence(DataClassJsonMixin):
    schedule: Optional[PatchTaskRequestRecurrenceSchedule] = None
    """ Task recurrence settings. For non-periodic tasks the value is 'None' """
    
    ending_condition: Optional[PatchTaskRequestRecurrenceEndingCondition] = None
    """ Task ending condition """
    
    ending_after: Optional[int] = None
    """ Count of iterations of periodic tasks """
    
    ending_on: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """ End date of periodic task """
    

class PatchTaskRequestAttachmentsItemType(Enum):
    """ Type of an attachment """
    
    Event = 'Event'
    File = 'File'
    Note = 'Note'
    Task = 'Task'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class PatchTaskRequestAttachmentsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of an attachment """
    
    type: Optional[PatchTaskRequestAttachmentsItemType] = None
    """ Type of an attachment """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class PatchTaskRequest(DataClassJsonMixin):
    subject: Optional[str] = None
    """ Task name/subject. Max allowed length is 250 characters. """
    
    assignees: Optional[List[PatchTaskRequestAssigneesItem]] = None
    completeness_condition: Optional[PatchTaskRequestCompletenessCondition] = None
    start_date: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """ Task start date in UTC time zone """
    
    due_date: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """ Task due date/time in UTC time zone """
    
    color: Optional[PatchTaskRequestColor] = None
    section: Optional[str] = None
    """ Task section to group/search by. Max allowed legth is 100 characters """
    
    description: Optional[str] = None
    """ Task details. Max allowed legth is 102400 characters (100kB) """
    
    recurrence: Optional[PatchTaskRequestRecurrence] = None
    attachments: Optional[List[PatchTaskRequestAttachmentsItem]] = None

class PatchTaskResponseRecordsItemType(Enum):
    """ Type of a task """
    
    Task = 'Task'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class PatchTaskResponseRecordsItemCreator(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a user who created a note/task """
    

class PatchTaskResponseRecordsItemStatus(Enum):
    """ Status of task execution """
    
    Pending = 'Pending'
    InProgress = 'InProgress'
    Completed = 'Completed'

class PatchTaskResponseRecordsItemAssigneesItemStatus(Enum):
    """ Status of the task execution by assignee """
    
    Pending = 'Pending'
    Completed = 'Completed'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class PatchTaskResponseRecordsItemAssigneesItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of an assignee """
    
    status: Optional[PatchTaskResponseRecordsItemAssigneesItemStatus] = None
    """ Status of the task execution by assignee """
    

class PatchTaskResponseRecordsItemCompletenessCondition(Enum):
    """ Specifies how to determine task completeness """
    
    Simple = 'Simple'
    AllAssignees = 'AllAssignees'
    Percentage = 'Percentage'

class PatchTaskResponseRecordsItemColor(Enum):
    """ Font color of a post with the current task """
    
    Black = 'Black'
    Red = 'Red'
    Orange = 'Orange'
    Yellow = 'Yellow'
    Green = 'Green'
    Blue = 'Blue'
    Purple = 'Purple'
    Magenta = 'Magenta'

class PatchTaskResponseRecordsItemRecurrenceSchedule(Enum):
    """ Task recurrence settings. For non-periodic tasks the value is 'None' """
    
    None_ = 'None'
    Daily = 'Daily'
    Weekdays = 'Weekdays'
    Weekly = 'Weekly'
    Monthly = 'Monthly'
    Yearly = 'Yearly'

class PatchTaskResponseRecordsItemRecurrenceEndingCondition(Enum):
    """ Task ending condition """
    
    None_ = 'None'
    Count = 'Count'
    Date = 'Date'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class PatchTaskResponseRecordsItemRecurrence(DataClassJsonMixin):
    schedule: Optional[PatchTaskResponseRecordsItemRecurrenceSchedule] = None
    """ Task recurrence settings. For non-periodic tasks the value is 'None' """
    
    ending_condition: Optional[PatchTaskResponseRecordsItemRecurrenceEndingCondition] = None
    """ Task ending condition """
    
    ending_after: Optional[int] = None
    """ Count of iterations of periodic tasks """
    
    ending_on: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """ End date of periodic task """
    

class PatchTaskResponseRecordsItemAttachmentsItemType(Enum):
    """ Attachment type (currently only `File` value is supported). """
    
    File = 'File'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class PatchTaskResponseRecordsItemAttachmentsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a file """
    
    type: Optional[PatchTaskResponseRecordsItemAttachmentsItemType] = None
    """ Attachment type (currently only `File` value is supported). """
    
    name: Optional[str] = None
    """ Name of the attached file (including extension name). """
    
    content_uri: Optional[str] = None
    """ Link to an attachment content """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class PatchTaskResponseRecordsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a task """
    
    creation_time: Optional[str] = None
    """ Datetime of the task creation in UTC time zone. """
    
    last_modified_time: Optional[str] = None
    """ Datetime of the last modification of the task in UTC time zone. """
    
    type: Optional[PatchTaskResponseRecordsItemType] = None
    """ Type of a task """
    
    creator: Optional[PatchTaskResponseRecordsItemCreator] = None
    chat_ids: Optional[List[str]] = None
    """ Chat IDs where the task is posted or shared. """
    
    status: Optional[PatchTaskResponseRecordsItemStatus] = None
    """ Status of task execution """
    
    subject: Optional[str] = None
    """ Name/subject of a task """
    
    assignees: Optional[List[PatchTaskResponseRecordsItemAssigneesItem]] = None
    completeness_condition: Optional[PatchTaskResponseRecordsItemCompletenessCondition] = None
    """ Specifies how to determine task completeness """
    
    completeness_percentage: Optional[int] = None
    """
    Current completeness percentage of the task with the specified percentage completeness
    condition
    """
    
    start_date: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """ Task start date """
    
    due_date: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """ Task due date/time """
    
    color: Optional[PatchTaskResponseRecordsItemColor] = None
    """ Font color of a post with the current task """
    
    section: Optional[str] = None
    """ Task section to group/search by """
    
    description: Optional[str] = None
    """ Task details """
    
    recurrence: Optional[PatchTaskResponseRecordsItemRecurrence] = None
    attachments: Optional[List[PatchTaskResponseRecordsItemAttachmentsItem]] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class PatchTaskResponse(DataClassJsonMixin):
    records: Optional[List[PatchTaskResponseRecordsItem]] = None

class CompleteTaskRequestStatus(Enum):
    """
    Completeness status. 'Mandatory' if `completenessCondition` is set to `Simple`, otherwise
    'Optional'
    
    Generated by Python OpenAPI Parser
    """
    
    Incomplete = 'Incomplete'
    Complete = 'Complete'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CompleteTaskRequestAssigneesItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of an assignee """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CompleteTaskRequest(DataClassJsonMixin):
    status: Optional[CompleteTaskRequestStatus] = None
    """
    Completeness status. 'Mandatory' if `completenessCondition` is set to `Simple`, otherwise
    'Optional'
    """
    
    assignees: Optional[List[CompleteTaskRequestAssigneesItem]] = None
    completeness_percentage: Optional[int] = None
    """
    Current completeness percentage of a task with the 'Percentage' completeness condition.
    'Mandatory' if `completenessCondition` is set to `Percentage`, otherwise 'Optional'
    """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadGlipPersonResponse(DataClassJsonMixin):
    """
    Required Properties:
     - id
    
    Generated by Python OpenAPI Parser
    """
    
    id: str
    """ Internal identifier of a user """
    
    first_name: Optional[str] = None
    """ First name of a user """
    
    last_name: Optional[str] = None
    """ Last name of a user """
    
    email: Optional[str] = None
    """ Email of a user """
    
    avatar: Optional[str] = None
    """ Photo of a user """
    
    company_id: Optional[str] = None
    """ Internal identifier of a company """
    
    creation_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """ Time of creation in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format """
    
    last_modified_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """ Time of the last modification in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadGlipCompanyResponse(DataClassJsonMixin):
    """
    Required Properties:
     - id
     - creation_time
     - last_modified_time
    
    Generated by Python OpenAPI Parser
    """
    
    id: str
    """
    Internal identifier of an RC account/Glip company, or tilde (~) to indicate a company the
    current user belongs to
    """
    
    creation_time: str
    """ Datetime of creation in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format """
    
    last_modified_time: str
    """ Datetime of last modification in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format """
    
    name: Optional[str] = None
    """ Name of a company """
    
    domain: Optional[str] = None
    """ Domain name of a company """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadGlipCompanyResponse(DataClassJsonMixin):
    """
    Required Properties:
     - id
     - creation_time
     - last_modified_time
    
    Generated by Python OpenAPI Parser
    """
    
    id: str
    """
    Internal identifier of an RC account/Glip company, or tilde (~) to indicate a company the
    current user belongs to
    """
    
    creation_time: str
    """ Datetime of creation in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format """
    
    last_modified_time: str
    """ Datetime of last modification in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format """
    
    name: Optional[str] = None
    """ Name of a company """
    
    domain: Optional[str] = None
    """ Domain name of a company """
    

class ListGlipGroupWebhooksResponseRecordsItemStatus(Enum):
    """ Current status of a webhook """
    
    Active = 'Active'
    Suspended = 'Suspended'
    Deleted = 'Deleted'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListGlipGroupWebhooksResponseRecordsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a webhook """
    
    creator_id: Optional[str] = None
    """ Internal identifier of the user who created a webhook """
    
    group_ids: Optional[List[str]] = None
    """ Internal identifiers of groups where a webhook has been created """
    
    creation_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """ Webhook creation time in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format """
    
    last_modified_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """ Webhook last update time in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format """
    
    uri: Optional[str] = None
    """ Public link to send a webhook payload """
    
    status: Optional[ListGlipGroupWebhooksResponseRecordsItemStatus] = None
    """ Current status of a webhook """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListGlipGroupWebhooksResponse(DataClassJsonMixin):
    records: Optional[List[ListGlipGroupWebhooksResponseRecordsItem]] = None

class CreateGlipGroupWebhookResponseStatus(Enum):
    """ Current status of a webhook """
    
    Active = 'Active'
    Suspended = 'Suspended'
    Deleted = 'Deleted'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateGlipGroupWebhookResponse(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a webhook """
    
    creator_id: Optional[str] = None
    """ Internal identifier of the user who created a webhook """
    
    group_ids: Optional[List[str]] = None
    """ Internal identifiers of groups where a webhook has been created """
    
    creation_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """ Webhook creation time in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format """
    
    last_modified_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """ Webhook last update time in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format """
    
    uri: Optional[str] = None
    """ Public link to send a webhook payload """
    
    status: Optional[CreateGlipGroupWebhookResponseStatus] = None
    """ Current status of a webhook """
    

class ListGlipWebhooksResponseRecordsItemStatus(Enum):
    """ Current status of a webhook """
    
    Active = 'Active'
    Suspended = 'Suspended'
    Deleted = 'Deleted'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListGlipWebhooksResponseRecordsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a webhook """
    
    creator_id: Optional[str] = None
    """ Internal identifier of the user who created a webhook """
    
    group_ids: Optional[List[str]] = None
    """ Internal identifiers of groups where a webhook has been created """
    
    creation_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """ Webhook creation time in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format """
    
    last_modified_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """ Webhook last update time in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format """
    
    uri: Optional[str] = None
    """ Public link to send a webhook payload """
    
    status: Optional[ListGlipWebhooksResponseRecordsItemStatus] = None
    """ Current status of a webhook """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListGlipWebhooksResponse(DataClassJsonMixin):
    records: Optional[List[ListGlipWebhooksResponseRecordsItem]] = None

class ListGlipWebhooksResponseRecordsItemStatus(Enum):
    """ Current status of a webhook """
    
    Active = 'Active'
    Suspended = 'Suspended'
    Deleted = 'Deleted'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListGlipWebhooksResponseRecordsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a webhook """
    
    creator_id: Optional[str] = None
    """ Internal identifier of the user who created a webhook """
    
    group_ids: Optional[List[str]] = None
    """ Internal identifiers of groups where a webhook has been created """
    
    creation_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """ Webhook creation time in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format """
    
    last_modified_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """ Webhook last update time in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format """
    
    uri: Optional[str] = None
    """ Public link to send a webhook payload """
    
    status: Optional[ListGlipWebhooksResponseRecordsItemStatus] = None
    """ Current status of a webhook """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListGlipWebhooksResponse(DataClassJsonMixin):
    records: Optional[List[ListGlipWebhooksResponseRecordsItem]] = None

class ReadGlipWebhookResponseRecordsItemStatus(Enum):
    """ Current status of a webhook """
    
    Active = 'Active'
    Suspended = 'Suspended'
    Deleted = 'Deleted'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadGlipWebhookResponseRecordsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a webhook """
    
    creator_id: Optional[str] = None
    """ Internal identifier of the user who created a webhook """
    
    group_ids: Optional[List[str]] = None
    """ Internal identifiers of groups where a webhook has been created """
    
    creation_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """ Webhook creation time in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format """
    
    last_modified_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """ Webhook last update time in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format """
    
    uri: Optional[str] = None
    """ Public link to send a webhook payload """
    
    status: Optional[ReadGlipWebhookResponseRecordsItemStatus] = None
    """ Current status of a webhook """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadGlipWebhookResponse(DataClassJsonMixin):
    records: Optional[List[ReadGlipWebhookResponseRecordsItem]] = None

class ReadGlipPreferencesResponseChatsLeftRailMode(Enum):
    SeparateAllChatTypes = 'SeparateAllChatTypes'
    SeparateConversationsAndTeams = 'SeparateConversationsAndTeams'
    CombineAllChatTypes = 'CombineAllChatTypes'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadGlipPreferencesResponseChats(DataClassJsonMixin):
    max_count: Optional[int] = 10
    left_rail_mode: Optional[ReadGlipPreferencesResponseChatsLeftRailMode] = 'CombineAllChatTypes'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadGlipPreferencesResponse(DataClassJsonMixin):
    chats: Optional[ReadGlipPreferencesResponseChats] = None

class ListGlipGroupsType(Enum):
    Group = 'Group'
    Team = 'Team'
    PrivateChat = 'PrivateChat'
    PersonalChat = 'PersonalChat'

class ListGlipGroupsResponseRecordsItemType(Enum):
    """
    Type of a group. 'PrivateChat' is a group of 2 members. 'Group' is a chat of 2 and more
    participants, the membership cannot be changed after group creation. 'Team' is a chat of 1 and
    more participants, the membership can be modified in future. 'PersonalChat' is a private chat
    thread of a user
    
    Generated by Python OpenAPI Parser
    """
    
    PrivateChat = 'PrivateChat'
    Group = 'Group'
    Team = 'Team'
    PersonalChat = 'PersonalChat'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListGlipGroupsResponseRecordsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a group """
    
    type: Optional[ListGlipGroupsResponseRecordsItemType] = None
    """
    Type of a group. 'PrivateChat' is a group of 2 members. 'Group' is a chat of 2 and more
    participants, the membership cannot be changed after group creation. 'Team' is a chat of 1 and
    more participants, the membership can be modified in future. 'PersonalChat' is a private chat
    thread of a user
    """
    
    is_public: Optional[bool] = None
    """ For 'Team' group type only. Team access level """
    
    name: Optional[str] = None
    """ For 'Team' group type only. Team name """
    
    description: Optional[str] = None
    """ For 'Team' group type only. Team description """
    
    members: Optional[List[str]] = None
    """ “List of glip members” """
    
    creation_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """ Group creation datetime in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format """
    
    last_modified_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """ Group last change datetime in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListGlipGroupsResponseNavigation(DataClassJsonMixin):
    prev_page_token: Optional[str] = None
    """
    Previous page token. To get previous page, user should pass one of returned token in next
    request and, in turn, required page will be returned with new tokens
    """
    
    next_page_token: Optional[str] = None
    """
    Next page token. To get next page, user should pass one of returned token in next request and,
    in turn, required page will be returned with new tokens
    """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListGlipGroupsResponse(DataClassJsonMixin):
    """
    Required Properties:
     - records
    
    Generated by Python OpenAPI Parser
    """
    
    records: List[ListGlipGroupsResponseRecordsItem]
    """ List of groups/teams/private chats """
    
    navigation: Optional[ListGlipGroupsResponseNavigation] = None

class CreateGlipGroupRequestType(Enum):
    """
    Type of a group to be created. 'PrivateChat' is a group of 2 members. 'Team' is a chat of 1 and
    more participants, the membership can be modified in future. 'PersonalChat' is a private chat
    thread of a user
    
    Generated by Python OpenAPI Parser
    """
    
    PrivateChat = 'PrivateChat'
    Team = 'Team'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateGlipGroupRequestMembersItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a user """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateGlipGroupRequest(DataClassJsonMixin):
    """
    Required Properties:
     - type
    
    Generated by Python OpenAPI Parser
    """
    
    type: CreateGlipGroupRequestType
    """
    Type of a group to be created. 'PrivateChat' is a group of 2 members. 'Team' is a chat of 1 and
    more participants, the membership can be modified in future. 'PersonalChat' is a private chat
    thread of a user
    """
    
    is_public: Optional[bool] = None
    """ For 'Team' group type only. Team access level """
    
    name: Optional[str] = None
    """ For 'Team' group type only. Team name """
    
    description: Optional[str] = None
    """ For 'Team' group type only. Team description """
    
    members: Optional[List[CreateGlipGroupRequestMembersItem]] = None
    """ “List of glip members. For 'PrivateChat' group type 2 members only are supported” """
    

class CreateGlipGroupResponseType(Enum):
    """
    Type of a group. 'PrivateChat' is a group of 2 members. 'Group' is a chat of 2 and more
    participants, the membership cannot be changed after group creation. 'Team' is a chat of 1 and
    more participants, the membership can be modified in future. 'PersonalChat' is a private chat
    thread of a user
    
    Generated by Python OpenAPI Parser
    """
    
    PrivateChat = 'PrivateChat'
    Group = 'Group'
    Team = 'Team'
    PersonalChat = 'PersonalChat'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateGlipGroupResponse(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a group """
    
    type: Optional[CreateGlipGroupResponseType] = None
    """
    Type of a group. 'PrivateChat' is a group of 2 members. 'Group' is a chat of 2 and more
    participants, the membership cannot be changed after group creation. 'Team' is a chat of 1 and
    more participants, the membership can be modified in future. 'PersonalChat' is a private chat
    thread of a user
    """
    
    is_public: Optional[bool] = None
    """ For 'Team' group type only. Team access level """
    
    name: Optional[str] = None
    """ For 'Team' group type only. Team name """
    
    description: Optional[str] = None
    """ For 'Team' group type only. Team description """
    
    members: Optional[List[str]] = None
    """ “List of glip members” """
    
    creation_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """ Group creation datetime in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format """
    
    last_modified_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """ Group last change datetime in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format """
    

class ReadGlipGroupResponseType(Enum):
    """
    Type of a group. 'PrivateChat' is a group of 2 members. 'Group' is a chat of 2 and more
    participants, the membership cannot be changed after group creation. 'Team' is a chat of 1 and
    more participants, the membership can be modified in future. 'PersonalChat' is a private chat
    thread of a user
    
    Generated by Python OpenAPI Parser
    """
    
    PrivateChat = 'PrivateChat'
    Group = 'Group'
    Team = 'Team'
    PersonalChat = 'PersonalChat'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadGlipGroupResponse(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a group """
    
    type: Optional[ReadGlipGroupResponseType] = None
    """
    Type of a group. 'PrivateChat' is a group of 2 members. 'Group' is a chat of 2 and more
    participants, the membership cannot be changed after group creation. 'Team' is a chat of 1 and
    more participants, the membership can be modified in future. 'PersonalChat' is a private chat
    thread of a user
    """
    
    is_public: Optional[bool] = None
    """ For 'Team' group type only. Team access level """
    
    name: Optional[str] = None
    """ For 'Team' group type only. Team name """
    
    description: Optional[str] = None
    """ For 'Team' group type only. Team description """
    
    members: Optional[List[str]] = None
    """ “List of glip members” """
    
    creation_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """ Group creation datetime in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format """
    
    last_modified_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """ Group last change datetime in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format """
    

class ReadGlipGroupResponseType(Enum):
    """
    Type of a group. 'PrivateChat' is a group of 2 members. 'Group' is a chat of 2 and more
    participants, the membership cannot be changed after group creation. 'Team' is a chat of 1 and
    more participants, the membership can be modified in future. 'PersonalChat' is a private chat
    thread of a user
    
    Generated by Python OpenAPI Parser
    """
    
    PrivateChat = 'PrivateChat'
    Group = 'Group'
    Team = 'Team'
    PersonalChat = 'PersonalChat'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ReadGlipGroupResponse(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a group """
    
    type: Optional[ReadGlipGroupResponseType] = None
    """
    Type of a group. 'PrivateChat' is a group of 2 members. 'Group' is a chat of 2 and more
    participants, the membership cannot be changed after group creation. 'Team' is a chat of 1 and
    more participants, the membership can be modified in future. 'PersonalChat' is a private chat
    thread of a user
    """
    
    is_public: Optional[bool] = None
    """ For 'Team' group type only. Team access level """
    
    name: Optional[str] = None
    """ For 'Team' group type only. Team name """
    
    description: Optional[str] = None
    """ For 'Team' group type only. Team description """
    
    members: Optional[List[str]] = None
    """ “List of glip members” """
    
    creation_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """ Group creation datetime in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format """
    
    last_modified_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """ Group last change datetime in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class AssignGlipGroupMembersRequest(DataClassJsonMixin):
    added_person_ids: Optional[List[str]] = None
    """ List of users to be added to a team """
    
    added_person_emails: Optional[List[str]] = None
    """ List of user email addresses to be added to a team (i.e. as guests) """
    
    removed_person_ids: Optional[List[str]] = None
    """ List of users to be removed from a team """
    

class AssignGlipGroupMembersResponseType(Enum):
    """
    Type of a group. 'PrivateChat' is a group of 2 members. 'Group' is a chat of 2 and more
    participants, the membership cannot be changed after group creation. 'Team' is a chat of 1 and
    more participants, the membership can be modified in future. 'PersonalChat' is a private chat
    thread of a user
    
    Generated by Python OpenAPI Parser
    """
    
    PrivateChat = 'PrivateChat'
    Group = 'Group'
    Team = 'Team'
    PersonalChat = 'PersonalChat'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class AssignGlipGroupMembersResponse(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a group """
    
    type: Optional[AssignGlipGroupMembersResponseType] = None
    """
    Type of a group. 'PrivateChat' is a group of 2 members. 'Group' is a chat of 2 and more
    participants, the membership cannot be changed after group creation. 'Team' is a chat of 1 and
    more participants, the membership can be modified in future. 'PersonalChat' is a private chat
    thread of a user
    """
    
    is_public: Optional[bool] = None
    """ For 'Team' group type only. Team access level """
    
    name: Optional[str] = None
    """ For 'Team' group type only. Team name """
    
    description: Optional[str] = None
    """ For 'Team' group type only. Team description """
    
    members: Optional[List[str]] = None
    """ “List of glip members” """
    
    creation_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """ Group creation datetime in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format """
    
    last_modified_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """ Group last change datetime in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format """
    

class ListGlipPostsResponseRecordsItemType(Enum):
    """ Type of a post """
    
    TextMessage = 'TextMessage'
    PersonJoined = 'PersonJoined'
    PersonsAdded = 'PersonsAdded'

class ListGlipPostsResponseRecordsItemAttachmentsItemType(Enum):
    """ Type of an attachment """
    
    Card = 'Card'
    Event = 'Event'
    Note = 'Note'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListGlipPostsResponseRecordsItemAttachmentsItemAuthor(DataClassJsonMixin):
    """ Information about the author """
    
    name: Optional[str] = None
    """ Name of a message author """
    
    uri: Optional[str] = None
    """ Link to an author's name """
    
    icon_uri: Optional[str] = None
    """ Link to an image displayed to the left of an author's name; sized 82x82px """
    

class ListGlipPostsResponseRecordsItemAttachmentsItemFieldsItemStyle(Enum):
    """ Style of width span applied to a field """
    
    Short = 'Short'
    Long = 'Long'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListGlipPostsResponseRecordsItemAttachmentsItemFieldsItem(DataClassJsonMixin):
    title: Optional[str] = None
    """ Title of an individual field """
    
    value: Optional[str] = None
    """ Value of an individual field (supports Markdown) """
    
    style: Optional[ListGlipPostsResponseRecordsItemAttachmentsItemFieldsItemStyle] = 'Short'
    """ Style of width span applied to a field """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListGlipPostsResponseRecordsItemAttachmentsItemFootnote(DataClassJsonMixin):
    """ Message Footer """
    
    text: Optional[str] = None
    """ Text of a footer """
    
    icon_uri: Optional[str] = None
    """ Link to an icon displayed to the left of a footer; sized 32x32px """
    
    time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """
    Message creation datetime in ISO 8601 format including timezone, for example
    *2016-03-10T18:07:52.534Z*
    """
    

class ListGlipPostsResponseRecordsItemAttachmentsItemRecurrence(Enum):
    """ Event recurrence settings. """
    
    None_ = 'None'
    Day = 'Day'
    Weekday = 'Weekday'
    Week = 'Week'
    Month = 'Month'
    Year = 'Year'

class ListGlipPostsResponseRecordsItemAttachmentsItemEndingOn(Enum):
    """ Iterations end datetime for periodic events """
    
    None_ = 'None'
    Count = 'Count'
    Date = 'Date'

class ListGlipPostsResponseRecordsItemAttachmentsItemColor(Enum):
    """
    Color of Event title, including its presentation in Calendar; or the color of the side border
    of an interactive message of a Card
    
    Generated by Python OpenAPI Parser
    """
    
    Black = 'Black'
    Red = 'Red'
    Orange = 'Orange'
    Yellow = 'Yellow'
    Green = 'Green'
    Blue = 'Blue'
    Purple = 'Purple'
    Magenta = 'Magenta'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListGlipPostsResponseRecordsItemAttachmentsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of an attachment """
    
    type: Optional[ListGlipPostsResponseRecordsItemAttachmentsItemType] = 'Card'
    """ Type of an attachment """
    
    fallback: Optional[str] = None
    """
    A string of default text that will be rendered in the case that the client does not support
    Interactive Messages
    """
    
    intro: Optional[str] = None
    """ A pretext to the message """
    
    author: Optional[ListGlipPostsResponseRecordsItemAttachmentsItemAuthor] = None
    """ Information about the author """
    
    title: Optional[str] = None
    """ Message title """
    
    text: Optional[str] = None
    """
    A large string field (up to 1000 chars) to be displayed as the body of a message (Supports
    GlipDown)
    """
    
    image_uri: Optional[str] = None
    """ Link to an image displayed at the bottom of a message """
    
    thumbnail_uri: Optional[str] = None
    """ Link to an image preview displayed to the right of a message (82x82) """
    
    fields: Optional[List[ListGlipPostsResponseRecordsItemAttachmentsItemFieldsItem]] = None
    """ Information on navigation """
    
    footnote: Optional[ListGlipPostsResponseRecordsItemAttachmentsItemFootnote] = None
    """ Message Footer """
    
    creator_id: Optional[str] = None
    """ Internal identifier of a person created an event """
    
    start_time: Optional[str] = None
    """ Datetime of starting an event """
    
    end_time: Optional[str] = None
    """ Datetime of ending an event """
    
    all_day: Optional[bool] = False
    """ Indicates whether an event has some specific time slot or lasts for the whole day(s) """
    
    recurrence: Optional[ListGlipPostsResponseRecordsItemAttachmentsItemRecurrence] = None
    """ Event recurrence settings. """
    
    ending_condition: Optional[str] = None
    """ Condition of ending """
    
    ending_after: Optional[int] = None
    """ Count of iterations. For periodic events only """
    
    ending_on: Optional[ListGlipPostsResponseRecordsItemAttachmentsItemEndingOn] = 'None'
    """ Iterations end datetime for periodic events """
    
    color: Optional[ListGlipPostsResponseRecordsItemAttachmentsItemColor] = 'Black'
    """
    Color of Event title, including its presentation in Calendar; or the color of the side border
    of an interactive message of a Card
    """
    
    location: Optional[str] = None
    """ Event location """
    
    description: Optional[str] = None
    """ Event details """
    

class ListGlipPostsResponseRecordsItemMentionsItemType(Enum):
    """ Type of mentions """
    
    Person = 'Person'
    Team = 'Team'
    File = 'File'
    Link = 'Link'
    Event = 'Event'
    Task = 'Task'
    Note = 'Note'
    Card = 'Card'

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListGlipPostsResponseRecordsItemMentionsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a user """
    
    type: Optional[ListGlipPostsResponseRecordsItemMentionsItemType] = None
    """ Type of mentions """
    
    name: Optional[str] = None
    """ Name of a user """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListGlipPostsResponseRecordsItem(DataClassJsonMixin):
    id: Optional[str] = None
    """ Internal identifier of a post """
    
    group_id: Optional[str] = None
    """ Internal identifier of a group a post belongs to """
    
    type: Optional[ListGlipPostsResponseRecordsItemType] = None
    """ Type of a post """
    
    text: Optional[str] = None
    """ For 'TextMessage' post type only. Text of a message """
    
    creator_id: Optional[str] = None
    """ Internal identifier of a user - author of a post """
    
    added_person_ids: Optional[List[str]] = None
    """ For 'PersonsAdded' post type only. Identifiers of persons added to a group """
    
    creation_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """ Post creation datetime in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format """
    
    last_modified_time: Optional[datetime] = field(metadata=config(encoder=datetime.isoformat, decoder=datetime_decoder(datetime)), default=None)
    """ Post last modification datetime in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format """
    
    attachments: Optional[List[ListGlipPostsResponseRecordsItemAttachmentsItem]] = None
    """ List of posted attachments """
    
    mentions: Optional[List[ListGlipPostsResponseRecordsItemMentionsItem]] = None
    activity: Optional[str] = None
    """ Label of activity type """
    
    title: Optional[str] = None
    """ Title of a message. (Can be set for bot's messages only) """
    
    icon_uri: Optional[str] = None
    """ Link to an image used as an icon for this message """
    
    icon_emoji: Optional[str] = None
    """ Emoji used as an icon for this message """
    
