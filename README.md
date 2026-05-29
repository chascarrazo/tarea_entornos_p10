# P10 - Gestor de Pedidos

## Problemas detectados
1. **Código Duplicado:** La lógica condicional de asignación de descuentos se encontraba clonada de forma redundante en los métodos `ver_pedidos` y `calcular_total_desde_menu` de `pedidos.py`.
2. **Validaciones Débiles:** El alta de clientes permitía introducir estructuras de correos inválidas e inconsistentes sin arrojar advertencias.
3. **Código Muerto:** Presencia de la función huérfana `cambiar_estado_pedido` sin invocaciones en todo el flujo del software.

## Refactorizaciones realizadas
| Problema | Refactorización | Archivo | Commit |
|---|---|---|---|
| Validación Pobre | Extracción de validación lógica de e-mails | clientes.py | "Mejora nombres de variables y validaciones" |
| Lógica Duplicada | Extracción de comportamiento a `calcular_descuento_comercial` | pedidos.py | "Extrae lógica de cálculo de pedidos" |
| Escalabilidad de Precios | Creación de tramo preferente del 15% para grandes cuentas | pedidos.py | "Refactoriza lógica de descuentos" |

## Pruebas creadas
| Test | Qué comprueba |
|---|---|
| test_pedidos.py | Verifica la exactitud matemática de los descuentos comerciales (0%, 5%, 10%) según los límites de la base imponible. |

## Analizador de código
Analizador usado: Ruff
Opciones configuradas:
1. line-length = 100
2. target-version = "py312"
3. select = ["E", "F", "W", "I"]

## Trabajo con Git y ramas
Rama creada: `refactor-descuentos`
Commits principales: "Inicializa el proyecto base", "Extrae lógica de cálculo de pedidos", "Refactoriza lógica de descuentos"
Fusión realizada: Fusión e integración limpia tipo *Fast-forward* hacia la rama primordial `main`.

## Integración continua
Resultado del workflow: Estatus Green / Success. El pipeline automatizado en GitHub Actions compila de forma perfecta ejecutando el linter Ruff y los tests de Pytest bajo un entorno virtualizado Ubuntu.