# SQLUser.PHC_PBSTreatmentPhase

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PBSTPH_RowId | bigint | PK |  | NO | - |
| PBSTPH_Code | varchar |  |  | NO | The PBS unique code for a phase of treatment for t... |
| PBSTPH_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PBSTPH_CreatedDate | date |  |  | SI | Created Date |
| PBSTPH_CreatedTime | time |  |  | SI | Created Time |
| PBSTPH_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PBSTPH_DateFrom | date |  |  | SI | Date From |
| PBSTPH_DateTo | date |  |  | SI | Date To |
| PBSTPH_Desc | varchar |  |  | NO | The textual description of the phase of treatment |
| PBSTPH_Owner | varchar |  |  | SI | Owner |
| PBSTPH_UpdatedDate | date |  |  | SI | Updated Date |
| PBSTPH_UpdatedTime | time |  |  | SI | Updated Time |
| PBSTPH_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*