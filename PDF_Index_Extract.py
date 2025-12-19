import PyPDF2

def print_outline_with_filter(outlines, level=0):
    for item in outlines:
        if isinstance(item, list):
            print_outline_with_filter(item, level+1)
        else:
            if level == 1:
                if hasattr(item, 'children') and item.children:
                    has_third = any(
                        (hasattr(child, 'children') and child.children) or
                        (not isinstance(child, list) and hasattr(child, 'title'))
                        for child in item.children
                    )
                    if has_third:
                        print('  ' * level + '- ' + item.title)
                        for child in item.children:
                            if not isinstance(child, list) and hasattr(child, 'title'):
                                print('  ' * (level + 1) + '- ' + child.title)
                            elif isinstance(child, list):
                                print_outline_with_filter(child, level + 2)
            else:
                print_outline_with_filter(getattr(item, 'children', []), level+1)

with open(r"E:\Document\Academic\4\SA\CW2\Chaper7.pdf", "rb") as f:
    reader = PyPDF2.PdfReader(f)
    # 自动适配不同PyPDF2版本
    outlines = reader.outline if hasattr(reader, "outline") else reader.outlines
    if callable(outlines):
        outlines = outlines()
    print_outline_with_filter(outlines)