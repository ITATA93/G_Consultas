# questionnaire.QTCEECO1114

**Schema:** questionnaire
**Columnas:** 67
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q28 | varchar | PK |  | SI | Fecha Última Regla |
| Q29 | varchar | PK |  | SI | Edad Gestacional (FUR) |
| QANATOMGRU | varchar | PK |  | SI | Anatomia Gruesa |
| QANEXOS | varchar | PK |  | SI | Anexos |
| QCERVIX | varchar | PK |  | SI | Cervix |
| QCONCLUSION | varchar | PK |  | SI | Conclusion |
| QDBP | varchar | PK |  | SI | Diámetro Biparietal |
| QDOPUTED | bit | PK |  | SI | Doppler de uterinas promedio  |
| QDUCTUS | varchar | PK |  | SI | Ductus |
| QEGESTDBP | varchar | PK |  | SI | Edad Gestacional (DBP) |
| QEGESTFEM | varchar | PK |  | SI | Edad Gestacional (FEM) |
| QEGESTFUR | varchar | PK |  | SI | Edad Gestacional (FUR) |
| QEGESTLCN | varchar | PK |  | SI | Edad Gestacional (LCN) |
| QEGESTREAL | varchar | PK |  | SI | Edad gestacional Real |
| QFECHAEXAMEN | date | PK |  | SI | Fecha Examen |
| QFEM | varchar | PK |  | SI | Longitud Femur |
| QFUR | date | PK |  | SI | Fecha de Ultima Regla |
| QGR | varchar | PK |  | SI | Grado |
| QHN | varchar | PK |  | SI | Hueso Nasal |
| QHUESONAS | varchar | PK |  | SI | Hueso Nasal |
| QINS | varchar | PK |  | SI | Inserción |
| QLCF | varchar | PK |  | SI | LCF |
| QLCN | varchar | PK |  | SI | Longitud Cefalo-Nalgas |
| QLOC | varchar | PK |  | SI | Localización |
| QLOVULAR | varchar | PK |  | SI | Lovular |
| QLPM | varchar | PK |  | SI | LPM |
| QTRANSRETRO | varchar | PK |  | SI | Translucencia Retronucal |
| QTROFOPLA | varchar | PK |  | SI | Trofoblasto o placenta |
| QUESAnaDR | varchar | PK | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar | PK | FK | SI | Operation |
| QUESConsultDR | varchar | PK | FK | SI | Consult |
| QUESCopiedComments | varchar | PK |  | SI | Copied Comments |
| QUESCopiedDate | date | PK |  | SI | Copied Date |
| QUESCopiedEpDR | bigint | PK | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint | PK | FK | SI | Copied Source DR |
| QUESCopiedTime | time | PK |  | SI | Copied Time |
| QUESCopiedUserDR | bigint | PK | FK | SI | Copied User |
| QUESCreateDate | date | PK |  | SI | Creation Date |
| QUESCreateTime | time | PK |  | SI | Creation Time |
| QUESCreateUserDR | bigint | PK | FK | SI | Creation User |
| QUESDate | date | PK |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint | PK | FK | SI | Error Reason |
| QUESFHResidentDR | bigint | PK | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar | PK | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar | PK | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar | PK | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint | PK | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar | PK | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint | PK | FK | SI | Operating Room |
| QUESPAAdmDR | bigint | PK | FK | SI | Admission |
| QUESPAPatMasDR | bigint | PK | FK | SI | Patient |
| QUESPAPregnancyDR | bigint | PK | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint | PK | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar | PK | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar | PK | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar | PK | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar | PK | FK | SI | Appointment Outcome |
| QUESReasonForCorrectionDR | bigint | PK | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint | PK | FK | SI | Questionnaire |
| QUESScore | varchar | PK |  | SI | Score |
| QUESStatusDR | bigint | PK | FK | SI | Status |
| QUESTextResultDR | bigint | PK | FK | SI | Text Result |
| QUESTime | time | PK |  | SI | Last Update Time |
| QUESTransactionDR | varchar | PK | FK | SI | Transaction |
| QUESUserDR | bigint | PK | FK | SI | Last Update User |
| Qobs | varchar | PK |  | SI | Observaciones |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*