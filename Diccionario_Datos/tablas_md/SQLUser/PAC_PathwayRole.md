# SQLUser.PAC_PathwayRole

**Schema:** SQLUser
**Columnas:** 98
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PACPR_ParRef | bigint | PK |  | NO | Parent Reference |
| ChildQ30DR | - |  |  | SI | Child Reference: Bone mineral density |
| PACPR_Childsub | double |  |  | NO | Childsub |
| PACPR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PACPR_CreatedDate | date |  |  | SI | Created Date |
| PACPR_CreatedTime | time |  |  | SI | Created Time |
| PACPR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PACPR_Mandatory | varchar |  |  | SI | Mandatory |
| PACPR_Role_DR | bigint |  | FK | SI | Multidisciplinary Team Role |
| PACPR_RowId | varchar |  |  | NO | - |
| PACPR_UpdatedDate | date |  |  | SI | Updated Date |
| PACPR_UpdatedTime | time |  |  | SI | Updated Time |
| PACPR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Assessment type |
| Q02 | - |  |  | SI | Assessment date |
| Q03 | - |  |  | SI | Assessment time |
| Q04 | - |  |  | SI | Osteoporosis diagnosis established |
| Q05 | - |  |  | SI | Previous osteoporosis diagnosis |
| Q06 | - |  |  | SI | New fragility fracture |
| Q07 | - |  |  | SI | Identify risk factors for fractures and falls |
| Q08 | - |  |  | SI | Prior fracture after age 50 years |
| Q09 | - |  |  | SI | Other fracture, specify |
| Q10 | - |  |  | SI | Prolonged glucocorticoid use |
| Q11 | - |  |  | SI | Parental hip fracture |
| Q12 | - |  |  | SI | Rheumatoid arthritis |
| Q13 | - |  |  | SI | Menopause at age <45 years |
| Q14 | - |  |  | SI | Current smoker |
| Q15 | - |  |  | SI | Consumes 3 units (oz.) alcohol/day |
| Q16 | - |  |  | SI | Has fallen 2 times in past 12 months |
| Q17 | - |  |  | SI | Low body weight (<60 kg) |
| Q18 | - |  |  | SI | Major weight loss |
| Q19 | - |  |  | SI | Diet + supplement calcium intake 1200 mg/day |
| Q20 | - |  |  | SI | A. Assess balance and gait for fracture risk |
| Q21 | - |  |  | SI | Can patient rise from chair without using arms and... |
| Q22 | - |  |  | SI | B. Screening for vertebral fracture |
| Q23 | - |  |  | SI | Current height (cm) |
| Q23ObsDR | - |  |  | SI | Current height (cm) DR |
| Q24 | - |  |  | SI | Prospective height loss > 2 cm |
| Q25 | - |  |  | SI | Historical height loss > 6 cm |
| Q26 | - |  |  | SI | Rib-pelvis distance ≥ 2 fingers |
| Q27 | - |  |  | SI | Occiput-wall distance > 5 cm |
| Q28 | - |  |  | SI | If Yes to any, order PA lateral spine x-ray to rul... |
| Q29 | - |  |  | SI | Lab test done and reviewed |
| Q33 | - |  |  | SI | Previous risk |
| Q34 | - |  |  | SI | Current risk |
| Q35 | - |  |  | SI | Low risk |
| Q36 | - |  |  | SI | No pharmacotherapy indicated |
| Q37 | - |  |  | SI | Reassessment in 1-3 years |
| Q38 | - |  |  | SI | Moderate risk |
| Q39 | - |  |  | SI | Consider pharmacotherapy if patient has at least o... |
| Q40 | - |  |  | SI | High risk |
| Q41 | - |  |  | SI | OR one fragility fracture hip/spine |
| Q42 | - |  |  | SI | OR more than one fragility fracture |
| Q43 | - |  |  | SI | Start pharmacotherapy |
| Q44 | - |  |  | SI | T-score fermoral neck (female) |
| Q45 | - |  |  | SI | T-score fermoral neck (male) |
| Q46 | - |  |  | SI | Date |
| Q47 | - |  |  | SI | Time |
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