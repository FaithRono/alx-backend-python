# 🐳 Docker Documentation Hub

[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com/)
[![Documentation](https://img.shields.io/badge/Documentation-1f425f.svg?style=for-the-badge)](https://github.com/yourusername/docker-docs)
[![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg?style=for-the-badge)](CONTRIBUTING.md)

> **A comprehensive, enterprise-ready documentation project for Docker containerization platform**

Welcome to the most complete Docker documentation resource! This repository provides in-depth guides, best practices, real-world examples, and enterprise patterns to help you master Docker from beginner to expert level.

---

## 📚 Table of Contents

- [🌟 Features](#-features)
- [🚀 Quick Start](#-quick-start)
- [📖 Documentation Structure](#-documentation-structure)
- [💻 Installation Methods](#-installation-methods)
- [🔧 Docker Fundamentals](#-docker-fundamentals)
- [📋 Prerequisites](#-prerequisites)
- [🛠️ Advanced Topics](#️-advanced-topics)
- [📱 API Reference](#-api-reference)
- [🏗️ Real-World Examples](#️-real-world-examples)
- [🔒 Security Best Practices](#-security-best-practices)
- [📊 Monitoring & Observability](#-monitoring--observability)
- [🤝 Contributing](#-contributing)
- [🆘 Support & Troubleshooting](#-support--troubleshooting)
- [📜 License](#-license)
- [🙏 Acknowledgments](#-acknowledgments)

---

## 🌟 Features

### 📖 Comprehensive Coverage
- **Complete Installation Guides** - Multiple installation methods across all platforms
- **Dockerfile Mastery** - From basic to advanced multi-stage builds
- **Docker Compose** - Orchestrating multi-container applications
- **Container Security** - Enterprise-grade security hardening
- **Performance Optimization** - Production-ready container optimization

### 🎯 Practical Examples
- **Real-world Applications** - Complete application containerization
- **Microservices Architecture** - Container-based microservices patterns
- **CI/CD Integration** - Docker in continuous integration pipelines
- **Cloud Deployment** - AWS, Azure, GCP container deployments
- **Orchestration** - Kubernetes, Docker Swarm, and more

### 🔧 Advanced Features
- **Multi-stage Builds** - Optimized container builds
- **Health Checks** - Container health monitoring
- **Networking** - Advanced container networking
- **Storage** - Persistent data management
- **Registry Management** - Private registry setup and management

---

## 🚀 Quick Start

### For Absolute Beginners
```bash
# Install Docker (Ubuntu/Debian)
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Verify installation
docker --version
docker run hello-world

# Your first container
docker run -it ubuntu:latest bash
```

### For Developers
```bash
# Clone this documentation
git clone https://github.com/yourusername/docker-docs.git
cd docker-docs

# Start with practical examples
1. Read: docs/getting-started/README.md
2. Follow: examples/web-app-containerization/
3. Try: examples/microservices-example/
```

### For DevOps Engineers
```bash
# Jump to advanced topics
1. Architecture: docs/architecture/container-orchestration.md
2. Security: docs/security/enterprise-hardening.md
3. Monitoring: docs/monitoring/container-observability.md
```

---

## 📖 Documentation Structure

```
docker-docs/
├── 📁 docs/
│   ├── 🚀 getting-started/
│   │   ├── overview.md                    # Docker fundamentals
│   │   ├── core-concepts.md              # Images, containers, volumes
│   │   ├── dockerfile-basics.md          # Your first Dockerfile
│   │   └── docker-compose-intro.md       # Multi-container applications
│   │
│   ├── ⚙️ installation/
│   │   ├── linux/
│   │   │   ├── ubuntu-debian.md          # Ubuntu/Debian installation
│   │   │   ├── centos-rhel.md            # CentOS/RHEL installation
│   │   │   ├── arch-linux.md             # Arch Linux installation
│   │   │   └── post-install-setup.md     # Post-installation configuration
│   │   ├── windows/
│   │   │   ├── docker-desktop.md         # Docker Desktop for Windows
│   │   │   ├── wsl2-backend.md           # WSL2 backend configuration
│   │   │   └── hyper-v-setup.md          # Hyper-V configuration
│   │   ├── macos/
│   │   │   ├── docker-desktop-mac.md     # Docker Desktop for Mac
│   │   │   ├── homebrew-install.md       # Homebrew installation
│   │   │   └── m1-arm-setup.md           # Apple Silicon (M1/M2) setup
│   │   └── cloud/
│   │       ├── aws-ec2.md                # AWS EC2 Docker setup
│   │       ├── azure-vm.md               # Azure VM Docker setup
│   │       └── gcp-compute.md            # GCP Compute Engine setup
│   │
│   ├── 🐳 dockerfile/
│   │   ├── syntax-reference.md           # Complete Dockerfile syntax
│   │   ├── best-practices.md             # Dockerfile best practices
│   │   ├── multi-stage-builds.md         # Multi-stage build patterns
│   │   ├── optimization-techniques.md    # Image size optimization
│   │   ├── security-considerations.md    # Security in Dockerfiles
│   │   └── language-specific/
│   │       ├── python-dockerfile.md      # Python application Dockerfiles
│   │       ├── nodejs-dockerfile.md      # Node.js application Dockerfiles
│   │       ├── java-dockerfile.md        # Java application Dockerfiles
│   │       ├── golang-dockerfile.md      # Go application Dockerfiles
│   │       └── dotnet-dockerfile.md      # .NET application Dockerfiles
│   │
│   ├── 🔧 docker-compose/
│   │   ├── compose-file-reference.md     # Complete compose file syntax
│   │   ├── services-configuration.md     # Service configuration patterns
│   │   ├── networking.md                 # Compose networking
│   │   ├── volumes-and-storage.md        # Data persistence
│   │   ├── environment-variables.md      # Environment management
│   │   ├── secrets-management.md         # Secrets in compose
│   │   └── production-patterns/
│   │       ├── web-app-stack.md          # LAMP/MEAN/MERN stacks
│   │       ├── microservices-compose.md  # Microservices with compose
│   │       ├── monitoring-stack.md       # Prometheus/Grafana stack
│   │       └── logging-stack.md          # ELK/EFK stack
│   │
│   ├── 🌐 networking/
│   │   ├── network-types.md              # Bridge, host, overlay networks
│   │   ├── custom-networks.md            # Creating custom networks
│   │   ├── inter-container-communication.md # Container-to-container
│   │   ├── port-mapping.md               # Port publishing strategies
│   │   ├── load-balancing.md             # Load balancing patterns
│   │   └── network-security.md           # Network security best practices
│   │
│   ├── 💾 storage/
│   │   ├── volumes-overview.md           # Docker volumes explained
│   │   ├── bind-mounts.md                # Host directory mounting
│   │   ├── tmpfs-mounts.md               # Temporary filesystems
│   │   ├── volume-drivers.md             # Storage drivers and plugins
│   │   ├── backup-strategies.md          # Data backup patterns
│   │   └── performance-tuning.md         # Storage performance optimization
│   │
│   ├── 🔒 security/
│   │   ├── container-security.md         # Container security fundamentals
│   │   ├── image-security.md             # Secure image building
│   │   ├── runtime-security.md           # Runtime security measures
│   │   ├── secrets-management.md         # Secrets and credentials
│   │   ├── user-namespaces.md            # User namespace isolation
│   │   ├── apparmor-selinux.md           # AppArmor and SELinux
│   │   └── vulnerability-scanning.md     # Security scanning tools
│   │
│   ├── 📊 monitoring/
│   │   ├── container-metrics.md          # Container metrics collection
│   │   ├── logging-strategies.md         # Centralized logging
│   │   ├── health-checks.md              # Container health monitoring
│   │   ├── prometheus-integration.md     # Prometheus monitoring
│   │   ├── grafana-dashboards.md         # Grafana visualization
│   │   └── alerting-setup.md             # Alert configuration
│   │
│   ├── 🏗️ orchestration/
│   │   ├── docker-swarm/
│   │   │   ├── swarm-mode-overview.md    # Docker Swarm introduction
│   │   │   ├── cluster-setup.md          # Swarm cluster setup
│   │   │   ├── service-deployment.md     # Service deployment patterns
│   │   │   └── swarm-networking.md       # Swarm networking
│   │   ├── kubernetes/
│   │   │   ├── docker-kubernetes.md      # Docker in Kubernetes
│   │   │   ├── pod-specifications.md     # Pod and container specs
│   │   │   ├── deployment-strategies.md  # Deployment patterns
│   │   │   └── service-mesh.md           # Service mesh integration
│   │   └── nomad/
│   │       ├── nomad-docker.md           # HashiCorp Nomad integration
│   │       └── job-specifications.md     # Nomad job specs
│   │
│   ├── ☁️ cloud-integration/
│   │   ├── aws/
│   │   │   ├── ecs-fargate.md            # AWS ECS and Fargate
│   │   │   ├── ecr-registry.md           # Amazon ECR
│   │   │   ├── lambda-containers.md      # AWS Lambda containers
│   │   │   └── batch-processing.md       # AWS Batch
│   │   ├── azure/
│   │   │   ├── container-instances.md    # Azure Container Instances
│   │   │   ├── kubernetes-service.md     # Azure Kubernetes Service
│   │   │   ├── container-registry.md     # Azure Container Registry
│   │   │   └── app-service.md            # Azure App Service containers
│   │   ├── gcp/
│   │   │   ├── cloud-run.md              # Google Cloud Run
│   │   │   ├── gke-deployment.md         # Google Kubernetes Engine
│   │   │   ├── container-registry.md     # Google Container Registry
│   │   │   └── compute-engine.md         # GCE container deployments
│   │   └── multi-cloud/
│   │       ├── cloud-agnostic-patterns.md # Cloud-agnostic designs
│   │       └── hybrid-deployments.md     # Hybrid cloud strategies
│   │
│   ├── 🔄 ci-cd-integration/
│   │   ├── jenkins-docker.md             # Jenkins and Docker
│   │   ├── github-actions.md             # GitHub Actions integration
│   │   ├── gitlab-ci.md                  # GitLab CI/CD integration
│   │   ├── azure-devops.md               # Azure DevOps integration
│   │   ├── circleci.md                   # CircleCI integration
│   │   └── tekton-pipelines.md           # Tekton CI/CD
│   │
│   ├── 🛡️ registry/
│   │   ├── docker-hub.md                 # Docker Hub usage
│   │   ├── private-registry.md           # Setting up private registry
│   │   ├── harbor-setup.md               # Harbor enterprise registry
│   │   ├── security-scanning.md          # Registry security scanning
│   │   └── image-management.md           # Image lifecycle management
│   │
│   └── 🆘 troubleshooting/
│       ├── common-issues.md              # Common problems & solutions
│       ├── performance-debugging.md      # Performance troubleshooting
│       ├── networking-issues.md          # Network troubleshooting
│       ├── storage-problems.md           # Storage issue resolution
│       └── log-analysis.md               # Container log analysis
│
├── 📁 examples/
│   ├── web-applications/
│   │   ├── django-app/                   # Django application containerization
│   │   ├── nodejs-express/               # Node.js Express application
│   │   ├── react-frontend/               # React frontend application
│   │   ├── spring-boot/                  # Spring Boot application
│   │   └── nginx-reverse-proxy/          # Nginx reverse proxy setup
│   │
│   ├── databases/
│   │   ├── postgresql/                   # PostgreSQL containerization
│   │   ├── mysql/                        # MySQL containerization
│   │   ├── mongodb/                      # MongoDB containerization
│   │   ├── redis/                        # Redis containerization
│   │   └── elasticsearch/                # Elasticsearch containerization
│   │
│   ├── microservices/
│   │   ├── complete-microservices/       # Full microservices example
│   │   ├── api-gateway/                  # API Gateway pattern
│   │   ├── service-discovery/            # Service discovery patterns
│   │   └── event-driven-architecture/    # Event-driven microservices
│   │
│   ├── monitoring-stacks/
│   │   ├── prometheus-grafana/           # Monitoring stack
│   │   ├── elk-stack/                    # Elasticsearch, Logstash, Kibana
│   │   ├── jaeger-tracing/               # Distributed tracing
│   │   └── metrics-collection/           # Metrics collection patterns
│   │
│   ├── development-environments/
│   │   ├── full-stack-dev/               # Full-stack development setup
│   │   ├── database-dev-env/             # Database development environment
│   │   ├── testing-environment/          # Automated testing environment
│   │   └── code-quality-tools/           # Code quality and linting tools
│   │
│   └── production-patterns/
│       ├── blue-green-deployment/        # Blue-green deployment
│       ├── canary-deployment/            # Canary deployment patterns
│       ├── rolling-updates/              # Rolling update strategies
│       └── disaster-recovery/            # Disaster recovery patterns
│
├── 📁 scripts/
│   ├── installation/                     # Installation automation scripts
│   ├── container-management/             # Container lifecycle scripts
│   ├── image-optimization/               # Image optimization tools
│   ├── security-scanning/                # Security scanning automation
│   ├── monitoring/                       # Monitoring setup scripts
│   └── backup-restore/                   # Backup and restore scripts
│
├── 📁 templates/
│   ├── dockerfile-templates/             # Production-ready Dockerfile templates
│   ├── compose-templates/                # Docker Compose templates
│   ├── kubernetes-manifests/             # Kubernetes deployment templates
│   ├── ci-cd-pipelines/                  # CI/CD pipeline templates
│   └── monitoring-configs/               # Monitoring configuration templates
│
└── 📁 assets/
    ├── diagrams/                         # Architecture diagrams
    ├── images/                           # Documentation images
    ├── videos/                           # Tutorial videos
    └── cheat-sheets/                     # Quick reference guides
```

---

## 💻 Installation Methods

### 🐧 Linux Distributions

#### Ubuntu/Debian (Recommended)
```bash
# Remove old versions
sudo apt-get remove docker docker-engine docker.io containerd runc

# Update package index
sudo apt-get update

# Install required packages
sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

# Add Docker's official GPG key
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

# Set up repository
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install Docker Engine
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin

# Verify installation
sudo docker run hello-world
```

#### CentOS/RHEL/Fedora
```bash
# Remove old versions
sudo yum remove docker \
    docker-client \
    docker-client-latest \
    docker-common \
    docker-latest \
    docker-latest-logrotate \
    docker-logrotate \
    docker-engine

# Install yum-utils
sudo yum install -y yum-utils

# Set up repository
sudo yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo

# Install Docker Engine
sudo yum install docker-ce docker-ce-cli containerd.io docker-compose-plugin

# Start Docker
sudo systemctl start docker
sudo systemctl enable docker

# Verify installation
sudo docker run hello-world
```

#### Arch Linux
```bash
# Install Docker
sudo pacman -S docker docker-compose

# Start and enable Docker service
sudo systemctl start docker.service
sudo systemctl enable docker.service

# Add user to docker group
sudo usermod -aG docker $USER

# Verify installation
docker run hello-world
```

### 🪟 Windows

#### Docker Desktop for Windows
1. **Download**: [Docker Desktop for Windows](https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe)
2. **System Requirements**:
   - Windows 10/11 64-bit
   - WSL 2 feature enabled
   - BIOS-level hardware virtualization support

```powershell
# Enable WSL 2 (Run as Administrator)
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart

# Restart computer and install Docker Desktop
# Verify installation
docker --version
docker run hello-world
```

#### Windows Server
```powershell
# Install Docker on Windows Server 2019/2022
Install-Module -Name DockerMsftProvider -Repository PSGallery -Force
Install-Package -Name docker -ProviderName DockerMsftProvider

# Start Docker service
Start-Service Docker

# Verify installation
docker run hello-world
```

### 🍎 macOS

#### Docker Desktop for Mac
1. **Download**: [Docker Desktop for Mac](https://desktop.docker.com/mac/main/amd64/Docker.dmg)
2. **System Requirements**:
   - macOS 10.15 or newer
   - Apple Silicon (M1/M2) or Intel processor

```bash
# Alternative: Install via Homebrew
brew install --cask docker

# Start Docker Desktop from Applications
# Verify installation
docker --version
docker run hello-world
```

#### Mac with Apple Silicon (M1/M2)
```bash
# Install Docker Desktop for Apple Silicon
# Download ARM64 version from Docker website

# For command line installation
arch -arm64 brew install --cask docker

# Verify architecture
docker version --format 'Server: {{.Server.Arch}}'
```

### 🐳 Docker Installation Script (Universal)
```bash
# Official Docker installation script (Linux)
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Add current user to docker group
sudo usermod -aG docker $USER

# Apply group membership
newgrp docker

# Verify installation
docker --version
docker-compose --version
```

---

## 🔧 Docker Fundamentals

### Core Concepts

#### 1. Images and Containers
```bash
# Understanding Docker Images
docker images                    # List all images
docker image inspect ubuntu     # Inspect image details
docker image history ubuntu     # Show image layers

# Working with Containers
docker ps                       # List running containers
docker ps -a                    # List all containers
docker container inspect myapp  # Inspect container details
```

#### 2. Container Lifecycle
```bash
# Container lifecycle management
docker create --name myapp nginx        # Create container
docker start myapp                      # Start container
docker stop myapp                       # Stop container
docker restart myapp                    # Restart container
docker pause myapp                      # Pause container
docker unpause myapp                    # Unpause container
docker rm myapp                         # Remove container
```

### Your First Dockerfile

#### Basic Dockerfile Structure
```dockerfile
# Use official base image
FROM ubuntu:22.04

# Set metadata
LABEL maintainer="your-email@example.com"
LABEL description="My first Docker application"
LABEL version="1.0.0"

# Set environment variables
ENV APP_HOME=/app
ENV APP_USER=appuser

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Create application user
RUN groupadd -r ${APP_USER} && \
    useradd -r -g ${APP_USER} ${APP_USER}

# Create application directory
RUN mkdir -p ${APP_HOME} && \
    chown -R ${APP_USER}:${APP_USER} ${APP_HOME}

# Set working directory
WORKDIR ${APP_HOME}

# Copy application files
COPY --chown=${APP_USER}:${APP_USER} requirements.txt .
COPY --chown=${APP_USER}:${APP_USER} . .

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Switch to non-root user
USER ${APP_USER}

# Expose port
EXPOSE 8000

# Add health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Define entrypoint
ENTRYPOINT ["python3"]
CMD ["app.py"]
```

#### Advanced Multi-stage Dockerfile
```dockerfile
# Multi-stage build for Python application
FROM python:3.11-slim as base

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Development stage
FROM base as development
RUN pip install pytest pytest-cov black flake8
COPY requirements-dev.txt .
RUN pip install -r requirements-dev.txt
WORKDIR /app
CMD ["python", "-m", "pytest"]

# Dependencies stage
FROM base as dependencies
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Production stage
FROM python:3.11-slim as production

# Copy installed packages from dependencies stage
COPY --from=dependencies /root/.local /root/.local

# Create non-root user
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Set working directory
WORKDIR /app

# Copy application code
COPY --chown=appuser:appuser . .

# Switch to non-root user
USER appuser

# Add local packages to PATH
ENV PATH=/root/.local/bin:$PATH

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python health_check.py || exit 1

# Expose port
EXPOSE 8000

# Run application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "app:app"]
```

### Docker Compose Essentials

#### Basic Docker Compose File
```yaml
version: '3.8'

services:
  web:
    build: 
      context: .
      dockerfile: Dockerfile
      target: production
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://user:password@db:5432/mydb
      - REDIS_URL=redis://redis:6379/0
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_started
    volumes:
      - ./app:/app
      - static_volume:/app/staticfiles
    networks:
      - app-network
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s

  db:
    image: postgres:15
    environment:
      POSTGRES_DB: mydb
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql
    networks:
      - app-network
    restart: unless-stopped
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U user -d mydb"]
      interval: 10s
      timeout: 5s
      retries: 5

  redis:
    image: redis:7-alpine
    command: redis-server --appendonly yes
    volumes:
      - redis_data:/data
    networks:
      - app-network
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 3s
      retries: 3

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
      - static_volume:/var/www/html/static:ro
      - ssl_certs:/etc/nginx/ssl:ro
    depends_on:
      - web
    networks:
      - app-network
    restart: unless-stopped

volumes:
  postgres_data:
    driver: local
  redis_data:
    driver: local
  static_volume:
    driver: local
  ssl_certs:
    driver: local

networks:
  app-network:
    driver: bridge
    ipam:
      config:
        - subnet: 172.20.0.0/16
```

#### Production Docker Compose
```yaml
version: '3.8'

x-common-variables: &common-variables
  ENVIRONMENT: production
  LOG_LEVEL: info

x-restart-policy: &restart-policy
  restart: unless-stopped

services:
  web:
    <<: *restart-policy
    build:
      context: .
      dockerfile: Dockerfile.prod
      args:
        BUILD_DATE: ${BUILD_DATE}
        VCS_REF: ${VCS_REF}
    ports:
      - "8000:8000"
    environment:
      <<: *common-variables
      DATABASE_URL: postgresql://${DB_USER}:${DB_PASSWORD}@db:5432/${DB_NAME}
      REDIS_URL: redis://redis:6379/0
      SECRET_KEY: ${SECRET_KEY}
    env_file:
      - .env.production
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_healthy
    volumes:
      - static_volume:/app/staticfiles:ro
      - media_volume:/app/media
      - logs_volume:/app/logs
    networks:
      - app-network
      - monitoring-network
    deploy:
      replicas: 3
      resources:
        limits:
          cpus: '0.5'
          memory: 512M
        reservations:
          cpus: '0.25'
          memory: 256M
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health/"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"

  db:
    <<: *restart-policy
    image: postgres:15
    environment:
      POSTGRES_DB: ${DB_NAME}
      POSTGRES_USER: ${DB_USER}
      POSTGRES_PASSWORD: ${DB_PASSWORD}
      POSTGRES_INITDB_ARGS: "--encoding=UTF8 --lc-collate=C --lc-ctype=C"
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./postgresql.conf:/etc/postgresql/postgresql.conf:ro
      - ./pg_hba.conf:/etc/postgresql/pg_hba.conf:ro
      - postgres_logs:/var/log/postgresql
    networks:
      - app-network
    deploy:
      resources:
        limits:
          cpus: '1.0'
          memory: 1G
        reservations:
          cpus: '0.5'
          memory: 512M
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${DB_USER} -d ${DB_NAME}"]
      interval: 10s
      timeout: 5s
      retries: 5
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"

  redis:
    <<: *restart-policy
    image: redis:7-alpine
    command: >
      redis-server
      --appendonly yes
      --appendfsync everysec
      --maxmemory 256mb
      --maxmemory-policy allkeys-lru
    volumes:
      - redis_data:/data
      - ./redis.conf:/etc/redis/redis.conf:ro
    networks:
      - app-network
    deploy:
      resources:
        limits:
          cpus: '0.25'
          memory: 256M
        reservations:
          cpus: '0.1'
          memory: 128M
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 3s
      retries: 3

  nginx:
    <<: *restart-policy
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf:ro
      - ./nginx/conf.d:/etc/nginx/conf.d:ro
      - static_volume:/var/www/html/static:ro
      - media_volume:/var/www/html/media:ro
      - ssl_certs:/etc/nginx/ssl:ro
      - nginx_logs:/var/log/nginx
    depends_on:
      - web
    networks:
      - app-network
    deploy:
      resources:
        limits:
          cpus: '0.25'
          memory: 128M
        reservations:
          cpus: '0.1'
          memory: 64M
    healthcheck:
      test: ["CMD", "wget", "--quiet", "--tries=1", "--spider", "http://localhost/health"]
      interval: 30s
      timeout: 10s
      retries: 3

volumes:
  postgres_data:
    driver: local
    driver_opts:
      type: none
      o: bind
      device: /opt/docker-data/postgres
  redis_data:
    driver: local
  static_volume:
    driver: local
  media_volume:
    driver: local
  ssl_certs:
    driver: local
  logs_volume:
    driver: local
  postgres_logs:
    driver: local
  nginx_logs:
    driver: local

networks:
  app-network:
    driver: bridge
    ipam:
      config:
        - subnet: 172.20.0.0/16
  monitoring-network:
    external: true
```

---

## 📋 Prerequisites

### System Requirements

#### Minimum Requirements
- **CPU**: 2 cores
- **RAM**: 4 GB
- **Storage**: 20 GB free space
- **OS**: 64-bit operating system
- **Internet**: Stable internet connection

#### Recommended Requirements
- **CPU**: 4+ cores
- **RAM**: 8+ GB
- **Storage**: 100+ GB SSD
- **OS**: Latest 64-bit OS version
- **Network**: High-speed internet connection

### Software Dependencies

#### Required Software
```bash
# Git (for version control)
sudo apt update && sudo apt install git

# curl (for downloads)
sudo apt install curl

# Text editor (choose one)
sudo apt install vim nano code
```

#### Development Tools
```bash
# Build tools
sudo apt install build-essential

# Python development
sudo apt install python3 python3-pip python3-venv

# Node.js development
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt install nodejs

# Java development
sudo apt install openjdk-17-jdk maven
```

### Network Configuration

#### Firewall Settings
```bash
# Ubuntu/Debian
sudo ufw allow 2375/tcp    # Docker daemon (if needed)
sudo ufw allow 2376/tcp    # Docker daemon TLS
sudo ufw allow 80/tcp      # HTTP
sudo ufw allow 443/tcp     # HTTPS

# CentOS/RHEL
sudo firewall-cmd --permanent --add-port=2375/tcp
sudo firewall-cmd --permanent --add-port=2376/tcp
sudo firewall-cmd --permanent --add-port=80/tcp
sudo firewall-cmd --permanent --add-port=443/tcp
sudo firewall-cmd --reload
```

#### Proxy Configuration
```bash
# Configure Docker to use proxy
sudo mkdir -p /etc/systemd/system/docker.service.d

# Create proxy configuration
sudo cat > /etc/systemd/system/docker.service.d/http-proxy.conf << EOF
[Service]
Environment="HTTP_PROXY=http://proxy.example.com:8080"
Environment="HTTPS_PROXY=http://proxy.example.com:8080"
Environment="NO_PROXY=localhost,127.0.0.1,.example.com"
EOF

# Reload and restart Docker
sudo systemctl daemon-reload
sudo systemctl restart docker
```

---

## 🛠️ Advanced Topics

### Container Orchestration

#### Docker Swarm
```bash
# Initialize Docker Swarm
docker swarm init

# Add worker nodes
docker swarm join --token SWMTKN-1-token worker-node-ip:2377

# Deploy a stack
docker stack deploy -c docker-compose.yml myapp

# Scale services
docker service scale myapp_web=5

# Monitor services
docker service ls
docker service ps myapp_web
```

#### Kubernetes Integration
```yaml
# Kubernetes Deployment for Docker containers
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
    spec:
      containers:
      - name: myapp
        image: myapp:latest
        ports:
        - containerPort: 8000
        env:
        - name: DATABASE_URL
          valueFrom:
            secretKeyRef:
              name: myapp-secrets
              key: database-url
        resources:
          requests:
            memory: "256Mi"
            cpu: "250m"
          limits:
            memory: "512Mi"
            cpu: "500m"
        livenessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /ready
            port: 8000
          initialDelaySeconds: 5
          periodSeconds: 5
```

### Performance Optimization

#### Image Size Optimization
```dockerfile
# Use multi-stage builds
FROM node:18 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

FROM node:18-alpine AS production
RUN addgroup -g 1001 -S nodejs
RUN adduser -S nodejs -u 1001
WORKDIR /app
COPY --from=builder --chown=nodejs:nodejs /app/node_modules ./node_modules
COPY --chown=nodejs:nodejs . .
USER nodejs
EXPOSE 3000
CMD ["npm", "start"]
```

#### Build Caching Strategies
```dockerfile
# Optimize layer caching
FROM python:3.11-slim

# Install system dependencies first (changes rarely)
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies before code
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code last (changes frequently)
COPY . .

CMD ["python", "app.py"]
```

#### Resource Management
```yaml
# Docker Compose resource limits
services:
  web:
    image: myapp:latest
    deploy:
      resources:
        limits:
          cpus: '0.50'
          memory: 512M
        reservations:
          cpus: '0.25'
          memory: 256M
      restart_policy:
        condition: on-failure
        delay: 5s
        max_attempts: 3
        window: 120s
```

### Advanced Networking

#### Custom Bridge Networks
```bash
# Create custom bridge network
docker network create \
  --driver bridge \
  --subnet=172.20.0.0/16 \
  --ip-range=172.20.240.0/20 \
  --gateway=172.20.0.1 \
  my-bridge-network

# Connect containers to custom network
docker run -d --name web --network my-bridge-network nginx
docker run -d --name db --network my-bridge-network postgres
```

#### Overlay Networks (Swarm)
```bash
# Create overlay network
docker network create \
  --driver overlay \
  --subnet=10.0.0.0/16 \
  --attachable \
  my-overlay-network

# Use in stack deployment
services:
  web:
    image: nginx
    networks:
      - my-overlay-network
    deploy:
      replicas: 3

networks:
  my-overlay-network:
    external: true
```

#### Network Security
```bash
# Create isolated network
docker network create \
  --driver bridge \
  --internal \
  isolated-network

# Network with custom DNS
docker network create \
  --driver bridge \
  --dns=8.8.8.8 \
  --dns=8.8.4.4 \
  custom-dns-network
```

### Storage Solutions

#### Named Volumes
```bash
# Create named volume
docker volume create \
  --driver local \
  --opt type=nfs \
  --opt o=addr=192.168.1.100,rw \
  --opt device=:/path/to/nfs/share \
  nfs-volume

# Use in containers
docker run -d \
  --name myapp \
  -v nfs-volume:/app/data \
  myapp:latest
```

#### Bind Mounts with Options
```bash
# Bind mount with specific options
docker run -d \
  --name myapp \
  --mount type=bind,source=/host/path,target=/container/path,readonly \
  myapp:latest

# Bind mount with SELinux labels
docker run -d \
  --name myapp \
  -v /host/path:/container/path:Z \
  myapp:latest
```

#### Volume Plugins
```yaml
# Docker Compose with volume driver
version: '3.8'
services:
  db:
    image: postgres
    volumes:
      - db-data:/var/lib/postgresql/data

volumes:
  db-data:
    driver: rexray/ebs
    driver_opts:
      size: 100
      volumetype: gp2
      encrypted: true
```

---

## 📱 API Reference

### Docker Engine API

#### Container Operations
```bash
# List containers via API
curl --unix-socket /var/run/docker.sock \
  http://localhost/containers/json

# Create container via API
curl -X POST --unix-socket /var/run/docker.sock \
  -H "Content-Type: application/json" \
  -d '{
    "Image": "nginx:latest",
    "Cmd": ["nginx", "-g", "daemon off;"],
    "ExposedPorts": {"80/tcp": {}},
    "HostConfig": {
      "PortBindings": {"80/tcp": [{"HostPort": "8080"}]}
    }
  }' \
  http://localhost/containers/create?name=my-nginx

# Start container
curl -X POST --unix-socket /var/run/docker.sock \
  http://localhost/containers/my-nginx/start
```

#### Image Operations
```bash
# Pull image via API
curl -X POST --unix-socket /var/run/docker.sock \
  "http://localhost/images/create?fromImage=ubuntu&tag=latest"

# Build image via API
curl -X POST --unix-socket /var/run/docker.sock \
  -H "Content-Type: application/x-tar" \
  --data-binary @Dockerfile.tar \
  "http://localhost/build?t=myapp:latest"

# List images
curl --unix-socket /var/run/docker.sock \
  http://localhost/images/json
```

### Docker SDK Examples

#### Python SDK
```python
import docker

# Initialize client
client = docker.from_env()

# List containers
containers = client.containers.list()
for container in containers:
    print(f"Container: {container.name}, Status: {container.status}")

# Run container
container = client.containers.run(
    "nginx:latest",
    ports={'80/tcp': 8080},
    detach=True,
    name="my-nginx"
)

# Build image
image = client.images.build(
    path=".",
    tag="myapp:latest",
    dockerfile="Dockerfile"
)

# Push image
client.images.push("myapp:latest")
```

#### Go SDK
```go
package main

import (
    "context"
    "fmt"
    "github.com/docker/docker/api/types"
    "github.com/docker/docker/client"
)

func main() {
    ctx := context.Background()
    cli, err := client.NewClientWithOpts(client.FromEnv)
    if err != nil {
        panic(err)
    }

    // List containers
    containers, err := cli.ContainerList(ctx, types.ContainerListOptions{})
    if err != nil {
        panic(err)
    }

    for _, container := range containers {
        fmt.Printf("Container: %s, Image: %s\n", 
            container.Names[0], container.Image)
    }
}
```

#### Node.js SDK
```javascript
const Docker = require('dockerode');
const docker = new Docker();

// List containers
async function listContainers() {
    try {
        const containers = await docker.listContainers();
        containers.forEach(container => {
            console.log(`Container: ${container.Names[0]}, Status: ${container.Status}`);
        });
    } catch (error) {
        console.error('Error:', error);
    }
}

// Create and start container
async function runContainer() {
    try {
        const container = await docker.createContainer({
            Image: 'nginx:latest',
            name: 'my-nginx',
            ExposedPorts: { '80/tcp': {} },
            HostConfig: {
                PortBindings: { '80/tcp': [{ HostPort: '8080' }] }
            }
        });
        
        await container.start();
        console.log('Container started successfully');
    } catch (error) {
        console.error('Error:', error);
    }
}
```

---

## 🏗️ Real-World Examples

### Full-Stack Web Application

#### Django Application with PostgreSQL
```dockerfile
# Dockerfile for Django application
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=myproject.settings.production

# Install system dependencies
RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Create app user
RUN adduser --disabled-password --gecos '' appuser

# Set working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY --chown=appuser:appuser . .

# Switch to app user
USER appuser

# Collect static files
RUN python manage.py collectstatic --noinput

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python manage.py check --deploy || exit 1

# Expose port
EXPOSE 8000

# Run application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "myproject.wsgi:application"]
```

```yaml
# docker-compose.yml for Django stack
version: '3.8'

services:
  db:
    image: postgres:15
    environment:
      POSTGRES_DB: myproject
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5

  redis:
    image: redis:7-alpine
    command: redis-server --appendonly yes
    volumes:
      - redis_data:/data

  web:
    build: .
    command: gunicorn --bind 0.0.0.0:8000 myproject.wsgi:application
    environment:
      - DATABASE_URL=postgresql://postgres:postgres@db:5432/myproject
      - REDIS_URL=redis://redis:6379
      - DEBUG=False
    ports:
      - "8000:8000"
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_started
    volumes:
      - static_volume:/app/staticfiles
      - media_volume:/app/media

  celery:
    build: .
    command: celery -A myproject worker -l info
    environment:
      - DATABASE_URL=postgresql://postgres:postgres@db:5432/myproject
      - REDIS_URL=redis://redis:6379
    depends_on:
      - db
      - redis

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
      - static_volume:/var/www/html/static
      - media_volume:/var/www/html/media
    depends_on:
      - web

volumes:
  postgres_data:
  redis_data:
  static_volume:
  media_volume:
```

### Microservices Architecture

#### Service Discovery with Consul
```yaml
# docker-compose.yml for microservices
version: '3.8'

services:
  consul:
    image: consul:latest
    ports:
      - "8500:8500"
    command: consul agent -dev -ui -client 0.0.0.0

  user-service:
    build: ./user-service
    ports:
      - "3001:3000"
    environment:
      - CONSUL_HOST=consul
      - SERVICE_NAME=user-service
      - SERVICE_PORT=3000
    depends_on:
      - consul
      - user-db

  product-service:
    build: ./product-service
    ports:
      - "3002:3000"
    environment:
      - CONSUL_HOST=consul
      - SERVICE_NAME=product-service
      - SERVICE_PORT=3000
    depends_on:
      - consul
      - product-db

  order-service:
    build: ./order-service
    ports:
      - "3003:3000"
    environment:
      - CONSUL_HOST=consul
      - SERVICE_NAME=order-service
      - SERVICE_PORT=3000
    depends_on:
      - consul
      - order-db

  api-gateway:
    build: ./api-gateway
    ports:
      - "8080:8080"
    environment:
      - CONSUL_HOST=consul
    depends_on:
      - consul
      - user-service
      - product-service
      - order-service

  user-db:
    image: postgres:15
    environment:
      POSTGRES_DB: userdb
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
    volumes:
      - user_db_data:/var/lib/postgresql/data

  product-db:
    image: postgres:15
    environment:
      POSTGRES_DB: productdb
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
    volumes:
      - product_db_data:/var/lib/postgresql/data

  order-db:
    image: postgres:15
    environment:
      POSTGRES_DB: orderdb
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
    volumes:
      - order_db_data:/var/lib/postgresql/data

volumes:
  user_db_data:
  product_db_data:
  order_db_data:
```

### CI/CD Pipeline Integration

#### GitLab CI with Docker
```yaml
# .gitlab-ci.yml
stages:
  - test
  - build
  - security
  - deploy

variables:
  DOCKER_DRIVER: overlay2
  DOCKER_TLS_CERTDIR: "/certs"
  REGISTRY: registry.gitlab.com
  IMAGE_NAME: $CI_PROJECT_PATH

services:
  - docker:dind

before_script:
  - docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY

test:
  stage: test
  image: docker:latest
  script:
    - docker build --target development -t $IMAGE_NAME:test .
    - docker run --rm $IMAGE_NAME:test pytest tests/
  only:
    - merge_requests
    - main

build:
  stage: build
  image: docker:latest
  script:
    - docker build --target production -t $REGISTRY/$IMAGE_NAME:$CI_COMMIT_SHA .
    - docker build --target production -t $REGISTRY/$IMAGE_NAME:latest .
    - docker push $REGISTRY/$IMAGE_NAME:$CI_COMMIT_SHA
    - docker push $REGISTRY/$IMAGE_NAME:latest
  only:
    - main

security_scan:
  stage: security
  image: docker:latest
  script:
    - docker run --rm -v /var/run/docker.sock:/var/run/docker.sock 
      aquasec/trivy image $REGISTRY/$IMAGE_NAME:$CI_COMMIT_SHA
  allow_failure: true
  only:
    - main

deploy_staging:
  stage: deploy
  image: docker/compose:latest
  script:
    - docker-compose -f docker-compose.staging.yml pull
    - docker-compose -f docker-compose.staging.yml up -d
  environment:
    name: staging
    url: https://staging.example.com
  only:
    - main

deploy_production:
  stage: deploy
  image: docker/compose:latest
  script:
    - docker-compose -f docker-compose.production.yml pull
    - docker-compose -f docker-compose.production.yml up -d
  environment:
    name: production
    url: https://production.example.com
  when: manual
  only:
    - main
```

---

## 🔒 Security Best Practices

### Container Security

#### Secure Base Images
```dockerfile
# Use official, minimal base images
FROM python:3.11-slim

# Update packages and remove package manager cache
RUN apt-get update && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends \
        gcc \
        libc6-dev \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Set working directory
WORKDIR /app

# Copy and install dependencies as root
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code and change ownership
COPY --chown=appuser:appuser . .

# Switch to non-root user
USER appuser

# Use COPY instead of ADD
COPY config.json /app/config.json

# Avoid running as root
# Don't use: USER root
# Don't use: RUN chmod 777 /app
```

#### Security Scanning
```bash
# Scan images for vulnerabilities
docker run --rm -v /var/run/docker.sock:/var/run/docker.sock \
    aquasec/trivy image myapp:latest

# Scan with Snyk
docker run --rm -it \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v $(pwd):/app \
    snyk/snyk:docker test myapp:latest

# Scan with Clair
docker run -d --name clair-db postgres:latest
docker run -d --name clair --link clair-db:postgres \
    quay.io/coreos/clair:latest
```

#### Runtime Security
```yaml
# Docker Compose security configurations
version: '3.8'

services:
  app:
    image: myapp:latest
    security_opt:
      - no-new-privileges:true
      - apparmor:docker-default
    cap_drop:
      - ALL
    cap_add:
      - NET_BIND_SERVICE
    read_only: true
    tmpfs:
      - /tmp
      - /var/run
    volumes:
      - ./data:/app/data:ro
    user: "1000:1000"
    ulimits:
      nproc: 65535
      nofile:
        soft: 65535
        hard: 65535
```

### Secrets Management

#### Docker Secrets (Swarm)
```yaml
# docker-compose.yml with secrets
version: '3.8'

services:
  web:
    image: myapp:latest
    secrets:
      - db_password
      - api_key
    environment:
      - DB_PASSWORD_FILE=/run/secrets/db_password
      - API_KEY_FILE=/run/secrets/api_key

secrets:
  db_password:
    external: true
  api_key:
    external: true
```

```bash
# Create secrets in Swarm
echo "my_secure_password" | docker secret create db_password -
echo "my_api_key" | docker secret create api_key -

# Deploy stack with secrets
docker stack deploy -c docker-compose.yml myapp
```

#### External Secrets Integration
```yaml
# Using external secrets operator
apiVersion: external-secrets.io/v1beta1
kind: SecretStore
metadata:
  name: vault-secret-store
spec:
  provider:
    vault:
      server: "https://vault.example.com"
      path: "secret"
      version: "v2"
      auth:
        kubernetes:
          mountPath: "kubernetes"
          role: "myapp"
---
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata:
  name: app-secrets
spec:
  secretStoreRef:
    name: vault-secret-store
    kind: SecretStore
  target:
    name: app-secrets
    creationPolicy: Owner
  data:
  - secretKey: database-password
    remoteRef:
      key: database
      property: password
```

### Network Security

#### Network Isolation
```bash
# Create isolated networks
docker network create --internal backend-network
docker network create frontend-network

# Run containers in isolated networks
docker run -d --name db --network backend-network postgres
docker run -d --name app --network backend-network --network frontend-network myapp
docker run -d --name proxy --network frontend-network nginx
```

#### TLS/SSL Configuration
```yaml
# nginx.conf for TLS termination
server {
    listen 443 ssl http2;
    server_name example.com;

    ssl_certificate /etc/nginx/ssl/cert.pem;
    ssl_certificate_key /etc/nginx/ssl/key.pem;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers ECDHE-RSA-AES256-GCM-SHA512:DHE-RSA-AES256-GCM-SHA512;
    ssl_prefer_server_ciphers off;
    ssl_session_cache shared:SSL:10m;

    location / {
        proxy_pass http://app:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

---

## 📊 Monitoring & Observability

### Container Metrics

#### Prometheus Configuration
```yaml
# docker-compose.monitoring.yml
version: '3.8'

services:
  prometheus:
    image: prom/prometheus:latest
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
      - prometheus_data:/prometheus
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'
      - '--storage.tsdb.path=/prometheus'
      - '--web.console.libraries=/etc/prometheus/console_libraries'
      - '--web.console.templates=/etc/prometheus/consoles'

  grafana:
    image: grafana/grafana:latest
    ports:
      - "3000:3000"
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=admin
    volumes:
      - grafana_data:/var/lib/grafana
      - ./grafana/dashboards:/etc/grafana/provisioning/dashboards
      - ./grafana/datasources:/etc/grafana/provisioning/datasources

  node-exporter:
    image: prom/node-exporter:latest
    ports:
      - "9100:9100"
    volumes:
      - /proc:/host/proc:ro
      - /sys:/host/sys:ro
      - /:/rootfs:ro
    command:
      - '--path.procfs=/host/proc'
      - '--path.rootfs=/rootfs'
      - '--path.sysfs=/host/sys'
      - '--collector.filesystem.mount-points-exclude=^/(sys|proc|dev|host|etc)($$|/)'

  cadvisor:
    image: gcr.io/cadvisor/cadvisor:latest
    ports:
      - "8080:8080"
    volumes:
      - /:/rootfs:ro
      - /var/run:/var/run:ro
      - /sys:/sys:ro
      - /var/lib/docker/:/var/lib/docker:ro
      - /dev/disk/:/dev/disk:ro
    privileged: true
    devices:
      - /dev/kmsg

volumes:
  prometheus_data:
  grafana_data:
```

#### Prometheus Configuration File
```yaml
# prometheus.yml
global:
  scrape_interval: 15s
  evaluation_interval: 15s

rule_files:
  - "alert_rules.yml"

scrape_configs:
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']

  - job_name: 'node-exporter'
    static_configs:
      - targets: ['node-exporter:9100']

  - job_name: 'cadvisor'
    static_configs:
      - targets: ['cadvisor:8080']

  - job_name: 'docker-containers'
    docker_sd_configs:
      - host: unix:///var/run/docker.sock
        refresh_interval: 5s
    relabel_configs:
      - source_labels: [__meta_docker_container_name]
        target_label: container_name
      - source_labels: [__meta_docker_container_id]
        target_label: container_id

alerting:
  alertmanagers:
    - static_configs:
        - targets:
          - alertmanager:9093
```

### Centralized Logging

#### ELK Stack Configuration
```yaml
# docker-compose.logging.yml
version: '3.8'

services:
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:8.5.0
    environment:
      - discovery.type=single-node
      - "ES_JAVA_OPTS=-Xms512m -Xmx512m"
      - xpack.security.enabled=false
    ports:
      - "9200:9200"
    volumes:
      - elasticsearch_data:/usr/share/elasticsearch/data

  logstash:
    image# 🐳 Docker Documentation Hub

[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com/)
[![Documentation](https://img.shields.io/badge/Documentation-1f425f.svg?style=for-the-badge)](https://github.com/yourusername/docker-docs)
[![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg?style=for-the-badge)](CONTRIBUTING.md)

> **A comprehensive, enterprise-ready documentation project for Docker containerization platform**

Welcome to the most complete Docker documentation resource! This repository provides in-depth guides, best practices, real-world examples, and enterprise patterns to help you master Docker from beginner to expert level.

---

## 📚 Table of Contents

- [🌟 Features](#-features)
- [🚀 Quick Start](#-quick-start)
- [📖 Documentation Structure](#-documentation-structure)
- [💻 Installation Methods](#-installation-methods)
- [🔧 Docker Fundamentals](#-docker-fundamentals)
- [📋 Prerequisites](#-prerequisites)
- [🛠️ Advanced Topics](#️-advanced-topics)
- [📱 API Reference](#-api-reference)
- [🏗️ Real-World Examples](#️-real-world-examples)
- [🔒 Security Best Practices](#-security-best-practices)
- [📊 Monitoring & Observability](#-monitoring--observability)
- [🤝 Contributing](#-contributing)
- [🆘 Support & Troubleshooting](#-support--troubleshooting)
- [📜 License](#-license)
- [🙏 Acknowledgments](#-acknowledgments)

---

## 🌟 Features

### 📖 Comprehensive Coverage
- **Complete Installation Guides** - Multiple installation methods across all platforms
- **Dockerfile Mastery** - From basic to advanced multi-stage builds
- **Docker Compose** - Orchestrating multi-container applications
- **Container Security** - Enterprise-grade security hardening
- **Performance Optimization** - Production-ready container optimization

### 🎯 Practical Examples
- **Real-world Applications** - Complete application containerization
- **Microservices Architecture** - Container-based microservices patterns
- **CI/CD Integration** - Docker in continuous integration pipelines
- **Cloud Deployment** - AWS, Azure, GCP container deployments
- **Orchestration** - Kubernetes, Docker Swarm, and more

### 🔧 Advanced Features
- **Multi-stage Builds** - Optimized container builds
- **Health Checks** - Container health monitoring
- **Networking** - Advanced container networking
- **Storage** - Persistent data management
- **Registry Management** - Private registry setup and management

---

## 🚀 Quick Start

### For Absolute Beginners
```bash
# Install Docker (Ubuntu/Debian)
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Verify installation
docker --version
docker run hello-world

# Your first container
docker run -it ubuntu:latest bash
```

### For Developers
```bash
# Clone this documentation
git clone https://github.com/yourusername/docker-docs.git
cd docker-docs

# Start with practical examples
1. Read: docs/getting-started/README.md
2. Follow: examples/web-app-containerization/
3. Try: examples/microservices-example/
```

### For DevOps Engineers
```bash
# Jump to advanced topics
1. Architecture: docs/architecture/container-orchestration.md
2. Security: docs/security/enterprise-hardening.md
3. Monitoring: docs/monitoring/container-observability.md
```

---

## 📖 Documentation Structure

```
docker-docs/
├── 📁 docs/
│   ├── 🚀 getting-started/
│   │   ├── overview.md                    # Docker fundamentals
│   │   ├── core-concepts.md              # Images, containers, volumes
│   │   ├── dockerfile-basics.md          # Your first Dockerfile
│   │   └── docker-compose-intro.md       # Multi-container applications
│   │
│   ├── ⚙️ installation/
│   │   ├── linux/
│   │   │   ├── ubuntu-debian.md          # Ubuntu/Debian installation
│   │   │   ├── centos-rhel.md            # CentOS/RHEL installation
│   │   │   ├── arch-linux.md             # Arch Linux installation
│   │   │   └── post-install-setup.md     # Post-installation configuration
│   │   ├── windows/
│   │   │   ├── docker-desktop.md         # Docker Desktop for Windows
│   │   │   ├── wsl2-backend.md           # WSL2 backend configuration
│   │   │   └── hyper-v-setup.md          # Hyper-V configuration
│   │   ├── macos/
│   │   │   ├── docker-desktop-mac.md     # Docker Desktop for Mac
│   │   │   ├── homebrew-install.md       # Homebrew installation
│   │   │   └── m1-arm-setup.md           # Apple Silicon (M1/M2) setup
│   │   └── cloud/
│   │       ├── aws-ec2.md                # AWS EC2 Docker setup
│   │       ├── azure-vm.md               # Azure VM Docker setup
│   │       └── gcp-compute.md            # GCP Compute Engine setup
│   │
│   ├── 🐳 dockerfile/
│   │   ├── syntax-reference.md           # Complete Dockerfile syntax
│   │   ├── best-practices.md             # Dockerfile best practices
│   │   ├── multi-stage-builds.md         # Multi-stage build patterns
│   │   ├── optimization-techniques.md    # Image size optimization
│   │   ├── security-considerations.md    # Security in Dockerfiles
│   │   └── language-specific/
│   │       ├── python-dockerfile.md      # Python application Dockerfiles
│   │       ├── nodejs-dockerfile.md      # Node.js application Dockerfiles
│   │       ├── java-dockerfile.md        # Java application Dockerfiles
│   │       ├── golang-dockerfile.md      # Go application Dockerfiles
│   │       └── dotnet-dockerfile.md      # .NET application Dockerfiles
│   │
│   ├── 🔧 docker-compose/
│   │   ├── compose-file-reference.md     # Complete compose file syntax
│   │   ├── services-configuration.md     # Service configuration patterns
│   │   ├── networking.md                 # Compose networking
│   │   ├── volumes-and-storage.md        # Data persistence
│   │   ├── environment-variables.md      # Environment management
│   │   ├── secrets-management.md         # Secrets in compose
│   │   └── production-patterns/
│   │       ├── web-app-stack.md          # LAMP/MEAN/MERN stacks
│   │       ├── microservices-compose.md  # Microservices with compose
│   │       ├── monitoring-stack.md       # Prometheus/Grafana stack
│   │       └── logging-stack.md          # ELK/EFK stack
│   │
│   ├── 🌐 networking/
│   │   ├── network-types.md              # Bridge, host, overlay networks
│   │   ├── custom-networks.md            # Creating custom networks
│   │   ├── inter-container-communication.md # Container-to-container
│   │   ├── port-mapping.md               # Port publishing strategies
│   │   ├── load-balancing.md             # Load balancing patterns
│   │   └── network-security.md           # Network security best practices
│   │
│   ├── 💾 storage/
│   │   ├── volumes-overview.md           # Docker volumes explained
│   │   ├── bind-mounts.md                # Host directory mounting
│   │   ├── tmpfs-mounts.md               # Temporary filesystems
│   │   ├── volume-drivers.md             # Storage drivers and plugins
│   │   ├── backup-strategies.md          # Data backup patterns
│   │   └── performance-tuning.md         # Storage performance optimization
│   │
│   ├── 🔒 security/
│   │   ├── container-security.md         # Container security fundamentals
│   │   ├── image-security.md             # Secure image building
│   │   ├── runtime-security.md           # Runtime security measures
│   │   ├── secrets-management.md         # Secrets and credentials
│   │   ├── user-namespaces.md            # User namespace isolation
│   │   ├── apparmor-selinux.md           # AppArmor and SELinux
│   │   └── vulnerability-scanning.md     # Security scanning tools
│   │
│   ├── 📊 monitoring/
│   │   ├── container-metrics.md          # Container metrics collection
│   │   ├── logging-strategies.md         # Centralized logging
│   │   ├── health-checks.md              # Container health monitoring
│   │   ├── prometheus-integration.md     # Prometheus monitoring
│   │   ├── grafana-dashboards.md         # Grafana visualization
│   │   └── alerting-setup.md             # Alert configuration
│   │
│   ├── 🏗️ orchestration/
│   │   ├── docker-swarm/
│   │   │   ├── swarm-mode-overview.md    # Docker Swarm introduction
│   │   │   ├── cluster-setup.md          # Swarm cluster setup
│   │   │   ├── service-deployment.md     # Service deployment patterns
│   │   │   └── swarm-networking.md       # Swarm networking
│   │   ├── kubernetes/
│   │   │   ├── docker-kubernetes.md      # Docker in Kubernetes
│   │   │   ├── pod-specifications.md     # Pod and container specs
│   │   │   ├── deployment-strategies.md  # Deployment patterns
│   │   │   └── service-mesh.md           # Service mesh integration
│   │   └── nomad/
│   │       ├── nomad-docker.md           # HashiCorp Nomad integration
│   │       └── job-specifications.md     # Nomad job specs
│   │
│   ├── ☁️ cloud-integration/
│   │   ├── aws/
│   │   │   ├── ecs-fargate.md            # AWS ECS and Fargate
│   │   │   ├── ecr-registry.md           # Amazon ECR
│   │   │   ├── lambda-containers.md      # AWS Lambda containers
│   │   │   └── batch-processing.md       # AWS Batch
│   │   ├── azure/
│   │   │   ├── container-instances.md    # Azure Container Instances
│   │   │   ├── kubernetes-service.md     # Azure Kubernetes Service
│   │   │   ├── container-registry.md     # Azure Container Registry
│   │   │   └── app-service.md            # Azure App Service containers
│   │   ├── gcp/
│   │   │   ├── cloud-run.md              # Google Cloud Run
│   │   │   ├── gke-deployment.md         # Google Kubernetes Engine
│   │   │   ├── container-registry.md     # Google Container Registry
│   │   │   └── compute-engine.md         # GCE container deployments
│   │   └── multi-cloud/
│   │       ├── cloud-agnostic-patterns.md # Cloud-agnostic designs
│   │       └── hybrid-deployments.md     # Hybrid cloud strategies
│   │
│   ├── 🔄 ci-cd-integration/
│   │   ├── jenkins-docker.md             # Jenkins and Docker
│   │   ├── github-actions.md             # GitHub Actions integration
│   │   ├── gitlab-ci.md                  # GitLab CI/CD integration
│   │   ├── azure-devops.md               # Azure DevOps integration
│   │   ├── circleci.md                   # CircleCI integration
│   │   └── tekton-pipelines.md           # Tekton CI/CD
│   │
│   ├── 🛡️ registry/
│   │   ├── docker-hub.md                 # Docker Hub usage
│   │   ├── private-registry.md           # Setting up private registry
│   │   ├── harbor-setup.md               # Harbor enterprise registry
│   │   ├── security-scanning.md          # Registry security scanning
│   │   └── image-management.md           # Image lifecycle management
│   │
│   └── 🆘 troubleshooting/
│       ├── common-issues.md              # Common problems & solutions
│       ├── performance-debugging.md      # Performance troubleshooting
│       ├── networking-issues.md          # Network troubleshooting
│       ├── storage-problems.md           # Storage issue resolution
│       └── log-analysis.md               # Container log analysis
│
├── 📁 examples/
│   ├── web-applications/
│   │   ├── django-app/                   # Django application containerization
│   │   ├── nodejs-express/               # Node.js Express application
│   │   ├── react-frontend/               # React frontend application
│   │   ├── spring-boot/                  # Spring Boot application
│   │   └── nginx-reverse-proxy/          # Nginx reverse proxy setup
│   │
│   ├── databases/
│   │   ├── postgresql/                   # PostgreSQL containerization
│   │   ├── mysql/                        # MySQL containerization
│   │   ├── mongodb/                      # MongoDB containerization
│   │   ├── redis/                        # Redis containerization
│   │   └── elasticsearch/                # Elasticsearch containerization
│   │
│   ├── microservices/
│   │   ├── complete-microservices/       # Full microservices example
│   │   ├── api-gateway/                  # API Gateway pattern
│   │   ├── service-discovery/            # Service discovery patterns
│   │   └── event-driven-architecture/    # Event-driven microservices
│   │
│   ├── monitoring-stacks/
│   │   ├── prometheus-grafana/           # Monitoring stack
│   │   ├── elk-stack/                    # Elasticsearch, Logstash, Kibana
│   │   ├── jaeger-tracing/               # Distributed tracing
│   │   └── metrics-collection/           # Metrics collection patterns
│   │
│   ├── development-environments/
│   │   ├── full-stack-dev/               # Full-stack development setup
│   │   ├── database-dev-env/             # Database development environment
│   │   ├── testing-environment/          # Automated testing environment
│   │   └── code-quality-tools/           # Code quality and linting tools
│   │
│   └── production-patterns/
│       ├── blue-green-deployment/        # Blue-green deployment
│       ├── canary-deployment/            # Canary deployment patterns
│       ├── rolling-updates/              # Rolling update strategies
│       └── disaster-recovery/            # Disaster recovery patterns
│
├── 📁 scripts/
│   ├── installation/                     # Installation automation scripts
│   ├── container-management/             # Container lifecycle scripts
│   ├── image-optimization/               # Image optimization tools
│   ├── security-scanning/                # Security scanning automation
│   ├── monitoring/                       # Monitoring setup scripts
│   └── backup-restore/                   # Backup and restore scripts
│
├── 📁 templates/
│   ├── dockerfile-templates/             # Production-ready Dockerfile templates
│   ├── compose-templates/                # Docker Compose templates
│   ├── kubernetes-manifests/             # Kubernetes deployment templates
│   ├── ci-cd-pipelines/                  # CI/CD pipeline templates
│   └── monitoring-configs/               # Monitoring configuration templates
│
└── 📁 assets/
    ├── diagrams/                         # Architecture diagrams
    ├── images/                           # Documentation images
    ├── videos/                           # Tutorial videos
    └── cheat-sheets/                     # Quick reference guides
```

---

## 💻 Installation Methods

### 🐧 Linux Distributions

#### Ubuntu/Debian (Recommended)
```bash
# Remove old versions
sudo apt-get remove docker docker-engine docker.io containerd runc

# Update package index
sudo apt-get update

# Install required packages
sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

# Add Docker's official GPG key
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

# Set up repository
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install Docker Engine
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin

# Verify installation
sudo docker run hello-world
```

#### CentOS/RHEL/Fedora
```bash
# Remove old versions
sudo yum remove docker \
    docker-client \
    docker-client-latest \
    docker-common \
    docker-latest \
    docker-latest-logrotate \
    docker-logrotate \
    docker-engine

# Install yum-utils
sudo yum install -y yum-utils

# Set up repository
sudo yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo

# Install Docker Engine
sudo yum install docker-ce docker-ce-cli containerd.io docker-compose-plugin

# Start Docker
sudo systemctl start docker
sudo systemctl enable docker

# Verify installation
sudo docker run hello-world
```

#### Arch Linux
```bash
# Install Docker
sudo pacman -S docker docker-compose

# Start and enable Docker service
sudo systemctl start docker.service
sudo systemctl enable docker.service

# Add user to docker group
sudo usermod -aG docker $USER

# Verify installation
docker run hello-world
```

### 🪟 Windows

#### Docker Desktop for Windows
1. **Download**: [Docker Desktop for Windows](https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe)
2. **System Requirements**:
   - Windows 10/11 64-bit
   - WSL 2 feature enabled
   - BIOS-level hardware virtualization support

```powershell
# Enable WSL 2 (Run as Administrator)
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart

# Restart computer and install Docker Desktop
# Verify installation
docker --version
docker run hello-world
```

#### Windows Server
```powershell
# Install Docker on Windows Server 2019/2022
Install-Module -Name DockerMsftProvider -Repository PSGallery -Force
Install-Package -Name docker -ProviderName DockerMsftProvider

# Start Docker service
Start-Service Docker

# Verify installation
docker run hello-world
```

### 🍎 macOS

#### Docker Desktop for Mac
1. **Download**: [Docker Desktop for Mac](https://desktop.docker.com/mac/main/amd64/Docker.dmg)
2. **System Requirements**:
   - macOS 10.15 or newer
   - Apple Silicon (M1/M2) or Intel processor

```bash
# Alternative: Install via Homebrew
brew install --cask docker

# Start Docker Desktop from Applications
# Verify installation
docker --version
docker run hello-world
```

#### Mac with Apple Silicon (M1/M2)
```bash
# Install Docker Desktop for Apple Silicon
# Download ARM64 version from Docker website

# For command line installation
arch -arm64 brew install --cask docker

# Verify architecture
docker version --format 'Server: {{.Server.Arch}}'
```

### 🐳 Docker Installation Script (Universal)
```bash
# Official Docker installation script (Linux)
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Add current user to docker group
sudo usermod -aG docker $USER

# Apply group membership
newgrp docker

# Verify installation
docker --version
docker-compose --version
```

---

## 🔧 Docker Fundamentals

### Core Concepts

#### 1. Images and Containers
```bash
# Understanding Docker Images
docker images                    # List all images
docker image inspect ubuntu     # Inspect image details
docker image history ubuntu     # Show image layers

# Working with Containers
docker ps                       # List running containers
docker ps -a                    # List all containers
docker container inspect myapp  # Inspect container details
```

#### 2. Container Lifecycle
```bash
# Container lifecycle management
docker create --name myapp nginx        # Create container
docker start myapp                      # Start container
docker stop myapp                       # Stop container
docker restart myapp                    # Restart container
docker pause myapp                      # Pause container
docker unpause myapp                    # Unpause container
docker rm myapp                         # Remove container
```

### Your First Dockerfile

#### Basic Dockerfile Structure
```dockerfile
# Use official base image
FROM ubuntu:22.04

# Set metadata
LABEL maintainer="your-email@example.com"
LABEL description="My first Docker application"
LABEL version="1.0.0"

# Set environment variables
ENV APP_HOME=/app
ENV APP_USER=appuser

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Create application user
RUN groupadd -r ${APP_USER} && \
    useradd -r -g ${APP_USER} ${APP_USER}

# Create application directory
RUN mkdir -p ${APP_HOME} && \
    chown -R ${APP_USER}:${APP_USER} ${APP_HOME}

# Set working directory
WORKDIR ${APP_HOME}

# Copy application files
COPY --chown=${APP_USER}:${APP_USER} requirements.txt .
COPY --chown=${APP_USER}:${APP_USER} . .

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Switch to non-root user
USER ${APP_USER}

# Expose port
EXPOSE 8000

# Add health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Define entrypoint
ENTRYPOINT ["python3"]
CMD ["app.py"]
```

#### Advanced Multi-stage Dockerfile
```dockerfile
# Multi-stage build for Python application
FROM python:3.11-slim as base

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Development stage
FROM base as development
RUN pip install pytest pytest-cov black flake8
COPY requirements-dev.txt .
RUN pip install -r requirements-dev.txt
WORKDIR /app
CMD ["python", "-m", "pytest"]

# Dependencies stage
FROM base as dependencies
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Production stage
FROM python:3.11-slim as production

# Copy installed packages from dependencies stage
COPY --from=dependencies /root/.local /root/.local

# Create non-root user
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Set working directory
WORKDIR /app

# Copy application code
COPY --chown=appuser:appuser . .

# Switch to non-root user
USER appuser

# Add local packages to PATH
ENV PATH=/root/.local/bin:$PATH

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python health_check.py || exit 1

# Expose port
EXPOSE 8000

# Run application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "app:app"]
```

### Docker Compose Essentials

#### Basic Docker Compose File
```yaml
version: '3.8'

services:
  web:
    build: 
      context: .
      dockerfile: Dockerfile
      target: production
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://user:password@db:5432/mydb
      - REDIS_URL=redis://redis:6379/0
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_started
    volumes:
      - ./app:/app
      - static_volume:/app/staticfiles
    networks:
      - app-network
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s

  db:
    image: postgres:15
    environment:
      POSTGRES_DB: mydb
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql
    networks:
      - app-network
    restart: unless-stopped
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U user -d mydb"]
      interval: 10s
      timeout: 5s
      retries: 5

  redis:
    image: redis:7-alpine
    command: redis-server --appendonly yes
    volumes:
      - redis_data:/data
    networks:
      - app-network
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 3s
      retries: 3

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
      - static_volume:/var/www/html/static:ro
      - ssl_certs:/etc/nginx/ssl:ro
    depends_on:
      - web
    networks:
      - app-network
    restart: unless-stopped

volumes:
  postgres_data:
    driver: local
  redis_data:
    driver: local
  static_volume:
    driver: local
  ssl_certs:
    driver: local

networks:
  app-network:
    driver: bridge
    ipam:
      config:
        - subnet: 172.20.0.0/16
```

#### Production Docker Compose
```yaml
version: '3.8'

x-common-variables: &common-variables
  ENVIRONMENT: production
  LOG_LEVEL: info

x-restart-policy: &restart-policy
  restart: unless-stopped

services:
  web:
    <<: *restart-policy
    build:
      context: .
      dockerfile: Dockerfile.prod
      args:
        BUILD_DATE: ${BUILD_DATE}
        VCS_REF: ${VCS_REF}
    ports:
      - "8000:8000"
    environment:
      <<: *common-variables
      DATABASE_URL: postgresql://${DB_USER}:${DB_PASSWORD}@db:5432/${DB_NAME}
      REDIS_URL: redis://redis:6379/0
      SECRET_KEY: ${SECRET_KEY}
    env_file:
      - .env.production
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_healthy
    volumes:
      - static_volume:/app/staticfiles:ro
      - media_volume:/app/media
      - logs_volume:/app/logs
    networks:
      - app-network
      - monitoring-network
    deploy:
      replicas: 3
      resources:
        limits:
          cpus: '0.5'
          memory: 512M
        reservations:
          cpus: '0.25'
          memory: 256M
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health/"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"

  db:
    <<: *restart-policy
    image: postgres:15
    environment:
      POSTGRES_DB: ${DB_NAME}
      POSTGRES_USER: ${DB_USER}
      POSTGRES_PASSWORD: ${DB_PASSWORD}
      POSTGRES_INITDB_ARGS: "--encoding=UTF8 --lc-collate=C --lc-ctype=C"
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./postgresql.conf:/etc/postgresql/postgresql.conf:ro
      - ./pg_hba.conf:/etc/postgresql/pg_hba.conf:ro
      - postgres_logs:/var/log/postgresql
    networks:
      - app-network
    deploy:
      resources:
        limits:
          cpus: '1.0'
          memory: 1G
        reservations:
          cpus: '0.5'
          memory: 512M
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${DB_USER} -d ${DB_NAME}"]
      interval: 10s
      timeout: 5s
      retries: 5
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"

  redis:
    <<: *restart-policy
    image: redis:7-alpine
    command: >
      redis-server
      --appendonly yes
      --appendfsync everysec
      --maxmemory 256mb
      --maxmemory-policy allkeys-lru
    volumes:
      - redis_data:/data
      - ./redis.conf:/etc/redis/redis.conf:ro
    networks:
      - app-network
    deploy:
      resources:
        limits:
          cpus: '0.25'
          memory: 256M
        reservations:
          cpus: '0.1'
          memory: 128M
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 3s
      retries: 3

  nginx:
    <<: *restart-policy
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf:ro
      - ./nginx/conf.d:/etc/nginx/conf.d:ro
      - static_volume:/var/www/html/static:ro
      - media_volume:/var/www/html/media:ro
      - ssl_certs:/etc/nginx/ssl:ro
      - nginx_logs:/var/log/nginx
    depends_on:
      - web
    networks:
      - app-network
    deploy:
      resources:
        limits:
          cpus: '0.25'
          memory: 128M
        reservations:
          cpus: '0.1'
          memory: 64M
    healthcheck:
      test: ["CMD", "wget", "--quiet", "--tries=1", "--spider", "http://localhost/health"]
      interval: 30s
      timeout: 10s
      retries: 3

volumes:
  postgres_data:
    driver: local
    driver_opts:
      type: none
      o: bind
      device: /opt/docker-data/postgres
  redis_data:
    driver: local
  static_volume:
    driver: local
  media_volume:
    driver: local
  ssl_certs:
    driver: local
  logs_volume:
    driver: local
  postgres_logs:
    driver: local
  nginx_logs:
    driver: local

networks:
  app-network:
    driver: bridge
    ipam:
      config:
        - subnet: 172.20.0.0/16
  monitoring-network:
    external: true
```

---

## 📋 Prerequisites

### System Requirements

#### Minimum Requirements
- **CPU**: 2 cores
- **RAM**: 4 GB
- **Storage**: 20 GB free space
- **OS**: 64-bit operating system
- **Internet**: Stable internet connection

#### Recommended Requirements
- **CPU**: 4+ cores
- **RAM**: 8+ GB
- **Storage**: 100+ GB SSD
- **OS**: Latest 64-bit OS version
- **Network**: High-speed internet connection

### Software Dependencies

#### Required Software
```bash
# Git (for version control)
sudo apt update && sudo apt install git

# curl (for downloads)
sudo apt install curl

# Text editor (choose one)
sudo apt install vim nano code
```

#### Development Tools
```bash
# Build tools
sudo apt install build-essential

# Python development
sudo apt install python3 python3-pip python3-venv

# Node.js development
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt install nodejs

# Java development
sudo apt install openjdk-17-jdk maven
```

### Network Configuration

#### Firewall Settings
```bash
# Ubuntu/Debian
sudo ufw allow 2375/tcp    # Docker daemon (if needed)
sudo ufw allow 2376/tcp    # Docker daemon TLS
sudo ufw allow 80/tcp      # HTTP
sudo ufw allow 443/tcp     # HTTPS

# CentOS/RHEL
sudo firewall-cmd --permanent --add-port=2375/tcp
sudo firewall-cmd --permanent --add-port=2376/tcp
sudo firewall-cmd --permanent --add-port=80/tcp
sudo firewall-cmd --permanent --add-port=443/tcp
sudo firewall-cmd --reload
```

#### Proxy Configuration
```bash
# Configure Docker to use proxy
sudo mkdir -p /etc/systemd/system/docker.service.d

# Create proxy configuration
sudo cat > /etc/systemd/system/docker.service.d/http-proxy.conf << EOF
[Service]
Environment="HTTP_PROXY=http://proxy.example.com:8080"
Environment="HTTPS_PROXY=http://proxy.example.com:8080"
Environment="NO_PROXY=localhost,127.0.0.1,.example.com"
EOF

# Reload and restart Docker
sudo systemctl daemon-reload
sudo systemctl restart docker
```

---

## 🛠️ Advanced Topics

### Container Orchestration

#### Docker Swarm
```bash
# Initialize Docker Swarm
docker swarm init

# Add worker nodes
docker swarm join --token SWMTKN-1-token worker-node-ip:2377

# Deploy a stack
docker stack deploy -c docker-compose.yml myapp

# Scale services
docker service scale myapp_web=5

# Monitor services
docker service ls
docker service ps myapp_web
```

#### Kubernetes Integration
```yaml
# Kubernetes Deployment for Docker containers
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
    spec:
      containers:
      - name: myapp
        image: myapp:latest
        ports:
        - containerPort: 8000
        env:
        - name: DATABASE_URL
          valueFrom:
            secretKeyRef:
              name: myapp-secrets
              key: database-url
        resources:
          requests:
            memory: "256Mi"
            cpu: "250m"
          limits:
            memory: "512Mi"
            cpu: "500m"
        livenessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /ready
            port: 8000
          initialDelaySeconds: 5
          periodSeconds: 5
```

### Performance Optimization

#### Image Size Optimization
```dockerfile
# Use multi-stage builds
FROM node:18 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

FROM node:18-alpine AS production
RUN addgroup -g 1001 -S nodejs
RUN adduser -S nodejs -u 1001
WORKDIR /app
COPY --from=builder --chown=nodejs:nodejs /app/node_modules ./node_modules
COPY --chown=nodejs:nodejs . .
USER nodejs
EXPOSE 3000
CMD ["npm", "start"]
```

#### Build Caching Strategies
```dockerfile
# Optimize layer caching
FROM python:3.11-slim

# Install system dependencies first (changes rarely)
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies before code
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code last (changes frequently)
COPY . .

CMD ["python", "app.py"]
```

#### Resource Management
```yaml
# Docker Compose resource limits
services:
  web:
    image: myapp:latest
    deploy:
      resources:
        limits:
          cpus: '0.50'
          memory: 512M
        reservations:
          cpus: '0.25'
          memory: 256M
      restart_policy:
        condition: on-failure
        delay: 5s
        max_attempts: 3
        window: 120s
```

### Advanced Networking

#### Custom Bridge Networks
```bash
# Create custom bridge network
docker network create \
  --driver bridge \
  --subnet=172.20.0.0/16 \
  --ip-range=172.20.240.0/20 \
  --gateway=172.20.0.1 \
  my-bridge-network

# Connect containers to custom network
docker run -d --name web --network my-bridge-network nginx
docker run -d --name db --network my-bridge-network postgres
```

#### Overlay Networks (Swarm)
```bash
# Create overlay network
docker network create \
  --driver overlay \
  --subnet=10.0.0.0/16 \
  --attachable \
  my-overlay-network

# Use in stack deployment
services:
  web:
    image: nginx
    networks:
      - my-overlay-network
    deploy:
      replicas: 3

networks:
  my-overlay-network:
    external: true
```

#### Network Security
```bash
# Create isolated network
docker network create \
  --driver bridge \
  --internal \
  isolated-network

# Network with custom DNS
docker network create \
  --driver bridge \
  --dns=8.8.8.8 \
  --dns=8.8.4.4 \
  custom-dns-network
```

### Storage Solutions

#### Named Volumes
```bash
# Create named volume
docker volume create \
  --driver local \
  --opt type=nfs \
  --opt o=addr=192.168.1.100,rw \
  --opt device=:/path/to/nfs/share \
  nfs-volume

# Use in containers
docker run -d \
  --name myapp \
  -v nfs-volume:/app/data \
  myapp:latest
```

#### Bind Mounts with Options
```bash
# Bind mount with specific options
docker run -d \
  --name myapp \
  --mount type=bind,source=/host/path,target=/container/path,readonly \
  myapp:latest

# Bind mount with SELinux labels
docker run -d \
  --name myapp \
  -v /host/path:/container/path:Z \
  myapp:latest
```

#### Volume Plugins
```yaml
# Docker Compose with volume driver
version: '3.8'
services:
  db:
    image: postgres
    volumes:
      - db-data:/var/lib/postgresql/data

volumes:
  db-data:
    driver: rexray/ebs
    driver_opts:
      size: 100
      volumetype: gp2
      encrypted: true
```

---

## 📱 API Reference

### Docker Engine API

#### Container Operations
```bash
# List containers via API
curl --unix-socket /var/run/docker.sock \
  http://localhost/containers/json

# Create container via API
curl -X POST --unix-socket /var/run/docker.sock \
  -H "Content-Type: application/json" \
  -d '{
    "Image": "nginx:latest",
    "Cmd": ["nginx", "-g", "daemon off;"],
    "ExposedPorts": {"80/tcp": {}},
    "HostConfig": {
      "PortBindings": {"80/tcp": [{"HostPort": "8080"}]}
    }
  }' \
  http://localhost/containers/create?name=my-nginx

# Start container
curl -X POST --unix-socket /var/run/docker.sock \
  http://localhost/containers/my-nginx/start
```

#### Image Operations
```bash
# Pull image via API
curl -X POST --unix-socket /var/run/docker.sock \
  "http://localhost/images/create?fromImage=ubuntu&tag=latest"

# Build image via API
curl -X POST --unix-socket /var/run/docker.sock \
  -H "Content-Type: application/x-tar" \
  --data-binary @Dockerfile.tar \
  "http://localhost/build?t=myapp:latest"

# List images
curl --unix-socket /var/run/docker.sock \
  http://localhost/images/json
```

### Docker SDK Examples

#### Python SDK
```python
import docker

# Initialize client
client = docker.from_env()

# List containers
containers = client.containers.list()
for container in containers:
    print(f"Container: {container.name}, Status: {container.status}")

# Run container
container = client.containers.run(
    "nginx:latest",
    ports={'80/tcp': 8080},
    detach=True,
    name="my-nginx"
)

# Build image
image = client.images.build(
    path=".",
    tag="myapp:latest",
    dockerfile="Dockerfile"
)

# Push image
client.images.push("myapp:latest")
```

#### Go SDK
```go
package main

import (
    "context"
    "fmt"
    "github.com/docker/docker/api/types"
    "github.com/docker/docker/client"
)

func main() {
    ctx := context.Background()
    cli, err := client.NewClientWithOpts(client.FromEnv)
    if err != nil {
        panic(err)
    }

    // List containers
    containers, err := cli.ContainerList(ctx, types.ContainerListOptions{})
    if err != nil {
        panic(err)
    }

    for _, container := range containers {
        fmt.Printf("Container: %s, Image: %s\n", 
            container.Names[0], container.Image)
    }
}
```

#### Node.js SDK
```javascript
const Docker = require('dockerode');
const docker = new Docker();

// List containers
async function listContainers() {
    try {
        const containers = await docker.listContainers();
        containers.forEach(container => {
            console.log(`Container: ${container.Names[0]}, Status: ${container.Status}`);
        });
    } catch (error) {
        console.error('Error:', error);
    }
}

// Create and start container
async function runContainer() {
    try {
        const container = await docker.createContainer({
            Image: 'nginx:latest',
            name: 'my-nginx',
            ExposedPorts: { '80/tcp': {} },
            HostConfig: {
                PortBindings: { '80/tcp': [{ HostPort: '8080' }] }
            }
        });
        
        await container.start();
        console.log('Container started successfully');
    } catch (error) {
        console.error('Error:', error);
    }
}
```

---

## 🏗️ Real-World Examples

### Full-Stack Web Application

#### Django Application with PostgreSQL
```dockerfile
# Dockerfile for Django application
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=myproject.settings.production

# Install system dependencies
RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Create app user
RUN adduser --disabled-password --gecos '' appuser

# Set working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY --chown=appuser:appuser . .

# Switch to app user
USER appuser

# Collect static files
RUN python manage.py collectstatic --noinput

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python manage.py check --deploy || exit 1

# Expose port
EXPOSE 8000

# Run application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "myproject.wsgi:application"]
```

```yaml
# docker-compose.yml for Django stack
version: '3.8'

services:
  db:
    image: postgres:15
    environment:
      POSTGRES_DB: myproject
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5

  redis:
    image: redis:7-alpine
    command: redis-server --appendonly yes
    volumes:
      - redis_data:/data

  web:
    build: .
    command: gunicorn --bind 0.0.0.0:8000 myproject.wsgi:application
    environment:
      - DATABASE_URL=postgresql://postgres:postgres@db:5432/myproject
      - REDIS_URL=redis://redis:6379
      - DEBUG=False
    ports:
      - "8000:8000"
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_started
    volumes:
      - static_volume:/app/staticfiles
      - media_volume:/app/media

  celery:
    build: .
    command: celery -A myproject worker -l info
    environment:
      - DATABASE_URL=postgresql://postgres:postgres@db:5432/myproject
      - REDIS_URL=redis://redis:6379
    depends_on:
      - db
      - redis

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
      - static_volume:/var/www/html/static
      - media_volume:/var/www/html/media
    depends_on:
      - web

volumes:
  postgres_data:
  redis_data:
  static_volume:
  media_volume:
```

### Microservices Architecture

#### Service Discovery with Consul
```yaml
# docker-compose.yml for microservices
version: '3.8'

services:
  consul:
    image: consul:latest
    ports:
      - "8500:8500"
    command: consul agent -dev -ui -client 0.0.0.0

  user-service:
    build: ./user-service
    ports:
      - "3001:3000"
    environment:
      - CONSUL_HOST=consul
      - SERVICE_NAME=user-service
      - SERVICE_PORT=3000
    depends_on:
      - consul
      - user-db

  product-service:
    build: ./product-service
    ports:
      - "3002:3000"
    environment:
      - CONSUL_HOST=consul
      - SERVICE_NAME=product-service
      - SERVICE_PORT=3000
    depends_on:
      - consul
      - product-db

  order-service:
    build: ./order-service
    ports:
      - "3003:3000"
    environment:
      - CONSUL_HOST=consul
      - SERVICE_NAME=order-service
      - SERVICE_PORT=3000
    depends_on:
      - consul
      - order-db

  api-gateway:
    build: ./api-gateway
    ports:
      - "8080:8080"
    environment:
      - CONSUL_HOST=consul
    depends_on:
      - consul
      - user-service
      - product-service
      - order-service

  user-db:
    image: postgres:15
    environment:
      POSTGRES_DB: userdb
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
    volumes:
      - user_db_data:/var/lib/postgresql/data

  product-db:
    image: postgres:15
    environment:
      POSTGRES_DB: productdb
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
    volumes:
      - product_db_data:/var/lib/postgresql/data

  order-db:
    image: postgres:15
    environment:
      POSTGRES_DB: orderdb
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
    volumes:
      - order_db_data:/var/lib/postgresql/data

volumes:
  user_db_data:
  product_db_data:
  order_db_data:
```

### CI/CD Pipeline Integration

#### GitLab CI with Docker
```yaml
# .gitlab-ci.yml
stages:
  - test
  - build
  - security
  - deploy

variables:
  DOCKER_DRIVER: overlay2
  DOCKER_TLS_CERTDIR: "/certs"
  REGISTRY: registry.gitlab.com
  IMAGE_NAME: $CI_PROJECT_PATH

services:
  - docker:dind

before_script:
  - docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY

test:
  stage: test
  image: docker:latest
  script:
    - docker build --target development -t $IMAGE_NAME:test .
    - docker run --rm $IMAGE_NAME:test pytest tests/
  only:
    - merge_requests
    - main

build:
  stage: build
  image: docker:latest
  script:
    - docker build --target production -t $REGISTRY/$IMAGE_NAME:$CI_COMMIT_SHA .
    - docker build --target production -t $REGISTRY/$IMAGE_NAME:latest .
    - docker push $REGISTRY/$IMAGE_NAME:$CI_COMMIT_SHA
    - docker push $REGISTRY/$IMAGE_NAME:latest
  only:
    - main

security_scan:
  stage: security
  image: docker:latest
  script:
    - docker run --rm -v /var/run/docker.sock:/var/run/docker.sock 
      aquasec/trivy image $REGISTRY/$IMAGE_NAME:$CI_COMMIT_SHA
  allow_failure: true
  only:
    - main

deploy_staging:
  stage: deploy
  image: docker/compose:latest
  script:
    - docker-compose -f docker-compose.staging.yml pull
    - docker-compose -f docker-compose.staging.yml up -d
  environment:
    name: staging
    url: https://staging.example.com
  only:
    - main

deploy_production:
  stage: deploy
  image: docker/compose:latest
  script:
    - docker-compose -f docker-compose.production.yml pull
    - docker-compose -f docker-compose.production.yml up -d
  environment:
    name: production
    url: https://production.example.com
  when: manual
  only:
    - main
```

---

## 🔒 Security Best Practices

### Container Security

#### Secure Base Images
```dockerfile
# Use official, minimal base images
FROM python:3.11-slim

# Update packages and remove package manager cache
RUN apt-get update && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends \
        gcc \
        libc6-dev \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Set working directory
WORKDIR /app

# Copy and install dependencies as root
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code and change ownership
COPY --chown=appuser:appuser . .

# Switch to non-root user
USER appuser

# Use COPY instead of ADD
COPY config.json /app/config.json

# Avoid running as root
# Don't use: USER root
# Don't use: RUN chmod 777 /app
```

#### Security Scanning
```bash
# Scan images for vulnerabilities
docker run --rm -v /var/run/docker.sock:/var/run/docker.sock \
    aquasec/trivy image myapp:latest

# Scan with Snyk
docker run --rm -it \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v $(pwd):/app \
    snyk/snyk:docker test myapp:latest

# Scan with Clair
docker run -d --name clair-db postgres:latest
docker run -d --name clair --link clair-db:postgres \
    quay.io/coreos/clair:latest
```

#### Runtime Security
```yaml
# Docker Compose security configurations
version: '3.8'

services:
  app:
    image: myapp:latest
    security_opt:
      - no-new-privileges:true
      - apparmor:docker-default
    cap_drop:
      - ALL
    cap_add:
      - NET_BIND_SERVICE
    read_only: true
    tmpfs:
      - /tmp
      - /var/run
    volumes:
      - ./data:/app/data:ro
    user: "1000:1000"
    ulimits:
      nproc: 65535
      nofile:
        soft: 65535
        hard: 65535
```

### Secrets Management

#### Docker Secrets (Swarm)
```yaml
# docker-compose.yml with secrets
version: '3.8'

services:
  web:
    image: myapp:latest
    secrets:
      - db_password
      - api_key
    environment:
      - DB_PASSWORD_FILE=/run/secrets/db_password
      - API_KEY_FILE=/run/secrets/api_key

secrets:
  db_password:
    external: true
  api_key:
    external: true
```

```bash
# Create secrets in Swarm
echo "my_secure_password" | docker secret create db_password -
echo "my_api_key" | docker secret create api_key -

# Deploy stack with secrets
docker stack deploy -c docker-compose.yml myapp
```

#### External Secrets Integration
```yaml
# Using external secrets operator
apiVersion: external-secrets.io/v1beta1
kind: SecretStore
metadata:
  name: vault-secret-store
spec:
  provider:
    vault:
      server: "https://vault.example.com"
      path: "secret"
      version: "v2"
      auth:
        kubernetes:
          mountPath: "kubernetes"
          role: "myapp"
---
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata:
  name: app-secrets
spec:
  secretStoreRef:
    name: vault-secret-store
    kind: SecretStore
  target:
    name: app-secrets
    creationPolicy: Owner
  data:
  - secretKey: database-password
    remoteRef:
      key: database
      property: password
```

### Network Security

#### Network Isolation
```bash
# Create isolated networks
docker network create --internal backend-network
docker network create frontend-network

# Run containers in isolated networks
docker run -d --name db --network backend-network postgres
docker run -d --name app --network backend-network --network frontend-network myapp
docker run -d --name proxy --network frontend-network nginx
```

#### TLS/SSL Configuration
```yaml
# nginx.conf for TLS termination
server {
    listen 443 ssl http2;
    server_name example.com;

    ssl_certificate /etc/nginx/ssl/cert.pem;
    ssl_certificate_key /etc/nginx/ssl/key.pem;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers ECDHE-RSA-AES256-GCM-SHA512:DHE-
    location / {
        proxy_pass http://app:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

---

## 📊 Monitoring & Observability

### Container Metrics

#### Prometheus Configuration
```yaml
# docker-compose.monitoring.yml
version:'3.8'

services :
  prometheus:
    image: prom/prometheus:latest
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
      - prometheus_data:/prometheus
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'
      - '--storage.tsdb.path=/prometheus'
      - '--web.console.libraries=/etc/prometheus/console_libraries'
      - '--web.console.templates=/etc/prometheus/consoles'

  grafana:
    image: grafana/grafana:latest
    ports:
      - "3000:3000"
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=admin
    volumes:
      - grafana_data:/var/lib/grafana
      - ./grafana/dashboards:/etc/grafana/provisioning/dashboards
      - ./grafana/datasources:/etc/grafana/provisioning/datasources

  node-exporter:
    image: prom/node-exporter:latest
    ports:
      - "9100:9100"
    volumes:
      - /proc:/host/proc:ro
      - /sys:/host/sys:ro
      - /:/rootfs:ro
    command:
      - '--path.procfs=/host/proc'
      - '--path.rootfs=/rootfs'
      - '--path.sysfs=/host/sys'
      - '--collector.filesystem.mount-points-exclude=^/(sys|proc|dev|host|etc)($$|/)'

  cadvisor:
    image: gcr.io/cadvisor/cadvisor:latest
    ports:
      - "8080:8080"
    volumes:
      - /:/rootfs:ro
      - /var/run:/var/run:ro
      - /sys:/sys:ro
      - /var/lib/docker/:/var/lib/docker:ro
      - /dev/disk/:/dev/disk:ro
    privileged: true
    devices:
     - /dev/kmsg

volumes:
  prometheus_data:
  grafana_data:
```

#### Prometheus Configuration File
```yaml
# prometheus.yml
global:
  scrape_interval: 15s
  evaluation_interval: 15s

rule_files:
  - "alert_rules.yml"

scrape_configs:
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']

  - job_name: 'node-exporter'
    static_configs:
      - targets: ['node-exporter:9100']

  - job_name: 'cadvisor'
    static_configs:
      - targets: ['cadvisor:8080']

  - job_name: 'docker-containers'
    docker_sd_configs:
      - host: unix:///var/run/docker.sock
        refresh_interval: 5s
    relabel_configs:
      - source_labels: [__meta_docker_container_name]
        target_label: container_name
      - source_labels: [__meta_docker_container_id]
        target_label: container_id

alerting:
  alertmanagers:
    - static_configs:
        - targets:
          - alertmanager:9093
```

### Centralized Logging

#### ELK Stack Configuration
```yaml
# docker-compose.logging.yml
version: '3.8'

services:
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:8.5.0
    environment:
      - discovery.type=single-node
      - "ES_JAVA_OPTS=-Xms512m -Xmx512m"
      - xpack.security.enabled=false
    ports:
      - "9200:9200"
    volumes:
     elasticsearch_data:/usr/share/elasticsearch/data

  logstash:
    image# 🐳 Docker Documentation Hub

[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com/)
[![Documentation](https://img.shields.io/badge/Documentation-1f425f.svg?style=for-the-badge)](https://github.com/yourusername/docker-docs)
[![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg?style=for-the-badge)](CONTRIBUTING.md)