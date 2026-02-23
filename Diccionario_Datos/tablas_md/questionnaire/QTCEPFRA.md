# questionnaire.QTCEPFRA

> Edmonson Psychiatric Fall Risk Assessment

**Schema:** questionnaire
**Columnas:** 95
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Edmonson Psychiatric Fall Risk Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Complete on admission and then for the next seven ... |
| Q02 | date |  |  | SI | Date |
| Q03 | time |  |  | SI | Time |
| Q04 | varchar |  |  | SI | Age |
| Q05 | varchar |  |  | SI | Mental status |
| Q06 | varchar |  |  | SI | Elimination |
| Q07 | varchar |  |  | SI | Medications |
| Q08 | varchar |  |  | SI | Diagnosis |
| Q09 | varchar |  |  | SI | Ambulation / Balance |
| Q10 | varchar |  |  | SI | Nutrition |
| Q11 | varchar |  |  | SI | Sleep disturbance |
| Q12 | varchar |  |  | SI | History of falls |
| Q13 | varchar |  |  | SI | Instructions for Completing the Edmonson Psychiatr... |
| Q14 | varchar |  |  | SI | Definition of a fall: |
| Q15 | varchar |  |  | SI | “an event which results in a person coming to rest... |
| Q16 | varchar |  |  | SI | This includes slips, trips, loss of balance and ap... |
| Q17 | varchar |  |  | SI | If a patient is found on the floor, it should be a... |
| Q18 | varchar |  |  | SI | The Edmonson Psychiatric Falls Risk Assessment mus... |
| Q19 | varchar |  |  | SI | - Is admitted to the Psychiatric Unit |
| Q20 | varchar |  |  | SI | - Has been identified as a medium or high risk fro... |
| Q21 | varchar |  |  | SI | - Has had a fall |
| Q22 | varchar |  |  | SI | The falls risk assessment tool must be completed w... |
| Q23 | varchar |  |  | SI | Definition Key for Risk Factors: |
| Q24 | varchar |  |  | SI | Mental Status:  Patient may score for agitation an... |
| Q25 | varchar |  |  | SI | Elimination: Elimination with assistance is define... |
| Q26 | varchar |  |  | SI | Diagnosis: Use the doctor’s diagnosis.  Some patie... |
| Q27 | varchar |  |  | SI | Ambulation/Balance: Patient may score in more than... |
| Q28 | varchar |  |  | SI | Nutrition: Use the Nurses Notes (24 hour summaries... |
| Q29 | varchar |  |  | SI | A patient can be given a score of 12 based on any ... |
| Q30 | varchar |  |  | SI | - Caregiver or patient report of decreased appetit... |
| Q31 | varchar |  |  | SI | - Documentation of patient meal/supplement intake ... |
| Q32 | varchar |  |  | SI | - Documentation of “poor fluid intake” within the ... |
| Q33 | varchar |  |  | SI | - Physical assessment reveals signs of dehydration... |
| Q34 | varchar |  |  | SI | Sleep Disturbance: Use the nurse’s notes (24 hour ... |
| Q35 | varchar |  |  | SI | A patient can be given a score of 12 for sleep dis... |
| Q36 | varchar |  |  | SI | - Patient, family or caregiver report of sleep dis... |
| Q37 | varchar |  |  | SI | - Documentation of 4 hours or less of consecutive ... |
| Q38 | varchar |  |  | SI | Medications: (list includes, but is not limited to... |
| Q39 | varchar |  |  | SI | Psychotropic: Haloperidol, Risperidone, Zyprexa Pr... |
| Q40 | varchar |  |  | SI | Antidepressants: Zoloft, Celexa, Lexapro, Wellbutr... |
| Q41 | varchar |  |  | SI | Protriptyline, *Include MAOI's at nurse's discreti... |
| Q42 | varchar |  |  | SI | Benzodiazepines: Lorazepam, Diazepam, Alprazolam, ... |
| Q43 | varchar |  |  | SI | Beta Blockers: Atenolol, Esmolol Hydrochloride, La... |
| Q44 | varchar |  |  | SI | Calcium Channel Blockers: Amlodipine, Diltiazem, I... |
| Q45 | varchar |  |  | SI | Anti-Arrythrmias: Amiodarone Hydrochloride, Beryll... |
| Q46 | varchar |  |  | SI | Tocainide Hydrochloride |
| Q47 | varchar |  |  | SI | ACE Inhibitors: Capotopril, Enalapril, Lisinopriol... |
| Q48 | varchar |  |  | SI | Vasodilators: Clonidine Hydrochloride, Hydralazine... |
| Q49 | varchar |  |  | SI | Score |
| Q50 | varchar |  |  | SI | Classification |
| Q51 | varchar |  |  | SI | Falls risk |
| Q52 | varchar |  |  | SI | The Edmonson Psychiatric Fall Risk Assessment Tool... |
| Q53 | varchar |  |  | SI | ≥ 90 |
| Q54 | varchar |  |  | SI | ≥ 90: Falls risk |
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