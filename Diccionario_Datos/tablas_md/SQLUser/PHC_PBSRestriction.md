# SQLUser.PHC_PBSRestriction

**Schema:** SQLUser
**Columnas:** 21
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PBSRES_RowId | bigint | PK |  | NO | - |
| PBSRES_AdministrativeAdviceList | varchar |  |  | SI | A list of PBS unique code for the non-legally bind... |
| PBSRES_CautionList | varchar |  |  | SI | A list of PBS unique code for the caution that app... |
| PBSRES_Code | varchar |  |  | NO | Code |
| PBSRES_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PBSRES_CreatedDate | date |  |  | SI | Created Date |
| PBSRES_CreatedTime | time |  |  | SI | Created Time |
| PBSRES_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PBSRES_DateFrom | date |  |  | SI | Date From |
| PBSRES_DateTo | date |  |  | SI | Date To |
| PBSRES_DefinitionList | varchar |  |  | SI | A list of PBS unique code for the definition that ... |
| PBSRES_Desc | varchar |  |  | NO | Description |
| PBSRES_ForewordList | varchar |  |  | SI | A list of PBS unique code for the foreward that ap... |
| PBSRES_Indication_DR | bigint |  | FK | SI | The PBS unique code for the condition affecting th... |
| PBSRES_Owner | varchar |  |  | SI | Owner |
| PBSRES_PrescriberInstructionList | varchar |  |  | SI | A list of PBS unique code for the legally binding ... |
| PBSRES_StreamlineCode | varchar |  |  | SI | The approval code to use when the benefit type is ... |
| PBSRES_TreatmentPhase_DR | bigint |  | FK | SI | The PBS unique code for the phase of treatment for... |
| PBSRES_UpdatedDate | date |  |  | SI | Updated Date |
| PBSRES_UpdatedTime | time |  |  | SI | Updated Time |
| PBSRES_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*