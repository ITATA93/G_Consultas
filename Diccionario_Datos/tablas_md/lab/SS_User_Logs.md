# lab.SS_User_Logs

**Schema:** lab
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Registro de eventos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SULG_ParRef | varchar | PK |  | NO | SS_User Parent Reference |
| SULG_Comment | varchar |  |  | SI | Comment |
| SULG_Date | date |  |  | SI | Date |
| SULG_Order | double |  |  | NO | Order |
| SULG_PCName | varchar |  |  | SI | PC name |
| SULG_RowID | varchar |  |  | NO | - |
| SULG_Time | time |  |  | SI | Time |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*