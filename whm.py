import math

GLARE_POT = 300
DIA_POT = 120
DIA_DOT_POT = 60
ASSIZE_POT = 400
MISERY_POT = 900

CASTER_TAX = 0.1
LD_PER_MIN = 0.8
RES_PER_MIN = 0
C3_PER_MIN = 0.3
M2_PER_MIN = 1
CLIPS_PER_MIN = 1
NON_GLARE_IN_TA = 0


def main():
    for sps in range(0, 5000):
        x, y = gcd(action_delay=2500, sps=sps)
        print(sps, x, y)


# finalResult(sps, CASTER_TAX, C3_PER_MIN, M2_PER_MIN, RES_PER_MIN,NON_GLARE_IN_TA,CLIPS_PER_MIN)
def pps_whm(sps, caster_tax, c3_per_min, m2_per_min, res_per_min, non_glare_in_ta, clips_per_min):
    cycle = get_cycle(sps, caster_tax, clips_per_min)
    afflatus_t = afflatus_time(sps, cycle)
    cycle += afflatus_t
    return get_potency(sps, c3_per_min + m2_per_min + res_per_min + 0.5 * non_glare_in_ta, cycle) / cycle


# Actual time taken by a 270s rotation
def get_cycle(sps, caster_tax, clips):
    short_gcd = gcd(2500, sps, False)
    result = 0
    # 1 dia + x glares + 1 afflatus
    if (30 - short_gcd) % (short_gcd + caster_tax) > 1.5:
        result += 9 * (short_gcd + math.ceil((30 - short_gcd) / (short_gcd + caster_tax)) * (
                caster_tax + short_gcd) - caster_tax) + 3 * short_gcd
    else:
        result += 9 * (short_gcd + math.floor((30 - short_gcd) / (short_gcd + caster_tax)) * (
                caster_tax + short_gcd) - caster_tax) + 3 * short_gcd
    # POM as multiplier normalized over 300s
    result *= 300 / ((30 / 0.80) + 270)
    result += clips * 4.5 * 0.7
    return result


def afflatus_time(sps, cycle):
    return 3 * gcd(2500, sps, False) * (cycle / 270 - 1)


# Average potency of a 270s rotation
def get_potency(sps, filler, cycle):
    result = 0
    short_gcd = gcd(2500, sps, False)
    result += 6 * ASSIZE_POT * cycle / 270
    result += 3 * MISERY_POT * cycle / 270
    if (30 - short_gcd) % (short_gcd + 0.1) > 1.5:
        result += 9 * (math.ceil((30 - short_gcd) / (short_gcd + 0.1)) - 1) * GLARE_POT + 9 * DIA_POT
        result += 9 * 10 * ss_scalar(sps) * DIA_DOT_POT
    else:
        result += 9 * (math.floor((30 - short_gcd) / (short_gcd + 0.1)) - 1) * GLARE_POT + 9 * DIA_POT
        result += 9 * 9 * ss_scalar(sps) * DIA_DOT_POT
        result += 9 * ((3 - ((30 - short_gcd) % (short_gcd + 0.1))) / 3) * ss_scalar(sps) * DIA_DOT_POT
    result -= 4.5 * filler * GLARE_POT
    return result


def gcd(action_delay, sps, gcd_reduction=0):
    gcd_m = int(int(1000 - int(130 * (sps - 380) / 3300) * action_delay / 1000) * (100 - gcd_reduction) / 100 / 10)
    gcd_c = int(gcd_m * (100 - gcd_reduction) / 100 / 10)
    time = gcd_c / 100
    time2 = int(int(
        1000 * (100 - gcd_reduction) * (int(action_delay * (1000 - int(130 * (sps - 380) / 3300)) / 1000) / 1000)) / 1000) / 100

    return time, time2


def ss_scalar(ss):
    return (1000 + int(130 * (ss - 380) / 3300)) / 1000


def det_dmg(det):
    return int(130 * (det - 340) / 3300 + 1000) / 1000


def dh_rate(dh):
    return int(550 * (dh - 380) / 3300 + 0) / 1000


def crit_rate(crit):
    return int(200 * (crit - 380) / 3300 + 50) / 1000


def crit_dmg(crit):
    return int(200 * (crit - 380) / 3300 + 1400) / 1000


def ss_dmg(ss):
    return int(130 * (ss - 380) / 3300 + 1000) / 1000


def ten_dmg(tnc):
    return int(100 * (tnc - 380) / 3300 + 1000) / 1000


if __name__ == "__main__":
    main()
