"""
Solving the two-dimensional diffusion equation

Example acquired from https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/
"""

import numpy as np
import matplotlib.pyplot as plt

from .output import create_plot, output_plots


def do_timestep(u_nm1, u, D, dt, dx2, dy2):
    """Advance the solution by one time step."""
    # Propagate with forward-difference in time, central-difference in space
    u[1:-1, 1:-1] = u_nm1[1:-1, 1:-1] + D * dt * (
        (u_nm1[2:, 1:-1] - 2 * u_nm1[1:-1, 1:-1] + u_nm1[:-2, 1:-1]) / dx2
        + (u_nm1[1:-1, 2:] - 2 * u_nm1[1:-1, 1:-1] + u_nm1[1:-1, :-2]) / dy2
    )

    u_nm1 = u.copy()
    return u_nm1, u


def solve(dx=0.1, dy=0.1, D=4.0):
    """Solve the 2D diffusion equation and plot four time snapshots.

    Parameters
    ----------
    dx, dy : float
        Spatial step sizes in x and y (mm).
    D : float
        Thermal diffusivity (mm^2/s).
    """
    # plate size, mm
    w = h = 10.0

    # temperatures
    T_cold = 300.0
    T_hot = 700.0

    # grid
    nx, ny = int(w / dx), int(h / dy)

    # stable timestep
    dx2, dy2 = dx * dx, dy * dy
    dt = dx2 * dy2 / (2 * D * (dx2 + dy2))
    print(f"dt = {dt}")

    # initial field
    u0 = T_cold * np.ones((nx, ny))
    u = u0.copy()

    # circular hot region
    r = min(h, w) / 4.0
    cx = w / 2.0
    cy = h / 2.0
    r2 = r ** 2
    for i in range(nx):
        for j in range(ny):
            p2 = (i * dx - cx) ** 2 + (j * dy - cy) ** 2
            if p2 < r2:
                u0[i, j] = T_hot

    # time-stepping parameters
    nsteps = 101
    # Output 4 figures at these timesteps
    n_output = [0, 10, 50, 100]

    fig_counter = 0
    fig = plt.figure()
    im = None  # will hold the last image for the colorbar

    # Time loop
    for n in range(nsteps):
        u0, u = do_timestep(u0, u, D, dt, dx2, dy2)

        # Create figure panels at selected steps
        if n in n_output:
            fig_counter += 1
            time_ms = n * dt * 1000.0
            im = create_plot(fig, fig_counter, u, T_cold, T_hot, time_ms)

    # Plot output figures
    output_plots(fig, im)


if __name__ == "__main__":
    # Run with default parameters when executed as a script
    solve()
