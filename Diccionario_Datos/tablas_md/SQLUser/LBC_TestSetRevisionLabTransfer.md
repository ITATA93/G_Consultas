# SQLUser.LBC_TestSetRevisionLabTransfer

**Schema:** SQLUser
**Columnas:** 105
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCTSRLT_ParRef | bigint | PK |  | NO | Parent Reference LBCTestSetRevision DR |
| LBCTSRLT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCTSRLT_CurrentLocation_DR | bigint |  | FK | SI | Current Location |
| LBCTSRLT_DateFrom | date |  |  | SI | Effective date for the record |
| LBCTSRLT_DateTo | date |  |  | SI | Last day the record is active  |
| LBCTSRLT_DestinationLocation_DR | bigint |  | FK | SI | Destination Location |
| LBCTSRLT_DistinctSpecimenContainer | varchar |  |  | SI | Flag to indicated if the destination location requ... |
| LBCTSRLT_NotPriority | varchar |  |  | SI | Not Priority
Logically negate the selected Priori... |
| LBCTSRLT_Priority_DR | bigint |  | FK | SI | Test Set's Order Item Priority |
| LBCTSRLT_ReferralLaboratory_DR | bigint |  | FK | SI | Referral Laboratory |
| LBCTSRLT_RowID | varchar |  |  | NO | - |
| LBCTSRLT_Sequence | double |  |  | SI | Priority  Sequence |
| LBCTSRLT_SubjectType_DR | bigint |  | FK | SI | - |
| Q1 | - |  |  | SI | Fecha de Ingreso a Programa |
| Q10 | - |  |  | SI | Permanente |
| Q11 | - |  |  | SI | Esporádico |
| Q12 | - |  |  | SI | Anorexia |
| Q13 | - |  |  | SI | Enflaquecido |
| Q14 | - |  |  | SI | Caquexico |
| Q15 | - |  |  | SI | Ansiedad |
| Q16 | - |  |  | SI | Mareos |
| Q17 | - |  |  | SI | Temblor |
| Q18 | - |  |  | SI | Fatiga |
| Q19 | - |  |  | SI | Ictericia |
| Q2 | - |  |  | SI | Año Diagnóstico enfermedad |
| Q20 | - |  |  | SI | Linfidema |
| Q21 | - |  |  | SI | Edema |
| Q22 | - |  |  | SI | Ascitis |
| Q23 | - |  |  | SI | Náuseas |
| Q24 | - |  |  | SI | Vómitos |
| Q25 | - |  |  | SI | Hipo |
| Q26 | - |  |  | SI | Estreñimiento |
| Q27 | - |  |  | SI | Diarrea |
| Q28 | - |  |  | SI | Gastralgia |
| Q29 | - |  |  | SI | Disfagia |
| Q3 | - |  |  | SI | Centro Derivador |
| Q30 | - |  |  | SI | Cefalea |
| Q31 | - |  |  | SI | Disnea |
| Q32 | - |  |  | SI | Tos |
| Q33 | - |  |  | SI | Insomnio |
| Q34 | - |  |  | SI | Somnolencia |
| Q35 | - |  |  | SI | Letargo |
| Q36 | - |  |  | SI | Desorientacion |
| Q37 | - |  |  | SI | Prurito |
| Q38 | - |  |  | SI | Fistula |
| Q39 | - |  |  | SI | Ostomia |
| Q4 | - |  |  | SI | Fecha |
| Q40 | - |  |  | SI | Hemorragias |
| Q41 | - |  |  | SI | Disuria |
| Q48 | - |  |  | SI | Incontinencia |
| Q49 | - |  |  | SI | Localización del Dolor |
| Q5 | - |  |  | SI | Paciente |
| Q50 | - |  |  | SI | Quimioterapia |
| Q51 | - |  |  | SI | Radioterapia |
| Q52 | - |  |  | SI | Adiccion |
| Q53 | - |  |  | SI | Oxigenoterapia |
| Q54 | - |  |  | SI | Fecha |
| Q55 | - |  |  | SI | Fecha |
| Q56 | - |  |  | SI | Fecha |
| Q57 | - |  |  | SI | Fecha |
| Q6 | - |  |  | SI | Familia |
| Q7 | - |  |  | SI | EVA |
| Q8 | - |  |  | SI | Tipo de Dolor |
| Q9 | - |  |  | SI | Mixto |
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
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*