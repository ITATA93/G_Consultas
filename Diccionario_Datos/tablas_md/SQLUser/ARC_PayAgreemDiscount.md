# SQLUser.ARC_PayAgreemDiscount

**Schema:** SQLUser
**Columnas:** 83
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Pagos**. Tarifas y facturación.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DISC_ParRef | bigint | PK |  | NO | ARC_PaymentAgreement Parent Reference |
| DISC_ARCIM_DR | varchar |  | FK | SI | Des Ref ARCIM |
| DISC_BillGroup_DR | bigint |  | FK | SI | Des Ref BillGroup |
| DISC_BillSub_DR | varchar |  | FK | SI | Des Ref BillSub |
| DISC_Childsub | double |  |  | NO | Childsub |
| DISC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DISC_CreatedDate | date |  |  | SI | Created Date |
| DISC_CreatedTime | time |  |  | SI | Created Time |
| DISC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DISC_DateFrom | date |  |  | SI | Date From |
| DISC_DateTo | date |  |  | SI | Date To |
| DISC_DayFrom | double |  |  | SI | Day From |
| DISC_DayTo | double |  |  | SI | Day To |
| DISC_Discount | double |  |  | SI | % Discount |
| DISC_DiscountAmount | double |  |  | SI | DiscountAmount |
| DISC_DocSpec_DR | bigint |  | FK | SI | Des Ref DocSpec |
| DISC_EpisBill_DR | bigint |  | FK | SI | Des Ref EpisBill |
| DISC_EpisSubType_DR | bigint |  | FK | SI | Des Ref EpisSubType |
| DISC_EpisodeType | varchar |  |  | SI | EpisodeType |
| DISC_Hosp_DR | bigint |  | FK | SI | Des Ref Hospital |
| DISC_Location_DR | bigint |  | FK | SI | Des Ref Location |
| DISC_PayorOnly | varchar |  |  | SI | Payor Only |
| DISC_PayorShare | varchar |  |  | SI | PayorShare |
| DISC_RowId | varchar |  |  | NO | - |
| DISC_UpdatedDate | date |  |  | SI | Updated Date |
| DISC_UpdatedTime | time |  |  | SI | Updated Time |
| DISC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Edad > 45 años |
| Q02 | - |  |  | SI | Sin antecedentes de convulsiones o epilepsia |
| Q03 | - |  |  | SI | Tiempo de evolución de los sintomas > 24 horas |
| Q04 | - |  |  | SI | Al comienzo el paciente no está en la silla de rue... |
| Q05 | - |  |  | SI | Glicemia entre 60 y 400 mg. |
| Q06 | - |  |  | SI | Asimentría evidente (derecha vs izquierda) |
| Q07 | - |  |  | SI | Sonrisa / Gesticulación Facial |
| Q08 | - |  |  | SI | Prensión Derecha |
| Q09 | - |  |  | SI | Prensión Izquierda |
| Q10 | - |  |  | SI | Fuerza del Miembro Superior Derecho |
| Q11 | - |  |  | SI | Fuerza del Miembro Superior Izquierdo |
| Q12 | - |  |  | SI | Resultado |
| Q12ObsDR | - |  |  | SI | Resultado DR |
| Q13 | - |  |  | SI | Recomendaciones |
| Q14 | - |  |  | SI | Examen Físico |
| Q15 | - |  |  | SI | (*) Considerar Examen Físico para responder esta p... |
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