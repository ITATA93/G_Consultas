# SQLUser.ORC_OtherAnaestheticTechniques

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OTANTE_Code | varchar | PK |  | NO | Code |
| OTANTE_CodeTableTags | varchar | PK |  | SI | List of code table Tags |
| OTANTE_CreatedDate | date | PK |  | SI | Created Date |
| OTANTE_CreatedTime | time | PK |  | SI | Created Time |
| OTANTE_CreatedUser_DR | bigint | PK | FK | SI | Created User |
| OTANTE_DateFrom | date | PK |  | SI | Date From |
| OTANTE_DateTo | date | PK |  | SI | Date To |
| OTANTE_Desc | varchar | PK |  | NO | Description |
| OTANTE_Owner | varchar | PK |  | SI | Owner |
| OTANTE_RowId | bigint | PK |  | NO | - |
| OTANTE_UpdatedDate | date | PK |  | SI | Updated Date |
| OTANTE_UpdatedTime | time | PK |  | SI | Updated Time |
| OTANTE_UpdatedUser_DR | bigint | PK | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*