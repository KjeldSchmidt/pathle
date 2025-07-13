from enum import Enum


class Pf2eAreaType(Enum):
    burst = "burst"
    cone = "cone"
    cube = "cube"
    cylinder = "cylinder"
    emanation = "emanation"
    line = "line"
    square = "square"


class Pf2eSaveType(Enum):
    reflex = "reflex"
    will = "will"
    fortitude = "fortitude"

    reflex_dc = "reflex-dc"
    will_dc = "will-dc"
    fortitude_dc = "fortitude-dc"

    ac = "ac"


class Pf2eRarity(Enum):
    uncommon = "uncommon"
    common = "common"
    rare = "rare"
    unique = "unique"


class Pf2eTradition(Enum):
    arcane = "arcane"
    primal = "primal"
    divine = "divine"
    occult = "occult"


class Pf2eTraits(Enum):
    acid = "acid"
    air = "air"
    animist = "animist"
    attack = "attack"
    auditory = "auditory"
    aura = "aura"
    bard = "bard"
    beast = "beast"
    cantrip = "cantrip"
    champion = "champion"
    chaotic = "chaotic"
    cleric = "cleric"
    cold = "cold"
    composition = "composition"
    concentrate = "concentrate"
    conjuration = "conjuration"
    consecration = "consecration"
    contingency = "contingency"
    curse = "curse"
    custom = "custom"
    darkness = "darkness"
    death = "death"
    detection = "detection"
    disease = "disease"
    divination = "divination"
    dream = "dream"
    druid = "druid"
    earth = "earth"
    eidolon = "eidolon"
    electricity = "electricity"
    emotion = "emotion"
    enchantment = "enchantment"
    evil = "evil"
    evocation = "evocation"
    exploration = "exploration"
    extradimensional = "extradimensional"
    fear = "fear"
    fire = "fire"
    focus = "focus"
    force = "force"
    fortune = "fortune"
    fungus = "fungus"
    good = "good"
    healing = "healing"
    hex = "hex"
    holy = "holy"
    illusion = "illusion"
    incapacitation = "incapacitation"
    incarnate = "incarnate"
    incorporeal = "incorporeal"
    lawful = "lawful"
    light = "light"
    linguistic = "linguistic"
    magus = "magus"
    manipulate = "manipulate"
    mental = "mental"
    metal = "metal"
    misfortune = "misfortune"
    monk = "monk"
    morph = "morph"
    move = "move"
    mythic = "mythic"
    necromancy = "necromancy"
    nonlethal = "nonlethal"
    olfactory = "olfactory"
    oracle = "oracle"
    plant = "plant"
    poison = "poison"
    polymorph = "polymorph"
    possession = "possession"
    prediction = "prediction"
    psychic = "psychic"
    ranger = "ranger"
    revelation = "revelation"
    sanctified = "sanctified"
    scrying = "scrying"
    shadow = "shadow"
    sleep = "sleep"
    sonic = "sonic"
    sorcerer = "sorcerer"
    spellshape = "spellshape"
    spirit = "spirit"
    stance = "stance"
    structure = "structure"
    subtle = "subtle"
    summon = "summon"
    summoner = "summoner"
    teleportation = "teleportation"
    transmutation = "transmutation"
    trial = "trial"
    true_name = "true-name"
    unholy = "unholy"
    unique = "unique"
    visual = "visual"
    vitality = "vitality"
    void = "void"
    water = "water"
    witch = "witch"
    wizard = "wizard"
    wood = "wood"
    cursebound = "cursebound"


class Pf2eDamageType(Enum):
    acid = "acid"
    bleed = "bleed"
    bludgeoning = "bludgeoning"
    cold = "cold"
    electricity = "electricity"
    fire = "fire"
    force = "force"
    poison = "poison"
    spirit = "spirit"
    void = "void"
    mental = "mental"
    piercing = "piercing"
    slashing = "slashing"
    sonic = "sonic"
    untyped = "untyped"
    vitality = "vitality"


class Pf2eSpellRange(Enum):
    self = "self"
    touch = "touch"

    varies = "varies"
    speed_half = "half your speed"
    speed = "your speed"

    feet_5 = "5 feet"
    feet_10 = "10 feet"
    feet_15 = "15 feet"
    feet_20 = "20 feet"
    feet_30 = "30 feet"
    feet_40 = "40 feet"
    feet_50 = "50 feet"
    feet_60 = "60 feet"
    feet_70 = "70 feet"
    feet_80 = "80 feet"
    feet_90 = "90 feet"
    feet_100 = "100 feet"
    feet_120 = "120 feet"
    feet_150 = "150 feet"
    feet_240 = "240 feet"
    feet_250 = "250 feet"
    feet_500 = "500 feet"
    feet_800 = "800 feet"
    feet_1000 = "1000 feet"
    feet_2000 = "2000 feet"
    feet_2200 = "2200 feet"

    miles_half = "half a mile"
    miles_1 = "1 mile"
    miles_10 = "10 miles"
    miles_25 = "25 miles"
    miles_100 = "100 miles"
    miles_500 = "500 miles"
    miles_1000 = "1000 miles"

    planetary = "planetary"
    unlimited = "unlimited"

    interplanar = "interplanar"

class Pf2eSpellDuration(Enum):
    instant = "instantaneous"

    rounds_1 = "1 round"
    rounds_1_plus = "1 or more rounds"
    rounds_2 = "2 rounds"
    rounds_3 = "3 rounds"
    rounds_4 = "4 rounds"
    rounds_5 = "5 rounds"

    minutes_1 = "1 minute"
    minutes_5 = "5 minutes"
    minutes_10 = "10 minutes"
    minutes_20 = "20 minutes"

    hours_1 = "1 hour"
    hours_3 = "3 hours"
    hours_7 = "7 hours"
    hours_8 = "8 hours"

    hours_12 = "12 hours"
    until_midnight = "until midnight"

    days_1 = "1 day"
    days_3 = "3 days"
    days_5 = "5 days"
    days_7 = "7 days"
    days_14 = "14 days"

    months_1 = "1 month"

    years_1 = "1 year"

    unlimited = "unlimited"

    self_end_of_turn = "until the end of your turn"

    self_start_of_next_turn = "until the start of your next turn"
    self_end_of_next_turn = "until the end of your next turn"

    target_end_next_turn = "until the end of the target's next turn"

    self_next_daily_preparations = "until your next daily preparations"
    target_next_daily_preparations = "until the target's next daily preparations"

    until_condition_is_met = "until a condition is met"

    varies = "varies"

    @classmethod
    def _missing_(cls, value):
        if value == "":
            return cls.instant

        if isinstance(value, str):
            value = value.lower()
            value = value.replace("sustained up to ", "")
            value = value.replace("up to ", "")
            value = value.replace("(see text)", "")
            value = value.replace("(see below)", "")
            value = value.strip()

            if value == "24 hours":
                return cls.days_1

            if value == "1 week":
                return cls.days_7

            if value in [
                "until full tribute is paid",
                "until you leave the stance",
                "until the next time you refocus",
                "until the arcane cascade stance ends",
                "until the wager's completion",
            ]:
                return cls.until_condition_is_met

            for member in cls:
                if member.value == value:
                    return member
        return None
