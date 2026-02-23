# questionnaire.QTCENDOPAC

> Endoscopy Pre Admission Check

**Schema:** questionnaire
**Columnas:** 97
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Endoscopy Pre Admission Check

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | date |  |  | SI | Date / Time of pre admission assessment |
| Q04 | time |  |  | SI | Time of pre admission assessment |
| Q05 | varchar |  |  | SI | Pre admission assessment conducted by |
| Q06 | varchar |  |  | SI | Patient's previous notes reviewed |
| Q07 | varchar |  |  | SI | National resident |
| Q08 | varchar |  |  | SI | Interpreter required |
| Q09 | varchar |  |  | SI | Referral type |
| Q10 | varchar |  |  | SI | Hospital admission (overnight) in last six months |
| Q11 | varchar |  |  | SI | Hospital admission comments |
| Q12 | varchar |  |  | SI | Indications for procedure |
| Q13 | varchar |  |  | SI | History of heart disease |
| Q14 | varchar |  |  | SI | Comments |
| Q15 | varchar |  |  | SI | History of hypertension / hypotension |
| Q16 | varchar |  |  | SI | Comments |
| Q17 | varchar |  |  | SI | Is the patient on anticoagulants? |
| Q18 | varchar |  |  | SI | Nurse anticoagulant assessment completed |
| Q19 | varchar |  |  | SI | Anti-coagulant information provided to the patient |
| Q20 | varchar |  |  | SI | Comments |
| Q21 | varchar |  |  | SI | History of organ transplant / immunosuppression |
| Q22 | varchar |  |  | SI | Comments |
| Q23 | varchar |  |  | SI | History of infectious disease |
| Q24 | varchar |  |  | SI | Comments |
| Q25 | varchar |  |  | SI | History of respiratory disease |
| Q26 | varchar |  |  | SI | Comments |
| Q27 | varchar |  |  | SI | History of diabetes |
| Q28 | varchar |  |  | SI | Comments |
| Q29 | varchar |  |  | SI | Diabetes information provided to the patient |
| Q30 | varchar |  |  | SI | Allergies / Sensitivities status confirmed |
| Q31 | varchar |  |  | SI | Comments |
| Q32 | varchar |  |  | SI | Significant surgical history |
| Q33 | varchar |  |  | SI | Comments |
| Q34 | varchar |  |  | SI | Significant family history |
| Q35 | varchar |  |  | SI | Comments |
| Q36 | varchar |  |  | SI | Patient medical history documentation status |
| Q37 | varchar |  |  | SI | Patient has read the endoscopy information leaflet... |
| Q38 | varchar |  |  | SI | Patient has watched the  information video provide... |
| Q39 | varchar |  |  | SI | Patient provided opportunity to ask questions |
| Q40 | varchar |  |  | SI | Patient requested further information from doctor |
| Q41 | varchar |  |  | SI | Details of request |
| Q42 | varchar |  |  | SI | Patient advised not to drive a motor vehicle post ... |
| Q43 | varchar |  |  | SI | Patient advised bed rails will be in situ in recov... |
| Q44 | varchar |  |  | SI | Procedure risks and complications explained |
| Q45 | varchar |  |  | SI | Procedure preparation and diet discussed with pati... |
| Q46 | varchar |  |  | SI | Preparation comments |
| Q47 | varchar |  |  | SI | Consent discussed with patient |
| Q48 | varchar |  |  | SI | Covid questions completed |
| Q49 | varchar |  |  | SI | Details of any positive Covid responses |
| Q50 | varchar |  |  | SI | Prostheses |
| Q51 | varchar |  |  | SI | Prostheses comments |
| Q52 | varchar |  |  | SI | Mobility |
| Q53 | varchar |  |  | SI | Special nursing needs |
| Q54 | varchar |  |  | SI | Dietary requirements |
| Q55 | varchar |  |  | SI | Requires further patient assessment |
| Q56 | varchar |  |  | SI | Comments and further considerations |
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