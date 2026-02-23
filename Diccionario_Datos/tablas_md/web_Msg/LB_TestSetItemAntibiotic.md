# web_Msg.LB_TestSetItemAntibiotic

**Schema:** web_Msg
**Columnas:** 26
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Exámenes de Laboratorio**. Solicitudes y resultados. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBTSIANTMsg_ParRef | varchar |  |  | SI | A temperory DR link to web.Msg.LBTestSetItem |
| LBTSIANT_AntibioticPanel_DR | bigint |  | FK | SI | Antibiotic Panel DR |
| LBTSIANT_Antibiotic_DR | bigint |  | FK | SI | Antibiotics Code |
| LBTSIANT_Default | varchar |  |  | SI | Marks that Record was inserted due to Code Table D... |
| LBTSIANT_Instrument_DR | bigint |  | FK | SI | Instrument DR |
| LBTSIANT_ParRef | varchar |  |  | SI | LBTestSet Parent Reference
Required by User.LBTes... |
| LBTSIANT_Reportable | varchar |  |  | SI | Reportable |
| LBTSIANT_Restricted | varchar |  |  | SI | Restricted |
| LBTSIANT_ResultETest | varchar |  |  | SI | Result E Test |
| LBTSIANT_ResultETest_DR | bigint |  | FK | SI | Sensitivity ETest |
| LBTSIANT_ResultMIC | varchar |  |  | SI | Result MIC |
| LBTSIANT_ResultMICIntermediate | varchar |  |  | SI | Result MIC Intermediate Point |
| LBTSIANT_ResultMICResistant | varchar |  |  | SI | Result MIC Resistant Point |
| LBTSIANT_ResultMICSensitive | varchar |  |  | SI | Result MIC Sensitive Point |
| LBTSIANT_ResultMIC_DR | bigint |  | FK | SI | Sensitivity MIC |
| LBTSIANT_Result_DR | bigint |  | FK | SI | Des Ref Sensitivity table |
| LBTSIANT_Resultmm | varchar |  |  | SI | Result mm |
| LBTSIANT_Resultmm_DR | bigint |  | FK | SI | Sensitivity mm |
| LBTSIANT_RowID | varchar |  |  | SI | - |
| LBTSIANT_Sequence | double |  |  | SI | Sequence |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*