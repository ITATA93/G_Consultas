# lab.SS_User_VerificationQueue

**Schema:** lab
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SUVQ_ParRef | varchar | PK |  | NO | SS_User Parent Reference |
| SUVQ_Printable | varchar |  |  | SI | Printable |
| SUVQ_Queue_DR | varchar |  | FK | NO | Queue DR |
| SUVQ_RowID | varchar |  |  | NO | - |
| SUVQ_Viewable | varchar |  |  | SI | Viewable |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*