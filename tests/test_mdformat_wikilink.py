import textwrap

import mdformat


def test_preserve_link():
    md = "[[Target|Alias]] [[Target]]"

    assert mdformat.text(md, extensions={"wikilink"}).strip() == md.strip()


def test_only_real_links():
    unformatted_md = textwrap.dedent(
        """
    [[
    ]]
    [[What is this?
    [Yo
    ]]
    [ hello, [[World!
    """
    )

    formatted_md = textwrap.dedent(
        r"""
    \[\[
    \]\]
    \[\[What is this?
    \[Yo
    \]\]
    \[ hello, \[\[World!
    """
    )

    assert (
        mdformat.text(unformatted_md, extensions={"wikilink"}).strip()
        == formatted_md.strip()
    )
