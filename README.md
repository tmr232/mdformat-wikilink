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

[mdformat]: https://github.com/executablebooks/mdformat
