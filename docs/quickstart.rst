Quickstart
==========

Get to a working first call in under 2 minutes.

Installation
------------

.. code-block:: bash

   pip install anchorregistry

   # With DataFrame support
   pip install anchorregistry[analytics]

Configure
---------

.. code-block:: python

   from anchorregistry import configure

   configure(network="sepolia")   # Sepolia testnet
   # configure(network="base")   # Base mainnet

Your first anchor
-----------------

.. code-block:: python

   from anchorregistry import configure, get_by_arid

   configure(network="sepolia")
   record = get_by_arid("AR-2026-x1llnO1")

   record["title"]              # → artifact title
   record["author"]             # → registrant name
   record["artifact_type_name"] # → e.g. "CODE"
   record["data"]               # → type-specific fields dict

Every record has two levels:

- **Universal fields** — ``ar_id``, ``title``, ``author``, ``artifact_type_name``, ``manifest_hash``, ``registrant``, ``tree_id``, ``parent_ar_id``, ``block_number``, ``tx_hash``
- **Type-specific fields** — nested under ``record["data"]`` — keys depend on ``artifact_type_name``

----

See the interactive version: :doc:`notebooks/quickstart`
