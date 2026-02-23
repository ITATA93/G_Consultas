# SQLUser.PHC_PBSPrescriberInstruction

**Schema:** SQLUser
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PBSPIN_RowId | bigint | PK |  | NO | - |
| PBSPIN_Code | varchar |  |  | NO | The PBS unique code for a legally binding note to ... |
| PBSPIN_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PBSPIN_CreatedDate | date |  |  | SI | Created Date |
| PBSPIN_CreatedTime | time |  |  | SI | Created Time |
| PBSPIN_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PBSPIN_DateFrom | date |  |  | SI | Date From |
| PBSPIN_DateTo | date |  |  | SI | Date To |
| PBSPIN_Desc | varchar |  |  | NO | Description of the prescriber instruction |
| PBSPIN_Owner | varchar |  |  | SI | Owner |
| PBSPIN_Text | varchar |  |  | NO | Textual representation of the prescriber instructi... |
| PBSPIN_UpdatedDate | date |  |  | SI | Updated Date |
| PBSPIN_UpdatedTime | time |  |  | SI | Updated Time |
| PBSPIN_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*