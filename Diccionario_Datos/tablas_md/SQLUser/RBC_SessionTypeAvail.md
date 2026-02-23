# SQLUser.RBC_SessionTypeAvail

**Schema:** SQLUser
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| AVL_ParRef | bigint | PK |  | NO | RBC_SessionType Parent Reference |
| AVL_Childsub | double |  |  | NO | Childsub |
| AVL_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| AVL_ConversionRules | varchar |  |  | SI | ConversionRules |
| AVL_CreatedDate | date |  |  | SI | Created Date |
| AVL_CreatedTime | time |  |  | SI | Created Time |
| AVL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| AVL_DOW_DR | double |  | FK | SI | Des Ref DOW |
| AVL_DateFrom | date |  |  | SI | Date From |
| AVL_DateTo | date |  |  | SI | Date To |
| AVL_GenerateOnDay | varchar |  |  | SI | Generate On Day |
| AVL_GenerateUntilDay | varchar |  |  | SI | Generate Until Day |
| AVL_NumberOfMonths | double |  |  | SI | Number Of Months |
| AVL_ReleaseDays | double |  |  | SI | ReleaseDays |
| AVL_ReleaseTime | time |  |  | SI | ReleaseTime |
| AVL_RowId | varchar |  |  | NO | - |
| AVL_ServiceGroup_DR | bigint |  | FK | SI | Des Ref ServiceGroup |
| AVL_UpdatedDate | date |  |  | SI | Updated Date |
| AVL_UpdatedTime | time |  |  | SI | Updated Time |
| AVL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*