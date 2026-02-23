# SQLUser.MRC_BodyArea

**Schema:** SQLUser
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BODAR_RowId | bigint | PK |  | NO | - |
| BODAR_CTLOC_DR | bigint |  | FK | SI | Des Ref to CTLOC |
| BODAR_Code | varchar |  |  | NO | Code |
| BODAR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| BODAR_CreatedDate | date |  |  | SI | Created Date |
| BODAR_CreatedTime | time |  |  | SI | Created Time |
| BODAR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| BODAR_DateFrom | date |  |  | SI | Date From |
| BODAR_DateTo | date |  |  | SI | Date To |
| BODAR_Desc | varchar |  |  | NO | Description |
| BODAR_Owner | varchar |  |  | SI | Owner |
| BODAR_UpdatedDate | date |  |  | SI | Updated Date |
| BODAR_UpdatedTime | time |  |  | SI | Updated Time |
| BODAR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ46DR | - |  |  | SI | Child Reference: Lesiones cutáneas |
| Q127Q1 | - |  |  | SI | Acciones preventivas |
| Q127Q2 | - |  |  | SI | Situación |
| Q127Q3 | - |  |  | SI | Comentario |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*