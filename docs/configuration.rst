Configuration
=============

``anchorregistry`` resolves its configuration through a four-level priority chain. Higher levels override lower ones.

Priority chain (highest → lowest)
----------------------------------

1. **Explicit call to** ``configure()`` — always wins
2. **Environment variables** — ``ANCHOR_REGISTRY_ADDRESS``, ``BASE_RPC_URL``, ``NETWORK``
3. **Network preset** — built-in defaults for ``"base"`` and ``"sepolia"``
4. **Package defaults** — falls back to Sepolia testnet if nothing is set

Environment variables
---------------------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Variable
     - Description
   * - ``NETWORK``
     - Network preset to use: ``"base"`` or ``"sepolia"``
   * - ``BASE_RPC_URL``
     - Full JSON-RPC endpoint URL (overrides preset RPC)
   * - ``ANCHOR_REGISTRY_ADDRESS``
     - Contract address (overrides preset address)

Example ``.env`` file:

.. code-block:: bash

   NETWORK=sepolia
   BASE_RPC_URL=https://sepolia.infura.io/v3/YOUR_KEY

``configure()`` function
------------------------

.. code-block:: python

   from anchorregistry import configure

   configure(
       network="base",          # "base" or "sepolia"
       rpc_url="https://...",   # override RPC endpoint
       contract_address="0x...",# override contract address
   )

All parameters are optional. Pass only what you need to override.

Network presets
---------------

.. list-table::
   :header-rows: 1
   :widths: 20 45 20 15

   * - Network
     - Contract Address
     - Deploy Block
     - Chain ID
   * - Base mainnet
     - TBD — mainnet deploy
     - TBD
     - 8453
   * - Sepolia testnet
     - ``0x9dAb9f5B754f8C56B5F7BAd3E92A8bDe7317AD29``
     - 10562312
     - 11155111

Switching networks within a process
-------------------------------------

``configure()`` is idempotent — call it again to switch networks:

.. code-block:: python

   from anchorregistry import configure, get_by_arid

   # Query Sepolia
   configure(network="sepolia")
   record = get_by_arid("AR-2026-x1llnO1")

   # Switch to mainnet
   configure(network="base")
   record = get_by_arid("AR-2026-x1llnO1")

Using a custom RPC endpoint
---------------------------

Any EVM-compatible JSON-RPC endpoint works — Infura, Alchemy, QuickNode, or your own node:

.. code-block:: python

   configure(
       network="sepolia",
       rpc_url="https://sepolia.infura.io/v3/YOUR_PROJECT_ID",
   )

No AnchorRegistry account or API key is required at any point.
