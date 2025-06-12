# 📱 CallTech - Sistema de Gestión de Contactos

CallTech es una aplicación web moderna para gestionar contactos de manera eficiente, con características avanzadas de organización y compartición de perfiles.

## ✨ Características Principales

- 📋 **Gestión de Contactos**
  - Agregar, editar y eliminar contactos
  - Detección automática de duplicados
  - Notas y detalles por contacto
  - Búsqueda y filtrado avanzado

- 🎨 **Categorización Inteligente**
  - Categorías predefinidas: Familia, Amigos, Trabajo, etc.
  - Códigos de color para fácil identificación
  - Iconos distintivos por categoría

- 🔄 **Compartición de Perfil**
  - Generación de códigos QR
  - Enlaces compartibles
  - Perfil público personalizable

- 🎯 **Características Técnicas**
  - Interfaz responsive
  - Base de datos SQLite
  - API REST para operaciones AJAX
  - Validación de datos en tiempo real

## 🚀 Instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/tu-usuario/calltech.git
cd calltech
```

2. **Crear entorno virtual (recomendado)**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

4. **Iniciar la aplicación**
```bash
python app.py
```

La aplicación estará disponible en: `http://localhost:5000`

## 💻 Requisitos

- Python 3.8 o superior
- Dependencias principales:
  - Flask 2.3.3
  - SQLAlchemy 3.0.5
  - Pillow 10.0.0
  - qrcode 7.4.2

## 🌐 Despliegue

### Opción 1: Heroku (Recomendado)
```bash
heroku create calltech-agenda
git push heroku main
```

### Opción 2: Railway
- Conectar con GitHub
- Seleccionar repositorio
- Railway detectará automáticamente la configuración

### Opción 3: Render
- Crear Web Service
- Conectar repositorio
- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn app:app`

Para más detalles sobre el despliegue, consulta [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)

## 🎯 Uso

1. **Gestión de Contactos**
   - Agregar nuevo contacto: `/add`
   - Ver contacto: `/contact/<id>`
   - Editar contacto: `/edit/<id>`

2. **Perfil Personal**
   - Configurar perfil: `/my-profile`
   - Compartir perfil: `/share-profile`
   - Ver perfil público: `/profile/<code>`

3. **API Endpoints**
   - Lista de contactos: `/api/contacts`
   - Categorías: `/api/categories`
   - Verificar duplicados: `/api/check-duplicate`

## 🔧 Configuración

La configuración se realiza a través de variables de entorno o el archivo `config.py`:

- `SECRET_KEY`: Clave secreta para la aplicación
- `DEBUG`: Modo de depuración (True/False)
- `PORT`: Puerto para el servidor (default: 5000)

## 📚 Estructura del Proyecto

```
calltech/
├── app.py           # Aplicación principal
├── config.py        # Configuración
├── models.py        # Modelos de datos
├── utils.py         # Utilidades
├── static/          # Archivos estáticos
│   ├── css/
│   ├── js/
│   └── images/
└── templates/       # Plantillas HTML
```

## 🤝 Contribución

1. Fork del repositorio
2. Crear rama para feature: `git checkout -b feature/NuevaCaracteristica`
3. Commit cambios: `git commit -am 'Agregar nueva característica'`
4. Push a la rama: `git push origin feature/NuevaCaracteristica`
5. Crear Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## 🔗 Enlaces Útiles

- [Guía de Inicio](START_CALLTECH.md)
- [Guía de Despliegue](DEPLOYMENT_GUIDE.md)
- [Documentación de Flask](https://flask.palletsprojects.com/)

## 📞 Soporte

Para reportar problemas o solicitar nuevas características, por favor crear un issue en el repositorio.

---
Desarrollado con ❤️ usando Flask y SQLAlchemy
