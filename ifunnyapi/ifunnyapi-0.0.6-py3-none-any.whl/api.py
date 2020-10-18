import base64
import hashlib
import io
import json
from PIL import Image, UnidentifiedImageError
import requests
from time import sleep
import uuid
from typing import Generator, List, Union
from .auth import AuthBearer
from .exceptions import APIError
from .utils import api_request


class _iFunnyBaseAPI:
    """Private API class, only interacts with iFunny API endpoints"""

    BASE = "https://api.ifunny.mobi/v4"

    def __init__(self, token: str):
        self.token = token
        self.auth = AuthBearer(self.token)

    @api_request
    def _get(self, path: str, **kwargs) -> dict:
        """GET request with authorization"""

        r = requests.get(iFunnyAPI.BASE + path, auth=self.auth, **kwargs)
        return r.json()

    @api_request
    def _post(self, path: str, **kwargs) -> dict:
        """POST request with authorization"""

        r = requests.post(iFunnyAPI.BASE + path, auth=self.auth, **kwargs)
        return r.json()

    @api_request
    def _put(self, path: str, **kwargs) -> dict:
        """PUT request with authorization"""

        r = requests.put(iFunnyAPI.BASE + path, auth=self.auth, **kwargs)
        return r.json()

    @api_request
    def _delete(self, path: str, **kwargs) -> dict:
        """DELETE request with authorization"""

        r = requests.delete(iFunnyAPI.BASE + path, auth=self.auth, **kwargs)
        return r.json()

    @property
    def account(self) -> dict:
        """"""

        r = self._get("/account")
        return r["data"]

    def _get_paging_items(
            self,
            path: str,
            key: str,
            limit: int = None,
            **kwargs
    ) -> List[dict]:
        """"""

        def get_next(r: dict) -> int:
            return r["data"][key]["paging"]["cursors"]["next"]

        def has_next(r: dict) -> bool:
            return r["data"][key]["paging"]["hasNext"]

        def get_items(r: dict) -> list:
            return r["data"][key]["items"]

        lnone = limit is None
        ilim = 100 if lnone or limit > 100 else limit
        urlparams = "&".join(f"{k}={v}" for k, v in kwargs.items())
        batch = self._get(f"{path}?limit={ilim}{urlparams}")
        items = get_items(batch)

        if not lnone and limit <= 100:
            return items

        if not lnone:
            val, rem = divmod(limit - 100, 100)

        nexturl = f"{path}?limit=100&next={get_next(batch)}{urlparams}"
        lbuffer = 0  # Significant only when limit is not None
        while has_next(batch) if lnone else lbuffer in range(val):
            lbuffer += 1
            batch = self._get(nexturl)
            items.extend(get_items(batch))
            nexturl = f"{path}?limit=100&next={get_next(batch)}{urlparams}"

        if lnone:
            nexturl = f"{path}?limit=100&next={get_next(batch)}{urlparams}"
        else:
            nexturl = f"{path}?limit={rem}{urlparams}"

        batch = self._get(nexturl)
        items.extend(get_items(batch))
        return items

    def my_activity(
            self,
            limit: int = None,
            **kwargs
    ) -> List[dict]:
        """"""

        return self._get_paging_items(
            f"/news/my",
            "news",
            limit,
            **kwargs
        )

    def my_comments(
            self,
            limit: int = None,
            **kwargs
    ) -> List[dict]:
        """"""

        return self._get_paging_items(
            f"/users/my/comments",
            "comments",
            limit,
            **kwargs
        )

    def user_subscribers(
            self,
            *,
            user_id: str,
            limit: int = None,
            **kwargs
    ) -> List[dict]:
        """"""

        return self._get_paging_items(
            f"/users/{user_id}/subscribers",
            "users",
            limit,
            **kwargs
        )

    def user_subscriptions(
            self,
            *,
            user_id: str,
            limit: int = None,
            **kwargs
    ) -> List[dict]:
        """"""

        return self._get_paging_items(
            f"/users/{user_id}/subscriptions",
            "users",
            limit,
            **kwargs
        )

    def user_posts(
            self,
            *,
            user_id: str,
            limit: int = None,
            **kwargs
    ) -> List[dict]:
        """"""

        return self._get_paging_items(
            f"/timelines/users/{user_id}",
            "content",
            limit,
            **kwargs
        )

    def user_features(
            self,
            *,
            user_id: str,
            limit: int = None,
            **kwargs
    ) -> List[dict]:
        """"""

        return self._get_paging_items(
            f"/timelines/users/{user_id}/featured",
            "content",
            limit,
            **kwargs
        )

    def user_guests(
            self,
            *,
            user_id: str,
            limit: int = None,
            **kwargs
    ) -> List[dict]:
        """"""

        return self._get_paging_items(
            f"/users/{user_id}/guests",
            "guests",
            limit,
            **kwargs
        )

    def tag_posts(
            self,
            *,
            tag: str,
            limit: int = None,
            **kwargs
    ) -> List[dict]:
        """"""

        return self._get_paging_items(
            f"/search/content",
            "content",
            limit,
            counters="content",
            tag=tag,
            **kwargs
        )

    def post_comments(
            self,
            *,
            post_id: str,
            limit: int = None,
            **kwargs
    ) -> List[dict]:
        """"""

        return self._get_paging_items(
            f"/content/{post_id}/comments",
            "comments",
            limit,
            **kwargs
        )

    def comment_replies(
            self,
            *,
            post_id: str,
            comment_id: str,
            limit: int = None,
            **kwargs
    ) -> List[dict]:
        """"""

        return self._get_paging_items(
            f"/content/{post_id}/comments/{comment_id}/replies",
            "replies",
            limit,
            **kwargs
        )

    def featured(
            self,
            limit: int = None,
            read: bool = True
    ) -> Generator[dict, None, None]:
        """"""

        iterator = iter(int, 1) if limit is None else range(limit)
        for _ in iterator:
            r = self._get("/feeds/featured?limit=1")
            feat = r["data"]["content"]["items"]
            if not len(feat):
                feat = next(self.featured(limit=1))
            feat = feat[0]
            if read:
                self._put(
                    f"/reads/{feat['id']}?from=feat",
                    headers={"User-Agent": "*"}
                )
            yield feat

    def collective(
            self,
            limit: int = None
    ) -> Generator[dict, None, None]:
        """"""

        iterator = iter(int, 1) if limit is None else range(limit)
        for _ in iterator:
            r = self._post("/feeds/collective?limit=1")
            coll = r["data"]["content"]["items"]
            if not len(coll):
                coll = next(self.collective(limit=1))
            coll = coll[0]
            yield coll

    def subscriptions(
            self,
            limit: int = None,
            read: bool = True
    ) -> Generator[dict, None, None]:
        """"""

        iterator = iter(int, 1) if limit is None else range(limit)
        for _ in iterator:
            r = self._get("/timelines/home?limit=1")
            subscr = r["data"]["content"]["items"]
            if not len(subscr):
                subscr = next(self.subscriptions(limit=1))
            subscr = subscr[0]
            if read:
                self._put(
                    f"/reads/{subscr['id']}?from=subs",
                    headers={"User-Agent": "*"}
                )
            yield subscr

    def popular(
            self,
            limit: int = None
    ) -> Generator[dict, None, None]:
        """"""

        iterator = iter(int, 1) if limit is None else range(limit)
        for _ in iterator:
            r = self._get("/feeds/popular?limit=1")
            pop = r["data"]["content"]["items"]
            if not len(pop):
                pop = next(self.popular(limit=1))
            pop = pop[0]
            yield pop

    def upload(
            self,
            media: Union[bytes, str],
            description: str = None,
            tags: list = None,
            public: bool = True
    ):
        """"""

        media = media if type(media) is bytes else open(media, "rb").read()
        try:
            im = Image.open(io.BytesIO(media))
        except UnidentifiedImageError:
            mtype = "video_clip"
            ftype = "video"
        else:
            mtype = "gif" if im.format == "GIF" else "pic"
            ftype = "image"
        self._post(
            "/content",
            data={"description": description or "",
                  "tags": json.dumps(tags or []),
                  "type": mtype,
                  "visibility": "public" if public else "subscribers"},
            files={ftype: media}
        )

    def block(self, *, user_id: str, blockall: bool = False):
        """"""

        self._put(
            f"/users/my/blocked/{user_id}",
            data={"type": "installation" if blockall else "user"}
        )

    def unblock(self, *, user_id: str, unblockall: bool = False):
        """"""

        self._delete(
            f"/users/my/blocked/{user_id}",
            data={"type": "installation" if unblockall else "user"}
        )

    def comment(self, comment: str, *, post_id: str):
        """"""

        self._post(
            f"/content/{post_id}/comments?from=feat",
            data={"text": comment}
        )

    def reply(self, reply: str, *, post_id: str, comment_id: str):
        """"""

        self._post(
            f"/content/{post_id}/comments/{comment_id}/replies",
            data={"text": reply}
        )

    def smile_post(self, *, post_id: str):
        """"""

        self._put(f"/content/{post_id}/smiles?from=feat")

    def unsmile_post(self, *, post_id: str):
        """"""

        self._delete(f"/content/{post_id}/smiles?from=feat")

    def delete_post(self, *, post_id: str):
        """"""

        self._delete(f"/content/{post_id}")

    def smile_comment(self, *, post_id: str, comment_id: str):
        """"""

        self._put(f"/content/{post_id}/comments/{comment_id}/smiles")

    def unsmile_comment(self, *, post_id: str, comment_id: str):
        """"""

        self._delete(f"/content/{post_id}/comments/{comment_id}/smiles")

    def delete_comment(self, *, post_id: str, comment_id: str):
        """"""

        self._delete(f"/content/{post_id}/comments/{comment_id}")

    def user_by_nick(self, nick: str) -> dict:
        """"""

        return self._get(f"/users/by_nick/{nick}")["data"]

    def is_nick_available(self, nick: str):
        """"""

        j = self._get(f"/users/nicks_available?nick={nick}")
        return j["data"]["available"]

    def is_email_available(self, email: str) -> bool:
        """"""

        j = self._get(f"/users/emails_available?email={email}")
        return j["data"]["available"]


