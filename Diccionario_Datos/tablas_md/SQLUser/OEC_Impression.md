# SQLUser.OEC_Impression

**Schema:** SQLUser
**Columnas:** 127
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Entry Orders**. Tipos y estados de órdenes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| IMPR_RowId | bigint | PK |  | NO | - |
| IMPR_Code | varchar |  |  | NO | Code |
| IMPR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| IMPR_CreatedDate | date |  |  | SI | Created Date |
| IMPR_CreatedTime | time |  |  | SI | Created Time |
| IMPR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| IMPR_Desc | varchar |  |  | NO | Description |
| IMPR_Owner | varchar |  |  | SI | Owner |
| IMPR_UpdatedDate | date |  |  | SI | Updated Date |
| IMPR_UpdatedTime | time |  |  | SI | Updated Time |
| IMPR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Informed consent collected |
| Q02 | - |  |  | SI | Date |
| Q03 | - |  |  | SI | Time |
| Q04 | - |  |  | SI | Dilated |
| Q05 | - |  |  | SI | Vitreous |
| Q06 | - |  |  | SI | Clear |
| Q07 | - |  |  | SI | Notes |
| Q08 | - |  |  | SI | Optic Nerve |
| Q09 | - |  |  | SI | Right Eye |
| Q10 | - |  |  | SI | Left Eye |
| Q11 | - |  |  | SI | Disc size |
| Q12 | - |  |  | SI | Disc size 2 |
| Q13 | - |  |  | SI | C/D ratio - Hz |
| Q14 | - |  |  | SI | CD ration Hz 2 |
| Q15 | - |  |  | SI | C/D ratio - Vt |
| Q16 | - |  |  | SI | CD ratio Vt 2 |
| Q17 | - |  |  | SI | Apperance |
| Q18 | - |  |  | SI | Appearance 2 |
| Q19 | - |  |  | SI | Nerve fiber layer |
| Q20 | - |  |  | SI | Nerve fiber layer 2 |
| Q21 | - |  |  | SI | Neural rim |
| Q22 | - |  |  | SI | Neural rim 2 |
| Q23 | - |  |  | SI | Margin |
| Q24 | - |  |  | SI | Margin 2 |
| Q25 | - |  |  | SI | Neurovasularization |
| Q26 | - |  |  | SI | Neurovascularization 2 |
| Q27 | - |  |  | SI | Notes |
| Q28 | - |  |  | SI | Retina |
| Q29 | - |  |  | SI | Dilated macular / Fundus exam |
| Q30 | - |  |  | SI | Right Eye |
| Q31 | - |  |  | SI | Left Eye |
| Q32 | - |  |  | SI | Foveal reflex |
| Q33 | - |  |  | SI | Foveal Reflex  2 |
| Q34 | - |  |  | SI | Macual |
| Q35 | - |  |  | SI | Manual 2 |
| Q36 | - |  |  | SI | Macula oedema |
| Q37 | - |  |  | SI | Macual oedema 2 |
| Q38 | - |  |  | SI | Posterior pole |
| Q39 | - |  |  | SI | Posterior Pole 2 |
| Q40 | - |  |  | SI | Vessels |
| Q41 | - |  |  | SI | Vessels |
| Q42 | - |  |  | SI | NVE |
| Q43 | - |  |  | SI | NVE 2 |
| Q44 | - |  |  | SI | Periphery |
| Q45 | - |  |  | SI | periphery 2 |
| Q46 | - |  |  | SI | Notes |
| Q47 | - |  |  | SI | Image |
| Q48 | - |  |  | SI | Image Annotation |
| Q49 | - |  |  | SI | Clear 2 |
| Q50 | - |  |  | SI | Right Eye |
| Q51 | - |  |  | SI | Left Eye |
| Q52 | - |  |  | SI | Clear |
| Q53 | - |  |  | SI | Disc size |
| Q54 | - |  |  | SI | C/D ratio - Hz |
| Q55 | - |  |  | SI | C/D ratio - Vt |
| Q56 | - |  |  | SI | Apperance |
| Q57 | - |  |  | SI | Nerve fiber layer |
| Q58 | - |  |  | SI | Neural rim |
| Q59 | - |  |  | SI | Margin |
| Q60 | - |  |  | SI | Neurovasularization |
| Q61 | - |  |  | SI | Foveal reflex |
| Q62 | - |  |  | SI | Macual |
| Q63 | - |  |  | SI | Macula oedema |
| Q64 | - |  |  | SI | Posterior pole |
| Q65 | - |  |  | SI | Vessels |
| Q66 | - |  |  | SI | NVE |
| Q67 | - |  |  | SI | Periphery |
| Q68 | - |  |  | SI | Date |
| Q69 | - |  |  | SI | Time |
| Q70 | - |  |  | SI | Dilated |
| Q71 | - |  |  | SI | Clear |
| Q72 | - |  |  | SI | Disc size |
| Q73 | - |  |  | SI | Disc size 2 |
| Q74 | - |  |  | SI | Dilated macular / Fundus exam |
| Q75 | - |  |  | SI | Foveal reflex |
| Q76 | - |  |  | SI | Foveal reflex 2 |
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