# SQLUser.ORC_OperTheatreType

**Schema:** SQLUser
**Columnas:** 25
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OTTYPE_RowId | bigint | PK |  | NO | - |
| ChildQ12DR | - |  |  | SI | Child Reference: Post Dobutamine Infusion |
| OTTYPE_Code | varchar |  |  | NO | Code |
| OTTYPE_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| OTTYPE_CreatedDate | date |  |  | SI | Created Date |
| OTTYPE_CreatedTime | time |  |  | SI | Created Time |
| OTTYPE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| OTTYPE_DateFrom | date |  |  | SI | Date From |
| OTTYPE_DateTo | date |  |  | SI | Date To |
| OTTYPE_Desc | varchar |  |  | NO | Description |
| OTTYPE_Owner | varchar |  |  | SI | Owner |
| OTTYPE_UpdatedDate | date |  |  | SI | Updated Date |
| OTTYPE_UpdatedTime | time |  |  | SI | Updated Time |
| OTTYPE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q11Q1 | - |  |  | SI | Time |
| Q11Q10 | - |  |  | SI | Medication given during testing |
| Q11Q2 | - |  |  | SI | Dobutamine (mcg/kg/min) |
| Q11Q3 | - |  |  | SI | Rate (microdrop/min) |
| Q11Q4 | - |  |  | SI | Heart rate (/min) |
| Q11Q5 | - |  |  | SI | Systolic BP (mmHg) |
| Q11Q6 | - |  |  | SI | Diastolic BP (mmHg) |
| Q11Q7 | - |  |  | SI | ECG result |
| Q11Q8 | - |  |  | SI | Patient symptoms |
| Q11Q9 | - |  |  | SI | Other details |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*