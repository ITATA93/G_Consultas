# questionnaire.QTCHOPA

> Home Oxygen Program Assessment

**Schema:** questionnaire
**Columnas:** 112
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Home Oxygen Program Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Patient Location at Time of Request |
| Q02 | varchar |  |  | SI | Ward |
| Q03 | date |  |  | SI | Discharge date |
| Q04 | varchar |  |  | SI | Delivery details |
| Q05 | varchar |  |  | SI | Give details |
| Q06 | varchar |  |  | SI | Select therapy group |
| Q07 | varchar |  |  | SI | Has the patient been referred to palliative care s... |
| Q08 | varchar |  |  | SI | Is life expectancy <3 months |
| Q09 | varchar |  |  | SI | Arterial blood gases taken? |
| Q10 | varchar |  |  | SI | Diagnostic details |
| Q11 | varchar |  |  | SI | Provide details |
| Q12 | varchar |  |  | SI | Right heart failure |
| Q13 | varchar |  |  | SI | Polycythaemia |
| Q14 | varchar |  |  | SI | Pulmonary hypertension |
| Q15 | varchar |  |  | SI | Medication class |
| Q16 | varchar |  |  | SI | Provide details |
| Q17 | bigint |  |  | SI | Four week review details |
| Q17TxtOnly | bigint |  |  | SI | Four week review details Plain Text Only |
| Q18 | varchar |  |  | SI | Name |
| Q19 | varchar |  |  | SI | Speciality |
| Q20 | varchar |  |  | SI | Department |
| Q21 | numeric |  |  | SI | Phone |
| Q22 | numeric |  |  | SI | Pager |
| Q23 | longvarbinary |  |  | SI | Signed |
| Q23UDt | date |  |  | SI | Signed Last Updated Date |
| Q23UTm | time |  |  | SI | Signed Last Updated Time |
| Q24 | date |  |  | SI | Date |
| Q25 | varchar |  |  | SI | NB. May be signed by either Physician or Chronic R... |
| Q26 | date |  |  | SI | Date |
| Q27 | varchar |  |  | SI | Room Air |
| Q28 | numeric |  |  | SI | pH |
| Q29 | numeric |  |  | SI | PaCO2 (mmHg) |
| Q30 | numeric |  |  | SI | PaO2 (mmHg) |
| Q31 | numeric |  |  | SI | SaO2 (%) |
| Q32 | numeric |  |  | SI | COHb % |
| Q33 | date |  |  | SI | Date |
| Q34 | numeric |  |  | SI | Awake baseline SpO2 (%) |
| Q35 | numeric |  |  | SI | Minimum asleep SpO2 (%) |
| Q36 | numeric |  |  | SI | % Sleep time SpO2 < 88% |
| Q37 | varchar |  |  | SI | Patient mobility |
| Q38 | varchar |  |  | SI | Aid detail |
| Q39 | date |  |  | SI | Date |
| Q40 | numeric |  |  | SI | SpO2 (%) room air |
| Q41 | numeric |  |  | SI | SpO2 (%) on oxygen |
| Q42 | varchar |  |  | SI | Select options and specify O2 flow rate and usage |
| Q43 | varchar |  |  | SI | Oxygen concentrator |
| Q44 | numeric |  |  | SI | O2 flow (L/min) |
| Q45 | numeric |  |  | SI | Usage (hrs/day) |
| Q46 | varchar |  |  | SI | Portable oxygen |
| Q47 | varchar |  |  | SI | Type |
| Q48 | varchar |  |  | SI | Cylinder |
| Q49 | numeric |  |  | SI | O2 flow (L/min) |
| Q50 | varchar |  |  | SI | Usage (hrs/day) |
| Q51 | varchar |  |  | SI | Cylinder |
| Q52 | varchar |  |  | SI | Emergency |
| Q53 | numeric |  |  | SI | O2 flow (L/min) |
| Q54 | varchar |  |  | SI | Usage (hrs/day) |
| Q55 | longvarbinary |  |  | SI | Signature |
| Q55UDt | date |  |  | SI | Signature Last Updated Date |
| Q55UTm | time |  |  | SI | Signature Last Updated Time |
| Q56 | varchar |  |  | SI | Name |
| Q57 | varchar |  |  | SI | Destination |
| Q58 | date |  |  | SI | Date |
| Q59 | varchar |  |  | SI | If Palliative: |
| Q60 | varchar |  |  | SI | Patient checks |
| Q61 | varchar |  |  | SI | Delivery address |
| Q62 | varchar |  |  | SI | Delivery address comments |
| Q63 | date |  |  | SI | Date |
| Q64 | time |  |  | SI | Time |
| Q65 | varchar |  |  | SI | Provider number |
| Q66 | numeric |  |  | SI | COHb % |
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