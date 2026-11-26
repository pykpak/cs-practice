from logstats import count_levels, top_errors, format_report

def main():
    file_name = input().strip()
    
    try:
        with open(file_name, encoding="utf-8") as f:
            lines = f.readlines()
            
        valid_lines = [line for line in lines if line.strip()]
        total_lines = len(valid_lines)
        
        counts = count_levels(lines)
        errors = top_errors(lines, 3)
        
        error_count = counts.get("ERROR", 0)
        broken_count = counts.get("BROKEN", 0)
        
        print(total_lines)
        print(error_count)
        print(broken_count)
        
        report_text = format_report(counts, errors)
        with open("report.txt", "w", encoding="utf-8") as out:
            out.write(report_text)
            
    except FileNotFoundError:
        print(f"Файл {file_name} не найден")
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()