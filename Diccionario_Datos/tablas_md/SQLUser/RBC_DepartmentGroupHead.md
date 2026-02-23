# SQLUser.RBC_DepartmentGroupHead

**Schema:** SQLUser
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de RB**. Parámetros de módulos RB.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CP_ParRef | bigint | PK |  | NO | RBC_DepartmentGroup Parent Reference |
| CP_CareProv_DR | varchar |  | FK | SI | Des REf CareProv |
| CP_Childsub | double |  |  | NO | Childsub |
| CP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CP_CreatedDate | date |  |  | SI | Created Date |
| CP_CreatedTime | time |  |  | SI | Created Time |
| CP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CP_DateFrom | date |  |  | SI | Date From |
| CP_DateTo | date |  |  | SI | Date To |
| CP_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| CP_RowId | varchar |  |  | NO | - |
| CP_UpdatedDate | date |  |  | SI | Updated Date |
| CP_UpdatedTime | time |  |  | SI | Updated Time |
| CP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*