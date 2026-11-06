def parse_event(line):
    line = line.strip()
    
    # Если строка пустая, сразу вызываем ошибку
    if not line:
        raise ValueError("Empty line")

    # Твоя идея проверки времени (строки 3 и 4). 
    # Мы делим строку по пробелам максимум на 3 части.
    parts = line.split(' ', 2)
    
    if len(parts) < 3:
        raise ValueError("Not enough parts")
    
    time_str, level, message = parts
    
    # Проверка времени: делим по 'T', затем по '-', затем по ':'
    try:
        date_part, time_part = time_str.split('T')
        y, m, d = date_part.split('-')
        h, min_, s = time_part.split(':')
        # Проверяем, что все кусочки состоят из цифр
        if not (y.isdigit() and m.isdigit() and d.isdigit() and 
                h.isdigit() and min_.isdigit() and s.isdigit()):
            raise ValueError
    except ValueError:
        # Если не получилось разбить или там буквы — строка испорчена
        raise ValueError("Invalid time format")
        
    # Проверка уровня (по условию только 4 разрешенных)
    allowed_levels = {'DEBUG', 'INFO', 'WARNING', 'ERROR'}
    if level not in allowed_levels:
        raise ValueError("Unknown level")

    return {'time': time_str, 'level': level, 'message': message}


def count_levels(lines):
    counts = {}
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
            lvl = event['level']
            counts[lvl] = counts.get(lvl, 0) + 1
        except ValueError:
            # Испорченные строки считаем под ключом BROKEN
            counts['BROKEN'] = counts.get('BROKEN', 0) + 1
    return counts


def top_errors(lines, n):
    errors_dict = {}
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
            if event['level'] == 'ERROR':
                msg = event['message']
                errors_dict[msg] = errors_dict.get(msg, 0) + 1
        except ValueError:
            pass # Испорченные строки здесь игнорируем
            
    # Превращаем в список пар [сообщение, количество]
    result = [[msg, count] for msg, count in errors_dict.items()]
    
    # Сортируем: сначала по убыванию количества (-x[1]), потом по алфавиту (x[0])
    result.sort(key=lambda x: (-x[1], x[0]))
    
    return result[:n]


def format_report(counts, errors):
    # Формируем текст отчета
    report = "Отчёт по журналу\n\n"
    
    # Выводим уровни по алфавиту
    for level in sorted(counts.keys()):
        report += f"{level}: {counts[level]}\n"
        
    report += "\nЧастые ошибки:\n"
    if not errors:
        report += "-\n"
    else:
        for msg, count in errors:
            report += f"- {msg} — {count}\n"
            
    return report
