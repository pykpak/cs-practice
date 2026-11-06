from logstats import parse_event, count_levels, top_errors, format_report

# 2. Первый проход: считаем уровни
with open('events.log', 'r', encoding='utf-8') as file:
    counts = count_levels(file)

# 3. Второй проход: ищем топ ошибок (судя по примеру, n=3, но можно поставить любое)
with open('events.log', 'r', encoding='utf-8') as file:
    errors = top_errors(file, 3)

# Выводим три требуемых числа в консоль
total_lines = sum(counts.values())
error_lines = counts.get('ERROR', 0)
broken_lines = counts.get('BROKEN', 0)

print(total_lines)
print(error_lines)
print(broken_lines)

# 4. Формируем и записываем отчет в файл
report_text = format_report(counts, errors)

with open('report.txt', 'w', encoding='utf-8') as report_file:
    report_file.write(report_text)
