foodstuff = ["Banana", "Mango", "Fish", "Carrot", "cabbage"]
flag=found = False
for food in foodstuff:
    if food == "Mango":
        flag_found = True
        break
if flag_found:
    print("マンゴーが入っています")
else:
    print("ありません")

