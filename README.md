# CallTech - Sistema de Gestión de Contactos

Una aplicación web moderna y eficiente para gestionar contactos profesionales, con características avanzadas de categorización, búsqueda inteligente y compartición de perfiles mediante códigos QR.

## 🌟 Características Principales

- ✨ **Gestión Completa de Contactos**
  - Crear, ver, editar y eliminar contactos
  - Interfaz intuitiva y fácil de usar
  - Validación de datos en tiempo real
  - Prevención de duplicados inteligente

- 🏷️ **Categorización Avanzada**
  - Categorías predefinidas: Familia, Amigos, Trabajo, Compañeros, Clientes
  - Colores personalizados por categoría
  - Filtrado rápido por categorías
  - Estadísticas y métricas por categoría

- 🔍 **Búsqueda Inteligente**
  - Búsqueda en tiempo real
  - Filtros por nombre, teléfono, email o empresa
  - Resultados instantáneos
  - Historial de búsquedas recientes

- 📱 **Compartir Perfiles**
  - Generación de códigos QR únicos
  - Compartir perfil personal
  - Escaneo rápido desde dispositivos móviles
  - Enlaces directos para compartir

- 🎨 **Diseño Moderno**
  - Interfaz responsive para todos los dispositivos
  - Tema claro/oscuro automático
  - Animaciones suaves
  - Diseño minimalista y profesional

## 🛠️ Tecnologías Utilizadas

### Backend
- **Flask** (Python 3.8+)
  - Routing y manejo de peticiones
  - Blueprints para modularización
  - Gestión de sesiones
  - Validación de formularios

- **SQLAlchemy**
  - ORM para gestión de base de datos
  - Migraciones automáticas
  - Relaciones entre modelos
  - Consultas optimizadas

### Frontend
- **HTML5 & CSS3**
  - Semántica moderna
  - Flexbox y Grid
  - Variables CSS
  - Animaciones y transiciones

- **JavaScript**
  - Validación en tiempo real
  - Actualizaciones dinámicas
  - Gestión de eventos
  - AJAX para peticiones asíncronas

- **Bootstrap 5**
  - Sistema de grid responsive
  - Componentes predefinidos
  - Personalización de temas
  - Utilidades CSS

### Herramientas Adicionales
- **qrcode**: Generación de códigos QR
- **Gunicorn**: Servidor WSGI de producción
- **SQLite**: Base de datos ligera y portable

## 📦 Instalación y Configuración

### Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Git

### Pasos de Instalación

1. **Clonar el Repositorio**
```bash
git clone <url-del-repositorio>
cd calltech
```

2. **Crear y Activar Entorno Virtual**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. **Instalar Dependencias**
```bash
pip install -r requirements.txt
```

4. **Configurar Variables de Entorno**
```bash
# Windows
set FLASK_APP=app.py
set FLASK_ENV=development

# Linux/Mac
export FLASK_APP=app.py
export FLASK_ENV=development
```

5. **Inicializar Base de Datos**
```bash
flask db upgrade
```

6. **Ejecutar la Aplicación**
```bash
python app.py
```

## 📁 Estructura del Proyecto

```
calltech/
├── app.py              # Aplicación principal Flask
├── models.py           # Modelos de base de datos
├── forms.py            # Formularios y validación
├── utils.py            # Funciones utilitarias
├── config.py          # Configuraciones
├── wsgi.py            # Punto de entrada WSGI
├── migrations/        # Scripts de migración
├── static/           # Archivos estáticos
│   ├── css/         # Estilos CSS
│   ├── js/          # Scripts JavaScript
│   └── images/      # Imágenes y recursos
├── templates/        # Plantillas HTML
│   ├── base.html    # Plantilla base
│   ├── index.html   # Página principal
│   └── ...          # Otras plantillas
└── instance/        # Datos de instancia
```

## 👥 Equipo de Desarrollo

- **Fabian Sneider Caceres Rincon** - Product Owner
  - 📞 3232886669
  - ✉️ Fabic7550@gmail.com

- **Yeinner Sebastian Sanchez Suarez** - Scrum Master
  - 📞 3228906507
  - ✉️ yeinnersebastiansanchez@gmail.com

- **Adolf Junior Acuña Garcia** - Developer
  - 📞 3217750510
  - ✉️ Garciaadolf47@gmail.com

## 🤝 Contribuir

1. Fork el proyecto
2. Crea tu rama de feature (`git checkout -b feature/NuevaFuncionalidad`)
3. Commit tus cambios (`git commit -m 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/NuevaFuncionalidad`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo `LICENSE` para más detalles.

## 🆘 Soporte

Si encuentras algún problema o tienes sugerencias:
1. Revisa los issues existentes
2. Crea un nuevo issue detallando el problema
3. Incluye pasos para reproducir el error
4. Adjunta capturas de pantalla si es necesario

## 🔄 Actualizaciones Futuras

- [ ] Implementación de autenticación de usuarios
- [ ] Sincronización con servicios en la nube
- [ ] Exportación de contactos en múltiples formatos
- [ ] Integración con redes sociales
- [ ] API REST para desarrolladores
