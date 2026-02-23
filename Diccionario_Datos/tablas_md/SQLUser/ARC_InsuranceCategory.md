# SQLUser.ARC_InsuranceCategory

**Schema:** SQLUser
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Seguros**. Planes y convenios.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INSC_RowId | bigint | PK |  | NO | - |
| INSC_Code | varchar |  |  | NO | Code |
| INSC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| INSC_CreatedDate | date |  |  | SI | Created Date |
| INSC_CreatedTime | time |  |  | SI | Created Time |
| INSC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| INSC_Desc | varchar |  |  | NO | Description |
| INSC_Owner | varchar |  |  | SI | Owner |
| INSC_UpdatedDate | date |  |  | SI | Updated Date |
| INSC_UpdatedTime | time |  |  | SI | Updated Time |
| INSC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q85Q1 | - |  |  | SI | Características |
| Q85Q2 | - |  |  | SI | Evaluación |
| Q85Q3 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*