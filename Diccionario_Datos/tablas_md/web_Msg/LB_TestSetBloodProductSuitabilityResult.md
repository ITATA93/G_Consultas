# web_Msg.LB_TestSetBloodProductSuitabilityResult

**Schema:** web_Msg
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Exámenes de Laboratorio**. Solicitudes y resultados.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBTSBPSR_ABORhException_DR | varchar |  | FK | SI | ABO / Rh Exception record |
| LBTSBPSR_AcknowledgedBy_DR | bigint |  | FK | SI | User who Acknowledgement the suitability rule |
| LBTSBPSR_AcknowledgedDate | date |  |  | SI | Date of Acknowledgement |
| LBTSBPSR_AcknowledgedTime | time |  |  | SI | Time of Acknowledgement |
| LBTSBPSR_Action | varchar |  |  | SI | Action
Required by User.LBTestSetBloodProductSuit... |
| LBTSBPSR_AntibodyIncompatibleAntigen_DR | varchar |  | FK | SI | Antibody Incompatible Antigen |
| LBTSBPSR_BloodProductSuitabilityRule_DR | varchar |  | FK | SI | Blood Product Suitability Rule |
| LBTSBPSR_MaternalResult | varchar |  |  | SI | A flag to indicate that the result was based on te... |
| LBTSBPSR_Message | varchar |  |  | SI | Message
Required by User.LBTestSetBloodProductSui... |
| LBTSBPSR_OverrideReasonComment | varchar |  |  | SI | Override Reason Comment |
| LBTSBPSR_OverrideReason_DR | bigint |  | FK | SI | Override Reason |
| LBTSBPSR_OverrideUser_DR | bigint |  | FK | SI | Override User |
| LBTSBPSR_ParRef | varchar |  |  | SI | Test Set / Blood Product Parent Reference
Require... |
| LBTSBPSR_RowID | varchar |  |  | SI | - |
| LBTSBPSR_Source | varchar |  |  | SI | Source
See BPRuleSourceVALUELIST
Required by Use... |
| LBTSBPSR_TestSetBloodProduct_DR | varchar |  | FK | SI | Test Set / Blood Product Message Parent Reference |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*