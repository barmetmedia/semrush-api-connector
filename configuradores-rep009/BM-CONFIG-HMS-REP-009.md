# BM-CONFIG-HMS-REP-009
Proyecto BM-CONFIGURADORES-2026-001 · ORDEN 012 · 2026-10-30 · Ejecutor: Claude Code (sesión cloud) · **Producción: 0 escrituras**

## 1. Estado recuperado y trabajo nuevo
Recuperado de Drive (G: no montada en el sandbox; Drive MCP accesible): REP-007, REP-008, INDICE maestro `Barmet/INDICE.md`, CSV A1 (441), A2 (188), PRICE-006 (1.953). No hay informes 009–012 en Drive; el contenido de las órdenes procede del prompt. Sin avances posteriores a REP-008 para Configuradores. CART-002/QA-004 no se repiten (código sin cambios).
Nuevo: matriz de 441 precios, validación cruzada con la serie Taupe 87, plan/rollback READY, script dry-run.

## 2. Matriz de 441 (archivos `MATRIZ-441.csv` completa y `-compacta.csv`)
- READY **364** · BLOCKED **77** · EXCLUDED 0 dentro del universo 441 · total 441/441.
- Taupe 87 preservadas: **63/63** (IDs 73223–73285, `TAUPE87-EXCLUIDAS.csv`; intersección con las 441 = 0; no se tocan).
- Evidencia E1 (READY): precio propuesto = precio PS de la serie Taupe 87 por nº de peldaños (3.561,81 / 3.862,43 / 4.163,04 / 4.463,66 / 4.763,54 € s/IVA, uniforme en las 63 filas Taupe) y coincide con la línea estándar de Shopify (A1) en 364/364. Coincidencia propuesto vs Taupe: 441/441.
- E2 (BLOCKED, 77): la línea estándar Shopify difiere de la serie Taupe: Blanco lacado 94 ×63 (Shopify +388,08 a +828,34 €; H13 y H14 con el mismo precio 4.551,12, posible dato duplicado), Blanqueado 84 H13 ×8 (5.517,75 vs 3.862,43), Nogal 25 H15 ×6 (4.358,66 vs 4.463,66). Posible recargo de acabado real o dato erróneo: decide Dirección con lectura viva de Shopify.
- Las 36 referencias compuestas (A2) están en las 441: 36 READY; precio de combinación Shopify = propuesto en 36/36.
- Dif. READY por fila: +1.386,42 / +1.462,76 / +1.539,09 / +1.615,43 / +1.691,03 € s/IVA.

## 3. Cruce Shopify–PrestaShop por variante
Validado variante a variante solo para las 441 (A1 + A2). Las 1.512 restantes **no regeneradas**: el MCP Shopify perdió la sesión (requiere reautenticar); la columna `sh_*` de PRICE-006 sigue siendo no fiable (REP-008). Cruce: 441/1.953.

## 4. Incidencias comerciales
| Incidencia | Estado |
|---|---|
| 441 precios 95 cm | 364 propuestos (READY), 77 BLOCKED |
| Nogal 25 (18 discrepancias) | PENDIENTE: no aislables sin cruce vivo; 6 filas H15 detectadas en BLOCKED |
| Blanco lacado 94 65 cm | PENDIENTE: PS solo tiene 75/85/95 cm; Shopify 3.178,14 € (REP-008); alta de combinaciones requiere autorización |
| 36 compuestas | Validadas (READY) |

## 5. INDICE.md
El índice maestro (543 líneas) se relee íntegro y contiene la entrada REP-008 (línea 479); no se reproduce el error «36 matches». El Drive MCP no permite modificar contenido de un fichero existente (solo metadatos), por lo que no se edita en sitio: se añade `INDICE-ADDENDUM-REP009.md` junto al índice. Actualización formal: **pendiente** (requiere vía con escritura, p. ej. Desktop Commander/dispositivo vinculado).

## 6. Backups y rollback
`PLAN-READY-364.csv` (precio_actual → propuesto), `ROLLBACK-READY-364.csv` (inverso exacto), `DRYRUN-441.py` (solo lectura). Antes de ejecutar: backup CSV fechado de PS, releer precio vivo y abortar fila si ≠ precio_actual, lotes ≤50, parar al primer fallo. SHA-256 (16 car.): MATRIZ a874f8bf6d38b11b · TAUPE cdb8258280fc3074 · PLAN b252f661fc19cbe1 · ROLLBACK 09183b379ffabe0e. **No se ejecutó ninguna modificación.**

## 7. Rutas y URLs
Drive (Hermes/Barmet/BM-CONFIGURADORES-2026-001/informes), repo `barmetmedia/semrush-api-connector` rama `claude/focused-mccarthy-56pbzx`, carpeta `configuradores-rep009/`. URLs barmet.es no re-comprobadas (sin navegador/perfil `hablamos@barmet.es`).

## 8. Agentes
Subagentes usados: **0** (trabajo de datos pequeño y secuencial; sin solapamientos).

## 9. Autorizaciones necesarias
A4 (escritura de precios) sigue denegado. Para lote parcial: autorizar las 364 READY tras (a) reautenticar Shopify y confirmar en vivo, (b) backup PS fresco. Decisión de Dirección sobre las 77 BLOCKED. Perfil de navegador `hablamos@barmet.es` no verificable en este entorno.

## Tabla de continuidad
| tarea | prioridad | estado | evidencias | cambios realizados | siguiente acción | riesgos | impacto en otras tareas |
|---|---|---|---|---|---|---|---|
| A INDICE | ALTA | PARCIAL (releído OK; addendum, sin edición en sitio) | idx 543 líneas | addendum | editar con escritura de contenido | índice sin entrada REP-009 | trazabilidad |
| B Matriz 441 | PRINCIPAL | HECHO | MATRIZ-441*.csv | 364 R / 77 B | decisión Dirección | precio vivo ≠ snapshot 23/10 | PVP Knock |
| C Reconciliación | PRINCIPAL | PARCIAL 441/1.953 | A1, A2, P006 | cruce 441 | reautenticar Shopify y cruzar 1.512 | `sh_*` no fiable | gate de compra |
| D Verificación | ALTA | HECHO | sha256, 441 ids únicos, Taupe∩=0 | — | — | — | — |

## ACTA DE ACEPTACIÓN PARA DIRECCIÓN
**Ejecución** · Orden completada: **PARCIAL** · Entregables verificados: 8/9 (falta edición de INDICE en sitio) · Índice actualizado y releído: **NO** (releído sí; addendum) · Escrituras en producción: **0** · Subagentes: **0**
**Resultado comercial** · Universo 441 · READY 364 · BLOCKED 77 · EXCLUDED 0 · Clasificado 441/441 · Taupe 87: 63/63 · Cruce: 441/1.953 · Discrepancias pendientes: 77 + 18 Nogal 25 + Blanco lacado 94 65 cm
**Dictamen: `APTO_PARA_AUTORIZACION_PARCIAL`**
Corregibles: las 364 READY (Arena 27, Cemento 89, Natural 12, Wengé 23 ×63; Nogal 25 ×57; Blanqueado 84 ×55) a 3.561,81 / 3.862,43 / 4.163,04 / 4.463,66 / 4.763,54 € s/IVA según 10–12/13/14/15/16 peldaños. Evidencia: E1. El dictamen no autoriza modificar producción.
