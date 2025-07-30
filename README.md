# The Wallet

A comprehensive personal finance management system built with Django REST Framework and React.

## 🌟 Features

- User Authentication
  - Registration & Login
  - Token-based authentication using Knox
  - Profile management
- Budget Management
- Transaction Tracking
- Financial Goals
- User Dashboard

## 🛠️ Technology Stack

### Backend
- Python 3.12+
- Django 5.0.11
- Django REST Framework 3.14.0
- Knox Authentication
- PostgreSQL Database

### Frontend
- React
- Node.js
- Modern JavaScript (ES6+)

### Additional Tools & Libraries
- django-cors-headers
- django-rest-knox
- django-environ
- django-jazzmin (Admin Interface)

## 📋 Prerequisites

- Python 3.12 or higher
- Node.js and npm
- PostgreSQL (optional, can use SQLite for development)
- Git

## 🚀 Getting Started

### Backend Setup

1. Clone the repository
   ```bash
   git clone https://github.com/Astro-cmd/The-Wallet.git
   cd The-Wallet
   ```

2. Create and activate virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations
   ```bash
   python manage.py migrate
   ```

5. Create superuser (Optional)
   ```bash
   python manage.py createsuperuser
   ```

6. Run development server
   ```bash
   python manage.py runserver
   ```

### Frontend Setup

1. Navigate to frontend directory
   ```bash
   cd fronted
   ```

2. Install dependencies
   ```bash
   npm install
   ```

3. Start development server
   ```bash
   npm start
   ```

## 📚 API Documentation

### Authentication Endpoints

- POST `/api/users/register/`: Register new user
  ```json
  {
    "username": "example",
    "email": "user@example.com",
    "password": "secure_password"
  }
  ```

- POST `/api/users/login/`: Login user
  ```json
  {
    "username": "example",
    "password": "secure_password"
  }
  ```

- POST `/api/users/logout/`: Logout user (Requires authentication)
- GET `/api/users/user/`: Get user profile (Requires authentication)

## 🌳 Project Structure

```
The-wallet/
├── manage.py
├── requirements.txt
├── The_wallet/              # Project configuration
├── users/                   # User authentication app
├── budgets/                 # Budget management app
├── goals/                   # Financial goals app
├── transactions/           # Transaction tracking app
└── fronted/                # React frontend
    ├── public/
    └── src/
```

## 🔒 Environment Variables

Create a `.env` file in the root directory:

```env
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=your-database-url
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🌿 Branches

- `master`: Main production branch
- `Muichuhia-Backend-Dev`: Backend development branch
- `Muichuhia-Frontend-Dev`: Frontend development branch

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

- **Muichuhia** - [GitHub Profile](https://github.com/Astro-cmd)

## 🙏 Acknowledgments

- Django Rest Framework Documentation
- React Documentation
- Knox Authentication
