from collections.abc import Mapping

from markdown_it import MarkdownIt
from mdformat.renderer import RenderContext, RenderTreeNode
from mdformat.renderer.typing import Render

from mdformat_wikilink.mdit_wikilink_plugin import wikilink_plugin


def update_mdit(mdit: MarkdownIt) -> None:
    mdit.use(wikilink_plugin)


def _render_wikilink(node: RenderTreeNode, context: RenderContext) -> str:
    return node.content


RENDERERS: Mapping[str, Render] = {"wikilink": _render_wikilink}
