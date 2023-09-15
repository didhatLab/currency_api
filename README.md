# Currency converter service

## Endpoints
#### GET /api/rates
```bash
curl -X "GET" "http://localhost:8000/api/rates?from=EUR&to=RUB&value=5000"
```
```json
{"value": 400000}
```

## Dependencies
### External API
- [OpenExchangerRates](https://openexchangerates.org/) — API for currency rates

### Python libs
- [FastAPI](https://fastapi.tiangolo.com/) - Web framework
- [AioHttp](https://docs.aiohttp.org/en/stable/) - Library for async requests
- [Attrs](https://www.attrs.org/en/stable/) - Like python dataclasses, works better with cattrs
- [Cattrs](https://catt.rs/en/stable/) - library for structuring and unstructuring data

### Setup
Clone repository
```bash
git clone git@github.com:didhatLab/currency_api.git
cd currency_api
```
After build and run docker container
```bash
docker build -t currency_api .
docker run -e open_exchange_app_id='your_open_exchange_app_id' -p 8000:8000  test
```

### Possible improvements

- Add request caching in `Redis` from open exchanger
- Add e2e tests
