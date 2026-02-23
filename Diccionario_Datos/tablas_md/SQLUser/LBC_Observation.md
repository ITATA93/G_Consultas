# SQLUser.LBC_Observation

**Schema:** SQLUser
**Columnas:** 139
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCO_RowID | bigint | PK |  | NO | - |
| ChildQ54DR | - |  |  | SI | Child Reference: Ulcer examination |
| LBCO_Code | varchar |  |  | NO | Code |
| LBCO_CodeTableTags | varchar |  |  | SI | List of code table tags |
| LBCO_CreatedDate | date |  |  | SI | Created Date |
| LBCO_CreatedTime | time |  |  | SI | Created Time |
| LBCO_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCO_DateFrom | date |  |  | SI | Date Active From |
| LBCO_DateTo | date |  |  | SI | Date Active To |
| LBCO_Desc | varchar |  |  | NO | Description |
| LBCO_Owner | varchar |  |  | SI | Owner |
| LBCO_Protocol_DR | bigint |  | FK | SI | SubProtocol Handler |
| LBCO_Type | varchar |  |  | SI | Observation Type |
| LBCO_UpdatedDate | date |  |  | SI | Updated Date |
| LBCO_UpdatedTime | time |  |  | SI | Updated Time |
| LBCO_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Diabetes Complication Status |
| Q04 | - |  |  | SI | Eye review date |
| Q05 | - |  |  | SI | Eye review outcome |
| Q06 | - |  |  | SI | Macular oedema |
| Q07 | - |  |  | SI | Previous treatment |
| Q08 | - |  |  | SI | Laser treatment |
| Q09 | - |  |  | SI | Injections |
| Q10 | - |  |  | SI | Chronic kidney disease |
| Q11 | - |  |  | SI | Albuminuria test |
| Q12 | - |  |  | SI | Urine ACR or 24h urine protein date |
| Q13 | - |  |  | SI | Urine ACR or 24h urine protein result |
| Q14 | - |  |  | SI | Glomerular filtration rate (eGFR) date |
| Q15 | - |  |  | SI | eGFR result |
| Q16 | - |  |  | SI | Neuropathy |
| Q17 | - |  |  | SI | Examination findings |
| Q18 | - |  |  | SI | Sensory |
| Q19 | - |  |  | SI | Motor |
| Q20 | - |  |  | SI | Peripheral vascular disease |
| Q21 | - |  |  | SI | Symptoms |
| Q22 | - |  |  | SI | Which side, what muscle group |
| Q23 | - |  |  | SI | Pain location |
| Q24 | - |  |  | SI | Ulcer location |
| Q25 | - |  |  | SI | Examination findings |
| Q26 | - |  |  | SI | Femoral pulse |
| Q27 | - |  |  | SI | Popliteal pulse |
| Q28 | - |  |  | SI | Posterior tibial pulse |
| Q29 | - |  |  | SI | Dorsalis pedis pulse |
| Q30 | - |  |  | SI | Trophic changes |
| Q31 | - |  |  | SI | Ulcer grade (University of Texas system) |
| Q32 | - |  |  | SI | Ulcer stage (University of Texas system) |
| Q33 | - |  |  | SI | Imaging |
| Q34 | - |  |  | SI | Foot review date |
| Q35 | - |  |  | SI | Foot review outcome |
| Q36 | - |  |  | SI | Wound |
| Q37 | - |  |  | SI | Ischaemia - Toe pressure / TCPO2 |
| Q38 | - |  |  | SI | Foot infection |
| Q39 | - |  |  | SI | Acanthosis nigricans |
| Q40 | - |  |  | SI | Previous laser treatment |
| Q41 | - |  |  | SI | Previous injections |
| Q42 | - |  |  | SI | Ophthalmic review notes |
| Q43 | - |  |  | SI | Kidney function review date |
| Q44 | - |  |  | SI | Kidney disease review notes |
| Q45 | - |  |  | SI | Neuropathy notes |
| Q46 | - |  |  | SI | Peripheral vascular disease (PVD) symptom review |
| Q47 | - |  |  | SI | Claudication |
| Q48 | - |  |  | SI | Laterality |
| Q49 | - |  |  | SI | Muscle group(s) involved |
| Q50 | - |  |  | SI | Rest pain |
| Q51 | - |  |  | SI | Pain score at rest |
| Q52 | - |  |  | SI | Pain location |
| Q53 | - |  |  | SI | Non-healing ulcer(s) |
| Q55 | - |  |  | SI | Skin examination |
| Q56 | - |  |  | SI | Pulses examination |
| Q57 | - |  |  | SI | PVD review notes |
| Q58 | - |  |  | SI | Right Foot |
| Q59 | - |  |  | SI | Left Foot |
| Q60 | - |  |  | SI | Right foot wound |
| Q61 | - |  |  | SI | Left foot wound |
| Q62 | - |  |  | SI | Right foot ischaemia - Toe pressure / TCPO2 |
| Q63 | - |  |  | SI | Left foot ischaemia - Toe pressure / TCPO2 |
| Q64 | - |  |  | SI | Right foot infection |
| Q65 | - |  |  | SI | Left foot infection |
| Q66 | - |  |  | SI | Foot review notes |
| Q67 | - |  |  | SI | Date of last annual review of management and compl... |
| Q68 | - |  |  | SI | Diabetes complication status notes |
| Q69 | - |  |  | SI | Eye review outcome |
| Q70 | - |  |  | SI | Wound |
| Q71 | - |  |  | SI | Ischaemia Toe pressure / TCPO2 |
| Q72 | - |  |  | SI | Foot infection |
| Q73 | - |  |  | SI | Right Foot |
| Q74 | - |  |  | SI | Right Foot |
| Q75 | - |  |  | SI | Right Foot |
| Q76 | - |  |  | SI | Left Foot |
| Q77 | - |  |  | SI | Left Foot |
| Q78 | - |  |  | SI | Left Foot |
| Q79 | - |  |  | SI | Wound |
| Q80 | - |  |  | SI | Sensory loss |
| Q81 | - |  |  | SI | Monofilament (10 g semmes weinstein monofilament) |
| Q82 | - |  |  | SI | Vibration (128Hz tuning fork) |
| Q83 | - |  |  | SI | Pin prick |
| Q84 | - |  |  | SI | Joint position sense |
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