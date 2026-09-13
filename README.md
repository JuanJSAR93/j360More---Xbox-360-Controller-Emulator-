# j360More - Multi-Gamepad Emulator (1 a 12 Mandos Xbox 360)

> **Desarrollado por JuanJSAR**  
> Repositorio Oficial: [GitHub - JuanJSAR93/j360More](https://github.com/JuanJSAR93/j360More---Xbox-360-Controller-Emulator-)  
> Descargas y Versiones: [Releases Oficiales](https://github.com/JuanJSAR93/j360More---Xbox-360-Controller-Emulator-/releases)  
> Documentación Web (GitHub Pages): Disponible en la carpeta `/docs`

**j360More** es una solución avanzada de emulación multi-mando para Windows desarrollada por **JuanJSAR** sobre el controlador kernel **ViGEmBus**, con soporte bilingüe (**Español e Inglés**), interfaz gráfica intuitiva inspirada en x360ce, soporte para hasta **12 mandos virtuales de Xbox 360** simultáneos e integración opcional con **Nefarius HidHide** para erradicar el molesto problema de "doble entrada" (doble mando) en juegos de PC y emuladores.

Permite asociar periféricos físicos reales (mandos USB o Bluetooth DirectInput/XInput, Joysticks genéricos, Teclado y Ratón) a cada mando virtual, calibrar curvas analógicas en tiempo real y probar la respuesta reactiva directamente sobre un diagrama vectorial interactivo.

---

## 🎮 Características Principales

### 1. Soporte Extendido de 1 a 12 Mandos Simultáneos
- Configura libremente la cantidad de mandos virtuales activos (de 1 a 12) desde la ventana de **`⚙ Configuración...`**.
- Pestañas individuales e independientes para cada jugador (`Control 1` a `Control 12`).

### 2. Activación Inteligente y Bloqueo de Mapeo sin Dispositivo
- Si un control tiene asignado `-- Ninguno / Desconectado --`:
  - La casilla **`[ ] Habilitado`** se bloquea de forma opaca (`disabled`) con valor `False`.
  - Todas las opciones de mapeo (comboboxes, botones `...`, curvas de calibración, canvas) quedan **desactivadas y opacas**.
  - **ViGEmBus no crea mandos fantasma**: solo se instancian en el sistema los mandos que tienen un periférico físico asignado y habilitado.
  - Si intentas iniciar la emulación sin ningún periférico asignado a ningún control, la app muestra un aviso preventivo y no inicia mandos innecesarios.
- Al seleccionar un dispositivo (Joystick, Teclado o Ratón), todas las opciones y la casilla de habilitación se reactivan automáticamente.

### 3. Integración Opcional con Nefarius HidHide (Anti Doble Entrada)
- **Completamente Opcional**: Si HidHide no está instalado en tu equipo, j360More funciona con total normalidad para emular controles.
- **Aviso Informativo Suave**: Si no se detecta HidHide, la app muestra un aviso leve con la casilla **`[ ] No volver a mostrar este aviso`** para no volver a interrumpirte si prefieres usarlo sin él.
- **Ruta Personalizada**: En `⚙ Configuración...` puedes ver el estado del driver, activar/desactivar el *Cloaking* global y especificar manualmente la ruta a `HidHideCLI.exe` con un botón **`📂 Examinar...`**.
- **Gestión en `🎮 Dispositivos DirectInput...`**:
  - Tabla con columna **`HidHide`** (`🚫 Oculto` vs `👁 Visible`).
  - Botones **`🔒 Ocultar al Emular`** y **`🔓 Mantener Visible`** (se muestran opacos y deshabilitados si HidHide no está presente).
  - **Ocultamiento Dinámico**: Al pulsar **`▶ Iniciar Emulación`**, j360More oculta de inmediato los periféricos seleccionados para todo Windows mediante HidHide, permitiendo que **solo j360More** pueda leerlos (gracias a la lista blanca automática). Al pulsar **`⏹ Detener Emulación`** (o cerrar la app), los periféricos vuelven a ser visibles para todo el sistema automáticamente.

### 4. Diagrama Vectorial Interactivo del Mando Xbox 360
- Diagrama renderizado en alta fidelidad.
- **Mapeo por Clic**: Haz clic directo sobre cualquier botón o palanca del dibujo del mando para iniciar su asignación instantánea.
- **LEDs Reactivos Glow**: Cada botón, gatillo, cruceta o movimiento de stick se ilumina en verde neón en tiempo real al pulsarlo en tu mando físico.
- **Halo de Asignación**: Indicador visual pulsante ambar/rojo sobre el componente que está esperando que presiones un botón o tecla.

### 5. Calibración Especializada de Gatillos y Sticks
- **Sub-pestaña `Triggers` (Gatillos LT / RT)**:
  - Gráfica cuadrática de respuesta en tiempo real (DI vs XI).
  - Ajustes de **Dead Zone (Zona Muerta)**, **Anti-Dead Zone**, **Sensibilidad** e **Inversión**.
- **Sub-pestaña `Sticks` (Sticks Izquierdo y Derecho)**:
  - Visualizador cartesiano 2D con retícula, punto verde de posición actual, y círculos de Dead Zone y Anti-Dead Zone.
  - Gráfica de curva de sensibilidad de respuesta angular y magnitud.
  - Controles de **Dead Zone**, **Anti-Dead Zone**, **Sensibilidad**, **Invertir Eje X** e **Invertir Eje Y**.
- **Entrada Numérica Dual**: Cada parámetro cuenta con un slider de pasos enteros y un campo numérico para ingresar valores exactos o decimales con `%`.

### 6. Productividad y Utilidades
- **Botón `...` (Captura Rápida / Record)**: Presiónalo y oprime el botón o eje de tu mando para mapearlo al instante sin buscarlo en listas.
- **Botón `📋 Copiar Mapeo a...`**: Duplica la configuración de botones y calibración hacia otro mando (o a todos los demás) sin sobreescribir el periférico asignado a cada uno.
- **Botón `🎮 Abrir joy.cpl`**: Acceso directo al panel de dispositivos de juego nativo de Windows.
- **Inspección de Hardware**: Consulta VID, PID, GUID SDL, Instance ID y tipo de conexión (USB/BT).

---

## 📋 Requisitos del Sistema

### Obligatorios:
- **Windows 10 o Windows 11 (64-bit)**.
- **Controlador ViGEmBus**: Necesario para crear los mandos virtuales de Xbox 360 en el sistema.
  - Descarga oficial: [ViGEmBus Releases (GitHub)](https://github.com/nefarius/ViGEmBus/releases)

### Opcionales:
- **Nefarius HidHide**: Recomendado si vas a jugar títulos que detectan periféricos DirectInput genéricos simultáneamente con mandos de Xbox 360, evitando la doble pulsación.
  - Descarga oficial: [HidHide Releases (GitHub)](https://github.com/nefarius/HidHide/releases)

---

## 🛠 Instalación y Uso desde Código Fuente

### 1. Clonar o descargar el repositorio
```powershell
cd C:\ruta\a\j360More
```

### 2. Crear / Activar entorno de Python (Recomendado Python 3.10 a 3.14)
```powershell
python -m venv venv
.\venv\Scripts\activate
```

### 3. Instalar dependencias
```powershell
pip install -r requirements.txt
```

### 4. Ejecutar la aplicación
```powershell
python gui_app.py
# o alternativamente:
python emulator.py
```

---

## 📦 Compilación a Ejecutable (.exe)

La aplicación se compila en una distribución optimizada portátil que **inicia al instante (<0.2s)** y **sin parpadeos de consola negra**:

### Método 1: Compilación Automática con `build.bat` (Recomendado)
Haz doble clic en el archivo **`build.bat`** en la raíz del proyecto. El script se encargará automáticamente de:
1. Comprobar Python y Pip.
2. Instalar dependencias (`requirements.txt`).
3. Limpiar compilaciones anteriores.
4. Empaquetar la aplicación en **`dist\j360More\j360More.exe`** en modo ventana (`--windowed`) y directorio distribuido (`--onedir`), incluyendo librerías nativas (`ViGEmClient.dll`, `resvg_py`).
5. Copiar automáticamente los archivos de configuración (`config_mapping.json`) y recursos visuales.

### Método 2: Compilación Manual con PyInstaller
Ejecuta en tu terminal:
```powershell
pyinstaller --noconfirm --onedir --windowed --name "j360More" --add-data "assets;assets" --collect-all "vgamepad" --collect-all "resvg_py" gui_app.py
```
El ejecutable resultante estará en **`dist\j360More\j360More.exe`** (puedes ejecutarlo también desde la raíz con `Iniciar_j360More.bat`).

---

## 📂 Estructura del Proyecto

```text
xbox_multi_emulator/
├── assets/                     # Recursos visuales
│   ├── controller.svg          # Diagrama vectorial del mando Xbox 360
│   ├── controller_render.png   # Render optimizado de alta resolución
│   └── controller.png          # Imagen de respaldo
├── build.bat                   # Compilador con un solo clic a dist\j360More\
├── docs/                       # Página web oficial para GitHub Pages
│   ├── assets/                 # Recursos gráficos web (logos, render)
│   ├── index.html              # Landing page principal
│   ├── script.js               # Interactividad (menú, acordeón FAQ, copiar)
│   └── styles.css              # Estilos modernos Cyber Gaming
├── Iniciar_j360More.bat        # Lanzador rápido desde la raíz del proyecto
├── config_mapping.json         # Archivo de configuración persistente (JSON)
├── driver_manager.py           # Administrador de controladores ViGEmBus e HidHide
├── emulator.py                 # Punto de entrada y modos consola/test
├── emulator_engine.py          # Motor de emulación a 120Hz con vgamepad
├── gui_app.py                  # Interfaz gráfica principal Tkinter/TTK
├── input_devices.py            # Detección SDL2 en caliente y correlación PnP
└── requirements.txt            # Dependencias de Python
```

---

## 📄 Licencia y Créditos
- **Creador y Desarrollador Principal**: **JuanJSAR** ([@JuanJSAR93](https://github.com/JuanJSAR93))
- Emulación del bus de control virtual impulsada por **ViGEmBus** y **HidHide** creados por Benjamin Höglinger-Stelzer (Nefarius Software Solutions).
- Soporte para detección en caliente y periféricos provisto por **pygame-ce** (SDL2).
- Diseñado para entusiastas de juegos locales multijugador en PC de todo el mundo.
