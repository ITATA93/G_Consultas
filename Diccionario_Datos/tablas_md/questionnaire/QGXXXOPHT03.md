# questionnaire.QGXXXOPHT03

**Schema:** questionnaire
**Columnas:** 99
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q03 | varchar | PK |  | SI | Lachrymal Gland |
| Q07 | varchar | PK |  | SI | Notes |
| Q08 | varchar | PK |  | SI | Notes |
| Q12 | varchar | PK |  | SI | Lachrymal Gland@OD |
| Q13 | varchar | PK |  | SI | Lachrymal Gland@OS |
| Q14 | varchar | PK |  | SI | Lachrymal Drainage@OD |
| Q15 | varchar | PK |  | SI | Lachrymal Drainage@OS |
| Q16 | varchar | PK |  | SI | Lymphnodes@OD |
| Q17 | varchar | PK |  | SI | Lymphnodes@OS |
| Q18 | varchar | PK |  | SI | Lids@OD |
| Q19 | varchar | PK |  | SI | Lids@OS |
| Q23 | varchar | PK |  | SI | Bulbar@OD |
| Q24 | varchar | PK |  | SI | Palpebral@OD |
| Q25 | varchar | PK |  | SI | Bulbar@OS |
| Q26 | varchar | PK |  | SI | Palpebral@OS |
| Q28 | varchar | PK |  | SI | Dye Type@OD |
| Q29 | varchar | PK |  | SI | Dye Type@OS |
| Q30 | varchar | PK |  | SI | Epithelium@OD |
| Q31 | varchar | PK |  | SI | Epithelium@OS |
| Q32 | varchar | PK |  | SI | Stroma@OD |
| Q33 | varchar | PK |  | SI | Stroma@OS |
| Q34 | varchar | PK |  | SI | Endothelium@OD |
| Q35 | varchar | PK |  | SI | Endothelium@OS |
| Q36 | varchar | PK |  | SI | Tear Film@OD |
| Q37 | varchar | PK |  | SI | Tear Film@OS |
| Q39 | varchar | PK |  | SI | Depth@OD |
| Q40 | varchar | PK |  | SI | Depth@OS |
| Q43 | varchar | PK |  | SI | Flare@OD |
| Q44 | varchar | PK |  | SI | Flare@OS |
| Q45 | varchar | PK |  | SI | Iris - Colour@OD |
| Q46 | varchar | PK |  | SI | Iris - Colour@OS |
| Q47 | varchar | PK |  | SI | Iris - Pathology@OD |
| Q48 | varchar | PK |  | SI | Iris - Pathology@OS |
| Q49 | varchar | PK |  | SI | Notes |
| Q50 | varchar | PK |  | SI | Conjuntiva & Sclera |
| Q51 | varchar | PK |  | SI | Lachrymal Drainage |
| Q53 | varchar | PK |  | SI | Clarity@OD |
| Q54 | varchar | PK |  | SI | Clarity@OS |
| Q55 | varchar | PK |  | SI | Anterior capsule@OD |
| Q56 | varchar | PK |  | SI | Post capsule@OD |
| Q57 | varchar | PK |  | SI | Post capsule@OS |
| Q58 | varchar | PK |  | SI | Anterior capsule@OS |
| Q59 | varchar | PK |  | SI | Cortex@OD |
| Q60 | varchar | PK |  | SI | Nucleus@OD |
| Q61 | varchar | PK |  | SI | Cortex@OS |
| Q62 | varchar | PK |  | SI | Nucleus@OS |
| Q64 | varchar | PK |  | SI | Lymphnodes |
| Q65 | varchar | PK |  | SI | Cells@OD |
| Q66 | varchar | PK |  | SI | Plus@OD |
| Q67 | varchar | PK |  | SI | Plus@OS |
| Q68 | varchar | PK |  | SI | Cells@OS |
| Q69 | varchar | PK |  | SI | Lids |
| Q70 | varchar | PK |  | SI | Bulbar |
| Q71 | varchar | PK |  | SI | Palpebral |
| Q72 | varchar | PK |  | SI | Dye Type |
| Q73 | varchar | PK |  | SI | Epithelium |
| Q74 | varchar | PK |  | SI | Stroma |
| Q75 | varchar | PK |  | SI | Endothelium |
| Q76 | varchar | PK |  | SI | Tear Film |
| Q77 | varchar | PK |  | SI | Depth |
| Q78 | varchar | PK |  | SI | Flare |
| Q79 | varchar | PK |  | SI | Iris - Colour |
| Q80 | varchar | PK |  | SI | Iris - Pathology |
| Q81 | varchar | PK |  | SI | Clarity |
| Q82 | varchar | PK |  | SI | Post capsule |
| Q90 | varchar | PK |  | SI | Cortex |
| Q91 | varchar | PK |  | SI | Plus |
| Q92 | varchar | PK |  | SI | Cells |
| Q94 | varchar | PK |  | SI | Anterior Capsule |
| Q95 | varchar | PK |  | SI | Nucleus |
| QUESAnaDR | varchar | PK | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar | PK | FK | SI | Operation |
| QUESConsultDR | varchar | PK | FK | SI | Consult |
| QUESCopiedComments | varchar | PK |  | SI | Copied Comments |
| QUESCopiedDate | date | PK |  | SI | Copied Date |
| QUESCopiedEpDR | bigint | PK | FK | SI | Copied Episode |
| QUESCopiedTime | time | PK |  | SI | Copied Time |
| QUESCopiedUserDR | bigint | PK | FK | SI | Copied User |
| QUESCreateDate | date | PK |  | SI | Creation Date |
| QUESCreateTime | time | PK |  | SI | Creation Time |
| QUESCreateUserDR | bigint | PK | FK | SI | Creation User |
| QUESDate | date | PK |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint | PK | FK | SI | Error Reason |
| QUESFHResidentDR | bigint | PK | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar | PK | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar | PK | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar | PK | FK | SI | Order Execution |
| QUESOperRoomDR | bigint | PK | FK | SI | Operating Room |
| QUESPAAdmDR | bigint | PK | FK | SI | Admission |
| QUESPAPatMasDR | bigint | PK | FK | SI | Patient |
| QUESRBAppointmentDR | varchar | PK | FK | SI | Appointments |
| QUESReasonForCorrectionDR | bigint | PK | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint | PK | FK | SI | Questionnaire |
| QUESScore | varchar | PK |  | SI | Score |
| QUESStatusDR | bigint | PK | FK | SI | Status |
| QUESTextResultDR | bigint | PK | FK | SI | Text Result |
| QUESTime | time | PK |  | SI | Last Update Time |
| QUESUserDR | bigint | PK | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*