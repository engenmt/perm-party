import asyncio
import permpy as pp
from math import pow

# from pyscript import Element, display

from js import document


def get_random(n=4, N=5):
    for _ in range(N):
        p = str(pp.Perm.random(n))
        append_count_js(str(n), p)


def attempt_to_log(elt):
    print(f"{elt}:")
    for attr in ["id", "innerHtml", "innerHTML", "element"]:
        try:
            val = getattr(elt, attr)
        except AttributeError:
            continue
        print(f"\t{attr}: {val}")


def append_count_js(n, count):
    if n == 0:
        return

    table = document.querySelector("#table-enumeration tbody")

    row = document.createElement("tr")
    row_id = f"row-{n}"
    row.id = row_id

    cell_n = document.createElement("td")
    cell_n.id = f"n-{n}"
    cell_n.innerHTML = str(n)

    cell_count = document.createElement("td")
    cell_count.id = f"count-{n}"
    cell_count.innerHTML = str(count)

    cell_count_root = document.createElement("td")
    cell_count_root.id = f"count-root-{n}"
    cell_count_root.innerHTML = f"{pow(count, 1 / n): 6.3f}"

    row.append(cell_n)
    row.append(cell_count)
    row.append(cell_count_root)

    table.append(row)


def reset_table():
    while elt := document.querySelector("tr:not(:first-child)"):
        elt.remove()


async def enumerate_by_basis(basis, N):
    N = int(N)
    if N >= 10:
        return
    document.querySelector("button").disabled = True
    reset_table()

    basis = [pp.Perm(elt.strip()) for elt in basis.split(",")]
    A = pp.AvClass(basis, max_len=0)
    for n in range(1, N + 1):
        await asyncio.sleep(0.01)
        A.extend_by_one()
        append_count_js(n, len(A[-1]))

    document.querySelector("button").disabled = False
    # await asyncio.sleep(0.01)


document.querySelector("button").disabled = False


def main():
    pass


if __name__ == "__main__":
    main()
