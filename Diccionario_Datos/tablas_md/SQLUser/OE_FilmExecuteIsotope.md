# SQLUser.OE_FilmExecuteIsotope

**Schema:** SQLUser
**Columnas:** 160
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| IS_ParRef | bigint | PK |  | NO | OE_FilmExecute Parent Reference |
| IS_Childsub | double |  |  | NO | Childsub |
| IS_IsotopeDose | double |  |  | SI | Isotope Dose |
| IS_RadioPharmaceutical_DR | bigint |  | FK | SI | Des Ref Radio Pharmaceutical |
| IS_RowId | varchar |  |  | NO | - |
| Q01 | - |  |  | SI | Upper Limb |
| Q02 | - |  |  | SI | Joint |
| Q03 | - |  |  | SI | Muscle Group |
| Q04 | - |  |  | SI | Description of Movement |
| Q05 | - |  |  | SI | Tardieu Scale |
| Q06 | - |  |  | SI | R1 (V3) |
| Q07 | - |  |  | SI | R2 (V1) |
| Q08 | - |  |  | SI | Spasticity Angle (R1-R2) |
| Q09 | - |  |  | SI | Quality of Muscle Reaction |
| Q10 | - |  |  | SI | Shoulder |
| Q100 | - |  |  | SI | R2 is at V1 |
| Q101 | - |  |  | SI | Spasticity angle =  (R1-R2) |
| Q11 | - |  |  | SI | Flexors |
| Q12 | - |  |  | SI | Shoulder - Flexors (Description of Movement) |
| Q13 | - |  |  | SI | Shoulder - Flexors R1 (V3) |
| Q14 | - |  |  | SI | Shoulder - Flexors R2 (V1) |
| Q15 | - |  |  | SI | Shoulder - Flexors (Spasticity Angle) |
| Q16 | - |  |  | SI | Shoulder - Flexors (Quality of Muscle Reaction) |
| Q16ObsDR | - |  |  | SI | Shoulder - Flexors (Quality of Muscle Reaction) DR |
| Q17 | - |  |  | SI | Internal Rotators |
| Q18 | - |  |  | SI | Shoulder - Internal Rotators (Description of Movem... |
| Q19 | - |  |  | SI | Shoulder - Internal Rotators R1 (V3) |
| Q20 | - |  |  | SI | Shoulder - Internal Rotators R2 (V1) |
| Q21 | - |  |  | SI | Shoulder - Internal Rotators (Spasticity Angle) |
| Q22 | - |  |  | SI | Shoulder - Internal Rotators (Quality of Muscle Re... |
| Q22ObsDR | - |  |  | SI | Shoulder - Internal Rotators (Quality of Muscle Re... |
| Q23 | - |  |  | SI | Elbow |
| Q24 | - |  |  | SI | Flexors |
| Q25 | - |  |  | SI | Elbow - Flexors  (Description of Movement) |
| Q26 | - |  |  | SI | Elbow - Flexors R1 (V3) |
| Q27 | - |  |  | SI | Elbow - Flexors R2 (V1) |
| Q28 | - |  |  | SI | Elbow - Flexors (Spasticity Angle) |
| Q29 | - |  |  | SI | Elbow - Flexors (Quality of Muscle Reaction) |
| Q29ObsDR | - |  |  | SI | Elbow - Flexors (Quality of Muscle Reaction) DR |
| Q30 | - |  |  | SI | Extensors |
| Q31 | - |  |  | SI | Elbow - Extensors (Description of Movement) |
| Q32 | - |  |  | SI | Elbow - Extensors R1 (V3) |
| Q33 | - |  |  | SI | Elbow - Extensors R2 (V1) |
| Q34 | - |  |  | SI | Elbow - Extensors (Spasticity Angle) |
| Q35 | - |  |  | SI | Elbow - Extensors (Quality of Muscle Reaction) |
| Q35ObsDR | - |  |  | SI | Elbow - Extensors (Quality of Muscle Reaction) DR |
| Q36 | - |  |  | SI | Forearm |
| Q37 | - |  |  | SI | Supinators |
| Q38 | - |  |  | SI | Forearm - Supinators (Description of Movement) |
| Q39 | - |  |  | SI | Forearm - Supinators R1 (V3) |
| Q40 | - |  |  | SI | Forearm - Supinators R2 (V1) |
| Q41 | - |  |  | SI | Forearm - Supinators (Spasticity Angle) |
| Q42 | - |  |  | SI | Forearm - Supinators (Quality of Muscle Reaction) |
| Q42ObsDR | - |  |  | SI | Forearm - Supinators (Quality of Muscle Reaction) ... |
| Q43 | - |  |  | SI | Pronators |
| Q44 | - |  |  | SI | Forearm - Pronators (Description of Movement) |
| Q45 | - |  |  | SI | Forearm - Pronators R1 (V3) |
| Q46 | - |  |  | SI | Forearm - Pronators R2 (V1) |
| Q47 | - |  |  | SI | Forearm - Pronators (Spasticity Angle) |
| Q48 | - |  |  | SI | Forearm - Pronators (Quality of Muscle Reaction) |
| Q48ObsDR | - |  |  | SI | Forearm - Pronators (Quality of Muscle Reaction) D... |
| Q49 | - |  |  | SI | Wrist |
| Q50 | - |  |  | SI | Flexors |
| Q51 | - |  |  | SI | Wrist - Flexors (Description of Movement) |
| Q52 | - |  |  | SI | Wrist - Flexors R1 (V3) |
| Q53 | - |  |  | SI | Wrist - Flexors R2 (V1) |
| Q54 | - |  |  | SI | Wrist - Flexors (Spasticity Angle) |
| Q55 | - |  |  | SI | Wrist - Flexors (Quality of Muscle Reaction) |
| Q55ObsDR | - |  |  | SI | Wrist - Flexors (Quality of Muscle Reaction) DR |
| Q56 | - |  |  | SI | Extensors |
| Q57 | - |  |  | SI | Wrist - Extensors (Description of Movement) |
| Q58 | - |  |  | SI | Wrist - Extensors R1 (V3) |
| Q59 | - |  |  | SI | Wrist - Extensors R2 (V1) |
| Q60 | - |  |  | SI | Wrist - Extensors (Spasticity Angle) |
| Q61 | - |  |  | SI | Wrist - Extensors (Quality of Muscle Reaction) |
| Q61ObsDR | - |  |  | SI | Wrist - Extensors (Quality of Muscle Reaction) DR |
| Q62 | - |  |  | SI | Fingers |
| Q63 | - |  |  | SI | Flexors |
| Q64 | - |  |  | SI | Fingers - Flexors (Description of Movement) |
| Q65 | - |  |  | SI | Fingers - Flexors R1 (V3) |
| Q66 | - |  |  | SI | Fingers - Flexors R2 (V1) |
| Q67 | - |  |  | SI | Fingers - Flexors (Spasticity Angle) |
| Q68 | - |  |  | SI | Fingers - Flexors (Quality of Muscle Reaction) |
| Q68ObsDR | - |  |  | SI | Fingers - Flexors (Quality of Muscle Reaction) DR |
| Q69 | - |  |  | SI | Extensors |
| Q70 | - |  |  | SI | Fingers - Extensors (Description of Movement) |
| Q71 | - |  |  | SI | Fingers - Extensors R1 (V3) |
| Q72 | - |  |  | SI | Fingers - Extensors R2 (V1) |
| Q73 | - |  |  | SI | Fingers - Extensors (Spasticity Angle) |
| Q74 | - |  |  | SI | Fingers - Extensors (Quality of Muscle Reaction) |
| Q74ObsDR | - |  |  | SI | Fingers - Extensors (Quality of Muscle Reaction) D... |
| Q75 | - |  |  | SI | Thumb |
| Q76 | - |  |  | SI | Abductors |
| Q77 | - |  |  | SI | Thumb - Abductors (Description of Movement) |
| Q78 | - |  |  | SI | Thumb - Abductors R1 (V3) |
| Q79 | - |  |  | SI | Thumb - Abductors R2 (V1) |
| Q80 | - |  |  | SI | Thumb - Abductors (Spasticity Angle) |
| Q81 | - |  |  | SI | Thumb - Abductors (Quality of Muscle Reaction) |
| Q81ObsDR | - |  |  | SI | Thumb - Abductors (Quality of Muscle Reaction) DR |
| Q82 | - |  |  | SI | Adductors |
| Q83 | - |  |  | SI | Thumb - Adductors (Description of Movement) |
| Q84 | - |  |  | SI | Thumb - Adductors R1 (V3) |
| Q85 | - |  |  | SI | Thumb - Adductors R2 (V1) |
| Q86 | - |  |  | SI | Thumb - Adductors (Spasticity Angle) |
| Q87 | - |  |  | SI | Thumb - Adductors (Quality of Muscle Reaction) |
| Q87ObsDR | - |  |  | SI | Thumb - Adductors (Quality of Muscle Reaction) DR |
| Q88 | - |  |  | SI | Comments (including other muscle groups) |
| Q89 | - |  |  | SI | Occupational Therapist Name |
| Q90 | - |  |  | SI | Signature |
| Q90UDt | - |  |  | SI | Signature Last Updated Date |
| Q90UTm | - |  |  | SI | Signature Last Updated Time |
| Q91 | - |  |  | SI | Date |
| Q92 | - |  |  | SI | Tardieu Scale |
| Q93 | - |  |  | SI | Velocity dependent – Once V is chosen it remains t... |
| Q94 | - |  |  | SI | Velocity of stretch |
| Q95 | - |  |  | SI | V1 – As slow as possible |
| Q96 | - |  |  | SI | V2 – Speed of limb falling under gravity |
| Q97 | - |  |  | SI | V3 – As fast as possible |
| Q98 | - |  |  | SI | Range (R) |
| Q99 | - |  |  | SI | R1 is at V3 or V2 |
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