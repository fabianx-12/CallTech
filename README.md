# CallTech - Gestor de Contactos

Una aplicación web moderna para gestionar contactos con categorización, búsqueda avanzada y funcionalidades de compartir perfil mediante códigos QR.

## Características

- ✨ Gestión completa de contactos (CRUD)
- 🏷️ Categorización de contactos con colores personalizados
- 🔍 Búsqueda avanzada por nombre, teléfono, email o empresa
- 📱 Generación de códigos QR para compartir perfiles
- 👤 Perfil personal personalizable
- 📊 Estadísticas por categoría
- 🎨 Interfaz moderna y responsive
- 🔄 Detección automática de contactos duplicados

## Tecnologías

- **Backend**: Flask (Python)
- **Base de datos**: SQLAlchemy con PostgreSQL en producción
- **Frontend**: HTML5, CSS3, JavaScript
- **Estilos**: Bootstrap 5
- **QR Codes**: qrcode library
- **Servidor**: Gunicorn

## Instalación Local

1. Clona el repositorio:
```bash
git clone <url-del-repositorio>
cd calltech
```

2. Crea un entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instala las dependencias:
```bash
pip install -r requirements.txt
```

4. Configura las variables de entorno:
```bash
cp .env.example .env
# Edita .env con tus configuraciones
```

5. Ejecuta la aplicación:
```bash
python app.py
```

La aplicación estará disponible en `http://localhost:5000`

## Despliegue en Heroku

### Prerrequisitos
- Cuenta en [Heroku](https://heroku.com)
- [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) instalado
- Git configurado

### Pasos de despliegue

1. **Crear aplicación en Heroku:**
```bash
heroku create tu-app-calltech
```

2. **Agregar addon de PostgreSQL:**
```bash
heroku addons:create heroku-postgresql:mini
```

3. **Configurar variables de entorno:**
```bash
# Generar una clave secreta segura
heroku config:set SECRET_KEY=$(python -c 'import secrets; print(secrets.token_hex(32))')

# Configurar modo producción
heroku config:set DEBUG=False
```

4. **Desplegar la aplicación:**
```bash
git add .
git commit -m "Preparar para despliegue en Heroku"
git push heroku main
```

5. **Inicializar la base de datos:**
```bash
heroku run python -c "from app import create_tables; create_tables()"
```

6. **Abrir la aplicación:**
```bash
heroku open
```

### Variables de entorno requeridas en Heroku

| Variable | Descripción | Ejemplo |
|----------|-------------|---------|
| `SECRET_KEY` | Clave secreta para Flask | `abc123...` |
| `DATABASE_URL` | URL de PostgreSQL (automática) | `postgresql://...` |
| `DEBUG` | Modo debug (False en producción) | `False` |

### Comandos útiles de Heroku

```bash
# Ver logs de la aplicación
heroku logs --tail

# Ejecutar comandos en Heroku
heroku run python migrations.py

# Ver configuración
heroku config

# Reiniciar la aplicación
heroku restart
```

## Estructura del Proyecto

```
calltech/
├── app.py              # Aplicación principal Flask
├── models.py           # Modelos de base de datos
├── utils.py            # Funciones utilitarias
├── config.py           # Configuraciones
├── wsgi.py            # Punto de entrada WSGI
├── migrations.py       # Scripts de migración
├── requirements.txt    # Dependencias Python
├── runtime.txt        # Versión de Python para Heroku
├── Procfile           # Configuración de procesos Heroku
├── .env.example       # Ejemplo de variables de entorno
├── static/            # Archivos estáticos (CSS, JS, imágenes)
├── templates/         # Plantillas HTML
└── instance/          # Archivos de instancia (ignorados en git)
```

## Desarrollo

### Agregar nuevas funcionalidades

1. Modifica los modelos en `models.py` si es necesario
2. Actualiza las rutas en `app.py`
3. Crea/modifica plantillas en `templates/`
4. Actualiza estilos en `static/css/style.css`
5. Ejecuta migraciones si hay cambios en la BD

### Testing local con configuración de producción

```bash
# Configurar variables de entorno de producción
export DEBUG=False
export SECRET_KEY=tu-clave-secreta
export DATABASE_URL=postgresql://...

# Ejecutar con gunicorn
gunicorn app:app
```

## Solución de Problemas

### Error de base de datos en Heroku
```bash
# Reiniciar la base de datos
heroku pg:reset DATABASE_URL
heroku run python -c "from app import create_tables; create_tables()"
```

### Problemas con archivos estáticos
- Verifica que los archivos estén en la carpeta `static/`
- Asegúrate de que las rutas en las plantillas usen `url_for('static', filename='...')`

### Logs de error
```bash
# Ver logs detallados
heroku logs --tail --app tu-app-calltech
```

## Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Crea un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## Soporte

Si encuentras algún problema o tienes sugerencias, por favor crea un issue en el repositorio.
