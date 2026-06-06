"""Tests del ejercicio 6."""

import unittest

import pandas as pd

from src.exercises.ex6 import fun_total_goals


class TestFunTotalGoals(unittest.TestCase):
    """Tests de la funcion fun_total_goals."""

    def test_total_home_goals(self):
        """Comprueba que se suman correctamente los goles locales, visitantes y totales."""
        # Comprobamos que se suman correctamente los goles de los equipos locales
        data = pd.DataFrame({
            "FTHG": [2, 1, 0],
            "FTAG": [1, 1, 3],
        })

        home_goals, away_goals, total_goals = fun_total_goals(data)

        self.assertEqual(home_goals, 3)
        self.assertEqual(away_goals, 5)
        self.assertEqual(total_goals, 8)
