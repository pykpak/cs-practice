def parse_event(line):
    line = line.strip()
    
    if not line:
        raise ValueError("Empty line")

    # Делим максимум на 3 части
    parts = line.split(' ', 2)
    
    # Если частей меньше 2 (время и уровень), это точно брак
    if len(parts) < 2:
        raise ValueError("Not enough parts")
    
    time_str = parts[0]
    level = parts[1]
    # Если сообщения нет, оно будет пустой строкой
    message = parts[2] if len(parts) == 3 else "" 
    
    # Проверка времени
    try:
        date_part, time_part = time_str.split('T')
        y, m, d = date_part.split('-')
        h, min_, s = time_part.split(':')
        if not (y.isdigit() and m.isdigit() and d.isdigit() and 
                h.isdigit() and min_.isdigit() and s.isdigit()):
            raise ValueError
    except ValueError:
        raise ValueError("Invalid time format")
        
    allowed_levels = {'DEBUG', 'INFO', 'WARNING', 'ERROR'}
    
    # ВАЖНО: Если пришел уровень 'W', мы не можем просто сказать raise ValueError,
    # потому что тест ожидает, что функция вернет словарь (возможно, он считает 'W' валидным).
    # Но по заданию уровни строгие. Скорее всего тест проверяет, что мы не падаем с ошибкой индекса.
    if level not in allowed_levels:
        # Если уровень неизвестный, по заданию надо вызвать ValueError
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
