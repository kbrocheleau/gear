import csv

# Party buff things
BATTLE_VOICE_AVG = (20 / 180) * 0.2
BATTLE_LITANY_AVG = (20 / 180) * 0.1
CHAIN_STRAT_AVG = (15 / 120) * 0.1
DEVILMENT_AVG = (20 / 120) * 0.2
BRD_CRIT_AVG = (30 / 80) * 0.02
BRD_DH_AVG = (20 / 80) * 0.03

# Traits and eno
MAGIC_AND_MEND = 1.3
ENOCHIAN = 1.15

MAX_STAT = 10000
DET_DMG = [0] * MAX_STAT
DH_RATE = [0] * MAX_STAT
CRIT_RATE = [0] * MAX_STAT
CRIT_DMG = [0] * MAX_STAT
SS_DMG = [0] * MAX_STAT
TEN_DMG = [0] * MAX_STAT

for stat in range(0, 10000):
    DET_DMG[stat] = int(130 * (stat - 340) / 3300 + 1000) / 1000
    DH_RATE[stat] = int(550 * (stat - 380) / 3300 + 0) / 1000
    CRIT_RATE[stat] = int(200 * (stat - 380) / 3300 + 50) / 1000
    CRIT_DMG[stat] = int(200 * (stat - 380) / 3300 + 1400) / 1000
    SS_DMG[stat] = int(130 * (stat - 380) / 3300 + 1000) / 1000
    TEN_DMG = int(100 * (stat-380) / 3300 + 1000) / 1000

def main():
    sets = []
    with open('sets.csv', encoding='utf-8') as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            row = list(map(int, row))
            sets.append(row)
    f.close()
    for row in sets:
        print(row)
    print(damage(215.199837813373, 172, 115, 4867, 1915, 528, 2974, 380, 380, False, False, False, False, 5))

def damage2(potency, weapon_damage, job_mod, main_stat, Det, Crit, DH, SS, TEN, hasBrd, hasDrg, hasSch, hasDnc,
           classNum):
    main_stat = int(main_stat * (1 + 0.01 * classNum))
    dmg = int(potency * (weapon_damage + int(340 * job_mod / 1000)) * (100 + int((main_stat - 340) * 165 / 340)) / 100)
    dmg =
# Pulled from Orinx's Gear Comparison Sheet with slight modifications
def damage(potency, weapon_damage, job_mod, main_stat, Det, Crit, DH, SS, TEN, hasBrd, hasDrg, hasSch, hasDnc,
           classNum):
    main_stat = int(main_stat * (1 + 0.01 * classNum))
    dmg = int(potency * (weapon_damage + int(340 * job_mod / 1000)) * (100 + int((main_stat - 340) * 165 / 340)) / 100)
    dmg = int(dmg * (1000 + int(130 * (Det - 340) / 3300)) / 1000)
    dmg = int(dmg * (1000 + int(100 * (TEN - 380) / 3300)) / 1000)
    dmg = int(dmg * (1000 + int(130 * (SS - 380) / 3300)) / 1000 / 100)
    dmg = int(dmg * MAGIC_AND_MEND)
    dmg = int(dmg * ENOCHIAN)
    CritDamage = int(dmg * (1000 * CalcCritDamage(Crit)) / 1000)
    DHDamage = int(dmg * 1250 / 1000)
    CritDHDamage = int(CritDamage * 1250 / 1000)
    CritRate = (CalcCritRate(Crit)
                + (hasDrg * BATTLE_LITANY_AVG)
                + (hasSch * CHAIN_STRAT_AVG)
                + (hasDnc * DEVILMENT_AVG)
                + (hasBrd * BRD_CRIT_AVG)
                )
    DHRate = CalcDHRate(DH) + (hasBrd * (BATTLE_VOICE_AVG + BRD_DH_AVG)) + (hasDnc * DEVILMENT_AVG)
    CritDHRate = CritRate * DHRate
    NormalRate = 1 - CritRate - DHRate + CritDHRate

    return dmg * NormalRate + CritDamage * (CritRate - CritDHRate) + DHDamage * (
            DHRate - CritDHRate) + CritDHDamage * CritDHRate


def CalcCritRate(Crit):
    return int((200 * (Crit - 380) / 3300 + 50)) / 1000


def CalcCritDamage(Crit):
    return (1000 + int(200 * (Crit - 380) / 3300 + 400)) / 1000


def CalcDHRate(DH):
    return int(550 * (DH - 380) / 3300) / 1000


def CalcDetDamage(Det):
    return (1000 + int(130 * (Det - 340) / 3300)) / 1000


def CalcDamage(Potency, Multiplier, CritDamageMult, CritRate, DHRate):
    Damage = Potency * Multiplier
    DHDamage = 1.25 * Damage
    CritDamage = CritDamageMult * Damage
    CritDHDamage = CritDamageMult * 1.25 * Damage
    CritDHRate = CritRate * DHRate
    NormalRate = 1 - CritRate - DHRate + CritDHRate

    return Damage * NormalRate + CritDamage * (CritRate - CritDHRate) + DHDamage * (
            DHRate - CritDHRate) + CritDHDamage * CritDHRate


if __name__ == "__main__":
    main()
