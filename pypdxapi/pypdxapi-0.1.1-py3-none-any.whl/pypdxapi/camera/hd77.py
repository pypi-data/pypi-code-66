""" Python implementation of Paradox HD77 camera."""
import logging
from typing import Any, List
from datetime import datetime

from .camera import ParadoxCamera

_LOGGER = logging.getLogger(__name__)


class ParadoxHD77(ParadoxCamera):
    """

    """

    def __init__(self, host: str, port: int, module_password: str, **kwargs) -> None:
        """ Constructs a :class:`ParadoxHD77 <ParadoxHD77>`.

        :param host: (required) The IP address of your Paradox camera.
        :param port: (required) The port of your Paradox camera.
        :param module_password: (required) The module password. The default value is usually
            paradox.
        :param client_session: (optional) aiohttp.ClientSession for performing HTTP requests.
             If not provided, a new one will be created and later destroyed.
        :param request_timeout: (optional) Request timeout. Default is 10sec.
        :param user_agent: (optional) HTTP user agent. Default is "PyPdxApi/" + Package_Version.
        :param raise_on_result_code_error: (optional) Raise exception on invalid result code.
            Default is false.
        """
        super().__init__(host=host, port=port, module_password=module_password, **kwargs)

    @staticmethod
    def _client_datetime() -> str:
        """ Return current datetime in timestamp """
        return str(datetime.now().timestamp())

    async def login(self, usercode: str, username: str) -> dict:
        """ Logs the user into the camera and obtains the camera data such as: series, version,
        model and name.
        It also stores the session key for access to other functions that require authentication.
        This session key will expire if not used in 2 minutes.

        :param usercode: (required) User code on the panel.
        :param username: (required) User name on the panel.
        :return: JSON data from camera
        """
        payload = {
            "DeviceID": '',
            "ClientDateTime": self._client_datetime(),
            "CPUserId": 1,
            "UserCode": usercode,
            "DeveloperKey": self._developer_key,
            "ServerPassword": self._module_password,
            "UserName": username
        }
        self._session_key = None

        data = self._parse_response(
            await self.api_request('POST', endpoint='/app/login', payload=payload),
            result_code=33554432
        )

        if data['ResultCode'] == 33554432:
            self._name = data['Server']['Label'].strip()
            self._model = 'HD77'
            self._serial = data['Server']['SerialNo'].strip()
            self._version = data['Server']['SdCardVersion'].strip()
            self._session_key = data['sessionKey']

        return data

    async def logout(self) -> dict:
        """
        Set session_key to None so you will not be able to make calls that require authentication.

        :return: JSON data from camera
        """
        payload = {
            "ClientDateTime": self._client_datetime(),
            "SessionKey": self._session_key
        }
        self._session_key = None

        return await self.api_request('POST', endpoint='/app/logout', payload=payload)

    async def pingstatus(self) -> dict:
        """ Get some info from camera and panel. This not require login.

        :return: JSON data from camera
        """
        payload = {
            "DeveloperKey": self._developer_key,
            "ClientDateTime": self._client_datetime(),
            "ServerPassword": self._module_password,
        }

        return self._parse_response(
            await self.api_request('POST', endpoint='/app/pingstatus', payload=payload),
            result_code=35127296
        )

    async def getstatus(self, status_type: int, keep_alive: bool = False) -> dict:
        """ Get more info from camera and panel like zones, areas, status, etc...

        :param status_type: (required) It can be 1, 2, or 3. Each one returns a type of information.
        :param keep_alive: (optional) I still don't know what it's for.
        :return: JSON data from camera
        """
        payload = {
            "ClientDateTime": self._client_datetime(),
            "StatusType": status_type,
            "SessionKey": self._session_key,
            "keepAlive": keep_alive
        }

        return self._parse_response(
            await self.api_request('POST', endpoint='/app/getstatus', payload=payload),
            result_code=33619968
        )

    async def rod(self, action: int = 3) -> dict:
        """ Command recording on demand (ROD).

        :param action: (optional)
            3 -> Start
            4 -> Stop
        :return: JSON data from camera
        """
        payload = {
            "ClientDateTime": self._client_datetime(),
            "Action": action,
            "SessionKey": self._session_key,
            "RecResolution": 720
        }

        return self._parse_response(
            await self.api_request('POST', endpoint='/app/rod', payload=payload),
            result_code=33816578
        )

    async def areacontrol(self, area_commands: List[dict]) -> dict:
        """ Control Areas.

        :param area_commands: (required) Command.
            [
                {
                    "AreaID": Area number
                    "AreaCommand":
                        2 -> regular arm
                        3 -> stay arm
                        4 -> instant arm
                        5 -> force arm
                        6 -> disarm
                    "ForceZones": True/False
                }
            ]
        :return: JSON data from camera
        """
        payload = {
            "AreaCommands": area_commands,
            "ClientDateTime": self._client_datetime(),
            "SessionKey": self._session_key
        }

        return await self.api_request('POST', endpoint='/app/areacontrol', payload=payload)

    async def zonecontrol(self, zone_commands: List[dict]) -> dict:
        """ Control zones.

        :param zone_commands: (required) Command.
            [
                {
                    "ZoneID": Zone number
                    "ZoneCommand":
                        0 -> clear bypass
                        1 -> bypass
                }
            ]
        :return: JSON data from camera
        """
        payload = {
            "ZoneCommands": zone_commands,
            "ClientDateTime": self._client_datetime(),
            "SessionKey": self._session_key
        }

        return await self.api_request('POST', endpoint='/app/zonecontrol', payload=payload)

    async def pgmcontrol(self, pgm_commands: List[dict]) -> dict:
        """ Control PGMs.

        :param pgm_commands: (required) Command.
            [
                {
                    "PGMID": PGM number
                    "SerialNo": ?
                    "PGMCommand":
                        0 -> override on
                        1 -> override off
                        2 -> release on
                        3 -> release off
                }
            ]
        :return: JSON data from camera
        """
        payload = {
            "PGMCommands": pgm_commands,
            "ClientDateTime": self._client_datetime(),
            "SessionKey": self._session_key
        }

        return await self.api_request('POST', endpoint='/app/pgmcontrol', payload=payload)

    async def panic(self, panic_type: int) -> dict:
        """ Command recording on demand (ROD).

        :param panic_type: (required)
            1 -> police
            2 -> medical
            3 -> fire
        :return: JSON data from camera
        """
        payload = {
            "ClientDateTime": self._client_datetime(),
            "PanicType": panic_type,
            "SessionKey": self._session_key
        }

        return self._parse_response(
            await self.api_request('POST', endpoint='/app/panic', payload=payload),
            result_code=34799616
        )

    async def getitemlist(self, items_count: int = 150, direction: str = 'ascending',
                          order_by: str = 'date', item_index: int = 0) -> dict:
        """ Returns the list of files stored on the camera

        :param items_count: (optional) Max number of items to be returned. Default is 150
        :param direction: (optional) Sorting direction.
            ascending -> Ascending
            descending -> Descending
        :param order_by: (optional) Order by.
            date -> date
            name -> name
            type -> type
        :param item_index: (optional) Start index. Default is 0
        :return: JSON data from camera
        """
        payload = {
            "ClientDateTime": self._client_datetime(),
            "ItemsCount": items_count,
            "Direction": direction,
            "OrderBy": order_by,
            "SessionKey": self._session_key,
            "ItemIndex": item_index
        }

        return self._parse_response(
            await self.api_request('POST', endpoint='/fil/getitemlist', payload=payload),
            result_code=33882112
        )

    async def deleteitem(self, item_id: str) -> dict:
        """ Delete recording file

        :param item_id: (required) File id returned in getitemlist
        :return: JSON data from camera
        """
        payload = {
            "ItemId": item_id,
            "ClientDateTime": self._client_datetime(),
            "SessionKey": self._session_key,
        }

        return self._parse_response(
            await self.api_request('POST', endpoint='/fil/deleteitem', payload=payload),
            result_code=34144256
        )

    async def playback(self, item_id: str, action: int = 0) -> dict:
        """ Prepares the recording file to play and returns the url for access.

        :param item_id: (required) File id returned in getitemlist
        :param action: (optional)
            0 -> Play from begining
            1 -> Pause clip
            2 -> Set marker
            3 -> Next marker (pause only)
            4 -> Previous marker (pause only)
            5 -> Next frame (pause only)
            6 -> Previous frame (pause only)
        :return: JSON data from camera
        """
        payload = {
            "ClientDateTime": self._client_datetime(),
            "Action": action,
            "SessionKey": self._session_key,
            "ItemId": item_id
        }

        return self._parse_response(
            await self.api_request('POST', endpoint='/fil/playback', payload=payload),
            result_code=544210944
        )

    async def downloaditem(self, item_id: str, resolution: int = 720) -> dict:
        """ Delete recording file

        :param item_id: (required) File id returned in getitemlist
        :param resolution: (optional) Resolution
            360 -> 360px
            720 -> 720px

        :return: mp4 file.
        """
        payload = {
            "ItemId": item_id,
            "ItemResolution": resolution,
            "ClientDateTime": self._client_datetime(),
            "SessionKey": self._session_key,
        }
        return await self.api_request(
            'POST',
            endpoint='/fil/downloaditem',
            payload=payload,
            content_type='application/octet-stream'
        )

    async def getthumbnail(self) -> Any:
        """ Capture a thumbnail in real time.

        :return: JPEG Image
        """
        payload = {
            "ClientDateTime": self._client_datetime(),
            "SessionKey": self._session_key
        }

        return await self.api_request(
            'POST',
            endpoint='/fil/getthumbnail',
            payload=payload,
            content_type='application/octet-stream'
        )

    async def vod(self, channel_type: str = 'normal') -> Any:
        """ Request the video on demand and return an m3u8 file containing the access urls.

        :param channel_type: (optional) Video quality.
            low -> Low bit rate
            normal -> Normal bit rate
            high -> High bit rate
        :return: m3u8 file.
        """
        payload = {
            "ClientDateTime": self._client_datetime(),
            "Action": 1,
            "SessionKey": self._session_key,
            "ChannelType": channel_type,
        }

        return await self.api_request(
            'POST',
            endpoint='/hls/vod',
            payload=payload,
            content_type='audio/x-mpegURL'
        )
