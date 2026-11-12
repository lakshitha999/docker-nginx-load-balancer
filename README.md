# Docker-Based Web Application Deployment Using NGINX Load Balancer

## Project Overview
This project demonstrates the deployment of a web application using Docker containers and an NGINX load balancer. It distributes incoming requests across three Flask backend containers using the round-robin load-balancing algorithm.

## Architecture
- React – Frontend
- Flask – Backend API
- PostgreSQL – Database
- Docker – Containerization
- Docker Compose – Container orchestration
- NGINX – Reverse proxy and load balancer

## Key Features
- Three Flask backend instances.
- NGINX-based round-robin load balancing.
- User registration and login.
- Password hashing.
- PostgreSQL persistent storage.
- Containerized frontend and backend.
- Backend health-check API.

## Project Structure
```text
docker-load-balancer-project/
├── app/
├── frontend/
├── nginx/
└── docker-compose.yml
```

## How to Run

1. Install Docker Desktop.
2. Clone the repository:
   `git clone https://github.com/lakshitha999/docker-nginx-load-balancer.git`
3. Open the project directory:
   `cd docker-nginx-load-balancer`
4. Start the application:
   `docker compose up --build -d`
5. Open:
   `http://localhost:8080`

## Testing
- Access the application through the NGINX load balancer.
- Test backend health using `/api/health`.
- Send repeated requests to observe distribution across backend containers.

## Learning Outcomes
- Docker containerization.
- Docker Compose.
- NGINX reverse proxy and load balancing.
- Frontend and backend integration.
- Database connectivity.
- Basic rolling-update concepts.
