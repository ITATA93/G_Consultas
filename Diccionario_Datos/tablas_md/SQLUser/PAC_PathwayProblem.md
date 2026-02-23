# SQLUser.PAC_PathwayProblem

**Schema:** SQLUser
**Columnas:** 144
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PACPP_ParRef | bigint | PK |  | NO | Parent Reference |
| PACPP_Childsub | double |  |  | NO | Childsub |
| PACPP_CodeTableTags | varchar |  |  | SI | List of Code Table Tags |
| PACPP_CreatedDate | date |  |  | SI | Created Date |
| PACPP_CreatedTime | time |  |  | SI | Created Time |
| PACPP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PACPP_Desc | varchar |  |  | SI | Description |
| PACPP_ICDCode_DR | bigint |  | FK | SI | Des Ref to MRCID |
| PACPP_ICPC2Codes_DR | bigint |  | FK | SI | Des Ref MRCICPC2Codes |
| PACPP_ManualDescription | bit |  |  | SI | Manual Description |
| PACPP_RowId | varchar |  |  | NO | - |
| PACPP_SnomedConcept_DR | bigint |  | FK | SI | Des Ref PACSnomedConcept |
| PACPP_SnomedTerms_DR | bigint |  | FK | SI | Des Ref PACSnomedTerms |
| PACPP_Stage_DR | bigint |  | FK | SI | [DEPRECATED]TC-99176 Replaces this with PACPPStage... |
| PACPP_Stages | varchar |  |  | SI | List of MRCCancerStageIdentifier |
| PACPP_UpdatedDate | date |  |  | SI | Updated Date |
| PACPP_UpdatedTime | time |  |  | SI | Updated Time |
| PACPP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Identify |
| Q02 | - |  |  | SI | To be completed for ward transfers and transfers b... |
| Q03 | - |  |  | SI | Transfer of care discussed with patient |
| Q04 | - |  |  | SI | Family / Carer / Other (please specify) |
| Q05 | - |  |  | SI | Consultant notified |
| Q06 | - |  |  | SI | If no, reason |
| Q07 | - |  |  | SI | Discharge summary completed |
| Q08 | - |  |  | SI | Interpreter required |
| Q09 | - |  |  | SI | Primary language spoken |
| Q10 | - |  |  | SI | Situation |
| Q11 | - |  |  | SI | Principal diagnosis |
| Q12 | - |  |  | SI | Nursing problem |
| Q12A | - |  |  | SI | Nursing problem |
| Q13 | - |  |  | SI | Reason for transfer |
| Q14 | - |  |  | SI | Legal status |
| Q15 | - |  |  | SI | Allergies (please check the patient record) |
| Q16 | - |  |  | SI | Patient ID band checked and updated |
| Q17 | - |  |  | SI | Mode of transportation |
| Q18 | - |  |  | SI | Other mode of transportation |
| Q19 | - |  |  | SI | By whom |
| Q20 | - |  |  | SI | Background |
| Q21 | - |  |  | SI | Clinical risk and alerts updated and communicated ... |
| Q22 | - |  |  | SI | Alerts comments |
| Q23 | - |  |  | SI | Mental / Cognitive / Behaviour |
| Q24 | - |  |  | SI | Other |
| Q25 | - |  |  | SI | Current cognitive state |
| Q26 | - |  |  | SI | Patient living arrangements |
| Q27 | - |  |  | SI | ACAS completed |
| Q28 | - |  |  | SI | Anticipated living arrangement |
| Q29 | - |  |  | SI | Allied health interventions completed |
| Q30 | - |  |  | SI | Other AHP |
| Q31 | - |  |  | SI | Nutrition |
| Q32 | - |  |  | SI | Nutrition comments |
| Q33 | - |  |  | SI | Elimination |
| Q34 | - |  |  | SI | Bowel patterns |
| Q35 | - |  |  | SI | Last bowel motion date and time |
| Q36 | - |  |  | SI | Urinary patterns |
| Q37 | - |  |  | SI | Last voided date |
| Q38 | - |  |  | SI | Indwelling catheter |
| Q39 | - |  |  | SI | Size |
| Q40 | - |  |  | SI | Date inserted |
| Q41 | - |  |  | SI | Mobility |
| Q42 | - |  |  | SI | ADL / Hygiene |
| Q43 | - |  |  | SI | Assessment |
| Q44 | - |  |  | SI | Intravascular access |
| Q45 | - |  |  | SI | Other IV access |
| Q46 | - |  |  | SI | Site 1 |
| Q47 | - |  |  | SI | Site 2 |
| Q48 | - |  |  | SI | Site 3 |
| Q49 | - |  |  | SI | Date inserted 1 |
| Q50 | - |  |  | SI | Date inserted 2 |
| Q51 | - |  |  | SI | Date inserted 3 |
| Q52 | - |  |  | SI | Skin |
| Q53 | - |  |  | SI | Wound surgical site |
| Q54 | - |  |  | SI | Closure technique |
| Q55 | - |  |  | SI | Drain inserted on |
| Q56 | - |  |  | SI | Drain changed on |
| Q57 | - |  |  | SI | Wound status |
| Q58 | - |  |  | SI | Sleep patterns |
| Q59 | - |  |  | SI | Neurological status |
| Q60 | - |  |  | SI | Valuables |
| Q61 | - |  |  | SI | Clothing |
| Q62 | - |  |  | SI | Glasses |
| Q63 | - |  |  | SI | Dentures |
| Q64 | - |  |  | SI | Hearing aid |
| Q65 | - |  |  | SI | Jewelleries |
| Q66 | - |  |  | SI | Contact lens |
| Q67 | - |  |  | SI | Bridge |
| Q68 | - |  |  | SI | Prosthesis |
| Q69 | - |  |  | SI | Valuables comments |
| Q70 | - |  |  | SI | Toiletries |
| Q71 | - |  |  | SI | Request / Recommendations |
| Q72 | - |  |  | SI | Discharge plan |
| Q73 | - |  |  | SI | Estimated discharge date |
| Q74 | - |  |  | SI | Discharge destination |
| Q75 | - |  |  | SI | Ongoing nursing plan |
| Q76 | - |  |  | SI | Ongoing rehabilitation goals |
| Q77 | - |  |  | SI | Discharge requirement |
| Q78 | - |  |  | SI | Handover given |
| Q79 | - |  |  | SI | Name of the clinician receiving handover |
| Q80 | - |  |  | SI | CP FT |
| Q81 | - |  |  | SI | Form completed by |
| Q82 | - |  |  | SI | Last bowel motion time |
| Q84 | - |  |  | SI | Estimated discharge date |
| Q85 | - |  |  | SI | Date |
| Q86 | - |  |  | SI | Time |
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