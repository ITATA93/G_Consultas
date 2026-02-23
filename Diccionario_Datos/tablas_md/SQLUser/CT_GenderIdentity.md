# SQLUser.CT_GenderIdentity

**Schema:** SQLUser
**Columnas:** 146
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| GENID_RowId | bigint | PK |  | NO | - |
| GENID_Code | varchar |  |  | NO | Code |
| GENID_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| GENID_CreatedDate | date |  |  | SI | Created Date |
| GENID_CreatedTime | time |  |  | SI | Created Time |
| GENID_CreatedUser_DR | bigint |  | FK | SI | Created User |
| GENID_DateFrom | date |  |  | SI | Date From |
| GENID_DateTo | date |  |  | SI | Date To |
| GENID_Desc | varchar |  |  | NO | Description |
| GENID_Gender | varchar |  |  | SI | Gender |
| GENID_GroupCode | varchar |  |  | SI | Group Code |
| GENID_HL7Mapping | varchar |  |  | SI | HL7 Mapping |
| GENID_Owner | varchar |  |  | SI | Owner |
| GENID_UpdatedDate | date |  |  | SI | Updated Date |
| GENID_UpdatedTime | time |  |  | SI | Updated Time |
| GENID_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Hand Function |
| Q02 | - |  |  | SI | Hand Function Evaluation |
| Q03 | - |  |  | SI | Side |
| Q04 | - |  |  | SI | Reach Forward |
| Q05 | - |  |  | SI | Carry Out |
| Q06 | - |  |  | SI | Release |
| Q07 | - |  |  | SI | Spherical |
| Q08 | - |  |  | SI | Cylindrical |
| Q09 | - |  |  | SI | Hook |
| Q10 | - |  |  | SI | Lateral Pinch |
| Q11 | - |  |  | SI | Tripod pinch |
| Q12 | - |  |  | SI | Pad Pinch |
| Q13 | - |  |  | SI | Tip Pinch |
| Q14 | - |  |  | SI | Eye-Hand Coordination |
| Q15 | - |  |  | SI | In-Hand Manipulation |
| Q16 | - |  |  | SI | Hand Dexterity |
| Q17 | - |  |  | SI | Finger to Palm |
| Q18 | - |  |  | SI | Activities of Daily Living (ADL) |
| Q19 | - |  |  | SI | ADL Evaluation |
| Q20 | - |  |  | SI | Bed Mobility |
| Q21 | - |  |  | SI | Transfer |
| Q22 | - |  |  | SI | Locomotion |
| Q23 | - |  |  | SI | Toileting |
| Q24 | - |  |  | SI | Eating |
| Q25 | - |  |  | SI | Dressing |
| Q26 | - |  |  | SI | Bathing |
| Q27 | - |  |  | SI | Hygiene / Grooming |
| Q28 | - |  |  | SI | Swallowing |
| Q29 | - |  |  | SI | Swallowing Evaluation |
| Q30 | - |  |  | SI | Feeding by |
| Q31 | - |  |  | SI | Tracheostomy |
| Q32 | - |  |  | SI | Drooling |
| Q33 | - |  |  | SI | Lip Control |
| Q34 | - |  |  | SI | Tongue Movement |
| Q35 | - |  |  | SI | Jaw Control |
| Q36 | - |  |  | SI | Cough Reflex |
| Q37 | - |  |  | SI | Gag Reflex |
| Q38 | - |  |  | SI | Swallow Reflex |
| Q39 | - |  |  | SI | Bite Reflex |
| Q40 | - |  |  | SI | Swallowing Test |
| Q41 | - |  |  | SI | Cognitive and Perception |
| Q42 | - |  |  | SI | Cognitive and Perception Evaluation |
| Q43 | - |  |  | SI | Neglect |
| Q44 | - |  |  | SI | Memory (Short) |
| Q45 | - |  |  | SI | Memory (Long) |
| Q46 | - |  |  | SI | Orientation to Time |
| Q47 | - |  |  | SI | Orientation to Place |
| Q48 | - |  |  | SI | Object Identification |
| Q49 | - |  |  | SI | Spatial Relations |
| Q50 | - |  |  | SI | Utilization of Objects |
| Q51 | - |  |  | SI | Calculation |
| Q52 | - |  |  | SI | Copy Two-Dimensional |
| Q53 | - |  |  | SI | Attention Span |
| Q54 | - |  |  | SI | Fall Risk Assessment |
| Q55 | - |  |  | SI | Fall Risk |
| Q56 | - |  |  | SI | High Risk by |
| Q57 | - |  |  | SI | Fracture Risk |
| Q58 | - |  |  | SI | Pain Assessment |
| Q59 | - |  |  | SI | Does Patient have Pain? |
| Q60 | - |  |  | SI | Location |
| Q61 | - |  |  | SI | Assessment Tool |
| Q62 | - |  |  | SI | Pain Assessment Score |
| Q63 | - |  |  | SI | Characteristic of Pain |
| Q64 | - |  |  | SI | Other Characteristic |
| Q65 | - |  |  | SI | Frequency |
| Q66 | - |  |  | SI | Duration |
| Q67 | - |  |  | SI | Pain Re-Assessment Score |
| Q68 | - |  |  | SI | Goals and Planning |
| Q69 | - |  |  | SI | Goal No 1 |
| Q70 | - |  |  | SI | Type |
| Q71 | - |  |  | SI | Performance |
| Q72 | - |  |  | SI | Satisfaction |
| Q73 | - |  |  | SI | Goal No 2 |
| Q74 | - |  |  | SI | Type |
| Q75 | - |  |  | SI | Performance |
| Q76 | - |  |  | SI | Satisfaction |
| Q77 | - |  |  | SI | Goal No 3 |
| Q78 | - |  |  | SI | Type |
| Q79 | - |  |  | SI | Performance |
| Q80 | - |  |  | SI | Satisfaction |
| Q81 | - |  |  | SI | Goal No 4 |
| Q82 | - |  |  | SI | Type |
| Q83 | - |  |  | SI | Performance |
| Q84 | - |  |  | SI | Satisfaction |
| Q85 | - |  |  | SI | Intervention Plan |
| Q86 | - |  |  | SI | Re-Assessment Date |
| Q87 | - |  |  | SI | Instruction |
| Q88 | - |  |  | SI | Patient and/or Family was given and understood abo... |
| Q89 | - |  |  | SI | Need Reviewed |
| Q90 | - |  |  | SI | Goal |
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