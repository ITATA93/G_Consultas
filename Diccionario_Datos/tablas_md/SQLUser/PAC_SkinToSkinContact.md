# SQLUser.PAC_SkinToSkinContact

**Schema:** SQLUser
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| STSC_RowId | bigint | PK |  | NO | - |
| Q62Q1 | - |  |  | SI | Side |
| Q62Q2 | - |  |  | SI | Range of motion |
| Q62Q3 | - |  |  | SI | Frequency |
| Q62Q4 | - |  |  | SI | Duration |
| Q62Q5 | - |  |  | SI | Comment |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| STSC_Code | varchar |  |  | NO | Code |
| STSC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| STSC_CreatedDate | date |  |  | SI | Created Date |
| STSC_CreatedTime | time |  |  | SI | Created Time |
| STSC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| STSC_DateFrom | date |  |  | SI | Date From |
| STSC_DateTo | date |  |  | SI | Date To |
| STSC_Desc | varchar |  |  | NO | Desc |
| STSC_Owner | varchar |  |  | SI | Owner |
| STSC_UpdatedDate | date |  |  | SI | Updated Date |
| STSC_UpdatedTime | time |  |  | SI | Updated Time |
| STSC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*