import asyncio
import permpy as pp

from pyscript import Element, display

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

    n = str(n)
    count = str(count)

    table = document.getElementById("table-enumeration")
    attempt_to_log(table)

    row = document.createElement("tr")
    row_id = f"row-{n}"
    row.id = row_id
    attempt_to_log(row)

    cell_n = document.createElement("td")
    cell_n.id = f"n-{n}"
    cell_n.innerHTML = n
    attempt_to_log(cell_n)

    cell_count = document.createElement("td")
    cell_count.id = f"count-{n}"
    cell_count.innerHTML = count
    attempt_to_log(cell_count)

    row.append(cell_n)
    row.append(cell_count)
    attempt_to_log(row)
    table.append(row)
    attempt_to_log(table)


async def enumerate_by_basis(basis, N):
    N = int(N)
    basis = [pp.Perm(elt.strip()) for elt in basis.split(",")]
    A = pp.AvClass(basis, max_len=0)
    for n in range(1, N + 1):
        await asyncio.sleep(0.01)
        A.extend_by_one()
        append_count_js(n, len(A[-1]))


def main():
    pass


if __name__ == "__main__":
    main()
