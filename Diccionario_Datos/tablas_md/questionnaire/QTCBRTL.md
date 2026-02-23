# questionnaire.QTCBRTL

> Modified Barthel Index (Collin, 1988)

**Schema:** questionnaire
**Columnas:** 125
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Modified Barthel Index (Collin, 1988)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Completed at |
| Q04 | varchar |  |  | SI | For completion within 72 hours of admission and di... |
| Q05 | varchar |  |  | SI | Personal hygiene |
| Q06 | varchar |  |  | SI | Bathing self |
| Q07 | varchar |  |  | SI | Feeding |
| Q08 | varchar |  |  | SI | Toilet |
| Q09 | varchar |  |  | SI | Stair climbing |
| Q10 | varchar |  |  | SI | Dressing |
| Q11 | varchar |  |  | SI | Bowel control |
| Q12 | varchar |  |  | SI | Bladder control |
| Q13 | varchar |  |  | SI | Ambulation |
| Q14 | varchar |  |  | SI | Or wheelchair |
| Q15 | varchar |  |  | SI | *Score only if patient is unable to ambulate and i... |
| Q16 | varchar |  |  | SI | Chair/bed transfer |
| Q17 | varchar |  |  | SI | Personal hygiene |
| Q18 | varchar |  |  | SI | 0- patient is unable to attend personal hygiene an... |
| Q19 | varchar |  |  | SI | 1- assistance is required in all steps of personal... |
| Q20 | varchar |  |  | SI | 3- some assistance is required in one or more step... |
| Q21 | varchar |  |  | SI | 4- patient is able to conduct his/her personal hyg... |
| Q22 | varchar |  |  | SI | 5- patient can wash his/her hands and face, comb h... |
| Q23 | varchar |  |  | SI | Bathing self |
| Q24 | varchar |  |  | SI | 0- total dependence in bathing self. |
| Q25 | varchar |  |  | SI | 1- assistance is required in all aspects of bathin... |
| Q26 | varchar |  |  | SI | 3- assistance is required with either transfer to ... |
| Q27 | varchar |  |  | SI | 4- supervision is required for safety in adjusting... |
| Q28 | varchar |  |  | SI | 5- the patient may use a bath tub, a shower, or ta... |
| Q29 | varchar |  |  | SI | Feeding |
| Q30 | varchar |  |  | SI | 0- dependent in all respects and needs to be fed. |
| Q31 | varchar |  |  | SI | 2- can manipulate an eating device, usually a spoo... |
| Q32 | varchar |  |  | SI | 5- able to feed self with supervision. assistance ... |
| Q33 | varchar |  |  | SI | 8- independence in feeding with prepared tray, exc... |
| Q34 | varchar |  |  | SI | 10- the patient can feed self from a tray or table... |
| Q35 | varchar |  |  | SI | Toilet |
| Q36 | varchar |  |  | SI | 0- fully dependent in toileting |
| Q37 | varchar |  |  | SI | 2- assistance required in all aspects of toileting |
| Q38 | varchar |  |  | SI | 5- assistance may be required with management of c... |
| Q39 | varchar |  |  | SI | 8- supervision may be required for safety with nor... |
| Q40 | varchar |  |  | SI | 10- the patient is able to get on and off the toil... |
| Q41 | varchar |  |  | SI | Stair climbing |
| Q42 | varchar |  |  | SI | 0- the patient is unable to climb stairs |
| Q43 | varchar |  |  | SI | 2- assistance is required in all respects of stair... |
| Q44 | varchar |  |  | SI | 5- the patient is able to ascent/ descend but is u... |
| Q45 | varchar |  |  | SI | 8- generally no assistance is required. at times, ... |
| Q46 | varchar |  |  | SI | 10- the patient is able to go up and down a flight... |
| Q47 | varchar |  |  | SI | Dressing |
| Q48 | varchar |  |  | SI | 0- the patient is dependent in all aspects of dres... |
| Q49 | varchar |  |  | SI | 2- the patient is able to participate to some degr... |
| Q50 | varchar |  |  | SI | 5- assistance is needed in putting on and/or remov... |
| Q51 | varchar |  |  | SI | 8- only minimal assistance is required with fasten... |
| Q52 | varchar |  |  | SI | 10- the patient should be able to put on / remove ... |
| Q53 | varchar |  |  | SI | Bowel control |
| Q54 | varchar |  |  | SI | 0- The patient is incontinent.  |
| Q55 | varchar |  |  | SI | 2- the patient needs help to assume appropriate po... |
| Q56 | varchar |  |  | SI | 5- the patient is generally dry by day and night, ... |
| Q57 | varchar |  |  | SI | 8- the patient may require supervision with the us... |
| Q58 | varchar |  |  | SI | 10- the patient can control bowels and has no acci... |
| Q59 | varchar |  |  | SI | Bladder control |
| Q60 | varchar |  |  | SI | 0- the patient is dependent in bladder management,... |
| Q61 | varchar |  |  | SI | 2- the patient is incontinent but is able to assis... |
| Q62 | varchar |  |  | SI | 5- the patient is generally dry by day, but not at... |
| Q63 | varchar |  |  | SI | 8- the patient is generally dry by day and night, ... |
| Q64 | varchar |  |  | SI | 10- the patient is able to control bladder day and... |
| Q65 | varchar |  |  | SI | Ambulation |
| Q66 | varchar |  |  | SI | 0- dependent on ambulation |
| Q67 | varchar |  |  | SI | 3- constant supervision of one or more assistants ... |
| Q68 | varchar |  |  | SI | 8- assistance is required with reaching aids and/o... |
| Q69 | varchar |  |  | SI | 12- the patient is independent in ambulation but u... |
| Q70 | varchar |  |  | SI | 15- the patient must be able to wear braces if req... |
| Q71 | varchar |  |  | SI | *Wheelchair management |
| Q72 | varchar |  |  | SI | 0- dependent on wheelchair ambulation |
| Q73 | varchar |  |  | SI | 1- patient can propel short distances on flat surf... |
| Q74 | varchar |  |  | SI | 3- presence of one person is necessary and constan... |
| Q75 | varchar |  |  | SI | 4- the patient can propel self for a reasonable du... |
| Q76 | varchar |  |  | SI | 5- to propel independently, the patient must be ab... |
| Q77 | varchar |  |  | SI | Chair/bed transfer |
| Q78 | varchar |  |  | SI | 0- unable to participate in a transfer. two attend... |
| Q79 | varchar |  |  | SI | 3-able to participate but maximum assistance of on... |
| Q80 | varchar |  |  | SI | 8- the transfer requires the assistance of one oth... |
| Q81 | varchar |  |  | SI | 12-the presence of another person is required, eit... |
| Q82 | varchar |  |  | SI | 15-the patient can safely approach the bed/chair i... |
| Q83 | varchar |  |  | SI | The modified scoring of the Barthel Index achieved... |
| Q84 | varchar |  |  | SI | Score |
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