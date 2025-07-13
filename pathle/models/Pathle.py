from enum import Enum

from pydantic import BaseModel

from pathle.models.Pathfinder2e import (
    Pf2eTradition,
    Pf2eSaveType,
    Pf2eSpellRange,
    Pf2eTraits,
    Pf2eRarity,
    Pf2eDamageType, Pf2eSpellDuration,
)
from pathle.models.foundry import FoundrySpell


class PathleSpellType(Enum):
    cantrip = "cantrip"
    focus = "focus"
    slot = "slot"
    ritual = "ritual"


class PathleSpellTarget(Enum):
    creature = "creature"
    self = "self"
    cone = "cone"
    burst = "burst"
    line = "line"
    square = "square"
    cube = "cube"
    cylinder = "cylinder"
    emanation = "emanation"
    other = "other"

    @classmethod
    def from_foundry_spell(cls, foundry_spell: FoundrySpell) -> "PathleSpellTarget":
        print(foundry_spell.system.target)
        print(foundry_spell.system.area)
        exit(0)


class PathleSpellDamageDetails:
    formula: str
    kinds: list[str] | None = None
    materials: list[str] | None = None
    type: Pf2eDamageType


class PathleSpell(BaseModel):
    name: str
    range: Pf2eSpellRange
    basic_save: Pf2eSaveType | None
    rank: int
    type: PathleSpellType
    traditions: set[Pf2eTradition]
    traits: set[Pf2eTraits]
    rarity: Pf2eRarity
    target: PathleSpellTarget
    description: list[str]
    damage_types: set[Pf2eDamageType]
    duration: Pf2eSpellDuration
