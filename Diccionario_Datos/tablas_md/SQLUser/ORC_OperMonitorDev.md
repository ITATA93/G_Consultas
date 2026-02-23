# SQLUser.ORC_OperMonitorDev

**Schema:** SQLUser
**Columnas:** 124
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OPMON_RowId | bigint | PK |  | NO | - |
| OPMON_Code | varchar |  |  | NO | Monitor Device Code |
| OPMON_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| OPMON_CreatedDate | date |  |  | SI | Created Date |
| OPMON_CreatedTime | time |  |  | SI | Created Time |
| OPMON_CreatedUser_DR | bigint |  | FK | SI | Created User |
| OPMON_DateFrom | date |  |  | SI | Date From |
| OPMON_DateTo | date |  |  | SI | Date To |
| OPMON_Desc | varchar |  |  | NO | Mon. Device Description |
| OPMON_Owner | varchar |  |  | SI | Owner |
| OPMON_UpdatedDate | date |  |  | SI | Updated Date |
| OPMON_UpdatedTime | time |  |  | SI | Updated Time |
| OPMON_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Completed at	 |
| Q02 | - |  |  | SI | Eye opening	 |
| Q03 | - |  |  | SI | Communication ability |
| Q04 | - |  |  | SI | Motor response |
| Q05 | - |  |  | SI | Feeding (cognitive ability only) |
| Q06 | - |  |  | SI | Toileting (cognitive ability only)	 |
| Q07 | - |  |  | SI | Grooming (cognitive ability only) |
| Q08 | - |  |  | SI | Level of functioning (physical, mental, emotional ... |
| Q09 | - |  |  | SI | Employability'' (as a full time worker, homemaker ... |
| Q10 | - |  |  | SI | 0 indicates no disability |
| Q11 | - |  |  | SI | 29 indicates an extreme vegetative state |
| Q12 | - |  |  | SI | 0-Spontaneus: eyes open with sleep / wake rhythms ... |
| Q13 | - |  |  | SI | 1 - To speech and/or sensory stimulation: a respon... |
| Q14 | - |  |  | SI | not necessarily the command to open the eyes. Also... |
| Q15 | - |  |  | SI | 2 - To pain: tested by a painful stimulation |
| Q16 | - |  |  | SI | 3 - None: no eye opening even to painful stimulati... |
| Q17 | - |  |  | SI | 0 - Oriented: implies awareness of self and the en... |
| Q18 | - |  |  | SI | 1 - Confused: attention can be held and patient re... |
| Q19 | - |  |  | SI | 2 - Inappropriate: intelligible articulation but s... |
| Q20 | - |  |  | SI | 3 - Incomprehensible: moaning, groaning or sounds ... |
| Q21 | - |  |  | SI | 4 - None: no sounds or communication signs from pa... |
| Q22 | - |  |  | SI | 0 - Obeying: obeying command to move finger on bes... |
| Q23 | - |  |  | SI | 1 - Localizing: a painful stimulus at more than on... |
| Q24 | - |  |  | SI | If there is doubt as to whether withdrawal or loca... |
| Q25 | - |  |  | SI | 2 - Withdrawing: any generalized movement away fro... |
| Q26 | - |  |  | SI | 3 - Flexing: painful stimulation results in either... |
| Q27 | - |  |  | SI | If there is confusion between flexing and withdraw... |
| Q28 | - |  |  | SI | 4 - Extending: painful stimulation results in exte... |
| Q29 | - |  |  | SI | 5 - None: no response can be elicited. Usually ass... |
| Q30 | - |  |  | SI | 0 - Complete: continuously shows awareness that he... |
| Q31 | - |  |  | SI | 1 - Partial: intermittently shows awareness that h... |
| Q32 | - |  |  | SI | 2 - Minimal: shows questionable or infrequent awar... |
| Q33 | - |  |  | SI | sounds or activities that he is vaguely aware when... |
| Q34 | - |  |  | SI | 3 - None: shows virtually no awareness at any time... |
| Q35 | - |  |  | SI | 0 - Completetly independent: able to live as he wi... |
| Q36 | - |  |  | SI | 1 - Independent in special environment: capable of... |
| Q37 | - |  |  | SI | 3 - Moderately dependent-moderate assist (person i... |
| Q38 | - |  |  | SI | 4 - Markedly dependent-moderate assist (person in ... |
| Q39 | - |  |  | SI | 5 - Totally dependent - 24 hour nursing care: not ... |
| Q40 | - |  |  | SI | The psychosocial adaptability or ''employability''... |
| Q41 | - |  |  | SI | This determination should take into account consid... |
| Q42 | - |  |  | SI | 1. Able to understand, remember and follow instruc... |
| Q43 | - |  |  | SI | industrial situations or can do school assignments |
| Q44 | - |  |  | SI | using private or public transportation effectively |
| Q45 | - |  |  | SI | 7. Ability to keep track of time schedules and app... |
| Q46 | - |  |  | SI | 0 - Not restricted: can compete in the open market... |
| Q47 | - |  |  | SI | responsibilities associated with homemaking |
| Q48 | - |  |  | SI | 1 - Selected jobs, competitive: can compete in a l... |
| Q49 | - |  |  | SI | limitations |
| Q50 | - |  |  | SI | 2 - Sheltered workshop, non - competitive: cannot ... |
| Q51 | - |  |  | SI | cannot without major assistance initiate, plan, ex... |
| Q52 | - |  |  | SI | understand and carry out even relatively simple sc... |
| Q53 | - |  |  | SI | 3 - Not employable: completely unemployable becaus... |
| Q54 | - |  |  | SI | plan, execute and assume any responsibilities asso... |
| Q55 | - |  |  | SI | Score |
| Q56 | - |  |  | SI | Classification |
| Q57 | - |  |  | SI | 0 |
| Q58 | - |  |  | SI | Indicates no disability |
| Q59 | - |  |  | SI | 29 |
| Q60 | - |  |  | SI | Indicates an extreme vegetative state |
| Q61 | - |  |  | SI | 0 - 29: A higher score indicates a more severe veg... |
| Q62 | - |  |  | SI | The DRS is intended to accurately measure general ... |
| Q63 | - |  |  | SI | 2 - Mildly dependent-Limited assistance (non-resid... |
| Q64 | - |  |  | SI | Eye opening |
| Q65 | - |  |  | SI | Communication ability |
| Q66 | - |  |  | SI | Motor response |
| Q67 | - |  |  | SI | Feeding (cognitive ability only) |
| Q68 | - |  |  | SI | Toileting (cognitive ability only) |
| Q69 | - |  |  | SI | Grooming (cognitive ability only) |
| Q70 | - |  |  | SI | Level of functioning (physical, mental, emotional ... |
| Q71 | - |  |  | SI | Employability'' (as a full time worker, homemaker ... |
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

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*