from src import utils


def main():
    import_data = utils.load_products("products.json")
    categories_list = utils.category_init(import_data)

    print(categories_list)


if __name__ == "__main__":
    main()
