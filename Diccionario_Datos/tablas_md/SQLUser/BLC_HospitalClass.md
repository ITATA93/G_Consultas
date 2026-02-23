# SQLUser.BLC_HospitalClass

**Schema:** SQLUser
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Banco de Sangre**. Gestión de hemoderivados.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HOSCL_RowId | bigint | PK |  | NO | - |
| ChildQ18DR | - |  |  | SI | Child Reference: Tratamiento Farmacológico |
| HOSCL_Code | varchar |  |  | NO | Code |
| HOSCL_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| HOSCL_CreatedDate | date |  |  | SI | Created Date |
| HOSCL_CreatedTime | time |  |  | SI | Created Time |
| HOSCL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| HOSCL_Desc | varchar |  |  | NO | Description |
| HOSCL_Owner | varchar |  |  | SI | Owner |
| HOSCL_UpdatedDate | date |  |  | SI | Updated Date |
| HOSCL_UpdatedTime | time |  |  | SI | Updated Time |
| HOSCL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q17Q1 | - |  |  | SI | Fecha |
| Q17Q2 | - |  |  | SI | Modificación |
| Q17Q3 | - |  |  | SI | Página |
| Q17Q4 | - |  |  | SI | Aprobado por |
| Q17Q5 | - |  |  | SI | Firma Responsable |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*