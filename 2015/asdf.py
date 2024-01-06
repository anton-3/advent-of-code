import functools
import sys

OPERATORS = {
    None: lambda arg: arg(0),
    "NOT": lambda arg: ~arg(1),
    "AND": lambda arg: arg(0) & arg(2),
    "OR": lambda arg: arg(0) | arg(2),
    "LSHIFT": lambda arg: arg(0) << arg(2),
    "RSHIFT": lambda arg: arg(0) >> arg(2),
}

class Solver:
    def __init__(self, operators, definitions):
        self._operators = operators
        self._definitions = definitions

    @functools.lru_cache()
    def get(self, key):
        try:
            value = int(key)
        except ValueError:
            cmd = self._definitions[key].split(" ")
            operator = self._parse_operator(cmd)
            argument = functools.partial(self._get_argument, cmd)
            value = self._operators[operator](argument)

        return value

    def replace(self, update):
        return Solver(self._operators, {**self._definitions, **update})

    def _parse_operator(self, cmd):
        return next((x for x in self._operators if x in cmd), None)

    def _get_argument(self, cmd, index):
        return self.get(cmd[index])

def read_input(stream):
    lines = stream.readlines()
    pairs = (x.strip().split(" -> ") for x in lines)
    return {k: v for v, k in pairs}

if __name__ == "__main__":
    part1 = Solver(OPERATORS, read_input(sys.stdin))
    result1 = part1.get("a")
    print(result1)

    part2 = part1.replace({"b": str(result1)})
    result2 = part2.get("a")
    print(result2)
