# questionnaire.QTCNSSHC

> Safe at Home Checklist

**Schema:** questionnaire
**Columnas:** 88
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Safe at Home Checklist

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Use this list to identify fall hazards and accessi... |
| Q02 | varchar |  |  | SI | Exterior entrances and exit |
| Q02A | varchar |  |  | SI | Exterior entrances and exit |
| Q03 | varchar |  |  | SI | Interior doors, stairs, halls |
| Q03A | varchar |  |  | SI | Interior doors, stairs, halls |
| Q04 | varchar |  |  | SI | Bathroom |
| Q04A | varchar |  |  | SI | Bathroom |
| Q05 | varchar |  |  | SI | Kitchen |
| Q05A | varchar |  |  | SI | Kitchen |
| Q06 | varchar |  |  | SI | Living, dining, bedroom |
| Q06A | varchar |  |  | SI | Living, dining, bedroom |
| Q07 | varchar |  |  | SI | Laundry |
| Q07A | varchar |  |  | SI | Laundry |
| Q08 | varchar |  |  | SI | Telephone and door |
| Q08A | varchar |  |  | SI | Telephone and door |
| Q09 | varchar |  |  | SI | Storage space |
| Q09A | varchar |  |  | SI | Storage space |
| Q10 | varchar |  |  | SI | Windows |
| Q10A | varchar |  |  | SI | Windows |
| Q11 | varchar |  |  | SI | Electrical outlets and controls |
| Q11A | varchar |  |  | SI | Electrical outlets and controls |
| Q12 | varchar |  |  | SI | Heat, light, ventilation, security, carbon monoxid... |
| Q12A | varchar |  |  | SI | Heat, light, ventilation, security, carbon monoxid... |
| Q13 | varchar |  |  | SI | Comments |
| Q14 | varchar |  |  | SI | Use this list to prioritize work tasks |
| Q15 | varchar |  |  | SI | Exterior entrances and exits |
| Q15A | varchar |  |  | SI | Exterior entrances and exits |
| Q16 | varchar |  |  | SI | Interior doors, halls, stairs |
| Q16A | varchar |  |  | SI | Interior doors, halls, stairs |
| Q17 | varchar |  |  | SI | Bathroom |
| Q17A | varchar |  |  | SI | Bathroom |
| Q18 | varchar |  |  | SI | Kitchen |
| Q18A | varchar |  |  | SI | Kitchen |
| Q19 | varchar |  |  | SI | Living, dining, bedroom |
| Q19A | varchar |  |  | SI | Living, dining, bedroom |
| Q20 | varchar |  |  | SI | Laundry |
| Q20A | varchar |  |  | SI | Laundry |
| Q21 | varchar |  |  | SI | Telephone and door |
| Q21A | varchar |  |  | SI | Telephone and door |
| Q22 | varchar |  |  | SI | Storage space |
| Q22A | varchar |  |  | SI | Storage space |
| Q23 | varchar |  |  | SI | Windows |
| Q23A | varchar |  |  | SI | Windows |
| Q24 | varchar |  |  | SI | Electrical outlets and controls |
| Q24A | varchar |  |  | SI | Electrical outlets and controls |
| Q25 | varchar |  |  | SI | Heat, light, ventilation, security, carbon monoxid... |
| Q25A | varchar |  |  | SI | Heat, light, ventilation, security, carbon monoxid... |
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