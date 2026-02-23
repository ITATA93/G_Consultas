# questionnaire.QTCPHYSOBSA

> Physiotherapy Obstetric Assessment

**Schema:** questionnaire
**Columnas:** 96
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Physiotherapy Obstetric Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Please ensure any of the following Past Medical Hi... |
| Q02 | varchar |  |  | SI | Where is the pain perceived? |
| Q03 | varchar |  |  | SI | How long has the pain been present?  |
| Q04 | varchar |  |  | SI | Pain intensity (0-10): |
| Q05 | varchar |  |  | SI | Pain increased by |
| Q06 | varchar |  |  | SI | Pain worsened by |
| Q07 | varchar |  |  | SI | Pain during the night? |
| Q08 | varchar |  |  | SI | Comments |
| Q09 | varchar |  |  | SI | Does the pain prevent you from doing any daily act... |
| Q10 | varchar |  |  | SI | Comments |
| Q11 | varchar |  |  | SI | Have you used any self-help techniques? |
| Q12 | varchar |  |  | SI | Comments |
| Q13 | varchar |  |  | SI | Verbal Consent |
| Q14 | varchar |  |  | SI | Indicate reason |
| Q15 | varchar |  |  | SI | Charperone required? |
| Q16 | varchar |  |  | SI | Name of chaperone |
| Q17 | varchar |  |  | SI | Gait |
| Q18 | varchar |  |  | SI | Other |
| Q19 | varchar |  |  | SI | Visual inspection of spinal alignment:  |
| Q20 | varchar |  |  | SI | Palpation of lumbar region |
| Q21 | varchar |  |  | SI | Assessment of lumbar range of motion |
| Q22 | varchar |  |  | SI | Palpation of thoracic region |
| Q23 | varchar |  |  | SI | Sitting leg abduction range of motion |
| Q24 | varchar |  |  | SI | Distance between medial aspect of knees |
| Q26 | varchar |  |  | SI | Active straight leg raise test |
| Q27 | varchar |  |  | SI | Comments |
| Q28 | varchar |  |  | SI | Pain provocation tests |
| Q29 | varchar |  |  | SI | Palpation of LDL / Sacral sulcus |
| Q30 | varchar |  |  | SI | Comments |
| Q31 | varchar |  |  | SI | P4 test |
| Q32 | varchar |  |  | SI | Comments |
| Q33 | varchar |  |  | SI | Patrick’s FABER test |
| Q34 | varchar |  |  | SI | Comments |
| Q35 | varchar |  |  | SI | Gaenslen’s test |
| Q36 | varchar |  |  | SI | Comments |
| Q37 | varchar |  |  | SI | Distraction test |
| Q38 | varchar |  |  | SI | Comments |
| Q39 | varchar |  |  | SI | Compression test |
| Q40 | varchar |  |  | SI | Comments |
| Q41 | varchar |  |  | SI | Palpation of SP |
| Q42 | varchar |  |  | SI | Modified Trendelemburg Test |
| Q43 | varchar |  |  | SI | Kinetic tests |
| Q44 | varchar |  |  | SI | Forward flexion in standing / sitting (Piedallu te... |
| Q45 | varchar |  |  | SI | Comments |
| Q46 | varchar |  |  | SI | Hip flexion in standing (Guillet test) |
| Q47 | varchar |  |  | SI | Comments |
| Q48 | varchar |  |  | SI | Positional assessment |
| Q49 | varchar |  |  | SI | Superior aspect of iliac crest |
| Q50 | varchar |  |  | SI | Underside of ASIS |
| Q51 | varchar |  |  | SI | Underside of PSIS |
| Q52 | varchar |  |  | SI | Confirmatory sit-up test |
| Q53 | varchar |  |  | SI | Positional diagnosis |
| Q54 | varchar |  |  | SI | Treatment plan / advice |
| Q55 | varchar |  |  | SI | Additional comments |
| Q57 | varchar |  |  | SI | Supporting Information / Leaflets provided: |
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