# questionnaire.QTCCCLC

> Cardiac Catheterisation Checklist

**Schema:** questionnaire
**Columnas:** 88
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Cardiac Catheterisation Checklist

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Transport arranged |
| Q02 | varchar |  |  | SI | Someone staying with patient overnight |
| Q03 | varchar |  |  | SI | Carer's name and phone number |
| Q04 | varchar |  |  | SI | Support services arranged |
| Q05 | varchar |  |  | SI | Type of service |
| Q06 | varchar |  |  | SI | Phone number |
| Q07 | varchar |  |  | SI | Action taken |
| Q08 | varchar |  |  | SI | Patient lives within 20km of a hospital |
| Q09 | varchar |  |  | SI | Accommodation arranged |
| Q10 | varchar |  |  | SI | Medical certificate required |
| Q11 | varchar |  |  | SI | Completed and given to the patient |
| Q12 | varchar |  |  | SI | ECG monitoring commenced |
| Q13 | varchar |  |  | SI | Any difficulties with swallowing |
| Q14 | varchar |  |  | SI | Antiseptic wash |
| Q15 | varchar |  |  | SI | Lie flat post sheath removal |
| Q16 | time |  |  | SI | May sit up at |
| Q17 | varchar |  |  | SI | Bed rest |
| Q18 | time |  |  | SI | Ambulate at |
| Q19 | time |  |  | SI | Food and fluids as desired at |
| Q20 | varchar |  |  | SI | Observe wound / puncture site blood pressure, puls... |
| Q21 | varchar |  |  | SI | Observe wound / puncture site blood pressure, puls... |
| Q22 | varchar |  |  | SI | Continue medication as charted |
| Q23 | varchar |  |  | SI | No arm movements on affected side for 24 hours |
| Q24 | varchar |  |  | SI | Post procedure ECG |
| Q25 | varchar |  |  | SI | Post procedure X-Ray on inspiration / non inspirat... |
| Q26 | varchar |  |  | SI | Patient requires telemetry monitoring |
| Q27 | time |  |  | SI | Check activated clotting time at |
| Q28 | varchar |  |  | SI | Other |
| Q29 | varchar |  |  | SI | Report to HMO immediately |
| Q30 | varchar |  |  | SI | - signs of peripheral ischaemia |
| Q31 | varchar |  |  | SI | - insertion / puncture site haematoma |
| Q32 | varchar |  |  | SI | IV cannula removed |
| Q33 | varchar |  |  | SI | Wound dry and dressing intact |
| Q34 | varchar |  |  | SI | Nausea and vomiting controlled |
| Q35 | varchar |  |  | SI | Pain controlled |
| Q36 | varchar |  |  | SI | Tolerating fluids and diet |
| Q37 | varchar |  |  | SI | Discharge medication given to patient |
| Q38 | varchar |  |  | SI | Home management plan understood by patient and car... |
| Q39 | varchar |  |  | SI | Vital signs within normal parameters |
| Q40 | varchar |  |  | SI | Valuables returned to patient |
| Q41 | varchar |  |  | SI | Follow up appointment arranged |
| Q42 | varchar |  |  | SI | Patient ambulant without assistance (if previously... |
| Q43 | varchar |  |  | SI | Patient reviewed by medical staff |
| Q44 | varchar |  |  | SI | Cardiac rehabilitation referral completed |
| Q45 | varchar |  |  | SI | Medications to be recommenced as per medication ch... |
| Q46 | date |  |  | SI | Date |
| Q47 | time |  |  | SI | Time |
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