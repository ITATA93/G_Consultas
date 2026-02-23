# SQLUser.OEC_SchemaPreference

**Schema:** SQLUser
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Entry Orders**. Tipos y estados de órdenes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SCPREF_RowId | bigint | PK |  | NO | - |
| Q99Q1 | - |  |  | SI | Care provider |
| Q99Q2 | - |  |  | SI | Care provider type |
| Q99Q3 | - |  |  | SI | Medical emergency team role |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| SCPREF_CreatedDate | date |  |  | SI | Created Date |
| SCPREF_CreatedTime | time |  |  | SI | Created Time |
| SCPREF_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SCPREF_Filters | varchar |  |  | SI | - |
| SCPREF_ReferenceType | varchar |  |  | NO | - |
| SCPREF_Summary | varchar |  |  | SI | Summary |
| SCPREF_UpdatedDate | date |  |  | SI | Updated Date |
| SCPREF_UpdatedTime | time |  |  | SI | Updated Time |
| SCPREF_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*