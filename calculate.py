import circle
import square
import triangle

FIGS = ['circle', 'square', 'triangle']
FUNCS = ['perimeter', 'area']
SIZES = {
    'circle-area': 1,
    'circle-perimeter': 1,
    'square-area': 1,
    'square-perimeter': 1,
    'triangle-area': 3,
    'triangle-perimeter': 3,
}


def calc(fig, func, size):
    """Calculate area or perimeter of a given figure."""
    assert fig in FIGS, "Invalid figure"
    assert func in FUNCS, "Invalid function"

    key = f'{fig}-{func}'
    args = SIZES.get(key)
    assert args is not None, "Invalid size configuration"
    assert len(size) == args, "Invalid number of arguments"

    assert all(s >= 0 for s in size), "Sizes must be non-negative"

    if fig == "triangle":
        a, b, c = size
        assert a + b > c and a + c > b and b + c > a, "Invalid triangle sides"

    result = eval(f'{fig}.{func}(*{size})')
    return result


if __name__ == "__main__":
    func = ''
    fig = ''
    size = []

    while fig not in FIGS:
        fig = input(f"Enter figure name, available are {FIGS}:\n")

    while func not in FUNCS:
        func = input(f"Enter function name, available are {FUNCS}:\n")

    while len(size) != SIZES.get(f"{fig}-{func}", 1):
        size = list(map(int, input(
            "Input figure sizes separated by space, "
            "1 for circle and square:\n"
        ).split()))

    result = calc(fig, func, size)
    print(f"Result: {result}")
