from typing import List, Any

from pydantic import BaseModel, Field


class CategoryGetSuperCategoryRespSubcategories(BaseModel):
    subcid: int = Field(...)
    subcname: str = Field(...)
    scpic: str = Field(...)


class CategoryGetSuperCategoryResp(BaseModel):
    cid: int = Field(...)
    cname: str = Field(...)
    cpic: str = Field(...)
    subcategories: List[CategoryGetSuperCategoryRespSubcategories] = Field(...)


class GoodsPriceTrendRespList(BaseModel):
    id: int = Field(...)
    goodsId: str = Field(...)
    title: str = Field(...)
    dtitle: str = Field(...)
    originalPrice: float = Field(...)
    actualPrice: float = Field(...)
    shopType: int = Field(...)
    goldSellers: int = Field(...)
    monthSales: int = Field(...)
    twoHoursSales: int = Field(...)
    dailySales: int = Field(...)
    commissionType: int = Field(...)
    desc: str = Field(...)
    couponReceiveNum: int = Field(...)
    couponLink: str = Field(...)
    couponEndTime: str = Field(...)
    couponStartTime: str = Field(...)
    couponPrice: float = Field(...)
    couponConditions: str = Field(...)
    activityType: int = Field(...)
    createTime: str = Field(...)
    mainPic: str = Field(...)
    marketingMainPic: str = Field(...)
    sellerId: str = Field(...)
    cid: int = Field(...)
    discounts: float = Field(...)
    commissionRate: float = Field(...)
    couponTotalNum: int = Field(...)
    haitao: int = Field(...)
    activityStartTime: str = Field(...)
    activityEndTime: str = Field(...)
    shopName: str = Field(...)
    shopLevel: int = Field(...)
    descScore: float = Field(...)
    brand: int = Field(...)
    brandId: int = Field(...)
    brandName: str = Field(...)
    hotPush: int = Field(...)
    teamName: str = Field(...)
    itemLink: str = Field(...)
    tchaoshi: int = Field(...)
    dsrScore: float = Field(...)
    dsrPercent: float = Field(...)
    shipScore: float = Field(...)
    shipPercent: float = Field(...)
    serviceScore: float = Field(...)
    servicePercent: float = Field(...)
    subcid: list = Field(...)
    quanMLink: int = Field(...)
    hzQuanOver: int = Field(...)
    yunfeixian: int = Field(...)
    estimateAmount: int = Field(...)
    freeshipRemoteDistrict: int = Field(...)
    tbcid: int = Field(...)


class GoodsPriceTrendResp(BaseModel):
    list: List[GoodsPriceTrendRespList] = Field(...)
    totalNum: int = Field(...)
    pageId: str = Field(...)


class GoodsGetRankingListResp(BaseModel):
    id: int = Field(...)
    goodsId: str = Field(...)
    ranking: int = Field(...)
    dtitle: str = Field(...)
    actualPrice: float = Field(...)
    commissionRate: float = Field(...)
    couponPrice: float = Field(...)
    couponReceiveNum: int = Field(...)
    couponTotalNum: int = Field(...)
    monthSales: int = Field(...)
    twoHoursSales: int = Field(...)
    dailySales: int = Field(...)
    hotPush: int = Field(...)
    mainPic: str = Field(...)
    title: str = Field(...)
    desc: str = Field(...)
    originalPrice: float = Field(...)
    couponLink: str = Field(...)
    couponStartTime: str = Field(...)
    couponEndTime: str = Field(...)
    commissionType: int = Field(...)
    createTime: str = Field(...)
    activityType: int = Field(...)
    imgs: str = Field(...)
    guideName: str = Field(...)
    shopType: int = Field(...)
    couponConditions: str = Field(...)
    newRankingGoods: int = Field(...)
    sellerId: str = Field(...)
    quanMLink: int = Field(...)
    hzQuanOver: int = Field(...)
    yunfeixian: int = Field(...)
    estimateAmount: int = Field(...)
    freeshipRemoteDistrict: int = Field(...)


class GoodsGetGoodsDetailsResp(BaseModel):
    id: int = Field(...)
    goodsId: str = Field(...)
    title: str = Field(...)
    dtitle: str = Field(...)
    originalPrice: float = Field(...)
    actualPrice: float = Field(...)
    shopType: int = Field(...)
    goldSellers: int = Field(...)
    monthSales: int = Field(...)
    twoHoursSales: int = Field(...)
    dailySales: int = Field(...)
    commissionType: int = Field(...)
    desc: str = Field(...)
    couponReceiveNum: int = Field(...)
    couponLink: str = Field(...)
    couponEndTime: str = Field(...)
    couponStartTime: str = Field(...)
    couponPrice: float = Field(...)
    couponConditions: str = Field(...)
    activityType: int = Field(...)
    createTime: str = Field(...)
    mainPic: str = Field(...)
    marketingMainPic: str = Field(...)
    sellerId: str = Field(...)
    cid: int = Field(...)
    discounts: float = Field(...)
    commissionRate: float = Field(...)
    couponTotalNum: int = Field(...)
    haitao: int = Field(...)
    activityStartTime: str = Field(...)
    activityEndTime: str = Field(...)
    shopName: str = Field(...)
    shopLevel: int = Field(...)
    descScore: float = Field(...)
    brand: int = Field(...)
    brandId: int = Field(...)
    brandName: str = Field(...)
    hotPush: int = Field(...)
    teamName: str = Field(...)
    itemLink: str = Field(...)
    tchaoshi: int = Field(...)
    dsrScore: float = Field(...)
    dsrPercent: float = Field(...)
    shipScore: float = Field(...)
    shipPercent: float = Field(...)
    serviceScore: float = Field(...)
    servicePercent: float = Field(...)
    subcid: list = Field(...)
    imgs: str = Field(...)
    reimgs: str = Field(...)
    quanMLink: int = Field(...)
    hzQuanOver: int = Field(...)
    yunfeixian: int = Field(...)
    estimateAmount: int = Field(...)
    shopLogo: str = Field(...)
    specialText: list = Field(...)
    freeshipRemoteDistrict: int = Field(...)
    video: str = Field(...)
    detailPics: str = Field(...)
    tbcid: int = Field(...)


