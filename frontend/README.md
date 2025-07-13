# Pathle Frontend

A Wordle-style game for Pathfinder 2e spells.

## How to Play

1. **Objective**: Guess the secret Pathfinder 2e spell in 6 attempts or less.

2. **Making Guesses**: 
   - Type a spell name in the input field
   - Use the autocomplete suggestions to find valid spells
   - Click Submit or press Enter to make your guess

3. **Understanding Results**:
   - Each guess shows a row with the spell's attributes
   - **Green cells**: Correct match with the target spell
   - **Gray cells**: Incorrect match
   - Compare your guesses with the target across these attributes:
     - **Name**: The spell name
     - **Rank**: Spell level (1-10)
     - **Type**: cantrip, focus, slot, or ritual
     - **Range**: How far the spell can be cast
     - **Save**: Required saving throw (Will/Reflex/Fortitude/None)
     - **Traditions**: Magic traditions that can cast it
     - **Rarity**: common, uncommon, rare, unique
     - **Target**: What the spell targets
     - **Damage**: Types of damage dealt
     - **Duration**: How long the spell lasts

4. **Winning**: Get all attributes correct (entire row green) to win!

## Features

- **Autocomplete**: Type to search through 1,700+ Pathfinder 2e spells
- **Visual Feedback**: Wordle-style color coding for correct/incorrect matches
- **Attempt Tracking**: 6 attempts maximum per game
- **New Game**: Start fresh with a new random spell
- **Responsive Design**: Works on desktop and mobile

## Running the Game

To run the game locally:

1. Ensure you have generated the spell data:
   ```bash
   python -m scripts.export_spells_for_frontend
   ```

2. Serve the frontend directory with a local web server:
   ```bash
   # Using Python's built-in server
   cd frontend
   python -m http.server 8000
   
   # Or using Node.js
   npx serve .
   ```

3. Open your browser to `http://localhost:8000`

## Files

- `index.html`: Main game interface
- `styles.css`: Styling and layout
- `script.js`: Game logic and interactivity
- `data/spells.json`: Complete spell data
- `data/spell_names.json`: Spell names for autocomplete

## Game Rules

- Each spell can only be guessed once per game
- Only valid Pathfinder 2e spell names are accepted
- Use the autocomplete suggestions to find the correct spelling
- The target spell is randomly selected from all available spells

Enjoy playing Pathle! 