# lab.PSL_PackingSlip

**Schema:** lab
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PSL_RowID | varchar | PK |  | NO | - |
| PSL_Code | varchar |  |  | NO | Packing Slip Code |
| PSL_Destination | varchar |  |  | NO | Destination |
| PSL_FileCreated_Date | date |  |  | SI | File Created Date |
| PSL_FileCreated_Time | time |  |  | SI | File Created Time |
| PSL_FileCreated_User_DR | varchar |  | FK | SI | File Created User DR |
| PSL_ReportPrinted_Date | date |  |  | SI | Report Printed Date |
| PSL_ReportPrinted_Time | time |  |  | SI | Report Printed Time |
| PSL_ReportPrinted_User_DR | varchar |  | FK | SI | Report Printed User |
| PSL_Sender_DR | varchar |  | FK | NO | User Site From DR |
| PSL_ToType | varchar |  |  | NO | To Type |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*