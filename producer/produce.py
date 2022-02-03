from app.models.model import Purchase
from datetime import datetime, timedelta
from fastapi.encoders import jsonable_encoder

import requests


def main() -> None:

    while True:
        p = Purchase(
            purchase_id="UUID1",
            stock_code=5,
            item_description="123",
            quantity=10,
            customer_id=1,
            cost=1,
            purchase_date=datetime.now(),
        )
        requests.post("http://127.0.0.1:8000/produce/sales", json=jsonable_encoder(p))
        return


if __name__ == "__main__":
    main()
