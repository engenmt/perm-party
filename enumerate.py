import asyncio
import permpy as pp
from math import pow

from utils import AsyncTable, create_row, reset_table


async def enumerate_by_basis(basis, N):
    N = int(N)

    async with AsyncTable("table-enumeration") as table:
        if N:
            basis = [pp.Perm(elt.strip()) for elt in basis.split(",") if elt]
            A = pp.AvClass(basis, max_len=0)
            reset_table()

        for n in range(1, N + 1):
            A.extend_to_length(n)
            await asyncio.sleep(0.01)

            count = len(A[n])
            nth_root = pow(count, 1 / n)
            ratio = count / len(A[n - 1]) if n > 1 else 1.00

            row = await create_row(n, count, nth_root, ratio)
            table.append(row)
