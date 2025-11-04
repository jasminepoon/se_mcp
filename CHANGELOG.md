# Changelog

## 0.2.1 (2025-11-04)

Full Changelog: [v0.2.0...v0.2.1](https://github.com/jasminepoon/se_mcp/compare/v0.2.0...v0.2.1)

### Bug Fixes

* **client:** close streams without requiring full consumption ([7f33f66](https://github.com/jasminepoon/se_mcp/commit/7f33f662bc2460b6781a6b9bc1c0c1b57574b42d))


### Chores

* bump `httpx-aiohttp` version to 0.1.9 ([eb2efc3](https://github.com/jasminepoon/se_mcp/commit/eb2efc3fd441c43a604997939e68513dad352236))
* do not install brew dependencies in ./scripts/bootstrap by default ([f486875](https://github.com/jasminepoon/se_mcp/commit/f4868751dc4a96fd838797703d477f543485cd24))
* **internal/tests:** avoid race condition with implicit client cleanup ([5a2d98d](https://github.com/jasminepoon/se_mcp/commit/5a2d98d71ab141dc3546871cd57dbe23d552905c))
* **internal:** codegen related update ([ebd2fdc](https://github.com/jasminepoon/se_mcp/commit/ebd2fdc7d8aa51129b1acd66816dda80093e5f3a))
* **internal:** detect missing future annotations with ruff ([cfee284](https://github.com/jasminepoon/se_mcp/commit/cfee2842e571e2c741c5a5601ca03c7af09007e1))
* **internal:** grammar fix (it's -&gt; its) ([a63ca8e](https://github.com/jasminepoon/se_mcp/commit/a63ca8ee937dea2d16fe99e8431959e172fad243))
* **internal:** update pydantic dependency ([5b5fb07](https://github.com/jasminepoon/se_mcp/commit/5b5fb0795bc05b3669bc48ac4bc4932461996d08))
* **tests:** simplify `get_platform` test ([082b778](https://github.com/jasminepoon/se_mcp/commit/082b778d19df98d7c1a90fe63146168a8d092d92))
* **types:** change optional parameter type from NotGiven to Omit ([318e729](https://github.com/jasminepoon/se_mcp/commit/318e729e4047ab85c676ea227418d921019d6e41))

## 0.2.0 (2025-09-04)

Full Changelog: [v0.1.0...v0.2.0](https://github.com/jasminepoon/se_mcp/compare/v0.1.0...v0.2.0)

### Features

* improve future compat with pydantic v3 ([8baadf3](https://github.com/jasminepoon/se_mcp/commit/8baadf380e7deb35d0e61ed5c3d3f000ab5d3495))
* **types:** replace List[str] with SequenceNotStr in params ([0e9109a](https://github.com/jasminepoon/se_mcp/commit/0e9109acbd377afe043101f886294d5b6f53e5c4))


### Bug Fixes

* avoid newer type syntax ([29fdc96](https://github.com/jasminepoon/se_mcp/commit/29fdc9696674990e964baf46c9dbd8daf2da3ed6))


### Chores

* **internal:** add Sequence related utils ([70045fd](https://github.com/jasminepoon/se_mcp/commit/70045fdae3e33f61239583c5d37d595662245b34))
* **internal:** change ci workflow machines ([165c72b](https://github.com/jasminepoon/se_mcp/commit/165c72b5e32a891b0723d39c42c986d8d9d67988))
* **internal:** update pyright exclude list ([79b16b1](https://github.com/jasminepoon/se_mcp/commit/79b16b154f7a238da9d0e050ab9c5e20292f4055))
* update github action ([ddda9da](https://github.com/jasminepoon/se_mcp/commit/ddda9dacb282388b5273f694821ba793f5f3fede))

## 0.1.0 (2025-08-16)

Full Changelog: [v0.0.1...v0.1.0](https://github.com/jasminepoon/se_mcp/compare/v0.0.1...v0.1.0)

### Features

* **api:** update via SDK Studio ([b0045eb](https://github.com/jasminepoon/se_mcp/commit/b0045eb51c672334283daa1789fb3c0d1bc2ce86))


### Chores

* update SDK settings ([4f9411a](https://github.com/jasminepoon/se_mcp/commit/4f9411abf7c2d061d79d4e04e8525251b3f72ee4))
* update SDK settings ([2b80ee4](https://github.com/jasminepoon/se_mcp/commit/2b80ee4efa69f9447ca0da73170af64f60616dd1))
