import json
import os
from pathlib import Path

from pathle.models.Pathle import PathleSpell
from scripts.transform_spells import transform, IGNORED_FILES


def export_spells_for_frontend():
    """Export all spells as JSON for the frontend"""
    in_folder = Path("resources/in/spells/")
    output_file = Path("frontend/data/spells.json")
    
    # Ensure output directory exists
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    spells = []
    
    # Process all spell files
    for dirpath, _, filenames in os.walk(in_folder):
        for filename in filenames:
            if filename.endswith(".json") and filename not in IGNORED_FILES:
                filepath = Path(dirpath) / filename
                result = transform(filepath)
                
                if isinstance(result, PathleSpell):
                    spell_data = {
                        "name": result.name,
                        "range": result.range.value if result.range else None,
                        "basic_save": result.basic_save.value if result.basic_save else None,
                        "rank": result.rank,
                        "type": result.type.value,
                        "traditions": [t.value for t in result.traditions],
                        "traits": [t.value for t in result.traits],
                        "rarity": result.rarity.value,
                        "target": result.target.value,
                        "damage_types": [dt.value for dt in result.damage_types],
                        "duration": result.duration.value if result.duration else None
                    }
                    spells.append(spell_data)
    
    # Sort spells by name for easier searching
    spells.sort(key=lambda x: x["name"])
    
    # Export to JSON
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(spells, f, indent=2, ensure_ascii=False)
    
    print(f"Exported {len(spells)} spells to {output_file}")
    
    # Also create a simple spell names list for autocomplete
    spell_names = [spell["name"] for spell in spells]
    names_file = Path("frontend/data/spell_names.json")
    with open(names_file, 'w', encoding='utf-8') as f:
        json.dump(spell_names, f, indent=2, ensure_ascii=False)
    
    print(f"Exported {len(spell_names)} spell names to {names_file}")

if __name__ == "__main__":
    export_spells_for_frontend() 
