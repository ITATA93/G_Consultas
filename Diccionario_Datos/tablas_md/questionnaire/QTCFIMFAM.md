# questionnaire.QTCFIMFAM

> UK FIM FAM Assessment

**Schema:** questionnaire
**Columnas:** 152
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* UK FIM FAM Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Stage of assessment |
| Q02 | varchar |  |  | SI | Scale |
| Q03 | varchar |  |  | SI | 7 : Complete independence (timely, safely) |
| Q04 | varchar |  |  | SI | 6 : Modified independence (extra time, devices, sa... |
| Q05 | varchar |  |  | SI | 5 : Supervision or set up (cuing, coaxing, prompti... |
| Q06 | varchar |  |  | SI | 4 : Minimal assist (performs 75% or more of task) |
| Q07 | varchar |  |  | SI | 3 : Moderate assist (performs 50% - 74% of task) |
| Q08 | varchar |  |  | SI | 2 : Maximal assist (performs 25% to 49% of task) |
| Q09 | varchar |  |  | SI | 1 : Total assist (performs less than 25% of task) |
| Q10 | numeric |  |  | SI | Eating |
| Q100 | varchar |  |  | SI | 2. Turner-Stokes L, Nyein K, Turner-Stokes T, Gate... |
| Q101 | varchar |  |  | SI | 3. Turner-Stokes L; UK FIM+FAM Users Group. The UK... |
| Q102 | varchar |  |  | SI | https://kcl.ac.uk/nmpc/assets/rehab/fimfam-manual.... |
| Q103 | varchar |  |  | SI | TOTAL MOTOR SUBSCORE |
| Q104 | varchar |  |  | SI | TOTAL COGNITIVE SUBSCORE |
| Q105 | varchar |  |  | SI | Self Care |
| Q106 | varchar |  |  | SI | Bladder / Bowels |
| Q107 | varchar |  |  | SI | Locomotion |
| Q108 | varchar |  |  | SI | Communication |
| Q109 | varchar |  |  | SI | Cognitive / Psychosocial |
| Q11 | numeric |  |  | SI | Swallowing |
| Q110 | varchar |  |  | SI | TOTAL EXTENDED ACTIVITIES OF DAILY LIVING |
| Q111 | varchar |  |  | SI | UK FIM + FAM TOTAL SCORE |
| Q12 | numeric |  |  | SI | Grooming |
| Q13 | numeric |  |  | SI | Bathing |
| Q14 | numeric |  |  | SI | Dressing upper body |
| Q15 | numeric |  |  | SI | Dressing lower body |
| Q16 | numeric |  |  | SI | Toileting |
| Q17 | varchar |  |  | SI | Score both level of assistance and frequency |
| Q18 | numeric |  |  | SI | Bladder - level of assistance |
| Q19 | numeric |  |  | SI | Bladder - frequency of accidents |
| Q20 | numeric |  |  | SI | Bowel - level of assistance |
| Q21 | numeric |  |  | SI | Bowel - frequency of accidents |
| Q22 | numeric |  |  | SI | Bed, chair, wheelchair transfer |
| Q23 | numeric |  |  | SI | Toilet transfer |
| Q24 | numeric |  |  | SI | Tub, shower transfer |
| Q25 | numeric |  |  | SI | Car transfer |
| Q26 | numeric |  |  | SI | Walking 'w' |
| Q27 | numeric |  |  | SI | Wheelchair 'c' |
| Q28 | varchar |  |  | SI | Frequent mode of locomotion |
| Q29 | numeric |  |  | SI | Stairs |
| Q30 | numeric |  |  | SI | Community mobility |
| Q31 | varchar |  |  | SI | Indicate usual mode |
| Q32 | numeric |  |  | SI | Comprehension |
| Q33 | numeric |  |  | SI | Expression |
| Q34 | numeric |  |  | SI | Reading |
| Q35 | numeric |  |  | SI | Writing |
| Q36 | numeric |  |  | SI | Speech intelligibility |
| Q37 | numeric |  |  | SI | Social interaction |
| Q38 | numeric |  |  | SI | Emotional status |
| Q39 | numeric |  |  | SI | Adjustment to limitations |
| Q40 | numeric |  |  | SI | Leisure activities |
| Q41 | numeric |  |  | SI | Problem solving |
| Q42 | numeric |  |  | SI | Memory |
| Q43 | numeric |  |  | SI | Orientation |
| Q44 | numeric |  |  | SI | Concentration |
| Q45 | numeric |  |  | SI | Safety awareness |
| Q46 | numeric |  |  | SI | Meal preparation |
| Q47 | numeric |  |  | SI | Laundry |
| Q48 | numeric |  |  | SI | Housework |
| Q49 | numeric |  |  | SI | Shopping |
| Q50 | numeric |  |  | SI | Financial management |
| Q51 | numeric |  |  | SI | Work / education |
| Q52 | date |  |  | SI | Date |
| Q53 | time |  |  | SI | Time |
| Q54 | varchar |  |  | SI | FIM FAM Total score |
| Q55 | varchar |  |  | SI | FIM FAM Total calculation - Bowel |
| Q56 | varchar |  |  | SI | Frequent mode of locomotion score |
| Q57 | varchar |  |  | SI | Eating |
| Q58 | varchar |  |  | SI | Swallowing |
| Q59 | varchar |  |  | SI | Grooming |
| Q60 | varchar |  |  | SI | Bathing |
| Q61 | varchar |  |  | SI | Dressing Upper Body |
| Q62 | varchar |  |  | SI | Dressing Lower Body |
| Q63 | varchar |  |  | SI | Toileting |
| Q64 | varchar |  |  | SI | Bladder Management - Level of Assistance |
| Q65 | varchar |  |  | SI | Bladder Management - Frequency of Accidents |
| Q66 | varchar |  |  | SI | Bowel Management - Level of Assistance |
| Q67 | varchar |  |  | SI | Bowel Management - Frequency of Accidents |
| Q68 | varchar |  |  | SI | Transfers - Bed, Chair, Wheelchair |
| Q69 | varchar |  |  | SI | Transfers - Toilet |
| Q70 | varchar |  |  | SI | Transfers - Tub or Shower |
| Q71 | varchar |  |  | SI | Transfers - Car |
| Q72 | varchar |  |  | SI | Locomotion - Walking |
| Q73 | varchar |  |  | SI | Locomotion - Wheelchair |
| Q74 | varchar |  |  | SI | Locomotion - Stairs |
| Q75 | varchar |  |  | SI | Community Mobility |
| Q76 | varchar |  |  | SI | Comprehension |
| Q77 | varchar |  |  | SI | Expression |
| Q78 | varchar |  |  | SI | Reading |
| Q79 | varchar |  |  | SI | Writing |
| Q80 | varchar |  |  | SI | Speech Intelligibility |
| Q81 | varchar |  |  | SI | Social Interaction |
| Q82 | varchar |  |  | SI | Emotional Status |
| Q83 | varchar |  |  | SI | Adjustments to Limitations |
| Q84 | varchar |  |  | SI | Use of Leisure Time |
| Q85 | varchar |  |  | SI | Problem Solving |
| Q86 | varchar |  |  | SI | Memory |
| Q87 | varchar |  |  | SI | Orientation |
| Q88 | varchar |  |  | SI | Concentration |
| Q89 | varchar |  |  | SI | Safety Awareness |
| Q90 | varchar |  |  | SI | Meal Preparation |
| Q91 | varchar |  |  | SI | Laundry |
| Q92 | varchar |  |  | SI | Housework |
| Q93 | varchar |  |  | SI | Shopping |
| Q94 | varchar |  |  | SI | Home Finances |
| Q95 | varchar |  |  | SI | Work / Education |
| Q96 | varchar |  |  | SI | The UK FIM+FAM is an instrument for the functional... |
| Q97 | varchar |  |  | SI | The UK FIM+FAM was originally described in 1999 [2... |
| Q98 | varchar |  |  | SI | 1. Hall KM, Hamilton BB, Gordon WA, Zasler ND. Cha... |
| Q99 | varchar |  |  | SI | J Head Trauma Rehab 1993;8:60–74. |
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

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*