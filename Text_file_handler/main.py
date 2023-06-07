import len_in_one_stroke_0_3






if __name__ == "__main__":

    with open(".settings", "r", encoding="utf-8") as settings:

        for stroke in settings.read().split("\n"):
            if stroke[stroke.find(" ") + 1:] == "1":  # 1-й режим запускает скрипт на 120 символов
                len_in_one_stroke_0_3.file_readwrite(1)
            elif stroke[stroke.find(" ") + 1:] == "2":  # 1-й режим запускает скрипт на 180 символов
                len_in_one_stroke_0_3.file_readwrite(2)

    print()
    with open("output_stroke.txt", "r", encoding="utf-8") as file:
        print(file.read())