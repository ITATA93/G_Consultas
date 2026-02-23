# SQLUser.PAC_SnomedSubsetOther

**Schema:** SQLUser
**Columnas:** 104
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SNOO_ParRef | bigint | PK |  | NO | PAC_SnomedSubset Parent Reference |
| ChildQ17DR | - |  |  | SI | Child Reference: Muscle tone |
| ID | varchar |  |  | NO | - |
| Q01 | - |  |  | SI | Reason for admission |
| Q02 | - |  |  | SI | Comments |
| Q03 | - |  |  | SI | Previous functional status |
| Q04 | - |  |  | SI | Previous physical therapies |
| Q05 | - |  |  | SI | Lives with |
| Q06 | - |  |  | SI | Mother's number of pregnacies |
| Q07 | - |  |  | SI | Respiratory function |
| Q08 | - |  |  | SI | Nutrition |
| Q09 | - |  |  | SI | Non - autonomous nutrition |
| Q10 | - |  |  | SI | Level cof consciousness (AVPU) |
| Q10ObsDR | - |  |  | SI | Level cof consciousness (AVPU) DR |
| Q11 | - |  |  | SI | Vision |
| Q12 | - |  |  | SI | Corneal reflex |
| Q13 | - |  |  | SI | Fixation |
| Q14 | - |  |  | SI | Following a target |
| Q15 | - |  |  | SI | Physical examination |
| Q16 | - |  |  | SI | Spontaneous posture |
| Q20 | - |  |  | SI | Musculo - skeletal deformities |
| Q21 | - |  |  | SI | Musculo - skeletal deformities |
| Q23 | - |  |  | SI | Motor skills |
| Q24 | - |  |  | SI | Head control |
| Q25 | - |  |  | SI | Trunk control |
| Q26 | - |  |  | SI | Hips control |
| Q27 | - |  |  | SI | Postural movements |
| Q28 | - |  |  | SI | Supine to the side |
| Q28ObsDR | - |  |  | SI | Supine to the side DR |
| Q29 | - |  |  | SI | Supine to sitting |
| Q29ObsDR | - |  |  | SI | Supine to sitting DR |
| Q30 | - |  |  | SI | Sitting to standing |
| Q30ObsDR | - |  |  | SI | Sitting to standing DR |
| Q31 | - |  |  | SI | Sitting position: Level of sitting scale |
| Q32 | - |  |  | SI | Walking assessment |
| Q33 | - |  |  | SI | Gait |
| Q34 | - |  |  | SI | Gait analysis |
| Q35 | - |  |  | SI | Manipulation |
| Q36 | - |  |  | SI | Manipulation type |
| Q37 | - |  |  | SI | Devices / Aids |
| Q38 | - |  |  | SI | Type of devices / aids |
| Q39 | - |  |  | SI | Pain |
| Q40 | - |  |  | SI | Other issues |
| Q41 | - |  |  | SI | Treatment plan |
| Q42 | - |  |  | SI | Treatment goals |
| Q43 | - |  |  | SI | Treatment options |
| Q44 | - |  |  | SI | Family involved in treatment plan |
| Q45 | - |  |  | SI | Family involvement |
| Q46 | - |  |  | SI | Comments |
| Q47 | - |  |  | SI | Date |
| Q48 | - |  |  | SI | Time |
| Q49 | - |  |  | SI | Respiratory function |
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
| SNOO_Childsub | double |  |  | NO | Childsub |
| SNOO_LinkedConceptID_DR | bigint |  | FK | SI | Des Ref SnomedConcept |
| SNOO_LinkedTermID_DR | bigint |  | FK | SI | Des Ref SnomedConcept |
| SNOO_MemberConceptID_DR | bigint |  | FK | SI | Des Ref SnomedConcept |
| SNOO_MemberStatus | varchar |  |  | SI | MemberStatus |
| SNOO_MemberTermID_DR | bigint |  | FK | SI | Des Ref SnomedDescription |
| _CreatedDate | date |  |  | SI | Created Date |
| _CreatedTime | time |  |  | SI | Created Time |
| _CreatedUser_DR | bigint |  | FK | SI | Created User |
| _UpdatedDate | date |  |  | SI | Updated Date |
| _UpdatedTime | time |  |  | SI | Updated Time |
| _UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*