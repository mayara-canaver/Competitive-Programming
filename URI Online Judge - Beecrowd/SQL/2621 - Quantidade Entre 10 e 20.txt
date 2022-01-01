SELECT products.name FROM products INNER JOIN providers ON products.id_providers = providers.id
WHERE providers.name LIKE 'P%' AND products.amount >= 10 AND products.amount <= 20