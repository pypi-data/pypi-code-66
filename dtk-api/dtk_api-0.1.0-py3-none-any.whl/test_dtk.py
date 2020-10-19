import os

import pytest

from .gen import DtkSync, GoodsNineOpGoodsListArgs, DtkAsync


def test_demo():
    assert 1 == 1


def get_app_key_and_secret() -> (str, str):
    app_key = os.getenv("DTK_APP_KEY")
    app_secret = os.getenv("DTK_APP_SECRET")
    print(f"{app_key=}")
    print(f"{app_secret=}")
    return app_key, app_secret


def test_simple():
    app_key, app_secret = get_app_key_and_secret()
    args = GoodsNineOpGoodsListArgs(pageId=1, pageSize=10, nineCid=2)
    dtk = DtkSync(app_key=app_key, app_secret=app_secret)
    ret = dtk.goods_nine_op_goods_list(args=args)
    print(ret)


@pytest.mark.asyncio
async def test_async_simple():
    app_key, app_secret = get_app_key_and_secret()
    args = GoodsNineOpGoodsListArgs(pageId=1, pageSize=10, nineCid=2)
    dtk = DtkAsync(app_key=app_key, app_secret=app_secret)
    ret = await dtk.goods_nine_op_goods_list(args=args)
    print(ret)
