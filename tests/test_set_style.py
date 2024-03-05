import matplotlib.pyplot as plt
import pytest

import lovelyplots


def test_style():
    for style in ['paper', 'ipynb']:
        plt.style.use(style)