# SQLUser.PAC_VacDisOrders

**Schema:** SQLUser
**Columnas:** 108
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ORD_ParRef | bigint | PK |  | NO | PAC_VaccinationDesease Parent Reference |
| ChildQ20DR | - |  |  | SI | Child Reference: Primary cannula site check |
| ORD_ARCIM_DR | varchar |  | FK | SI | Des Ref ARCItmMast |
| ORD_Childsub | double |  |  | NO | Childsub |
| ORD_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ORD_CreatedDate | date |  |  | SI | Created Date |
| ORD_CreatedTime | time |  |  | SI | Created Time |
| ORD_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ORD_DateFrom | date |  |  | SI | Date From |
| ORD_DateTo | date |  |  | SI | Date To |
| ORD_Default | varchar |  |  | SI | Default |
| ORD_Dosage | varchar |  |  | SI | Dosage |
| ORD_LowerAge | double |  |  | SI | LowerAge |
| ORD_LowerAgePeriod | varchar |  |  | SI | LowerAgePeriod |
| ORD_RowId | varchar |  |  | NO | - |
| ORD_Sex_DR | bigint |  | FK | SI | Des Ref CTSex |
| ORD_UpdatedDate | date |  |  | SI | Updated Date |
| ORD_UpdatedTime | time |  |  | SI | Updated Time |
| ORD_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ORD_UpperAge | double |  |  | SI | UpperAge |
| ORD_UpperAgePeriod | varchar |  |  | SI | UpperAgePeriod |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Block region under review |
| Q04 | - |  |  | SI | Eye block |
| Q05 | - |  |  | SI | Other eye block details |
| Q06 | - |  |  | SI | Brachial plexus block |
| Q07 | - |  |  | SI | Other brachial plexus block details |
| Q08 | - |  |  | SI | Forearm block |
| Q09 | - |  |  | SI | Other forearm block details |
| Q10 | - |  |  | SI | Back block |
| Q11 | - |  |  | SI | Other back block details |
| Q12 | - |  |  | SI | Chest block |
| Q13 | - |  |  | SI | Other chest block details |
| Q14 | - |  |  | SI | Abdominal block |
| Q15 | - |  |  | SI | Other abdominal block details |
| Q16 | - |  |  | SI | Lower limb block |
| Q17 | - |  |  | SI | Other lower limb block details |
| Q18 | - |  |  | SI | Other block region under review details |
| Q19 | - |  |  | SI | Laterality |
| Q21 | - |  |  | SI | Secondary block performed |
| Q22 | - |  |  | SI | Secondary block region under review |
| Q23 | - |  |  | SI | Secondary eye block |
| Q24 | - |  |  | SI | Other secondary eye block details |
| Q25 | - |  |  | SI | Secondary brachial plexus block |
| Q26 | - |  |  | SI | Other secondary brachial plexus block details |
| Q27 | - |  |  | SI | Secondary forearm block |
| Q28 | - |  |  | SI | Other secondary forearm block details |
| Q29 | - |  |  | SI | Secondary back block |
| Q30 | - |  |  | SI | Other secondary back block details |
| Q31 | - |  |  | SI | Secondary chest block |
| Q32 | - |  |  | SI | Other secondary chest block details |
| Q33 | - |  |  | SI | Secondary abdominal block |
| Q34 | - |  |  | SI | Other secondary abdominal block details |
| Q35 | - |  |  | SI | Secondary lower limb block |
| Q36 | - |  |  | SI | Other secondary lower limb block details |
| Q37 | - |  |  | SI | Specify other secondary details |
| Q38 | - |  |  | SI | Laterality (secondary block) |
| Q39 | - |  |  | SI | Secondary Site Check |
| Q41 | - |  |  | SI | Pain score at rest |
| Q41ObsDR | - |  |  | SI | Pain score at rest DR |
| Q42 | - |  |  | SI | Current pain |
| Q43 | - |  |  | SI | Patient's pain description |
| Q44 | - |  |  | SI | Numbness, reduced feeling or reduced sensation |
| Q45 | - |  |  | SI | Patient's sensation description |
| Q46 | - |  |  | SI | Weakness |
| Q47 | - |  |  | SI | Patient's weakness description |
| Q48 | - |  |  | SI | Review notes |
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