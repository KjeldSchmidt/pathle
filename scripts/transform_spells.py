import os
from pathlib import Path
from typing import Literal

from pydantic import ValidationError

from pathle.models.foundry import FoundrySpell

# Files to ignore during processing
IGNORED_FILES = [
    "_folders.json",
]

in_folder = Path("resources/in/spells/")
out_folder = Path("resources/out/spells/")

ExecutionMode = Literal["single", "statistical"]
execution_mode: ExecutionMode = "single"


def transform(path: Path):
    raw_text = path.read_text()
    try:
        return FoundrySpell.model_validate_json(raw_text)
    except ValidationError as err:
        return err


processed = 0
successes = 0
new_traits = set()
for dirpath, _, filenames in os.walk(in_folder):
    for filename in filenames:
        if filename.endswith(".json") and filename not in IGNORED_FILES:
            filepath = Path(dirpath) / filename
            result = transform(filepath)
            success = isinstance(result, FoundrySpell)
            processed += 1

            if success:
                successes += 1

            if not success and execution_mode == "statistical":
                for error in result.errors():
                    if error["type"] == "enum" and error["loc"][1] == "traits":
                        new_traits.add(error["input"])

            if not success and execution_mode == "single":
                print(f"Processed {successes} files before error:")
                print(f"Validation errors for file {filepath}:")
                for error in result.errors():
                    print(f"  - {error}")
                    if error["type"] == "enum" and error["loc"][1] == "traits":
                        new_traits.add(error["input"])

                for trait in new_traits:
                    print(f'{trait} = "{trait}"')
                exit(0)

for trait in new_traits:
    print(f'{trait} = "{trait}"')

print(
    f"Processed {processed} files, {successes} succeeded, {successes / processed:.2%} success rate"
)
