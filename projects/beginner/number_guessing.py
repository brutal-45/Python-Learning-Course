"""
Project: Number Guessing Game
Level: Beginner
Description: A simple number guessing game with different difficulty levels.

This project demonstrates:
- Random number generation
- User input handling
- Loops and conditionals
- Functions
- Game logic
"""

import random
import time


class NumberGuessingGame:
    """
    A number guessing game with multiple difficulty levels.

    The player tries to guess a randomly generated number
    within a certain number of attempts.
    """

    # Class-level difficulty settings
    DIFFICULTY = {
        'easy': {'range': (1, 50), 'attempts': 10},
        'medium': {'range': (1, 100), 'attempts': 7},
        'hard': {'range': (1, 200), 'attempts': 5}
    }

    def __init__(self, difficulty='medium'):
        """
        Initialize the game with the specified difficulty.

        Args:
            difficulty: Game difficulty ('easy', 'medium', 'hard')
        """
        if difficulty not in self.DIFFICULTY:
            difficulty = 'medium'

        self.difficulty = difficulty
        settings = self.DIFFICULTY[difficulty]
        self.min_num, self.max_num = settings['range']
        self.max_attempts = settings['attempts']
        self.reset()

    def reset(self):
        """Reset the game for a new round."""
        self.target = random.randint(self.min_num, self.max_num)
        self.attempts_left = self.max_attempts
        self.guesses = []
        self.game_over = False
        self.won = False

    def make_guess(self, guess):
        """
        Process a player's guess.

        Args:
            guess: The player's guess

        Returns:
            tuple: (message, game_over)
        """
        if self.game_over:
            return "Game is over! Start a new game.", True

        try:
            guess = int(guess)
        except ValueError:
            return "Please enter a valid number!", False

        if guess < self.min_num or guess > self.max_num:
            return f"Please enter a number between {self.min_num} and {self.max_num}!", False

        self.guesses.append(guess)
        self.attempts_left -= 1

        if guess == self.target:
            self.game_over = True
            self.won = True
            return self._win_message(), True
        elif self.attempts_left == 0:
            self.game_over = True
            return self._lose_message(), True
        elif guess < self.target:
            hint = self._get_hint(guess)
            return f"Too low! {hint} Attempts left: {self.attempts_left}", False
        else:
            hint = self._get_hint(guess)
            return f"Too high! {hint} Attempts left: {self.attempts_left}", False

    def _get_hint(self, guess):
        """Generate a hint based on how close the guess is."""
        diff = abs(guess - self.target)

        if diff <= 5:
            return "🔥 Very close!"
        elif diff <= 15:
            return "🌡️ Getting warmer!"
        elif diff <= 30:
            return "❄️ Cold!"
        else:
            return "🧊 Freezing!"

    def _win_message(self):
        """Generate win message."""
        attempts_used = self.max_attempts - self.attempts_left
        score = self._calculate_score()
        return f"""
🎉 Congratulations! You guessed it!
   The number was {self.target}
   Attempts used: {attempts_used}/{self.max_attempts}
   Your score: {score} points
"""

    def _lose_message(self):
        """Generate lose message."""
        return f"""
😢 Game Over!
   The number was {self.target}
   Your guesses: {self.guesses}
"""

    def _calculate_score(self):
        """Calculate score based on attempts and difficulty."""
        attempts_used = self.max_attempts - self.attempts_left
        difficulty_multiplier = {'easy': 1, 'medium': 2, 'hard': 3}
        base_score = 1000
        penalty = attempts_used * 50

        score = (base_score - penalty) * difficulty_multiplier[self.difficulty]
        return max(score, 100)

    def get_stats(self):
        """Get current game statistics."""
        return {
            'difficulty': self.difficulty,
            'range': (self.min_num, self.max_num),
            'attempts_left': self.attempts_left,
            'guesses': self.guesses,
            'game_over': self.game_over,
            'won': self.won
        }

    def display_welcome(self):
        """Display welcome message and instructions."""
        print("\n" + "=" * 50)
        print("🎯 NUMBER GUESSING GAME 🎯")
        print("=" * 50)
        print(f"\nDifficulty: {self.difficulty.upper()}")
        print(f"Guess a number between {self.min_num} and {self.max_num}")
        print(f"You have {self.max_attempts} attempts")
        print("\nType 'quit' to exit, 'hint' for a hint, 'stats' for game stats")
        print("-" * 50)


def play_game():
    """Main game loop with simulated inputs for demonstration."""
    print("\n" + "=" * 50)
    print("🎮 DEMONSTRATION MODE")
    print("=" * 50)

    # Simulate a game
    game = NumberGuessingGame('medium')
    game.display_welcome()

    # For demonstration, we'll play with known values
    # In a real game, target is random
    game.target = 42  # Set known target for demo
    game.attempts_left = game.max_attempts

    # Simulated guesses
    demo_guesses = [25, 60, 40, 45, 42]

    print("\n📝 Simulated gameplay:")
    for guess in demo_guesses:
        if game.game_over:
            break

        print(f"\nGuess: {guess}")
        time.sleep(0.5)
        message, game_over = game.make_guess(guess)
        print(message)

        if game_over:
            break

    # Show final stats
    print("\n📊 Final Stats:")
    stats = game.get_stats()
    for key, value in stats.items():
        print(f"   {key}: {value}")


def interactive_game():
    """
    Interactive game mode (for real play).
    Uncomment and run this for actual gameplay.
    """
    print("\n" + "=" * 50)
    print("🎮 INTERACTIVE MODE")
    print("=" * 50)

    # Select difficulty
    print("\nSelect Difficulty:")
    for i, diff in enumerate(NumberGuessingGame.DIFFICULTY.keys(), 1):
        settings = NumberGuessingGame.DIFFICULTY[diff]
        print(f"  {i}. {diff.capitalize()}: "
              f"Range {settings['range'][0]}-{settings['range'][1]}, "
              f"{settings['attempts']} attempts")

    while True:
        choice = input("\nEnter difficulty (1-3) or name: ").lower().strip()
        difficulties = list(NumberGuessingGame.DIFFICULTY.keys())

        if choice in ['1', 'easy']:
            difficulty = 'easy'
            break
        elif choice in ['2', 'medium']:
            difficulty = 'medium'
            break
        elif choice in ['3', 'hard']:
            difficulty = 'hard'
            break
        else:
            print("Invalid choice. Please try again.")

    # Create and start game
    game = NumberGuessingGame(difficulty)
    game.display_welcome()

    # Game loop
    while not game.game_over:
        guess = input("\nEnter your guess: ").strip()

        if guess.lower() == 'quit':
            print(f"\nThanks for playing! The number was {game.target}")
            break
        elif guess.lower() == 'hint':
            # Give a hint about the range
            mid = (game.min_num + game.max_num) // 2
            if game.target > mid:
                print(f"💡 Hint: The number is above {mid}")
            else:
                print(f"💡 Hint: The number is at or below {mid}")
            continue
        elif guess.lower() == 'stats':
            stats = game.get_stats()
            print("\n📊 Current Stats:")
            for key, value in stats.items():
                print(f"   {key}: {value}")
            continue

        message, game_over = game.make_guess(guess)
        print(message)

    # Play again?
    if input("\nPlay again? (y/n): ").lower() == 'y':
        interactive_game()


# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("🎯 NUMBER GUESSING GAME")
    print("=" * 50)

    # Run demonstration
    play_game()

    # Uncomment the next line for interactive play:
    # interactive_game()

    print("\n✅ Thanks for checking out the Number Guessing Game!")
    print("📚 To play interactively, uncomment interactive_game() in the code")
