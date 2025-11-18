# output.py

import matplotlib.pyplot as plt


def create_plot(fig, fig_counter, u, T_cold, T_hot, time_ms):
    """Create one subplot for a given time snapshot.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        The figure to which the subplot will be added.
    fig_counter : int
        Index (1..4) of the subplot.
    u : 2D ndarray
        Temperature field at the current time.
    T_cold : float
        Minimum temperature (for color scale).
    T_hot : float
        Maximum temperature (for color scale).
    time_ms : float
        Time in milliseconds (for the title).

    Returns
    -------
    im : matplotlib.image.AxesImage
        The image object (needed later for the colorbar).
    """
    ax = fig.add_subplot(220 + fig_counter)
    im = ax.imshow(u.copy(),
                   cmap=plt.get_cmap('hot'),
                   vmin=T_cold,
                   vmax=T_hot)
    ax.set_axis_off()
    ax.set_title('{:.1f} ms'.format(time_ms))
    return im


def output_plots(fig, im):
    """Finalize the figure: add colorbar and show it."""
    fig.subplots_adjust(right=0.85)
    cbar_ax = fig.add_axes([0.9, 0.15, 0.03, 0.7])
    cbar_ax.set_xlabel('$T$ / K', labelpad=20)
    fig.colorbar(im, cax=cbar_ax)
    plt.show()
