# SQLUser.MRC_EmergencyCondition

**Schema:** SQLUser
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EMC_RowId | bigint | PK |  | NO | - |
| ChildQ55DR | - |  |  | SI | Child Reference: Piel |
| EMC_Code | varchar |  |  | NO | Code |
| EMC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| EMC_CreatedDate | date |  |  | SI | Created Date |
| EMC_CreatedTime | time |  |  | SI | Created Time |
| EMC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| EMC_DateFrom | date |  |  | SI | Date From |
| EMC_DateTo | date |  |  | SI | Date To |
| EMC_Desc | varchar |  |  | NO | Description |
| EMC_IconName | varchar |  |  | SI | Icon Name |
| EMC_IconPriority | varchar |  |  | SI | Icon Priority |
| EMC_Owner | varchar |  |  | SI | Owner |
| EMC_UpdatedDate | date |  |  | SI | Updated Date |
| EMC_UpdatedTime | time |  |  | SI | Updated Time |
| EMC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q39Q1 | - |  |  | SI | Área |
| Q39Q2 | - |  |  | SI | Orientación |
| Q39Q3 | - |  |  | SI | Comentarios (Texto libre) |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*