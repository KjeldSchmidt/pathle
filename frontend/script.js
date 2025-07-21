class PathleGame {
    constructor() {
        this.spells = [];
        this.spellNames = [];
        this.currentSpell = null;
        this.attempts = 0;
        this.gameOver = false;
        this.guessedSpells = [];
        
        this.elements = {
            input: document.getElementById('spell-input'),
            submitBtn: document.getElementById('submit-btn'),
            resultsContainer: document.getElementById('results-container'),
            message: document.getElementById('message'),
            attempts: document.getElementById('attempts'),
            newGameBtn: document.getElementById('new-game-btn'),
            suggestions: document.getElementById('suggestions')
        };
        
        this.init();
    }
    
    async init() {
        await this.loadSpellData();
        this.setupEventListeners();
        this.startNewGame();
    }
    
    async loadSpellData() {
        try {
            const [spellsResponse, namesResponse] = await Promise.all([
                fetch('data/spells.json'),
                fetch('data/spell_names.json')
            ]);
            
            this.spells = await spellsResponse.json();
            this.spellNames = await namesResponse.json();
            
            console.log(`Loaded ${this.spells.length} spells`);
        } catch (error) {
            console.error('Error loading spell data:', error);
            this.elements.message.textContent = 'Error loading spell data. Please refresh the page.';
        }
    }
    
    setupEventListeners() {
        this.elements.input.addEventListener('input', (e) => this.handleInput(e));
        this.elements.input.addEventListener('keydown', (e) => this.handleKeyDown(e));
        this.elements.submitBtn.addEventListener('click', () => this.submitGuess());
        this.elements.newGameBtn.addEventListener('click', () => this.startNewGame());
        
        // Hide suggestions when clicking outside
        document.addEventListener('click', (e) => {
            if (!e.target.closest('.input-section')) {
                this.hideSuggestions();
            }
        });
    }
    
    handleInput(e) {
        const query = e.target.value.toLowerCase();
        if (query.length < 1) {
            this.hideSuggestions();
            return;
        }
        
        const matches = this.spellNames.filter(name => 
            name.toLowerCase().includes(query)
        ).slice(0, 10);
        
        this.showSuggestions(matches);
    }
    
    handleKeyDown(e) {
        if (e.key === 'Enter') {
            this.submitGuess();
        } else if (e.key === 'Escape') {
            this.hideSuggestions();
        }
    }
    
    showSuggestions(matches) {
        if (matches.length === 0) {
            this.hideSuggestions();
            return;
        }
        
        this.elements.suggestions.innerHTML = matches.map(name => 
            `<div class="suggestion-item" data-name="${name}">${name}</div>`
        ).join('');
        
        this.elements.suggestions.classList.add('show');
        
        // Add click listeners to suggestions
        this.elements.suggestions.querySelectorAll('.suggestion-item').forEach(item => {
            item.addEventListener('click', () => {
                this.elements.input.value = item.dataset.name;
                this.hideSuggestions();
                this.elements.input.focus();
            });
        });
    }
    
    hideSuggestions() {
        this.elements.suggestions.classList.remove('show');
    }
    
    submitGuess() {
        if (this.gameOver) return;
        
        const guess = this.elements.input.value.trim();
        if (!guess) return;
        
        const spell = this.spells.find(s => s.name.toLowerCase() === guess.toLowerCase());
        if (!spell) {
            this.elements.message.textContent = 'Spell not found. Please select from the suggestions.';
            return;
        }
        
        if (this.guessedSpells.some(g => g.name === spell.name)) {
            this.elements.message.textContent = 'You already guessed that spell!';
            return;
        }
        
        this.makeGuess(spell);
        this.elements.input.value = '';
        this.hideSuggestions();
        this.elements.message.textContent = '';
    }
    
    makeGuess(spell) {
        this.attempts++;
        this.guessedSpells.push(spell);
        this.updateAttempts();
        
        const isCorrect = spell.name === this.currentSpell.name;
        this.addResultRow(spell, isCorrect);
        
        if (isCorrect) {
            this.endGame(true);
        }
    }
    
    addResultRow(spell, isCorrect) {
        const row = document.createElement('div');
        row.className = 'result-row';
        
        const cells = [
            { value: spell.name, class: 'name' },
            { value: spell.rank },
            { value: spell.type },
            { value: spell.range || 'N/A' },
            { value: spell.basic_save || 'None' },
            { value: this.formatArray(spell.traditions), class: 'traditions-cell' },
            { value: spell.rarity },
            { value: spell.target },
            { value: this.formatArray(spell.damage_types) },
            { value: spell.duration || 'N/A' }
        ];
        
        cells.forEach((cell, index) => {
            const cellElement = document.createElement('div');
            cellElement.className = 'result-cell';
            if (cell.class) cellElement.classList.add(cell.class);
            
            let matchType;
            if (index === 1) { // Rank column
                matchType = this.compareRank(cell.value, this.getCellValue(this.currentSpell, index));
            } else {
                matchType = this.compareValuesWithPartial(cell.value, this.getCellValue(this.currentSpell, index));
            }
            
            cellElement.classList.add(matchType === 'exact' ? 'correct' : matchType === 'partial' ? 'partial' : matchType === 'high' ? 'high' : matchType === 'low' ? 'low' : 'wrong');
            cellElement.textContent = cell.value;
            
            row.appendChild(cellElement);
        });
        
        this.elements.resultsContainer.appendChild(row);
    }
    
    getCellValue(spell, index) {
        const values = [
            spell.name,
            spell.rank,
            spell.type,
            spell.range || 'N/A',
            spell.basic_save || 'None',
            this.formatArray(spell.traditions),
            spell.rarity,
            spell.target,
            this.formatArray(spell.damage_types),
            spell.duration || 'N/A'
        ];
        return values[index];
    }
    
    compareValues(guess, target) {
        if (typeof guess === 'string' && typeof target === 'string') {
            return guess.toLowerCase() === target.toLowerCase();
        }
        return guess === target;
    }
    
    compareValuesWithPartial(guess, target) {
        // Handle simple string comparisons first
        if (typeof guess === 'string' && typeof target === 'string') {
            // Check if these are comma-separated strings (formatted arrays)
            if (guess.includes(',') || target.includes(',') || guess === 'None' || target === 'None') {
                if (guess === 'None' && target === 'None') return 'exact';
                if (guess === 'None' || target === 'None') return 'none';
                
                const guessItems = guess.split(',').map(s => s.trim().toLowerCase());
                const targetItems = target.split(',').map(s => s.trim().toLowerCase());
                
                const matches = guessItems.filter(g => targetItems.includes(g));
                const allGuessMatch = guessItems.every(g => targetItems.includes(g));
                const allTargetMatch = targetItems.every(t => guessItems.includes(t));
                
                if (allGuessMatch && allTargetMatch) return 'exact';
                if (matches.length > 0) return 'partial';
                return 'none';
            }
            
            // Simple string comparison
            return guess.toLowerCase() === target.toLowerCase() ? 'exact' : 'none';
        }
        
        // Handle array comparisons (like traditions, damage_types)
        if (Array.isArray(guess) && Array.isArray(target)) {
            if (guess.length === 0 && target.length === 0) return 'exact';
            if (guess.length === 0 || target.length === 0) return 'none';
            
            const guessLower = guess.map(g => g.toLowerCase());
            const targetLower = target.map(t => t.toLowerCase());
            
            const matches = guessLower.filter(g => targetLower.includes(g));
            const allGuessMatch = guessLower.every(g => targetLower.includes(g));
            const allTargetMatch = targetLower.every(t => guessLower.includes(t));
            
            if (allGuessMatch && allTargetMatch) return 'exact';
            if (matches.length > 0) return 'partial';
            return 'none';
        }
        
        // Fallback for other types
        return guess === target ? 'exact' : 'none';
    }
    
    compareRank(guess, target) {
        // Convert to numbers for comparison
        const guessNum = parseInt(guess);
        const targetNum = parseInt(target);
        
        if (isNaN(guessNum) || isNaN(targetNum)) {
            // Fallback to string comparison if not numbers
            return guess === target ? 'exact' : 'none';
        }
        
        if (guessNum === targetNum) return 'exact';
        if (guessNum > targetNum) return 'high';
        return 'low';
    }
    
    formatArray(arr) {
        if (!arr || arr.length === 0) return 'None';
        return arr.join(', ');
    }
    
    updateAttempts() {
        this.elements.attempts.textContent = `Attempts: ${this.attempts}`;
    }
    
    endGame(won) {
        this.gameOver = true;
        this.elements.input.disabled = true;
        this.elements.submitBtn.disabled = true;
        
        this.elements.message.innerHTML = `<span class="win-message">Congratulations! You found the spell!</span>`;
        
        this.elements.newGameBtn.style.display = 'inline-block';
    }
    
    startNewGame() {
        // Reset game state
        this.attempts = 0;
        this.gameOver = false;
        this.guessedSpells = [];
        
        // Reset UI
        this.elements.input.disabled = false;
        this.elements.submitBtn.disabled = false;
        this.elements.input.value = '';
        this.elements.message.textContent = '';
        this.elements.resultsContainer.innerHTML = '';
        this.elements.newGameBtn.style.display = 'none';
        this.hideSuggestions();
        this.updateAttempts();
        
        // Choose random spell
        if (this.spells.length > 0) {
            const randomIndex = Math.floor(Math.random() * this.spells.length);
            this.currentSpell = this.spells[randomIndex];
            console.log('Target spell:', this.currentSpell.name); // For debugging
        }
        
        this.elements.input.focus();
    }
}

// Initialize the game when the page loads
document.addEventListener('DOMContentLoaded', () => {
    new PathleGame();
}); 