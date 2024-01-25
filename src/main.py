from src.utils import load_operation
from src.sorted import Sorted
from src.mask import Mask


def solution():
    final_string = ""
    filename = "operations.json"
    operations = load_operation(filename)
    operations_list = Sorted()
    executed_list = operations_list.executed_sort(operations)
    data_sort = operations_list.data_sort(executed_list)
    mask_from = Mask()
    for i in data_sort[:5]:
        year, month, day = i["date"][:10].split('-')
        formatted_date = f"{day}.{month}.{year}"
        final_string += f"{formatted_date} {i["description"]}\n"
        if "from" in i:
            final_string += f"{mask_from.mask_number(i.get("from"))} -> {mask_from.mask_number(i.get("to"))}\n"
        else:
            final_string += f"{mask_from.mask_number(i.get("to"))}\n"
        final_string += f"{i.get("operationAmount").get("amount")} {i.get("operationAmount").get("currency").get("name")}\n\n"
    return final_string


if __name__ == '__main__':
    print(solution().rstrip())