class iFunnyAPI(_iFunnyBaseAPI):
    """Public API class, includes extra features"""

    CLIENTID = "JuiUH&3822"
    CLIENTSEC = "HuUIC(ZQ918lkl*7"

    @classmethod
    def basic_token(cls) -> str:
        """"""

        hexstr = str(uuid.uuid4()).encode("utf-8").hex().upper()
        hid = hexstr + "_" + cls.CLIENTID
        hashdec = hexstr + ":" + cls.CLIENTID + ":" + cls.CLIENTSEC
        hashenc = hashlib.sha1(hashdec.encode("utf-8")).hexdigest()
        btoken = base64.b64encode(bytes(hid + ":" + hashenc, "utf-8")).decode()
        return btoken

    @classmethod
    def _req_auth(cls, btoken: str, email: str, password: str) -> dict:
        """"""

        r = requests.post(
            cls.BASE + "/oauth2/token",
            headers={"Authorization": "Basic " + btoken},
            data={"grant_type": "password",
                  "username": email,
                  "password": password}
        )
        return r.json()

    @classmethod
    def from_creds(cls, email: str, password: str, primer: int = 10):
        """"""

        btoken = cls.basic_token()
        cls._req_auth(btoken, email, password)  # Primer request
        sleep(primer)
        r = cls._req_auth(btoken, email, password)
        if "error" in r:
            raise APIError(r["status"], r["error_description"])
        token = r["access_token"]
        return cls(token)

    @classmethod
    def generate_account(
            cls,
            email: str,
            nick: str,
            password: str,
            accepted_mailing: bool = False
    ):
        """"""

        raise NotImplementedError("generate_account is not yet implemented")
        # btoken = cls.basic_token()
        # r = requests.post(
        #     cls.BASE.replace("v4", "v3") + "/users",
        #     headers={"Authorization": "Basic " + btoken},
        #     data={"accepted_mailing": int(accepted_mailing),
        #           "email": email,
        #           "nick": nick,
        #           "password": password,
        #           "reg_type": "pwd"}
        # )
        # print(r.json())

    @staticmethod
    def crop_ifunny_watermark(im: Image) -> Image:
        """"""

        w, h = im.size
        return im.crop((0, 0, w, h - 20))
