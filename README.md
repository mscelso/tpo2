# TPO2 - Automatización de pruebas y pipeline CI/CD

## Objetivo

Implementar un flujo básico de automatización de pruebas integrado a un pipeline de integración continua, aplicando conceptos de testing y DevOps.

## Funcionalidad desarrollada

Se desarrolló un sistema simple de descuentos en Python.

La función principal recibe un precio original y un porcentaje de descuento, y devuelve el precio final con el descuento aplicado.

## Escenario de prueba

Se desea validar que el cálculo de descuentos funcione correctamente ante casos normales, casos inválidos y casos borde.

## Casos de prueba

### Caso exitoso

Entrada:

- Precio: 1000
- Descuento: 20%

Resultado esperado:

- Precio final: 800

### Caso de error

Entrada:

- Precio: -1000
- Descuento: 20%

Resultado esperado:

- El sistema debe lanzar un error porque el precio no puede ser negativo.

### Caso borde

Entrada:

- Precio: 1000
- Descuento: 100%

Resultado esperado:

- Precio final: 0

## Automatización de pruebas

Las pruebas fueron automatizadas utilizando Python y pytest.

## Pipeline CI/CD

Se configuró un pipeline con GitHub Actions que se ejecuta automáticamente al hacer push.

El pipeline instala dependencias, ejecuta los tests y genera un reporte HTML como artefacto.