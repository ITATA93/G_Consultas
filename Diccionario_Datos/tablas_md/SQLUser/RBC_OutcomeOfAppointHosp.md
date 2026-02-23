# SQLUser.RBC_OutcomeOfAppointHosp

**Schema:** SQLUser
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de RB**. Parámetros de módulos RB.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HOSP_ParRef | bigint | PK |  | NO | RBC_OutcomeOfAppoint Parent Reference |
| HOSP_Childsub | double |  |  | NO | Childsub |
| HOSP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| HOSP_CreatedDate | date |  |  | SI | Created Date |
| HOSP_CreatedTime | time |  |  | SI | Created Time |
| HOSP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| HOSP_Hosp_DR | bigint |  | FK | SI | Des Ref CTLoc |
| HOSP_RowId | varchar |  |  | NO | - |
| HOSP_UpdatedDate | date |  |  | SI | Updated Date |
| HOSP_UpdatedTime | time |  |  | SI | Updated Time |
| HOSP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*