# SQLUser.BLC_BillNumberSetup

**Schema:** SQLUser
**Columnas:** 84
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Banco de Sangre**. Gestión de hemoderivados.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| NUM_RowId | bigint | PK |  | NO | - |
| NUM_BillCounter_DR | bigint |  | FK | SI | Des Ref BillCounter |
| NUM_BillRefund | varchar |  |  | SI | Bill/Refund |
| NUM_CashierLocation_DR | bigint |  | FK | SI | Des Ref CTLOC |
| NUM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| NUM_CreatedDate | date |  |  | SI | Created Date |
| NUM_CreatedTime | time |  |  | SI | Created Time |
| NUM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| NUM_DateFrom | date |  |  | SI | DateFrom |
| NUM_DateTo | date |  |  | SI | DateTo |
| NUM_DepositHospital_DR | bigint |  | FK | SI | Deposit Hospital - Des Ref CTHospital |
| NUM_EpisSubtype_DR | bigint |  | FK | SI | Des Ref EpisSubtype |
| NUM_EpisodeType | varchar |  |  | SI | Episode Type |
| NUM_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| NUM_InsType_DR | bigint |  | FK | SI | Des Ref ARCInsuranceType |
| NUM_Owner | varchar |  |  | SI | Owner |
| NUM_PayorGroup_DR | bigint |  | FK | SI | Des Ref ARCPayorGroup |
| NUM_PayorType | varchar |  |  | SI | PayorType |
| NUM_Rank | double |  |  | SI | Rank |
| NUM_UpdatedDate | date |  |  | SI | Updated Date |
| NUM_UpdatedTime | time |  |  | SI | Updated Time |
| NUM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| NUM_Value | varchar |  |  | SI | Value |
| NUM_Way | varchar |  |  | SI | Way |
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
| Q17 | - |  |  | SI | ¿Utiliza el niño o niña pasta con flúor? |
| Q18 | - |  |  | SI | VI. Motivación de los Padres / Cuidadores |
| Q19 | - |  |  | SI | Luego de las preguntas anteriores, según usted (de... |
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