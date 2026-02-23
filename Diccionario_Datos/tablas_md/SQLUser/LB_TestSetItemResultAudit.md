# SQLUser.LB_TestSetItemResultAudit

**Schema:** SQLUser
**Columnas:** 36
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Exámenes de Laboratorio**. Solicitudes y resultados. Auditoría de modificaciones.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBTSIRA_ParRef | varchar | PK |  | NO | LBTestSetItem Parent Reference |
| LBTSIRA_AuthorisedBy_DR | bigint |  | FK | SI | User who authorised |
| LBTSIRA_Comments_DR | bigint |  | FK | SI | Test Set Item Comment
HTMLRichText |
| LBTSIRA_Date | date |  |  | SI | Date the result was entered |
| LBTSIRA_Diluted | varchar |  |  | SI | Flag that indicates that the sample the test was p... |
| LBTSIRA_DilutionFactor | numeric |  |  | SI | Dilution factor of the sample the test was perform... |
| LBTSIRA_InstrumentFlags | varchar |  |  | SI | Translated Instrument flags transmitted for this r... |
| LBTSIRA_InstrumentPerformedDate | date |  |  | SI | Instrument Performed Date |
| LBTSIRA_InstrumentPerformedTime | time |  |  | SI | Instrument Performed Time |
| LBTSIRA_Instrument_DR | bigint |  | FK | SI | Performed on instrument |
| LBTSIRA_OriginalInstrumentFlags | varchar |  |  | SI | Original Instrument flags transmitted for this res... |
| LBTSIRA_PathogenConfirmed | varchar |  |  | SI | Pathogen confirmed flag |
| LBTSIRA_PathogenDuplicate | varchar |  |  | SI | Pathogen duplicate flag |
| LBTSIRA_PathogenGrowthQualifierDesc | varchar |  |  | SI | Pathogen Growth Qualifier |
| LBTSIRA_PathogenSignificant | varchar |  |  | SI | Pathogen significant flag |
| LBTSIRA_PathogenSubTypeDesc | varchar |  |  | SI | Pathogen SubType Desc |
| LBTSIRA_PerformedAtLabSite_DR | bigint |  | FK | SI | Lab Site the result was entered or performed |
| LBTSIRA_PreviousResultAudit_DR | varchar |  | FK | SI | Link to the previous result audit |
| LBTSIRA_RepeatNumber | numeric |  |  | SI | Repeat number |
| LBTSIRA_ResultAbnormalFlag | varchar |  |  | SI | Result abnormal flag |
| LBTSIRA_ResultDesc | varchar |  |  | SI | Test Set Item Result |
| LBTSIRA_ResultNormalRange | varchar |  |  | SI | Result Range
Stores Range as of authorisation dat... |
| LBTSIRA_ResultStatus | varchar |  |  | SI | Result Status |
| LBTSIRA_RowID | varchar |  |  | NO | - |
| LBTSIRA_StaffNotes_DR | bigint |  | FK | SI | Test Set Item Staff Notes
HTMLRichText |
| LBTSIRA_TextResult_DR | bigint |  | FK | SI | Test Set Item Text Result
HTMLRichText |
| LBTSIRA_Time | time |  |  | SI | Time the result was entered |
| LBTSIRA_User_DR | bigint |  | FK | SI | User who entered the result |
| Q01Q1 | - |  |  | SI | Fecha del Evento |
| Q01Q2 | - |  |  | SI | Descripción del Evento |
| Q01Q3 | - |  |  | SI | Fecha de Registro |
| Q01Q4 | - |  |  | SI | Hora de Registro |
| Q01Q5 | - |  |  | SI | Profesional que Registra |
| Q01Q6 | - |  |  | SI | CESFAM |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*