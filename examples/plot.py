# %%
import matplotlib.pyplot as plt
import numpy as np


# %%
def plot_dist(
    temperatures,
    v,
    mass=85 * 1.66e-27,
    pparam={"xlabel": "Speed", "ylabel": "Speed distribution"},
    save_name="",
):
    fig, ax = plt.subplots()
    for T in temperatures:
        fv = MB_speed(v, mass, T)
        ax.plot(v, fv, label=f"T={T}K")
        ax.legend()
        ax.set(
            **pparam,
        )
        fig.savefig(save_name)


v = np.arange(0, 800, 10)
temperatures = [i for i in range(100, 500, 75)]


def MB_speed(v, m, T):
    """Maxwell-Boltzmann speed distribution for speeds"""
    kB = 1.38e-23
    return (
        (m / (2 * np.pi * kB * T)) ** 1.5 * 4 * np.pi * v**2 * np.exp(-m * v**2 / (2 * kB * T))
    )


styles = [
    [
        "ipynb",
        "use_mathtext",
    ],
    [
        "ipynb",
        "use_mathtext",
        "colors5-light",
    ],
    [
        "ipynb",
        "use_mathtext",
        "colors10-ls",
    ],
    [
        "ipynb",
        "use_mathtext",
        "colors10-markers",
    ],
    ["classic"],
    ["ipynb"],
    ["paper", "use_mathtext"],
]
names = [
    "out/ipynb+use_mathtext.svg",
    "out/ipynb+use_mathtext+colors5-light.svg",
    "out/ipynb+use_mathtext+colors10-ls.svg",
    "out/ipynb+use_mathtext+colors10-markers.svg",
    "out/classicmpl.svg",
    "out/ipynb.svg",
    "out/paper+use_mathtext.svg",
]
# %%

for style, name in zip(styles, names):
    with plt.style.context(style):
        plot_dist(temperatures, v, save_name=name)

# %%
