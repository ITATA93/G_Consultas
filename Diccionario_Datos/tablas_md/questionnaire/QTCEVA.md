# questionnaire.QTCEVA

> Extravasation Assessment

**Schema:** questionnaire
**Columnas:** 136
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Extravasation Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date of incident |
| Q02 | time |  |  | SI | Time of incident |
| Q03 | varchar |  |  | SI | Comments |
| Q04 | varchar |  |  | SI | Name of drug extravasation |
| Q05 | numeric |  |  | SI | Approximate volume extravasated (mLs) |
| Q06 | numeric |  |  | SI | Approximate volume administered prior to extravasa... |
| Q07 | varchar |  |  | SI | When was extravasation recognised? |
| Q08 | numeric |  |  | SI | No. of hours |
| Q09 | numeric |  |  | SI | No. of days |
| Q10 | varchar |  |  | SI | Type of access |
| Q11 | varchar |  |  | SI | Type of central venous access device |
| Q12 | date |  |  | SI | Date IV cannula inserted |
| Q13 | time |  |  | SI | Time IV cannula inserted |
| Q14 | varchar |  |  | SI | Difficult cannulation |
| Q15 | varchar |  |  | SI | Number of attempts |
| Q16 | varchar |  |  | SI | Type of administration |
| Q17 | varchar |  |  | SI | If other, please specify |
| Q18 | varchar |  |  | SI | Signs and symptoms |
| Q19 | varchar |  |  | SI | Colour of skin |
| Q20 | numeric |  |  | SI | Measurement of area (mm) |
| Q21 | varchar |  |  | SI | Mark area that is affected |
| Q22 | date |  |  | SI | Date of intervention |
| Q23 | time |  |  | SI | Time of intervention |
| Q24 | varchar |  |  | SI | Antidote administered? |
| Q25 | varchar |  |  | SI | If yes, please specify |
| Q26 | varchar |  |  | SI | Interventions performed |
| Q27 | varchar |  |  | SI | Extravasation grading |
| Q28 | varchar |  |  | SI | Referrals or appointments made? |
| Q29 | varchar |  |  | SI | Referral details |
| Q30 | varchar |  |  | SI | Discharge checklist |
| Q31 | varchar |  |  | SI | If extravasation is suspected the initial SLAP ste... |
| Q32 | varchar |  |  | SI | Stop the injection / infusion immediately |
| Q33 | varchar |  |  | SI | Leave the venous access device (VAD) in place |
| Q34 | varchar |  |  | SI | Aspirate any residual drug from the VAD with a ste... |
| Q35 | varchar |  |  | SI | Plan |
| Q36 | varchar |  |  | SI | S |
| Q37 | varchar |  |  | SI | L |
| Q38 | varchar |  |  | SI | A |
| Q39 | varchar |  |  | SI | P |
| Q40 | varchar |  |  | SI | Grading scale |
| Q41 | varchar |  |  | SI | Skin Color |
| Q42 | varchar |  |  | SI | Skin Temperature |
| Q43 | varchar |  |  | SI | Skin Intergrity |
| Q44 | varchar |  |  | SI | Absent |
| Q45 | varchar |  |  | SI | Normal |
| Q46 | varchar |  |  | SI | Normal |
| Q47 | varchar |  |  | SI | Unbroken |
| Q48 | varchar |  |  | SI | Oedema |
| Q49 | varchar |  |  | SI | Pink |
| Q50 | varchar |  |  | SI | Warm |
| Q51 | varchar |  |  | SI | Blistered |
| Q52 | varchar |  |  | SI | Non-pitting |
| Q53 | varchar |  |  | SI | Red |
| Q54 | varchar |  |  | SI | Hot |
| Q55 | varchar |  |  | SI | Superficial skin loss |
| Q56 | varchar |  |  | SI | Pitting |
| Q57 | varchar |  |  | SI | Blanched centre |
| Q58 | varchar |  |  | SI | Tissue loss exposing subcutaneous tissue |
| Q59 | varchar |  |  | SI | Blackend |
| Q60 | varchar |  |  | SI | Tissue loss exposing subcutaneous tissue |
| Q61 | varchar |  |  | SI | Mobility |
| Q62 | varchar |  |  | SI | Pain |
| Q63 | varchar |  |  | SI | Fever |
| Q64 | varchar |  |  | SI | Grading Scale |
| Q65 | varchar |  |  | SI | 0 |
| Q66 | varchar |  |  | SI | 1 |
| Q67 | varchar |  |  | SI | 2 |
| Q68 | varchar |  |  | SI | 3 |
| Q69 | varchar |  |  | SI | 4 |
| Q70 | varchar |  |  | SI | Stop the injection / infusion immediately |
| Q71 | varchar |  |  | SI | Leave the venous access device (VAD) in place |
| Q72 | varchar |  |  | SI | Aspirate any residual drug from the VAD with a ste... |
| Q73 | varchar |  |  | SI | Plan |
| Q74 | varchar |  |  | SI | Grading Scale |
| Q75 | varchar |  |  | SI | Grading Scale |
| Q76 | varchar |  |  | SI | Grading Scale |
| Q77 | varchar |  |  | SI | Grading Scale |
| Q78 | varchar |  |  | SI | Skin Color |
| Q79 | varchar |  |  | SI | Skin Color |
| Q80 | varchar |  |  | SI | Skin Color |
| Q81 | varchar |  |  | SI | Skin Color |
| Q82 | varchar |  |  | SI | Skin Temperature |
| Q83 | varchar |  |  | SI | Skin Temperature |
| Q84 | varchar |  |  | SI | Skin Temperature |
| Q85 | varchar |  |  | SI | Skin Temperature |
| Q86 | varchar |  |  | SI | Skin Intergrity |
| Q87 | varchar |  |  | SI | Skin Intergrity |
| Q88 | varchar |  |  | SI | Skin Intergrity |
| Q89 | varchar |  |  | SI | Skin Intergrity |
| Q90 | varchar |  |  | SI | Absent |
| Q91 | varchar |  |  | SI | Absent |
| Q92 | varchar |  |  | SI | Absent |
| Q93 | varchar |  |  | SI | Absent |
| Q95 | date |  |  | SI | Date |
| Q96 | time |  |  | SI | Time |
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