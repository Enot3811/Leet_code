-- https://sql-academy.org/ru/trainer/tasks/93
-- Какой средний возраст клиентов, купивших Smartwatch
-- (использовать наименование товара product.name) в 2024 году?


-- Запрос, чтобы получить средний возраст, но с дублями одного и того же покупателя
-- SELECT AVG(Customer.age) AS average_age
-- FROM Customer
-- JOIN Purchase ON Purchase.customer_key = Customer.customer_key
-- JOIN Product ON Product.product_key = Purchase.product_key
-- WHERE Product.name = 'Smartwatch'
-- AND YEAR(Purchase.date) = 2024

-- С учётом и отсеиванием дубликатов
SELECT AVG(unique_customers.age) AS average_age
FROM (
    SELECT DISTINCT Customer.customer_key, Customer.age
    FROM Customer
    JOIN Purchase ON Purchase.customer_key = Customer.customer_key
    JOIN Product ON Product.product_key = Purchase.product_key
    WHERE Product.name = 'Smartwatch'
    AND YEAR(Purchase.date) = 2024
) AS unique_customers
