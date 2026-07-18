"""
risk.py

Risk Management Module

Calculates:
- Lot size
- Stop Loss
- Take Profit
- Spread checks
- Open position limits
"""

import MetaTrader5 as mt5

from config import (
    SYMBOL,
    RISK_PER_TRADE,
    RISK_REWARD,
    ATR_SL_MULTIPLIER,
    MAX_SPREAD,
    MAX_OPEN_TRADES,
)


class RiskManager:

    def __init__(self):
        pass

    def account_balance(self):

        account = mt5.account_info()

        if account is None:
            raise Exception("Unable to read account information")

        return account.balance

    def current_spread(self):

        tick = mt5.symbol_info_tick(SYMBOL)

        symbol = mt5.symbol_info(SYMBOL)

        spread = (tick.ask - tick.bid) / symbol.point

        return spread

    def spread_ok(self):

        return self.current_spread() <= MAX_SPREAD

    def open_positions(self):

        positions = mt5.positions_get(symbol=SYMBOL)

        if positions is None:
            return 0

        return len(positions)

    def can_trade(self):

        return self.open_positions() < MAX_OPEN_TRADES

    def stop_loss_take_profit(self, signal, price, atr):

        distance = atr * ATR_SL_MULTIPLIER

        if signal == "BUY":

            sl = price - distance

            tp = price + (distance * RISK_REWARD)

        elif signal == "SELL":

            sl = price + distance

            tp = price - (distance * RISK_REWARD)

        else:

            return None, None

        return round(sl, 2), round(tp, 2)

    def lot_size(self, price, sl):

        balance = self.account_balance()

        risk_amount = balance * RISK_PER_TRADE

        stop_distance = abs(price - sl)

        if stop_distance <= 0:
            return 0.01

        symbol = mt5.symbol_info(SYMBOL)

        tick_value = symbol.trade_tick_value

        tick_size = symbol.trade_tick_size

        value_per_point = tick_value / tick_size

        volume = risk_amount / (stop_distance * value_per_point)

        volume = max(symbol.volume_min, volume)

        volume = min(symbol.volume_max, volume)

        step = symbol.volume_step

        volume = round(volume / step) * step

        return round(volume, 2)
