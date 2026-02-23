# SQLUser.OE_OrdSnomedCodes

**Schema:** SQLUser
**Columnas:** 126
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Órdenes Médicas**. Solicitudes de exámenes, procedimientos, etc.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SNO_ParRef | varchar | PK |  | NO | OE_OrdItem Parent Reference |
| ChildQ22DR | - |  |  | SI | Child Reference: Superficial Reflexes |
| Q01 | - |  |  | SI | Previous Physical Therapy Services |
| Q02 | - |  |  | SI | Previous Functional Status |
| Q03 | - |  |  | SI | Occupation |
| Q04 | - |  |  | SI | Place of Residence |
| Q05 | - |  |  | SI | Lives with |
| Q06 | - |  |  | SI | Floors |
| Q07 | - |  |  | SI | Stairs |
| Q08 | - |  |  | SI | Marital Status |
| Q09 | - |  |  | SI | No. of children |
| Q10 | - |  |  | SI | Hand Dominance |
| Q11 | - |  |  | SI | Precautions |
| Q12 | - |  |  | SI | Patient Goals / Concerns |
| Q13 | - |  |  | SI | Orientation |
| Q14 | - |  |  | SI | Speech |
| Q15 | - |  |  | SI | Hearing |
| Q16 | - |  |  | SI | Best Gaze |
| Q17 | - |  |  | SI | Visual Field (Right) |
| Q18 | - |  |  | SI | Visual Field (Left) |
| Q19 | - |  |  | SI | Involuntary Movements |
| Q20 | - |  |  | SI | Tremor |
| Q21 | - |  |  | SI | Other Involuntary Movements |
| Q37 | - |  |  | SI | Deformities |
| Q38 | - |  |  | SI | Comments |
| Q39 | - |  |  | SI | Contractures |
| Q40 | - |  |  | SI | Comments |
| Q42 | - |  |  | SI | Functional Ambulation Score |
| Q43 | - |  |  | SI | Score |
| Q44 | - |  |  | SI | Category |
| Q45 | - |  |  | SI | 0 |
| Q46 | - |  |  | SI | Nonfunctional Ambulation |
| Q47 | - |  |  | SI | Patient cannot ambulate, ambulates in parallel bar... |
| Q48 | - |  |  | SI | 1 |
| Q49 | - |  |  | SI | Ambulator-Dependence for Physical Assisstance Leve... |
| Q50 | - |  |  | SI | Patient requires manual contacts of no more than o... |
| Q51 | - |  |  | SI | Manual contacts are continuous and necessary to su... |
| Q52 | - |  |  | SI | 2 |
| Q53 | - |  |  | SI | Ambulator-Dependent for Physical Assisstance Level... |
| Q54 | - |  |  | SI | Patient requires manual contact of no more than on... |
| Q55 | - |  |  | SI | 3 |
| Q56 | - |  |  | SI | Ambulator-Dependent for Supervision |
| Q57 | - |  |  | SI | Patient can physically ambulate on level surfaces ... |
| Q58 | - |  |  | SI | or the need for verbal cuing to complete the task |
| Q59 | - |  |  | SI | 4 |
| Q60 | - |  |  | SI | Ambulator-Independent Level Surfaces only |
| Q61 | - |  |  | SI | Patient can ambulate independently on level surfac... |
| Q62 | - |  |  | SI | 5 |
| Q63 | - |  |  | SI | Ambulator-Independent |
| Q64 | - |  |  | SI | Patient can ambulate independently on non level an... |
| Q65 | - |  |  | SI | Pattern |
| Q66 | - |  |  | SI | Stairs |
| Q67 | - |  |  | SI | Problems List |
| Q68 | - |  |  | SI | Rehabilitation Potential |
| Q69 | - |  |  | SI | Family / Patient involved in and verbalized unders... |
| Q70 | - |  |  | SI | Treatment Plan |
| Q71 | - |  |  | SI | Short Term Goals Period |
| Q72 | - |  |  | SI | Short Term Goals |
| Q73 | - |  |  | SI | Long Term Goals Period |
| Q74 | - |  |  | SI | Long Term Goals |
| Q75 | - |  |  | SI | Treatment |
| Q76 | - |  |  | SI | Re evaluation Date |
| Q77 | - |  |  | SI | Treatment Options |
| Q78 | - |  |  | SI | Assistive Device |
| Q79 | - |  |  | SI | Other |
| Q80 | - |  |  | SI | Social History |
| Q81 | - |  |  | SI | Mental Status |
| Q82 | - |  |  | SI | Behaviour / Cognitive |
| Q83 | - |  |  | SI | Vision |
| Q84 | - |  |  | SI | Visual Field |
| Q85 | - |  |  | SI | Involuntary Movements |
| Q86 | - |  |  | SI | Rolling |
| Q87 | - |  |  | SI | Bridging |
| Q88 | - |  |  | SI | Lying to Sitting |
| Q89 | - |  |  | SI | Shifting Hip |
| Q90 | - |  |  | SI | Sitting to Standing |
| Q91 | - |  |  | SI | Transfer Bed to Wheelchair |
| Q92 | - |  |  | SI | Functional Mobility |
| Q93 | - |  |  | SI | Comments |
| Q94 | - |  |  | SI | Comments |
| Q95 | - |  |  | SI | Comments |
| Q96 | - |  |  | SI | Date |
| Q97 | - |  |  | SI | Time |
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
| SNO_Childsub | double |  |  | NO | Childsub |
| SNO_RowId | varchar |  |  | NO | - |
| SNO_SnomedCode | varchar |  |  | SI | SnomedCode |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*