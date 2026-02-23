# SQLUser.OE_OrdDiagnos

**Schema:** SQLUser
**Columnas:** 113
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Órdenes Médicas**. Solicitudes de exámenes, procedimientos, etc.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DIA_ParRef | varchar | PK |  | NO | OE_OrdItem Parent Reference |
| DIA_Childsub | double |  |  | NO | Childsub |
| DIA_MRDiagnos_DR | varchar |  | FK | SI | Des Ref MRDiagnos |
| DIA_RowId | varchar |  |  | NO | - |
| Q42 | - |  |  | SI | SELF CARE ITEMS |
| Q43 | - |  |  | SI | SPHINCTER CONTROL |
| Q44 | - |  |  | SI | MOBILITY ITEMS |
| Q45 | - |  |  | SI | LOCOMOTION |
| Q46 | - |  |  | SI | COMMUNICATION ITEMS |
| Q47 | - |  |  | SI | PSYCHOSOCIAL ADJUSTMENT |
| Q48 | - |  |  | SI | COGNITIVE FUNCTION |
| Q49 | - |  |  | SI | *FAM items |
| Q50 | - |  |  | SI | Care provider |
| Q51 | - |  |  | SI | Care provider type |
| Q52 | - |  |  | SI | Signature |
| Q52UDt | - |  |  | SI | Signature Last Updated Date |
| Q52UTm | - |  |  | SI | Signature Last Updated Time |
| Q53 | - |  |  | SI | Scale: |
| Q54 | - |  |  | SI | 7 : Complete independence (timely, safely) |
| Q55 | - |  |  | SI | 6 : Modified independence (extra time, devices) |
| Q56 | - |  |  | SI | 5 : Supervision (cuing, coaxing, prompting) |
| Q57 | - |  |  | SI | 4 : Minimal assist (performs 75% or more of task) |
| Q58 | - |  |  | SI | 3 : Moderate assist (performs 50%-74% of task) |
| Q59 | - |  |  | SI | 2 : Maximal assist (performs 25% to 49% of task) |
| Q60 | - |  |  | SI | 1 : Total assist (performs less than 25% of task) |
| Q61 | - |  |  | SI | Self care score |
| Q62 | - |  |  | SI | Sphincter control score |
| Q63 | - |  |  | SI | Mobility score |
| Q64 | - |  |  | SI | Locomotion score |
| Q65 | - |  |  | SI | Communication score |
| Q66 | - |  |  | SI | Psychosocial adjustment score |
| Q67 | - |  |  | SI | Cognitive function score |
| Q68 | - |  |  | SI | Care provider type |
| Q69 | - |  |  | SI | *FAM items |
| Q70 | - |  |  | SI | 5 : Supervision (cueing, coaxing, prompting) |
| QAUB3A | - |  |  | SI | Impairment |
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
| QVFIM1 | - |  |  | SI | Assessment date |
| QVFIM10 | - |  |  | SI | Bladder management |
| QVFIM11 | - |  |  | SI | Bowel management |
| QVFIM12 | - |  |  | SI | Transfers - bed / chair / wheelchair |
| QVFIM13 | - |  |  | SI | Transfers - toilet |
| QVFIM14 | - |  |  | SI | Transfers - bath / shower |
| QVFIM15 | - |  |  | SI | Walk / Wheelchair |
| QVFIM16 | - |  |  | SI | Stairs |
| QVFIM17 | - |  |  | SI | Comprehension |
| QVFIM18 | - |  |  | SI | Expression |
| QVFIM19 | - |  |  | SI | Social interaction |
| QVFIM2 | - |  |  | SI | Time of assessment |
| QVFIM20 | - |  |  | SI | Memory |
| QVFIM21 | - |  |  | SI | FIM + FAM score total |
| QVFIM22 | - |  |  | SI | Stage of assessment |
| QVFIM23 | - |  |  | SI | Community access* |
| QVFIM28 | - |  |  | SI | Swallowing* |
| QVFIM29 | - |  |  | SI | Car transfer* |
| QVFIM3 | - |  |  | SI | Eating |
| QVFIM30 | - |  |  | SI | Indicate locomotion |
| QVFIM31 | - |  |  | SI | Indicate comprehension |
| QVFIM32 | - |  |  | SI | Indicate expression |
| QVFIM33 | - |  |  | SI | Reading* |
| QVFIM34 | - |  |  | SI | Writing* |
| QVFIM35 | - |  |  | SI | Speech intelligibility* |
| QVFIM36 | - |  |  | SI | Emotional status* |
| QVFIM37 | - |  |  | SI | Adjustment to limitations* |
| QVFIM38 | - |  |  | SI | Employability* |
| QVFIM39 | - |  |  | SI | Orientation* |
| QVFIM4 | - |  |  | SI | Grooming |
| QVFIM40 | - |  |  | SI | Attention* |
| QVFIM41 | - |  |  | SI | Safety judgement* |
| QVFIM5 | - |  |  | SI | Bathing |
| QVFIM6 | - |  |  | SI | Dressing upper body |
| QVFIM7 | - |  |  | SI | Dressing lower body |
| QVFIM8 | - |  |  | SI | Problem solving |
| QVFIM9 | - |  |  | SI | Toileting |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*