# lab.SS_GroupVerificationQueue

**Schema:** lab
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SSGRC_ParRef | bigint | PK |  | NO | SS_Group Parent Reference |
| SSGRC_Printable | varchar |  |  | SI | Printable |
| SSGRC_Queue_DR | varchar |  | FK | NO | Queue DR |
| SSGRC_RowID | varchar |  |  | NO | - |
| SSGRC_Viewable | varchar |  |  | SI | Viewable |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*