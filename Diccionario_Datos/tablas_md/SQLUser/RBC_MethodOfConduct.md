# SQLUser.RBC_MethodOfConduct

**Schema:** SQLUser
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de RB**. Parámetros de módulos RB.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MOC_RowId | bigint | PK |  | NO | - |
| MOC_Code | varchar |  |  | NO | Code |
| MOC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| MOC_CreatedDate | date |  |  | SI | Created Date |
| MOC_CreatedTime | time |  |  | SI | Created Time |
| MOC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MOC_Desc | varchar |  |  | NO | Description |
| MOC_Owner | varchar |  |  | SI | Owner |
| MOC_UpdatedDate | date |  |  | SI | Updated Date |
| MOC_UpdatedTime | time |  |  | SI | Updated Time |
| MOC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*