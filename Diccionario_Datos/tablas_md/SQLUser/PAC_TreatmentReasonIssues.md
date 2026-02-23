# SQLUser.PAC_TreatmentReasonIssues

**Schema:** SQLUser
**Columnas:** 153
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PACTI_ParRef | bigint | PK |  | NO | PACTreatmentReason Parent Reference |
| PACTI_Childsub | double |  |  | NO | Childsub |
| PACTI_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PACTI_CreatedDate | date |  |  | SI | Created Date |
| PACTI_CreatedTime | time |  |  | SI | Created Time |
| PACTI_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PACTI_Default | varchar |  |  | SI | Default Issue |
| PACTI_Issues_DR | bigint |  | FK | SI | Des Ref NRCIssues |
| PACTI_RowId | varchar |  |  | NO | - |
| PACTI_UpdatedDate | date |  |  | SI | Updated Date |
| PACTI_UpdatedTime | time |  |  | SI | Updated Time |
| PACTI_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Reason for presentation |
| Q04 | - |  |  | SI | Dominant arm |
| Q05 | - |  |  | SI | Left arm |
| Q06 | - |  |  | SI | Right arm |
| Q07 | - |  |  | SI | Lower 1/3 forearm size (mm) |
| Q08 | - |  |  | SI | Middle 1/3 forearm size (mm) |
| Q09 | - |  |  | SI | Upper 1/3 forearm size (mm) |
| Q10 | - |  |  | SI | Upper arm cephalic vein size (mm) |
| Q100 | - |  |  | SI | Right arm |
| Q101 | - |  |  | SI | Right arm |
| Q11 | - |  |  | SI | Upper arm basilic vein size (mm) |
| Q12 | - |  |  | SI | Fistula vein notes |
| Q13 | - |  |  | SI | Lower 1/3 forearm size, left arm (mm) |
| Q14 | - |  |  | SI | Middle 1/3 forearm size, left arm (mm) |
| Q15 | - |  |  | SI | Upper 1/3 forearm size, left arm (mm) |
| Q16 | - |  |  | SI | Upper arm cephalic vein size, left arm (mm) |
| Q17 | - |  |  | SI | Upper arm basilic vein size, left arm (mm) |
| Q18 | - |  |  | SI | Left arm fistula vein measurement notes |
| Q19 | - |  |  | SI | Lower 1/3 forearm size, right arm (mm) |
| Q20 | - |  |  | SI | Middle 1/3 forearm size, right arm (mm) |
| Q21 | - |  |  | SI | Upper 1/3 forearm size, right arm (mm) |
| Q22 | - |  |  | SI | Upper arm cephalic vein size, right arm (mm) |
| Q23 | - |  |  | SI | Upper arm basilic vein size, right arm (mm) |
| Q24 | - |  |  | SI | Right arm fistula vein measurement notes |
| Q25 | - |  |  | SI | Fistula artery measurement |
| Q26 | - |  |  | SI | Left arm |
| Q27 | - |  |  | SI | Right arm |
| Q28 | - |  |  | SI | Radial artery (mm) |
| Q29 | - |  |  | SI | Radial artery calcified |
| Q30 | - |  |  | SI | Radial artery flow rate (mm/sec) |
| Q31 | - |  |  | SI | Brachial artery (mm) |
| Q32 | - |  |  | SI | Brachial artery calcified |
| Q33 | - |  |  | SI | Brachial artery flow rate (mm/sec) |
| Q34 | - |  |  | SI | Fistula artery notes |
| Q35 | - |  |  | SI | Radial artery, left arm (mm) |
| Q36 | - |  |  | SI | Radial artery, left arm - calcified |
| Q37 | - |  |  | SI | Radial artery flow rate, left arm (mm/sec) |
| Q38 | - |  |  | SI | Brachial artery, left arm (mm) |
| Q39 | - |  |  | SI | Brachia artery, left arm - calcified |
| Q40 | - |  |  | SI | Brachial artery flow rate, left arm (mm/sec) |
| Q41 | - |  |  | SI | Left fistula artery measurement notes |
| Q42 | - |  |  | SI | Radial artery, right arm (mm) |
| Q43 | - |  |  | SI | Radial artery, right arm - calcified |
| Q44 | - |  |  | SI | Radial artery flow rate, right arm (mm/sec) |
| Q45 | - |  |  | SI | Brachial artery, right arm (mm) |
| Q46 | - |  |  | SI | Brachial artery, right arm calcified |
| Q47 | - |  |  | SI | Brachial artery flow rate, right arm (mm/sec) |
| Q48 | - |  |  | SI | Right fistula artery measurement notes |
| Q49 | - |  |  | SI | Abdominal hernia |
| Q50 | - |  |  | SI | Other abdominal hernia |
| Q51 | - |  |  | SI | Peritoneal assessment including significant surgic... |
| Q52 | - |  |  | SI | Outcome |
| Q53 | - |  |  | SI | Other outcome details |
| Q54 | - |  |  | SI | Outcome decision notes |
| Q55 | - |  |  | SI | Plan for access outcome |
| Q56 | - |  |  | SI | Consent for planned procedure completed |
| Q57 | - |  |  | SI | Consent notes |
| Q58 | - |  |  | SI | Access team follow up required |
| Q59 | - |  |  | SI | Other access team follow up notes |
| Q60 | - |  |  | SI | Assessment outcome notes |
| Q61 | - |  |  | SI | Fistula vein measurement |
| Q62 | - |  |  | SI | Fistula vein measurement |
| Q63 | - |  |  | SI | Fistula vein measurement |
| Q64 | - |  |  | SI | Fistula vein measurement |
| Q65 | - |  |  | SI | Fistula vein measurement |
| Q66 | - |  |  | SI | Fistula vein measurement |
| Q67 | - |  |  | SI | Fistula vein measurement |
| Q68 | - |  |  | SI | Fistula artery measurement |
| Q69 | - |  |  | SI | Fistula artery measurement |
| Q70 | - |  |  | SI | Fistula artery measurement |
| Q71 | - |  |  | SI | Fistula artery measurement |
| Q72 | - |  |  | SI | Fistula artery measurement |
| Q73 | - |  |  | SI | Fistula artery measurement |
| Q74 | - |  |  | SI | Fistula artery measurement |
| Q75 | - |  |  | SI | Fistula artery measurement |
| Q76 | - |  |  | SI | Left arm |
| Q77 | - |  |  | SI | Left arm |
| Q78 | - |  |  | SI | Left arm |
| Q79 | - |  |  | SI | Left arm |
| Q80 | - |  |  | SI | Left arm |
| Q81 | - |  |  | SI | Left arm |
| Q82 | - |  |  | SI | Left arm |
| Q83 | - |  |  | SI | Left arm |
| Q84 | - |  |  | SI | Left arm |
| Q85 | - |  |  | SI | Left arm |
| Q86 | - |  |  | SI | Left arm |
| Q87 | - |  |  | SI | Left arm |
| Q88 | - |  |  | SI | Left arm |
| Q89 | - |  |  | SI | Right arm |
| Q90 | - |  |  | SI | Right arm |
| Q91 | - |  |  | SI | Right arm |
| Q92 | - |  |  | SI | Right arm |
| Q93 | - |  |  | SI | Right arm |
| Q94 | - |  |  | SI | Right arm |
| Q95 | - |  |  | SI | Right arm |
| Q96 | - |  |  | SI | Right arm |
| Q97 | - |  |  | SI | Right arm |
| Q98 | - |  |  | SI | Right arm |
| Q99 | - |  |  | SI | Right arm |
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