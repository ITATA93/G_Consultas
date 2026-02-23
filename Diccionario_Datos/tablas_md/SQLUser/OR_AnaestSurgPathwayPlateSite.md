# SQLUser.OR_AnaestSurgPathwayPlateSite

**Schema:** SQLUser
**Columnas:** 69
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Pabellón Quirúrgico**. Gestión de cirugías.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PLATESITE_ParRef | varchar | PK |  | NO | OR_AnaestSurgPathway Parent Reference |
| PLATESITE_AppliedBy_DR | varchar |  | FK | SI |  Des Ref CT_CareProv |
| PLATESITE_BodySite_DR | bigint |  | FK | SI |  Des Ref OEC_BodySite |
| PLATESITE_Childsub | numeric |  |  | NO | Childsub |
| PLATESITE_Comments | varchar |  |  | SI | Comments |
| PLATESITE_DiathMethod_DR | bigint |  | FK | SI |  Des Ref ORCDiathermyMethod  |
| PLATESITE_PlateSiteIntact | varchar |  |  | SI | PlateSiteIntact |
| PLATESITE_RemovedBy_DR | varchar |  | FK | SI |  Des Ref CT_CareProv |
| PLATESITE_RowId | varchar |  |  | NO | - |
| Q01 | - |  |  | SI | ¿Está usted cansado? |
| Q02 | - |  |  | SI | ¿Es incapaz de subir un piso de escaleras? |
| Q03 | - |  |  | SI | ¿Es incapaz de caminar una manzana? |
| Q04 | - |  |  | SI | ¿Tienes más de cinco enfermedades? |
| Q05 | - |  |  | SI | * hipertensión, diabetes, cáncer, enfermedad pulmo... |
| Q06 | - |  |  | SI | ¿Ha perdido más del 5% de su peso en los últimos m... |
| Q07 | - |  |  | SI | Puntaje |
| Q08 | - |  |  | SI | Clasificación |
| Q09 | - |  |  | SI | 0 |
| Q10 | - |  |  | SI | Robusto(a) |
| Q11 | - |  |  | SI | 1 - 2 |
| Q12 | - |  |  | SI | Pre-Frágil |
| Q13 | - |  |  | SI | 3 - 5 |
| Q14 | - |  |  | SI | Frágil |
| Q15 | - |  |  | SI | 0: Robusto(a) |
| Q16 | - |  |  | SI | 1 - 2: Pre-Frágil |
| Q17 | - |  |  | SI | 3 - 5: Frágil |
| Q18 | - |  |  | SI | La escala FRAIL (Fatiga, Resistencia, Deambulación... |
| Q19 | - |  |  | SI | Fecha |
| Q20 | - |  |  | SI | Hora |
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