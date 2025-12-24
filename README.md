# Inteligencia de la Seguridad – Práctica 3  
## Escenario de ataque simulado (keylogging) y análisis forense en memoria con Volatility

Práctica de la asignatura **Inteligencia de la Seguridad (URJC)** centrada en diseñar un
**escenario de ataque propio** que deje rastro en el sistema, capturar un **memory dump**
de una máquina Windows y analizarlo con **Volatility** para reconstruir el vector de ataque.

En este caso, el escenario elegido es un **keylogger educativo desarrollado por el alumno**,
utilizado únicamente en un entorno de laboratorio controlado.

---

## Estructura del repositorio

```text
.
├─ src/
│  └─ CrackGTAVI.pyw        # Script del escenario (keylogger educativo en Windows)
├─ artifacts/
│  └─ keyoutput.txt         # Ejemplo de salida
└─ extra/
   └─ pyHook-*.whl          # Wheel de pyHook usada en el laboratorio
```

El memory dump y los ficheros de Volatility no se incluyen por tamaño.
