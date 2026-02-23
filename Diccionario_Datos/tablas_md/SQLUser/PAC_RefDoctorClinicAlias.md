# SQLUser.PAC_RefDoctorClinicAlias

**Schema:** SQLUser
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ALIAS_ParRef | varchar | PK |  | NO | PAC_RefDoctorClinic Parent Reference |
| ALIAS_Childsub | double |  |  | NO | Childsub |
| ALIAS_CreatedDate | date |  |  | SI | Created Date |
| ALIAS_CreatedTime | time |  |  | SI | Created Time |
| ALIAS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ALIAS_DefaultSend | varchar |  |  | SI | Default Send |
| ALIAS_LocationCode | bigint |  |  | SI | LOcation Code |
| ALIAS_RowId | varchar |  |  | NO | - |
| ALIAS_System | bigint |  |  | SI | System |
| ALIAS_SystemText | varchar |  |  | SI | System Text |
| ALIAS_Text | varchar |  |  | SI | Text |
| ALIAS_UpdatedDate | date |  |  | SI | Updated Date |
| ALIAS_UpdatedTime | time |  |  | SI | Updated Time |
| ALIAS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q38Q1 | - |  |  | SI | Meal type |
| Q38Q2 | - |  |  | SI | Amount |
| Q38Q3 | - |  |  | SI | Any problems eating or swallowing? |
| Q38Q4 | - |  |  | SI | Notes |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*