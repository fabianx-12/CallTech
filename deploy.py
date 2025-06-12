"""
Script de despliegue para CallTech
Configura la aplicación para producción y genera un link accesible
"""

import os
import subprocess
import sys
from flask import Flask
from app import app

def create_production_config():
    """Crear configuración para producción"""
    config_content = """
# Configuración de producción para CallTech
import os

class ProductionConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'calltech-production-key-2024'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///calltech_production.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
    
    # Configuración para servidor web
    HOST = '0.0.0.0'
    PORT = int(os.environ.get('PORT', 8080))
"""
    
    with open('config.py', 'w') as f:
        f.write(config_content)
    
    print("✅ Configuración de producción creada")

def create_wsgi_file():
    """Crear archivo WSGI para servidores de producción"""
    wsgi_content = """
from app import app

if __name__ == "__main__":
    app.run()
"""
    
    with open('wsgi.py', 'w') as f:
        f.write(wsgi_content)
    
    print("✅ Archivo WSGI creado")

def create_dockerfile():
    """Crear Dockerfile para contenedorización"""
    dockerfile_content = """
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["python", "app.py"]
"""
    
    with open('Dockerfile', 'w') as f:
        f.write(dockerfile_content)
    
    print("✅ Dockerfile creado")

def create_deployment_script():
    """Crear script de despliegue automático"""
    script_content = """#!/bin/bash

# Script de despliegue para CallTech
echo "🚀 Iniciando despliegue de CallTech..."

# Instalar dependencias
echo "📦 Instalando dependencias..."
pip install -r requirements.txt

# Crear base de datos
echo "🗄️ Configurando base de datos..."
python -c "from app import create_tables; create_tables()"

# Iniciar servidor
echo "🌐 Iniciando servidor..."
echo "CallTech estará disponible en: http://localhost:8080"
python app.py

echo "✅ CallTech desplegado exitosamente!"
"""
    
    with open('deploy.sh', 'w') as f:
        f.write(script_content)
    
    # Hacer el script ejecutable en sistemas Unix
    try:
        os.chmod('deploy.sh', 0o755)
    except:
        pass
    
    print("✅ Script de despliegue creado")

def create_readme():
    """Crear README con instrucciones de despliegue"""
    readme_content = """# CallTech - Sistema de Agenda de Contactos

## 🚀 Despliegue Rápido

### Opción 1: Ejecución Local
```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar aplicación
python app.py
```

### Opción 2: Script Automático
```bash
# En Windows
python deploy.py

# En Linux/Mac
chmod +x deploy.sh
./deploy.sh
```

### Opción 3: Docker
```bash
# Construir imagen
docker build -t calltech .

# Ejecutar contenedor
docker run -p 8080:8080 calltech
```

## 🌐 Acceso

Una vez iniciado, CallTech estará disponible en:
- **Local**: http://localhost:8080
- **Red local**: http://[tu-ip]:8080

## 📱 Características

- ✅ Gestión completa de contactos (CRUD)
- ✅ Categorización (Familia, Amigos, Trabajo, etc.)
- ✅ Sistema anti-duplicación
- ✅ Compartir perfil personal via QR/Link
- ✅ Diseño moderno y responsivo
- ✅ Animaciones fluidas
- ✅ Búsqueda avanzada

## 🔧 Configuración

### Variables de Entorno
```bash
export SECRET_KEY="tu-clave-secreta"
export DATABASE_URL="sqlite:///calltech.db"
export PORT=8080
```

### Base de Datos
La aplicación crea automáticamente la base de datos SQLite al iniciar.

## 📞 Soporte

Para soporte técnico, contacta al desarrollador.

---
© 2024 CallTech. Sistema de gestión de contactos moderno y eficiente.
"""
    
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print("✅ README.md creado")

def update_app_for_production():
    """Actualizar app.py para producción"""
    # Leer el contenido actual
    with open('app.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Reemplazar la línea final para producción
    content = content.replace(
        "if __name__ == '__main__':\n    app.run(debug=True, host='0.0.0.0', port=5000)",
        """if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 8080))
    debug = os.environ.get('DEBUG', 'False').lower() == 'true'
    app.run(debug=debug, host='0.0.0.0', port=port)"""
    )
    
    with open('app.py', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ App configurada para producción")

def get_local_ip():
    """Obtener IP local para acceso en red"""
    try:
        import socket
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "localhost"

def main():
    """Función principal de despliegue"""
    print("🎯 CallTech - Configuración de Despliegue")
    print("=" * 50)
    
    # Crear archivos de configuración
    create_production_config()
    create_wsgi_file()
    create_dockerfile()
    create_deployment_script()
    create_readme()
    update_app_for_production()
    
    # Obtener IP local
    local_ip = get_local_ip()
    
    print("\n🌐 URLs de Acceso:")
    print(f"   Local: http://localhost:8080")
    print(f"   Red:   http://{local_ip}:8080")
    
    print("\n📋 Próximos pasos:")
    print("1. Ejecutar: python app.py")
    print("2. Abrir navegador en http://localhost:8080")
    print("3. ¡Disfrutar CallTech!")
    
    print("\n✅ Configuración completada exitosamente!")

if __name__ == "__main__":
    main()
