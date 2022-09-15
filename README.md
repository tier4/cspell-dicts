# cspell-dicts

TIER IV's dictionaries for [CSpell](https://github.com/streetsidesoftware/cspell).
The mechanism is a simplified version of [streetsidesoftware/cspell-dicts](https://github.com/streetsidesoftware/cspell-dicts).

## Installation

To install the dictionaries:

```bash
npm install -g yarn
yarn global add https://github.com/tier4/cspell-dicts
```

To link a dictionary:

```bash
cspell link add @tier4/cspell-dicts/{dict-name}/cspell-ext.json
```

Or import the dictionary in your `.cspell.json`.

```json
{
  ...
  "import": ["@tier4/cspell-dicts/{dict-name}/cspell-ext.json"],
  ...
}
```

To uninstall:

```bash
yarn global remove @tier4/cspell-dicts
```
