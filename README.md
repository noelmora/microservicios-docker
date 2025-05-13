# Microservicios con Docker


**Dos microservicios en Flask, cada uno dentro de su contenedor Docker, con Docker Compose.**


## 📝 Descripción

Este repositorio contiene dos microservicios escritos en Python (Flask):

* **servicio-usuario**: API REST que expone datos de usuarios.
* **servicio-pedidos**: API REST que consume `servicio-usuario` para enriquecer la información de pedidos.

Ambos servicios se ejecutan en contenedores Docker separados y se comunican internamente mediante una red creada por Docker Compose.

---


## ⚙️ Requisitos

* [Docker Desktop](https://www.docker.com/products/docker-desktop) (versión 20.10+)
* Docker Compose (integrado en la CLI `docker compose`)

---

## 🚀 Instalación y ejecución

1. Clona el repositorio:

   ```bash
   git clone https://github.com/tu-usuario/microservicios-docker.git
   cd microservicios-docker
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


## Imagenes
![image](https://github.com/user-attachments/assets/955439e1-995f-4efd-9c47-74361adc4d46)
![image](https://github.com/user-attachments/assets/f59bbc1c-df3d-435f-b9b6-37b9fa9013bb)






