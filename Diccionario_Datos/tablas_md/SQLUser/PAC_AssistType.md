# SQLUser.PAC_AssistType

**Schema:** SQLUser
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ASST_RowId | bigint | PK |  | NO | - |
| ASST_Code | varchar |  |  | NO | Code |
| ASST_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ASST_CreatedDate | date |  |  | SI | Created Date |
| ASST_CreatedTime | time |  |  | SI | Created Time |
| ASST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ASST_DateFrom | date |  |  | SI | Date From |
| ASST_DateTo | date |  |  | SI | Date To |
| ASST_Desc | varchar |  |  | NO | Description |
| ASST_Owner | varchar |  |  | SI | Owner |
| ASST_UpdatedDate | date |  |  | SI | Updated Date |
| ASST_UpdatedTime | time |  |  | SI | Updated Time |
| ASST_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q13Q1 | - |  |  | SI | Lead used |
| Q13Q2 | - |  |  | SI | Pacing threshold (mv)	 |
| Q13Q3 | - |  |  | SI | Sensing threshold (mv)	 |
| Q13Q4 | - |  |  | SI | Lead impedance (ohm)	 |
| Q13Q5 | - |  |  | SI | Shock impedance used (ohm)	 |
| Q13Q6 | - |  |  | SI | At last shock (mv)	 |
| Q13Q7 | - |  |  | SI | Low energy (mv)	 |
| Q13Q8 | - |  |  | SI | Sense / pace issues	 |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*