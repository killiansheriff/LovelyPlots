# from https://github.com/garrettj403/SciencePlots

# to setup on Pypi: https://towardsdatascience.com/how-to-upload-your-python-package-to-pypi-de1b363a1b3

"""Install LovelyPlots.

This script (setup.py) will install the LovelyPlots package.
In order to expose .mplstyle files to matplotlib, "import lovelyplots"
must be called before plt.style.use(...).
"""

import os
from setuptools import setup

# Get description from README
root = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(root, 'README.md'), 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='LovelyPlots',
    version='1.0.0',
    author="Killian Sheriff",
    author_email="killian.sheriff@gmail.com",
    description="Format Matplotlib Plots for thesis, scientific papers and reports.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license="MIT",
    url="https://github.com/killiansheriff/LovelyPlots",
    install_requires=['matplotlib'],
    packages=["LovelyPlots"],
    package_data={
      'LovelyPlots': ['styles/**/*.mplstyle'],
    },

    classifiers=[
        'Framework :: Matplotlib', 
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],
    keywords=[
        "matplotlib-style-sheets",
        "matplotlib-figures",
        "scientific-papers",
        "PhD",
        "thesis-template",
        "matplotlib-styles",
        "Adobe Illustrator",
        "Latex",
        "latex-figures",
    ],
)