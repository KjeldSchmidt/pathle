import os
from pathlib import Path
from typing import Literal

from pydantic import ValidationError

from pathle.models.foundry import FoundrySpell
from pathle.models.Pathle import PathleSpell, PathleSpellType, PathleSpellTarget
from pathle.models.Pathfinder2e import Pf2eTraits, Pf2eDamageType, Pf2eSpellRange

# Files to ignore during processing
IGNORED_FILES = [
    "_folders.json",
]

in_folder = Path("resources/in/spells/")
out_folder = Path("resources/out/spells/")

ExecutionMode = Literal["single", "statistical"]
execution_mode: ExecutionMode = "single"


def determine_spell_type(foundry_spell: FoundrySpell) -> PathleSpellType:
    """Determine PathleSpellType from FoundrySpell"""
    traits = foundry_spell.system.traits.value
    
    if Pf2eTraits.cantrip.value in traits:
        return PathleSpellType.cantrip
    elif Pf2eTraits.focus.value in traits:
        return PathleSpellType.focus
    elif foundry_spell.system.ritual is not None:
        return PathleSpellType.ritual
    else:
        return PathleSpellType.slot


def determine_target(foundry_spell: FoundrySpell) -> PathleSpellTarget:
    """Determine PathleSpellTarget from FoundrySpell"""
    target_value = foundry_spell.system.target.value.lower()
    area = foundry_spell.system.area
    
    # If there's an area, use area type
    if area:
        area_type = area.type.value.lower()  # Get the enum value
        if area_type == "cone":
            return PathleSpellTarget.cone
        elif area_type == "burst":
            return PathleSpellTarget.burst
        elif area_type == "line":
            return PathleSpellTarget.line
        elif area_type == "emanation":
            return PathleSpellTarget.emanation
        elif area_type in ["square", "rectangle"]:
            return PathleSpellTarget.square
        elif area_type == "cube":
            return PathleSpellTarget.cube
        elif area_type == "cylinder":
            return PathleSpellTarget.cylinder
        else:
            return PathleSpellTarget.other
    
    # If no area, check target value
    if not target_value or target_value == "":
        return PathleSpellTarget.self
    elif "creature" in target_value:
        return PathleSpellTarget.creature
    else:
        return PathleSpellTarget.other


def extract_damage_types(foundry_spell: FoundrySpell) -> set[Pf2eDamageType]:
    """Extract damage types from FoundrySpell"""
    damage_types = set()
    for damage_detail in foundry_spell.system.damage.values():
        damage_types.add(damage_detail.type)
    return damage_types


def clean_description(description: str) -> list[str]:
    """Clean and split description into paragraphs"""
    import re
    # Remove HTML tags
    clean_desc = re.sub(r'<[^>]+>', '', description)
    # Split by paragraph breaks and clean whitespace
    paragraphs = [p.strip() for p in clean_desc.split('\n') if p.strip()]
    return paragraphs


def transform(path: Path):
    raw_json = path.read_text()
    try:
        foundry_spell = FoundrySpell.model_validate_json(raw_json)
        if foundry_spell.system.range.value is None:
            print(foundry_spell.name)

        pathle_spell = PathleSpell(
            name=foundry_spell.name,
            range=foundry_spell.system.range.value,
            basic_save=foundry_spell.system.defense.save.statistic if foundry_spell.system.defense and foundry_spell.system.defense.save and foundry_spell.system.defense.save.basic else None,
            rank=foundry_spell.system.level.value,
            type=determine_spell_type(foundry_spell),
            traditions=set(foundry_spell.system.traits.traditions),
            traits=set(foundry_spell.system.traits.value),
            rarity=foundry_spell.system.traits.rarity,
            target=determine_target(foundry_spell),
            description=clean_description(foundry_spell.system.description.value),
            damage_types=extract_damage_types(foundry_spell),
            duration=foundry_spell.system.duration.value
        )
        
        return pathle_spell
    except ValidationError as err:
        return err


def main():
    processed = 0
    successes = 0
    for dirpath, _, filenames in os.walk(in_folder):
        for filename in filenames:
            if filename.endswith(".json") and filename not in IGNORED_FILES:
                filepath = Path(dirpath) / filename
                result = transform(filepath)
                success = isinstance(result, PathleSpell)
                processed += 1
                successes += 1 if success else 0

                if not success and execution_mode == "single":
                    print(f"Processed {successes} files before error:")
                    print(f"Validation errors for file {filepath}:")
                    for error in result.errors():
                        print(f"  - {error}")
                        if error["type"] == "enum":
                            print(error["input"])

                    exit(0)

    print(
        f"Processed {processed} files, {successes} succeeded, {successes / processed:.2%} success rate"
    )


main()
