# 🚀 Guía de Despliegue CallTech

## Opción A: Heroku (Recomendado - Gratuito)

### 1. Preparar el proyecto
```bash
# Instalar Heroku CLI desde: https://devcenter.heroku.com/articles/heroku-cli
# Verificar instalación
heroku --version
```

### 2. Inicializar Git y Heroku
```bash
# Inicializar repositorio Git
git init
git add .
git commit -m "Initial commit - CallTech"

# Crear aplicación en Heroku
heroku create calltech-agenda
# O con nombre personalizado:
heroku create tu-nombre-calltech

# Configurar variables de entorno
heroku config:set SECRET_KEY="calltech-production-key-2024"
heroku config:set DEBUG="False"
```

### 3. Desplegar
```bash
# Subir código a Heroku
git push heroku main

# Abrir aplicación
heroku open
```

### 4. Tu URL será:
```
https://calltech-agenda.herokuapp.com
```

---

## Opción B: Railway (Alternativa Gratuita)

### 1. Conectar con GitHub
- Ve a [railway.app](https://railway.app)
- Conecta tu cuenta de GitHub
- Sube tu código a un repositorio de GitHub

### 2. Desplegar
- Selecciona "Deploy from GitHub repo"
- Elige tu repositorio CallTech
- Railway detectará automáticamente que es una app Flask

### 3. Tu URL será:
```
https://calltech-production.up.railway.app
```

---

## Opción C: Render (Otra Alternativa)

### 1. Crear cuenta en Render
- Ve a [render.com](https://render.com)
- Conecta tu GitHub

### 2. Configurar Web Service
- Selecciona tu repositorio
- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn app:app`

### 3. Tu URL será:
```
https://calltech.onrender.com
```

---

## Opción D: PythonAnywhere (Hosting Python)

### 1. Crear cuenta gratuita
- Ve a [pythonanywhere.com](https://pythonanywhere.com)
- Crea cuenta gratuita

### 2. Subir archivos
- Usa el file manager para subir tu proyecto
- O clona desde GitHub

### 3. Configurar Web App
- Crea nueva Web App
- Selecciona Flask
- Configura el path a tu app.py

### 4. Tu URL será:
```
https://tuusuario.pythonanywhere.com
```

---

## 🎯 Recomendación: Heroku

**Heroku es la opción más fácil y confiable:**

1. **Comando rápido:**
```bash
# Todo en uno
git init && git add . && git commit -m "CallTech" && heroku create calltech-agenda && git push heroku main && heroku open
```

2. **Ventajas:**
   - ✅ Despliegue automático
   - ✅ HTTPS incluido
   - ✅ Dominio personalizable
   - ✅ Escalable
   - ✅ Base de datos incluida

3. **Tu CallTech estará en:**
```
https://calltech-agenda.herokuapp.com
```

---

## 🔧 Configuración de Dominio Personalizado

### Para tener http://calltech.com:

1. **Comprar dominio** (GoDaddy, Namecheap, etc.)
2. **En Heroku:**
```bash
heroku domains:add calltech.com
heroku domains:add www.calltech.com
```
3. **Configurar DNS** en tu proveedor de dominio:
```
CNAME www calltech-agenda.herokuapp.com
ALIAS @ calltech-agenda.herokuapp.com
```

---

## 📱 Resultado Final

Una vez desplegado, tendrás:
- ✅ **URL pública accesible desde cualquier dispositivo**
- ✅ **Certificado SSL (HTTPS) automático**
- ✅ **Base de datos persistente**
- ✅ **Todas las funcionalidades de CallTech**

¡Tu sistema de agenda de contactos estará disponible 24/7 en internet!
