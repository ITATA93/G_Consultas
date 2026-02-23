# SQLUser.PHC_PBSPrescribingRule

**Schema:** SQLUser
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PBSRUL_RowId | bigint | PK |  | NO | - |
| PBSRUL_Code | varchar |  |  | NO | The unique code assigned to this PBS pharmaceutica... |
| PBSRUL_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PBSRUL_CreatedDate | date |  |  | SI | Created Date |
| PBSRUL_CreatedTime | time |  |  | SI | Created Time |
| PBSRUL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PBSRUL_DateFrom | date |  |  | SI | Date From |
| PBSRUL_DateTo | date |  |  | SI | Date To |
| PBSRUL_Desc | varchar |  |  | NO | The unique description assigned to this PBS pharma... |
| PBSRUL_DispensingRuleList | varchar |  |  | SI | List of Dispensing Rules  |
| PBSRUL_MaxQuantity | double |  |  | SI | Maximum allowed quantity or amount to be prescribe... |
| PBSRUL_MaxRepeats | integer |  |  | SI | Maximum allowed number of repeats for a prescripti... |
| PBSRUL_MaximumQuantityUnit | varchar |  |  | SI | The unit of measure the maximum quantity is expres... |
| PBSRUL_MedicationDesc | varchar |  |  | NO | The pharmaceutical description associated with the... |
| PBSRUL_Owner | varchar |  |  | SI | Owner |
| PBSRUL_Program_DR | varchar |  | FK | SI | The PBS Benefit program this PBS Item belongs to |
| PBSRUL_UpdatedDate | date |  |  | SI | Updated Date |
| PBSRUL_UpdatedTime | time |  |  | SI | Updated Time |
| PBSRUL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*