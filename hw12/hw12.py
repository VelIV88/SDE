import matplotlib.pyplot as plt


def read_sales_data(file_path: str) -> list[dict]:
    """
    Функия принимает путь до файла с данными
    и возвращает сптсок словарей продаж.
    Написана в функциональном стиле.
    """
    with open(file_path, "r", encoding="utf-8") as input_file:
        raw_data = input_file.readlines()
        cleaned_data = filter(lambda row: len(row) > 0, raw_data)
        splitted_data = map(lambda row: row.strip().split(", "), cleaned_data)
        structured_data = map(
            lambda row: {
                "product_name": row[0], 
                "quantity": int(row[1]), 
                "price": float(row[2]), 
                "date": row[3]
                },
            splitted_data
            )
        
    return list(structured_data)
    

def get_total_sales_per_product(sales_data: list[dict]) -> dict:
    """
    Функция принимает на вход спиок словарей с продажами
    и возвращает словарь суммарных продаж каждого продукта,
    отсортированный по убыванию суммы продаж.
    """
    sum_sales = {}
    for sale in sales_data:
        product_name = sale["product_name"]
        amount = sale["quantity"] * sale["price"]
        if product_name in sum_sales:
            sum_sales[product_name] += amount
        else:
            sum_sales[product_name] = amount
    
    return dict(sorted(sum_sales.items(), key=lambda elem: elem[1], reverse=True))


def get_sales_over_time(sales_data: list[dict]) -> dict:
    """
    Функция принимает на вход спиок словарей с продажами
    и возвращает словарь суммарных продаж за каждую дату,
    отсортированный возрастанию дат.
    """
    sum_sales = {}
    for sale in sales_data:
        date = sale["date"]
        amount = sale["quantity"] * sale["price"]
        if date in sum_sales:
            sum_sales[date] += amount
        else:
            sum_sales[date] = amount
    
    return dict(sorted(sum_sales.items()))


if __name__ == "__main__":
    sales = read_sales_data("sales.txt")
    sales_per_product = get_total_sales_per_product(sales)
    sales_over_time = get_sales_over_time(sales)

    # Блок расчёта максимальной выручки
    product_with_max_total_sales = max(sales_per_product, key=lambda key: sales_per_product[key])
    date_with_max_total_sales = max(sales_over_time, key=lambda key: sales_over_time[key])
    
    print(f"Продукт, принёсший максимальную выручку: {product_with_max_total_sales}")
    print(f"Дата с наибольшой суммой продаж: {date_with_max_total_sales}")

    # Блок построения графиков продаж
    fig, axs = plt.subplots(2)

    axs[0].plot(sales_over_time.keys(), sales_over_time.values())
    axs[0].set_title("График суммы продаж по дням")
    for label in axs[0].get_xticklabels():
        label.set_rotation(25)
        label.set_ha('right')
        label.set_fontsize(8)
    axs[0].grid()

    axs[1].bar(sales_per_product.keys(), sales_per_product.values())
    axs[1].set_title("Суммарные продажи каждого продукта")
    for label in axs[1].get_xticklabels():
        label.set_rotation(25)
        label.set_ha('right')
        label.set_fontsize(8)

    fig.tight_layout()
    fig.savefig("result.png")