class TbServiceGetBrandListRespShop(BaseModel):
    name: str = Field(...)
    sellerId: str = Field(...)


class TbServiceGetBrandListResp(BaseModel):
    brandId: int = Field(...)
    brandName: str = Field(...)
    brandLogo: str = Field(...)
    brandEnglish: str = Field(...)
    shop: List[TbServiceGetBrandListRespShop] = Field(...)
    brandScore: int = Field(...)
    location: str = Field(...)
    establishTime: str = Field(...)
    belongTo: str = Field(...)
    position: str = Field(...)
    consumer: str = Field(...)
    label: str = Field(...)
    simpleLabel: str = Field(...)
    cids: str = Field(...)


class GoodsNineOpGoodsListRespList(BaseModel):
    id: int = Field(...)
    goodsId: str = Field(...)
    title: str = Field(...)
    dtitle: str = Field(...)
    originalPrice: float = Field(...)
    actualPrice: float = Field(...)
    shopType: int = Field(...)
    goldSellers: int = Field(...)
    monthSales: int = Field(...)
    twoHoursSales: int = Field(...)
    dailySales: int = Field(...)
    commissionType: int = Field(...)
    desc: str = Field(...)
    couponReceiveNum: int = Field(...)
    couponLink: str = Field(...)
    couponEndTime: str = Field(...)
    couponStartTime: str = Field(...)
    couponPrice: float = Field(...)
    couponConditions: str = Field(...)
    activityType: int = Field(...)
    createTime: str = Field(...)
    mainPic: str = Field(...)
    marketingMainPic: str = Field(...)
    sellerId: str = Field(...)
    cid: int = Field(...)
    discounts: float = Field(...)
    commissionRate: float = Field(...)
    couponTotalNum: int = Field(...)
    haitao: int = Field(...)
    activityStartTime: str = Field(...)
    activityEndTime: str = Field(...)
    shopName: str = Field(...)
    shopLevel: int = Field(...)
    descScore: float = Field(...)
    brand: int = Field(...)
    brandId: int = Field(...)
    brandName: str = Field(...)
    hotPush: int = Field(...)
    teamName: str = Field(...)
    itemLink: str = Field(...)
    tchaoshi: int = Field(...)
    dsrScore: float = Field(...)
    dsrPercent: float = Field(...)
    shipScore: float = Field(...)
    shipPercent: float = Field(...)
    serviceScore: float = Field(...)
    servicePercent: float = Field(...)
    subcid: list = Field(...)
    nineCid: int = Field(...)
    quanMLink: int = Field(...)
    hzQuanOver: int = Field(...)
    yunfeixian: int = Field(...)
    estimateAmount: int = Field(...)
    freeshipRemoteDistrict: int = Field(...)
    video: str = Field(...)
    tbcid: int = Field(...)


class GoodsNineOpGoodsListResp(BaseModel):
    list: List[GoodsNineOpGoodsListRespList] = Field(...)
    totalNum: int = Field(...)
    pageId: str = Field(...)


CategoryDdqGoodsListResp = Any
CategoryGetTbTopicListResp = Any
CategoryGetTop100Resp = Any
GoodsActivityCatalogueResp = Any
GoodsActivityGoodsListResp = Any
GoodsExclusiveGoodsListResp = Any
GoodsExplosiveGoodsListResp = Any
GoodsFirstOrderGiftMoneyResp = Any
GoodsFriendsCircleListResp = Any
GoodsGetCollectionListResp = Any
GoodsGetGoodsListResp = Any
GoodsGetDtkSearchGoodsResp = Any
GoodsGetNewestGoodsResp = Any
GoodsGetOwnerGoodsResp = Any
GoodsGetStaleGoodsByTimeResp = Any
GoodsTopicCatalogueResp = Any
GoodsListSimilerGoodsByOpenResp = Any
GoodsListSuperGoodsResp = Any
GoodsLivematerialGoodsListResp = Any
GoodsPullGoodsByTimeResp = Any
GoodsSearchSuggestionResp = Any
GoodsTopicCatalogue = Any
GoodsTopicGoodsListResp = Any
TbServiceActivityLinkResp = Any
TbServiceCreatTaokoulingResp = Any
TbServiceGetOrderDetailsResp = Any
TbServiceGetPrivilegeLinkResp = Any
TbServiceGetTbServiceResp = Any
TbServiceParseContentResp = Any
TbServiceParseTaokoulingResp = Any
TbServiceTwdToTwdResp = Any
