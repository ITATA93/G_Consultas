# SQLUser.LB_Reagent

**Schema:** SQLUser
**Columnas:** 186
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBRE_RowID | bigint | PK |  | NO | - |
| CQGRG2 | - |  |  | SI | (null) |
| CQGr | - |  |  | SI | (null) |
| CQHNGI | - |  |  | SI | (null) |
| CQINS | - |  |  | SI | (null) |
| CQINSG2 | - |  |  | SI | (null) |
| CQLOC | - |  |  | SI | (null) |
| CQLOCG2 | - |  |  | SI | (null) |
| CQMEMBRANA | - |  |  | SI | (null) |
| CQMEMBRANAGI | - |  |  | SI | (null) |
| CQMENBRANAGII | - |  |  | SI | (null) |
| CQPLACENTAGI | - |  |  | SI | (null) |
| CQPRESENTGI | - |  |  | SI | (null) |
| CQPRESENTGII | - |  |  | SI | (null) |
| CQnasal | - |  |  | SI | (null) |
| LBRE_BatchNumber | varchar |  |  | NO | Batch Number |
| LBRE_ContainerNumber | varchar |  |  | SI | Container ID (Free text comments) |
| LBRE_DateInUse | date |  |  | SI | Date In Use |
| LBRE_DateReceived | date |  |  | SI | Date Received |
| LBRE_EntryDate | date |  |  | SI | Date of Entry |
| LBRE_EntryTime | time |  |  | SI | Time of Entry |
| LBRE_EntryUser_DR | bigint |  | FK | SI | User |
| LBRE_ExpiryDate | date |  |  | SI | Expiry Date |
| LBRE_ExpiryTime | time |  |  | SI | Expiry Time |
| LBRE_LabSite_DR | bigint |  | FK | SI | Lab Site |
| LBRE_Reagent_DR | bigint |  | FK | NO | Reagent |
| LBRE_ReceivedCondition_DR | bigint |  | FK | SI | Condition when Received |
| LBRE_Supplier_DR | bigint |  | FK | SI | Supplier |
| QANATOMIAGI | - |  |  | SI | Anatomía Gemelo I |
| QANATOMIAGII | - |  |  | SI | Anatomía Gemelo II |
| QATRIUMGI | - |  |  | SI | Atrium Gemelo I |
| QATRIUMGII | - |  |  | SI | Atrium Gemelo II |
| QCAGI | - |  |  | SI | Circunferencia Abdominal Gemelo I |
| QCAGII | - |  |  | SI | Circunferencia Abdominal Gemelo II |
| QCCGI | - |  |  | SI | Circunferencia Craneana GI |
| QCCGII | - |  |  | SI | Circunferencia Craneana GII |
| QCEREBGI | - |  |  | SI | Cerebelo GI |
| QCEREBGII | - |  |  | SI | Cerebelo GII |
| QCISTMAGNAGI | - |  |  | SI | Cisterna Magna Gemelo I |
| QCISTMAGNAGII | - |  |  | SI | Cisterna Magna Gemelo II |
| QCOLMAX1 | - |  |  | SI | Columna Máxima |
| QCOLMAX2 | - |  |  | SI | Columna Máxima |
| QCONCLUSION | - |  |  | SI | Conclusión |
| QDBPGI | - |  |  | SI | Diámetro Biparietal Gemelo I |
| QDBPGII | - |  |  | SI | Diámetro Biparietal Gemelo II |
| QDEL | - |  |  | SI | Delgadag2 |
| QDEL2 | - |  |  | SI | Delgadag2 |
| QDETERGI | - |  |  | SI | Peso Estimado GI Deter |
| QDETERGII | - |  |  | SI | Peso Estimado GII Deter |
| QDFO1 | - |  |  | SI | Diámetro Fronto Occipital |
| QDFO2 | - |  |  | SI | Diámetro Fronto Occipital |
| QDISCORD | - |  |  | SI | Discordancia |
| QEGEST | - |  |  | SI | EGEST |
| QEGESTDBP | - |  |  | SI | Edad Gestacional DBP |
| QEGESTDBP2 | - |  |  | SI | EGESTDBP2 |
| QEGESTFEM | - |  |  | SI | Edad Gestacional FEM |
| QEGESTFEM2 | - |  |  | SI | EGESTFEM2 |
| QEGESTREAL | - |  |  | SI | Edad gestacional real |
| QFCARDIACAGI | - |  |  | SI | Frecuencia Cardíaca Gemelo I |
| QFCARDIACAGII | - |  |  | SI | Frecuencia cardíaca Gemelo II |
| QFECHAEXAMEN | - |  |  | SI | Fecha Examen |
| QFEMGI | - |  |  | SI | Longitud Fémur Gemelo I |
| QFEMGII | - |  |  | SI | Longitud Fémur Gemelo II |
| QFUR | - |  |  | SI | Fecha última Regla |
| QG1 | - |  |  | SI | Gruesag1 |
| QG2 | - |  |  | SI | Gruesag2 |
| QGRG2 | - |  |  | SI | Grado |
| QGr | - |  |  | SI | Grado |
| QHADLOCKGI | - |  |  | SI | Peso Estimado GI Hadlock |
| QHADLOCKGII | - |  |  | SI | Peso Estimado GII Hadlock |
| QHNGI | - |  |  | SI | Hueso Nasal GI |
| QHUESONASALGI | - |  |  | SI | Hueso Nasal Gemelo I |
| QHUESONASALGII | - |  |  | SI | Hueso Nasal Gemelo II |
| QILAGI | - |  |  | SI | Índice Líquido Amniótico GI |
| QINS | - |  |  | SI | Inserción |
| QINSG2 | - |  |  | SI | Inserción |
| QIPACMGI | - |  |  | SI | Índice Ponderado Arteria Cerebral Media Gemelo I |
| QIPACMGII | - |  |  | SI | Índice Ponderado Arteria Cerebral Media Gemelo II |
| QIPDER | - |  |  | SI | IPDER |
| QIPIZQ | - |  |  | SI | IPIZQ |
| QIPPROM | - |  |  | SI | IP Promedio |
| QIPUMBGI | - |  |  | SI | Índice Ponderado Arteria Umbilical Gemelo I |
| QIPUMBGII | - |  |  | SI | Índice Ponderado Arteria Umbilical Gemelo II |
| QIRACMGI | - |  |  | SI | IR Arteria Cerebral Media Gemelo I |
| QIRACMGII | - |  |  | SI | IR Arteria Cerebral Media Gemelo II |
| QIRARTUMGI | - |  |  | SI | IR Arteria Umbilical Gemelo I |
| QIRDER | - |  |  | SI | IRDER |
| QIRIZQ | - |  |  | SI | IRIZQ |
| QIRUMBGI | - |  |  | SI | IR Umbilical Gemelo I |
| QIRUMBGII | - |  |  | SI | IR Umbilical Gemelo II |
| QLA1GI | - |  |  | SI | Líquido Amniótico 1 Gemelo I |
| QLA1GII | - |  |  | SI | Líquido Amniótico 1 Gemelo II |
| QLA2GI | - |  |  | SI | Líquido Amniótico 2 Gemelo I |
| QLA2GII | - |  |  | SI | Líquido Amniótico 2 Gemelo II |
| QLA3GI | - |  |  | SI | Líquido Amniótico 3 Gemelo I |
| QLA3GII | - |  |  | SI | Líquido Amniótico 3 Gemelo II |
| QLA4GI | - |  |  | SI | Líquido Amniótico 4 Gemelo I |
| QLA4GII | - |  |  | SI | Líquido Amniótico 4 Gemelo II |
| QLAMNIOTICOGI | - |  |  | SI | Líquido Amniótico Gemelo I |
| QLAMNIOTICOGII | - |  |  | SI | Líquido Amniótico Gemelo II |
| QLOC | - |  |  | SI | Localización |
| QLOCG2 | - |  |  | SI | LocalizaciónG2 |
| QMAXACMGI | - |  |  | SI | Max Arteria Cerebral Media Gemelo I |
| QMAXACMGII | - |  |  | SI | Max Arteria Cerebral Media Gemelo II |
| QMAXDER | - |  |  | SI | MAXDER |
| QMAXIZQ | - |  |  | SI | MAXIZQ |
| QMAXUMBGI | - |  |  | SI | Max Arteria Umbilical Gemelo I |
| QMAXUMBGII | - |  |  | SI | Max Arteria Umbilical Gemelo II |
| QMEDIAACMGI | - |  |  | SI | Media Arteria Cerebral Media Gemelo I |
| QMEDIAACMGII | - |  |  | SI | Media Arteria Cerebral Media Gemelo II |
| QMEDIADER | - |  |  | SI | MEDIADER |
| QMEDIAIZQ | - |  |  | SI | MEDIAIZQ |
| QMEDIAUMBGI | - |  |  | SI | Media Arteria Umbilical Gemelo I |
| QMEDIAUMBGII | - |  |  | SI | Media Arteria Umbilical Gemelo II |
| QMEMBRANA | - |  |  | SI | Membrana |
| QMEMBRANAGI | - |  |  | SI | Membrana Gemelo I |
| QMENBRANAGII | - |  |  | SI | Membrana Gemelo II |
| QMINACMGI | - |  |  | SI | Min Arteria Cerebral Media Gemelo I |
| QMINACMGII | - |  |  | SI | Min Arteria Cerebral Media Gemelo II |
| QMINDER | - |  |  | SI | MINDER |
| QMINIZQ | - |  |  | SI | MINIZQ |
| QMINUMBGI | - |  |  | SI | Min Arteria Umbilical Gemelo I |
| QMINUMBGII | - |  |  | SI | Min Arteria Umbilical Gemelo II |
| QObs1 | - |  |  | SI | Observaciones |
| QPLACENTAGI | - |  |  | SI | Placenta Gemelo I |
| QPLACENTAGII | - |  |  | SI | Placenta Gemelo II |
| QPRESENTGI | - |  |  | SI | Presentación Gemelo I |
| QPRESENTGII | - |  |  | SI | Presentación Gemelo II |
| QQILAGII | - |  |  | SI | QILAGII |
| QSDACMGI | - |  |  | SI | SD Arteria Cerebral Media Gemelo I |
| QSDACMGII | - |  |  | SI | SD Arteria Cerebral Media Gemelo II |
| QSDDER | - |  |  | SI | SDDERGI |
| QSDIZQ | - |  |  | SI | SDDERGII |
| QSDUMBGI | - |  |  | SI | SD Arteria Umbilical Gemelo I |
| QSDUMBGII | - |  |  | SI | SD Arteria Umbilical Gemelo II |
| QSHEPARDGI | - |  |  | SI | Peso Estimado GI Shepard |
| QSHEPARDGII | - |  |  | SI | Peso Estimado GII Shepard |
| QT2GI | - |  |  | SI | T2 Arteria Umbilical Gemelo I |
| QT2UMBGII | - |  |  | SI | T2 Arteria Umbilical Gemelo II |
| QTALLAGI | - |  |  | SI | Talla Gemelo I |
| QTALLAGII | - |  |  | SI | Talla Gemelo II |
| QTNGI | - |  |  | SI | TN Gemelo I |
| QTNGII | - |  |  | SI | TN Gemelo II |
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
| QVEJIGAGI | - |  |  | SI | Vejiga Gemelo I |
| QVEJIGAGII | - |  |  | SI | Vejiga Gemelo II |
| Qnasal | - |  |  | SI | Hueso Nasal GII |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*