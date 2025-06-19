# CallTech - Sistema de Gestión de Contactos

---

## Tabla de Contenidos

1. [Introducción](#1-introducción)
2. [Características principales](#2-características-principales)
3. [Instalación](#3-instalación)
4. [Uso](#4-uso)
5. [Capturas de pantalla](#5-capturas-de-pantalla)
6. [Solución de problemas](#6-solución-de-problemas)
7. [Pruebas y Estructura del proyecto](#7-pruebas-y-estructura-del-proyecto)
8. [Licencia, Créditos y Roadmap](#8-licencia-créditos-y-roadmap)
9. [Contribuciones y FAQ](#9-contribuciones-y-faq)

---

## 1. Introducción

CallTech es una aplicación web moderna y eficiente diseñada para la gestión integral de contactos profesionales y personales. Desarrollada con tecnologías web actuales, ofrece una experiencia de usuario intuitiva y funcionalidades avanzadas para organizar, categorizar y compartir información de contacto.

### ¿Qué es CallTech?

CallTech es más que una simple agenda de contactos. Es una solución completa que permite:
- Gestionar contactos de manera eficiente
- Categorizar información por tipo de relación
- Buscar y filtrar contactos inteligentemente
- Compartir perfiles mediante códigos QR
- Mantener un perfil personal actualizable

### ¿Para quién está diseñado?

- **Profesionales** que necesitan organizar contactos de trabajo
- **Empresarios** que manejan múltiples tipos de contactos
- **Estudiantes** que quieren organizar sus contactos académicos
- **Cualquier persona** que busque una solución moderna para gestionar contactos

### Tecnologías Utilizadas

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Base de Datos**: SQLAlchemy con SQLite
- **Funcionalidades Especiales**: Generación de códigos QR, validación en tiempo real

---

## 2. Características principales

### 🏠 Gestión Completa de Contactos
- **Crear contactos**: Formulario intuitivo con validación en tiempo real
- **Visualizar contactos**: Lista organizada con información clave
- **Editar contactos**: Modificación rápida de información existente
- **Eliminar contactos**: Eliminación segura con confirmación

### 🏷️ Sistema de Categorización
- **Categorías predefinidas**: Familia, Amigos, Trabajo, Compañeros, Clientes, Otros
- **Colores distintivos**: Cada categoría tiene un color único para fácil identificación
- **Filtrado por categoría**: Visualización rápida de contactos por tipo
- **Estadísticas**: Contadores automáticos por categoría

### 🔍 Búsqueda Avanzada
- **Búsqueda en tiempo real**: Resultados instantáneos mientras escribes
- **Múltiples campos**: Busca por nombre, teléfono, email o empresa
- **Filtros combinados**: Combina búsqueda con filtros de categoría
- **Resultados destacados**: Resaltado de términos de búsqueda

### 👤 Perfil Personal
- **Información personalizable**: Nombre, teléfono, email, empresa, biografía
- **Actualización fácil**: Formulario simple para modificar datos
- **Visualización atractiva**: Diseño moderno para mostrar información

### 📤 Compartir Perfil
- **Códigos QR**: Generación automática de códigos QR para compartir
- **Enlaces directos**: URLs únicas para acceso rápido
- **Compatibilidad móvil**: Escaneo desde cualquier dispositivo

### 🎨 Interfaz Moderna
- **Diseño responsive**: Adaptable a cualquier tamaño de pantalla
- **Tema oscuro/claro**: Cambio automático según preferencias del sistema
- **Animaciones suaves**: Transiciones elegantes entre estados
- **Iconografía intuitiva**: Iconos claros para cada acción

### 🛡️ Validación y Seguridad
- **Validación de email**: Verificación de formato correcto
- **Detección de duplicados**: Prevención automática de contactos repetidos
- **Formateo de teléfonos**: Normalización automática de números
- **Validación de formularios**: Verificación en tiempo real

---

## 3. Instalación

### Requisitos del Sistema

#### Requisitos Mínimos
- **Sistema Operativo**: Windows 10, macOS 10.14, Ubuntu 18.04 o superior
- **Python**: Versión 3.8 o superior
- **RAM**: 512 MB disponibles
- **Espacio en disco**: 100 MB libres
- **Navegador**: Chrome 80+, Firefox 75+, Safari 13+, Edge 80+

#### Requisitos Recomendados
- **Python**: Versión 3.9 o superior
- **RAM**: 1 GB disponibles
- **Espacio en disco**: 500 MB libres

### Instalación Paso a Paso

#### 1. Preparación del Entorno

```bash
# Verificar versión de Python
python --version

# Si no tienes Python instalado, descárgalo desde python.org
```

#### 2. Clonar el Repositorio

```bash
# Clonar desde GitHub
git clone https://github.com/tu-usuario/calltech.git
cd calltech

# O descargar ZIP y extraer
```

#### 3. Crear Entorno Virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

#### 4. Instalar Dependencias

```bash
# Instalar todas las dependencias
pip install -r requirements.txt

# Verificar instalación
pip list
```

#### 5. Configurar Variables de Entorno

```bash
# Windows (CMD)
set FLASK_APP=app.py
set FLASK_ENV=development
set SECRET_KEY=tu-clave-secreta

# Windows (PowerShell)
$env:FLASK_APP="app.py"
$env:FLASK_ENV="development"

# macOS/Linux
export FLASK_APP=app.py
export FLASK_ENV=development
export SECRET_KEY=tu-clave-secreta
```

#### 6. Inicializar Base de Datos

```bash
# La base de datos se crea automáticamente al ejecutar la aplicación
python app.py
```

#### 7. Verificar Instalación

```bash
# Ejecutar la aplicación
python app.py

# Abrir navegador en http://localhost:5000
```

### Instalación con Docker (Opcional)

```bash
# Construir imagen
docker build -t calltech .

# Ejecutar contenedor
docker run -p 5000:5000 calltech
```

---

## 4. Uso

### Inicio Rápido

#### Primera Ejecución
1. **Ejecutar la aplicación**: `python app.py`
2. **Abrir navegador**: Ir a `http://localhost:5000`
3. **Explorar la interfaz**: Familiarizarse con la navegación
4. **Configurar perfil**: Ir a "Mi Perfil" y completar información

### Gestión de Contactos

#### Agregar un Nuevo Contacto
1. **Hacer clic en "➕ Agregar"** en la barra de navegación
2. **Completar el formulario**:
   - **Nombre**: Campo obligatorio
   - **Teléfono**: Formato automático
   - **Email**: Validación automática
   - **Empresa**: Campo opcional
   - **Categoría**: Seleccionar del menú desplegable
   - **Notas**: Información adicional
3. **Hacer clic en "Guardar Contacto"**
4. **Verificar**: El contacto aparecerá en la lista principal

#### Buscar Contactos
1. **Usar la barra de búsqueda** en la página principal
2. **Escribir términos de búsqueda**: Nombre, teléfono, email o empresa
3. **Ver resultados en tiempo real**
4. **Combinar con filtros de categoría** para búsquedas más específicas

#### Editar un Contacto
1. **Hacer clic en el contacto** desde la lista principal
2. **Hacer clic en "✏️ Editar"**
3. **Modificar la información** necesaria
4. **Guardar cambios**

#### Eliminar un Contacto
1. **Ir a la vista del contacto**
2. **Hacer clic en "🗑️ Eliminar"**
3. **Confirmar la eliminación**

### Filtrado por Categorías

#### Usar Filtros de Categoría
1. **Hacer clic en las pestañas de categoría** en la página principal:
   - **Todos**: Mostrar todos los contactos
   - **Familia**: Contactos familiares
   - **Amigos**: Contactos de amistad
   - **Trabajo**: Contactos profesionales
   - **Compañeros**: Colegas y compañeros
   - **Clientes**: Contactos comerciales
   - **Otros**: Contactos sin categoría específica

2. **Ver estadísticas**: Cada categoría muestra el número de contactos

### Gestión del Perfil Personal

#### Configurar Mi Perfil
1. **Hacer clic en "👤 Mi Perfil"**
2. **Completar información**:
   - **Nombre completo**
   - **Número de teléfono**
   - **Dirección de email**
   - **Empresa o organización**
   - **Biografía personal**
3. **Guardar cambios**

#### Compartir Perfil
1. **Ir a "📤 Compartir"**
2. **Ver código QR generado automáticamente**
3. **Copiar enlace directo** para compartir
4. **Escanear código QR** desde dispositivos móviles

### Funciones Avanzadas

#### Detección de Duplicados
- El sistema **detecta automáticamente** contactos similares
- **Muestra advertencias** antes de crear duplicados
- **Sugiere fusionar** contactos existentes

#### Validación de Datos
- **Emails**: Verificación de formato válido
- **Teléfonos**: Formateo automático
- **Campos obligatorios**: Validación en tiempo real

---

## 5. Capturas de pantalla

### Página Principal - Lista de Contactos
```
[Descripción: Vista principal mostrando la lista de contactos organizados por categorías, 
con barra de búsqueda y filtros. Interfaz limpia con tarjetas de contacto que muestran 
información esencial.]
```

### Formulario de Agregar Contacto
```
[Descripción: Formulario intuitivo con campos claramente etiquetados, validación en 
tiempo real y selección de categorías con colores distintivos.]
```

### Vista Detallada de Contacto
```
[Descripción: Página de detalle mostrando toda la información del contacto con opciones 
para editar y eliminar. Diseño centrado en la legibilidad.]
```

### Mi Perfil Personal
```
[Descripción: Página de perfil personal con formulario editable y vista previa de cómo 
se mostrará la información al compartir.]
```

### Compartir Perfil con Código QR
```
[Descripción: Página de compartir mostrando código QR generado automáticamente y enlace 
directo para compartir el perfil.]
```

### Búsqueda y Filtrado
```
[Descripción: Demostración de la funcionalidad de búsqueda en tiempo real con resultados 
destacados y filtros de categoría activos.]
```

### Interfaz Responsive - Vista Móvil
```
[Descripción: Adaptación de la interfaz para dispositivos móviles, mostrando navegación 
optimizada y diseño responsive.]
```

### Tema Oscuro
```
[Descripción: Vista de la aplicación en modo oscuro, mostrando la adaptación automática 
de colores y mantenimiento de la legibilidad.]
```

---

## 6. Solución de problemas

### Problemas Comunes de Instalación

#### Error: "Python no reconocido como comando"
**Síntomas**: El comando `python` no funciona en la terminal
**Solución**:
1. Verificar que Python esté instalado
2. Agregar Python al PATH del sistema
3. En Windows, usar `py` en lugar de `python`
4. Reinstalar Python marcando "Add to PATH"

#### Error: "pip no encontrado"
**Síntomas**: El comando `pip` no funciona
**Solución**:
```bash
# Verificar instalación de pip
python -m pip --version

# Instalar pip si no está disponible
python -m ensurepip --upgrade

# Usar python -m pip en lugar de pip
python -m pip install -r requirements.txt
```

#### Error: "Permiso denegado" al instalar dependencias
**Síntomas**: Error de permisos al ejecutar `pip install`
**Solución**:
```bash
# Usar entorno virtual (recomendado)
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# O instalar para usuario actual
pip install --user -r requirements.txt
```

### Problemas de Ejecución

#### Error: "Puerto 5000 ya en uso"
**Síntomas**: La aplicación no puede iniciarse
**Solución**:
```bash
# Cambiar puerto en app.py
app.run(port=5001)

# O terminar proceso que usa el puerto
# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# Linux/Mac
lsof -ti:5000 | xargs kill -9
```

#### Error: "Base de datos bloqueada"
**Síntomas**: Errores al guardar o leer datos
**Solución**:
1. Cerrar todas las instancias de la aplicación
2. Eliminar archivo `calltech.db` si existe
3. Reiniciar la aplicación para recrear la base de datos

#### Error: "Módulo no encontrado"
**Síntomas**: ImportError al ejecutar la aplicación
**Solución**:
```bash
# Verificar entorno virtual activado
which python  # Linux/Mac
where python  # Windows

# Reinstalar dependencias
pip install -r requirements.txt

# Verificar instalación
pip list
```

### Problemas de Funcionalidad

#### Los códigos QR no se generan
**Síntomas**: Error al acceder a "Compartir Perfil"
**Solución**:
```bash
# Verificar instalación de qrcode
pip install qrcode[pil]

# Verificar permisos de escritura en directorio static
```

#### La búsqueda no funciona
**Síntomas**: No aparecen resultados al buscar
**Solución**:
1. Verificar que JavaScript esté habilitado en el navegador
2. Comprobar la consola del navegador para errores
3. Limpiar caché del navegador

#### Problemas de visualización
**Síntomas**: Interfaz desorganizada o estilos faltantes
**Solución**:
1. Verificar conexión a internet (para Bootstrap CDN)
2. Limpiar caché del navegador
3. Verificar que los archivos CSS estén en `static/css/`

### Problemas de Rendimiento

#### La aplicación es lenta
**Solución**:
1. Verificar cantidad de contactos (límite recomendado: 1000)
2. Limpiar base de datos de registros innecesarios
3. Reiniciar la aplicación

#### Uso excesivo de memoria
**Solución**:
1. Cerrar pestañas innecesarias del navegador
2. Reiniciar la aplicación Flask
3. Verificar procesos en segundo plano

### Obtener Ayuda Adicional

#### Logs de Error
```bash
# Ejecutar con debug activado
export FLASK_ENV=development
python app.py

# Revisar logs en la terminal
```

#### Información del Sistema
```bash
# Información de Python
python --version
pip --version

# Información de dependencias
pip list

# Información del sistema
# Windows: systeminfo
# Linux: uname -a
# Mac: system_profiler SPSoftwareDataType
```

---

## 7. Pruebas y Estructura del proyecto

### Estructura del Proyecto

```
calltech/
├── app.py                  # Aplicación principal Flask
├── models.py              # Modelos de base de datos SQLAlchemy
├── utils.py               # Funciones utilitarias
├── requirements.txt       # Dependencias del proyecto
├── README.md             # Documentación principal
├── .gitignore            # Archivos ignorados por Git
├── static/               # Archivos estáticos
│   ├── css/
│   │   └── style.css     # Estilos principales
│   ├── js/
│   │   └── main.js       # JavaScript principal
│   └── images/           # Imágenes y recursos
├── templates/            # Plantillas HTML Jinja2
│   ├── base.html         # Plantilla base
│   ├── index.html        # Página principal
│   ├── add_contact.html  # Formulario agregar contacto
│   ├── edit_contact.html # Formulario editar contacto
│   ├── view_contact.html # Vista detalle contacto
│   ├── my_profile.html   # Página mi perfil
│   ├── share_profile.html# Página compartir perfil
│   └── about.html        # Página quienes somos
└── instance/             # Datos de instancia (ignorado en Git)
    └── calltech.db       # Base de datos SQLite
```

### Descripción de Archivos Principales

#### `app.py`
- **Función**: Aplicación principal Flask
- **Contenido**: 
  - Configuración de la aplicación
  - Definición de rutas
  - Manejo de formularios
  - Lógica de negocio principal

#### `models.py`
- **Función**: Definición de modelos de datos
- **Contenido**:
  - Modelo `Contact`: Estructura de contactos
  - Modelo `Category`: Categorías de contactos
  - Modelo `UserProfile`: Perfil del usuario
  - Relaciones entre modelos

#### `utils.py`
- **Función**: Funciones auxiliares
- **Contenido**:
  - Generación de códigos QR
  - Validación de emails
  - Formateo de teléfonos
  - Detección de duplicados

### Pruebas del Sistema

#### Pruebas Manuales Realizadas

**1. Pruebas de Funcionalidad Básica**
- ✅ Crear contacto nuevo
- ✅ Editar contacto existente
- ✅ Eliminar contacto
- ✅ Visualizar lista de contactos
- ✅ Búsqueda por diferentes campos
- ✅ Filtrado por categorías

**2. Pruebas de Validación**
- ✅ Validación de email inválido
- ✅ Campos obligatorios vacíos
- ✅ Detección de contactos duplicados
- ✅ Formateo automático de teléfonos

**3. Pruebas de Interfaz**
- ✅ Navegación entre páginas
- ✅ Responsive design en móviles
- ✅ Tema oscuro/claro
- ✅ Animaciones y transiciones

**4. Pruebas de Perfil y Compartir**
- ✅ Actualización de perfil personal
- ✅ Generación de códigos QR
- ✅ Enlaces de compartir funcionales

#### Casos de Prueba Específicos

**Caso 1: Agregar Contacto Válido**
```
Entrada: Nombre="Juan Pérez", Email="juan@email.com", Categoría="Trabajo"
Resultado Esperado: Contacto creado exitosamente
Estado: ✅ PASÓ
```

**Caso 2: Email Inválido**
```
Entrada: Email="email-invalido"
Resultado Esperado: Error de validación mostrado
Estado: ✅ PASÓ
```

**Caso 3: Búsqueda Parcial**
```
Entrada: Búsqueda="Juan"
Resultado Esperado: Todos los contactos con "Juan" en cualquier campo
Estado: ✅ PASÓ
```

**Caso 4: Contacto Duplicado**
```
Entrada: Mismo nombre y teléfono de contacto existente
Resultado Esperado: Advertencia de duplicado
Estado: ✅ PASÓ
```

#### Pruebas de Rendimiento

**Carga de Contactos**
- ✅ 10 contactos: < 1 segundo
- ✅ 100 contactos: < 2 segundos
- ✅ 500 contactos: < 5 segundos

**Búsqueda en Tiempo Real**
- ✅ Respuesta instantánea con < 100 contactos
- ✅ Respuesta < 1 segundo con 500 contactos

#### Pruebas de Compatibilidad

**Navegadores Probados**
- ✅ Chrome 120+ (Windows, Mac, Linux)
- ✅ Firefox 115+ (Windows, Mac, Linux)
- ✅ Safari 16+ (Mac)
- ✅ Edge 120+ (Windows)

**Dispositivos Móviles**
- ✅ iPhone (Safari)
- ✅ Android (Chrome)
- ✅ Tablets (varios navegadores)

### Arquitectura del Sistema

#### Patrón MVC
- **Modelo**: `models.py` - Gestión de datos
- **Vista**: `templates/` - Presentación
- **Controlador**: `app.py` - Lógica de aplicación

#### Base de Datos
- **Motor**: SQLite (desarrollo), PostgreSQL (producción)
- **ORM**: SQLAlchemy
- **Migraciones**: Automáticas en primera ejecución

#### Frontend
- **Framework CSS**: Bootstrap 5
- **JavaScript**: Vanilla JS para interactividad
- **Iconos**: Emojis y símbolos Unicode

---

## 8. Licencia, Créditos y Roadmap

### Licencia

Este proyecto está licenciado bajo la **Licencia MIT**.

```
MIT License

Copyright (c) 2024 CallTech Team

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

### Créditos y Equipo de Desarrollo

#### Equipo Principal

**👑 Fabian Sneider Caceres Rincon - Product Owner**
- **Rol**: Definición de producto y requisitos
- **Responsabilidades**: 
  - Visión del producto
  - Gestión de stakeholders
  - Priorización de funcionalidades
- **Contacto**: 
  - 📞 3232886669
  - ✉️ Fabic7550@gmail.com

**📊 Yeinner Sebastian Sanchez Suarez - Scrum Master**
- **Rol**: Facilitación y gestión de procesos
- **Responsabilidades**:
  - Coordinación del equipo
  - Gestión de metodologías ágiles
  - Resolución de impedimentos
- **Contacto**:
  - 📞 3228906507
  - ✉️ yeinnersebastiansanchez@gmail.com

**💻 Adolf Junior Acuña Garcia - Developer**
- **Rol**: Desarrollo y implementación técnica
- **Responsabilidades**:
  - Arquitectura del sistema
  - Implementación de funcionalidades
  - Testing y debugging
- **Contacto**:
  - 📞 3217750510
  - ✉️ Garciaadolf47@gmail.com

#### Tecnologías y Herramientas Utilizadas

**Frameworks y Librerías**
- **Flask**: Framework web de Python
- **SQLAlchemy**: ORM para base de datos
- **Bootstrap**: Framework CSS
- **qrcode**: Generación de códigos QR

**Herramientas de Desarrollo**
- **Git**: Control de versiones
- **VS Code**: Editor de código
- **Python**: Lenguaje de programación principal

### Roadmap de Desarrollo

#### Versión Actual: 1.0.0
**Estado**: ✅ Completado
**Funcionalidades**:
- Gestión básica de contactos (CRUD)
- Categorización de contactos
- Búsqueda y filtrado
- Perfil personal y compartir
- Interfaz responsive

#### Versión 1.1.0 - Próxima Release
**Estado**: 🔄 En Planificación
**Fecha Estimada**: Q2 2024
**Funcionalidades Planificadas**:
- [ ] **Autenticación de usuarios**
  - Sistema de login/registro
  - Múltiples usuarios por instancia
  - Gestión de sesiones seguras

- [ ] **Importación/Exportación**
  - Importar desde CSV/vCard
  - Exportar contactos en múltiples formatos
  - Sincronización con Google Contacts

- [ ] **Mejoras de UI/UX**
  - Tema personalizable
  - Más opciones de categorización
  - Drag & drop para organización

#### Versión 1.2.0 - Release Futura
**Estado**: 📋 Backlog
**Fecha Estimada**: Q3 2024
**Funcionalidades Propuestas**:
- [ ] **API REST**
  - Endpoints para integración externa
  - Documentación con Swagger
  - Autenticación por tokens

- [ ] **Funcionalidades Avanzadas**
  - Historial de cambios
  - Backup automático
  - Notificaciones y recordatorios

- [ ] **Integración con Redes Sociales**
  - Importar contactos de LinkedIn
  - Sincronización con redes sociales
  - Actualización automática de información

#### Versión 2.0.0 - Visión a Largo Plazo
**Estado**: 💭 Conceptual
**Fecha Estimada**: Q1 2025
**Funcionalidades Visionarias**:
- [ ] **Aplicación Móvil Nativa**
  - App para iOS y Android
  - Sincronización en tiempo real
  - Funcionalidades offline

- [ ] **Inteligencia Artificial**
  - Sugerencias automáticas de categorización
  - Detección inteligente de duplicados
  - Análisis de patrones de contacto

- [ ] **Colaboración en Equipo**
  - Contactos compartidos en equipos
  - Permisos granulares
  - Comentarios y notas colaborativas

### Métricas y Objetivos

#### Objetivos de Calidad
- **Cobertura de Pruebas**: > 80%
- **Tiempo de Respuesta**: < 2 segundos
- **Compatibilidad**: 95% navegadores modernos
- **Accesibilidad**: Cumplimiento WCAG 2.1 AA

#### Métricas de Adopción (Objetivos)
- **Usuarios Activos**: 100+ en primer año
- **Satisfacción**: > 4.5/5 en encuestas
- **Retención**: > 70% usuarios mensuales

---

## 9. Contribuciones y FAQ

### Cómo Contribuir

#### Formas de Contribuir

**🐛 Reportar Bugs**
1. Verificar que el bug no esté ya reportado
2. Crear un issue detallado con:
   - Descripción del problema
   - Pasos para reproducir
   - Comportamiento esperado vs actual
   - Capturas de pantalla si aplica
   - Información del sistema

**💡 Sugerir Funcionalidades**
1. Revisar roadmap existente
2. Crear issue con etiqueta "enhancement"
3. Describir la funcionalidad propuesta
4. Justificar el valor agregado
5. Proponer implementación si es posible

**🔧 Contribuir Código**
1. Fork del repositorio
2. Crear rama para la funcionalidad: `git checkout -b feature/nueva-funcionalidad`
3. Implementar cambios siguiendo estándares
4. Escribir pruebas para nuevas funcionalidades
5. Commit con mensajes descriptivos
6. Push y crear Pull Request

#### Estándares de Código

**Python (Backend)**
```python
# Seguir PEP 8
# Usar docstrings para funciones
def validate_email(email):
    """
    Valida formato de email usando regex.
    
    Args:
        email (str): Email a validar
        
    Returns:
        bool: True si es válido, False si no
    """
    pass
```

**HTML/CSS (Frontend)**
```html
<!-- Usar indentación de 2 espacios -->
<!-- Comentarios descriptivos -->
<!-- Clases semánticas -->
<div class="contact-card">
  <h3 class="contact-name">{{ contact.name }}</h3>
</div>
```

**JavaScript**
```javascript
// Usar camelCase
// Comentarios para lógica compleja
// Funciones puras cuando sea posible
function formatPhoneNumber(phone) {
  // Formatear número de teléfono
  return phone.replace(/(\d{3})(\d{3})(\d{4})/, '($1) $2-$3');
}
```

#### Proceso de Review

1. **Revisión Automática**: CI/CD verifica estándares
2. **Revisión por Pares**: Al menos un maintainer revisa
3. **Testing**: Pruebas automáticas y manuales
4. **Merge**: Integración a rama principal

### FAQ - Preguntas Frecuentes

#### Instalación y Configuración

**P: ¿Puedo usar CallTech sin conexión a internet?**
R: Sí, CallTech funciona completamente offline una vez instalado. Solo necesitas internet para la instalación inicial y para cargar Bootstrap desde CDN (opcional).

**P: ¿En qué sistemas operativos funciona?**
R: CallTech es compatible con Windows, macOS y Linux. Solo necesitas Python 3.8+ instalado.

**P: ¿Puedo cambiar el puerto de la aplicación?**
