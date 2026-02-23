# SQLUser.DICOM_Series

**Schema:** SQLUser
**Columnas:** 71
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Imágenes Diagnósticas**. Radiología y estudios de imagen.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DCSRS_RowID | varchar | PK |  | NO | - |
| DCSRS_SeriesInstanceUID | varchar |  |  | NO | Series Instance UID |
| DCSRS_SeriesModality | varchar |  |  | SI | Modality |
| DCSRS_SeriesNumber | varchar |  |  | SI | Series Number |
| DCSRS_Study_DR | varchar |  | FK | SI | Study DR |
| Q01 | - |  |  | SI | Have you ever felt you should cut down on your dri... |
| Q02 | - |  |  | SI | Have people annoyed you by criticizing your drinki... |
| Q03 | - |  |  | SI | Have you ever felt bad or guilty about your drinki... |
| Q04 | - |  |  | SI | Have you ever had a drink first thing in the morni... |
| Q05 | - |  |  | SI | • Ask your patients the four questions to determin... |
| Q06 | - |  |  | SI | • Each response to the four alcohol assessment que... |
| Q07 | - |  |  | SI | Responses determine the percentage of the probabil... |
| Q08 | - |  |  | SI | Higher scores indicate a potential problem with al... |
| Q09 | - |  |  | SI | • While a total score of 2 or higher is considered... |
| Q10 | - |  |  | SI | • The CAGE questionnaire score is only the first s... |
| Q11 | - |  |  | SI | Score |
| Q12 | - |  |  | SI | Classification |
| Q13 | - |  |  | SI | 0 |
| Q14 | - |  |  | SI | Normal |
| Q15 | - |  |  | SI | 1 |
| Q16 | - |  |  | SI | Consider further evaluation |
| Q17 | - |  |  | SI | 2 - 4 |
| Q18 | - |  |  | SI | Considered clinically significant and warrants / i... |
| Q19 | - |  |  | SI | 0: Normal |
| Q20 | - |  |  | SI | 1: Consider further evaluation |
| Q21 | - |  |  | SI | 2 - 4: Considered clinically significant |
| Q22 | - |  |  | SI | The CAGE alcohol screening tool is a questionnaire... |
| Q23 | - |  |  | SI | Date |
| Q24 | - |  |  | SI | Time |
| Q25 | - |  |  | SI | Do you drink? |
| Q26 | - |  |  | SI | Regardless of what the score is, it is NOT a diagn... |
| QUESAnaDR | - |  |  | SI | Anaesthesia |
| QUESAnaOperationDR | - |  |  | SI | Operation |
| QUESConsultDR | - |  |  | SI | Consult |
| QUESCopiedComments | - |  |  | SI | Copied Comments |
| QUESCopiedDate | - |  |  | SI | Copied Date |
| QUESCopiedEpDR | - |  |  | SI | Copied Episode |
| QUESCopiedSourceDR | - |  |  | SI | Copied Source DR |
| QUESCopiedTime | - |  |  | SI | Copied Time |
| QUESCopiedUserDR | - |  |  | SI | Copied User |
| QUESCreateDate | - |  |  | SI | Creation Date |
| QUESCreateTime | - |  |  | SI | Creation Time |
| QUESCreateUserDR | - |  |  | SI | Creation User |
| QUESDate | - |  |  | SI | Last Update Date |
| QUESErrorReasonDR | - |  |  | SI | Error Reason |
| QUESFHResidentDR | - |  |  | SI | Resident |
| QUESMRClinicalPathWaysDR | - |  |  | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | - |  |  | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | - |  |  | SI | Order Execution |
| QUESORPreanaestheticConsultDR | - |  |  | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | - |  |  | SI | Observation Entry |
| QUESOperRoomDR | - |  |  | SI | Operating Room |
| QUESPAAdmDR | - |  |  | SI | Admission |
| QUESPAAdverseEventDR | - |  |  | SI | Adverse Event |
| QUESPAPatMasDR | - |  |  | SI | Patient |
| QUESPAPregnancyDR | - |  |  | SI | Pregnancy |
| QUESPAWaitingListDR | - |  |  | SI | Waiting List |
| QUESPathwayItemDR | - |  |  | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | - |  |  | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | - |  |  | SI | Appointments |
| QUESRBApptOutcomeDR | - |  |  | SI | Appointment Outcome |
| QUESRBApptSlotDR | - |  |  | SI | Appointment Slot |
| QUESReasonForCorrectionDR | - |  |  | SI | Reason for Correction |
| QUESSSUserDefWindowDR | - |  |  | SI | Questionnaire |
| QUESScore | - |  |  | SI | Score |
| QUESSecondUserDR | - |  |  | SI | Second Signature |
| QUESStatusDR | - |  |  | SI | Status |
| QUESTextResultDR | - |  |  | SI | Text Result |
| QUESTime | - |  |  | SI | Last Update Time |
| QUESTransactionDR | - |  |  | SI | Transaction |
| QUESUserDR | - |  |  | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*