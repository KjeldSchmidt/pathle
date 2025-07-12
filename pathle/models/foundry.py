from enum import Enum

from pydantic import BaseModel, ConfigDict, Field, field_validator

from pathle.models.Pathfinder2e import (
    Pf2eAreaType,
    Pf2eSaveType,
    Pf2eDamageType,
    Pf2eRarity,
    Pf2eTradition,
    Pf2eTraits,
)


class ClosedModel(BaseModel):
    model_config = ConfigDict(extra="forbid")


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


class FoundrySpellDefenseSave(ClosedModel):
    basic: bool | None = None
    statistic: Pf2eSaveType


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


class FoundrySpellDamageCategory(Enum):
    persistent = "persistent"
    splash = "splash"


class FoundrySpellDamageDetails(ClosedModel):
    applyMod: bool | None = None
    category: FoundrySpellDamageCategory | None
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
    rarity: Pf2eRarity | None = None
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
