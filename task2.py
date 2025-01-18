def get_cats_info(path):
    cats_info = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:

                data = line.strip().split(",") 
                if len(data) == 3:
                    unique_id = data[0].strip()
                    identifier = data[1].strip()
                    age = data[2].strip()
                    if age.isdigit():
                        cats_info.append({
                            "cat_id": unique_id,
                            "cat_name": identifier,
                            "age": int(age)
                        })
        return cats_info  

    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        return []
cats_info = get_cats_info("cats.txt")

for cat in cats_info:
    print(cat)

