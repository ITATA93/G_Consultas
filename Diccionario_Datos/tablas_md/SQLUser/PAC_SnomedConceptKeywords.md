# SQLUser.PAC_SnomedConceptKeywords

**Schema:** SQLUser
**Columnas:** 69
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| KEYW_ParRef | bigint | PK |  | NO | PAC_SnomedConcept Parent Reference |
| KEYW_Childsub | double |  |  | NO | Childsub |
| KEYW_Code | varchar |  |  | SI | Code |
| KEYW_Desc | varchar |  |  | SI | Description |
| KEYW_RowId | varchar |  |  | NO | - |
| KEYW_Term_DR | bigint |  | FK | SI | Des Ref Term |
| KEYW_Text | varchar |  |  | SI | Text |
| KEYW_Text1 | varchar |  |  | SI | Text1 |
| KEYW_Text2 | varchar |  |  | SI | Text2 |
| Q01 | - |  |  | SI | Please discuss the following urgent situations and... |
| Q02 | - |  |  | SI | Baby looks pale or blue in colour |
| Q03 | - |  |  | SI | Baby stops breathing |
| Q04 | - |  |  | SI | Baby is unresponsive when you try to wake them |
| Q05 | - |  |  | SI | Baby has glazed-over eyes, not focusing on anythin... |
| Q06 | - |  |  | SI | Baby has a fit or seizure |
| Q07 | - |  |  | SI | Baby has a rash that does not disappear under pres... |
| Q08 | - |  |  | SI | Baby has an abnormal temperature (below 36C or abo... |
| Q09 | - |  |  | SI | Mother has a sudden / heavy blood loss |
| Q10 | - |  |  | SI | Mother has difficulty breathing / shortness of bre... |
| Q11 | - |  |  | SI | Mother has red / swollen / tender calf or calves |
| Q12 | - |  |  | SI | Mother feels faint/has fast heartbeat |
| Q13 | - |  |  | SI | Mother has severe headaches / sudden swelling of t... |
| Q14 | - |  |  | SI | Mother has an abnormal temperature (below 35C or a... |
| Q15 | - |  |  | SI | Mother has a smelly or discoloured vaginal loss, a... |
| Q16 | - |  |  | SI | Mother experiences shivering, vomiting or confusio... |
| Q17 | - |  |  | SI | Parent(s) aware of postnatal booklet information |
| Q18 | - |  |  | SI | Additional comments |
| Q19 | - |  |  | SI | Date |
| Q20 | - |  |  | SI | Time |
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