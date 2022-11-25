def jsonFindAttr(attr: str, jsonData):
    for k, v in jsonData.items():
        if k == attr:
            yield v
        elif isinstance(v, dict):
            for id_val in jsonFindAttr(attr, v):
                yield id_val
