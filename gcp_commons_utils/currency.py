"""Currency formats."""

from decimal import Decimal


def currency_format(num, curr="$", neg="-", pos=None):
    """Format the number to currency style."""
    if not isinstance(num, (int, float, Decimal)):
        return ""
    magnitude = 0
    neg_symbol = ""
    if num < 0:
        num = abs(num)
        neg_symbol = neg
    elif num > 0 and pos is not None:
        neg_symbol = pos

    if num <= 999999:
        return f"{neg_symbol}{curr}" + "{:0,.0f}".format(num)
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0

    num = "{:0,.15f}".format(num)
    return "{neg_symbol}{curr}{number}{magnitude}".format(
        neg_symbol=neg_symbol,
        curr=curr,
        number=num[:-13],
        magnitude=["", "K", "M", "B", "T", "P"][magnitude],
    )
