from collections.abc import Mapping
from markdown_it import MarkdownIt
from mdformat.renderer import RenderTreeNode, RenderContext
from mdformat.renderer.typing import Render
from mdformat_wikilink.mdit_wikilink_plugin import wikilink_plugin


def update_mdit(mdit: MarkdownIt) -> None:
    """Update the parser, e.g. by adding a plugin: `mdit.use(myplugin)`"""
    mdit.use(wikilink_plugin)


def _render_wikilink(node: RenderTreeNode, context: RenderContext) -> str:
    return node.content


# A mapping from `RenderTreeNode.type` value to a `Render` function that can
# render the given `RenderTreeNode` type. These functions override the default
# `Render` funcs defined in `mdformat.renderer.DEFAULT_RENDERERS`.
RENDERERS: Mapping[str, Render] = {"wikilink": _render_wikilink}
