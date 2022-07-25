import matplotlib as mpl


def set_font(font_path):
    font = mpl.font_manager.FontEntry(fname=font_path, name="my_font")
    mpl.font_manager.fontManager.ttflist.append(font)

    mpl.rcParams.update(
        {
            "font.family": font.name,
        }
    )


def set_retina():
    from IPython import get_ipython

    get_ipython().run_line_magic("matplotlib", "inline")
    from IPython.display import set_matplotlib_formats

    set_matplotlib_formats("retina")


def set_size(subplots=(1, 1)):

    fig_width_in = mpl.rcParams["figure.figsize"][0]
    fig_height_in = mpl.rcParams["figure.figsize"][1] * (subplots[0] / subplots[1])

    return (fig_width_in, fig_height_in)
