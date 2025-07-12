from enum import Enum

from pydantic import BaseModel, ConfigDict, Field, field_validator


class ClosedModel(BaseModel):

    model_config = ConfigDict(extra="forbid")


class Pf2eAreaType(Enum):
    burst = "burst"
    cone = "cone"
    cube = "cube"
    cylinder = "cylinder"
    emanation = "emanation"
    line = "line"
    square = "square"

class FoundryArea(ClosedModel):
    area_type: Pf2eAreaType | None = Field(alias="areaType", default=None)
    type: Pf2eAreaType | None = None
    value: int
    details: str | None = None

    @field_validator("area_type", "type", mode="before")
    @classmethod
    def empty_string_to_none(cls, v):
        if v == "":
            return None
        return v

class SaveType(Enum):
    reflex = "reflex"
    will = "will"
    fortitude = "fortitude"

    reflex_dc = "reflex-dc"
    will_dc = "will-dc"
    fortitude_dc = "fortitude-dc"

    ac = "ac"


class FoundrySpellDefenseSave(ClosedModel):
    basic: bool | None = None
    statistic: SaveType

class FoundrySpellDefense(ClosedModel):
    save: FoundrySpellDefenseSave | None
    passive: FoundrySpellDefenseSave | None = None

class FoundrySpellLevel(ClosedModel):
    value: int

class FoundrySpellCost(ClosedModel):
    value: str

class FoundrySpellRules(ClosedModel):
    damage_type: str | None = Field(alias="damageType", default=None)
    dice_number: str | None = Field(alias="diceNumber", default=None)
    dieSize: str | None = Field(alias="dieSize", default=None)
    key: str
    predicate: list[str | dict[str, list[str]]]
    selector: str | None = None
    selectors: list[str] | None = None
    uuid: str | None = None
    mode: str | None = None
    property: str | None = None
    value: str | None = None
    slug: str | None = None
    hide_if_disabled: bool | None = Field(alias="hideIfDisabled", default=None)
    label: str | None = None
    option: str | None = None
    placement: str | None = None
    toggleable: bool | None = None
    item_id: str | None = Field(alias="itemId", default=None)
    suboptions: list[dict[str, str]] | None = None



class FoundryActionType(Enum):
    reaction = "reaction"


class FoundryTime(ClosedModel):
    value: FoundryActionType | str


class FoundrySpellTarget(ClosedModel):
    value: str


class FoundryRarity(Enum):
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


class Pf2eSpellDamageCategory(Enum):
    persistent = "persistent"
    splash = "splash"


class FoundrySpellDamageDetails(ClosedModel):
    applyMod: bool | None = None
    category: Pf2eSpellDamageCategory | None
    formula: str
    kinds: list[str] | None = None
    materials: list[str] | None = None
    type: Pf2eDamageType

    @field_validator("category", mode="before")
    @classmethod
    def empty_string_to_none(cls, v):
        if v == "":
            return None
        return v

class FoundryTraits(ClosedModel):
    rarity: FoundryRarity | None = None
    traditions: list[Pf2eTradition] = Field(default_factory=list)
    value: list[Pf2eTraits]
    selected: dict[Pf2eTraits, str] | list[Pf2eTraits] | None = None


class FoundrySpellRange(ClosedModel):
    value: str


class FoundryPathfinderPublicationDetails(ClosedModel):
    license: str
    remaster: bool
    title: str


class FoundrySpellDuration(ClosedModel):
    sustained: bool
    value: str


class FoundrySpellDescription(ClosedModel):
    value: str
    gm: str | None = None


class FoundryHeighteningType(Enum):
    interval = "interval"
    fixed = "fixed"


class FoundryHeighteningDetails(ClosedModel):
    area: FoundryArea | None = None
    range: FoundrySpellRange | None = None
    target: FoundrySpellTarget | None = None
    damage: dict[str, FoundrySpellDamageDetails] | None = None
    time: FoundryTime | None = None
    traits: FoundryTraits | None = None


class FoundrySpellHeightening(ClosedModel):
    area: int | None = None
    damage: dict[str, str] | None = None
    interval: int | None = None
    type: FoundryHeighteningType | None = None
    levels: dict[int, FoundryHeighteningDetails] | None = None


class FoundryPrimaryRitualCheck(ClosedModel):
    check: str

class FoundrySecondaryRitualCheck(ClosedModel):
    casters: int
    checks: str

class FoundrySpellRitual(ClosedModel):
    primary: FoundryPrimaryRitualCheck
    secondary: FoundrySecondaryRitualCheck


class FoundryOverlays(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)


class FoundrySpellSystem(ClosedModel):
    area: FoundryArea | None
    cost: FoundrySpellCost
    counteraction: bool
    damage: dict[str, FoundrySpellDamageDetails]
    defense: FoundrySpellDefense | None = None
    description: FoundrySpellDescription
    duration: FoundrySpellDuration
    heightening: FoundrySpellHeightening | None = None
    level: FoundrySpellLevel
    overlays: FoundryOverlays | None = None
    requirements: str
    publication: FoundryPathfinderPublicationDetails
    range: FoundrySpellRange
    ritual: FoundrySpellRitual | None = None
    rules: list[FoundrySpellRules]
    target: FoundrySpellTarget
    time: FoundryTime
    traits: FoundryTraits


class FoundrySpell(ClosedModel):
    folder: str | None = None
    id: str = Field(alias="_id")
    img: str
    name: str
    system: FoundrySpellSystem
    type: str
