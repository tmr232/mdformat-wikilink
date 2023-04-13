import re


from markdown_it import MarkdownIt
from markdown_it.rules_inline import StateInline

LINK_PATTERN = re.compile(r"\[\[([^[|\]\n])+(\|[^]\n]+)?]]")


def _wikilink_inline(state: StateInline, silent: bool) -> bool:
    match = LINK_PATTERN.match(state.src[state.pos :])
    if not match:
        return False

    token = state.push("wikilink", "", 0)
    token.content = match.group()

    state.pos += match.end()

    return True


def _wikilink_render(self, tokens, idx, options, env) -> str:
    return tokens[idx].content


def wikilink_plugin(md: MarkdownIt) -> None:
    md.inline.ruler.push("wikilink", _wikilink_inline)
    md.add_render_rule("wikilink", _wikilink_render)
