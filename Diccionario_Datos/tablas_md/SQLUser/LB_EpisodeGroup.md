# SQLUser.LB_EpisodeGroup

**Schema:** SQLUser
**Columnas:** 125
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBEPG_RowID | bigint | PK |  | NO | - |
| LBEPG_CollectionDate | date |  |  | SI | Collection Date of the episode group |
| LBEPG_CollectionTime | time |  |  | SI | Collection Time of the episode group |
| LBEPG_Facility_DR | bigint |  | FK | SI | Facility |
| LBEPG_Number | varchar |  |  | NO | Lab Episode Group Number  |
| LBEPG_ReceivedDate | date |  |  | SI | Received Date |
| LBEPG_ReceivedTime | time |  |  | SI | Received Time |
| LBEPG_ReferringDoctor_DR | bigint |  | FK | SI | Referring Doctor |
| LBEPG_RequestingLocation_DR | bigint |  | FK | SI | Subject Requesting Location |
| LBEPG_SecondaryReferringDoctor_DR | bigint |  | FK | SI | Secondary Referring Doctor (used Environmental) |
| LBEPG_SpeciesBreed_DR | varchar |  | FK | SI | Breed |
| LBEPG_Species_DR | bigint |  | FK | SI | Species |
| Q64 | - |  |  | SI | Arteria Umbilical |
| Q65 | - |  |  | SI | Arteria Cerebral Media |
| Q66 | - |  |  | SI | Arteria Uterina Derecha |
| Q67 | - |  |  | SI | Arteria Uterina Izquierda |
| Q68 | - |  |  | SI | Ductus |
| Q69 | - |  |  | SI | Máximo |
| Q70 | - |  |  | SI | Mínimo |
| Q71 | - |  |  | SI | Media |
| Q72 | - |  |  | SI | T/2 |
| Q73 | - |  |  | SI | IP |
| QANATOM | - |  |  | SI | Anatomia |
| QATRIO | - |  |  | SI | Atrio |
| QCA | - |  |  | SI | Circunferencia Abdominal |
| QCC | - |  |  | SI | Circunferencia Craneana |
| QCERVIX | - |  |  | SI | Cervix |
| QCISTMAGNA | - |  |  | SI | Cisterna Magna |
| QCONCLU | - |  |  | SI | Conclusion |
| QDBP | - |  |  | SI | Diámetro Biparietal |
| QDETER | - |  |  | SI | Peso Estimado Deter |
| QDFO | - |  |  | SI | Diametro Fronto-Occipital |
| QEGEST | - |  |  | SI | Edad Gestacional |
| QEGESTDBP | - |  |  | SI | Edad Gestacional (DBP) |
| QEGESTFEM | - |  |  | SI | Edad Gestacional (FEM) |
| QEGESTREAL | - |  |  | SI | Edad Gestacional Real |
| QFECHAEXAMEN | - |  |  | SI | Fecha de Examen |
| QFEM | - |  |  | SI | Longitud Femur |
| QFUR | - |  |  | SI | Fecha Ultima Regla |
| QGr | - |  |  | SI | Grado |
| QHADLOCK | - |  |  | SI | Peso Estimado Hadlock |
| QHUESONASAL | - |  |  | SI | Hueso Nasal |
| QINDICECP | - |  |  | SI | IndiceCP |
| QINDICEDUCTUS | - |  |  | SI | Indice Ductus |
| QINS | - |  |  | SI | Inserción |
| QIPACM | - |  |  | SI | IPACM |
| QIPDER | - |  |  | SI | IPDER |
| QIPDUC | - |  |  | SI | IPDUC |
| QIPIZQ | - |  |  | SI | IPIZQ |
| QIPPROM | - |  |  | SI | IP Promedio |
| QIPUMB | - |  |  | SI | IPUMB |
| QLA1 | - |  |  | SI | LA 1 |
| QLA2 | - |  |  | SI | LA 2 |
| QLA3 | - |  |  | SI | LA 3 |
| QLA4 | - |  |  | SI | LA 4 |
| QLAMNIOTICO | - |  |  | SI | Liquido Amniotico |
| QLOC | - |  |  | SI | Localización |
| QMAXACM | - |  |  | SI | Max ACM |
| QMAXDER | - |  |  | SI | Max Derecha |
| QMAXDUC | - |  |  | SI | Max Ductus |
| QMAXIZQ | - |  |  | SI | Max Izquierda |
| QMAXUMB | - |  |  | SI | Max Umbilical |
| QMEDIAACM | - |  |  | SI | Media ACM |
| QMEDIADER | - |  |  | SI | Media derecha |
| QMEDIADUC | - |  |  | SI | Media ductus |
| QMEDIAIZQ | - |  |  | SI | Media Izquierda |
| QMEDIAUMB | - |  |  | SI | Media Umbilical |
| QMINACM | - |  |  | SI | Min ACM |
| QMINDER | - |  |  | SI | Min Derecha |
| QMINDUC | - |  |  | SI | Min Ductus |
| QMINIZQ | - |  |  | SI | Min Izquierda |
| QMINUMB | - |  |  | SI | Min Umbilical |
| QObs | - |  |  | SI | Observaciones |
| QPBF | - |  |  | SI | Perfil Biofisico |
| QPLACENT | - |  |  | SI | Placenta |
| QPRESENT | - |  |  | SI | Presentacion |
| QSDACM | - |  |  | SI | SDACM |
| QSDDER | - |  |  | SI | SDDER |
| QSDDUC | - |  |  | SI | SDDUC |
| QSDIZQ | - |  |  | SI | SDIZQ |
| QSDUMB | - |  |  | SI | SD |
| QSHEPARD | - |  |  | SI | Peso Estimado Shepard |
| QT2 | - |  |  | SI | T2 |
| QTALLA | - |  |  | SI | Talla |
| QTOTALLA | - |  |  | SI | Total LA |
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