# SQLUser.OR_AnaestOrbitalBlock

**Schema:** SQLUser
**Columnas:** 155
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Pabellón Quirúrgico**. Gestión de cirugías.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ANAORB_ParRef | varchar | PK |  | NO | MR_Adm Parent Reference |
| ANAORB_Childsub | double |  |  | NO | Childsub |
| ANAORB_RowId | varchar |  |  | NO | - |
| ANAORB_Type_DR | bigint |  | FK | SI | Des Ref ORCOrbitalBlocks |
| Q01 | - |  |  | SI | Stage of assessment |
| Q02 | - |  |  | SI | Scale |
| Q03 | - |  |  | SI | 7 : Complete independence (timely, safely) |
| Q04 | - |  |  | SI | 6 : Modified independence (extra time, devices, sa... |
| Q05 | - |  |  | SI | 5 : Supervision or set up (cuing, coaxing, prompti... |
| Q06 | - |  |  | SI | 4 : Minimal assist (performs 75% or more of task) |
| Q07 | - |  |  | SI | 3 : Moderate assist (performs 50% - 74% of task) |
| Q08 | - |  |  | SI | 2 : Maximal assist (performs 25% to 49% of task) |
| Q09 | - |  |  | SI | 1 : Total assist (performs less than 25% of task) |
| Q10 | - |  |  | SI | Eating |
| Q100 | - |  |  | SI | 2. Turner-Stokes L, Nyein K, Turner-Stokes T, Gate... |
| Q101 | - |  |  | SI | 3. Turner-Stokes L |
| Q102 | - |  |  | SI | https://kcl.ac.uk/nmpc/assets/rehab/fimfam-manual.... |
| Q103 | - |  |  | SI | TOTAL MOTOR SUBSCORE |
| Q104 | - |  |  | SI | TOTAL COGNITIVE SUBSCORE |
| Q105 | - |  |  | SI | Self Care |
| Q106 | - |  |  | SI | Bladder / Bowels |
| Q107 | - |  |  | SI | Locomotion |
| Q108 | - |  |  | SI | Communication |
| Q109 | - |  |  | SI | Cognitive / Psychosocial |
| Q11 | - |  |  | SI | Swallowing |
| Q110 | - |  |  | SI | TOTAL EXTENDED ACTIVITIES OF DAILY LIVING |
| Q111 | - |  |  | SI | UK FIM + FAM TOTAL SCORE |
| Q12 | - |  |  | SI | Grooming |
| Q13 | - |  |  | SI | Bathing |
| Q14 | - |  |  | SI | Dressing upper body |
| Q15 | - |  |  | SI | Dressing lower body |
| Q16 | - |  |  | SI | Toileting |
| Q17 | - |  |  | SI | Score both level of assistance and frequency |
| Q18 | - |  |  | SI | Bladder - level of assistance |
| Q19 | - |  |  | SI | Bladder - frequency of accidents |
| Q20 | - |  |  | SI | Bowel - level of assistance |
| Q21 | - |  |  | SI | Bowel - frequency of accidents |
| Q22 | - |  |  | SI | Bed, chair, wheelchair transfer |
| Q23 | - |  |  | SI | Toilet transfer |
| Q24 | - |  |  | SI | Tub, shower transfer |
| Q25 | - |  |  | SI | Car transfer |
| Q26 | - |  |  | SI | Walking 'w |
| Q27 | - |  |  | SI | Wheelchair 'c |
| Q28 | - |  |  | SI | Frequent mode of locomotion |
| Q29 | - |  |  | SI | Stairs |
| Q30 | - |  |  | SI | Community mobility |
| Q31 | - |  |  | SI | Indicate usual mode |
| Q32 | - |  |  | SI | Comprehension |
| Q33 | - |  |  | SI | Expression |
| Q34 | - |  |  | SI | Reading |
| Q35 | - |  |  | SI | Writing |
| Q36 | - |  |  | SI | Speech intelligibility |
| Q37 | - |  |  | SI | Social interaction |
| Q38 | - |  |  | SI | Emotional status |
| Q39 | - |  |  | SI | Adjustment to limitations |
| Q40 | - |  |  | SI | Leisure activities |
| Q41 | - |  |  | SI | Problem solving |
| Q42 | - |  |  | SI | Memory |
| Q43 | - |  |  | SI | Orientation |
| Q44 | - |  |  | SI | Concentration |
| Q45 | - |  |  | SI | Safety awareness |
| Q46 | - |  |  | SI | Meal preparation |
| Q47 | - |  |  | SI | Laundry |
| Q48 | - |  |  | SI | Housework |
| Q49 | - |  |  | SI | Shopping |
| Q50 | - |  |  | SI | Financial management |
| Q51 | - |  |  | SI | Work / education |
| Q52 | - |  |  | SI | Date |
| Q53 | - |  |  | SI | Time |
| Q54 | - |  |  | SI | FIM FAM Total score |
| Q55 | - |  |  | SI | FIM FAM Total calculation - Bowel |
| Q56 | - |  |  | SI | Frequent mode of locomotion score |
| Q57 | - |  |  | SI | Eating |
| Q58 | - |  |  | SI | Swallowing |
| Q59 | - |  |  | SI | Grooming |
| Q60 | - |  |  | SI | Bathing |
| Q61 | - |  |  | SI | Dressing Upper Body |
| Q62 | - |  |  | SI | Dressing Lower Body |
| Q63 | - |  |  | SI | Toileting |
| Q64 | - |  |  | SI | Bladder Management - Level of Assistance |
| Q65 | - |  |  | SI | Bladder Management - Frequency of Accidents |
| Q66 | - |  |  | SI | Bowel Management - Level of Assistance |
| Q67 | - |  |  | SI | Bowel Management - Frequency of Accidents |
| Q68 | - |  |  | SI | Transfers - Bed, Chair, Wheelchair |
| Q69 | - |  |  | SI | Transfers - Toilet |
| Q70 | - |  |  | SI | Transfers - Tub or Shower |
| Q71 | - |  |  | SI | Transfers - Car |
| Q72 | - |  |  | SI | Locomotion - Walking |
| Q73 | - |  |  | SI | Locomotion - Wheelchair |
| Q74 | - |  |  | SI | Locomotion - Stairs |
| Q75 | - |  |  | SI | Community Mobility |
| Q76 | - |  |  | SI | Comprehension |
| Q77 | - |  |  | SI | Expression |
| Q78 | - |  |  | SI | Reading |
| Q79 | - |  |  | SI | Writing |
| Q80 | - |  |  | SI | Speech Intelligibility |
| Q81 | - |  |  | SI | Social Interaction |
| Q82 | - |  |  | SI | Emotional Status |
| Q83 | - |  |  | SI | Adjustments to Limitations |
| Q84 | - |  |  | SI | Use of Leisure Time |
| Q85 | - |  |  | SI | Problem Solving |
| Q86 | - |  |  | SI | Memory |
| Q87 | - |  |  | SI | Orientation |
| Q88 | - |  |  | SI | Concentration |
| Q89 | - |  |  | SI | Safety Awareness |
| Q90 | - |  |  | SI | Meal Preparation |
| Q91 | - |  |  | SI | Laundry |
| Q92 | - |  |  | SI | Housework |
| Q93 | - |  |  | SI | Shopping |
| Q94 | - |  |  | SI | Home Finances |
| Q95 | - |  |  | SI | Work / Education |
| Q96 | - |  |  | SI | The UK FIM+FAM is an instrument for the functional... |
| Q97 | - |  |  | SI | The UK FIM+FAM was originally described in 1999 [2... |
| Q98 | - |  |  | SI | 1. Hall KM, Hamilton BB, Gordon WA, Zasler ND. Cha... |
| Q99 | - |  |  | SI | J Head Trauma Rehab 1993 |
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