# SQLUser.ORC_BloodAvailability

**Schema:** SQLUser
**Columnas:** 137
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BLOAVA_RowId | bigint | PK |  | NO | - |
| BLOAVA_Code | varchar |  |  | NO | Code |
| BLOAVA_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| BLOAVA_CreatedDate | date |  |  | SI | Created Date |
| BLOAVA_CreatedTime | time |  |  | SI | Created Time |
| BLOAVA_CreatedUser_DR | bigint |  | FK | SI | Created User |
| BLOAVA_DateFrom | date |  |  | SI | Date From |
| BLOAVA_DateTo | date |  |  | SI | Date To |
| BLOAVA_Desc | varchar |  |  | NO | Description |
| BLOAVA_Owner | varchar |  |  | SI | Owner |
| BLOAVA_UpdatedDate | date |  |  | SI | Updated Date |
| BLOAVA_UpdatedTime | time |  |  | SI | Updated Time |
| BLOAVA_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Completed at |
| Q04 | - |  |  | SI | For completion within 72 hours of admission and di... |
| Q05 | - |  |  | SI | Personal hygiene |
| Q06 | - |  |  | SI | Bathing self |
| Q07 | - |  |  | SI | Feeding |
| Q08 | - |  |  | SI | Toilet |
| Q09 | - |  |  | SI | Stair climbing |
| Q10 | - |  |  | SI | Dressing |
| Q11 | - |  |  | SI | Bowel control |
| Q12 | - |  |  | SI | Bladder control |
| Q13 | - |  |  | SI | Ambulation |
| Q14 | - |  |  | SI | Or wheelchair |
| Q15 | - |  |  | SI | *Score only if patient is unable to ambulate and i... |
| Q16 | - |  |  | SI | Chair/bed transfer |
| Q17 | - |  |  | SI | Personal hygiene |
| Q18 | - |  |  | SI | 0- patient is unable to attend personal hygiene an... |
| Q19 | - |  |  | SI | 1- assistance is required in all steps of personal... |
| Q20 | - |  |  | SI | 3- some assistance is required in one or more step... |
| Q21 | - |  |  | SI | 4- patient is able to conduct his/her personal hyg... |
| Q22 | - |  |  | SI | 5- patient can wash his/her hands and face, comb h... |
| Q23 | - |  |  | SI | Bathing self |
| Q24 | - |  |  | SI | 0- total dependence in bathing self. |
| Q25 | - |  |  | SI | 1- assistance is required in all aspects of bathin... |
| Q26 | - |  |  | SI | 3- assistance is required with either transfer to ... |
| Q27 | - |  |  | SI | 4- supervision is required for safety in adjusting... |
| Q28 | - |  |  | SI | 5- the patient may use a bath tub, a shower, or ta... |
| Q29 | - |  |  | SI | Feeding |
| Q30 | - |  |  | SI | 0- dependent in all respects and needs to be fed. |
| Q31 | - |  |  | SI | 2- can manipulate an eating device, usually a spoo... |
| Q32 | - |  |  | SI | 5- able to feed self with supervision. assistance ... |
| Q33 | - |  |  | SI | 8- independence in feeding with prepared tray, exc... |
| Q34 | - |  |  | SI | 10- the patient can feed self from a tray or table... |
| Q35 | - |  |  | SI | Toilet |
| Q36 | - |  |  | SI | 0- fully dependent in toileting |
| Q37 | - |  |  | SI | 2- assistance required in all aspects of toileting |
| Q38 | - |  |  | SI | 5- assistance may be required with management of c... |
| Q39 | - |  |  | SI | 8- supervision may be required for safety with nor... |
| Q40 | - |  |  | SI | 10- the patient is able to get on and off the toil... |
| Q41 | - |  |  | SI | Stair climbing |
| Q42 | - |  |  | SI | 0- the patient is unable to climb stairs |
| Q43 | - |  |  | SI | 2- assistance is required in all respects of stair... |
| Q44 | - |  |  | SI | 5- the patient is able to ascent/ descend but is u... |
| Q45 | - |  |  | SI | 8- generally no assistance is required. at times, ... |
| Q46 | - |  |  | SI | 10- the patient is able to go up and down a flight... |
| Q47 | - |  |  | SI | Dressing |
| Q48 | - |  |  | SI | 0- the patient is dependent in all aspects of dres... |
| Q49 | - |  |  | SI | 2- the patient is able to participate to some degr... |
| Q50 | - |  |  | SI | 5- assistance is needed in putting on and/or remov... |
| Q51 | - |  |  | SI | 8- only minimal assistance is required with fasten... |
| Q52 | - |  |  | SI | 10- the patient should be able to put on / remove ... |
| Q53 | - |  |  | SI | Bowel control |
| Q54 | - |  |  | SI | 0- The patient is incontinent. |
| Q55 | - |  |  | SI | 2- the patient needs help to assume appropriate po... |
| Q56 | - |  |  | SI | 5- the patient is generally dry by day and night, ... |
| Q57 | - |  |  | SI | 8- the patient may require supervision with the us... |
| Q58 | - |  |  | SI | 10- the patient can control bowels and has no acci... |
| Q59 | - |  |  | SI | Bladder control |
| Q60 | - |  |  | SI | 0- the patient is dependent in bladder management,... |
| Q61 | - |  |  | SI | 2- the patient is incontinent but is able to assis... |
| Q62 | - |  |  | SI | 5- the patient is generally dry by day, but not at... |
| Q63 | - |  |  | SI | 8- the patient is generally dry by day and night, ... |
| Q64 | - |  |  | SI | 10- the patient is able to control bladder day and... |
| Q65 | - |  |  | SI | Ambulation |
| Q66 | - |  |  | SI | 0- dependent on ambulation |
| Q67 | - |  |  | SI | 3- constant supervision of one or more assistants ... |
| Q68 | - |  |  | SI | 8- assistance is required with reaching aids and/o... |
| Q69 | - |  |  | SI | 12- the patient is independent in ambulation but u... |
| Q70 | - |  |  | SI | 15- the patient must be able to wear braces if req... |
| Q71 | - |  |  | SI | *Wheelchair management |
| Q72 | - |  |  | SI | 0- dependent on wheelchair ambulation |
| Q73 | - |  |  | SI | 1- patient can propel short distances on flat surf... |
| Q74 | - |  |  | SI | 3- presence of one person is necessary and constan... |
| Q75 | - |  |  | SI | 4- the patient can propel self for a reasonable du... |
| Q76 | - |  |  | SI | 5- to propel independently, the patient must be ab... |
| Q77 | - |  |  | SI | Chair/bed transfer |
| Q78 | - |  |  | SI | 0- unable to participate in a transfer. two attend... |
| Q79 | - |  |  | SI | 3-able to participate but maximum assistance of on... |
| Q80 | - |  |  | SI | 8- the transfer requires the assistance of one oth... |
| Q81 | - |  |  | SI | 12-the presence of another person is required, eit... |
| Q82 | - |  |  | SI | 15-the patient can safely approach the bed/chair i... |
| Q83 | - |  |  | SI | The modified scoring of the Barthel Index achieved... |
| Q84 | - |  |  | SI | Score |
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