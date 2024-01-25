class Sorted:
    def __init__(self):
        pass

    def executed_sort(self, data):
        executed_list = []
        for i in data:
            if i.get("state") == "EXECUTED":
                executed_list.append(i)
        return executed_list

    def data_sort(self, data_list):
        return sorted(data_list, key=lambda x: x.get("date"), reverse=True)

