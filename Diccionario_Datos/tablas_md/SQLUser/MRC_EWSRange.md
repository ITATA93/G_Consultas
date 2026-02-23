# SQLUser.MRC_EWSRange

**Schema:** SQLUser
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EWS_RowId | bigint | PK |  | NO | - |
| ChildQ20DR | - |  |  | SI | Child Reference: Desarrollo Psicomotor |
| EWS_Code | varchar |  |  | SI | Code |
| EWS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| EWS_Colour | varchar |  |  | SI | Colour  |
| EWS_CreatedDate | date |  |  | SI | Created Date |
| EWS_CreatedTime | time |  |  | SI | Created Time |
| EWS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| EWS_DateFrom | date |  |  | SI | Date From |
| EWS_DateTo | date |  |  | SI | Date To |
| EWS_Desc | varchar |  |  | SI | Description |
| EWS_Owner | varchar |  |  | SI | Owner |
| EWS_Score | double |  |  | SI | Score |
| EWS_System | varchar |  |  | SI | System created |
| EWS_UpdatedDate | date |  |  | SI | Updated Date |
| EWS_UpdatedTime | time |  |  | SI | Updated Time |
| EWS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q13Q1 | - |  |  | SI | Área |
| Q13Q2 | - |  |  | SI | Comentarios (Texto libre): |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*