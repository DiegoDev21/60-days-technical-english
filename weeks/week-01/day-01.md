# 📘 Day 01: To Be in Technical Environments

[<< Inicio / README](../../README.md) | [Day 02 >>](day-02.md)

---

## 📑 Tabla de Contenidos de la Lección
- [Introducción](#introducción)
- [📚 Vocabulario del Día](#-vocabulario-del-día)
- [Reglas Gramaticales: Verbo To Be](#reglas-gramaticales-verbo-to-be)
  - [1. Forma Afirmativa (Status & Health)](#1-forma-afirmativa-status--health)
  - [2. Forma Negativa (Errors & Blockers)](#2-forma-negativa-errors--blockers)
  - [3. Preguntas e Interrogación (Debugging)](#3-preguntas-e-interrogación-debugging)
- [Casos de Uso en Ingeniería de Software](#casos-de-uso-en-ingeniería-de-software)
- [💻 Ejercicios del Día 1](#-ejercicios-del-día-1)

---

## Introducción
En la escuela nos enseñan que el verbo **To Be** (Ser o Estar) sirve para decir "I am happy" o "The car is blue". Sin embargo, en el desarrollo de software, este verbo es tu herramienta principal para **reportar el estado de sistemas, notificar caídas de servidores y describir la arquitectura**.

En esta lección aprenderás a construir oraciones técnicas directas, claras y sin ambigüedades.

---

## 📚 Vocabulario del Día

| # | Palabra / Término | Tipo | Traducción | Ejemplo de Uso en Ingeniería |
| :-: | :--- | :--- | :--- | :--- |
| **1** | **Database** | Sustantivo | Base de datos | *The production database is slow.* |
| **2** | **Server** | Sustantivo | Servidor | *The web server is ready for traffic.* |
| **3** | **Down** | Adjetivo | Caído / Fuera de servicio | *The API gateway is down.* |
| **4** | **Available** | Adjetivo | Disponible | *The new microservice is available.* |
| **5** | **Issue** | Sustantivo | Problema / Incidencia | *There is an issue with the auth system.* |
| **6** | **Fix** | Sustantivo | Solución / Parche | *The hotfix is deployed and active.* |
| **7** | **Delay** | Sustantivo | Retraso / Demora | *There is a delay in data processing.* |

---

## Reglas Gramaticales: Verbo To Be

En tecnología casi nunca hablamos de nosotros mismos (`I am`), sino de **Sistemas** (`It is`) o **Componentes Múltiples** (`They are`).

### 1. Forma Afirmativa (Status & Health)
Usamos la forma afirmativa para confirmar que un entorno funciona o reportar su estado actual.

* **Singular (It -> is):** Aplica para un servidor, una API, una base de datos o un error.
  * `The database is offline.` (La base de datos está fuera de línea).
  * `The main server is stable.` (El servidor principal está estable).
* **Plural (They -> are):** Aplica para microservicios, nodos, registros (logs) o usuarios.
  * `The microservices are active.` (Los microservicios están activos).
  * `The logs are available in Kibana.` (Los registros están disponibles en Kibana).

### 2. Forma Negativa (Errors & Blockers)
Para indicar que algo NO está funcionando, agregamos **`not`** después del verbo. En Slack, se suele usar la contracción (`isn't` / `aren't`).

* `The API is not ready.` (La API no está lista).
* `The backup server isn't available.` (El servidor de respaldo no está disponible).
* `The tests aren't passing.` (Las pruebas no están pasando).

### 3. Preguntas e Interrogación (Debugging)
En chats corporativos o *Daily Stand-ups*, inviertes el orden poniendo el verbo al inicio para preguntar por el estado de un componente.

* `Is the database down?` (¿Está caída la base de datos?)
* `Are the servers online?` (¿Están en línea los servidores?)
* `Is the fix ready?` (¿Está lista la solución?)

---

## Casos de Uso en Ingeniería de Software

### A. Reporte de Incidentes (Status Page)
Cuando redactas un reporte de estado para los usuarios o *stakeholders*, debes ser claro y formal:
> *"The primary database **is** down, but the replica server **is** active. The engineers **are** aware of the issue."*

### B. Comunicación en Slack (Daily Stand-up)
Durante las reuniones diarias, usas el verbo *To Be* para describir tus bloqueos:
> *"My pull request **is** ready for review. However, the testing environment **isn't** available right now."*

---

## 💻 Ejercicios del Día 1

### Nivel 1: Reto interactivo en CLI
Abre tu terminal en Visual Studio Code y ejecuta el script interactivo para validar tu redacción y ganar los puntos del día:

```bash
python src/cli.py --day 1