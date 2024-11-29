## Quick Start:

You can quickly start up the API server by following these steps:

1. Create a `.env` file in the root directory of the project (you can just rename the `.env.example` file)

2. Run the docker-compose file:

```bash
sudo docker-compose up
```

It spawns up a postgres database, a redis cache, and the API server.

### Notes:

. Note that the values in the `.env.example` file are based on the docker-compose file, so you don't need to change them if you're using the docker-compose file.

. The data directory of the postgres container is mapped to a volume in the docker-compose file, so any changes made to the database will persist even after the container is stopped. If you want to reset the database, you can delete the volume and recreate the container using the `docker-compose down` and `docker-compose up` commands.

## Usage:

For demo purposes, a user is created with `id = 1` and initial balance of **100$**. You can use this user to test the API.

For now, only **ABAN** currency is defined, but you can define more currencies by adding them to the `exchange/domain/currency/currencies.py` file.

To purchace a currency, you can use the following API endpoint:

**Method**: `POST`  
**URL**: `localhost:8000/api/buy/`  
**Description**: Buys the specified amount of a currency for the user.

#### Request Body

| Field      | Type   | Required | Description              |
| ---------- | ------ | -------- | ------------------------ |
| `user_id`  | Number | Yes      | The user's ID            |
| `currency` | String | Yes      | The name of the currency |
| `amount`   | Number | Yes      | The amount to buy        |

#### Example Request

```http
POST /api/buy HTTP/1.1
Content-Type: application/json

{
    "user_id": 1
    "currency": "ABAN",
    "amount": 5
}
```

#### Response Body

| Field                | Type   | Description                                             |
| -------------------- | ------ | ------------------------------------------------------- |
| `dollar_balance`     | Number | The current balance of dollors in the user's account    |
| `[currency]_balance` | Number | The current balance of `currency` in the user's account |

### Example Response

```json
{
    "dollar_balance": 36.0,
    "ABAN_balance": 16.0
}
```

## Running locally:

To run the API server locally, you can use the following steps:

1. Make sure you have a postgres database and a redis cache running. If you don't have them running, you can use docker-compose to start them up:

```bash
sudo docker-compose up -d postgres redis
```

2. Create a virtual environment:

```bash
python3 -m venv venv
```

3. Activate the virtual environment:

```bash
source venv/bin/activate
```

4. Install the required packages:

```bash
pip install -r requirements.txt
```

5. Run the migrations:

```bash
./manage.py migrate
```

6. Run the server:

```bash
./manage.py runserver
```

## Running Tests:

To run the tests, you can use the following command:

```bash
./manage.py test
```
