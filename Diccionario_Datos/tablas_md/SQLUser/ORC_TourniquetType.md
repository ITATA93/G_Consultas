# SQLUser.ORC_TourniquetType

**Schema:** SQLUser
**Columnas:** 107
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| TRQTYPE_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Complete on admission and then for the next seven ... |
| Q02 | - |  |  | SI | Date |
| Q03 | - |  |  | SI | Time |
| Q04 | - |  |  | SI | Age |
| Q05 | - |  |  | SI | Mental status |
| Q06 | - |  |  | SI | Elimination |
| Q07 | - |  |  | SI | Medications |
| Q08 | - |  |  | SI | Diagnosis |
| Q09 | - |  |  | SI | Ambulation / Balance |
| Q10 | - |  |  | SI | Nutrition |
| Q11 | - |  |  | SI | Sleep disturbance |
| Q12 | - |  |  | SI | History of falls |
| Q13 | - |  |  | SI | Instructions for Completing the Edmonson Psychiatr... |
| Q14 | - |  |  | SI | Definition of a fall: |
| Q15 | - |  |  | SI | “an event which results in a person coming to rest... |
| Q16 | - |  |  | SI | This includes slips, trips, loss of balance and ap... |
| Q17 | - |  |  | SI | If a patient is found on the floor, it should be a... |
| Q18 | - |  |  | SI | The Edmonson Psychiatric Falls Risk Assessment mus... |
| Q19 | - |  |  | SI | - Is admitted to the Psychiatric Unit |
| Q20 | - |  |  | SI | - Has been identified as a medium or high risk fro... |
| Q21 | - |  |  | SI | - Has had a fall |
| Q22 | - |  |  | SI | The falls risk assessment tool must be completed w... |
| Q23 | - |  |  | SI | Definition Key for Risk Factors: |
| Q24 | - |  |  | SI | Mental Status:  Patient may score for agitation an... |
| Q25 | - |  |  | SI | Elimination: Elimination with assistance is define... |
| Q26 | - |  |  | SI | Diagnosis: Use the doctor’s diagnosis.  Some patie... |
| Q27 | - |  |  | SI | Ambulation/Balance: Patient may score in more than... |
| Q28 | - |  |  | SI | Nutrition: Use the Nurses Notes (24 hour summaries... |
| Q29 | - |  |  | SI | A patient can be given a score of 12 based on any ... |
| Q30 | - |  |  | SI | - Caregiver or patient report of decreased appetit... |
| Q31 | - |  |  | SI | - Documentation of patient meal/supplement intake ... |
| Q32 | - |  |  | SI | - Documentation of “poor fluid intake” within the ... |
| Q33 | - |  |  | SI | - Physical assessment reveals signs of dehydration... |
| Q34 | - |  |  | SI | Sleep Disturbance: Use the nurse’s notes (24 hour ... |
| Q35 | - |  |  | SI | A patient can be given a score of 12 for sleep dis... |
| Q36 | - |  |  | SI | - Patient, family or caregiver report of sleep dis... |
| Q37 | - |  |  | SI | - Documentation of 4 hours or less of consecutive ... |
| Q38 | - |  |  | SI | Medications: (list includes, but is not limited to... |
| Q39 | - |  |  | SI | Psychotropic: Haloperidol, Risperidone, Zyprexa Pr... |
| Q40 | - |  |  | SI | Antidepressants: Zoloft, Celexa, Lexapro, Wellbutr... |
| Q41 | - |  |  | SI | Protriptyline, *Include MAOI's at nurse's discreti... |
| Q42 | - |  |  | SI | Benzodiazepines: Lorazepam, Diazepam, Alprazolam, ... |
| Q43 | - |  |  | SI | Beta Blockers: Atenolol, Esmolol Hydrochloride, La... |
| Q44 | - |  |  | SI | Calcium Channel Blockers: Amlodipine, Diltiazem, I... |
| Q45 | - |  |  | SI | Anti-Arrythrmias: Amiodarone Hydrochloride, Beryll... |
| Q46 | - |  |  | SI | Tocainide Hydrochloride |
| Q47 | - |  |  | SI | ACE Inhibitors: Capotopril, Enalapril, Lisinopriol... |
| Q48 | - |  |  | SI | Vasodilators: Clonidine Hydrochloride, Hydralazine... |
| Q49 | - |  |  | SI | Score |
| Q50 | - |  |  | SI | Classification |
| Q51 | - |  |  | SI | Falls risk |
| Q52 | - |  |  | SI | The Edmonson Psychiatric Fall Risk Assessment Tool... |
| Q53 | - |  |  | SI | ≥ 90 |
| Q54 | - |  |  | SI | ≥ 90: Falls risk |
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
| TRQTYPE_Code | varchar |  |  | NO | Code |
| TRQTYPE_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| TRQTYPE_CreatedDate | date |  |  | SI | Created Date |
| TRQTYPE_CreatedTime | time |  |  | SI | Created Time |
| TRQTYPE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| TRQTYPE_DateFrom | date |  |  | SI | Date From |
| TRQTYPE_DateTo | date |  |  | SI | Date To |
| TRQTYPE_Desc | varchar |  |  | NO | Description |
| TRQTYPE_Owner | varchar |  |  | SI | Owner |
| TRQTYPE_UpdatedDate | date |  |  | SI | Updated Date |
| TRQTYPE_UpdatedTime | time |  |  | SI | Updated Time |
| TRQTYPE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*