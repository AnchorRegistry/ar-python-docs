Contract Reference
==================

Deployed Contract
-----------------

.. list-table::
   :header-rows: 1
   :widths: 18 45 18 19

   * - Network
     - Address
     - Deploy Block
     - Etherscan
   * - Base mainnet
     - TBD
     - TBD
     - TBD
   * - Sepolia testnet
     - ``0xE772B7f4eC4a92109b8b892Add205ede7c850DBa``
     - 10575629
     - `View on Etherscan <https://sepolia.etherscan.io/address/0xE772B7f4eC4a92109b8b892Add205ede7c850DBa>`_

Anchored Event
--------------

The ``Anchored`` event is emitted once per registration. It is the sole source of truth for reconstructing the registry from on-chain data.

.. code-block:: solidity

   event Anchored(
       string  indexed arId,           // AR-ID (keccak256 indexed)
       address indexed registrant,     // wallet that called anchor()
       uint8           artifactType,   // ArtifactType enum value (0–23)
       string          arIdPlain,      // AR-ID plain text (not indexed)
       string          descriptor,     // short descriptor / subtitle
       string          title,          // artifact title
       string          author,         // human-readable author / org name
       string          manifestHash,   // content hash (SHA-256 or IPFS CID)
       string          parentArId,     // parent AR-ID ("" if root)
       string  indexed treeId,         // tree identifier (keccak256 indexed)
       string          treeIdPlain,    // tree identifier plain text
       bytes32         tokenCommitment // keccak256(K || arId), bytes32(0) for governance
   );

**Field descriptions:**

.. list-table::
   :header-rows: 1
   :widths: 22 12 66

   * - Field
     - Type
     - Description
   * - ``arId``
     - ``string``
     - Unique AnchorRegistry identifier, e.g. ``AR-2026-x1llnO1``. Indexed — stored as ``keccak256`` in logs.
   * - ``registrant``
     - ``address``
     - Ethereum address of the wallet that submitted the ``anchor()`` transaction.
   * - ``artifactType``
     - ``uint8``
     - Integer index into the ``ArtifactType`` enum (0–22). See the type taxonomy below.
   * - ``arIdPlain``
     - ``string``
     - Human-readable AR-ID. Identical to ``arId`` but not indexed — readable from log data.
   * - ``descriptor``
     - ``string``
     - Short subtitle or descriptor for the artifact.
   * - ``title``
     - ``string``
     - Full title of the artifact.
   * - ``author``
     - ``string``
     - Human-readable author or organization name.
   * - ``manifestHash``
     - ``string``
     - Content hash (SHA-256 hex or IPFS CID) proving the artifact's content at registration time.
   * - ``parentArId``
     - ``string``
     - AR-ID of the parent artifact. Empty string ``""`` if this is a root anchor.
   * - ``treeId``
     - ``string``
     - Identifier for the artifact tree this anchor belongs to. Indexed.
   * - ``treeIdPlain``
     - ``string``
     - Human-readable tree identifier. Identical to ``treeId`` but not indexed.
   * - ``tokenCommitment``
     - ``bytes32``
     - Ownership proof: ``keccak256(K || arId)`` for user-initiated anchors, ``bytes32(0)`` for governance anchors. ``K`` is the ownership token known only to the registrant.

Sealed Event
------------

The ``Sealed`` event is emitted when a tree root is sealed via ``registerSeal``. A sealed tree is authentic and complete — no new anchors may be appended. AR governance (VOID, REVIEW, AFFIRMED) can still target anchors within sealed trees.

.. code-block:: solidity

   event Sealed(
       string  indexed arId,            // root AR-ID being sealed
       string          newTreeRoot,      // optional continuation pointer
       string          reason,           // human-readable reason
       uint256         sealedAtBlock,    // block number of seal
       bytes32         tokenCommitment   // H(K || C_seal) — always non-zero
   );

READ_ABI
--------

The minimal ABI used by ``anchorregistry`` to read from the contract. This is the only ABI needed — the package never writes to the contract.

