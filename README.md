# Blog Interactions

This project provides an API with endpoints for submitting likes and comments on specific pages and querying the interaction counts.

## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Endpoints](#endpoints)

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/marcelo3macedo/blog_interactions
   cd blog_interactions
   ```

2. **Docker Setup**

   Ensure you have Docker and Docker Compose installed. To build and run the application, use:

   ```bash
   docker-compose up --build
   ```

   This will build the Docker image and start the Flask server on `http://localhost:5000`.

3. **Environment Variables**

   Create a `.env` file in the root directory with the following variables:

   ```plaintext
   MYSQL_USER=<your_mysql_user>
   MYSQL_PASSWORD=<your_mysql_password>
   MYSQL_HOST=<your_mysql_host>
   MYSQL_DB=<your_mysql_database>
   ```

   These variables will be used to configure the SQLAlchemy connection for MySQL.

## Usage

To start the application with Docker, ensure Docker is running, then use:

```bash
docker-compose up --build
```

The API will be available at `http://localhost:5000`.

## Endpoints

### 1. Submit a Like

**POST** `{{base_url}}/endpoint/like`

Submit a like for a specific page.

**Request Body:**

```json
{
    "email": "a@gmail.com",
    "name": "a",
    "origin": "a.com.br",
    "page_slug": "a"
}
```

| Field      | Type   | Description                  |
|------------|--------|------------------------------|
| `email`    | string | User's email address         |
| `name`     | string | User's name                  |
| `origin`   | string | Origin of the page           |
| `page_slug`| string | Identifier for the page      |

### 2. Submit a Comment

**POST** `{{base_url}}/endpoint/comment`

Submit a comment for a specific page.

**Request Body:**

```json
{
    "email": "a@gmail.com",
    "name": "a",
    "origin": "a.com.br",
    "page_slug": "teste",
    "content": "teste"
}
```

| Field      | Type   | Description                  |
|------------|--------|------------------------------|
| `email`    | string | User's email address         |
| `name`     | string | User's name                  |
| `origin`   | string | Origin of the page           |
| `page_slug`| string | Identifier for the page      |
| `content`  | string | Content of the comment       |

### 3. Get Interaction Counts

**GET** `{{base_url}}/endpoint/interactions`

Retrieve the total number of likes and comments for a specific page.

**Query Parameters:**

- `origin`: The origin of the page (e.g., `professoraantenada.com.br`)
- `page_slug`: Identifier for the page (e.g., `teste`)

**Example:**

```plaintext
GET {{base_url}}/endpoint/interactions?origin=professoraantenada.com.br&page_slug=teste
```

**Response:**

```json
{
    "like_count": 5,
    "comment_count": 3
}
```

## Notes

To stop the Docker container, run:

```bash
docker-compose down
```
