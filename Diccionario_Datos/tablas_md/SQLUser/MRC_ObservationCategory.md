# SQLUser.MRC_ObservationCategory

**Schema:** SQLUser
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CAT_RowId | bigint | PK |  | NO | - |
| CAT_Code | varchar |  |  | NO | Code |
| CAT_CodeTableTags | varchar |  |  | SI | Code Table Tags |
| CAT_CreatedDate | date |  |  | SI | Created Date |
| CAT_CreatedTime | time |  |  | SI | Created Time |
| CAT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CAT_DateFrom | date |  |  | SI | Date From |
| CAT_DateTo | date |  |  | SI | Date To |
| CAT_Desc | varchar |  |  | NO | Description |
| CAT_Owner | varchar |  |  | SI | Code Table Owner |
| CAT_UpdatedDate | date |  |  | SI | Updated Date |
| CAT_UpdatedTime | time |  |  | SI | Updated Time |
| CAT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q08Q1 | - |  |  | SI | Factores de Riesgo |
| Q08Q2 | - |  |  | SI | Factores Protectores |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*