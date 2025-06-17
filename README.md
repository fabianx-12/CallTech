# CallTech - Sistema de Gestión de Contactos

## 🔒 Mejoras de Seguridad Implementadas

### ✅ Correcciones Aplicadas (Fase 1)

#### **Seguridad Crítica**
- ✅ **SECRET_KEY segura**: Implementada generación automática con `secrets.token_hex(32)`
- ✅ **Protección CSRF**: Agregado Flask-WTF con CSRFProtect
- ✅ **Validación de datos**: Sanitización de inputs para prevenir XSS
- ✅ **Validación de email**: Usando `email-validator` para validación robusta
- ✅ **Validación de teléfono**: Usando `phonenumbers` para validación internacional
- ✅ **Manejo de excepciones**: Try-catch con rollback de transacciones
- ✅ **Límites de tamaño**: MAX_CONTENT_LENGTH configurado (16MB)

#### **Configuración Mejorada**
- ✅ **Configuración por entornos**: Separación dev/staging/prod
- ✅ **Variables de entorno**: Uso de .env para configuración sensible
- ✅ **Encoding corregido**: Problemas de caracteres UTF-8 solucionados
- ✅ **Puerto unificado**: Consistencia entre config.py y app.py (5000)

#### **Gestión de Recursos**
- ✅ **Memory leak corregido**: BytesIO cerrado correctamente en QR generation
- ✅ **Dependencias actualizadas**: Versiones específicas en requirements.txt

## 🚀 Instalación y Configuración

### Prerrequisitos
- Python 3.8+
- pip

### Instalación

1. **Clonar el repositorio**
```bash
git clone <repository-url>
cd CallTech
```

2. **Crear entorno virtual**
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

4. **Configurar variables de entorno**
```bash
cp .env.example .env
# Editar .env con tus configuraciones
```

5. **Ejecutar la aplicación**
```bash
# Desarrollo
python app.py

# Producción
gunicorn app:app
```

## 🔧 Configuración de Entorno

### Variables de Entorno (.env)

```env
FLASK_ENV=development
SECRET_KEY=tu-clave-secreta-super-segura-aqui
DATABASE_URL=sqlite:///calltech.db
PORT=5000
DEBUG=true
```

### Configuraciones por Entorno

- **Development**: Debug habilitado, base de datos local
- **Production**: Configuraciones de seguridad adicionales, cookies seguras
- **Testing**: Base de datos en memoria, CSRF deshabilitado

## 🛡️ Características de Seguridad

### Protección CSRF
Todos los formularios están protegidos contra ataques Cross-Site Request Forgery.

### Sanitización de Datos
- Escape HTML automático para prevenir XSS
- Validación de longitud de campos
- Validación de formato para emails y teléfonos

### Configuración Segura
- SECRET_KEY generada automáticamente
- Cookies seguras en producción
- Límites de tamaño de archivo

## 📊 Próximas Mejoras (Fase 2)

### Performance
- [ ] Índices en base de datos
- [ ] Paginación de contactos
- [ ] Optimización de consultas duplicadas

### Funcionalidad
- [ ] Rate limiting en APIs
- [ ] Logging estructurado
- [ ] Backup automático de datos

### Arquitectura
- [ ] Separación de blueprints
- [ ] Tests unitarios
- [ ] CI/CD pipeline

## 🐛 Problemas Conocidos

- La validación de teléfonos asume Colombia como país por defecto
- Sin paginación para listas grandes de contactos
- Falta implementar rate limiting

## 📝 Contribuir

1. Fork el proyecto
2. Crear una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.

## 👥 Desarrolladores

- Fabian Sneider Caceres Rincon
- Yeinner Sebastian Sanchez Suarez  
- Adolf junior Acuña Garcia
