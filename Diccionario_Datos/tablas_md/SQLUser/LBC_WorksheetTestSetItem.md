# SQLUser.LBC_WorksheetTestSetItem

**Schema:** SQLUser
**Columnas:** 90
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCWSTSI_ParRef | varchar | PK |  | NO | Parent Worsheet Definition DR  |
| LBCWSTSI_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCWSTSI_RowID | varchar |  |  | NO | - |
| LBCWSTSI_TestSetItem_DR | varchar |  | FK | SI | Reference to a test set item |
| Q01 | - |  |  | SI | Ecografía N° |
| Q02 | - |  |  | SI | Ecografía Solicitada por |
| Q03 | - |  |  | SI | FUR |
| Q04 | - |  |  | SI | Semanas |
| Q05 | - |  |  | SI | Días |
| Q06 | - |  |  | SI | Diagnóstico |
| Q07 | - |  |  | SI | Gestación |
| Q08 | - |  |  | SI | Actividad Caridíaca |
| Q09 | - |  |  | SI | Mov. Corporales |
| Q10 | - |  |  | SI | Saco Gestacional |
| Q11 | - |  |  | SI | Largo (mm) |
| Q12 | - |  |  | SI | Alto (mm) |
| Q13 | - |  |  | SI | Ancho (mm) |
| Q14 | - |  |  | SI | Saco Vitelino |
| Q15 | - |  |  | SI | Diámetro (mm) |
| Q16 | - |  |  | SI | DBP (mm) |
| Q17 | - |  |  | SI | DFO (mm) |
| Q18 | - |  |  | SI | Fémur (mm) |
| Q19 | - |  |  | SI | Húmero (mm) |
| Q20 | - |  |  | SI | LCN |
| Q21 | - |  |  | SI | Abdomen Transverso |
| Q22 | - |  |  | SI | Anteroposterior |
| Q23 | - |  |  | SI | Circunsferencia Abdominal |
| Q24 | - |  |  | SI | Calota |
| Q25 | - |  |  | SI | Columna Vertebral |
| Q26 | - |  |  | SI | Corazón |
| Q27 | - |  |  | SI | Estómago |
| Q28 | - |  |  | SI | Vejiga |
| Q29 | - |  |  | SI | Extremidades |
| Q30 | - |  |  | SI | Riñones |
| Q31 | - |  |  | SI | Traslucencia Nucal |
| Q32 | - |  |  | SI | Mide (mm) |
| Q33 | - |  |  | SI | Localización |
| Q34 | - |  |  | SI | Grado de Granumm |
| Q35 | - |  |  | SI | Relación con el OCI |
| Q36 | - |  |  | SI | Trofoblasto |
| Q37 | - |  |  | SI | Liquido Amniotico |
| Q38 | - |  |  | SI | Observaciones |
| Q38TxtOnly | - |  |  | SI | Observaciones Plain Text Only |
| Q39 | - |  |  | SI | Conclusión Ecografía |
| Q39TxtOnly | - |  |  | SI | Conclusión Ecografía Plain Text Only |
| Q40 | - |  |  | SI | Fecha de Exámen |
| Q41 | - |  |  | SI | Acompañante |
| Q41ObsDR | - |  |  | SI | Acompañante DR |
| Q42 | - |  |  | SI | Hueso Nasal |
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