# questionnaire.QGXXXOPHT04

**Schema:** questionnaire
**Columnas:** 86
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar | PK |  | SI | Dialation Drops |
| Q04 | date | PK |  | SI | Date |
| Q05 | time | PK |  | SI | Time |
| Q06 | varchar | PK |  | SI | Dialated |
| Q07 | varchar | PK |  | SI | Notes |
| Q09 | varchar | PK |  | SI | Vitreous-OD |
| Q10 | varchar | PK |  | SI | Notes |
| Q11 | varchar | PK |  | SI | Vitreous-OS |
| Q12 | varchar | PK |  | SI | C/D Ratio-Hz@OS |
| Q12ObsDR | varchar | PK | FK | SI | C/D Ratio-Hz@OS DR |
| Q13 | varchar | PK |  | SI | C/D Ratio - Hz@OD |
| Q13ObsDR | varchar | PK | FK | SI | C/D Ratio - Hz@OD DR |
| Q14 | varchar | PK |  | SI | C/D Ratio -Vt@OS |
| Q14ObsDR | varchar | PK | FK | SI | C/D Ratio -Vt@OS DR |
| Q15 | varchar | PK |  | SI | C/D Ratio- Vt@OD |
| Q15ObsDR | varchar | PK | FK | SI | C/D Ratio- Vt@OD DR |
| Q16 | varchar | PK |  | SI | Appearance@OD |
| Q17 | varchar | PK |  | SI | Appearance@OS |
| Q18 | varchar | PK |  | SI | Nerve fiber layer@OS |
| Q19 | varchar | PK |  | SI | Nerve fiber layer@OD |
| Q20 | varchar | PK |  | SI | Neural rim@OD |
| Q21 | varchar | PK |  | SI | Neural rim@OS |
| Q22 | varchar | PK |  | SI | Margin@OD |
| Q23 | varchar | PK |  | SI | Margin@OS |
| Q28 | bit | PK |  | SI | Dialated Macular or Fundus Exam |
| Q31 | varchar | PK |  | SI | Posterior Pole@OD |
| Q32 | varchar | PK |  | SI | Vessels@OD |
| Q33 | varchar | PK |  | SI | Periphery@OD |
| Q35 | varchar | PK |  | SI | Macula@OS |
| Q36 | varchar | PK |  | SI | Posterior Pole@OS |
| Q37 | varchar | PK |  | SI | Vessels@OS |
| Q38 | varchar | PK |  | SI | Periphery@OS |
| Q41 | varchar | PK |  | SI | Annotate Retina & Optic Nerve |
| Q42 | varchar | PK |  | SI | Macula@OD |
| Q43 | varchar | PK |  | SI | C/D Ratio - Hz |
| Q44 | varchar | PK |  | SI | C/D Ration - Vt |
| Q45 | varchar | PK |  | SI | Appearance |
| Q46 | varchar | PK |  | SI | Nerve Fiber Layer |
| Q47 | bit | PK |  | SI | PVD |
| Q48 | varchar | PK |  | SI | Neural Rim |
| Q49 | varchar | PK |  | SI | Margin |
| Q50 | varchar | PK |  | SI | Clear-OD |
| Q51 | varchar | PK |  | SI | Clear-OS |
| Q52 | varchar | PK |  | SI | Dilation drops |
| Q53 | date | PK |  | SI | Informed consent -Date |
| Q54 | time | PK |  | SI | Informed Consent- Time |
| Q55 | varchar | PK |  | SI | Foveal Reflex OD |
| Q56 | varchar | PK |  | SI | Foveal Reflex OS |
| Q57 | varchar | PK |  | SI | Informed consent taken ? |
| Q58 | varchar | PK |  | SI | C/D ratio- Vt@OS |
| Q58ObsDR | varchar | PK | FK | SI | C/D ratio- Vt@OS DR |
| Q59 | varchar | PK |  | SI | Fovela Reflex |
| Q60 | varchar | PK |  | SI | Macula |
| Q61 | varchar | PK |  | SI | Posterior Pole |
| Q62 | varchar | PK |  | SI | Vessels |
| Q64 | varchar | PK |  | SI | Periphery |
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
| QUESObsEntryDR | varchar | PK | FK | SI | Observation Entry |
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