# JaMoveo

JaMoveo is a web application built with Flask (backend) and Vue.js (frontend), using MongoDB as the database. The project is fully containerized with Docker and Docker Compose for easy setup and deployment.

## **Table of Contents**

- [Features](#features)  
- [Tech Stack](#tech-stack)  
- [Getting Started](#getting-started)  
- [Installation with Docker Compose](#installation-with-docker-compose)  
- [Environment Variables](#environment-variables)  
- [Project Structure](#project-structure)  
- [Contributing](#contributing)  
- [License](#license)


## **Features**

- Flask-based RESTful API.  
- Modern Vue.js SPA (Single Page Application).  
- Scalable MongoDB database (cloud-hosted or local).  
- Fully containerized with Docker.  
- Environment configuration with `.env` files.


## **Tech Stack**

- **Backend:** Flask, Python  
- **Frontend:** Vue.js, Vite  
- **Database:** MongoDB  
- **Containerization:** Docker, Docker Compose


## **Getting Started**

### Prerequisites

Make sure you have the following installed:  
- Docker  
- Docker Compose


## **Installation with Docker Compose**

### **Step 1: Clone the Repository**  
Run the following command in your terminal:  
git clone https://github.com/your-username/jamoveo.git  
cd jamoveo  

### **Step 2: Configure Environment Variables**  
Create a `.env` file in the root of the project with the following content:  
FLASK_ENV=production  
SECRET_KEY=your_secret_key  
MONGO_URI=mongodb+srv://<username>:<password>@cluster.mongodb.net/<database>  
VITE_API_URL=http://localhost:5000  

### **Step 3: Build and Run the Containers**  
Run the following command:  
docker-compose up --build  

### **Step 4: Access the Application**  
Frontend: http://localhost  
Backend API: http://localhost:5000


## **Environment Variables**

### Backend Variables
- `FLASK_ENV`: Set to `production` or `development`.  
- `SECRET_KEY`: A random 32 bits secret key for Flask sessions.  
- `MONGO_URI`: The connection string for your MongoDB instance.  


## **Project Structure**

Jamoveo/  
├── app/                   # Flask Backend  
│   ├── controllers/       # API routes  
│   ├── models/            # Database models  
│   ├── services/          # Business logic  
│   ├── utils/             # Utility functions  
│   └── requirements.txt   # Backend dependencies  
├── client/                # Vue.js Frontend  
│   ├── src/               # Application source code  
│   ├── public/            # Static files  
│   ├── nginx/             # NGINX configuration  
│   └── package.json       # Frontend dependencies  
├── docker/                # Docker configurations  
│   ├── Dockerfile.backend  
│   ├── Dockerfile.frontend  
├── docker-compose.yml     # Docker Compose configuration  
├── .env                   # Environment variables  
└── README.md              # Project documentation


## **Contact**

For any questions or feedback, feel free to contact:  
- **Email:** daniel1maymon@gmail.com
- **Linkedin:** https://www.linkedin.com/in/daniel-maymon/

