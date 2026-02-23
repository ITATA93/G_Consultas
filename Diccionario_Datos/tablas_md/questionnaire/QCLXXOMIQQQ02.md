# questionnaire.QCLXXOMIQQQ02

> Orden Médica de Ingreso Quirúrgico : Registro de Insumos Especiales

**Schema:** questionnaire
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Orden Médica de Ingreso Quirúrgico : Registro de Insumos Especiales

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q02Q1 | varchar |  |  | SI | Insumo |
| Q02Q2 | varchar |  |  | SI | Proveedor |
| Q02Q3 | numeric |  |  | SI | Cantidad |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*