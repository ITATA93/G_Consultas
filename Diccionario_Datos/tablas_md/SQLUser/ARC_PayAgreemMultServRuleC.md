# SQLUser.ARC_PayAgreemMultServRuleC

**Schema:** SQLUser
**Columnas:** 88
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Pagos**. Tarifas y facturación.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MSRULEC_ParRef | bigint | PK |  | NO | ARC_PaymentAgreement Parent Reference |
| MSRULEC_Amount | double |  |  | SI | Amount |
| MSRULEC_Childsub | double |  |  | NO | Childsub |
| MSRULEC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| MSRULEC_CreatedDate | date |  |  | SI | Created Date |
| MSRULEC_CreatedTime | time |  |  | SI | Created Time |
| MSRULEC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MSRULEC_DateFrom | date |  |  | SI | Date From |
| MSRULEC_DateTo | date |  |  | SI | Date To |
| MSRULEC_ItemCatNonConsult_DR | bigint |  | FK | SI | Des Ref ARCItemCat Non Consultation |
| MSRULEC_ItemCatRType_DR | bigint |  | FK | SI | Des Ref ARCItemCat RType |
| MSRULEC_RowId | varchar |  |  | NO | - |
| MSRULEC_UpdatedDate | date |  |  | SI | Updated Date |
| MSRULEC_UpdatedTime | time |  |  | SI | Updated Time |
| MSRULEC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Extremidad Superior Derecha (ESD) |
| Q02 | - |  |  | SI | Abducción de Hombro ESD |
| Q02ObsDR | - |  |  | SI | Abducción de Hombro ESD DR |
| Q03 | - |  |  | SI | Flexión de Codo ESD |
| Q03ObsDR | - |  |  | SI | Flexión de Codo ESD DR |
| Q04 | - |  |  | SI | Extensión de Muñeca ESD |
| Q04ObsDR | - |  |  | SI | Extensión de Muñeca ESD DR |
| Q05 | - |  |  | SI | Total ESD |
| Q06 | - |  |  | SI | Extremidad Superior Izquierda (ESI) |
| Q07 | - |  |  | SI | Abducción de Hombro ESI |
| Q07ObsDR | - |  |  | SI | Abducción de Hombro ESI DR |
| Q08 | - |  |  | SI | Flexión de Codo ESI |
| Q08ObsDR | - |  |  | SI | Flexión de Codo ESI DR |
| Q09 | - |  |  | SI | Extensión de Muñeca ESI |
| Q09ObsDR | - |  |  | SI | Extensión de Muñeca ESI DR |
| Q10 | - |  |  | SI | Extremidad Inferior Derecha (EID) |
| Q11 | - |  |  | SI | Flexión de Cadera EID |
| Q11ObsDR | - |  |  | SI | Flexión de Cadera EID DR |
| Q12 | - |  |  | SI | Extensión de Rodilla EID |
| Q12ObsDR | - |  |  | SI | Extensión de Rodilla EID DR |
| Q13 | - |  |  | SI | Dorsiflexión de Tobillo (Rodilla a 0°) EID |
| Q13ObsDR | - |  |  | SI | Dorsiflexión de Tobillo (Rodilla a 0°) EID DR |
| Q14 | - |  |  | SI | Extremidad Inferior Izquierda (EII) |
| Q15 | - |  |  | SI | Flexión de Cadera EII |
| Q15ObsDR | - |  |  | SI | Flexión de Cadera EII DR |
| Q16 | - |  |  | SI | Extensión de Rodilla EII |
| Q16ObsDR | - |  |  | SI | Extensión de Rodilla EII DR |
| Q17 | - |  |  | SI | Dorsiflexión de Tobillo (Rodilla a 0°) EII |
| Q17ObsDR | - |  |  | SI | Dorsiflexión de Tobillo (Rodilla a 0°) EII DR |
| Q18 | - |  |  | SI | Total ESI |
| Q19 | - |  |  | SI | Total EID |
| Q20 | - |  |  | SI | Total EII |
| Q21 | - |  |  | SI | Total Puntaje MRC |
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