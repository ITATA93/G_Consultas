# questionnaire.QTCBWAT

> Bates-Jensen Wound Assessment Tool (BWAT)

**Schema:** questionnaire
**Columnas:** 87
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Bates-Jensen Wound Assessment Tool (BWAT)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date of assessment |
| Q02 | varchar |  |  | SI | Location (anatomic site) |
| Q03 | varchar |  |  | SI | If other site, specify |
| Q04 | varchar |  |  | SI | Laterality |
| Q05 | varchar |  |  | SI | Shape |
| Q06 | varchar |  |  | SI | If other shape, specify |
| Q07 | varchar |  |  | SI | Body map |
| Q08 | varchar |  |  | SI | Size |
| Q09 | varchar |  |  | SI | Depth |
| Q10 | varchar |  |  | SI | Edges |
| Q11 | varchar |  |  | SI | Undermining |
| Q12 | varchar |  |  | SI | Necrotic tissue type |
| Q13 | varchar |  |  | SI | Necrotic tissue amount |
| Q14 | varchar |  |  | SI | Exudate type |
| Q15 | varchar |  |  | SI | Exudate amount |
| Q16 | varchar |  |  | SI | Skin colour surrounding wound |
| Q17 | varchar |  |  | SI | Peripheral tissue oedema |
| Q18 | varchar |  |  | SI | Peripheral tissue induration |
| Q19 | varchar |  |  | SI | Granulation tissue |
| Q20 | varchar |  |  | SI | Epithelialisation |
| Q21 | varchar |  |  | SI | Fill out the rating sheet to assess a wound’s stat... |
| Q22 | varchar |  |  | SI | Evaluate once a week and whenever a change occurs ... |
| Q23 | varchar |  |  | SI | Rate according to each item by picking the respons... |
| Q24 | varchar |  |  | SI | Once the wound is rated on all items, the total sc... |
| Q25 | varchar |  |  | SI | The HIGHER the total score, the more severe the wo... |
| Q26 | varchar |  |  | SI | Compare the total scores with their dates to deter... |
| Q27 | varchar |  |  | SI | Score |
| Q28 | varchar |  |  | SI | Classification |
| Q29 | varchar |  |  | SI | 13 - 20 |
| Q30 | varchar |  |  | SI | Minimal Severity |
| Q31 | varchar |  |  | SI | 21 - 30 |
| Q32 | varchar |  |  | SI | Mild Severity |
| Q33 | varchar |  |  | SI | 31 - 40 |
| Q34 | varchar |  |  | SI | Moderate Severity |
| Q35 | varchar |  |  | SI | The Bates-Jensen wound assessment tool (BWAT) is a... |
| Q36 | varchar |  |  | SI | of wound vocabulary and wound-assessment skills. |
| Q37 | varchar |  |  | SI | 13 - 20: Minimal Severity |
| Q38 | varchar |  |  | SI | 21 - 30: Mild Severity |
| Q39 | varchar |  |  | SI | 31 - 40: Moderate Severity |
| Q40 | varchar |  |  | SI | 41 - 65: Extreme Severity |
| Q41 | varchar |  |  | SI | 41 - 65 |
| Q42 | varchar |  |  | SI | Extreme Severity |
| Q43 | varchar |  |  | SI | Location (anatomic site) |
| Q44 | date |  |  | SI | Date |
| Q45 | time |  |  | SI | Time |
| Q46 | varchar |  |  | SI | Bates-Jensen BM, Vredevoe DL, Brecht ML. Validity ... |
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