# web_Msg.LB_EpisodeReporting

**Schema:** web_Msg
**Columnas:** 21
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBEPR_Association | varchar |  |  | SI | Association
This is an internal value used to den... |
| LBEPR_CareProv_DR | varchar |  | FK | SI | Care Provider
CareProvider DR (eg Doctor) to rece... |
| LBEPR_Clinic_DR | bigint |  | FK | SI | Clinic
The Clinic where the Referring Doctor DR t... |
| LBEPR_ConfidentialFax | varchar |  |  | SI | Confidential Fax Number |
| LBEPR_Copies | numeric |  |  | SI | Deprecated
No of Copies
0 = do not produce repor... |
| LBEPR_Fax | varchar |  |  | SI | Fax Number |
| LBEPR_Location_DR | bigint |  | FK | SI | Location
Location DR to receive the report |
| LBEPR_ParRef | bigint |  |  | SI | - |
| LBEPR_QuickPrint | varchar |  |  | SI | QuickPrint Flag
If set the request (all TestSets ... |
| LBEPR_RecipientID | varchar |  |  | SI | Recipient ID
CareProvider, Location, ReferringDoc... |
| LBEPR_RecipientType | varchar |  |  | SI | Recipient Type
The type of recipient for this rec... |
| LBEPR_ReferringDoctor_DR | bigint |  | FK | SI | Referring Doctor
Referring Doctor DR to receive t... |
| LBEPR_ReportEnabled | varchar |  |  | SI | Report Enabled
Report is Enabled |
| LBEPR_RowID | varchar |  |  | SI | - |
| LBEPR_ThirdParty_DR | bigint |  | FK | SI | Third Party
ThirdParty DR to receive the report |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*