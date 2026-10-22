from shared.contract import Block


def render(blocks: list[Block]) -> str:
    """Render allocated study blocks as a readable summary."""
    lines = []

    for block in blocks:
        lines.append(f"{block.task.title}: {block.hours:g} hours")

    return "\n".join(lines)