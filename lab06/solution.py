def count_by_extension(paths: list[str]) -> dict[str, int]:
    result = {}
    for path in paths:
        parts = path.rsplit('.', 1)
        
        if len(parts) > 1:
            ext = parts[1].lower()
        else:
            ext = ""
        
        result[ext] = result.get(ext, 0) + 1
        
    return result


def deepest_path(paths: list[str]) -> str:
    if not paths:
        return ""
        
    max_depth = -1
    deepest = ""
    
    for path in paths:
        depth = path.count('/')

        if depth > max_depth or (depth == max_depth and path < deepest):
            max_depth = depth
            deepest = path
            
    return deepest


def human_size(n_bytes: int) -> str:
    if n_bytes == 0:
        return "0 Б"

    units = ["Б", "КБ", "МБ", "ГБ", "ТБ"]

    size = float(n_bytes)
    unit_index = 0
    
    while size >= 1024 and unit_index < len(units) - 1:
        size /= 1024
        unit_index += 1

    if unit_index == 0:
        return f"{int(size)} {units[unit_index]}"
    else:
        return f"{size:.1f} {units[unit_index]}"