# Leaderboard API

## Overview

The **Leaderboard API** is designed to manage and display a ranking system based on user scores. It provides endpoints to add, retrieve, and sort scores efficiently. This API is useful for applications requiring a competitive ranking system, such as gaming platforms, coding challenges, and online contests.

## Features

✅ **Add Users & Scores** – Store user information along with their scores.  
✅ **Retrieve Leaderboard** – Get a sorted list of users based on scores.  
✅ **Efficient Sorting** – Optimized queries for ranking calculations.  
✅ **RESTful API** – Simple and structured endpoints for easy integration.  

## Technologies Used

- **Programming Language**: Python
- **Framework**: Flask
- **Database**: SQLite/PostgreSQL (Configurable)
- **Libraries**: Flask, SQLAlchemy, Marshmallow

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/leaderboard-api.git
cd leaderboard-api
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up the Database
```bash
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```

### 5. Run the API
```bash
flask run
```

The API will be available at `http://127.0.0.1:5000/`.

## API Endpoints

### 1. Add a New Score
- **Endpoint:** `POST /add-score`
- **Request Body:**
  ```json
  {
    "username": "player1",
    "score": 1500
  }
  ```
- **Response:**
  ```json
  {
    "message": "Score added successfully!"
  }
  ```

### 2. Get Leaderboard
- **Endpoint:** `GET /leaderboard`
- **Response:**
  ```json
  [
    { "username": "player1", "score": 1500 },
    { "username": "player2", "score": 1200 }
  ]
  ```

## Future Enhancements

🚀 **User Authentication** – Secure access with JWT tokens.  
📊 **Pagination & Filtering** – Optimize data retrieval for large leaderboards.  
⚡ **WebSocket Integration** – Real-time leaderboard updates.  

## License

This project is open-source and available for modification as needed.

## Author

👤 **Naman**   
🔗 GitHub: [Namaannn001](https://github.com/Namaannn001/)

