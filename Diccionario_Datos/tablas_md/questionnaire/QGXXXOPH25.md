# questionnaire.QGXXXOPH25

> Ophthalmic Photography Request

**Schema:** questionnaire
**Columnas:** 84
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Ophthalmic Photography Request

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Diagnosis |
| Q02 | varchar |  |  | SI | Dilation with |
| Q03 | varchar |  |  | SI | External |
| Q04 | varchar |  |  | SI | Other |
| Q05 | varchar |  |  | SI | Slit lamp |
| Q06 | bit |  |  | SI | With Fluorescein / rose bengal |
| Q07 | varchar |  |  | SI | Lids |
| Q08 | varchar |  |  | SI | Cornea |
| Q09 | varchar |  |  | SI | Iris |
| Q10 | varchar |  |  | SI | Lens |
| Q11 | varchar |  |  | SI | Conjunctiva |
| Q12 | varchar |  |  | SI | Gonioscopy |
| Q13 | varchar |  |  | SI | Specular microscopy |
| Q14 | varchar |  |  | SI | Endothial cell account needed in |
| Q15 | numeric |  |  | SI | Cell count: cell/mm2 |
| Q16 | numeric |  |  | SI | Cell count 2 |
| Q17 | numeric |  |  | SI | Polymegathism |
| Q18 | numeric |  |  | SI | Polymegathism 2 |
| Q19 | numeric |  |  | SI | Polymorphism |
| Q20 | numeric |  |  | SI | Polymorphism 2 |
| Q21 | varchar |  |  | SI | Guttata |
| Q22 | varchar |  |  | SI | Guttata 2 |
| Q23 | varchar |  |  | SI | Fundus |
| Q24 | varchar |  |  | SI | Color fundus photo |
| Q25 | varchar |  |  | SI | DR-7 filed view |
| Q26 | varchar |  |  | SI | stereo |
| Q27 | varchar |  |  | SI | Discs |
| Q28 | varchar |  |  | SI | Auto fluorescence |
| Q29 | varchar |  |  | SI | Fluorescin angiography |
| Q30 | varchar |  |  | SI | Trasit phase |
| Q31 | numeric |  |  | SI | Late photo at |
| Q32 | varchar |  |  | SI | minutes |
| Q33 | varchar |  |  | SI | View |
| Q34 | varchar |  |  | SI | Indocyanine green angiography |
| Q35 | varchar |  |  | SI | Transit phase |
| Q36 | varchar |  |  | SI | Notes |
| Q37 | varchar |  |  | SI | Image Annotation  |
| Q38 | varchar |  |  | SI | Right Eye |
| Q39 | varchar |  |  | SI | Left eye |
| Q40 | varchar |  |  | SI | Image |
| Q41 | varchar |  |  | SI | General |
| Q42 | date |  |  | SI | Date |
| Q43 | time |  |  | SI | Time |
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