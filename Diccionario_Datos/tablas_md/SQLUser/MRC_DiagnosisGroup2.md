# SQLUser.MRC_DiagnosisGroup2

**Schema:** SQLUser
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| GRP2_RowId | bigint | PK |  | NO | - |
| ChildQ87DR | - |  |  | SI | Child Reference: Hipótesis Diagnóstica (Ejes) |
| GRP2_Code | varchar |  |  | NO | Code |
| GRP2_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| GRP2_CreatedDate | date |  |  | SI | Created Date |
| GRP2_CreatedTime | time |  |  | SI | Created Time |
| GRP2_CreatedUser_DR | bigint |  | FK | SI | Created User |
| GRP2_Desc | varchar |  |  | NO | Description |
| GRP2_Owner | varchar |  |  | SI | Owner |
| GRP2_UpdatedDate | date |  |  | SI | Updated Date |
| GRP2_UpdatedTime | time |  |  | SI | Updated Time |
| GRP2_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q86Q1 | - |  |  | SI | Evaluación |
| Q86Q2 | - |  |  | SI | Comentarios (Texto libre) |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*