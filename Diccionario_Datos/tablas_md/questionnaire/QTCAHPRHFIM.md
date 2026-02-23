# questionnaire.QTCAHPRHFIM

> Indice de Independencia Funcional e Indice Evaluación Funcional

**Schema:** questionnaire
**Columnas:** 110
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Indice de Independencia Funcional e Indice Evaluación Funcional

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q42 | varchar |  |  | SI | SELF CARE ITEMS |
| Q43 | varchar |  |  | SI | SPHINCTER CONTROL |
| Q44 | varchar |  |  | SI | MOBILITY ITEMS |
| Q45 | varchar |  |  | SI | LOCOMOTION |
| Q46 | varchar |  |  | SI | COMMUNICATION ITEMS |
| Q47 | varchar |  |  | SI | PSYCHOSOCIAL ADJUSTMENT |
| Q48 | varchar |  |  | SI | COGNITIVE FUNCTION |
| Q49 | varchar |  |  | SI | *FAM items |
| Q50 | varchar |  |  | SI | Care provider |
| Q51 | varchar |  |  | SI | Care provider type |
| Q52 | longvarbinary |  |  | SI | Signature |
| Q52UDt | date |  |  | SI | Signature Last Updated Date |
| Q52UTm | time |  |  | SI | Signature Last Updated Time |
| Q53 | varchar |  |  | SI | Scale: |
| Q54 | varchar |  |  | SI | 7 : Complete independence (timely, safely) |
| Q55 | varchar |  |  | SI | 6 : Modified independence (extra time, devices) |
| Q56 | varchar |  |  | SI | 5 : Supervision (cuing, coaxing, prompting) |
| Q57 | varchar |  |  | SI | 4 : Minimal assist (performs 75% or more of task) |
| Q58 | varchar |  |  | SI | 3 : Moderate assist (performs 50%-74% of task) |
| Q59 | varchar |  |  | SI | 2 : Maximal assist (performs 25% to 49% of task) |
| Q60 | varchar |  |  | SI | 1 : Total assist (performs less than 25% of task) |
| Q61 | varchar |  |  | SI | Self care score |
| Q62 | varchar |  |  | SI | Sphincter control score |
| Q63 | varchar |  |  | SI | Mobility score |
| Q64 | varchar |  |  | SI | Locomotion score |
| Q65 | varchar |  |  | SI | Communication score |
| Q66 | varchar |  |  | SI | Psychosocial adjustment score |
| Q67 | varchar |  |  | SI | Cognitive function score |
| Q68 | varchar |  |  | SI | Care provider type |
| Q69 | varchar |  |  | SI | *FAM items |
| Q70 | varchar |  |  | SI | 5 : Supervision (cueing, coaxing, prompting) |
| QAUB3A | varchar |  |  | SI | Impairment |
| QUESAnaDR | varchar |  | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar |  | FK | SI | Operation |
| QUESConsultDR | varchar |  | FK | SI | Consult |
| QUESCopiedComments | varchar |  |  | SI | Copied Comments |
| QUESCopiedDate | date |  |  | SI | Copied Date |
| QUESCopiedEpDR | bigint |  | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint |  | FK | SI | Copied Source DR |
| QUESCopiedTime | time |  |  | SI | Copied Time |
| QUESCopiedUserDR | bigint |  | FK | SI | Copied User |
| QUESCreateDate | date |  |  | SI | Creation Date |
| QUESCreateTime | time |  |  | SI | Creation Time |
| QUESCreateUserDR | bigint |  | FK | SI | Creation User |
| QUESDate | date |  |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint |  | FK | SI | Error Reason |
| QUESFHResidentDR | bigint |  | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar |  | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar |  | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar |  | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint |  | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar |  | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint |  | FK | SI | Operating Room |
| QUESPAAdmDR | bigint |  | FK | SI | Admission |
| QUESPAAdverseEventDR | varchar |  | FK | SI | Adverse Event |
| QUESPAPatMasDR | bigint |  | FK | SI | Patient |
| QUESPAPregnancyDR | bigint |  | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint |  | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar |  | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar |  | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar |  | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar |  | FK | SI | Appointment Outcome |
| QUESRBApptSlotDR | varchar |  | FK | SI | Appointment Slot |
| QUESReasonForCorrectionDR | bigint |  | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint |  | FK | SI | Questionnaire |
| QUESScore | varchar |  |  | SI | Score |
| QUESSecondUserDR | bigint |  | FK | SI | Second Signature |
| QUESStatusDR | bigint |  | FK | SI | Status |
| QUESTextResultDR | bigint |  | FK | SI | Text Result |
| QUESTime | time |  |  | SI | Last Update Time |
| QUESTransactionDR | varchar |  | FK | SI | Transaction |
| QUESUserDR | bigint |  | FK | SI | Last Update User |
| QVFIM1 | date |  |  | SI | Assessment date |
| QVFIM10 | numeric |  |  | SI | Bladder management |
| QVFIM11 | numeric |  |  | SI | Bowel management |
| QVFIM12 | numeric |  |  | SI | Transfers - bed / chair / wheelchair |
| QVFIM13 | numeric |  |  | SI | Transfers - toilet |
| QVFIM14 | numeric |  |  | SI | Transfers - bath / shower |
| QVFIM15 | numeric |  |  | SI | Walk / Wheelchair |
| QVFIM16 | numeric |  |  | SI | Stairs |
| QVFIM17 | numeric |  |  | SI | Comprehension |
| QVFIM18 | numeric |  |  | SI | Expression |
| QVFIM19 | numeric |  |  | SI | Social interaction |
| QVFIM2 | time |  |  | SI | Time of assessment |
| QVFIM20 | numeric |  |  | SI | Memory |
| QVFIM21 | varchar |  |  | SI | FIM + FAM score total |
| QVFIM22 | varchar |  |  | SI | Stage of assessment |
| QVFIM23 | numeric |  |  | SI | Community access* |
| QVFIM28 | numeric |  |  | SI | Swallowing* |
| QVFIM29 | numeric |  |  | SI | Car transfer* |
| QVFIM3 | numeric |  |  | SI | Eating |
| QVFIM30 | varchar |  |  | SI | Indicate locomotion |
| QVFIM31 | varchar |  |  | SI | Indicate comprehension |
| QVFIM32 | varchar |  |  | SI | Indicate expression |
| QVFIM33 | numeric |  |  | SI | Reading* |
| QVFIM34 | numeric |  |  | SI | Writing* |
| QVFIM35 | numeric |  |  | SI | Speech intelligibility* |
| QVFIM36 | numeric |  |  | SI | Emotional status* |
| QVFIM37 | numeric |  |  | SI | Adjustment to limitations* |
| QVFIM38 | numeric |  |  | SI | Employability* |
| QVFIM39 | numeric |  |  | SI | Orientation* |
| QVFIM4 | numeric |  |  | SI | Grooming |
| QVFIM40 | numeric |  |  | SI | Attention* |
| QVFIM41 | numeric |  |  | SI | Safety judgement* |
| QVFIM5 | numeric |  |  | SI | Bathing |
| QVFIM6 | numeric |  |  | SI | Dressing upper body |
| QVFIM7 | numeric |  |  | SI | Dressing lower body |
| QVFIM8 | numeric |  |  | SI | Problem solving |
| QVFIM9 | numeric |  |  | SI | Toileting |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*