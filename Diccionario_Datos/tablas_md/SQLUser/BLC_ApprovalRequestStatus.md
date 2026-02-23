# SQLUser.BLC_ApprovalRequestStatus

**Schema:** SQLUser
**Columnas:** 84
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| APPREQST_RowId | bigint | PK |  | NO | - |
| APPREQST_AllowAmendOrdItem | varchar |  |  | SI | Allowed to Amend Order Item |
| APPREQST_ApplyDefaultTariff | varchar |  |  | SI | Apply Default Tariff |
| APPREQST_ApprovalComments | varchar |  |  | SI | Approval Comments |
| APPREQST_ApprovalExpired | varchar |  |  | SI | Approval Expired |
| APPREQST_Closed | varchar |  |  | SI | Approval Request Closed |
| APPREQST_Code | varchar |  |  | NO | Code |
| APPREQST_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| APPREQST_Colour | varchar |  |  | SI | Colour |
| APPREQST_CreatedDate | date |  |  | SI | Created Date |
| APPREQST_CreatedTime | time |  |  | SI | Created Time |
| APPREQST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| APPREQST_DateFrom | date |  |  | SI | Date From |
| APPREQST_DateTo | date |  |  | SI | Date To |
| APPREQST_DefaultInitial | varchar |  |  | SI | Default Initial |
| APPREQST_Desc | varchar |  |  | NO | Description |
| APPREQST_DisableMessageQtyPack | varchar |  |  | SI | Disable Message: Quantity Packed More Than Approve... |
| APPREQST_Exclude | varchar |  |  | SI | Exclude |
| APPREQST_Extension | varchar |  |  | SI | Extension |
| APPREQST_FinApprOverride | varchar |  |  | SI | Finance Approval Override |
| APPREQST_NoInclEpisTopUpCalc | varchar |  |  | SI | Do Not Include Episode in Top Up Calculation |
| APPREQST_NotRequired | varchar |  |  | SI | Approval No Longer Required |
| APPREQST_Owner | varchar |  |  | SI | Owner |
| APPREQST_PayorApprStatus | varchar |  |  | SI | Payor Approval Status |
| APPREQST_RequestTypes | varchar |  |  | SI | Approval Request Types |
| APPREQST_TopUpApproval | varchar |  |  | SI | Top Up Approval |
| APPREQST_UpdatedDate | date |  |  | SI | Updated Date |
| APPREQST_UpdatedTime | time |  |  | SI | Updated Time |
| APPREQST_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Resultado |
| Q01ObsDR | - |  |  | SI | Resultado DR |
| Q02 | - |  |  | SI | I. Anamnesis |
| Q03 | - |  |  | SI | ¿El niño(a) presenta una condición que disminuya s... |
| Q04 | - |  |  | SI | ¿El niño(a) presenta situación de discapacidad? |
| Q05 | - |  |  | SI | II. Dieta |
| Q06 | - |  |  | SI | ¿Cuántas veces al día el niño(a) ingiere alimentos... |
| Q07 | - |  |  | SI | ¿En qué momento el niño(a) realiza la ingesta de a... |
| Q08 | - |  |  | SI | Si el niño(a) toma mamadera, ¿Cuántas veces se que... |
| Q09 | - |  |  | SI | III. Higiene |
| Q10 | - |  |  | SI | ¿Cuántas veces al día el niño(a) se lava los dient... |
| Q11 | - |  |  | SI | ¿El niño o niña, se lava los dientes antes de ir a... |
| Q12 | - |  |  | SI | Los padres y/o cuidadores, ¿Ayudan al niño(a) a la... |
| Q13 | - |  |  | SI | IV. Motivación de los Padres / Cuidadores |
| Q14 | - |  |  | SI | Luego de las preguntas anteriores, según usted (de... |
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