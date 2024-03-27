import src.utils as utils


def main():
    import_data = utils.load_products("products.json")
    categories_list = utils.category_init(import_data)

    while True:
        utils.print_statistics(categories_list)

        match utils.print_operations():
            case '1':
                change_price_name = input("\033[34m{}\033[0m".format("Введите наименование продукта для изменения "
                                                                     "цены. Если цену менять не нужно, оставьте поле "
                                                                     "пустым: "))

                if not change_price_name:
                    break
                else:
                    utils.change_price(categories_list, change_price_name)
            case '2':
                buying_product_name = input("\033[34m{}\033[0m".format("Введите наименование продукта для покупки. "
                                                                       "Для отмены оставьте поле пустым: "))

                if not buying_product_name:
                    break
                else:
                    utils.get_order(categories_list, buying_product_name)
            case _:
                break


if __name__ == "__main__":
    main()
