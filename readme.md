# LovelyPlots
<!-- [![Github All Releases](https://img.shields.io/github/downloads/killiansheriff/LovelyPlots/total.svg)]()  -->

LovelyPlots is a repository containing ``matplotlib`` style sheets to nicely format figures for scientific papers, thesis and presentations while keeping them fully editable in ``Adobe Illustrator``. Additonaly, ``.svg`` exports options allows figures to automatically adapt their font to your document's font. For example, ``.svg`` figures imported in a ``.tex`` file will automatically be generated with the text font used in your ``.tex`` file.

<p align="center" width="50%">
    <img width="70%" src="figs/plots/ipynb+use_mathtext.svg">
</p>

# Installation

```bash
# to install latest PyPI release
pip install LovelyPlots

# to install latest GitHub commit
pip install git+https://github.com/killiansheriff/LovelyPlots
```

The pip installation will move all of the ``matplotlib`` style files ``*.mplstyle`` into the appropriate ``matplotlib`` directory.

# Usage

LovelyPlots main style is called ``ipynb``. To use it, add the following lines to the begining of your python scripts:

```python
import matplotlib.pyplot as plt
plt.style.use('ipynb')
```

Styles can be combined:

```python
import matplotlib.pyplot as plt
plt.style.use(['ipynb','colorsblind34'])
```

In the above case, the ``ipynb`` default color cycle will be overwritten by a 34 colors colorblind safe color cycle called ``colorsblind34``.

If you only wish to apply a style on a specific plot, this can be achieved using:

```python
import matplotlib.pyplot as plt

with plt.style.context('ipynb'):
  fig, ax = plt.subplots()
  ax.plot(x, y)
```

# Examples

A few styles are presented here, please see [Styles](#Styles) for a list of all implemented styles.


The ``['ipynb', 'use_mathtext']`` style:

![](figs/plots/ipynb%2Buse_mathtext.svg)

The ``['ipynb', 'use_mathtext','colors10-markers']`` style:

![](figs/plots/ipynb%2Buse_mathtext+colors10-markers.svg)

The ``['ipynb', 'use_mathtext','colors5-light']`` style:

![](figs/plots/ipynb%2Buse_mathtext+colors5-light.svg)

The ``['ipynb', 'use_mathtext', 'colors10-ls']`` style:

![](figs/plots/ipynb%2Buse_mathtext+colors10-ls.svg)

# Styles

LovelyPlots main style is called ``ipynb``. The latter by default sets the figure size to ``(4.5, 3.46) inches``, uses the default ``matplotlib`` font, activate scientific notation and makes sure your ``matplotlib`` exports will be editable in ``Adobe Illustrator``. Its default color cycle was set to ``colors10``.

## Color cycles

A multitude of color cycles were implemented:

``colors5-light``

![](figs/colors/colors5-light.png)

``colors5``

![](figs/colors/color5.png)

``colors10``

![](figs/colors/color10.png)

``colorsblind10``

![](figs/colors/colorsblind10.png)

``colorsblind34``

Can be seen [here](figs/colors/colorsblind34.png).


## Lines styles, markers and combinations styles

Line styles, markers styles and combinations can be set using the following styles: `ls5`, `marker7`, `colors10-ls`, `colors10-markers`.

## Utils

Specific ``matplotlibrc`` parameters can be turned ``on/off`` using the following utilities styles: ``svg_no_fonttype``, ``use_mathtex``, ``use_tex``.

## Fonts

By default the ``ipynb`` style uses the default ``matplotlib`` font. However, one can set its favorite font from a TIFF file:

```python
import matplotlib.pyplot as plt
import LovelyPlots.utils as lp

plt.style.use('ipynb')
lp.set_font('my_font.tiff')
```




# Tips and Tricks

## Adobe illustrator

Unfornunatly, ``mathtext`` (and thus nicely formated scientific notation) will mess up ``Adobe illustrator`` ability to detect text objects, and is thus not activate by default. If you wish to use it, please add the style ``use_mathtext``.

## Latex and SVG files
By default, the ``ipynb`` style sets ``svg.fonttype: none``. This allows for plots saved as ``.svg`` not to carry font information. Consequently, when opened in another environement, the plot will be generated with the default system font!

For example, this allows ``.svg`` plots imported inside a ``Latex`` file to directly be generated with the proper document font, without you having to manually edit the fonts to match your document's font. Additonally, you can open the ``.svg`` file as  text file, find the ugly ``1e10`` scientific notation and replace it with ``$10^10$`` so that it is nicely formated when included in your ``.tex`` file.

An example on how to show an svg in a ``.tex`` file:

```tex
\usepackage{svg}

\begin{figure}[htbp]
  \centering
  \includesvg{myfig.svg}
\end{figure}
```
## Retina displays

For those using ``IPython`` notebooks, you can set restina display support by adding the following lines to the begining on your python script:


```python
import LovelyPlots.utils as lp
lp.use_retina()
```
## Useth of Google Colab
You will need to run the following code:
```python
!pip install LovelyPlots
plt.style.reload_library()
plt.style.use('ipynb')
```

# Aknoledgements

This reprository was inspired by [SciencePlots](https://github.com/garrettj403/SciencePlots), but adds different styles and crucial functionalities for useth in ``.tex`` files and ``Adobe Illustrator``.


