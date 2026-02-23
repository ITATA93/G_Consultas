# SQLUser.CT_RefClinKeywords

**Schema:** SQLUser
**Columnas:** 101
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| KEYW_ParRef | bigint | PK |  | NO | CT_RefClin Parent Reference |
| KEYW_Childsub | double |  |  | NO | Childsub |
| KEYW_RowId | varchar |  |  | NO | - |
| KEYW_Text | varchar |  |  | SI | Text |
| Q01 | - |  |  | SI | Skin |
| Q01ObsDR | - |  |  | SI | Skin DR |
| Q02 | - |  |  | SI | Eyes |
| Q02ObsDR | - |  |  | SI | Eyes DR |
| Q03 | - |  |  | SI | Mouth |
| Q03ObsDR | - |  |  | SI | Mouth DR |
| Q04 | - |  |  | SI | Head |
| Q04ObsDR | - |  |  | SI | Head DR |
| Q05 | - |  |  | SI | Cord |
| Q05ObsDR | - |  |  | SI | Cord DR |
| Q06 | - |  |  | SI | Stools |
| Q06ObsDR | - |  |  | SI | Stools DR |
| Q07 | - |  |  | SI | Meconium within first 24Hrs |
| Q07ObsDR | - |  |  | SI | Meconium within first 24Hrs DR |
| Q08 | - |  |  | SI | Hypoglycaemia |
| Q08ObsDR | - |  |  | SI | Hypoglycaemia DR |
| Q09 | - |  |  | SI | NAS |
| Q09ObsDR | - |  |  | SI | NAS DR |
| Q10 | - |  |  | SI | Hearing screen offered |
| Q10ObsDR | - |  |  | SI | Hearing screen offered DR |
| Q11 | - |  |  | SI | Hearing screen accepted |
| Q11ObsDR | - |  |  | SI | Hearing screen accepted DR |
| Q12 | - |  |  | SI | NAS severity |
| Q12ObsDR | - |  |  | SI | NAS severity DR |
| Q13 | - |  |  | SI | Phototherapy required |
| Q13ObsDR | - |  |  | SI | Phototherapy required DR |
| Q14 | - |  |  | SI | Newborn blood spot screening |
| Q14ObsDR | - |  |  | SI | Newborn blood spot screening DR |
| Q15 | - |  |  | SI | Namebands X2 |
| Q16 | - |  |  | SI | Weight (grams) |
| Q16ObsDR | - |  |  | SI | Weight (grams) DR |
| Q18 | - |  |  | SI | Blood glucose |
| Q18ObsDR | - |  |  | SI | Blood glucose DR |
| Q19 | - |  |  | SI | No of wet nappies in 24Hrs |
| Q19ObsDR | - |  |  | SI | No of wet nappies in 24Hrs DR |
| Q20 | - |  |  | SI | No of dirty nappies in 24Hrs |
| Q20ObsDR | - |  |  | SI | No of dirty nappies in 24Hrs DR |
| Q21 | - |  |  | SI | Date hearing screen performed |
| Q22 | - |  |  | SI | Date hearing screen due |
| Q23 | - |  |  | SI | Comments |
| Q24 | - |  |  | SI | Feeding |
| Q25 | - |  |  | SI | Temperature |
| Q25ObsDR | - |  |  | SI | Temperature DR |
| Q27 | - |  |  | SI | Bilirubin level |
| Q27ObsDR | - |  |  | SI | Bilirubin level DR |
| Q28 | - |  |  | SI | Date blood spot screening done |
| Q29 | - |  |  | SI | Date blood spot screening due |
| Q30 | - |  |  | SI | Drugs given |
| Q31 | - |  |  | SI | Date phototherapy completed |
| Q32 | - |  |  | SI | Midwife countersigning |
| Q33 | - |  |  | SI | Type of feeding |
| Q33ObsDR | - |  |  | SI | Type of feeding DR |
| Q34 | - |  |  | SI | Date phototherapy started |
| Q35 | - |  |  | SI | Time phototherapy started |
| Q36 | - |  |  | SI | Time phototherapy completed |
| Q37 | - |  |  | SI | Time |
| Q38 | - |  |  | SI | Time |
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