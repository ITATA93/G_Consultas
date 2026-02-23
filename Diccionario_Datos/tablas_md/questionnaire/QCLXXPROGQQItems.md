# questionnaire.QCLXXPROGQQItems

> Programas Kinesiología : Detalle Items por Sesion

**Schema:** questionnaire
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

*Descripción original:* Programas Kinesiología : Detalle Items por Sesion

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| QCantidad | numeric |  |  | SI | N° de Sesiones |
| QCita | varchar |  |  | SI | Id Cita Asociada |
| QDetPago | varchar |  |  | SI | Detalle Pago |
| QEstadoSesion | varchar |  |  | SI | Estado de la Sesión |
| QOrdItem | varchar |  |  | SI | Item de Orden |
| QPrestDist | varchar |  |  | SI | Prestación por Sesión |
| QPrestacion | varchar |  |  | SI | Prestación Individual |
| QSelect | bit |  |  | SI | Select |
| QSesion | varchar |  |  | SI | Sesión |
| QSetOrden | varchar |  |  | SI | Set de Orden por Sesión |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*