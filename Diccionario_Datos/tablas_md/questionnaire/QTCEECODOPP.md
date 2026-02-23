# questionnaire.QTCEECODOPP

> Doppler Obstétrico

**Schema:** questionnaire
**Columnas:** 114
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Doppler Obstétrico

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q64 | varchar |  |  | SI | Arteria Umbilical |
| Q65 | varchar |  |  | SI | Arteria Cerebral Media |
| Q66 | varchar |  |  | SI | Arteria Uterina Derecha |
| Q67 | varchar |  |  | SI | Arteria Uterina Izquierda |
| Q68 | varchar |  |  | SI | Ductus |
| Q69 | varchar |  |  | SI | Máximo |
| Q70 | varchar |  |  | SI | Mínimo |
| Q71 | varchar |  |  | SI | Media |
| Q72 | varchar |  |  | SI | T/2 |
| Q73 | varchar |  |  | SI | IP |
| QANATOM | varchar |  |  | SI | Anatomia |
| QATRIO | varchar |  |  | SI | Atrio |
| QCA | varchar |  |  | SI | Circunferencia Abdominal |
| QCC | varchar |  |  | SI | Circunferencia Craneana |
| QCERVIX | varchar |  |  | SI | Cervix |
| QCISTMAGNA | varchar |  |  | SI | Cisterna Magna |
| QCONCLU | varchar |  |  | SI | Conclusion |
| QDBP | varchar |  |  | SI | Diámetro Biparietal |
| QDETER | varchar |  |  | SI | Peso Estimado Deter |
| QDFO | varchar |  |  | SI | Diametro Fronto-Occipital |
| QEGEST | varchar |  |  | SI | Edad Gestacional |
| QEGESTDBP | varchar |  |  | SI | Edad Gestacional (DBP) |
| QEGESTFEM | varchar |  |  | SI | Edad Gestacional (FEM) |
| QEGESTREAL | varchar |  |  | SI | Edad Gestacional Real |
| QFECHAEXAMEN | date |  |  | SI | Fecha de Examen |
| QFEM | varchar |  |  | SI | Longitud Femur |
| QFUR | date |  |  | SI | Fecha Ultima Regla |
| QGr | varchar |  |  | SI | Grado |
| QHADLOCK | varchar |  |  | SI | Peso Estimado Hadlock |
| QHUESONASAL | varchar |  |  | SI | Hueso Nasal |
| QINDICECP | varchar |  |  | SI | IndiceCP |
| QINDICEDUCTUS | varchar |  |  | SI | Indice Ductus |
| QINS | varchar |  |  | SI | Inserción |
| QIPACM | varchar |  |  | SI | IPACM |
| QIPDER | varchar |  |  | SI | IPDER |
| QIPDUC | varchar |  |  | SI | IPDUC |
| QIPIZQ | varchar |  |  | SI | IPIZQ |
| QIPPROM | varchar |  |  | SI | IP Promedio |
| QIPUMB | varchar |  |  | SI | IPUMB |
| QLA1 | varchar |  |  | SI | LA 1 |
| QLA2 | varchar |  |  | SI | LA 2 |
| QLA3 | varchar |  |  | SI | LA 3 |
| QLA4 | varchar |  |  | SI | LA 4 |
| QLAMNIOTICO | varchar |  |  | SI | Liquido Amniotico |
| QLOC | varchar |  |  | SI | Localización |
| QMAXACM | varchar |  |  | SI | Max ACM |
| QMAXDER | varchar |  |  | SI | Max Derecha |
| QMAXDUC | varchar |  |  | SI | Max Ductus |
| QMAXIZQ | varchar |  |  | SI | Max Izquierda |
| QMAXUMB | varchar |  |  | SI | Max Umbilical |
| QMEDIAACM | varchar |  |  | SI | Media ACM |
| QMEDIADER | varchar |  |  | SI | Media derecha |
| QMEDIADUC | varchar |  |  | SI | Media ductus |
| QMEDIAIZQ | varchar |  |  | SI | Media Izquierda |
| QMEDIAUMB | varchar |  |  | SI | Media Umbilical |
| QMINACM | varchar |  |  | SI | Min ACM |
| QMINDER | varchar |  |  | SI | Min Derecha |
| QMINDUC | varchar |  |  | SI | Min Ductus |
| QMINIZQ | varchar |  |  | SI | Min Izquierda |
| QMINUMB | varchar |  |  | SI | Min Umbilical |
| QObs | varchar |  |  | SI | Observaciones |
| QPBF | varchar |  |  | SI | Perfil Biofisico |
| QPLACENT | varchar |  |  | SI | Placenta |
| QPRESENT | varchar |  |  | SI | Presentacion |
| QSDACM | varchar |  |  | SI | SDACM |
| QSDDER | varchar |  |  | SI | SDDER |
| QSDDUC | varchar |  |  | SI | SDDUC |
| QSDIZQ | varchar |  |  | SI | SDIZQ |
| QSDUMB | varchar |  |  | SI | SD |
| QSHEPARD | varchar |  |  | SI | Peso Estimado Shepard |
| QT2 | varchar |  |  | SI | T2 |
| QTALLA | varchar |  |  | SI | Talla |
| QTOTALLA | varchar |  |  | SI | Total LA |
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