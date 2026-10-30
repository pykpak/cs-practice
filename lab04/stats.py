def parse_record(line: str) -> dict:
    parts = line.split(';')
    if len(parts) != 3:
        raise ValueError('Ожидается ровно 3 поля')

    city, temp, date = parts
    if not city or not date:
        raise ValueError("Город или дата пустые")
    try:
        temp = float(temp)
    except ValueError:
        raise ValueError("Температура не является числом")
    return {'city': city, 'temp': temp, 'date': date}


def read_valid(lines: list[str]) -> list[dict]:
    records = []
    for line in lines:
        if not line.strip():
            continue  # пустые строки пропускаем молча
        try:
            record = parse_record(line)
            records.append(record)
        except ValueError:
            continue  # негодную строку пропускаем
    return records

def average_by_city(records: list[dict]) -> dict:
    totals = {}
    counts = {}
    for record in records:
        city = record["city"]
        temp = record["temp"]
        totals[city] = totals.get(city, 0) + float(temp)
        counts[city] = counts.get(city, 0) + 1
        
    averages = {}
    for city in totals:
        # Считаем среднее и округляем до 1 знака после запятой
        averages[city] = round(totals[city] / counts[city], 1)
        
    return averages

def warmest_city(records: list[dict]) -> str:
    averages = average_by_city(records)
    if not averages:
        return ""

    sorted_cities = sorted(averages.keys())
    best_city = sorted_cities[0]
    best_temp = averages[best_city]
    
    for city in sorted_cities[1:]:
        if averages[city] > best_temp:
            best_temp = averages[city]
            best_city = city
            
    return best_city
