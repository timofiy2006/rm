
clothing_type = input("Який одяг ви хочете купити? (повсякденний або діловий): ")


if clothing_type == "повсякденний":
    item = input("Що ви хочете придбати? (футболку, спорт штани, кросівки): ")
    if item == "футболку":
        available_colors = ["червоний", "синій", "чорний"]
    elif item == "спорт штани":
        available_colors = ["чорний", "сірий", "червоний"]
    elif item == "кросівки":
        available_colors = ["чорний", "коричневий", "білий"]
    else:
        print("Такого товару не існує.")
       
elif clothing_type == "діловий":
    item = input("Що ви хочете придбати? (сорочку, костюм): ")
    if item == "сорочку":
        available_colors = ["білий", "сірий", "чорний"]
    elif item == "костюм":
        available_colors = ["чорний", "сірий", "помаранчевий"]
    else:
        print("Такого товару не існує.")
        
else:
    print("Такого типу одягу не існує.")
   


color = input(f"Якого кольору {item} ви хочете придбати? ({', '.join(available_colors)}): ")


if color in available_colors:
    print(f"Ви замовили {color} {item} {clothing_type} типу.")
else:
    print("Такого кольору не існує.")
