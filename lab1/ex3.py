__len: str = input("Enter len > ")

__len = int(__len) if __len.isdigit() else ""
if __len < 0:
    __len = 0

if __len:
    for r in range(__len):
        row_data = list(
            map(
                str,
                reversed(range(1, __len + 1))
            )
        )

        row_data = row_data[0: -r if r else len(row_data)]
        print(" ".join(row_data))
