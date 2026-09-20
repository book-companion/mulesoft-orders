%dw 2.0
fun lineTotal(item) = item.price * item.qty
fun orderTotal(items) = sum(items map (item) -> lineTotal(item))
