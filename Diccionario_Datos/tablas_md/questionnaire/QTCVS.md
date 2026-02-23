# questionnaire.QTCVS

> Voice Sheet

**Schema:** questionnaire
**Columnas:** 96
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Voice Sheet

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Chief Complaint Details |
| Q02 | varchar |  |  | SI | Duration |
| Q03 | varchar |  |  | SI | Sudden |
| Q04 | varchar |  |  | SI | Comments |
| Q05 | varchar |  |  | SI | Course |
| Q06 | varchar |  |  | SI | Impact Of Complaint On The Patient |
| Q07 | numeric |  |  | SI | VHI-10 |
| Q08 | varchar |  |  | SI | Etiological Factors |
| Q09 | varchar |  |  | SI | Occupation |
| Q10 | varchar |  |  | SI | Vocal Demand |
| Q11 | varchar |  |  | SI | Job Environment |
| Q16 | varchar |  |  | SI | Examination |
| Q17 | varchar |  |  | SI | Auditory Perceptual Assessment (APA) |
| Q18 | varchar |  |  | SI | Overall Grade |
| Q19 | varchar |  |  | SI | Comments |
| Q20 | varchar |  |  | SI | Character (Quality) |
| Q21 | varchar |  |  | SI | Pitch |
| Q22 | varchar |  |  | SI | Register - Habitual |
| Q23 | varchar |  |  | SI | Register Break |
| Q24 | varchar |  |  | SI | Comments |
| Q25 | varchar |  |  | SI | Loudness |
| Q26 | varchar |  |  | SI | Glottal Attack |
| Q28 | varchar |  |  | SI | External Laryngeal Examination |
| Q29 | varchar |  |  | SI | Laryngeal Skeleton |
| Q30 | varchar |  |  | SI | Comments |
| Q31 | varchar |  |  | SI | Laryngeal Click |
| Q32 | varchar |  |  | SI | Laryngeal Position |
| Q33 | varchar |  |  | SI | Cervical Veins |
| Q34 | varchar |  |  | SI | Neck Scars |
| Q35 | varchar |  |  | SI | Type |
| Q36 | varchar |  |  | SI | Site |
| Q37 | varchar |  |  | SI | Size |
| Q38 | varchar |  |  | SI | Tracheostomy |
| Q38ObsDR | varchar |  | FK | SI | Tracheostomy DR |
| Q39 | varchar |  |  | SI | Tracheostomy Size |
| Q39ObsDR | varchar |  | FK | SI | Tracheostomy Size DR |
| Q40 | varchar |  |  | SI | Tracheostomy Type |
| Q40ObsDR | varchar |  | FK | SI | Tracheostomy Type DR |
| Q41 | varchar |  |  | SI | Tracheostomy Cuff |
| Q41ObsDR | varchar |  | FK | SI | Tracheostomy Cuff DR |
| Q42 | varchar |  |  | SI | Tracheostomy Fenestration |
| Q42ObsDR | varchar |  | FK | SI | Tracheostomy Fenestration DR |
| Q43 | varchar |  |  | SI | Tracheostomy Speaking Valve |
| Q43ObsDR | varchar |  | FK | SI | Tracheostomy Speaking Valve DR |
| Q44 | varchar |  |  | SI | Tracheostomy Speaking Valve Type |
| Q45 | varchar |  |  | SI | Investigations |
| Q46 | varchar |  |  | SI | CT Head And Neck With Contrast |
| Q47 | varchar |  |  | SI | CT Head And Neck Without Contrast |
| Q48 | varchar |  |  | SI | CT Head And Neck And Upper Chest With Contrast |
| Q49 | varchar |  |  | SI | CT Head And Neck And Upper Chest Without Contrast |
| Q50 | varchar |  |  | SI | MRI Brain |
| Q51 | varchar |  |  | SI | Pharyngeal PH |
| Q52 | varchar |  |  | SI | 24-Hr Double-Probe PH-Metry |
| Q53 | varchar |  |  | SI | Upper GIT Endoscopy |
| Q54 | varchar |  |  | SI | Others |
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