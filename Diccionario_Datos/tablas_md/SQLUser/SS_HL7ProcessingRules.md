# SQLUser.SS_HL7ProcessingRules

**Schema:** SQLUser
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HL7PR_ParRef | varchar | PK |  | NO | SS_HL7 Parent Reference |
| HL7PR_Count | double |  |  | NO | Rule Count - Always 1 |
| HL7PR_DischSumNotRequired | varchar |  |  | SI | ADT^A03 Discharge summary not required |
| HL7PR_FileSTResultComments | varchar |  |  | SI | File ST Results as Comments |
| HL7PR_MatchOnUROnly | varchar |  |  | SI | Match patient for result/order on UR only |
| HL7PR_OverseasAddPermAdd | varchar |  |  | SI | Overseas address classed as permanent address |
| HL7PR_OverseasAddType | bigint |  |  | SI | Overseas address type |
| HL7PR_PreviousPermAddType | bigint |  |  | SI | Previous permanent address type |
| HL7PR_ReplaceInvalidDayMonth | varchar |  |  | SI | ReplaceInvalidDayMonth |
| HL7PR_RowId | varchar |  |  | NO | - |
| HL7PR_SavePermAddPrevPerm | varchar |  |  | SI | Save permanent address as previous permanent |
| HL7PR_SendReceivePatTitleDesc | varchar |  |  | SI | Send or Receive Patient Title Description |
| HL7PR_SuppressADTA28 | varchar |  |  | SI | Suppress ADT_A28 unless national id required |
| HL7PR_TempAddEndDelete | varchar |  |  | SI | End date or delete temporary address |
| HL7PR_TempAddFromDate | varchar |  |  | SI | Temporary address from date |
| HL7PR_UpdateDateTime | varchar |  |  | SI | Use EVN fields or current date/time |
| HL7PR_UpperExtCodes | varchar |  |  | SI | Convert received external order item code to upper... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*