# questionnaire.QTCDRS

> Disability Rating Scale (DRS)

**Schema:** questionnaire
**Columnas:** 112
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Disability Rating Scale (DRS)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Completed at	 |
| Q02 | varchar |  |  | SI | Eye opening	 |
| Q03 | varchar |  |  | SI | Communication ability |
| Q04 | varchar |  |  | SI | Motor response |
| Q05 | varchar |  |  | SI | Feeding (cognitive ability only) |
| Q06 | varchar |  |  | SI | Toileting (cognitive ability only)	 |
| Q07 | varchar |  |  | SI | Grooming (cognitive ability only) |
| Q08 | varchar |  |  | SI | Level of functioning (physical, mental, emotional ... |
| Q09 | varchar |  |  | SI | ''Employability'' (as a full time worker, homemake... |
| Q10 | varchar |  |  | SI | 0 indicates no disability |
| Q11 | varchar |  |  | SI | 29 indicates an extreme vegetative state |
| Q12 | varchar |  |  | SI | 0-Spontaneus: eyes open with sleep / wake rhythms ... |
| Q13 | varchar |  |  | SI | 1 - To speech and/or sensory stimulation: a respon... |
| Q14 | varchar |  |  | SI |  not necessarily the command to open the eyes. Als... |
| Q15 | varchar |  |  | SI | 2 - To pain: tested by a painful stimulation |
| Q16 | varchar |  |  | SI | 3 - None: no eye opening even to painful stimulati... |
| Q17 | varchar |  |  | SI | 0 - Oriented: implies awareness of self and the en... |
| Q18 | varchar |  |  | SI | 1 - Confused: attention can be held and patient re... |
| Q19 | varchar |  |  | SI | 2 - Inappropriate: intelligible articulation but s... |
| Q20 | varchar |  |  | SI | 3 - Incomprehensible: moaning, groaning or sounds ... |
| Q21 | varchar |  |  | SI | 4 - None: no sounds or communication signs from pa... |
| Q22 | varchar |  |  | SI | 0 - Obeying: obeying command to move finger on bes... |
| Q23 | varchar |  |  | SI | 1 - Localizing: a painful stimulus at more than on... |
| Q24 | varchar |  |  | SI | If there is doubt as to whether withdrawal or loca... |
| Q25 | varchar |  |  | SI | 2 - Withdrawing: any generalized movement away fro... |
| Q26 | varchar |  |  | SI | 3 - Flexing: painful stimulation results in either... |
| Q27 | varchar |  |  | SI | If there is confusion between flexing and withdraw... |
| Q28 | varchar |  |  | SI | 4 - Extending: painful stimulation results in exte... |
| Q29 | varchar |  |  | SI | 5 - None: no response can be elicited. Usually ass... |
| Q30 | varchar |  |  | SI | 0 - Complete: continuously shows awareness that he... |
| Q31 | varchar |  |  | SI | 1 - Partial: intermittently shows awareness that h... |
| Q32 | varchar |  |  | SI | 2 - Minimal: shows questionable or infrequent awar... |
| Q33 | varchar |  |  | SI | sounds or activities that he is vaguely aware when... |
| Q34 | varchar |  |  | SI | 3 - None: shows virtually no awareness at any time... |
| Q35 | varchar |  |  | SI | 0 - Completetly independent: able to live as he wi... |
| Q36 | varchar |  |  | SI | 1 - Independent in special environment: capable of... |
| Q37 | varchar |  |  | SI | 3 - Moderately dependent-moderate assist (person i... |
| Q38 | varchar |  |  | SI | 4 - Markedly dependent-moderate assist (person in ... |
| Q39 | varchar |  |  | SI | 5 - Totally dependent - 24 hour nursing care: not ... |
| Q40 | varchar |  |  | SI | The psychosocial adaptability or ''employability''... |
| Q41 | varchar |  |  | SI | This determination should take into account consid... |
| Q42 | varchar |  |  | SI | 1. Able to understand, remember and follow instruc... |
| Q43 | varchar |  |  | SI | industrial situations or can do school assignments... |
| Q44 | varchar |  |  | SI | using private or public transportation effectively... |
| Q45 | varchar |  |  | SI | 7. Ability to keep track of time schedules and app... |
| Q46 | varchar |  |  | SI | 0 - Not restricted: can compete in the open market... |
| Q47 | varchar |  |  | SI | responsibilities associated with homemaking; or ca... |
| Q48 | varchar |  |  | SI | 1 - Selected jobs, competitive: can compete in a l... |
| Q49 | varchar |  |  | SI | limitations; or can initiate, plan, execute and as... |
| Q50 | varchar |  |  | SI | 2 - Sheltered workshop, non - competitive: cannot ... |
| Q51 | varchar |  |  | SI | cannot without major assistance initiate, plan, ex... |
| Q52 | varchar |  |  | SI | understand and carry out even relatively simple sc... |
| Q53 | varchar |  |  | SI | 3 - Not employable: completely unemployable becaus... |
| Q54 | varchar |  |  | SI | plan, execute and assume any responsibilities asso... |
| Q55 | varchar |  |  | SI | Score |
| Q56 | varchar |  |  | SI | Classification |
| Q57 | varchar |  |  | SI | 0 |
| Q58 | varchar |  |  | SI | Indicates no disability |
| Q59 | varchar |  |  | SI | 29 |
| Q60 | varchar |  |  | SI | Indicates an extreme vegetative state |
| Q61 | varchar |  |  | SI | 0 - 29: A higher score indicates a more severe veg... |
| Q62 | varchar |  |  | SI | The DRS is intended to accurately measure general ... |
| Q63 | varchar |  |  | SI | 2 - Mildly dependent-Limited assistance (non-resid... |
| Q64 | varchar |  |  | SI | Eye opening |
| Q65 | varchar |  |  | SI | Communication ability |
| Q66 | varchar |  |  | SI | Motor response |
| Q67 | varchar |  |  | SI | Feeding (cognitive ability only) |
| Q68 | varchar |  |  | SI | Toileting (cognitive ability only) |
| Q69 | varchar |  |  | SI | Grooming (cognitive ability only) |
| Q70 | varchar |  |  | SI | Level of functioning (physical, mental, emotional ... |
| Q71 | varchar |  |  | SI | ''Employability'' (as a full time worker, homemake... |
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