# questionnaire.QTCNTS

> Nursing Transfer Summary

**Schema:** questionnaire
**Columnas:** 127
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Nursing Transfer Summary

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Identify |
| Q02 | varchar |  |  | SI | To be completed for ward transfers and transfers b... |
| Q03 | varchar |  |  | SI | Transfer of care discussed with patient |
| Q04 | varchar |  |  | SI | Family / Carer / Other (please specify) |
| Q05 | varchar |  |  | SI | Consultant notified |
| Q06 | varchar |  |  | SI | If no, reason |
| Q07 | varchar |  |  | SI | Discharge summary completed |
| Q08 | varchar |  |  | SI | Interpreter required |
| Q09 | varchar |  |  | SI | Primary language spoken |
| Q10 | varchar |  |  | SI | Situation |
| Q11 | varchar |  |  | SI | Principal diagnosis |
| Q12 | varchar |  |  | SI | Nursing problem |
| Q12A | varchar |  |  | SI | Nursing problem |
| Q13 | varchar |  |  | SI | Reason for transfer |
| Q14 | varchar |  |  | SI | Legal status |
| Q15 | varchar |  |  | SI | Allergies (please check the patient record) |
| Q16 | varchar |  |  | SI | Patient ID band checked and updated |
| Q17 | varchar |  |  | SI | Mode of transportation |
| Q18 | varchar |  |  | SI | Other mode of transportation |
| Q19 | varchar |  |  | SI | By whom |
| Q20 | varchar |  |  | SI | Background |
| Q21 | varchar |  |  | SI | Clinical risk and alerts updated and communicated ... |
| Q22 | varchar |  |  | SI | Alerts comments |
| Q23 | varchar |  |  | SI | Mental / Cognitive / Behaviour |
| Q24 | varchar |  |  | SI | Other |
| Q25 | varchar |  |  | SI | Current cognitive state |
| Q26 | varchar |  |  | SI | Patient living arrangements |
| Q27 | varchar |  |  | SI | ACAS completed |
| Q28 | varchar |  |  | SI | Anticipated living arrangement |
| Q29 | varchar |  |  | SI | Allied health interventions completed |
| Q30 | varchar |  |  | SI | Other AHP |
| Q31 | varchar |  |  | SI | Nutrition |
| Q32 | varchar |  |  | SI | Nutrition comments |
| Q33 | varchar |  |  | SI | Elimination |
| Q34 | varchar |  |  | SI | Bowel patterns |
| Q35 | date |  |  | SI | Last bowel motion date and time |
| Q36 | varchar |  |  | SI | Urinary patterns |
| Q37 | date |  |  | SI | Last voided date |
| Q38 | varchar |  |  | SI | Indwelling catheter |
| Q39 | varchar |  |  | SI | Size |
| Q40 | date |  |  | SI | Date inserted |
| Q41 | varchar |  |  | SI | Mobility |
| Q42 | varchar |  |  | SI | ADL / Hygiene |
| Q43 | varchar |  |  | SI | Assessment |
| Q44 | varchar |  |  | SI | Intravascular access |
| Q45 | varchar |  |  | SI | Other IV access |
| Q46 | varchar |  |  | SI | Site 1 |
| Q47 | varchar |  |  | SI | Site 2 |
| Q48 | varchar |  |  | SI | Site 3 |
| Q49 | date |  |  | SI | Date inserted 1 |
| Q50 | date |  |  | SI | Date inserted 2 |
| Q51 | date |  |  | SI | Date inserted 3 |
| Q52 | varchar |  |  | SI | Skin |
| Q53 | varchar |  |  | SI | Wound surgical site |
| Q54 | varchar |  |  | SI | Closure technique |
| Q55 | date |  |  | SI | Drain inserted on |
| Q56 | date |  |  | SI | Drain changed on |
| Q57 | varchar |  |  | SI | Wound status |
| Q58 | varchar |  |  | SI | Sleep patterns |
| Q59 | varchar |  |  | SI | Neurological status |
| Q60 | varchar |  |  | SI | Valuables |
| Q61 | varchar |  |  | SI | Clothing |
| Q62 | varchar |  |  | SI | Glasses |
| Q63 | varchar |  |  | SI | Dentures |
| Q64 | varchar |  |  | SI | Hearing aid |
| Q65 | varchar |  |  | SI | Jewelleries |
| Q66 | varchar |  |  | SI | Contact lens |
| Q67 | varchar |  |  | SI | Bridge |
| Q68 | varchar |  |  | SI | Prosthesis |
| Q69 | varchar |  |  | SI | Valuables comments |
| Q70 | varchar |  |  | SI | Toiletries |
| Q71 | varchar |  |  | SI | Request / Recommendations |
| Q72 | varchar |  |  | SI | Discharge plan |
| Q73 | varchar |  |  | SI | Estimated discharge date |
| Q74 | varchar |  |  | SI | Discharge destination |
| Q75 | varchar |  |  | SI | Ongoing nursing plan |
| Q76 | varchar |  |  | SI | Ongoing rehabilitation goals |
| Q77 | varchar |  |  | SI | Discharge requirement |
| Q78 | varchar |  |  | SI | Handover given |
| Q79 | varchar |  |  | SI | Name of the clinician receiving handover |
| Q80 | varchar |  |  | SI | CP FT |
| Q81 | varchar |  |  | SI | Form completed by |
| Q82 | time |  |  | SI | Last bowel motion time |
| Q84 | varchar |  |  | SI | Estimated discharge date |
| Q85 | date |  |  | SI | Date |
| Q86 | time |  |  | SI | Time |
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