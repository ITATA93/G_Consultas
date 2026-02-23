# SQLUser.OR_An_Oper_Diagnosis

**Schema:** SQLUser
**Columnas:** 139
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Pabellón Quirúrgico**. Gestión de cirugías.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DIA_ParREf | varchar | PK |  | NO | OR_Anaest_Operation Parent Reference |
| DIA_Childsub | double |  |  | NO | Childsub |
| DIA_ICD_DR | bigint |  | FK | SI | Des Ref ICD |
| DIA_RowId | varchar |  |  | NO | - |
| Q01 | - |  |  | SI | Date of incident |
| Q02 | - |  |  | SI | Time of incident |
| Q03 | - |  |  | SI | Comments |
| Q04 | - |  |  | SI | Name of drug extravasation |
| Q05 | - |  |  | SI | Approximate volume extravasated (mLs) |
| Q06 | - |  |  | SI | Approximate volume administered prior to extravasa... |
| Q07 | - |  |  | SI | When was extravasation recognised? |
| Q08 | - |  |  | SI | No. of hours |
| Q09 | - |  |  | SI | No. of days |
| Q10 | - |  |  | SI | Type of access |
| Q11 | - |  |  | SI | Type of central venous access device |
| Q12 | - |  |  | SI | Date IV cannula inserted |
| Q13 | - |  |  | SI | Time IV cannula inserted |
| Q14 | - |  |  | SI | Difficult cannulation |
| Q15 | - |  |  | SI | Number of attempts |
| Q16 | - |  |  | SI | Type of administration |
| Q17 | - |  |  | SI | If other, please specify |
| Q18 | - |  |  | SI | Signs and symptoms |
| Q19 | - |  |  | SI | Colour of skin |
| Q20 | - |  |  | SI | Measurement of area (mm) |
| Q21 | - |  |  | SI | Mark area that is affected |
| Q22 | - |  |  | SI | Date of intervention |
| Q23 | - |  |  | SI | Time of intervention |
| Q24 | - |  |  | SI | Antidote administered? |
| Q25 | - |  |  | SI | If yes, please specify |
| Q26 | - |  |  | SI | Interventions performed |
| Q27 | - |  |  | SI | Extravasation grading |
| Q28 | - |  |  | SI | Referrals or appointments made? |
| Q29 | - |  |  | SI | Referral details |
| Q30 | - |  |  | SI | Discharge checklist |
| Q31 | - |  |  | SI | If extravasation is suspected the initial SLAP ste... |
| Q32 | - |  |  | SI | Stop the injection / infusion immediately |
| Q33 | - |  |  | SI | Leave the venous access device (VAD) in place |
| Q34 | - |  |  | SI | Aspirate any residual drug from the VAD with a ste... |
| Q35 | - |  |  | SI | Plan |
| Q36 | - |  |  | SI | S |
| Q37 | - |  |  | SI | L |
| Q38 | - |  |  | SI | A |
| Q39 | - |  |  | SI | P |
| Q40 | - |  |  | SI | Grading scale |
| Q41 | - |  |  | SI | Skin Color |
| Q42 | - |  |  | SI | Skin Temperature |
| Q43 | - |  |  | SI | Skin Intergrity |
| Q44 | - |  |  | SI | Absent |
| Q45 | - |  |  | SI | Normal |
| Q46 | - |  |  | SI | Normal |
| Q47 | - |  |  | SI | Unbroken |
| Q48 | - |  |  | SI | Oedema |
| Q49 | - |  |  | SI | Pink |
| Q50 | - |  |  | SI | Warm |
| Q51 | - |  |  | SI | Blistered |
| Q52 | - |  |  | SI | Non-pitting |
| Q53 | - |  |  | SI | Red |
| Q54 | - |  |  | SI | Hot |
| Q55 | - |  |  | SI | Superficial skin loss |
| Q56 | - |  |  | SI | Pitting |
| Q57 | - |  |  | SI | Blanched centre |
| Q58 | - |  |  | SI | Tissue loss exposing subcutaneous tissue |
| Q59 | - |  |  | SI | Blackend |
| Q60 | - |  |  | SI | Tissue loss exposing subcutaneous tissue |
| Q61 | - |  |  | SI | Mobility |
| Q62 | - |  |  | SI | Pain |
| Q63 | - |  |  | SI | Fever |
| Q64 | - |  |  | SI | Grading Scale |
| Q65 | - |  |  | SI | 0 |
| Q66 | - |  |  | SI | 1 |
| Q67 | - |  |  | SI | 2 |
| Q68 | - |  |  | SI | 3 |
| Q69 | - |  |  | SI | 4 |
| Q70 | - |  |  | SI | Stop the injection / infusion immediately |
| Q71 | - |  |  | SI | Leave the venous access device (VAD) in place |
| Q72 | - |  |  | SI | Aspirate any residual drug from the VAD with a ste... |
| Q73 | - |  |  | SI | Plan |
| Q74 | - |  |  | SI | Grading Scale |
| Q75 | - |  |  | SI | Grading Scale |
| Q76 | - |  |  | SI | Grading Scale |
| Q77 | - |  |  | SI | Grading Scale |
| Q78 | - |  |  | SI | Skin Color |
| Q79 | - |  |  | SI | Skin Color |
| Q80 | - |  |  | SI | Skin Color |
| Q81 | - |  |  | SI | Skin Color |
| Q82 | - |  |  | SI | Skin Temperature |
| Q83 | - |  |  | SI | Skin Temperature |
| Q84 | - |  |  | SI | Skin Temperature |
| Q85 | - |  |  | SI | Skin Temperature |
| Q86 | - |  |  | SI | Skin Intergrity |
| Q87 | - |  |  | SI | Skin Intergrity |
| Q88 | - |  |  | SI | Skin Intergrity |
| Q89 | - |  |  | SI | Skin Intergrity |
| Q90 | - |  |  | SI | Absent |
| Q91 | - |  |  | SI | Absent |
| Q92 | - |  |  | SI | Absent |
| Q93 | - |  |  | SI | Absent |
| Q95 | - |  |  | SI | Date |
| Q96 | - |  |  | SI | Time |
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