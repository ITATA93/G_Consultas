# SQLUser.LBC_StaffNotesType

**Schema:** SQLUser
**Columnas:** 21
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCSNT_RowID | bigint | PK |  | NO | - |
| ChildQ02DR | - |  |  | SI | Child Reference: Via Venosa Central |
| LBCSNT_Code | varchar |  |  | NO | LabCode |
| LBCSNT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCSNT_CreatedDate | date |  |  | SI | Created Date |
| LBCSNT_CreatedTime | time |  |  | SI | Created Time |
| LBCSNT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCSNT_DateFrom | date |  |  | SI | Effective date for the record |
| LBCSNT_DateTo | date |  |  | SI | Last day the record is active  |
| LBCSNT_Departments_DR | varchar |  | FK | SI | List of asscoiated Departments |
| LBCSNT_Desc | varchar |  |  | NO | Lab Name |
| LBCSNT_Owner | varchar |  |  | SI | Owner |
| LBCSNT_UpdatedDate | date |  |  | SI | Updated Date |
| LBCSNT_UpdatedTime | time |  |  | SI | Updated Time |
| LBCSNT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01Q1 | - |  |  | SI | Diámetro (#) |
| Q01Q2 | - |  |  | SI | Ubicación |
| Q01Q3 | - |  |  | SI | Complejidad |
| Q01Q4 | - |  |  | SI | Observación |
| Q01Q5 | - |  |  | SI | Lateralidad |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*