# SQLUser.MRC_DiagnosisGroup1

**Schema:** SQLUser
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| GRP1_RowId | bigint | PK |  | NO | - |
| ChildQ86DR | - |  |  | SI | Child Reference: Actividades de la Vida Diaria y T... |
| GRP1_Code | varchar |  |  | NO | Code |
| GRP1_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| GRP1_CreatedDate | date |  |  | SI | Created Date |
| GRP1_CreatedTime | time |  |  | SI | Created Time |
| GRP1_CreatedUser_DR | bigint |  | FK | SI | Created User |
| GRP1_DateFrom | date |  |  | SI | Date From |
| GRP1_DateTo | date |  |  | SI | Date To |
| GRP1_Desc | varchar |  |  | NO | Description |
| GRP1_Owner | varchar |  |  | SI | Owner |
| GRP1_UpdatedDate | date |  |  | SI | Updated Date |
| GRP1_UpdatedTime | time |  |  | SI | Updated Time |
| GRP1_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| GRP1_UserDefWindow_DR | bigint |  | FK | SI | Des Ref UserDefWindow |
| Q83Q1 | - |  |  | SI | Evaluación |
| Q83Q2 | - |  |  | SI | Comentarios (Texto libre) |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*