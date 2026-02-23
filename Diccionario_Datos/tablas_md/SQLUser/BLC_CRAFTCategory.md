# SQLUser.BLC_CRAFTCategory

**Schema:** SQLUser
**Columnas:** 81
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Banco de Sangre**. Gestión de hemoderivados.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CRAFTC_RowId | bigint | PK |  | NO | - |
| CRAFTC_Code | varchar |  |  | NO | Code |
| CRAFTC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CRAFTC_CreatedDate | date |  |  | SI | Created Date |
| CRAFTC_CreatedTime | time |  |  | SI | Created Time |
| CRAFTC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CRAFTC_DHS_AverageLOS | double |  |  | SI | DHS AverageLOS |
| CRAFTC_DateFrom | date |  |  | SI | Date From |
| CRAFTC_DateTo | date |  |  | SI | Date To |
| CRAFTC_Desc | varchar |  |  | NO | Description |
| CRAFTC_HighInlierBoundary | double |  |  | SI | High Inlier Boundary |
| CRAFTC_HighOutlierPerDiem | double |  |  | SI | High Outlier PerDiem |
| CRAFTC_InlierWeight | double |  |  | SI | Inlier Weight |
| CRAFTC_LowInlierBoundary | double |  |  | SI | Low Inlier Boundary |
| CRAFTC_LowOutlierPerDiem | double |  |  | SI | Low Outlier Per Diem |
| CRAFTC_Owner | varchar |  |  | SI | Owner |
| CRAFTC_SameDayWeight | double |  |  | SI | Same Day Weight |
| CRAFTC_ShortStayWeight | double |  |  | SI | Short Stay Weight |
| CRAFTC_UpdatedDate | date |  |  | SI | Updated Date |
| CRAFTC_UpdatedTime | time |  |  | SI | Updated Time |
| CRAFTC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Resultado |
| Q01ObsDR | - |  |  | SI | Resultado DR |
| Q02 | - |  |  | SI | I. Anamnesis |
| Q03 | - |  |  | SI | ¿El niño(a) presenta una condición que disminuya s... |
| Q04 | - |  |  | SI | ¿El niño(a) presenta situación de discapacidad? |
| Q05 | - |  |  | SI | II. Condición Clínica |
| Q06 | - |  |  | SI | ¿Cuál es la historia de caries del niño(a)? |
| Q07 | - |  |  | SI | ¿Cuál es el estado de las encias del niño(a)? |
| Q08 | - |  |  | SI | III. Dieta |
| Q09 | - |  |  | SI | ¿Cuántas veces al día el niño(a) ingiere alimentos... |
| Q10 | - |  |  | SI | ¿En qué momento el niño(a) realiza la ingesta de a... |
| Q11 | - |  |  | SI | Si el niño(a) toma mamadera, ¿Cuántas veces se que... |
| Q12 | - |  |  | SI | IV. Higiene |
| Q13 | - |  |  | SI | ¿Cuántas veces al día el niño(a) se lava los dient... |
| Q14 | - |  |  | SI | ¿El niño o niña, se lava los dientes antes de ir a... |
| Q15 | - |  |  | SI | Los padres y/o cuidadores, ¿Ayudan al niño(a) a la... |
| Q16 | - |  |  | SI | V. Fluoruros |
| Q17 | - |  |  | SI | Luego de las preguntas anteriores, según usted (de... |
| Q18 | - |  |  | SI | VI. Motivación de los Padres / Cuidadores |
| Q19 | - |  |  | SI | ¿Utiliza el niño o niña pasta con flúor? |
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