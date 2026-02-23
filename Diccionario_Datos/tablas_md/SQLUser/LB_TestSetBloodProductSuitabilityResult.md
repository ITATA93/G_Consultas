# SQLUser.LB_TestSetBloodProductSuitabilityResult

**Schema:** SQLUser
**Columnas:** 21
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Exámenes de Laboratorio**. Solicitudes y resultados.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBTSBPSR_ParRef | varchar | PK |  | NO | Test Set / Blood Product Parent Reference |
| ChildQControlDR | - |  |  | SI | Child Reference: Control |
| LBTSBPSR_ABORhException_DR | varchar |  | FK | SI | ABO / Rh Exception record |
| LBTSBPSR_AcknowledgedBy_DR | bigint |  | FK | SI | User who Acknowledgement the suitability rule |
| LBTSBPSR_AcknowledgedDate | date |  |  | SI | Date of Acknowledgement |
| LBTSBPSR_AcknowledgedTime | time |  |  | SI | Time of Acknowledgement |
| LBTSBPSR_Action | varchar |  |  | NO | Action |
| LBTSBPSR_AntibodyIncompatibleAntigen_DR | varchar |  | FK | SI | Antibody Incompatible Antigen |
| LBTSBPSR_BloodProductSuitabilityRule_DR | varchar |  | FK | SI | Blood Product Suitability Rule |
| LBTSBPSR_MaternalResult | varchar |  |  | SI | A flag to indicate that the result was based on te... |
| LBTSBPSR_Message | varchar |  |  | NO | Message |
| LBTSBPSR_OverrideReasonComment | varchar |  |  | SI | Override Reason Comment |
| LBTSBPSR_OverrideReason_DR | bigint |  | FK | SI | Override Reason |
| LBTSBPSR_OverrideUser_DR | bigint |  | FK | SI | Override User |
| LBTSBPSR_RowID | varchar |  |  | NO | - |
| LBTSBPSR_Source | varchar |  |  | NO | Source
See BPRuleSourceVALUELIST |
| QExaQ1 | - |  |  | SI | Examenes |
| QExaQ2 | - |  |  | SI | Fecha |
| QExaQ3 | - |  |  | SI | Resultado |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*