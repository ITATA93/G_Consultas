# SQLUser.DICOM_Image

**Schema:** SQLUser
**Columnas:** 72
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Imágenes Diagnósticas**. Radiología y estudios de imagen.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DCIMG_RowID | varchar | PK |  | NO | - |
| DCIMG_Deleted | varchar |  |  | SI | Image deleted |
| DCIMG_ImageFileName | varchar |  |  | SI | Image File Name |
| DCIMG_ImageNumber | varchar |  |  | SI | Image Number |
| DCIMG_OeOrdRes_DR | varchar |  | FK | SI | Des Ref OeOrdRes |
| DCIMG_SOPInstanceUID | varchar |  |  | NO | Image SOP Instance UID |
| DCIMG_Series_DR | varchar |  | FK | SI | Series DR |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Discharge destination: abode type |
| Q04 | - |  |  | SI | Discharge destination: area |
| Q05 | - |  |  | SI | Other discharge area |
| Q06 | - |  |  | SI | Does dwelling have air-conditioning? |
| Q07 | - |  |  | SI | Who will assist them at home? |
| Q08 | - |  |  | SI | Dressing care location |
| Q09 | - |  |  | SI | Location details |
| Q10 | - |  |  | SI | Discharge destination notes |
| Q11 | - |  |  | SI | Date of dressing in situ at discharge |
| Q12 | - |  |  | SI | Type of dressing in situ at discharge |
| Q13 | - |  |  | SI | Has the patient been educated about care of dressi... |
| Q14 | - |  |  | SI | Has the patient been measured for pressure garment... |
| Q15 | - |  |  | SI | Has patient received patient educational material? |
| Q16 | - |  |  | SI | Occupational therapy has reviewed the patient prio... |
| Q17 | - |  |  | SI | Items supplied to the patient |
| Q18 | - |  |  | SI | Other (please specify) |
| Q19 | - |  |  | SI | Discharge check notes |
| Q20 | - |  |  | SI | Date of outpatient follow up clinic appointment |
| Q21 | - |  |  | SI | Date of outpatient follow up clinic appointment |
| Q22 | - |  |  | SI | Appointment information given to patient |
| Q23 | - |  |  | SI | Does patient require assistance for transport to a... |
| Q24 | - |  |  | SI | Transport arranged? |
| Q25 | - |  |  | SI | Follow up notes |
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