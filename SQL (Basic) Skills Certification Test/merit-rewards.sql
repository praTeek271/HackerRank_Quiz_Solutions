SELECT pt.stock_code
FROM price_today pt
JOIN price_tomorrow ptom ON pt.stock_code = ptom.stock_code
WHERE ptom.price > pt.price
ORDER BY pt.stock_code;
