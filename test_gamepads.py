import time
import vgamepad as vg

def test_8_controllers():
    print("==================================================")
    print(" VERIFICACION DE CREACION DE 8 MANDOS XBOX 360")
    print("==================================================")

    pads = []
    try:
        for i in range(1, 9):
            print(f"[*] Creando Mando #{i}...")
            pad = vg.VX360Gamepad()
            pad.reset()
            pad.update()
            pads.append(pad)
            time.sleep(0.1)

        print(f"\n[+] Se han instanciado satisfactoriamente los {len(pads)} mandos.")
        print("[*] Enviando pulsacion de prueba de los botones A, B, X, Y en cada mando...")

        buttons = [
            ("A", vg.XUSB_BUTTON.XUSB_GAMEPAD_A),
            ("B", vg.XUSB_BUTTON.XUSB_GAMEPAD_B),
            ("X", vg.XUSB_BUTTON.XUSB_GAMEPAD_X),
            ("Y", vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
        ]

        for i, pad in enumerate(pads, 1):
            print(f"\n--- Probando Mando #{i} ---")
            for name, btn in buttons:
                print(f"  Pulsando {name}...")
                pad.press_button(button=btn)
                pad.update()
                time.sleep(0.1)
                pad.release_button(button=btn)
                pad.update()
                time.sleep(0.05)

        print("\n[+] Prueba completada exitosamente.")
        print("[*] Desconectando mandos virtuales...")
    finally:
        for pad in pads:
            pad.reset()
            pad.update()
        del pads
        print("[+] Mandos desconectados y recursos liberados.")

if __name__ == '__main__':
    test_8_controllers()
