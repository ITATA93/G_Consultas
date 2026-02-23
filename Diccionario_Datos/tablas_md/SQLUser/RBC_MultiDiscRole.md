# SQLUser.RBC_MultiDiscRole

**Schema:** SQLUser
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de RB**. Parámetros de módulos RB.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MDR_RowId | bigint | PK |  | NO | - |
| MDR_CareProvType_DR | bigint |  | FK | SI | Care Provider Type |
| MDR_Code | varchar |  |  | NO | Code |
| MDR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| MDR_CreatedDate | date |  |  | SI | Created Date |
| MDR_CreatedTime | time |  |  | SI | Created Time |
| MDR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MDR_DateFrom | date |  |  | SI | DateFrom |
| MDR_DateTo | date |  |  | SI | DateTo |
| MDR_Desc | varchar |  |  | NO | Description |
| MDR_Owner | varchar |  |  | SI | Owner |
| MDR_UpdatedDate | date |  |  | SI | Updated Date |
| MDR_UpdatedTime | time |  |  | SI | Updated Time |
| MDR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*