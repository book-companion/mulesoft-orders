%dw 2.0
import orderTotal from modules::Pricing
output application/json
---
{orderId: payload.orderId, total: orderTotal(payload.items)}
