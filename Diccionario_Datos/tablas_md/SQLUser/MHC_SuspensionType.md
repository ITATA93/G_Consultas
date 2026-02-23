# SQLUser.MHC_SuspensionType

**Schema:** SQLUser
**Columnas:** 29
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MHCST_RowId | bigint | PK |  | NO | - |
| MHCST_Code | varchar |  |  | NO | Code |
| MHCST_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| MHCST_CreatedDate | date |  |  | SI | Created Date |
| MHCST_CreatedTime | time |  |  | SI | Created Time |
| MHCST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MHCST_DateFrom | date |  |  | SI | Date From |
| MHCST_DateTo | date |  |  | SI | Date To |
| MHCST_Desc | varchar |  |  | NO | Description |
| MHCST_GrantsFreeToGo | varchar |  |  | SI | GrantsFreeToGo |
| MHCST_MaxDurationDays | double |  |  | SI | MaxDuration |
| MHCST_MaxDurationUnits | varchar |  |  | SI | MaxDurationUnits |
| MHCST_MinDurationDays | double |  |  | SI | MinDurationDays |
| MHCST_MinDurationUnits | varchar |  |  | SI | RemindOffsetDays
MinDurationUnits |
| MHCST_Owner | varchar |  |  | SI | Owner |
| MHCST_UpdatedDate | date |  |  | SI | Updated Date |
| MHCST_UpdatedTime | time |  |  | SI | Updated Time |
| MHCST_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q109Q1 | - |  |  | SI | Factores Protectores |
| Q109Q10 | - |  |  | SI | CESFAM |
| Q109Q2 | - |  |  | SI | Factores de Riesgo Mayor |
| Q109Q3 | - |  |  | SI | Factores de Riesgo Intermedio |
| Q109Q4 | - |  |  | SI | Factores de Riesgo Bajo |
| Q109Q5 | - |  |  | SI | Riesgo Familiar |
| Q109Q6 | - |  |  | SI | Comentarios |
| Q109Q7 | - |  |  | SI | Fecha |
| Q109Q8 | - |  |  | SI | Hora |
| Q109Q9 | - |  |  | SI | Profesional |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*