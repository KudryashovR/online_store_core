import utils


def main():
    import_data = utils.load_products("products.json")
    categories_list = utils.category_init(import_data)

    for item in categories_list:
        print(item.product)


if __name__ == "__main__":
    main()
