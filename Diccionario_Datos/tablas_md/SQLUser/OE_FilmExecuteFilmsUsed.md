# SQLUser.OE_FilmExecuteFilmsUsed

**Schema:** SQLUser
**Columnas:** 146
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| FU_ParRef | bigint | PK |  | NO | OE_FilmExecute Parent Reference |
| FU_Childsub | double |  |  | NO | Childsub |
| FU_FilmType_DR | bigint |  | FK | SI | Des Ref FilmType |
| FU_NumberOfFilms | double |  |  | SI | Number Of Films |
| FU_OEFilmExecuteItems_DR | varchar |  | FK | SI | Des Ref OEFilmExecuteItems |
| FU_ReasonForRejection_DR | bigint |  | FK | SI | Des Ref ReasonForRejection |
| FU_RowId | varchar |  |  | NO | - |
| FU_UsageType | varchar |  |  | SI | Usage Type |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Task |
| Q03 | - |  |  | SI | Amount Scale |
| Q04 | - |  |  | SI | How Well Scale |
| Q05 | - |  |  | SI | Why affected UL not used? |
| Q06 | - |  |  | SI | Hold a Book |
| Q07 | - |  |  | SI | Hold a Book (AS) |
| Q08 | - |  |  | SI | Hold a Book (HW) |
| Q09 | - |  |  | SI | Hold a Book (Why UL not used?) |
| Q09ObsDR | - |  |  | SI | Hold a Book (Why UL not used?) DR |
| Q10 | - |  |  | SI | Use a Towel |
| Q11 | - |  |  | SI | Use a Towel (AS) |
| Q12 | - |  |  | SI | Use a Towel (HW) |
| Q13 | - |  |  | SI | Use a Towel (Why UL not used?) |
| Q13ObsDR | - |  |  | SI | Use a Towel (Why UL not used?) DR |
| Q14 | - |  |  | SI | Pick Up Glass |
| Q15 | - |  |  | SI | Pick Up Cup (AS) |
| Q16 | - |  |  | SI | Pick Up Glass (HW) |
| Q17 | - |  |  | SI | Pick Up Glass (Why UL not used?) |
| Q17ObsDR | - |  |  | SI | Pick Up Glass (Why UL not used?) DR |
| Q18 | - |  |  | SI | Brush Teeth |
| Q19 | - |  |  | SI | Brush Teeth (AS) |
| Q20 | - |  |  | SI | Brush Teeth (HW) |
| Q21 | - |  |  | SI | Brush Teeth (Why UL not used?) |
| Q21ObsDR | - |  |  | SI | Brush Teeth (Why UL not used?) DR |
| Q22 | - |  |  | SI | Shave / Make Up |
| Q23 | - |  |  | SI | Shave / Make Up (AS) |
| Q24 | - |  |  | SI | Shave / Make Up (HW) |
| Q25 | - |  |  | SI | Shave / Make Up (Why UL not used?) |
| Q25ObsDR | - |  |  | SI | Shave / Make Up (Why UL not used?) DR |
| Q26 | - |  |  | SI | Open Door with a Key |
| Q27 | - |  |  | SI | Open Door with a Key (AS) |
| Q28 | - |  |  | SI | Open Door with a Key (HW) |
| Q29 | - |  |  | SI | Open Door with a Key (Why UL not used?) |
| Q29ObsDR | - |  |  | SI | Open Door with a Key (Why UL not used?) DR |
| Q30 | - |  |  | SI | Write / Type |
| Q31 | - |  |  | SI | Write / Type (AS) |
| Q32 | - |  |  | SI | Write / Type (HW) |
| Q33 | - |  |  | SI | Write / Type (Why UL not used?) |
| Q33ObsDR | - |  |  | SI | Write / Type (Why UL not used?) DR |
| Q34 | - |  |  | SI | Steady Self |
| Q35 | - |  |  | SI | Steady Self (AS) |
| Q36 | - |  |  | SI | Steady Self (HW) |
| Q37 | - |  |  | SI | Steady Self (Why UL not used?) |
| Q37ObsDR | - |  |  | SI | Steady Self (Why UL not used?) DR |
| Q38 | - |  |  | SI | Put Arm through Clothing |
| Q39 | - |  |  | SI | Put Arm through Clothing (AS) |
| Q40 | - |  |  | SI | Put Arm through Clothing (HW) |
| Q41 | - |  |  | SI | Put Arm through Clothing (Why UL not used?) |
| Q41ObsDR | - |  |  | SI | Put Arm through Clothing (Why UL not used?) DR |
| Q42 | - |  |  | SI | Carry Object |
| Q43 | - |  |  | SI | Carry Object (AS) |
| Q44 | - |  |  | SI | Carry Object (HW) |
| Q45 | - |  |  | SI | Carry Object (Why UL not used?) |
| Q45ObsDR | - |  |  | SI | Carry Object (Why UL not used?) DR |
| Q46 | - |  |  | SI | Grasp Fork / Spoon |
| Q47 | - |  |  | SI | Grasp Fork / Spoon (AS) |
| Q48 | - |  |  | SI | Grasp Fork / Spoon (HW) |
| Q49 | - |  |  | SI | Grasp Fork / Spoon (Why UL not used?) |
| Q49ObsDR | - |  |  | SI | Grasp Fork / Spoon (Why UL not used?)  DR |
| Q50 | - |  |  | SI | Comb Hair |
| Q51 | - |  |  | SI | Comb Hair (AS) |
| Q52 | - |  |  | SI | Comb Hair (HW) |
| Q53 | - |  |  | SI | Comb Hair (Why UL not used?) |
| Q53ObsDR | - |  |  | SI | Comb Hair (Why UL not used?) DR |
| Q54 | - |  |  | SI | Pick Up Cup |
| Q55 | - |  |  | SI | Pick Up Cup (AS) |
| Q56 | - |  |  | SI | Pick Up Cup (HW) |
| Q57 | - |  |  | SI | Pick Up Cup (Why UL not used?) |
| Q57ObsDR | - |  |  | SI | Pick Up Cup (Why UL not used?) DR |
| Q58 | - |  |  | SI | Button Clothes |
| Q59 | - |  |  | SI | Button Clothes (AS) |
| Q60 | - |  |  | SI | Button Clothes (HW) |
| Q61 | - |  |  | SI | Button Clothes (Why UL not used?) |
| Q61ObsDR | - |  |  | SI | Button Clothes (Why UL not used?)  DR |
| Q62 | - |  |  | SI | Sum Score |
| Q63 | - |  |  | SI | Sum Score (AS) |
| Q64 | - |  |  | SI | Sum Score (HW) |
| Q65 | - |  |  | SI | Total ((Sum Score / Total Answerd) |
| Q66 | - |  |  | SI | Total AS (Sum Score AS/Total Answerd) |
| Q67 | - |  |  | SI | Total HW (Sum Score HW/Total Answerd) |
| Q68 | - |  |  | SI | Occupational Therapist Name |
| Q69 | - |  |  | SI | Date |
| Q70 | - |  |  | SI | Signature |
| Q70UDt | - |  |  | SI | Signature Last Updated Date |
| Q70UTm | - |  |  | SI | Signature Last Updated Time |
| Q71 | - |  |  | SI | Score (AS) |
| Q72 | - |  |  | SI | Score (HW) |
| Q73 | - |  |  | SI | Total (Sum Score / Total Answered) |
| Q74 | - |  |  | SI | Text |
| Q75 | - |  |  | SI | The highest the score, the closest is to normal pa... |
| Q76 | - |  |  | SI | Total Answered (AS) |
| Q77 | - |  |  | SI | Total Answered (HW) |
| Q78 | - |  |  | SI | Total Answered |
| Q79 | - |  |  | SI | Total |
| Q80 | - |  |  | SI | (Sum Score / Total Answered) |
| Q81 | - |  |  | SI | (AS=Amount Scale, HW=How Well Scale, Why affected ... |
| Q82 | - |  |  | SI | HW How Well Scale |
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