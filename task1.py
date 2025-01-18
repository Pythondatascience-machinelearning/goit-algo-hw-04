def total_salary(path):
    total = 0
    count = 0
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                data = line.strip().split(',')
                if len(data)==2 and data[1].strip().isdigit():
                    total += int(data[1].strip())
                    count +=1
        average = total/count if count >0 else 0

        return total, average
    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
        return 0,0
total, average = total_salary("file.txt")
print(f"Загальна сума зарплат: {total}, Середня зарплата:{average}")



