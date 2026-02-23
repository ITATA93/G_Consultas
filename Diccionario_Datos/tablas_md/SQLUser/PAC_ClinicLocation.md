# SQLUser.PAC_ClinicLocation

**Schema:** SQLUser
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CLNLOC_ParRef | bigint | PK |  | NO | PAC_Clinic Parent Reference |
| CLNLOC_Childsub | double |  |  | NO | Childsub |
| CLNLOC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CLNLOC_CreatedDate | date |  |  | SI | Created Date |
| CLNLOC_CreatedTime | time |  |  | SI | Created Time |
| CLNLOC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CLNLOC_DateFrom | date |  |  | SI | Date From |
| CLNLOC_DateTo | date |  |  | SI | Date to |
| CLNLOC_Location_DR | bigint |  | FK | SI | Des Ref Location |
| CLNLOC_RowID | varchar |  |  | NO | - |
| CLNLOC_UpdatedDate | date |  |  | SI | Updated Date |
| CLNLOC_UpdatedTime | time |  |  | SI | Updated Time |
| CLNLOC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q19Q1 | - |  |  | SI | Other symptom |
| Q19Q2 | - |  |  | SI | Other symptom - response |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*