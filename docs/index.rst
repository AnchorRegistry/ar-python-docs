anchorregistry
==============

.. rst-class:: lead

   | **No API key. No account. No dependency on AnchorRegistry infrastructure.**
   | Just an RPC endpoint and the contract address.

----

``anchorregistry`` is a Python package for reading from the AnchorRegistry smart contract — a permanent, on-chain registry of digital artifacts deployed on Base (EVM L2). It proves that any registered artifact existed at a specific point in time, anchored immutably to a public blockchain.

The package queries the contract directly via JSON-RPC. There are no AnchorRegistry servers in the call path. Anyone can clone the repo, run the notebooks, and verify the registry independently — forever.

Installation
------------

.. code-block:: bash

   pip install anchorregistry

   # With DataFrame support
   pip install anchorregistry[analytics]

----

.. toctree::
   :maxdepth: 2
   :caption: Documentation

   quickstart
   configuration
   api
   contract

.. toctree::
   :maxdepth: 1
   :caption: Interactive Notebooks

   notebooks/quickstart
   notebooks/querying
   notebooks/recover
   notebooks/watermark
   notebooks/dataframe
   notebooks/authenticate

----

Links
-----

- `anchorregistry.com <https://anchorregistry.com>`_
- `anchorregistry.ai <https://anchorregistry.ai>`_
- `PyPI — anchorregistry <https://pypi.org/project/anchorregistry/>`_
- `GitHub — ar-python <https://github.com/icmoore/ar-python>`_
