# SQLUser.LBC_AntibioticRuleCondition

**Schema:** SQLUser
**Columnas:** 106
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCACI_ParRef | bigint | PK |  | NO | LBCAntibiotic Rules Setup Parent Reference |
| LBCACI_Antibiotic_DR | bigint |  | FK | SI | Antibiotic	
Antibiotic DR |
| LBCACI_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCACI_RowID | varchar |  |  | NO | - |
| LBCACI_Sensitivity_DR | bigint |  | FK | SI | Sensitivity
Sensitivity DR |
| Q01 | - |  |  | SI | Habitual Refractions |
| Q02 | - |  |  | SI | Date |
| Q03 | - |  |  | SI | Type / Brand |
| Q04 | - |  |  | SI | Right Eye |
| Q05 | - |  |  | SI | Left Eye |
| Q06 | - |  |  | SI | Both Eyes |
| Q07 | - |  |  | SI | Base curve |
| Q08 | - |  |  | SI | bc 2 |
| Q09 | - |  |  | SI | Sphere |
| Q10 | - |  |  | SI | Sph2 |
| Q11 | - |  |  | SI | Cylinder |
| Q12 | - |  |  | SI | Cyl 2 |
| Q13 | - |  |  | SI | Axis |
| Q14 | - |  |  | SI | axis 2 |
| Q15 | - |  |  | SI | Visual acuity - Distance |
| Q16 | - |  |  | SI | va-dt2 |
| Q17 | - |  |  | SI | va-dt3 |
| Q18 | - |  |  | SI | Visual acuity - Near |
| Q19 | - |  |  | SI | VA-nr2 |
| Q20 | - |  |  | SI | va-nr3 |
| Q21 | - |  |  | SI | Material |
| Q22 | - |  |  | SI | Material 2 |
| Q23 | - |  |  | SI | Diameter |
| Q24 | - |  |  | SI | dia 2 |
| Q25 | - |  |  | SI | Notes |
| Q26 | - |  |  | SI | Final Refractions |
| Q27 | - |  |  | SI | Date |
| Q28 | - |  |  | SI | Type / Brand |
| Q29 | - |  |  | SI | Right Eye |
| Q30 | - |  |  | SI | Left Eye |
| Q31 | - |  |  | SI | Both Eye |
| Q32 | - |  |  | SI | Base curve |
| Q33 | - |  |  | SI | bc2 |
| Q34 | - |  |  | SI | Sphere |
| Q35 | - |  |  | SI | Sph 2 |
| Q36 | - |  |  | SI | Cylinder |
| Q37 | - |  |  | SI | Cyl2 |
| Q38 | - |  |  | SI | Axis |
| Q39 | - |  |  | SI | Axis 2 |
| Q40 | - |  |  | SI | Add |
| Q41 | - |  |  | SI | Add 2 |
| Q42 | - |  |  | SI | Visual acuity - Distance |
| Q43 | - |  |  | SI | va-dt 2 |
| Q44 | - |  |  | SI | va-dt 3 |
| Q45 | - |  |  | SI | Visual acuity - Near |
| Q46 | - |  |  | SI | VA-Nr 2 |
| Q47 | - |  |  | SI | VA-Nr 3 |
| Q48 | - |  |  | SI | Material |
| Q49 | - |  |  | SI | Material 2 |
| Q50 | - |  |  | SI | Diameter |
| Q51 | - |  |  | SI | Dia 2 |
| Q52 | - |  |  | SI | Notes |
| Q53 | - |  |  | SI | Add |
| Q54 | - |  |  | SI | add 2 |
| Q55 | - |  |  | SI | Contact Lens Image Annotation |
| Q56 | - |  |  | SI | Interpupillary Distance (IPD) |
| Q57 | - |  |  | SI | Distance |
| Q58 | - |  |  | SI | Near |
| Q59 | - |  |  | SI | Lens type |
| Q60 | - |  |  | SI | Lens specification |
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
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*