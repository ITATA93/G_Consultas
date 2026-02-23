# questionnaire.QTCAHOCCASP

> Spasticity Occupational Therapy Assessment

**Schema:** questionnaire
**Columnas:** 156
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Spasticity Occupational Therapy Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Upper Limb |
| Q02 | varchar |  |  | SI | Joint |
| Q03 | varchar |  |  | SI | Muscle Group |
| Q04 | varchar |  |  | SI | Description of Movement |
| Q05 | varchar |  |  | SI | Tardieu Scale |
| Q06 | varchar |  |  | SI | R1 (V3) |
| Q07 | varchar |  |  | SI | R2 (V1) |
| Q08 | varchar |  |  | SI | Spasticity Angle (R1-R2) |
| Q09 | varchar |  |  | SI | Quality of Muscle Reaction |
| Q10 | varchar |  |  | SI | Shoulder |
| Q100 | varchar |  |  | SI | R2 is at V1 |
| Q101 | varchar |  |  | SI | Spasticity angle =  (R1-R2) |
| Q11 | varchar |  |  | SI | Flexors |
| Q12 | varchar |  |  | SI | Shoulder - Flexors (Description of Movement) |
| Q13 | varchar |  |  | SI | Shoulder - Flexors R1 (V3) |
| Q14 | varchar |  |  | SI | Shoulder - Flexors R2 (V1) |
| Q15 | varchar |  |  | SI | Shoulder - Flexors (Spasticity Angle) |
| Q16 | varchar |  |  | SI | Shoulder - Flexors (Quality of Muscle Reaction) |
| Q16ObsDR | varchar |  | FK | SI | Shoulder - Flexors (Quality of Muscle Reaction) DR |
| Q17 | varchar |  |  | SI | Internal Rotators |
| Q18 | varchar |  |  | SI | Shoulder - Internal Rotators (Description of Movem... |
| Q19 | varchar |  |  | SI | Shoulder - Internal Rotators R1 (V3) |
| Q20 | varchar |  |  | SI | Shoulder - Internal Rotators R2 (V1) |
| Q21 | varchar |  |  | SI | Shoulder - Internal Rotators (Spasticity Angle) |
| Q22 | varchar |  |  | SI | Shoulder - Internal Rotators (Quality of Muscle Re... |
| Q22ObsDR | varchar |  | FK | SI | Shoulder - Internal Rotators (Quality of Muscle Re... |
| Q23 | varchar |  |  | SI | Elbow |
| Q24 | varchar |  |  | SI | Flexors |
| Q25 | varchar |  |  | SI | Elbow - Flexors  (Description of Movement) |
| Q26 | varchar |  |  | SI | Elbow - Flexors R1 (V3) |
| Q27 | varchar |  |  | SI | Elbow - Flexors R2 (V1) |
| Q28 | varchar |  |  | SI | Elbow - Flexors (Spasticity Angle) |
| Q29 | varchar |  |  | SI | Elbow - Flexors (Quality of Muscle Reaction) |
| Q29ObsDR | varchar |  | FK | SI | Elbow - Flexors (Quality of Muscle Reaction) DR |
| Q30 | varchar |  |  | SI | Extensors |
| Q31 | varchar |  |  | SI | Elbow - Extensors (Description of Movement) |
| Q32 | varchar |  |  | SI | Elbow - Extensors R1 (V3) |
| Q33 | varchar |  |  | SI | Elbow - Extensors R2 (V1) |
| Q34 | varchar |  |  | SI | Elbow - Extensors (Spasticity Angle) |
| Q35 | varchar |  |  | SI | Elbow - Extensors (Quality of Muscle Reaction) |
| Q35ObsDR | varchar |  | FK | SI | Elbow - Extensors (Quality of Muscle Reaction) DR |
| Q36 | varchar |  |  | SI | Forearm |
| Q37 | varchar |  |  | SI | Supinators |
| Q38 | varchar |  |  | SI | Forearm - Supinators (Description of Movement) |
| Q39 | varchar |  |  | SI | Forearm - Supinators R1 (V3) |
| Q40 | varchar |  |  | SI | Forearm - Supinators R2 (V1) |
| Q41 | varchar |  |  | SI | Forearm - Supinators (Spasticity Angle) |
| Q42 | varchar |  |  | SI | Forearm - Supinators (Quality of Muscle Reaction) |
| Q42ObsDR | varchar |  | FK | SI | Forearm - Supinators (Quality of Muscle Reaction) ... |
| Q43 | varchar |  |  | SI | Pronators |
| Q44 | varchar |  |  | SI | Forearm - Pronators (Description of Movement) |
| Q45 | varchar |  |  | SI | Forearm - Pronators R1 (V3) |
| Q46 | varchar |  |  | SI | Forearm - Pronators R2 (V1) |
| Q47 | varchar |  |  | SI | Forearm - Pronators (Spasticity Angle) |
| Q48 | varchar |  |  | SI | Forearm - Pronators (Quality of Muscle Reaction) |
| Q48ObsDR | varchar |  | FK | SI | Forearm - Pronators (Quality of Muscle Reaction) D... |
| Q49 | varchar |  |  | SI | Wrist |
| Q50 | varchar |  |  | SI | Flexors |
| Q51 | varchar |  |  | SI | Wrist - Flexors (Description of Movement) |
| Q52 | varchar |  |  | SI | Wrist - Flexors R1 (V3) |
| Q53 | varchar |  |  | SI | Wrist - Flexors R2 (V1) |
| Q54 | varchar |  |  | SI | Wrist - Flexors (Spasticity Angle) |
| Q55 | varchar |  |  | SI | Wrist - Flexors (Quality of Muscle Reaction) |
| Q55ObsDR | varchar |  | FK | SI | Wrist - Flexors (Quality of Muscle Reaction) DR |
| Q56 | varchar |  |  | SI | Extensors |
| Q57 | varchar |  |  | SI | Wrist - Extensors (Description of Movement) |
| Q58 | varchar |  |  | SI | Wrist - Extensors R1 (V3) |
| Q59 | varchar |  |  | SI | Wrist - Extensors R2 (V1) |
| Q60 | varchar |  |  | SI | Wrist - Extensors (Spasticity Angle) |
| Q61 | varchar |  |  | SI | Wrist - Extensors (Quality of Muscle Reaction) |
| Q61ObsDR | varchar |  | FK | SI | Wrist - Extensors (Quality of Muscle Reaction) DR |
| Q62 | varchar |  |  | SI | Fingers |
| Q63 | varchar |  |  | SI | Flexors |
| Q64 | varchar |  |  | SI | Fingers - Flexors (Description of Movement) |
| Q65 | varchar |  |  | SI | Fingers - Flexors R1 (V3) |
| Q66 | varchar |  |  | SI | Fingers - Flexors R2 (V1) |
| Q67 | varchar |  |  | SI | Fingers - Flexors (Spasticity Angle) |
| Q68 | varchar |  |  | SI | Fingers - Flexors (Quality of Muscle Reaction) |
| Q68ObsDR | varchar |  | FK | SI | Fingers - Flexors (Quality of Muscle Reaction) DR |
| Q69 | varchar |  |  | SI | Extensors |
| Q70 | varchar |  |  | SI | Fingers - Extensors (Description of Movement) |
| Q71 | varchar |  |  | SI | Fingers - Extensors R1 (V3) |
| Q72 | varchar |  |  | SI | Fingers - Extensors R2 (V1) |
| Q73 | varchar |  |  | SI | Fingers - Extensors (Spasticity Angle) |
| Q74 | varchar |  |  | SI | Fingers - Extensors (Quality of Muscle Reaction) |
| Q74ObsDR | varchar |  | FK | SI | Fingers - Extensors (Quality of Muscle Reaction) D... |
| Q75 | varchar |  |  | SI | Thumb |
| Q76 | varchar |  |  | SI | Abductors |
| Q77 | varchar |  |  | SI | Thumb - Abductors (Description of Movement) |
| Q78 | varchar |  |  | SI | Thumb - Abductors R1 (V3) |
| Q79 | varchar |  |  | SI | Thumb - Abductors R2 (V1) |
| Q80 | varchar |  |  | SI | Thumb - Abductors (Spasticity Angle) |
| Q81 | varchar |  |  | SI | Thumb - Abductors (Quality of Muscle Reaction) |
| Q81ObsDR | varchar |  | FK | SI | Thumb - Abductors (Quality of Muscle Reaction) DR |
| Q82 | varchar |  |  | SI | Adductors |
| Q83 | varchar |  |  | SI | Thumb - Adductors (Description of Movement) |
| Q84 | varchar |  |  | SI | Thumb - Adductors R1 (V3) |
| Q85 | varchar |  |  | SI | Thumb - Adductors R2 (V1) |
| Q86 | varchar |  |  | SI | Thumb - Adductors (Spasticity Angle) |
| Q87 | varchar |  |  | SI | Thumb - Adductors (Quality of Muscle Reaction) |
| Q87ObsDR | varchar |  | FK | SI | Thumb - Adductors (Quality of Muscle Reaction) DR |
| Q88 | varchar |  |  | SI | Comments (including other muscle groups) |
| Q89 | varchar |  |  | SI | Occupational Therapist Name |
| Q90 | longvarbinary |  |  | SI | Signature |
| Q90UDt | date |  |  | SI | Signature Last Updated Date |
| Q90UTm | time |  |  | SI | Signature Last Updated Time |
| Q91 | date |  |  | SI | Date |
| Q92 | varchar |  |  | SI | Tardieu Scale |
| Q93 | varchar |  |  | SI | Velocity dependent – Once V is chosen it remains t... |
| Q94 | varchar |  |  | SI | Velocity of stretch |
| Q95 | varchar |  |  | SI | V1 – As slow as possible |
| Q96 | varchar |  |  | SI | V2 – Speed of limb falling under gravity |
| Q97 | varchar |  |  | SI | V3 – As fast as possible |
| Q98 | varchar |  |  | SI | Range (R) |
| Q99 | varchar |  |  | SI | R1 is at V3 or V2 |
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