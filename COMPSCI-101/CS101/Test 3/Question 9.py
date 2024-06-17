def metric_to_imperial(kilos):
    grams = kilos * 1000
    ounce = grams / 28.349523125
    pound = ounce / 16
    stone = pound / 14.

    stone = pound // 14
    remaining_pound = pound % 14




metric_to_imperial(10.1)