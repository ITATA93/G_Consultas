# questionnaire.QTCEECOOBST

**Schema:** questionnaire
**Columnas:** 86
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| QANATOM | varchar | PK |  | SI | Anatomia |
| QANATOM8 | varchar | PK |  | SI | Anatomía |
| QATRIO | varchar | PK |  | SI | Atrio |
| QCA | varchar | PK |  | SI | CA |
| QCALCULAR | varchar | PK |  | SI | Calcular |
| QCC | varchar | PK |  | SI | CC |
| QCEREBELO | varchar | PK |  | SI | Cerebelo |
| QCERVIX | varchar | PK |  | SI | Cervix |
| QCISTMAGNA | varchar | PK |  | SI | Cisterna Magna |
| QCONCLU | varchar | PK |  | SI | Conclusion |
| QCONCLUSION | varchar | PK |  | SI | Conclusion |
| QDBP | varchar | PK |  | SI | DBP |
| QDETER | varchar | PK |  | SI | Peso Estimado Deter |
| QDFO | varchar | PK |  | SI | DFO |
| QEGEST | varchar | PK |  | SI | Edad Gestacional |
| QEGESTDBP | varchar | PK |  | SI | Edad Gestacional (DBP) |
| QEGESTFEM | varchar | PK |  | SI | Edad Gestacional (FEM) |
| QEGESTREAL | varchar | PK |  | SI | Edad Gestacional Real |
| QFC | varchar | PK |  | SI | Frecuencia Cardíaca |
| QFECHAEXAMEN | date | PK |  | SI | Fecha de Examen |
| QFEM | varchar | PK |  | SI | FEM |
| QFUR | date | PK |  | SI | Fecha Ultima Regla |
| QGr | varchar | PK |  | SI | Grado |
| QHADLOCK | varchar | PK |  | SI | Peso Estimado Hadlock |
| QHN | varchar | PK |  | SI | Hueso Nasal |
| QHUESONASAL | varchar | PK |  | SI | Hueso Nasal |
| QINS | varchar | PK |  | SI | Inserción |
| QLA1 | varchar | PK |  | SI | LA 1 |
| QLA2 | varchar | PK |  | SI | LA 2 |
| QLA3 | varchar | PK |  | SI | LA 3 |
| QLA4 | varchar | PK |  | SI | LA 4 |
| QLAMNIOTICO | varchar | PK |  | SI | Liquido Amniotico |
| QLOC | varchar | PK |  | SI | Localización |
| QMC | varchar | PK |  | SI | Movimientos Corporales |
| QMR | varchar | PK |  | SI | Movimientos respiratorios |
| QOb2 | varchar | PK |  | SI | Observaciones |
| QPBF | varchar | PK |  | SI | PBF |
| QPBF1 | varchar | PK |  | SI | Perfil Biofísico |
| QPD | varchar | PK |  | SI | Podálica |
| QPLACENT | varchar | PK |  | SI | Placenta |
| QPRESENT | varchar | PK |  | SI | Presenacion |
| QPr2 | varchar | PK |  | SI | Presentación |
| QSHEPARD | varchar | PK |  | SI | Peso Estimado Shepard |
| QTALLA | varchar | PK |  | SI | Talla |
| QTF | varchar | PK |  | SI | Tono Fetal |
| QTOTALLA | varchar | PK |  | SI | Total LA |
| QTPBF | varchar | PK |  | SI | Total (PBF) |
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
| QVA | varchar | PK |  | SI | Volumen Amniótico |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*