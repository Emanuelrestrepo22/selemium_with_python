# 📌 Ejecutar el código en otro ordenador

Este documento explica paso a paso cómo ejecutar el código en otro ordenador que no tenga configurado el entorno.

---

## 📝 **Descripción del código**
Este script en Python utiliza Selenium para automatizar el llenado de un formulario de Microsoft Forms. 

### **¿Qué hace el código?**
1. Inicia un navegador Chrome con Selenium.
2. Abre un formulario de Microsoft Forms.
3. Rellena automáticamente los campos requeridos (nombre, teléfono y correo electrónico).
4. Selecciona opciones en botones de radio.
5. Envía el formulario y cierra el navegador.

**Propósito:** Automatizar el llenado de formularios para ahorrar tiempo en tareas repetitivas.

---

## ⚙️ **Pasos para ejecutar el código en otro ordenador**

### **1️⃣ Clonar el repositorio desde GitHub**
Abre una terminal en Visual Studio Code y ejecuta:

```bash
git clone https://github.com/tu-usuario/tu-repositorio.git
cd tu-repositorio
```

---

### **2️⃣ Crear y activar un entorno virtual**
Para evitar conflictos con otras instalaciones de Python, crea un entorno virtual:

```bash
python -m venv .venv  # Crear el entorno virtual
```

#### **Windows**
```bash
.venv\Scripts\activate
```

#### **Mac/Linux**
```bash
source .venv/bin/activate
```

---

### **3️⃣ Instalar las dependencias necesarias**
Ejecuta el siguiente comando para instalar Selenium y las demás dependencias:

```bash
pip install -r requirements.txt
```

Si el archivo `requirements.txt` no está en el repositorio, instala manualmente Selenium:
```bash
pip install selenium
```

---

### **4️⃣ Descargar y configurar WebDriver para Chrome**
El código usa Selenium, que necesita un WebDriver para Chrome. Sigue estos pasos:

1. **Descargar ChromeDriver**:
   - Ve a [ChromeDriver](https://sites.google.com/chromium.org/driver/) y descarga la versión compatible con tu Chrome.
   - Extrae el archivo y copia `chromedriver.exe` en la carpeta del proyecto o en una ubicación accesible del sistema.

2. **Agregar ChromeDriver al PATH** *(Opcional, pero recomendado)*:
   - **Windows:** Agrega la ruta de `chromedriver.exe` en las variables de entorno.
   - **Mac/Linux:** Mueve el archivo a `/usr/local/bin/`:
     ```bash
     sudo mv chromedriver /usr/local/bin/
     ```

---

### **5️⃣ Ejecutar el código**
Una vez configurado todo, ejecuta el script con:

```bash
python main.py
```

Si necesitas ejecutar el código en segundo plano (sin abrir la ventana del navegador), descomenta la línea:
```python
# chrome_options.add_argument("--headless")
```

---

## 🚀 **Solución de problemas**
Si encuentras errores al ejecutar el código:

- **`chromedriver` no encontrado:** Verifica que está en la misma carpeta del proyecto o en el PATH del sistema.
- **Error de versión de Chrome:** Asegúrate de que `chromedriver` sea compatible con la versión de tu Chrome.
- **Problema con dependencias:** Reinstala Selenium con `pip install --upgrade selenium`.

---

## 📢 **Contacto**
Si tienes preguntas o sugerencias, abre un issue en el repositorio de GitHub.

✅ **¡Listo! Ahora puedes ejecutar el código en cualquier ordenador siguiendo estos pasos!** 🎉
