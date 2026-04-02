# anchorregistry — Documentation

Source for [anchorregistry.readthedocs.io](https://anchorregistry.readthedocs.io).

Built with Sphinx + nbsphinx + ReadTheDocs. Docs are generated from `.rst` pages and executable Jupyter notebooks that run against the live AnchorRegistry contract.

---

## Structure

```
docs/
├── conf.py                  # Sphinx configuration
├── index.rst                # Landing page + toctree
├── quickstart.rst           # pip install → first call → output
├── configuration.rst        # configure(), env vars, network switching
├── api.rst                  # autodoc — all public functions
├── contract.rst             # contract reference — address, ABI, Etherscan
├── requirements.txt         # ReadTheDocs build dependencies
│
└── notebooks/
    ├── quickstart.ipynb     # get_by_arid — single anchor, live output
    ├── querying.ipynb       # all five query functions demonstrated
    ├── recover.ipynb        # full registry reconstruction — the trust proof
    ├── watermark.ipynb      # SPDX-Anchor / DAPX-Anchor generation
    ├── dataframe.ipynb      # to_dataframe() — analytics use case
    └── authenticate.ipynb   # trustless initiation proof — authenticate_anchor / authenticate_tree
```

---

## Build locally

```bash
# Install dependencies
pip install sphinx sphinx-rtd-theme nbsphinx ipython anchorregistry
brew install pandoc   # required by nbsphinx

# Build
sphinx-build -b html docs docs/_build/html

# View
open docs/_build/html/index.html
```

Clean rebuild:

```bash
rm -rf docs/_build && sphinx-build -b html docs docs/_build/html
```

---

## Notebooks

Notebooks use `nbsphinx_execute = "never"` — outputs are pre-saved from real Sepolia runs. The docs build fast and reliably on ReadTheDocs without needing an RPC endpoint at build time.

To re-execute notebooks against Sepolia:

```bash
pip install jupyter anchorregistry

# Set your RPC endpoint
export BASE_RPC_URL=https://sepolia.infura.io/v3/YOUR_KEY

jupyter nbconvert --to notebook --execute --inplace docs/notebooks/*.ipynb
```

After mainnet deploy, re-run against mainnet and save new outputs before publishing.

---

## ReadTheDocs

Auto-builds on every push to `main`. Build config: [`.readthedocs.yaml`](.readthedocs.yaml).

---

## Related

- [`anchorregistry`](https://pypi.org/project/anchorregistry/) — Python package on PyPI
- [`ar-python`](https://github.com/icmoore/ar-python) — package source
- [anchorregistry.com](https://anchorregistry.com)
- [anchorregistry.ai](https://anchorregistry.ai)
