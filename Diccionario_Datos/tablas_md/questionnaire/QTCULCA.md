# questionnaire.QTCULCA

> Upper Limb Coordination Assessment

**Schema:** questionnaire
**Columnas:** 120
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Upper Limb Coordination Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Test |
| Q04 | varchar |  |  | SI | Left |
| Q05 | varchar |  |  | SI | Right |
| Q06 | varchar |  |  | SI | Bilateral Integration |
| Q07 | varchar |  |  | SI | Comments |
| Q08 | varchar |  |  | SI | Test |
| Q09 | varchar |  |  | SI | Left |
| Q10 | varchar |  |  | SI | Right |
| Q11 | varchar |  |  | SI | Comments |
| Q12 | varchar |  |  | SI | Rapid Alternating Movements (RAM) |
| Q13 | varchar |  |  | SI | Finger-to-nose |
| Q14 | varchar |  |  | SI | Finger-to-finger |
| Q15 | varchar |  |  | SI | Finger-to-therapist's finger |
| Q16 | varchar |  |  | SI | Alternate nose-to-finger |
| Q17 | varchar |  |  | SI | Mass grasp |
| Q18 | varchar |  |  | SI | Rebound phenomena |
| Q19 | varchar |  |  | SI | Rapid alternating movements - left |
| Q20 | varchar |  |  | SI | Rapid alternating movements - right |
| Q21 | varchar |  |  | SI | Rapid alternating movements - bilateral integratio... |
| Q22 | varchar |  |  | SI | Rapid alternating movements - comments |
| Q23 | varchar |  |  | SI | Finger-to-nose - left |
| Q24 | varchar |  |  | SI | Finger-to-nose - right |
| Q25 | varchar |  |  | SI | Finger-to-nose comments |
| Q26 | varchar |  |  | SI | Finger-to-finger - left |
| Q27 | varchar |  |  | SI | Finger-to-finger - right |
| Q28 | varchar |  |  | SI | Finger-to-finger comments |
| Q29 | varchar |  |  | SI | Finger-to-therapist's finger - left |
| Q30 | varchar |  |  | SI | Finger-to-therapist's finger - right |
| Q31 | varchar |  |  | SI | Finger-to-therapist's finger comments |
| Q32 | varchar |  |  | SI | Alternate nose-to-finger - left |
| Q33 | varchar |  |  | SI | Alternate nose-to-finger - right |
| Q34 | varchar |  |  | SI | Alternate nose-to-finger comments |
| Q35 | varchar |  |  | SI | Finger opposition - left |
| Q36 | varchar |  |  | SI | Finger opposition - right |
| Q37 | varchar |  |  | SI | Finger opposition comments |
| Q38 | varchar |  |  | SI | Mass grasp - left |
| Q39 | varchar |  |  | SI | Mass grasp - right |
| Q40 | varchar |  |  | SI | Mass grasp - bilateral integration |
| Q41 | varchar |  |  | SI | Mass grasp comments |
| Q42 | varchar |  |  | SI | Rebound phenomena - left |
| Q43 | varchar |  |  | SI | Rebound phenomena - right |
| Q44 | varchar |  |  | SI | Rebound phenomena - bilateral integration |
| Q45 | varchar |  |  | SI | Rebound phenomena comments |
| Q46 | varchar |  |  | SI | Additional detail |
| Q47 | varchar |  |  | SI | Assessment Instructions |
| Q48 | varchar |  |  | SI | Finger-to-Nose: |
| Q49 | varchar |  |  | SI | The shoulder is abducted to 90 degrees with elbow ... |
| Q50 | varchar |  |  | SI | Finger-to-Therapist’s finger: |
| Q51 | varchar |  |  | SI | The patient and therapist sit opposite each other.... |
| Q52 | varchar |  |  | SI | Finger-to-Finger: |
| Q53 | varchar |  |  | SI | Both shoulders are abducted to 90 degrees with the... |
| Q54 | varchar |  |  | SI | Alternate nose-to-finger:  |
| Q55 | varchar |  |  | SI | The patient alternately touches the tip of his or ... |
| Q56 | varchar |  |  | SI | Finger Opposition: |
| Q57 | varchar |  |  | SI | The patient touches the tip of the thumb to the ti... |
| Q58 | varchar |  |  | SI | Mass Grasp: |
| Q59 | varchar |  |  | SI | An alteration is made between opening and closing ... |
| Q60 | varchar |  |  | SI | Rebound phenomena: |
| Q61 | varchar |  |  | SI | The patient is positioned with the elbow flexed. T... |
| Q62 | varchar |  |  | SI | Normally, the opposite muscle group (triceps) will... |
| Q63 | varchar |  |  | SI | Guide to assessment |
| Q64 | varchar |  |  | SI | No impairment: |
| Q65 | varchar |  |  | SI | Able to accomplish activity with no notable impair... |
| Q66 | varchar |  |  | SI | Impairment: |
| Q67 | varchar |  |  | SI | Activity completed or partially completed with imp... |
| Q68 | varchar |  |  | SI | Minimal impairment: |
| Q69 | varchar |  |  | SI | Able to accomplish activity, slightly less than no... |
| Q70 | varchar |  |  | SI | Moderate impairment: |
| Q71 | varchar |  |  | SI | Able to accomplish activity movements are slow, aw... |
| Q72 | varchar |  |  | SI | Severe impairment: |
| Q73 | varchar |  |  | SI | Able only to initiate activity without completion;... |
| Q74 | varchar |  |  | SI | Activity not possible: |
| Q75 | varchar |  |  | SI | Not tested: |
| Q76 | varchar |  |  | SI | Test not commenced - use comments to explain as re... |
| Q77 | varchar |  |  | SI | Finger opposition |
| Q78 | varchar |  |  | SI | Finger opposition - bilateral integration |
| Q79 | varchar |  |  | SI | Patient unable to initiate activity. |
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