from js import document


def attempt_to_log(elt):
    print(f"{elt}:")
    for attr in ["id", "innerHtml", "innerHTML", "element"]:
        try:
            val = getattr(elt, attr)
        except AttributeError:
            continue
        print(f"\t{attr}: {val}")


def disable_button():
    document.querySelector("button").disabled = True


def enable_button():
    document.querySelector("button").disabled = False


class AsyncTable:
    def __init__(self, table_id):
        self.table_id = table_id

    async def __aenter__(self):
        disable_button()
        table_element = document.querySelector(f"#{self.table_id} tbody")
        return table_element

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        enable_button()


async def create_row(n, *args, num_decimal_places=2):
    if n == 0:
        reset_table()
        return

    row = document.createElement("tr")

    cell_n = document.createElement("th")
    cell_n.scope = "row"
    cell_n.innerHTML = f"{n}"
    row.append(cell_n)
    for val in args:
        cell = document.createElement("td")
        if isinstance(val, int):
            cell.innerHTML = f"{val}"
        else:
            cell.innerHTML = f"{val:.{num_decimal_places}f}"
        row.append(cell)

    return row


def reset_table():
    document.querySelector("tbody").innerHTML = ""
    # while elt := document.querySelector("tr:not(:first-child)"):
    #     elt.remove()


enable_button()
