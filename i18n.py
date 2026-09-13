# -*- coding: utf-8 -*-
"""
i18n.py - Sistema de Internacionalización (Español / English) para j360More
Desarrollado por JuanJSAR
"""

STRINGS = {
    "es": {
        "app_title": "j360More - Multi-Gamepad (1 a 12 Mandos) - por JuanJSAR - ViGEmBus",
        "author_credit": "Desarrollado por JuanJSAR",
        "header_title": "j360More ({count} Mandos) - por JuanJSAR",
        "btn_devices": "🎮 Dispositivos DirectInput...",
        "btn_settings": "⚙ Configuración...",
        "btn_language": "🌐 Idioma: Español",
        "status_stopped": "Emulación Detenida",
        "status_active": "Emulación Activa (120Hz)",
        "status_error": "Error en Emulación",
        "btn_start_emu": "▶ Iniciar Emulación",
        "btn_stop_emu": "⏹ Detener Emulación",
        "btn_joy_cpl": "🎮 joy.cpl Windows",
        "btn_save": "💾 Guardar",
        "btn_reset": "↺ Restaurar Preset",
        "tab_control": "Control {i}",
        "tab_c": "C{i}",
        
        # Tab content
        "lbl_enabled": "Habilitado",
        "lbl_device": "Periférico",
        "none_disconnected": "-- Ninguno / Desconectado --",
        "keyboard_device_name": "Teclado (Mapeo de Teclas)",
        "btn_refresh": "🔄 Refrescar",
        "btn_copy_to": "📋 Copiar Mapeo a...",
        
        # Sub-tabs
        "subtab_general": "General",
        "subtab_triggers": "Triggers",
        "subtab_sticks": "Sticks",
        
        # Section titles
        "sec_left_controls": "CONTROLES IZQUIERDOS",
        "row_left_trigger": "Trigger (LT):",
        "row_left_shoulder": "Bumper (LB):",
        "row_back": "Back:",
        "row_start": "Start:",
        "row_guide": "Guía (Xbox):",
        "sec_left_stick": "STICK IZQ. (EJES / TECLAS)",
        "row_stick_axis_x": "Stick Eje X:",
        "row_stick_axis_y": "Stick Eje Y:",
        "row_stick_button": "Stick Botón:",
        "row_stick_up": "Stick Arriba:",
        "row_stick_down": "Stick Abajo:",
        "row_stick_left": "Stick Izq.:",
        "row_stick_right": "Stick Der.:",
        
        # Canvas & D-Pad
        "hint_canvas_click": "💡 Clic en cualquier botón del mando para mapear",
        "hint_cancelled": "❌ Asignación cancelada con Escape",
        "hint_no_device": "⚠️ Sin periférico asignado. Selecciona un dispositivo arriba para habilitar el mapeo.",
        "hint_click_map": "👉 Clic para mapear: [{name}]",
        "hint_mapping_wait": "🎯 Mapeando: [{name}]... Presiona botón en tu mando o tecla (Esc para cancelar)",
        "sec_dpad": "CRUCETA (D-PAD)",
        "row_dpad_up": "D-Pad Arriba:",
        "row_dpad_down": "D-Pad Abajo:",
        "row_dpad_left": "D-Pad Izq.:",
        "row_dpad_right": "D-Pad Der.:",
        
        # Right controls
        "sec_right_controls": "CONTROLES DERECHOS",
        "row_right_trigger": "Trigger (RT):",
        "row_right_shoulder": "Bumper (RB):",
        "row_btn_y": "Botón Y:",
        "row_btn_x": "Botón X:",
        "row_btn_b": "Botón B:",
        "row_btn_a": "Botón A:",
        "sec_right_stick": "STICK DER. (EJES / TECLAS)",
        
        # Triggers & Sticks subtabs
        "curve_response": "Curva Respuesta",
        "pos_2d": "Posición 2D",
        "lbl_anti_deadzone": "Anti-Dead Zone:",
        "lbl_deadzone": "Dead Zone:",
        "lbl_sensitivity": "Sensibilidad:",
        "chk_invert_axis": "Invertir eje (Invert)",
        "chk_invert_x": "Invertir Eje X",
        "chk_invert_y": "Invertir Eje Y",
        "title_left_trigger": "Gatillo Izquierdo (Left Trigger)",
        "title_right_trigger": "Gatillo Derecho (Right Trigger)",
        "title_left_stick": "Stick Izquierdo (Left Stick)",
        "title_right_stick": "Stick Derecho (Right Stick)",
        
        "assigned_device": "Dispositivo físico asignado:",
        "no_device": "-- Ningún periférico asignado --",
        "keyboard_device": "⌨ Teclado (Mapeo por teclas)",
        "btn_calibrate": "🎯 Calibrar Ejes y Gatillos...",
        "btn_wizard": "🔴 Asistente de Grabación",
        "press_button": "Presiona un botón...",
        "unassigned_warning": "No se puede activar el control {i} porque no tiene ningún periférico asignado.",
        "config_saved": "¡Configuración guardada exitosamente en config_mapping.json!",
        "config_error": "No se pudo guardar la configuración: {e}",
        "preset_restored": "¡Mapeo predeterminado restaurado para Control {i}!",
        "none_option": "-- Ninguno --",
        
        # Copy dialog
        "copy_dlg_title": "Copiar Configuración",
        "copy_from_pad": "📋 Copiar Mapeo desde: Control {id}",
        "dest_controller": "Mando Destino:",
        "dest_all_others": "Todos los demás mandos (1 al {max})",
        "dest_pad_item": "Control {id}",
        "inc_calib": "Incluir calibración (Deadzone, Anti-Deadzone, Sensibilidad)",
        "copy_note": "ℹ️ El periférico físico asignado a cada mando se conservará intacto.",
        "btn_copy_submit": "✔ Copiar Configuración",
        "copy_success_title": "Copia Exitosa",
        "copy_success_msg": "¡Configuración de botones copiada con éxito a {dest}!\n\nSolo debes asignar el periférico físico a cada control.",
        
        # Conflict dialogs
        "conflict_same_title": "Aviso: Entrada ya mapeada en este mando",
        "conflict_same_msg": "⚠️ La entrada '{val}' ya está asignada en este mismo mando:\n\n  • Posición actual: [{other}]\n\n¿Qué deseas hacer para [{target}]?\n\n[Sí] Mover a esta nueva posición (se desasigna de [{other}]).\n[No] Mantener la entrada en ambas posiciones (compartir).\n[Cancelar] Descartar cambio y mantener valor anterior.",
        "conflict_other_title": "Aviso: Entrada ya mapeada en otro mando",
        "conflict_other_msg": "⚠️ La entrada '{val}' ya está asignada en otro mando virtual:\n\n  • Mando: {name} (Control {id})\n  • Botón asignado: [{other}]\n\n¿Qué deseas hacer?\n\n[Sí] Reasignar a este mando (se desasigna del Control {id}).\n[No] Mantener la entrada en ambos mandos (compartir).\n[Cancelar] Descartar cambio y mantener valor anterior.",
        
        # Emulation warnings
        "emu_unavailable_title": "Emulación No Disponible",
        "emu_unavailable_msg": "Ningún control tiene un periférico asignado o está habilitado.\n\nAsigna al menos un dispositivo físico (Joystick o Teclado) en alguno de los controles para poder iniciar la emulación.",
        
        # Devices dialog
        "dev_dlg_title": "Dispositivos DirectInput Detectados",
        "dev_dlg_header": "Direct Input Devices - Todo lo que j360More puede leer y mapear",
        "dev_col_slot": "Ranura / ID",
        "dev_col_name": "Nombre de Dispositivo",
        "dev_col_type": "Tipo",
        "dev_col_hide": "HidHide",
        "dev_col_path": "Ruta PnP (Hardware ID)",
        "dev_col_status": "Estado",
        "dev_status_connected": "✔ Conectado",
        "dev_btn_refresh": "🔄 Actualizar Lista",
        "dev_btn_hw": "🛠 Hardware...",
        "dev_btn_unhide": "🔓 Mantener Visible",
        "dev_btn_hide": "🔒 Ocultar al Emular",
        "dev_btn_assign": "🎯 Asignar al Control Actual",
        "dev_btn_close": "Cerrar",
        "dev_hide_hint": "Selecciona los dispositivos que deseas ocultar al iniciar la emulación para evitar doble control.",
        "dev_assign_success": "¡Dispositivo asignado exitosamente al Control {id}!",
        "dev_select_device": "Selecciona un dispositivo de la lista.",
        
        # Settings dialog
        "set_dlg_title": "Configuración General",
        "set_language_label": "Idioma de la Interfaz / Interface Language:",
        "set_max_ctrls": "Número máximo de mandos (1 a 12):",
        "set_mandos_title": "⚙ Mandos Virtuales a Emular",
        "set_hidhide_title": "🛡 Integración con Nefarius HidHide (Opcional)",
        "set_hidhide_path": "Ruta de HidHideCLI.exe:",
        "set_btn_browse": "Examinar...",
        "set_btn_save": "Guardar Configuración",
        "set_btn_cancel": "Cancelar",
        "set_saved": "Configuración actualizada correctamente.",
        
        # Driver check
        "vigem_missing_title": "ViGEmBus no encontrado",
        "vigem_missing_msg": "No se detectó el driver ViGEmBus.\n\nEs OBLIGATORIO para crear mandos virtuales de Xbox 360.\n¿Deseas abrir la página de descarga oficial de ViGEmBus?",
        "hidhide_missing_title": "Aviso HidHide (Opcional)",
        "hidhide_missing_msg": "HidHide no está instalado en tu sistema.\n\nHidHide es recomendado para evitar que los juegos detecten doble mando.\n¿Deseas abrir la página de descarga oficial?",
        
        # Target names
        "target_names": {
            "A": "Botón A",
            "B": "Botón B",
            "X": "Botón X",
            "Y": "Botón Y",
            "GUIDE": "Botón Guía (Xbox)",
            "BACK": "Botón Back / Selec",
            "START": "Botón Start",
            "LEFT_THUMB": "Stick Izq. Botón (L3)",
            "RIGHT_THUMB": "Stick Der. Botón (R3)",
            "LEFT_STICK_X": "Stick Izq. Eje X",
            "LEFT_STICK_Y": "Stick Izq. Eje Y",
            "LEFT_STICK_UP": "Stick Izq. Arriba",
            "LEFT_STICK_DOWN": "Stick Izq. Abajo",
            "LEFT_STICK_LEFT": "Stick Izq. Izquierda",
            "LEFT_STICK_RIGHT": "Stick Izq. Derecha",
            "RIGHT_STICK_X": "Stick Der. Eje X",
            "RIGHT_STICK_Y": "Stick Der. Eje Y",
            "RIGHT_STICK_UP": "Stick Der. Arriba",
            "RIGHT_STICK_DOWN": "Stick Der. Abajo",
            "RIGHT_STICK_LEFT": "Stick Der. Izquierda",
            "RIGHT_STICK_RIGHT": "Stick Der. Derecha",
            "DPAD_UP": "D-Pad Arriba",
            "DPAD_DOWN": "D-Pad Abajo",
            "DPAD_LEFT": "D-Pad Izquierda",
            "DPAD_RIGHT": "D-Pad Derecha",
            "LEFT_SHOULDER": "Bumper Izq. (LB)",
            "RIGHT_SHOULDER": "Bumper Der. (RB)",
            "LEFT_TRIGGER": "Gatillo Izq. (LT)",
            "RIGHT_TRIGGER": "Gatillo Der. (RT)"
        }
    },
    "en": {
        "app_title": "j360More - Multi-Gamepad (1 to 12 Controllers) - by JuanJSAR - ViGEmBus",
        "author_credit": "Developed by JuanJSAR",
        "header_title": "j360More ({count} Controllers) - by JuanJSAR",
        "btn_devices": "🎮 DirectInput Devices...",
        "btn_settings": "⚙ Settings...",
        "btn_language": "🌐 Language: English",
        "status_stopped": "Emulation Stopped",
        "status_active": "Emulation Active (120Hz)",
        "status_error": "Emulation Error",
        "btn_start_emu": "▶ Start Emulation",
        "btn_stop_emu": "⏹ Stop Emulation",
        "btn_joy_cpl": "🎮 Windows joy.cpl",
        "btn_save": "💾 Save",
        "btn_reset": "↺ Reset Preset",
        "tab_control": "Controller {i}",
        "tab_c": "C{i}",
        
        # Tab content
        "lbl_enabled": "Enabled",
        "lbl_device": "Device",
        "none_disconnected": "-- None / Disconnected --",
        "keyboard_device_name": "Keyboard (Key Mapping)",
        "btn_refresh": "🔄 Refresh",
        "btn_copy_to": "📋 Copy Mapping to...",
        
        # Sub-tabs
        "subtab_general": "General",
        "subtab_triggers": "Triggers",
        "subtab_sticks": "Sticks",
        
        # Section titles
        "sec_left_controls": "LEFT CONTROLS",
        "row_left_trigger": "Trigger (LT):",
        "row_left_shoulder": "Bumper (LB):",
        "row_back": "Back:",
        "row_start": "Start:",
        "row_guide": "Guide (Xbox):",
        "sec_left_stick": "LEFT STICK (AXES / KEYS)",
        "row_stick_axis_x": "Stick X Axis:",
        "row_stick_axis_y": "Stick Y Axis:",
        "row_stick_button": "Stick Button:",
        "row_stick_up": "Stick Up:",
        "row_stick_down": "Stick Down:",
        "row_stick_left": "Stick Left:",
        "row_stick_right": "Stick Right:",
        
        # Canvas & D-Pad
        "hint_canvas_click": "💡 Click on any controller button to map",
        "hint_cancelled": "❌ Mapping cancelled with Escape",
        "hint_no_device": "⚠️ No device assigned. Select a device above to enable mapping.",
        "hint_click_map": "👉 Click to map: [{name}]",
        "hint_mapping_wait": "🎯 Mapping: [{name}]... Press button on controller or key (Esc to cancel)",
        "sec_dpad": "D-PAD",
        "row_dpad_up": "D-Pad Up:",
        "row_dpad_down": "D-Pad Down:",
        "row_dpad_left": "D-Pad Left:",
        "row_dpad_right": "D-Pad Right:",
        
        # Right controls
        "sec_right_controls": "RIGHT CONTROLS",
        "row_right_trigger": "Trigger (RT):",
        "row_right_shoulder": "Bumper (RB):",
        "row_btn_y": "Button Y:",
        "row_btn_x": "Button X:",
        "row_btn_b": "Button B:",
        "row_btn_a": "Button A:",
        "sec_right_stick": "RIGHT STICK (AXES / KEYS)",
        
        # Triggers & Sticks subtabs
        "curve_response": "Response Curve",
        "pos_2d": "2D Position",
        "lbl_anti_deadzone": "Anti-Dead Zone:",
        "lbl_deadzone": "Dead Zone:",
        "lbl_sensitivity": "Sensitivity:",
        "chk_invert_axis": "Invert Axis",
        "chk_invert_x": "Invert X Axis",
        "chk_invert_y": "Invert Y Axis",
        "title_left_trigger": "Left Trigger (LT)",
        "title_right_trigger": "Right Trigger (RT)",
        "title_left_stick": "Left Stick (LS)",
        "title_right_stick": "Right Stick (RS)",
        
        "assigned_device": "Assigned Physical Device:",
        "no_device": "-- No device assigned --",
        "keyboard_device": "⌨ Keyboard (Key Mapping)",
        "btn_calibrate": "🎯 Calibrate Axes & Triggers...",
        "btn_wizard": "🔴 Quick Mapping Wizard",
        "press_button": "Press a button...",
        "unassigned_warning": "Cannot enable Controller {i} because no physical device is assigned.",
        "config_saved": "Configuration successfully saved to config_mapping.json!",
        "config_error": "Could not save configuration: {e}",
        "preset_restored": "Default mapping restored for Controller {i}!",
        "none_option": "-- None --",
        
        # Copy dialog
        "copy_dlg_title": "Copy Configuration",
        "copy_from_pad": "📋 Copy Mapping from: Controller {id}",
        "dest_controller": "Destination Controller:",
        "dest_all_others": "All other controllers (1 to {max})",
        "dest_pad_item": "Controller {id}",
        "inc_calib": "Include calibration (Deadzone, Anti-Deadzone, Sensitivity)",
        "copy_note": "ℹ️ The physical device assigned to each controller will remain intact.",
        "btn_copy_submit": "✔ Copy Configuration",
        "copy_success_title": "Copy Successful",
        "copy_success_msg": "Button configuration copied successfully to {dest}!\n\nYou only need to assign the physical device to each controller.",
        
        # Conflict dialogs
        "conflict_same_title": "Warning: Input already mapped on this controller",
        "conflict_same_msg": "⚠️ Input '{val}' is already assigned on this controller:\n\n  • Current position: [{other}]\n\nWhat would you like to do for [{target}]?\n\n[Yes] Move to this new position (unassign from [{other}]).\n[No] Keep input in both positions (share).\n[Cancel] Discard change and keep previous value.",
        "conflict_other_title": "Warning: Input already mapped on another controller",
        "conflict_other_msg": "⚠️ Input '{val}' is already assigned on another virtual controller:\n\n  • Controller: {name} (Controller {id})\n  • Assigned button: [{other}]\n\nWhat would you like to do?\n\n[Yes] Reassign to this controller (unassign from Controller {id}).\n[No] Keep input in both controllers (share).\n[Cancel] Discard change and keep previous value.",
        
        # Emulation warnings
        "emu_unavailable_title": "Emulation Not Available",
        "emu_unavailable_msg": "No controller has a physical device assigned or is enabled.\n\nAssign at least one physical device (Joystick or Keyboard) to a controller to start emulation.",
        
        # Devices dialog
        "dev_dlg_title": "Detected DirectInput Devices",
        "dev_dlg_header": "Direct Input Devices - Everything j360More can read and map",
        "dev_col_slot": "Slot / ID",
        "dev_col_name": "Device Name",
        "dev_col_type": "Type",
        "dev_col_hide": "HidHide",
        "dev_col_path": "PnP Path (Hardware ID)",
        "dev_col_status": "Status",
        "dev_status_connected": "✔ Connected",
        "dev_btn_refresh": "🔄 Refresh List",
        "dev_btn_hw": "🛠 Hardware...",
        "dev_btn_unhide": "🔓 Keep Visible",
        "dev_btn_hide": "🔒 Cloak on Emulation",
        "dev_btn_assign": "🎯 Assign to Current Controller",
        "dev_btn_close": "Close",
        "dev_hide_hint": "Select devices to cloak on emulation start to prevent double-controller issues.",
        "dev_assign_success": "Device successfully assigned to Controller {id}!",
        "dev_select_device": "Select a device from the list.",
        
        # Settings dialog
        "set_dlg_title": "General Settings",
        "set_language_label": "Interface Language / Idioma:",
        "set_max_ctrls": "Maximum controllers count (1 to 12):",
        "set_mandos_title": "⚙ Virtual Controllers to Emulate",
        "set_hidhide_title": "🛡 Nefarius HidHide Integration (Optional)",
        "set_hidhide_path": "HidHideCLI.exe path:",
        "set_btn_browse": "Browse...",
        "set_btn_save": "Save Settings",
        "set_btn_cancel": "Cancel",
        "set_saved": "Settings successfully updated.",
        
        # Driver check
        "vigem_missing_title": "ViGEmBus Not Found",
        "vigem_missing_msg": "ViGEmBus driver was not detected.\n\nIt is MANDATORY to spawn virtual Xbox 360 controllers.\nWould you like to open the official ViGEmBus download page?",
        "hidhide_missing_title": "HidHide Notice (Optional)",
        "hidhide_missing_msg": "HidHide is not installed on your system.\n\nHidHide is recommended to prevent games from detecting double inputs.\nWould you like to open the official download page?",
        
        # Target names
        "target_names": {
            "A": "Button A",
            "B": "Button B",
            "X": "Button X",
            "Y": "Button Y",
            "GUIDE": "Guide Button (Xbox)",
            "BACK": "Back / Select Button",
            "START": "Start Button",
            "LEFT_THUMB": "Left Thumb Button (L3)",
            "RIGHT_THUMB": "Right Thumb Button (R3)",
            "LEFT_STICK_X": "Left Stick X Axis",
            "LEFT_STICK_Y": "Left Stick Y Axis",
            "LEFT_STICK_UP": "Left Stick Up",
            "LEFT_STICK_DOWN": "Left Stick Down",
            "LEFT_STICK_LEFT": "Left Stick Left",
            "LEFT_STICK_RIGHT": "Left Stick Right",
            "RIGHT_STICK_X": "Right Stick X Axis",
            "RIGHT_STICK_Y": "Right Stick Y Axis",
            "RIGHT_STICK_UP": "Right Stick Up",
            "RIGHT_STICK_DOWN": "Right Stick Down",
            "RIGHT_STICK_LEFT": "Right Stick Left",
            "RIGHT_STICK_RIGHT": "Right Stick Right",
            "DPAD_UP": "D-Pad Up",
            "DPAD_DOWN": "D-Pad Down",
            "DPAD_LEFT": "D-Pad Left",
            "DPAD_RIGHT": "D-Pad Right",
            "LEFT_SHOULDER": "Left Bumper (LB)",
            "RIGHT_SHOULDER": "Right Bumper (RB)",
            "LEFT_TRIGGER": "Left Trigger (LT)",
            "RIGHT_TRIGGER": "Right Trigger (RT)"
        }
    }
}

def get_text(lang: str, key: str, **kwargs) -> str:
    lang = lang if lang in STRINGS else "es"
    val = STRINGS[lang].get(key, STRINGS["es"].get(key, key))
    if kwargs and isinstance(val, str):
        return val.format(**kwargs)
    return val

def get_target_name(lang: str, target: str) -> str:
    lang = lang if lang in STRINGS else "es"
    targets = STRINGS[lang].get("target_names", {})
    return targets.get(target, STRINGS["es"]["target_names"].get(target, target))

def get_input_options(lang: str = "es") -> list:
    none_lbl = "-- None --" if lang == "en" else "-- Ninguno --"
    options = [none_lbl]
    for b in range(1, 17):
        options.append(f"Button {b}")
    for a in range(1, 7):
        options.extend([f"Axis {a}", f"IAxis {a}"])
    for p in ["POV 1 Up", "POV 1 Down", "POV 1 Left", "POV 1 Right"]:
        options.append(p)
    return options
