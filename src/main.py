import utils


def main():
    import_data = utils.load_products("products.json")
    categories_list = utils.category_init(import_data)

    while True:
        for item in categories_list:
            print(item)

        print()

        for item in categories_list:
            print(item.product)

        print()

        change_price_name = input("Введите наименование продукта для изменения цены. Если цену менять не нужно, "
                                  "оставьте поле пустым. ")

        if change_price_name == "":
            break

        is_find = False

        for item in categories_list:
            for prod_item in item.prod:
                if prod_item.name == change_price_name:
                    is_find = True
                    new_price = float(input("Введите новую цену товара: "))
                    prod_item.price = new_price

        if not is_find:
            print("Указанный товар не найден")

        print()

    print()

    for item in categories_list:
        prod_sum = 0

        if len(item.prod) - 1 != 0:
            for index in range(len(item.prod) - 1):
                prod_sum += item.prod[index] + item.prod[index + 1]
        else:
            prod_sum = item.prod[0].price

        print(f"Категория: {item.name}, товаров на сумму: {prod_sum}")


if __name__ == "__main__":
    main()
