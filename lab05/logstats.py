def parse_event(line: str) -> dict:
    parts = line.split(maxsplit=2)  
    if len(parts) < 3:
        raise ValueError("Недостаточно данных в строке")
    
    time_str, level, message = parts
    
    valid_levels = {"DEBUG", "INFO", "WARNING", "ERROR"}
    if level not in valid_levels:
        raise ValueError(f"Неизвестный уровень: {level}")
    
    return {"time": time_str, "level": level, "message": message}


def count_levels(lines) -> dict:
    counts = {
        "DEBUG": 0,
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0,
        "BROKEN": 0
    }
    
    for line in lines:
        if not line.strip():
            continue
            
        try:
            event = parse_event(line)
            counts[event["level"]] += 1
        except ValueError:
            counts["BROKEN"] += 1
            
    return counts


def top_errors(lines, n: int) -> list:
    error_messages = {}
    
    for line in lines:
        if not line.strip():
            continue
            
        try:
            event = parse_event(line)
            if event["level"] == "ERROR":
                msg = event["message"]
                error_messages[msg] = error_messages.get(msg, 0) + 1
        except ValueError:
            pass
            
    
    sorted_errors = sorted(error_messages.items(), key=lambda x: (-x[1], x[0]))
    
    return [list(item) for item in sorted_errors[:n]]


def format_report(counts: dict, errors: list) -> str:
    report = "Отчёт по журналу\n\n"
    
    for level in sorted(counts.keys()):
        report += f"{level}: {counts[level]}\n"
        
    report += "\nЧастые ошибки:\n"
    
    if not errors:
        report += "- Нет ошибок\n"
    else:
        for msg, count in errors:
            report += f"- {msg} — {count}\n"
            
    return report