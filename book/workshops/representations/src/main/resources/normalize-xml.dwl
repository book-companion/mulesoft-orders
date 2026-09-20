%dw 2.0
output application/json
---
{orderId: payload.order.@id,
 items: payload.order.*item map (item) -> {
   sku: item.@sku, price: item.price as Number, qty: item.qty as Number
 }}
