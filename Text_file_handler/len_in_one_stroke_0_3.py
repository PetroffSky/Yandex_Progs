

def script_120(index, stroke):
    if len(stroke) > 120:
        print(f"Длина {index}-й строки {len(stroke)} символов")
        return False
    else:
        return True
                

def script_180(index, stroke):
    if len(stroke) > 180:
        print(f"Длина {index}-й строки {len(stroke)} символов")
        return False
    else:
        return True


def file_readwrite(mode):
    with open("input_stroke.txt", "r", encoding="utf-8") as infile, \
         open("output_stroke.txt", "w", encoding="utf-8") as outfile:

        total_len = 0
        for index, stroke in enumerate(infile.read().split("\n"), 1):
            stroke = stroke.strip(" ")
            total_len += len(stroke)
            if len(stroke) == 0:
                    continue
            if mode == 1:
                result_1 = script_120(index, stroke)
                if result_1 == False:
                    break
            elif mode == 2:
                result_2 = script_180(index, stroke)
                if result_2 == False:
                    break
            elif len(stroke) > 0:
                print(f"Длина строки {len(stroke)} символов")

            if stroke[-1] != '.':
                stroke = stroke + '.'

            new_stroke = f"— {stroke}  \n"
            outfile.write(new_stroke)

    print(f"Общее количество строк: {index}")
    print(f"Общая длина текста составляет {total_len} символов")