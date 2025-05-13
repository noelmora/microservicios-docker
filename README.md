# Microservicios con Docker

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) [![Docker Compose](https://img.shields.io/badge/docker--compose%20v3.8-blue.svg)](https://docs.docker.com/compose/)

**Una demostración de dos microservicios en Flask, cada uno dentro de su contenedor Docker, orquestados con Docker Compose.**

---

## 📋 Tabla de Contenidos

1. [Descripción](#descripción)
2. [Estructura del proyecto](#estructura-del-proyecto)
3. [Requisitos](#requisitos)
4. [Instalación y ejecución](#instalación-y-ejecución)
5. [Uso y endpoints](#uso-y-endpoints)
6. [Buenas prácticas](#buenas-prácticas)
7. [Contribuir](#contribuir)
8. [Licencia](#licencia)

---

## 📝 Descripción

Este repositorio contiene dos microservicios escritos en Python (Flask):

* **servicio-usuario**: API REST que expone datos de usuarios.
* **servicio-pedidos**: API REST que consume `servicio-usuario` para enriquecer la información de pedidos.

Ambos servicios se ejecutan en contenedores Docker separados y se comunican internamente mediante una red creada por Docker Compose.

---

## 🗂 Estructura del proyecto

```bash
docker-microservicios/
├── servicio-usuario/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── servicio-pedidos/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
└── docker-compose.yml
```

---

## ⚙️ Requisitos

* [Docker Desktop](https://www.docker.com/products/docker-desktop) (versión 20.10+)
* Docker Compose (integrado en la CLI `docker compose`)

---

## 🚀 Instalación y ejecución

1. Clona el repositorio:

   ```bash
   git clone https://github.com/tu-usuario/docker-microservicios.git
   cd docker-microservicios
   ```
2. Asegúrate de tener Docker Desktop en modo Linux Containers.
3. Construye y levanta los servicios:

   ```bash
   docker compose up --build
   ```
4. Verifica que estén corriendo:

   ```bash
   docker ps
   ```

---

## 🎯 Uso y endpoints

### Servicio de Usuarios

* **Puerto**: `5000`
* **Endpoint**:

  * `GET /usuarios` → Devuelve una lista de usuarios.

```bash
curl http://localhost:5000/usuarios
```

### Servicio de Pedidos

* **Puerto**: `5001`
* **Endpoint**:

  * `GET /pedidos` → Devuelve una lista de pedidos con datos de usuarios.

```bash
curl http://localhost:5001/pedidos
```

---

## 🛠️ Buenas prácticas

* En producción, reemplaza el servidor de desarrollo de Flask por un WSGI (Gunicorn, uWSGI).
* Utiliza variables de entorno para configuración (puertos, URLs, credenciales).
* Implementa un contenedor de base de datos (PostgreSQL, MongoDB) para persistencia.
* Agrega un API Gateway (Traefik, Kong) para enrutamiento y balanceo de carga.
* Configura pruebas automatizadas y CI/CD con GitHub Actions.

---

## 🤝 Contribuir

¡Las contribuciones son bienvenidas!

1. Haz un *fork* del proyecto.
2. Crea una rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz *commit* (`git commit -m 'Agrega nueva funcionalidad'`).
4. Haz *push* a la rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un *Pull Request*.

Lee [CONTRIBUTING.md](CONTRIBUTING.md) para más detalles.

---

## 📄 Licencia

Este proyecto está bajo la licencia **MIT**. Consulta el archivo [LICENSE](LICENSE) para más información.

---

© 2025 Tu Nombre o Tu Organización
