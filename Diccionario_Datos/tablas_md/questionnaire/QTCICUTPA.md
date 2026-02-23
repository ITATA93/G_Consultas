# questionnaire.QTCICUTPA

> Intensive Care Unit (ICU) Ward Round

**Schema:** questionnaire
**Columnas:** 84
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Intensive Care Unit (ICU) Ward Round

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | bigint |  |  | SI | ICU presenting problem |
| Q01TxtOnly | bigint |  |  | SI | ICU presenting problem Plain Text Only |
| Q02 | bigint |  |  | SI | ICU clinical examination |
| Q02TxtOnly | bigint |  |  | SI | ICU clinical examination Plain Text Only |
| Q03 | bigint |  |  | SI | ICU active problems |
| Q03TxtOnly | bigint |  |  | SI | ICU active problems Plain Text Only |
| Q04 | bigint |  |  | SI | ICU plan |
| Q04TxtOnly | bigint |  |  | SI | ICU plan Plain Text Only |
| Q05 | bigint |  |  | SI | ICU admission summary |
| Q05TxtOnly | bigint |  |  | SI | ICU admission summary Plain Text Only |
| Q06 | bigint |  |  | SI | ICU discharge plan |
| Q06TxtOnly | bigint |  |  | SI | ICU discharge plan Plain Text Only |
| Q07 | date |  |  | SI | Date |
| Q08 | time |  |  | SI | Time |
| Q09 | varchar |  |  | SI | Staff present on round |
| Q10 | varchar |  |  | SI | ICU presenting complaint |
| Q11 | varchar |  |  | SI | ICU active issues |
| Q12 | varchar |  |  | SI | ICU clinical examination |
| Q13 | varchar |  |  | SI | ICU plan |
| Q14 | varchar |  |  | SI | ICU admission summary |
| Q15 | varchar |  |  | SI | ICU discharge plan |
| Q16 | varchar |  |  | SI | Considerations During ICU Medical Round |
| Q17 | varchar |  |  | SI | Review invasive lines |
| Q18 | varchar |  |  | SI | Review for extubation |
| Q19 | varchar |  |  | SI | Deep Vein Thrombosis (DVT) prophylaxis |
| Q20 | varchar |  |  | SI | Peptic ulcer prophylaxis |
| Q21 | varchar |  |  | SI | Review antibiotics |
| Q22 | varchar |  |  | SI | Ventilator Associated Pneumonia (VAP) antibiotics |
| Q23 | varchar |  |  | SI | Sedation / Analgesia / CAM-ICU score |
| Q24 | varchar |  |  | SI | Nutritional planning |
| Q25 | varchar |  |  | SI | Bowels / Aperients |
| Q26 | varchar |  |  | SI | C-spine considered |
| Q27 | varchar |  |  | SI | Dummy 1 |
| Q28 | varchar |  |  | SI | Dummy 2 |
| Q29 | varchar |  |  | SI | Considerations for ICU Medical Discharge |
| Q30 | varchar |  |  | SI | ICU team leader aware |
| Q31 | varchar |  |  | SI | Ward team handover |
| Q32 | varchar |  |  | SI | Discharge summary completed |
| Q33 | varchar |  |  | SI | Plan for invasive devices documented in the discha... |
| Q34 | varchar |  |  | SI | Medication review completed |
| Q35 | varchar |  |  | SI | Patient and family informed |
| Q36 | varchar |  |  | SI | Dummy 3 |
| Q37 | varchar |  |  | SI | Dummy 4 |
| QUESAnaDR | varchar |  | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar |  | FK | SI | Operation |
| QUESConsultDR | varchar |  | FK | SI | Consult |
| QUESCopiedComments | varchar |  |  | SI | Copied Comments |
| QUESCopiedDate | date |  |  | SI | Copied Date |
| QUESCopiedEpDR | bigint |  | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint |  | FK | SI | Copied Source DR |
| QUESCopiedTime | time |  |  | SI | Copied Time |
| QUESCopiedUserDR | bigint |  | FK | SI | Copied User |
| QUESCreateDate | date |  |  | SI | Creation Date |
| QUESCreateTime | time |  |  | SI | Creation Time |
| QUESCreateUserDR | bigint |  | FK | SI | Creation User |
| QUESDate | date |  |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint |  | FK | SI | Error Reason |
| QUESFHResidentDR | bigint |  | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar |  | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar |  | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar |  | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint |  | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar |  | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint |  | FK | SI | Operating Room |
| QUESPAAdmDR | bigint |  | FK | SI | Admission |
| QUESPAAdverseEventDR | varchar |  | FK | SI | Adverse Event |
| QUESPAPatMasDR | bigint |  | FK | SI | Patient |
| QUESPAPregnancyDR | bigint |  | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint |  | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar |  | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar |  | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar |  | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar |  | FK | SI | Appointment Outcome |
| QUESRBApptSlotDR | varchar |  | FK | SI | Appointment Slot |
| QUESReasonForCorrectionDR | bigint |  | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint |  | FK | SI | Questionnaire |
| QUESScore | varchar |  |  | SI | Score |
| QUESSecondUserDR | bigint |  | FK | SI | Second Signature |
| QUESStatusDR | bigint |  | FK | SI | Status |
| QUESTextResultDR | bigint |  | FK | SI | Text Result |
| QUESTime | time |  |  | SI | Last Update Time |
| QUESTransactionDR | varchar |  | FK | SI | Transaction |
| QUESUserDR | bigint |  | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*