# SQLUser.PAC_BroadPatientGroup

**Schema:** SQLUser
**Columnas:** 23
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BPG_RowId | bigint | PK |  | NO | - |
| BPG_Code | varchar |  |  | NO | Code |
| BPG_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| BPG_CreatedDate | date |  |  | SI | Created Date |
| BPG_CreatedTime | time |  |  | SI | Created Time |
| BPG_CreatedUser_DR | bigint |  | FK | SI | Created User |
| BPG_DateFrom | date |  |  | SI | DateFrom |
| BPG_DateTo | date |  |  | SI | DateTo |
| BPG_Desc | varchar |  |  | NO | Description |
| BPG_Owner | varchar |  |  | SI | Owner |
| BPG_UpdatedDate | date |  |  | SI | Updated Date |
| BPG_UpdatedTime | time |  |  | SI | Updated Time |
| BPG_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q18Q1 | - |  |  | SI | Date / Time |
| Q18Q2 | - |  |  | SI | Time |
| Q18Q3 | - |  |  | SI | Method |
| Q18Q4 | - |  |  | SI | Type of balloon catheter |
| Q18Q5 | - |  |  | SI | Volume inserted into balloon catheter (ml) |
| Q18Q6 | - |  |  | SI | Time for removal / reassessment |
| Q18Q7 | - |  |  | SI | Notes |
| Q18Q8 | - |  |  | SI | Care provider |
| Q18Q9 | - |  |  | SI | Date / Time for removal / reassessment |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*