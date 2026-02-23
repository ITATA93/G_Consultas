# SQLUser.GL_Batch

**Schema:** SQLUser
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Contabilidad General (GL)**. Libro mayor y asientos contables.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| GLB_RowId | bigint | PK |  | NO | - |
| ChildQ49DR | - |  |  | SI | Child Reference: Drainage assessment |
| GLB_Date | date |  |  | SI | Date |
| GLB_DateFrom | date |  |  | SI | Date From |
| GLB_DateTo | date |  |  | SI | Date To |
| GLB_Number | varchar |  |  | SI | Batch Number |
| GLB_Time | time |  |  | SI | Time |
| GLB_User_DR | bigint |  | FK | SI | Des Ref User |
| Q48Q1 | - |  |  | SI | Line status |
| Q48Q2 | - |  |  | SI | Site condition |
| Q48Q3 | - |  |  | SI | Dressing |
| Q48Q4 | - |  |  | SI | Care |
| Q48Q5 | - |  |  | SI | Limb temperature |
| Q48Q6 | - |  |  | SI | Pulse distal to insertion site |
| Q48Q7 | - |  |  | SI | Assessment date and time |
| Q48Q8 | - |  |  | SI | Assessment time |
| Q48Q9 | - |  |  | SI | Assessing care provider |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*