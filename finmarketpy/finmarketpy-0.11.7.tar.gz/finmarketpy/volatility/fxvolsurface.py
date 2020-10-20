from financepy.market.curves.FinDiscountCurveFlat import FinDiscountCurveFlat
from financepy.market.volatility.FinFXVolSurface import FinFXVolSurface
from financepy.market.volatility.FinFXVolSurface import FinFXATMMethod
from financepy.market.volatility.FinFXVolSurface import FinFXDeltaMethod

from financepy.finutils.FinDate import FinDate

import datetime
from datetime import timedelta

class FXVolSurface(object):

    def __init__(self, market_df=None, tenors=['ON', '1W', '1M', '2M', '3M', '6M', '1Y', '2Y']):
        self._market_df = market_df
        self._tenors = tenors

        self._value_date = None
        self._fin_fx_vol_surface = None

    def build_vol_surface(self, value_date, asset=None, depo_tenor='1M', field='close', atm_method=FinFXATMMethod.FWD_DELTA_NEUTRAL,
        delta_method=FinFXDeltaMethod.SPOT_DELTA):

        value_date = self._parse_date(value_date)

        self._value_date = value_date

        value_fin_date = self._findate(self._parse_date(value_date))

        tenors = self._tenors

        # Change ON (overnight) to 1D (convention for financepy)
        # tenors_financepy = list(map(lambda b: b.replace("ON", "1D"), self._tenors.copy()))
        tenors_financepy = self._tenors.copy()
        market_df = self._market_df

        field = '.' + field

        for_name_base = asset[0:3]
        dom_name_terms = asset[3:6]

        date_index = market_df.index == value_date

        # CAREFUL: need to divide by 100 for depo rate, ie. 0.0346 = 3.46%
        forCCRate = market_df[for_name_base + depo_tenor + field][date_index].values[0] / 100.0 # 0.03460  # EUR
        domCCRate = market_df[dom_name_terms + depo_tenor + field][date_index].values[0] / 100.0 # 0.02940  # USD

        dom_discount_curve = FinDiscountCurveFlat(value_fin_date, domCCRate)
        for_discount_curve = FinDiscountCurveFlat(value_fin_date, forCCRate)

        currency_pair = for_name_base + dom_name_terms
        spot_fx_rate = market_df[currency_pair + field][date_index].values[0]

        # For vols we do NOT need to divide by 100 (financepy does that internally)
        atm_vols = market_df[[currency_pair + "V" + t + field for t in tenors]][date_index].values[0]
        market_strangle25DeltaVols = market_df[[currency_pair + "25B" + t + field for t in tenors]][date_index].values[0] #[0.65, 0.75, 0.85, 0.90, 0.95, 0.85]
        risk_reversal25DeltaVols = market_df[[currency_pair + "25R" + t + field for t in tenors]][date_index].values[0] #[-0.20, -0.25, -0.30, -0.50, -0.60, -0.562]

        notional_currency = for_name_base

        # Construct financepy vol surface (uses polynomial interpolation for determining vol between strikes)
        self._fin_fx_vol_surface = FinFXVolSurface(value_fin_date,
                                   spot_fx_rate,
                                   currency_pair,
                                   notional_currency,
                                   dom_discount_curve,
                                   for_discount_curve,
                                   tenors_financepy,
                                   atm_vols,
                                   market_strangle25DeltaVols,
                                   risk_reversal25DeltaVols,
                                   atm_method,
                                   delta_method)

        #fxMarket.checkCalibration()

        # fxMarket.plotVolCurves()

        # import matplotlib.pyplot as plt
        # plt.show()

    def calculate_vol_for_strike_expiry(self, K, date):
        tenor_index = None
        return self._fin_fx_vol_surface.volFunction(self, K, tenor_index)
        #
        # TODO

    def _get_tenor_index(self, tenor):
        return self._tenors.find(tenor)

    def get_atm_strike(self, tenor=None):
        return self._fin_fx_vol_surface._K_ATM[self._get_tenor_index(tenor)]

    def get_25d_call_strike(self, tenor=None):
        return self._fin_fx_vol_surface._K_25_D_C[self._get_tenor_index(tenor)]

    def get_25d_put_strike(self, tenor=None):
        return self._fin_fx_vol_surface._K_25_D_P[self._get_tenor_index(tenor)]

    def get_10d_call_strike(self, tenor=None):
        pass

    def get_10d_put_strike(self, tenor=None):
        pass

    def get_25d_call_ms_strike(self, tenor=None):
        return self._fin_fx_vol_surface._K_25_D_C_MS[self._get_tenor_index(tenor)]

    def get_25d_put_ms_strike(self, tenor=None):
        return self._fin_fx_vol_surface._K_25_D_P_MS[self._get_tenor_index(tenor)]

    def get_10d_call_ms_strike(self, expiry_date=None, tenor=None):
        pass

    def get_10d_put_ms_strike(self, expiry_date=None, tenor=None):
        pass


    def get_atm_vol(self, expiry_date=None, tenor=None):
        pass

    def get_25d_call_vol(self, expiry_date=None, tenor=None):
        pass

    def get_25d_put_vol(self, expiry_date=None, tenor=None):
        pass

    def get_10d_call_vol(self, expiry_date=None, tenor=None):
        pass

    def get_10d_put_vol(self, expiry_date=None, tenor=None):
        pass

    def plot_vol_curves(self):
        if self._fin_fx_vol_surface is not None:
    # fxMarket.checkCalibration()
            self._fin_fx_vol_surface.plotVolCurves()

            #import matplotlib.pyplot as plt
            #plt.show()

    def _parse_date(self, date):
        if isinstance(date, str):

            date1 = datetime.datetime.utcnow()

            if date is 'midnight':
                date1 = datetime.datetime(date1.year, date1.month, date1.day, 0, 0, 0)
            elif date is 'decade':
                date1 = date1 - timedelta(days=365 * 10)
            elif date is 'year':
                date1 = date1 - timedelta(days=365)
            elif date is 'month':
                date1 = date1 - timedelta(days=30)
            elif date is 'week':
                date1 = date1 - timedelta(days=7)
            elif date is 'day':
                date1 = date1 - timedelta(days=1)
            elif date is 'hour':
                date1 = date1 - timedelta(hours=1)
            else:
                # format expected 'Jun 1 2005 01:33', '%b %d %Y %H:%M'
                try:
                    date1 = datetime.datetime.strptime(date, '%b %d %Y %H:%M')
                except:
                    # ogger.warning("Attempted to parse date")
                    i = 0

                # format expected '1 Jun 2005 01:33', '%d %b %Y %H:%M'
                try:
                    date1 = datetime.datetime.strptime(date, '%d %b %Y %H:%M')
                except:
                    # logger.warning("Attempted to parse date")
                    i = 0

                try:
                    date1 = datetime.datetime.strptime(date, '%b %d %Y')
                except:
                    # logger.warning("Attempted to parse date")
                    i = 0

                try:
                    date1 = datetime.datetime.strptime(date, '%d %b %Y')
                except:
                    # logger.warning("Attempted to parse date")
                    i = 0
        else:
            date1 = pd.Timestamp(date)

        return pd.Timestamp(date1)

    def _findate(self, date):
        return FinDate(date.day, date.month, date.year)

if __name__ == '__main__':
    from findatapy.market import Market, MarketDataRequest, MarketDataGenerator

    ticker = 'EURUSD'
    start_date = '06 Oct 2020'
    md_request = MarketDataRequest(start_date=start_date, finish_date=start_date, data_source='bloomberg', cut='LDN', category='fx-vol-market',
                                   tickers=ticker)

    import os
    import pandas as pd

    if os.path.exists(ticker + '.parquet'):
        market_df = pd.read_parquet(ticker + '.parquet')
    else:
        market_df = Market(market_data_generator=MarketDataGenerator()).fetch_market(md_request)

        market_df.to_parquet(ticker + '.parquet')

    fx_vol_surface = FXVolSurface(market_df=market_df)

    fx_vol_surface.build_vol_surface(start_date, asset='EURUSD')