# lab.AU_AuditableTablesRecords

**Schema:** lab
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Auditoría de modificaciones.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| AUTR_ParRef | double | PK |  | NO | AU_AuditableTables Parent Reference |
| AUTR_Action | varchar |  |  | SI | Action |
| AUTR_Comment | varchar |  |  | SI | Comment |
| AUTR_DataNew | varchar |  |  | SI | New Data |
| AUTR_DataOld | varchar |  |  | SI | Old Data |
| AUTR_Date | date |  |  | SI | Date |
| AUTR_OrderNumber | double |  |  | NO | Order Number |
| AUTR_RowID | varchar |  |  | NO | - |
| AUTR_TableID_DR | double |  | FK | SI | Table ID |
| AUTR_Time | time |  |  | SI | Time |
| AUTR_User_DR | varchar |  | FK | SI | User DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*