.. code-block:: python

   READ_ABI = [
       # Anchored event
       {
           "anonymous": False,
           "name": "Anchored",
           "type": "event",
           "inputs": [
               {"indexed": True,  "internalType": "string",            "name": "arId",         "type": "string"},
               {"indexed": True,  "internalType": "address",           "name": "registrant",   "type": "address"},
               {"indexed": False, "internalType": "enum ArtifactType", "name": "artifactType", "type": "uint8"},
               {"indexed": False, "internalType": "string",            "name": "arIdPlain",    "type": "string"},
               {"indexed": False, "internalType": "string",            "name": "descriptor",   "type": "string"},
               {"indexed": False, "internalType": "string",            "name": "title",        "type": "string"},
               {"indexed": False, "internalType": "string",            "name": "author",       "type": "string"},
               {"indexed": False, "internalType": "string",            "name": "manifestHash", "type": "string"},
               {"indexed": False, "internalType": "string",            "name": "parentArId",   "type": "string"},
               {"indexed": True,  "internalType": "string",            "name": "treeId",       "type": "string"},
               {"indexed": False, "internalType": "string",            "name": "treeIdPlain",  "type": "string"},
               {"indexed": False, "internalType": "bytes32",           "name": "tokenCommitment", "type": "bytes32"},
           ],
       },
       # Sealed event
       {
           "anonymous": False,
           "name": "Sealed",
           "type": "event",
           "inputs": [
               {"indexed": True,  "internalType": "string",  "name": "arId",            "type": "string"},
               {"indexed": False, "internalType": "string",  "name": "newTreeRoot",      "type": "string"},
               {"indexed": False, "internalType": "string",  "name": "reason",           "type": "string"},
               {"indexed": False, "internalType": "uint256", "name": "sealedAtBlock",    "type": "uint256"},
               {"indexed": False, "internalType": "bytes32", "name": "tokenCommitment",  "type": "bytes32"},
           ],
       },
       # isSealed(arId) → bool
       {
           "type": "function",
           "name": "isSealed",
           "stateMutability": "view",
           "inputs":  [{"internalType": "string", "name": "", "type": "string"}],
           "outputs": [{"internalType": "bool",   "name": "", "type": "bool"}],
       },
       # sealContinuation(arId) → string
       {
           "type": "function",
           "name": "sealContinuation",
           "stateMutability": "view",
           "inputs":  [{"internalType": "string", "name": "", "type": "string"}],
           "outputs": [{"internalType": "string", "name": "", "type": "string"}],
       },
       # registered(arId) → bool
       {
           "type": "function",
           "name": "registered",
           "stateMutability": "view",
           "inputs":  [{"internalType": "string", "name": "", "type": "string"}],
           "outputs": [{"internalType": "bool",   "name": "", "type": "bool"}],
       },
       # getAnchorData(arId) → bytes
       {
           "type": "function",
           "name": "getAnchorData",
           "stateMutability": "view",
           "inputs":  [{"internalType": "string", "name": "arId", "type": "string"}],
           "outputs": [{"internalType": "bytes",  "name": "",     "type": "bytes"}],
       },
       # anchorTypes(arId) → uint8
       {
           "type": "function",
           "name": "anchorTypes",
           "stateMutability": "view",
           "inputs":  [{"internalType": "string",  "name": "",  "type": "string"}],
           "outputs": [{"internalType": "uint8",   "name": "",  "type": "uint8"}],
       },
   ]

Artifact Types
--------------

Twenty-four artifact types in eight logical groups. The ``artifact_type_name`` field in every record contains the string name. The ``artifactType`` field in the raw event contains the integer index.

.. list-table::
   :header-rows: 1
   :widths: 10 18 18 54

   * - Index
     - Name
     - Category
     - Type-specific ``data`` fields
   * - 0
     - ``CODE``
     - Content
     - ``git_hash``, ``license``, ``language``, ``version``, ``url``
   * - 1
     - ``RESEARCH``
     - Content
     - ``doi``, ``institution``, ``co_authors``, ``url``
   * - 2
     - ``DATA``
     - Content
     - ``data_version``, ``format``, ``row_count``, ``schema_url``, ``url``
   * - 3
     - ``MODEL``
     - Content
     - ``model_version``, ``architecture``, ``parameters``, ``training_dataset``, ``url``
   * - 4
     - ``AGENT``
     - Content
     - ``agent_version``, ``runtime``, ``capabilities``, ``url``
   * - 5
     - ``MEDIA``
     - Content
     - ``media_type``, ``platform``, ``format``, ``duration``, ``isrc``, ``url``
   * - 6
     - ``TEXT``
     - Content
     - ``text_type``, ``isbn``, ``publisher``, ``language``, ``url``
   * - 7
     - ``POST``
     - Content
     - ``platform``, ``post_id``, ``post_date``, ``url``
   * - 8
     - ``ONCHAIN``
     - Content
     - ``chain_id``, ``asset_type``, ``contract_address``, ``tx_hash``, ``token_id``, ``block_number``, ``url``
   * - 9
     - ``REPORT``
     - Content
     - ``report_type``, ``client``, ``engagement``, ``version``, ``authors``, ``institution``, ``url``, ``file_manifest_hash``
   * - 10
     - ``NOTE``
     - Content
     - ``note_type``, ``date``, ``participants``, ``url``, ``file_manifest_hash``
   * - 11
     - ``WEBSITE``
     - Content
     - ``url``, ``platform``, ``description``
   * - 12
     - ``EVENT``
     - Lifecycle
     - ``executor``, ``event_type``, ``event_date``, ``location``, ``orchestrator``, ``url``
   * - 13
     - ``RECEIPT``
     - Transaction
     - ``receipt_type``, ``merchant``, ``amount``, ``currency``, ``order_id``, ``platform``, ``url``, ``file_manifest_hash``
   * - 14
     - ``LEGAL``
     - Gated
     - ``doc_type``, ``jurisdiction``, ``parties``, ``effective_date``, ``url``
   * - 15
     - ``ENTITY``
     - Gated
     - ``entity_type``, ``entity_domain``, ``verification_method``, ``verification_proof``, ``canonical_url``, ``document_hash``
   * - 16
     - ``PROOF``
     - Gated
     - ``proof_type``, ``proof_system``, ``circuit_id``, ``vkey_hash``, ``audit_firm``, ``audit_scope``, ``verifier_url``, ``report_url``, ``proof_hash``
   * - 17
     - ``SEAL``
     - Self-service
     - *(registered via dedicated* ``registerSeal`` *function, not* ``registerContent`` *)*
   * - 18
     - ``RETRACTION``
     - Self-service
     - ``reason``, ``replaced_by``
   * - 19
     - ``REVIEW``
     - Review
     - ``review_type``, ``evidence_url``
   * - 20
     - ``VOID``
     - Review
     - ``review_ar_id``, ``finding_url``, ``evidence``
   * - 21
     - ``AFFIRMED``
     - Review
     - ``affirmed_by``, ``finding_url``
   * - 22
     - ``ACCOUNT``
     - Billing
     - ``capacity`` *(uint256)*
   * - 23
     - ``OTHER``
     - Catch-all
     - ``kind``, ``platform``, ``url``, ``value``, ``file_manifest_hash``
