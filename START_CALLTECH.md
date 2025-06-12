# 🚀 Iniciar CallTech Localmente

## Opción 1: Inicio Rápido

### Comando Simple:
```bash
python app.py
```

### Tu CallTech estará disponible en:
```
http://localhost:5000
```

---

## Opción 2: Usando el Script de Despliegue

### Ejecutar:
```bash
python deploy.py
```

### Luego:
```bash
python app.py
```

### Tu CallTech estará disponible en:
```
http://localhost:8080
```

---

## 🌐 Acceso desde Otros Dispositivos en tu Red

### Para acceder desde tu teléfono o tablet:

1. **Encuentra tu IP local:**
   - Windows: `ipconfig` (busca IPv4)
   - Mac/Linux: `ifconfig` (busca inet)

2. **Ejemplo de IP:** `192.168.1.100`

3. **Accede desde cualquier dispositivo en tu red:**
```
http://192.168.1.100:5000
```

---

## 📱 Instrucciones Paso a Paso

### 1. Abrir Terminal/CMD
- Windows: Presiona `Win + R`, escribe `cmd`, Enter
- Mac: Presiona `Cmd + Space`, escribe "Terminal"
- O usa la terminal integrada de VS Code

### 2. Navegar a la carpeta del proyecto
```bash
cd c:\Users\Fabia\Documents\curso-git
```

### 3. Instalar dependencias (solo la primera vez)
```bash
pip install -r requirements.txt
```

### 4. Iniciar CallTech
```bash
python app.py
```

### 5. Abrir en navegador
Ve a: `http://localhost:5000`

---

## 🔧 Configuración Avanzada

### Para cambiar el puerto:
Edita `app.py` y cambia:
```python
app.run(debug=debug, host='0.0.0.0', port=5000)
```

Por ejemplo, para puerto 3000:
```python
app.run(debug=debug, host='0.0.0.0', port=3000)
```

### Para acceso solo local (más seguro):
```python
app.run(debug=debug, host='127.0.0.1', port=5000)
```

---

## 🎯 Acceso Rápido

### Crear acceso directo:

1. **Crear archivo `iniciar_calltech.bat` (Windows):**
```batch
@echo off
cd /d "c:\Users\Fabia\Documents\curso-git"
python app.py
pause
```

2. **Crear archivo `iniciar_calltech.sh` (Mac/Linux):**
```bash
#!/bin/bash
cd "c:/Users/Fabia/Documents/curso-git"
python app.py
```

### Uso:
- Doble clic en el archivo
- CallTech se iniciará automáticamente

---

## 📊 Estado del Servidor

### Mientras CallTech esté ejecutándose verás:
```
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.1.100:5000
```

### Para detener el servidor:
Presiona `Ctrl + C` en la terminal

---

## 🌟 Características Disponibles

Una vez iniciado, tendrás acceso a:

- ✅ **Gestión de Contactos:** Agregar, editar, eliminar
- ✅ **Categorización:** Familia, Amigos, Trabajo, etc.
- ✅ **Anti-duplicación:** Evita contactos repetidos
- ✅ **Compartir Perfil:** QR y link personalizado
- ✅ **Búsqueda:** Filtrar por nombre, teléfono, email
- ✅ **Diseño Moderno:** Animaciones y colores CallTech
- ✅ **Responsive:** Funciona en móvil y desktop

---

## 🔗 URLs Principales

Una vez iniciado:

- **Inicio:** http://localhost:5000
- **Agregar Contacto:** http://localhost:5000/add
- **Mi Perfil:** http://localhost:5000/my-profile
- **Compartir:** http://localhost:5000/share-profile

---

## ⚠️ Notas Importantes

1. **Mantén la terminal abierta** mientras uses CallTech
2. **Los datos se guardan** en `calltech.db` automáticamente
3. **Para acceso desde otros dispositivos** usa tu IP local
4. **Para detener** presiona `Ctrl + C` en la terminal

¡Tu sistema CallTech está listo para usar localmente!
