# questionnaire.QGXXXLSF

> Laser Safety Form

**Schema:** questionnaire
**Columnas:** 124
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Laser Safety Form

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Laser console / type |
| Q02 | varchar |  |  | SI | Serial Number: Venacure Serial Number |
| Q03 | varchar |  |  | SI | Serial Number: Constellation Serial Number |
| Q04 | varchar |  |  | SI | Serial Number: Holmium Serial Number |
| Q05 | varchar |  |  | SI | Serial Number: CO2 Laser Serial Number |
| Q06 | varchar |  |  | SI | Venacure EVLT 1470 serial number |
| Q07 | varchar |  |  | SI | Constellation machine serial number |
| Q08 | varchar |  |  | SI | Holmium laser serial number |
| Q09 | varchar |  |  | SI | CO2 laser serial number |
| Q10 | varchar |  |  | SI | Laser settings |
| Q11 | varchar |  |  | SI | Left short saphenous |
| Q12 | varchar |  |  | SI | Power (LS) |
| Q13 | varchar |  |  | SI | Mode (LS) |
| Q14 | varchar |  |  | SI | Length (LS) |
| Q15 | varchar |  |  | SI | Duration (LS) |
| Q16 | varchar |  |  | SI | Energy (LS) |
| Q17 | varchar |  |  | SI | Power (RS) |
| Q18 | varchar |  |  | SI | Mode (RS) |
| Q19 | varchar |  |  | SI | Length (RS) |
| Q20 | varchar |  |  | SI | Duration (RS) |
| Q21 | varchar |  |  | SI | Energy (RS) |
| Q22 | varchar |  |  | SI | Power (LL) |
| Q23 | varchar |  |  | SI | Mode (LL) |
| Q24 | varchar |  |  | SI | Length (LL) |
| Q25 | varchar |  |  | SI | Duration (LL) |
| Q26 | varchar |  |  | SI | Energy (LL) |
| Q27 | varchar |  |  | SI | Power (RL) |
| Q28 | varchar |  |  | SI | Mode (RL) |
| Q29 | varchar |  |  | SI | Length (RL) |
| Q30 | varchar |  |  | SI | Duration (RL) |
| Q31 | varchar |  |  | SI | Energy (RL) |
| Q32 | varchar |  |  | SI | Right short saphenous |
| Q33 | varchar |  |  | SI | Left long saphenous |
| Q34 | varchar |  |  | SI | Right long saphenous |
| Q35 | varchar |  |  | SI | Indirect laser |
| Q36 | varchar |  |  | SI | Treatment power (mW) |
| Q37 | varchar |  |  | SI | Duration |
| Q38 | varchar |  |  | SI | Interval |
| Q39 | varchar |  |  | SI | Shots delivered |
| Q40 | varchar |  |  | SI | Total energy (joules) |
| Q46 | varchar |  |  | SI | Laser fibre type / reference number |
| Q47 | varchar |  |  | SI | Laser fibre lot number |
| Q48 | varchar |  |  | SI | Pulse / Sec (HZ) |
| Q49 | varchar |  |  | SI | Energy (kj) |
| Q50 | numeric |  |  | SI | Holium total time |
| Q51 | numeric |  |  | SI | Holium total energy |
| Q52 | varchar |  |  | SI | Safety checklist  |
| Q53 | varchar |  |  | SI | Adverse Events |
| Q55 | varchar |  |  | SI | Laser comments |
| Q56 | varchar |  |  | SI | Disposable laser fibre |
| Q58 | varchar |  |  | SI | Treatment power (mW) |
| Q59 | varchar |  |  | SI | Duration |
| Q60 | varchar |  |  | SI | Interval |
| Q61 | varchar |  |  | SI | Shots delivered |
| Q62 | varchar |  |  | SI | Total energy (joules) |
| Q63 | varchar |  |  | SI | Laser safety operator |
| Q64 | varchar |  |  | SI | Scout / Scribe 	 |
| Q65 | varchar |  |  | SI | Surgeon	 |
| Q66 | varchar |  |  | SI | Anaesthetist 	 |
| Q67 | varchar |  |  | SI | Anatomical area lasered 	 |
| Q68 | numeric |  |  | SI | Power (watts) |
| Q69 | varchar |  |  | SI | Emission mode	 |
| Q70 | date |  |  | SI | Date  |
| Q71 | numeric |  |  | SI | Theatre number 	 |
| Q72 | varchar |  |  | SI | Has smoke evacuator been used? |
| Q73 | varchar |  |  | SI | Emission Mode |
| Q74 | numeric |  |  | SI | Ultra pulse power |
| Q75 | numeric |  |  | SI | Continuous power |
| Q76 | varchar |  |  | SI | Emission mode |
| Q77 | date |  |  | SI | Date |
| Q78 | time |  |  | SI | Time |
| Q79 | time |  |  | SI | Laser start time  |
| Q80 | time |  |  | SI | Laser finish time |
| Q81 | varchar |  |  | SI | Other type of laser |
| Q82 | varchar |  |  | SI | Mode |
| Q83 | varchar |  |  | SI | Laser fibre (microns) |
| Q84 | varchar |  |  | SI | Laser fibre other |
| Q85 | varchar |  |  | SI | Type of patient eye protection applied |
| Q86 | varchar |  |  | SI | Comment |
| Q87 | numeric |  |  | SI | Laser total time |
| Q88 | varchar |  |  | SI | minutes and seconds |
| Q89 | varchar |  |  | SI | Left short saphenous |
| Q90 | numeric |  |  | SI | Power (watts) |
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