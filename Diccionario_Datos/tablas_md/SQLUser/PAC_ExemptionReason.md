# SQLUser.PAC_ExemptionReason

**Schema:** SQLUser
**Columnas:** 108
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EXR_RowId | bigint | PK |  | NO | - |
| EXR_ARCOS_DR | varchar |  | FK | SI | ARC_OrdSets DR |
| EXR_AuxInsType_DR | bigint |  | FK | SI | Plan DR |
| EXR_Code | varchar |  |  | NO | Code |
| EXR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| EXR_CreatedDate | date |  |  | SI | Created Date |
| EXR_CreatedTime | time |  |  | SI | Created Time |
| EXR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| EXR_Desc | varchar |  |  | NO | Description |
| EXR_InsType_DR | bigint |  | FK | SI | Payor DR |
| EXR_Owner | varchar |  |  | SI | Owner |
| EXR_Prefix | varchar |  |  | SI | Prefix |
| EXR_UpdatedDate | date |  |  | SI | Updated Date |
| EXR_UpdatedTime | time |  |  | SI | Updated Time |
| EXR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q1 | - |  |  | SI | Date |
| Q10 | - |  |  | SI | Weight |
| Q10ObsDR | - |  |  | SI | Weight DR |
| Q11 | - |  |  | SI | Height |
| Q11ObsDR | - |  |  | SI | Height DR |
| Q12 | - |  |  | SI | Body mass index |
| Q12ObsDR | - |  |  | SI | Body mass index DR |
| Q13 | - |  |  | SI | Fat (%) |
| Q14 | - |  |  | SI | Visceral fat (%) |
| Q15 | - |  |  | SI | Abdominal circumference (cm) |
| Q16 | - |  |  | SI | Hips circumference (cm) |
| Q17 | - |  |  | SI | Waist hip ratio |
| Q18 | - |  |  | SI | Gynecological examination |
| Q19 | - |  |  | SI | Papanicolaou test |
| Q2 | - |  |  | SI | Time |
| Q20 | - |  |  | SI | Previous test |
| Q21 | - |  |  | SI | Colposcopy |
| Q22 | - |  |  | SI | Mammography |
| Q23 | - |  |  | SI | Breast ultrasound |
| Q24 | - |  |  | SI | Computerized bone mineralometry |
| Q25 | - |  |  | SI | Indications |
| Q26 | - |  |  | SI | Therapeutic indications |
| Q27 | - |  |  | SI | Papanicolaou test date |
| Q28 | - |  |  | SI | Colposcopy date |
| Q29 | - |  |  | SI | Mammography date |
| Q3 | - |  |  | SI | Menopause |
| Q30 | - |  |  | SI | Breast ultrasound date |
| Q31 | - |  |  | SI | Computerized bone mineralometry date |
| Q32 | - |  |  | SI | Note |
| Q33 | - |  |  | SI | Papanicolaou test date |
| Q34 | - |  |  | SI | Colposcopy date |
| Q35 | - |  |  | SI | Mammography date |
| Q36 | - |  |  | SI | Breast ultrasound date |
| Q37 | - |  |  | SI | Computerized bone mineralometry date |
| Q38 | - |  |  | SI | Papanicolaou test result |
| Q39 | - |  |  | SI | Colposcopy result |
| Q4 | - |  |  | SI | Iatrogenic |
| Q40 | - |  |  | SI | Mammography result |
| Q41 | - |  |  | SI | Breast ultrasound result |
| Q42 | - |  |  | SI | Computerized bone mineralometry result |
| Q43 | - |  |  | SI | Pelvic ultrasound |
| Q44 | - |  |  | SI | Pelvic ultrasound date |
| Q45 | - |  |  | SI | Pelvic ultrasound result |
| Q46 | - |  |  | SI | Pelvic ultrasound |
| Q47 | - |  |  | SI | Summary of recent clinical events |
| Q48 | - |  |  | SI | Note |
| Q5 | - |  |  | SI | Menopause onset date |
| Q6 | - |  |  | SI | Menopausal transition |
| Q7 | - |  |  | SI | Hormone replacement therapy (HRT) |
| Q8 | - |  |  | SI | Arterial systolic |
| Q8ObsDR | - |  |  | SI | Arterial systolic DR |
| Q9 | - |  |  | SI | Arterial diastolic |
| Q9ObsDR | - |  |  | SI | Arterial diastolic DR |
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