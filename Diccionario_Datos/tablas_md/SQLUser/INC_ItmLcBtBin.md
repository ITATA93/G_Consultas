# SQLUser.INC_ItmLcBtBin

**Schema:** SQLUser
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Incidentes**. Reportes de eventos adversos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BIN_ParRef | varchar | PK |  | NO | Par Ref |
| BIN_ChildSub | numeric |  |  | NO | ChildSub |
| BIN_CreatedDate | date |  |  | SI | Created Date |
| BIN_CreatedTime | time |  |  | SI | Created Time |
| BIN_CreatedUser_DR | bigint |  | FK | SI | Created User |
| BIN_PhyQty | double |  |  | NO | Physical Quantity  |
| BIN_RowId | varchar |  |  | NO | - |
| BIN_StorageBin_DR | varchar |  | FK | NO | Des Ref to CTLocStorageBin |
| BIN_UpdatedDate | date |  |  | SI | Updated Date |
| BIN_UpdatedTime | time |  |  | SI | Updated Time |
| BIN_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ68DR | - |  |  | SI | Child Reference: Movement Loss / Muscle Power |
| Q70Q1 | - |  |  | SI | Pretest Symptoms Sitting |
| Q70Q2 | - |  |  | SI | Pretest Symptoms Lying |
| Q70Q3 | - |  |  | SI | If required pretest symptoms |
| Q70Q4 | - |  |  | SI | Symptoms During Testing |
| Q70Q5 | - |  |  | SI | Symptoms After Testing |
| Q70Q6 | - |  |  | SI | Mechanical Response |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*