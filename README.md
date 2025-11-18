# nikhilnl_diffusion2d

A Python package that solves the two-dimensional diffusion equation on a square domain using an explicit finite-difference method.

The simulation models heat spreading from a hot circular region into a colder surrounding plate and produces four visual snapshots showing the evolution of temperature over time.

## Description

* This package implements a two–dimensional diffusion simulation on a square domain.
* The simulation begins with a cold plate and a hot circular region at its center.  
* It uses an explicit finite–difference method to advance the temperature field in time and produces four snapshot plots at selected time steps.

The key features:

- Finite–difference solution of the diffusion equation in 2D  
- Adjustable spatial resolution (dx, dy) and thermal diffusivity (D)  
- Temperature initialization with a hot circular region  
- Four time–point visualizations using Matplotlib  
- Packaged as a standard Python module ready for TestPyPI publishing

You can control the spatial resolution and thermal diffusivity using:

- `dx` – spacing in x direction (mm)
- `dy` – spacing in y direction (mm)
- `D`  – thermal diffusivity (mm²/s)

This package exposes a single main function:

```python
from nikhilnl_diffusion2d import solve
```

which runs the entire simulation and displays the plots.

## Installing the package

After uploading your distribution to TestPyPI, you can install it using:

```bash
python -m pip install \
    --index-url https://test.pypi.org/simple/ \
    --extra-index-url https://pypi.org/simple \
    nikhilnl-diffusion2d
```

The `--extra-index-url` argument ensures that dependencies such as NumPy and Matplotlib are pulled from the main PyPI index, not TestPyPI.

## Running this package

### Running via Python import

After installation, run:

```python
from nikhilnl_diffusion2d import solve

# default parameters
solve()

# or call with custom parameters
solve(dx=0.05, dy=0.05, D=2.0)
```

You will see four subplots showing the thermal diffusion at different times.

### Running from source (during development)

If using the local repository:

1. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
python -m pip install numpy matplotlib
```

3. Run the module directly:

```bash
python -m nikhilnl_diffusion2d.diffusion2d
```

## Citing

If needed, cite the source of the numerical example:

- "Learning Scientific Programming with Python", Chapter 7  
  https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/

You may also cite this package using a link to your TestPyPI page once uploaded.
