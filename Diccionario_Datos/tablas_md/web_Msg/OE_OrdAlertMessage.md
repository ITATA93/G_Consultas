# web_Msg.OE_OrdAlertMessage

**Schema:** web_Msg
**Columnas:** 34
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Órdenes Médicas**. Solicitudes de exámenes, procedimientos, etc.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ALM_AlertResponseType | varchar |  |  | SI | Alert Response Type |
| ALM_AlertType | varchar |  |  | SI | AlertType |
| ALM_AllergyID | varchar |  |  | SI | Allergy Match ID |
| ALM_Arcim_DR | varchar |  | FK | SI | DR to ARCIM: Interacting Arcim (this order) |
| ALM_Childsub | double |  |  | SI | Childsub |
| ALM_DSSActionItem_DR | varchar |  | FK | SI | Alert Action Item from websys_DecisionSupport.Audi... |
| ALM_DateUpdate | date |  |  | SI | DateUpdate |
| ALM_Fatal | varchar |  |  | SI | Fatal alert |
| ALM_HardStop | bit |  |  | SI | Hard Stop |
| ALM_IntArcim_DR | varchar |  | FK | SI | DR to ARCIM: Arcim interacting with (other order) |
| ALM_MonoGraphLink | varchar |  |  | SI | Monograph link parameters |
| ALM_Note_DR | varchar |  | FK | SI | Alert Disagreement Notes ID |
| ALM_OEORI_DR | varchar |  | FK | SI | Des Ref OEORI |
| ALM_OverrideReason_DR | bigint |  | FK | SI | Des Ref OverrideReason |
| ALM_ParRef | varchar |  |  | SI | OE_OrdItem Parent Reference
Required by User.OEOr... |
| ALM_Priority | varchar |  |  | SI | Priority |
| ALM_ReasonRequired | varchar |  |  | SI | ReasonRequired |
| ALM_ResultID | varchar |  |  | SI | ResultID - Used to display link to current result ... |
| ALM_RowId | varchar |  |  | SI | - |
| ALM_Severity | varchar |  |  | SI | Severity |
| ALM_SeverityColour | varchar |  |  | SI | SeverityColour |
| ALM_TimeUpdate | time |  |  | SI | TimeUpdate |
| ALM_UserUpdate_DR | bigint |  | FK | SI | Des Ref UserUpdate |
| AdditionalDataString | varchar |  |  | SI | additional delimited string as stored according to... |
| GroupTypeCode | varchar |  |  | NO | additional coded type for query grouping |
| GroupTypeSequence | varchar |  |  | SI | additional coded interaction sequence order (per g... |
| ID | varchar |  |  | NO | - |
| InteractionAllIDs | varchar |  |  | SI | All Interaction rowids (as returned from query) |
| InteractionDateTimeDisplay | varchar |  |  | SI | Display Interaction Start Date Time (as returned f... |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*