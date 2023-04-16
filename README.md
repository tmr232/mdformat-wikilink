# mdformat-wikilink

An [mdformat] plugin for ensuring that wiki-style links (`[[Target|Alias]]`)
are preserved during formatting.

Source:

```markdown
This is a [[link]].
```

With the plugin:

```markdown
This is a [[link]].
```

Without the plugin:

```markdown
This is a \[\[link\]\].
```

## Installation

After installing mdformat,

```bash
# With pip
pip install mdformat-wikilink

# With pipx
pipx inject mdformat mdformat-wikilink
```

[mdformat]: https://github.com/executablebooks/mdformat
