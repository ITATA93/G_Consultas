# SQLUser.PA_AdmEstDischargeHistory

**Schema:** SQLUser
**Columnas:** 77
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Admisión de Pacientes**. Registra episodios de atención hospitalaria. Histórico de cambios.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ESTDIS_ParRef | bigint | PK |  | NO | PA_Adm Parent Reference |
| ESTDIS_Childsub | double |  |  | NO | Childsub |
| ESTDIS_DateUpdated | date |  |  | SI | Date Updated |
| ESTDIS_EstDate | date |  |  | SI | Est Date |
| ESTDIS_EstTime | time |  |  | SI | EstTime |
| ESTDIS_HospitalUpdated_DR | bigint |  | FK | SI | Des Ref HospitalUpdated |
| ESTDIS_RowId | varchar |  |  | NO | - |
| ESTDIS_TimeUpdated | time |  |  | SI | Time Updated |
| ESTDIS_UserUpdated_DR | bigint |  | FK | SI | UserUpdated |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Are you evaluating a patient with stroke? |
| Q04 | - |  |  | SI | This tool is not indicated |
| Q05 | - |  |  | SI | Diastolic Blood Pressure (mmHg) |
| Q06 | - |  |  | SI | Has the patient been vomiting? |
| Q07 | - |  |  | SI | Does the patient have a headache within 2 hours of... |
| Q08 | - |  |  | SI | Does the patient have a history of angina, diabete... |
| Q09 | - |  |  | SI | Patient's level of consciousness |
| Q10 | - |  |  | SI | Original Score |
| Q11 | - |  |  | SI | Please indicate which apply (optional) |
| Q12 | - |  |  | SI | Simplified Score |
| Q13 | - |  |  | SI | Score |
| Q14 | - |  |  | SI | Classification |
| Q15 | - |  |  | SI | The legend is reflective of the Simplified Score |
| Q16 | - |  |  | SI | > +1 |
| Q17 | - |  |  | SI | > +1: Indicative of cerebral haemorrhage |
| Q18 | - |  |  | SI | < -1 |
| Q19 | - |  |  | SI | < -1: Indicative of cerebral infarction |
| Q20 | - |  |  | SI | -1 to +1 |
| Q21 | - |  |  | SI | -1 to +1: Uncertain diagnosis |
| Q22 | - |  |  | SI | Indicative of cerebral haemorrhage |
| Q23 | - |  |  | SI | Indicative of cerebral infarction |
| Q24 | - |  |  | SI | Uncertain diagnosis |
| Q25 | - |  |  | SI | Total Score |
| Q26 | - |  |  | SI | The Siriraj Stroke Score, developed by Niphon Poun... |
| Q27 | - |  |  | SI | Original Score |
| Q28 | - |  |  | SI | Simplified Score |
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