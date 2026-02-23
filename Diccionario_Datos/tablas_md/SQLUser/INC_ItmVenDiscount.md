# SQLUser.INC_ItmVenDiscount

**Schema:** SQLUser
**Columnas:** 84
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Incidentes**. Reportes de eventos adversos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DISC_ParRef | varchar | PK |  | NO | INC_ItmVen Parent Reference |
| DISC_BonusStock | double |  |  | SI | Bonus Stock |
| DISC_Childsub | double |  |  | NO | Childsub |
| DISC_CreatedDate | date |  |  | SI | Created Date |
| DISC_CreatedTime | time |  |  | SI | Created Time |
| DISC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DISC_DateFrom | date |  |  | SI | Date From |
| DISC_DateTo | date |  |  | SI | Date To |
| DISC_Discount | double |  |  | SI | % Discount |
| DISC_QtyFrom | double |  |  | SI | Qty From |
| DISC_QtyTo | double |  |  | SI | Qty To |
| DISC_RowId | varchar |  |  | NO | - |
| DISC_UpdatedDate | date |  |  | SI | Updated Date |
| DISC_UpdatedTime | time |  |  | SI | Updated Time |
| DISC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Fecha realización chequeo |
| Q02 | - |  |  | SI | Hora realización chequeo |
| Q03 | - |  |  | SI | Chequeo Presencia de Brazalete de Identificación |
| Q04 | - |  |  | SI | Chequeo condición correcta de accesos venosos |
| Q05 | - |  |  | SI | Chequeo condición correcta de apósitos/vendajes |
| Q06 | - |  |  | SI | Chequeo presencia de globo vesical y/o medición de... |
| Q07 | - |  |  | SI | Chequeo documentación del caso |
| Q08 | - |  |  | SI | Chequeo condición ropa de cama del paciente |
| Q09 | - |  |  | SI | Chequeo último control de signos vitales |
| Q10 | - |  |  | SI | Chequear que el paciente egrese con todos los artí... |
| Q11 | - |  |  | SI | Observaciones al Egreso de Recuperación |
| Q12 | - |  |  | SI | Auxiliar de Enfermería responsable |
| Q13 | - |  |  | SI | Enfermera / Matrona responsable |
| Q14 | - |  |  | SI | Anestesia |
| Q15 | - |  |  | SI | Zona Operatoria |
| Q16 | - |  |  | SI | Uso medias antiembólicas |
| Q17 | - |  |  | SI | Uso Bomba Infusión |
| Q18 | - |  |  | SI | Procedencia |
| Q19 | - |  |  | SI | Responsable del traslado |
| Q20 | - |  |  | SI | Unidad de atención |
| Q21 | - |  |  | SI | Chequeo Presencia Brazalete Alergias |
| Q22 | - |  |  | SI | Comentario |
| Q23 | - |  |  | SI | Comentario |
| Q24 | - |  |  | SI | Comentario |
| Q25 | - |  |  | SI | Comentario |
| Q26 | - |  |  | SI | Comentario |
| Q27 | - |  |  | SI | Comentario |
| Q28 | - |  |  | SI | Comentario |
| Q29 | - |  |  | SI | Comentario |
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