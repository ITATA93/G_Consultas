# questionnaire.QTCAHOCCAML

> Motor Activity Log Assessment

**Schema:** questionnaire
**Columnas:** 139
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Motor Activity Log Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | varchar |  |  | SI | Task |
| Q03 | varchar |  |  | SI | Amount Scale |
| Q04 | varchar |  |  | SI | How Well Scale |
| Q05 | varchar |  |  | SI | Why affected UL not used? |
| Q06 | varchar |  |  | SI | Hold a Book |
| Q07 | varchar |  |  | SI | Hold a Book (AS) |
| Q08 | varchar |  |  | SI | Hold a Book (HW) |
| Q09 | varchar |  |  | SI | Hold a Book (Why UL not used?) |
| Q09ObsDR | varchar |  | FK | SI | Hold a Book (Why UL not used?) DR |
| Q10 | varchar |  |  | SI | Use a Towel |
| Q11 | varchar |  |  | SI | Use a Towel (AS) |
| Q12 | varchar |  |  | SI | Use a Towel (HW) |
| Q13 | varchar |  |  | SI | Use a Towel (Why UL not used?) |
| Q13ObsDR | varchar |  | FK | SI | Use a Towel (Why UL not used?) DR |
| Q14 | varchar |  |  | SI | Pick Up Glass |
| Q15 | varchar |  |  | SI | Pick Up Cup (AS) |
| Q16 | varchar |  |  | SI | Pick Up Glass (HW) |
| Q17 | varchar |  |  | SI | Pick Up Glass (Why UL not used?) |
| Q17ObsDR | varchar |  | FK | SI | Pick Up Glass (Why UL not used?) DR |
| Q18 | varchar |  |  | SI | Brush Teeth |
| Q19 | varchar |  |  | SI | Brush Teeth (AS) |
| Q20 | varchar |  |  | SI | Brush Teeth (HW) |
| Q21 | varchar |  |  | SI | Brush Teeth (Why UL not used?) |
| Q21ObsDR | varchar |  | FK | SI | Brush Teeth (Why UL not used?) DR |
| Q22 | varchar |  |  | SI | Shave / Make Up |
| Q23 | varchar |  |  | SI | Shave / Make Up (AS) |
| Q24 | varchar |  |  | SI | Shave / Make Up (HW) |
| Q25 | varchar |  |  | SI | Shave / Make Up (Why UL not used?) |
| Q25ObsDR | varchar |  | FK | SI | Shave / Make Up (Why UL not used?) DR |
| Q26 | varchar |  |  | SI | Open Door with a Key |
| Q27 | varchar |  |  | SI | Open Door with a Key (AS) |
| Q28 | varchar |  |  | SI | Open Door with a Key (HW) |
| Q29 | varchar |  |  | SI | Open Door with a Key (Why UL not used?) |
| Q29ObsDR | varchar |  | FK | SI | Open Door with a Key (Why UL not used?) DR |
| Q30 | varchar |  |  | SI | Write / Type |
| Q31 | varchar |  |  | SI | Write / Type (AS) |
| Q32 | varchar |  |  | SI | Write / Type (HW) |
| Q33 | varchar |  |  | SI | Write / Type (Why UL not used?) |
| Q33ObsDR | varchar |  | FK | SI | Write / Type (Why UL not used?) DR |
| Q34 | varchar |  |  | SI | Steady Self  |
| Q35 | varchar |  |  | SI | Steady Self (AS) |
| Q36 | varchar |  |  | SI | Steady Self (HW) |
| Q37 | varchar |  |  | SI | Steady Self (Why UL not used?) |
| Q37ObsDR | varchar |  | FK | SI | Steady Self (Why UL not used?) DR |
| Q38 | varchar |  |  | SI | Put Arm through Clothing  |
| Q39 | varchar |  |  | SI | Put Arm through Clothing (AS) |
| Q40 | varchar |  |  | SI | Put Arm through Clothing (HW) |
| Q41 | varchar |  |  | SI | Put Arm through Clothing (Why UL not used?) |
| Q41ObsDR | varchar |  | FK | SI | Put Arm through Clothing (Why UL not used?) DR |
| Q42 | varchar |  |  | SI | Carry Object  |
| Q43 | varchar |  |  | SI | Carry Object (AS) |
| Q44 | varchar |  |  | SI | Carry Object (HW) |
| Q45 | varchar |  |  | SI | Carry Object (Why UL not used?) |
| Q45ObsDR | varchar |  | FK | SI | Carry Object (Why UL not used?) DR |
| Q46 | varchar |  |  | SI | Grasp Fork / Spoon |
| Q47 | varchar |  |  | SI | Grasp Fork / Spoon (AS) |
| Q48 | varchar |  |  | SI | Grasp Fork / Spoon (HW) |
| Q49 | varchar |  |  | SI | Grasp Fork / Spoon (Why UL not used?)  |
| Q49ObsDR | varchar |  | FK | SI | Grasp Fork / Spoon (Why UL not used?)  DR |
| Q50 | varchar |  |  | SI | Comb Hair |
| Q51 | varchar |  |  | SI | Comb Hair (AS) |
| Q52 | varchar |  |  | SI | Comb Hair (HW) |
| Q53 | varchar |  |  | SI | Comb Hair (Why UL not used?) |
| Q53ObsDR | varchar |  | FK | SI | Comb Hair (Why UL not used?) DR |
| Q54 | varchar |  |  | SI | Pick Up Cup |
| Q55 | varchar |  |  | SI | Pick Up Cup (AS) |
| Q56 | varchar |  |  | SI | Pick Up Cup (HW) |
| Q57 | varchar |  |  | SI | Pick Up Cup (Why UL not used?) |
| Q57ObsDR | varchar |  | FK | SI | Pick Up Cup (Why UL not used?) DR |
| Q58 | varchar |  |  | SI | Button Clothes |
| Q59 | varchar |  |  | SI | Button Clothes (AS) |
| Q60 | varchar |  |  | SI | Button Clothes (HW) |
| Q61 | varchar |  |  | SI | Button Clothes (Why UL not used?)  |
| Q61ObsDR | varchar |  | FK | SI | Button Clothes (Why UL not used?)  DR |
| Q62 | varchar |  |  | SI | Sum Score |
| Q63 | varchar |  |  | SI | Sum Score (AS) |
| Q64 | varchar |  |  | SI | Sum Score (HW) |
| Q65 | varchar |  |  | SI | Total ((Sum Score / Total Answerd) |
| Q66 | numeric |  |  | SI | Total AS (Sum Score AS/Total Answerd) |
| Q67 | numeric |  |  | SI | Total HW (Sum Score HW/Total Answerd) |
| Q68 | varchar |  |  | SI | Occupational Therapist Name |
| Q69 | date |  |  | SI | Date |
| Q70 | longvarbinary |  |  | SI | Signature |
| Q70UDt | date |  |  | SI | Signature Last Updated Date |
| Q70UTm | time |  |  | SI | Signature Last Updated Time |
| Q71 | numeric |  |  | SI | Score (AS) |
| Q72 | numeric |  |  | SI | Score (HW) |
| Q73 | varchar |  |  | SI | Total (Sum Score / Total Answered) |
| Q74 | varchar |  |  | SI | Text |
| Q75 | varchar |  |  | SI | The highest the score, the closest is to normal pa... |
| Q76 | numeric |  |  | SI | Total Answered (AS) |
| Q77 | numeric |  |  | SI | Total Answered (HW) |
| Q78 | varchar |  |  | SI | Total Answered |
| Q79 | varchar |  |  | SI | Total |
| Q80 | varchar |  |  | SI | (Sum Score / Total Answered) |
| Q81 | varchar |  |  | SI | (AS=Amount Scale, HW=How Well Scale, Why affected ... |
| Q82 | varchar |  |  | SI | HW How Well Scale |
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