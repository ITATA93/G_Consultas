# lab.CT_CourierSchedule

**Schema:** lab
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTCRS_ParRef | varchar | PK |  | NO | CT_Courier Parent Reference |
| CTCRS_RowID | varchar |  |  | NO | - |
| CTCRS_Sequence | double |  |  | NO | Sequence |
| CTCRS_TimeEnd | time |  |  | SI | Time End |
| CTCRS_TimeStart | time |  |  | SI | Time Start |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*