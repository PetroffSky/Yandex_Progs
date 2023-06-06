

def script_120():
    with open("input_stroke.txt", "r", encoding="utf-8") as infile, \
        open("output_stroke.txt", "w", encoding="utf-8") as outfile:

        for index, stroke in enumerate(infile.read().split("\n"), 1):
            if index > 8:
                print(f"Количество строк достигло больше 8, а именно {index}")
            elif len(stroke) > 120:
                print(f"Длина {index}-й строки {len(stroke)} символов")
                break
            elif len(stroke) > 0:
                print(f"Длина строки {len(stroke)} символов")
                new_stroke = f"— {stroke}  \n"
                outfile.write(new_stroke)

                

def script_180():
    with open("input_stroke.txt", "r", encoding="utf-8") as infile, \
        open("output_stroke.txt", "w", encoding="utf-8") as outfile:
        total_len = 0

        for index, stroke in enumerate(infile.read().split("\n"), 1):
            total_len += len(stroke)
            if index > 8:
                print(f"Количество строк: {index}")
            elif len(stroke) > 180:
                print(f"Длина {index}-й строки {len(stroke)} символов")
                continue
            elif len(stroke) > 0:
                print(f"Длина строки {len(stroke)} символов")
                new_stroke = f"— {stroke}  \n"
                outfile.write(new_stroke)

        print(f"Общая длина текста составляет: {len(stroke)} символов")


