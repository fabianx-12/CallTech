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
- **Base de datos**: SQLAlchemy con SQLite
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

4. Ejecuta la aplicación:
```bash
python app.py
```

La aplicación estará disponible en `http://localhost:5000`

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
