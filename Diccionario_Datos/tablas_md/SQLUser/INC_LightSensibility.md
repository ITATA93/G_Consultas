# SQLUser.INC_LightSensibility

**Schema:** SQLUser
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Incidentes**. Reportes de eventos adversos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LTSEN_RowId | bigint | PK |  | NO | - |
| LTSEN_Code | varchar |  |  | NO | Code |
| LTSEN_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LTSEN_CreatedDate | date |  |  | SI | Created Date |
| LTSEN_CreatedTime | time |  |  | SI | Created Time |
| LTSEN_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LTSEN_DateFrom | date |  |  | SI | Date From |
| LTSEN_DateTo | date |  |  | SI | Date To |
| LTSEN_Desc | varchar |  |  | NO | Description |
| LTSEN_Owner | varchar |  |  | SI | Owner |
| LTSEN_UpdatedDate | date |  |  | SI | Updated Date |
| LTSEN_UpdatedTime | time |  |  | SI | Updated Time |
| LTSEN_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q146Q1 | - |  |  | SI | Infusión |
| Q146Q2 | - |  |  | SI | Velocidad |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*