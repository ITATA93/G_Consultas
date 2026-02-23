# SQLUser.PA_AdmReferralLocation

**Schema:** SQLUser
**Columnas:** 79
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Admisión de Pacientes**. Registra episodios de atención hospitalaria.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REFLOC_ParRef | bigint | PK |  | NO | PA_Adm Parent Reference |
| Q01 | - |  |  | SI | Age >= 65 |
| Q02 | - |  |  | SI | >= 3 Coronary Artery Disease (CAD) risk factors  (... |
| Q03 | - |  |  | SI | Known CAD (stenosis >= 50%) |
| Q04 | - |  |  | SI | Acetylsalicylic Acid (ASA) e.g. Aspirin use in pas... |
| Q05 | - |  |  | SI | Severe angina (>= 2 episodes in 24 hrs) |
| Q06 | - |  |  | SI | EKG ST changes >= 0.5mm |
| Q07 | - |  |  | SI | Positive cardiac marker |
| Q08 | - |  |  | SI | Score |
| Q09 | - |  |  | SI | Classification |
| Q10 | - |  |  | SI | 0 - 1 |
| Q11 | - |  |  | SI | 5% risk at 14 days of: all-cause mortality, new or... |
| Q12 | - |  |  | SI | 2 |
| Q13 | - |  |  | SI | 8% risk at 14 days of: all-cause mortality, new or... |
| Q14 | - |  |  | SI | 3 |
| Q15 | - |  |  | SI | 13% risk at 14 days of: all-cause mortality, new o... |
| Q16 | - |  |  | SI | 4 |
| Q17 | - |  |  | SI | 20% risk at 14 days of: all-cause mortality, new o... |
| Q18 | - |  |  | SI | 5 |
| Q19 | - |  |  | SI | 26% risk at 14 days of: all-cause mortality, new o... |
| Q20 | - |  |  | SI | 6 - 7 |
| Q21 | - |  |  | SI | 41% risk at 14 days of: all-cause mortality, new o... |
| Q22 | - |  |  | SI | 0 - 1: 5% risk at 14 days of: all-cause mortality,... |
| Q23 | - |  |  | SI | 2: 8% risk at 14 days of: all-cause mortality, new... |
| Q24 | - |  |  | SI | 3: 13% risk at 14 days of: all-cause mortality, ne... |
| Q25 | - |  |  | SI | 4: 20% risk at 14 days of: all-cause mortality, ne... |
| Q26 | - |  |  | SI | 5: 26% risk at 14 days of: all-cause mortality, ne... |
| Q27 | - |  |  | SI | 6 - 7: 41% risk at 14 days of: all-cause mortality... |
| Q28 | - |  |  | SI | The TIMI (Thrombolysis In Myocardial Infarction) R... |
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
| REFLOC_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC |
| REFLOC_Childsub | double |  |  | NO | Childsub |
| REFLOC_Date | date |  |  | SI | Date |
| REFLOC_Location | varchar |  |  | SI | Location |
| REFLOC_RowId | varchar |  |  | NO | - |
| REFLOC_Time | time |  |  | SI | Time |
| REFLOC_UpdateDate | date |  |  | SI | UpdateDate |
| REFLOC_UpdateTime | time |  |  | SI | UpdateTime |
| REFLOC_UpdateUserHospital_DR | bigint |  | FK | SI | Des Ref UpdateUserHospital |
| REFLOC_UpdateUser_DR | bigint |  | FK | SI | Des Ref UpdateUser |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*