from gendiff.format_parser import deserialize


def generate_diff(path1, path2):

    def gen_diff(dict_was, dict_become):
        keys = sorted(dict_was.keys() | dict_become.keys())
        diff = []
        for key in keys:
            if key in dict_was and key not in dict_become:
                diff.append(f"  - {key}: {dict_was[key]}")
            elif key not in dict_was and key in dict_become:
                diff.append(f"  + {key}: {dict_become[key]}")
            elif dict_was[key] != dict_become[key]:
                diff.append(f"  - {key}: {dict_was[key]}")
                diff.append(f"  + {key}: {dict_become[key]}")
            else:
                diff.append(f"    {key}: {dict_was[key]}")
        return '{\n' + '\n'.join(diff) + '\n}'

    return gen_diff(deserialize(path1), deserialize(path2))
