"""A Number Guessing Game"""
from __future__ import annotations
from jaclang import jac_import as __jac_import__
from jaclang.plugin.feature import JacFeature as _Jac
from jaclang.plugin.builtin import *
from dataclasses import dataclass as __jac_dataclass__
__jac_import__(target='random', base_path=__file__, mod_bundle=__jac_mod_bundle__, lng='py', absorb=False, mdl_alias=None, items={})
import random

@_Jac.make_obj(on_entry=[], on_exit=[])
@__jac_dataclass__(eq=False)
class Game:
    """
A generic Game base class.
"""
    attempts: int
    won: bool = _Jac.has_instance_default(gen_func=lambda: False)

    def play(self) -> None:
        raise NotImplementedError('Subclasses must implement this method.')

@_Jac.make_obj(on_entry=[], on_exit=[])
@__jac_dataclass__(eq=False)
class GuessTheNumberGame(Game):
    """
A number guessing game. The player must guess a number between 1 and 100.
"""
    attempts: int = _Jac.has_instance_default(gen_func=lambda: 10)
    correct_number: int = _Jac.has_instance_default(gen_func=lambda: random.randint(1, 100))

    def play(self) -> None:
        while self.attempts > 0:
            guess = input('Guess a number between 1 and 100: ')
            if guess.isdigit():
                self.process_guess(int(guess))
            else:
                print("That's not a valid number! Try again.")
        if not self.won:
            print("Sorry, you didn't guess the number. Better luck next time!")

    def process_guess(self, guess: int) -> None:
        if guess > self.correct_number:
            print('Too high!')
        elif guess < self.correct_number:
            print('Too low!')
        else:
            print('Congratulations! You guessed correctly.')
            self.attempts = 0
            self.won = True
        self.attempts -= 1
        print(f'You have {self.attempts} attempts left.')
game = GuessTheNumberGame()
game.play()