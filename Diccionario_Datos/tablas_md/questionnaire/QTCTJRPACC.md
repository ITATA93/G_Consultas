# questionnaire.QTCTJRPACC

> Total Joint Replacement Pre-Admission Clinic Checklist

**Schema:** questionnaire
**Columnas:** 84
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Total Joint Replacement Pre-Admission Clinic Checklist

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Anaesthetic assessment completed |
| Q04 | varchar |  |  | SI | Variance |
| Q05 | varchar |  |  | SI | Patient's understanding of procedure confirmed and... |
| Q06 | varchar |  |  | SI | Variance |
| Q07 | varchar |  |  | SI | Baseline vital signs and neurovascular observation... |
| Q08 | varchar |  |  | SI | Variance |
| Q09 | varchar |  |  | SI | Baseline height and weight recorded |
| Q10 | varchar |  |  | SI | Variance |
| Q11 | varchar |  |  | SI | 12 lead electrocardiogram performed and reviewed |
| Q12 | varchar |  |  | SI | Variance |
| Q13 | varchar |  |  | SI | Patient received radiology request form |
| Q14 | varchar |  |  | SI | Variance |
| Q15 | varchar |  |  | SI | Patient received pathology request form |
| Q16 | varchar |  |  | SI | Variance |
| Q17 | varchar |  |  | SI | Ordered blood tests completed and reviewed |
| Q18 | varchar |  |  | SI | Variance |
| Q19 | varchar |  |  | SI | Arranged for cross match two days prior to admissi... |
| Q20 | varchar |  |  | SI | Variance |
| Q21 | varchar |  |  | SI | Skin assessed for wounds or fungal infection |
| Q22 | varchar |  |  | SI | Variance |
| Q23 | varchar |  |  | SI | Methicillin - resistant staphylococcus aureus (MRS... |
| Q24 | varchar |  |  | SI | Variance |
| Q25 | varchar |  |  | SI | Decolonisation information pamphlet provided and e... |
| Q26 | varchar |  |  | SI | Variance |
| Q27 | varchar |  |  | SI | Topical antibiotic given and use-of explained |
| Q28 | varchar |  |  | SI | Variance |
| Q29 | varchar |  |  | SI | Education provided for pre-operative washes and pr... |
| Q30 | varchar |  |  | SI | Variance |
| Q31 | varchar |  |  | SI | Patient provided with information brochure / watch... |
| Q32 | varchar |  |  | SI | Variance |
| Q33 | varchar |  |  | SI | Fasting requirements explained |
| Q34 | varchar |  |  | SI | Variance |
| Q35 | varchar |  |  | SI | Potential infection risks discussed |
| Q36 | varchar |  |  | SI | Examples: wounds, urinary tract and chest infectio... |
| Q37 | varchar |  |  | SI | Variance |
| Q38 | varchar |  |  | SI | Length of stay discussed |
| Q39 | varchar |  |  | SI | Variance |
| Q40 | varchar |  |  | SI | Enoxaparin administration discussed |
| Q41 | varchar |  |  | SI | Variance |
| Q42 | varchar |  |  | SI | Referrals to allied health services organised as n... |
| Q43 | varchar |  |  | SI | Other referrals |
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