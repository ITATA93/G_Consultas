# questionnaire.QGXXXICUNAC

> ICU Nursing Admission Checklist

**Schema:** questionnaire
**Columnas:** 123
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* ICU Nursing Admission Checklist

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Two ID bands on patient |
| Q02 | varchar |  |  | SI | Alarm limits set |
| Q03 | varchar |  |  | SI | Bloods collected and sent  |
| Q04 | varchar |  |  | SI | ECG if indicated |
| Q05 | varchar |  |  | SI | Chest X-ray attended |
| Q06 | varchar |  |  | SI | Medications locked in patients drawer |
| Q07 | varchar |  |  | SI | Personal belongings with patient |
| Q08 | varchar |  |  | SI | Toiletries  |
| Q09 | varchar |  |  | SI | Dentures - Upper |
| Q10 | varchar |  |  | SI | Hearing aid - Left |
| Q11 | varchar |  |  | SI | Valuables |
| Q12 | varchar |  |  | SI | Valuables stored as per policy |
| Q13 | varchar |  |  | SI | Glasses |
| Q14 | varchar |  |  | SI | Alerts reviewed activated including signage / PPE ... |
| Q15 | varchar |  |  | SI | Admitted in central monitor |
| Q16 | varchar |  |  | SI | Admission book updated with date, time and diagnos... |
| Q17 | varchar |  |  | SI | Critical care certificate commenced at bedside |
| Q18 | varchar |  |  | SI | Anzics form commenced at bedside |
| Q19 | varchar |  |  | SI | Next of kin (NOK) details verified |
| Q20 | varchar |  |  | SI | Complete core obs set on admission |
| Q21 | varchar |  |  | SI | Set nursing task for core obs |
| Q22 | varchar |  |  | SI | Complete initial ICU nursing care assessment  |
| Q23 | varchar |  |  | SI | Monitoring plan assessed and completed |
| Q24 | varchar |  |  | SI | Clinical handover received documented in notes |
| Q25 | varchar |  |  | SI | Commence events i.e. ventilation |
| Q26 | varchar |  |  | SI | X-rays placed in the allocated slot at the desk |
| Q27 | varchar |  |  | SI | Denture - Lower |
| Q28 | varchar |  |  | SI | Hearing aid - Right |
| Q29 | varchar |  |  | SI | Check identification (ID) band/s on patient |
| Q30 | varchar |  |  | SI | Alarm limits set |
| Q31 | varchar |  |  | SI | Bloods collected and sent |
| Q32 | varchar |  |  | SI | ECG if indicated |
| Q33 | varchar |  |  | SI | Chest X-ray attended |
| Q34 | varchar |  |  | SI | Medications locked in patients drawer |
| Q35 | varchar |  |  | SI | Toiletries |
| Q36 | varchar |  |  | SI | Dentures - Upper |
| Q37 | varchar |  |  | SI | Hearing aid - Left |
| Q38 | varchar |  |  | SI | Valuables stored as per policy |
| Q39 | varchar |  |  | SI | Glasses |
| Q40 | varchar |  |  | SI | Precaution signage activated and personal protecti... |
| Q41 | varchar |  |  | SI | Admitted in central monitor |
| Q42 | varchar |  |  | SI | Admission book updated |
| Q43 | varchar |  |  | SI | Critical care certificate commenced at bedside |
| Q44 | varchar |  |  | SI | ANZICS form commenced at bedside |
| Q45 | varchar |  |  | SI | Patient contact details completed including next o... |
| Q46 | varchar |  |  | SI | Admission observations completed |
| Q47 | varchar |  |  | SI | Set nursing task for core observations |
| Q48 | varchar |  |  | SI | Admission assessments completed |
| Q49 | varchar |  |  | SI | Monitoring plan assessed and completed |
| Q50 | varchar |  |  | SI | Clinical handover received |
| Q51 | varchar |  |  | SI | Commence events i.e. ventilation |
| Q52 | varchar |  |  | SI | X-rays placed in the allocated slot at the desk |
| Q53 | varchar |  |  | SI | Denture - Lower |
| Q54 | varchar |  |  | SI | Hearing aid - Right |
| Q55 | date |  |  | SI | Date |
| Q56 | time |  |  | SI | Time |
| Q57 | varchar |  |  | SI | Allergies and alerts reviewed - red ID band in sit... |
| Q58 | varchar |  |  | SI | NOK / Relatives oriented to the unit and routines |
| Q59 | varchar |  |  | SI | NOK and/or patient provided with health charter, v... |
| Q60 | varchar |  |  | SI | Patient check and NOK notes |
| Q61 | varchar |  |  | SI | Connect patient to the ICU monitor, ventilator and... |
| Q62 | varchar |  |  | SI | Invasive devices summary reviewed and updated |
| Q63 | varchar |  |  | SI | Transduced all central line devices |
| Q64 | varchar |  |  | SI | Commence events i.e. ventilation |
| Q65 | varchar |  |  | SI | Admission bloods and arterial blood gas (ABG) take... |
| Q66 | varchar |  |  | SI | ECG performed and reviewed |
| Q67 | varchar |  |  | SI | Admission microbiology sent |
| Q68 | varchar |  |  | SI | Chest X-ray performed and reviewed |
| Q69 | varchar |  |  | SI | Toiletries |
| Q70 | varchar |  |  | SI | Dentures - upper |
| Q71 | varchar |  |  | SI | Denture - lower |
| Q72 | varchar |  |  | SI | Hearing aid - right |
| Q73 | varchar |  |  | SI | Hearing aid - left |
| Q74 | varchar |  |  | SI | Glasses |
| Q75 | varchar |  |  | SI | Personal belonging detail |
| Q76 | varchar |  |  | SI | Valuables stored as per policy |
| Q77 | varchar |  |  | SI | Valuables detail |
| Q78 | varchar |  |  | SI | Patient property form completed |
| Q79 | varchar |  |  | SI | Admission checklist notes |
| Q80 | varchar |  |  | SI | Medications locked in patient's drawer |
| Q81 | varchar |  |  | SI | X-rays placed in the allocated slot at the desk |
| Q82 | varchar |  |  | SI | Other personal belongings |
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