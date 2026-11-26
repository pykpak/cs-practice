def count_by_extension(paths: list[str]) -> dict[str, int]:
    result = {}
    for path in paths:
        # Разделяем путь по последней точке, берем последнюю часть (расширение)
        parts = path.rsplit('.', 1)
        
        # Если точка есть, берем расширение в нижнем регистре, иначе пустая строка
        if len(parts) > 1:
            ext = parts[1].lower()
        else:
            ext = ""
        
        # Считаем количество
        result[ext] = result.get(ext, 0) + 1
        
    return result


def deepest_path(paths: list[str]) -> str:
    if not paths:
        return ""
        
    max_depth = -1
    deepest = ""
    
    for path in paths:
        # Вложенность = количество слешей '/'
        depth = path.count('/')
        
        # Если вложенность больше, или равна, но путь лексикографически меньше (первый по алфавиту)
        if depth > max_depth or (depth == max_depth and path < deepest):
            max_depth = depth
            deepest = path
            
    return deepest


