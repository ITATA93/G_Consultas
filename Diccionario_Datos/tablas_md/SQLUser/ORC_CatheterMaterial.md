# SQLUser.ORC_CatheterMaterial

**Schema:** SQLUser
**Columnas:** 99
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTHMAT_RowId | bigint | PK |  | NO | - |
| CTHMAT_Code | varchar |  |  | NO | Code |
| CTHMAT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CTHMAT_CreatedDate | date |  |  | SI | Created Date |
| CTHMAT_CreatedTime | time |  |  | SI | Created Time |
| CTHMAT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CTHMAT_DateFrom | date |  |  | SI | Date From |
| CTHMAT_DateTo | date |  |  | SI | Date To |
| CTHMAT_Desc | varchar |  |  | NO | Description |
| CTHMAT_Owner | varchar |  |  | SI | Owner |
| CTHMAT_UpdatedDate | date |  |  | SI | Updated Date |
| CTHMAT_UpdatedTime | time |  |  | SI | Updated Time |
| CTHMAT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Respiratory problem |
| Q02 | - |  |  | SI | Other problems |
| Q03 | - |  |  | SI | Reason for request (please tick appropriate reason... |
| Q03A | - |  |  | SI | Other |
| Q04 | - |  |  | SI | Duration of smoking |
| Q05 | - |  |  | SI | months |
| Q06 | - |  |  | SI | years |
| Q07 | - |  |  | SI | No. of cigs/day |
| Q08 | - |  |  | SI | If ex-smoker: duration of smoking |
| Q09 | - |  |  | SI | months |
| Q10 | - |  |  | SI | years |
| Q11 | - |  |  | SI | Stopped |
| Q12 | - |  |  | SI | months |
| Q13 | - |  |  | SI | years |
| Q13A | - |  |  | SI | ago |
| Q14 | - |  |  | SI | History of Tuberculosis |
| Q15 | - |  |  | SI | History of Tuberculosis (if psoitive - when) |
| Q16 | - |  |  | SI | History of Tuberculosis (if psoitive - state) |
| Q17 | - |  |  | SI | History of exposure to asbestos |
| Q18 | - |  |  | SI | Other type of dust |
| Q18A | - |  |  | SI | Organic dust : Pigeon dropping |
| Q19 | - |  |  | SI | History of bronchial hyper responsiveness (cough /... |
| Q20 | - |  |  | SI | Dust |
| Q21 | - |  |  | SI | Strong perfumes |
| Q22 | - |  |  | SI | Incense |
| Q23 | - |  |  | SI | Insecticides |
| Q24 | - |  |  | SI | Cigarette smoke |
| Q25 | - |  |  | SI | History of upper respiratory tract problem |
| Q26 | - |  |  | SI | History of thoracic surgery |
| Q27 | - |  |  | SI | History of snoring |
| Q28 | - |  |  | SI | Duration of illness |
| Q28A | - |  |  | SI | Other |
| Q29 | - |  |  | SI | years |
| Q30 | - |  |  | SI | months |
| Q31 | - |  |  | SI | Productive cough |
| Q32 | - |  |  | SI | Nonproductive cough |
| Q33 | - |  |  | SI | Wheezing |
| Q34 | - |  |  | SI | Breathlessness at rest |
| Q35 | - |  |  | SI | Breathlessness during exertion |
| Q36 | - |  |  | SI | Wheeze |
| Q37 | - |  |  | SI | Crackles |
| Q38 | - |  |  | SI | Tachypnoea |
| Q39 | - |  |  | SI | Sputum - routine organism |
| Q40 | - |  |  | SI | Sputum - Acid Fast Bacilli |
| Q41 | - |  |  | SI | Medical Imaging (please enclose if Yes) |
| Q46 | - |  |  | SI | Other |
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