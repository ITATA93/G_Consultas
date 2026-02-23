# questionnaire.QGXXXOPH26

> Posterior Segment

**Schema:** questionnaire
**Columnas:** 117
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Posterior Segment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Informed consent collected |
| Q02 | date |  |  | SI | Date |
| Q03 | time |  |  | SI | Time |
| Q04 | varchar |  |  | SI | Dilated |
| Q05 | varchar |  |  | SI | Vitreous |
| Q06 | varchar |  |  | SI | Clear |
| Q07 | varchar |  |  | SI | Notes |
| Q08 | varchar |  |  | SI | Optic Nerve |
| Q09 | varchar |  |  | SI | Right Eye |
| Q10 | varchar |  |  | SI | Left Eye |
| Q11 | varchar |  |  | SI | Disc size |
| Q12 | varchar |  |  | SI | Disc size 2 |
| Q13 | varchar |  |  | SI | C/D ratio - Hz |
| Q14 | varchar |  |  | SI | CD ration Hz 2 |
| Q15 | varchar |  |  | SI | C/D ratio - Vt |
| Q16 | varchar |  |  | SI | CD ratio Vt 2 |
| Q17 | varchar |  |  | SI | Apperance |
| Q18 | varchar |  |  | SI | Appearance 2 |
| Q19 | varchar |  |  | SI | Nerve fiber layer |
| Q20 | varchar |  |  | SI | Nerve fiber layer 2 |
| Q21 | varchar |  |  | SI | Neural rim |
| Q22 | varchar |  |  | SI | Neural rim 2 |
| Q23 | varchar |  |  | SI | Margin |
| Q24 | varchar |  |  | SI | Margin 2 |
| Q25 | varchar |  |  | SI | Neurovasularization |
| Q26 | varchar |  |  | SI | Neurovascularization 2 |
| Q27 | varchar |  |  | SI | Notes  |
| Q28 | varchar |  |  | SI | Retina |
| Q29 | varchar |  |  | SI | Dilated macular / Fundus exam |
| Q30 | varchar |  |  | SI | Right Eye |
| Q31 | varchar |  |  | SI | Left Eye |
| Q32 | varchar |  |  | SI | Foveal reflex  |
| Q33 | varchar |  |  | SI | Foveal Reflex  2 |
| Q34 | varchar |  |  | SI | Macual |
| Q35 | varchar |  |  | SI | Manual 2 |
| Q36 | varchar |  |  | SI | Macula oedema |
| Q37 | varchar |  |  | SI | Macual oedema 2 |
| Q38 | varchar |  |  | SI | Posterior pole |
| Q39 | varchar |  |  | SI | Posterior Pole 2 |
| Q40 | varchar |  |  | SI | Vessels |
| Q41 | varchar |  |  | SI | Vessels |
| Q42 | varchar |  |  | SI | NVE |
| Q43 | varchar |  |  | SI | NVE 2 |
| Q44 | varchar |  |  | SI | Periphery |
| Q45 | varchar |  |  | SI | periphery 2 |
| Q46 | varchar |  |  | SI | Notes |
| Q47 | varchar |  |  | SI | Image |
| Q48 | varchar |  |  | SI | Image Annotation |
| Q49 | varchar |  |  | SI | Clear 2 |
| Q50 | varchar |  |  | SI | Right Eye |
| Q51 | varchar |  |  | SI | Left Eye |
| Q52 | varchar |  |  | SI | Clear |
| Q53 | varchar |  |  | SI | Disc size |
| Q54 | varchar |  |  | SI | C/D ratio - Hz |
| Q55 | varchar |  |  | SI | C/D ratio - Vt |
| Q56 | varchar |  |  | SI | Apperance |
| Q57 | varchar |  |  | SI | Nerve fiber layer |
| Q58 | varchar |  |  | SI | Neural rim |
| Q59 | varchar |  |  | SI | Margin |
| Q60 | varchar |  |  | SI | Neurovasularization |
| Q61 | varchar |  |  | SI | Foveal reflex |
| Q62 | varchar |  |  | SI | Macual |
| Q63 | varchar |  |  | SI | Macula oedema |
| Q64 | varchar |  |  | SI | Posterior pole |
| Q65 | varchar |  |  | SI | Vessels |
| Q66 | varchar |  |  | SI | NVE |
| Q67 | varchar |  |  | SI | Periphery |
| Q68 | date |  |  | SI | Date |
| Q69 | time |  |  | SI | Time |
| Q70 | varchar |  |  | SI | Dilated |
| Q71 | varchar |  |  | SI | Clear |
| Q72 | varchar |  |  | SI | Disc size |
| Q73 | varchar |  |  | SI | Disc size 2 |
| Q74 | varchar |  |  | SI | Dilated macular / Fundus exam |
| Q75 | varchar |  |  | SI | Foveal reflex |
| Q76 | varchar |  |  | SI | Foveal reflex 2 |
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