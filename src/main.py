import utils


def main():
    import_data = utils.load_products("products.json")
    categories_list = utils.category_init(import_data)

    while True:
        utils.print_statistics(categories_list)

        change_price_name = input("Введите наименование продукта для изменения цены. Если цену менять не нужно, "
                                  "оставьте поле пустым. ")

        if change_price_name == "":
            break
        else:
            utils.change_price(categories_list, change_price_name)


if __name__ == "__main__":
    main()
