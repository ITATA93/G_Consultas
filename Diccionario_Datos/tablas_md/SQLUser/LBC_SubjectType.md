# SQLUser.LBC_SubjectType

**Schema:** SQLUser
**Columnas:** 109
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCSUBT_RowID | bigint | PK |  | NO | - |
| LBCSUBT_Code | varchar |  |  | NO | Code |
| LBCSUBT_CodeTableTags | varchar |  |  | SI | List of code table tags |
| LBCSUBT_CreatedDate | date |  |  | SI | Created Date |
| LBCSUBT_CreatedTime | time |  |  | SI | Created Time |
| LBCSUBT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCSUBT_Desc | varchar |  |  | NO | Description |
| LBCSUBT_Owner | varchar |  |  | SI | Owner |
| LBCSUBT_UpdatedDate | date |  |  | SI | Updated Date |
| LBCSUBT_UpdatedTime | time |  |  | SI | Updated Time |
| LBCSUBT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Total - Hombres - Menores De 15 Años  - Establecim... |
| Q02 | - |  |  | SI | Total - Mujeres - Menores De 15 Años  - Establecim... |
| Q03 | - |  |  | SI | Total - Hombres - 15 Años Y Más - Establecimientos... |
| Q04 | - |  |  | SI | Total - Mujeres - 15 Años Y Más - Establecimientos... |
| Q05 | - |  |  | SI | Total - Institucional - Modalidad - Establecimient... |
| Q06 | - |  |  | SI | Total - Sistema - Compra De Servicio - Modalidad -... |
| Q07 | - |  |  | SI | Total - Extrasistema - Compra De Servicio - Modali... |
| Q08 | - |  |  | SI | Total - Hombres - Menores De 15 Años  - Procedimie... |
| Q09 | - |  |  | SI | Total - Mujeres - Menores De 15 Años  - Procedimie... |
| Q10 | - |  |  | SI | Total - Hombres - 15 Años Y Más - Procedimientos P... |
| Q11 | - |  |  | SI | Total - Mujeres - 15 Años Y Más - Procedimientos P... |
| Q12 | - |  |  | SI | Ecocardiograma - Hombres - Menores De 15 Años  - E... |
| Q13 | - |  |  | SI | Ecocardiograma - Mujeres - Menores De 15 Años  - E... |
| Q14 | - |  |  | SI | Ecocardiograma - Hombres - 15 Años Y Más - Estable... |
| Q15 | - |  |  | SI | Ecocardiograma - Mujeres - 15 Años Y Más - Estable... |
| Q16 | - |  |  | SI | Ecocardiograma - Institucional - Modalidad - Estab... |
| Q17 | - |  |  | SI | Ecocardiograma - Sistema - Compra De Servicio - Mo... |
| Q18 | - |  |  | SI | Ecocardiograma - Extrasistema - Compra De Servicio... |
| Q19 | - |  |  | SI | Ecocardiograma - Hombres - Menores De 15 Años  - P... |
| Q20 | - |  |  | SI | Ecocardiograma - Mujeres - Menores De 15 Años  - P... |
| Q21 | - |  |  | SI | Ecocardiograma - Hombres - 15 Años Y Más - Procedi... |
| Q22 | - |  |  | SI | Ecocardiograma - Mujeres - 15 Años Y Más - Procedi... |
| Q23 | - |  |  | SI | Trombolisis De Urgencia Infarto Cerebral (Acv) - H... |
| Q24 | - |  |  | SI | Trombolisis De Urgencia Infarto Cerebral (Acv) - M... |
| Q25 | - |  |  | SI | Trombolisis De Urgencia Infarto Cerebral (Acv) - H... |
| Q26 | - |  |  | SI | Trombolisis De Urgencia Infarto Cerebral (Acv) - M... |
| Q27 | - |  |  | SI | Trombolisis De Urgencia Infarto Cerebral (Acv) - I... |
| Q28 | - |  |  | SI | Trombolisis De Urgencia Infarto Cerebral (Acv) - S... |
| Q29 | - |  |  | SI | Trombolisis De Urgencia Infarto Cerebral (Acv) - E... |
| Q30 | - |  |  | SI | Trombolisis De Urgencia Infarto Cerebral (Acv) - H... |
| Q31 | - |  |  | SI | Trombolisis De Urgencia Infarto Cerebral (Acv) - M... |
| Q32 | - |  |  | SI | Trombolisis De Urgencia Infarto Cerebral (Acv) - H... |
| Q33 | - |  |  | SI | Trombolisis De Urgencia Infarto Cerebral (Acv) - M... |
| Q34 | - |  |  | SI | Trombolisis Intracoronaria (Iam) - Hombres - Menor... |
| Q35 | - |  |  | SI | Trombolisis Intracoronaria (Iam) - Mujeres - Menor... |
| Q36 | - |  |  | SI | Trombolisis Intracoronaria (Iam) - Hombres - 15 Añ... |
| Q37 | - |  |  | SI | Trombolisis Intracoronaria (Iam) - Mujeres - 15 Añ... |
| Q38 | - |  |  | SI | Trombolisis Intracoronaria (Iam) - Institucional -... |
| Q39 | - |  |  | SI | Trombolisis Intracoronaria (Iam) - Sistema - Compr... |
| Q40 | - |  |  | SI | Trombolisis Intracoronaria (Iam) - Extrasistema - ... |
| Q41 | - |  |  | SI | Trombolisis Intracoronaria (Iam) - Hombres - Menor... |
| Q42 | - |  |  | SI | Trombolisis Intracoronaria (Iam) - Mujeres - Menor... |
| Q43 | - |  |  | SI | Trombolisis Intracoronaria (Iam) - Hombres - 15 Añ... |
| Q44 | - |  |  | SI | Trombolisis Intracoronaria (Iam) - Mujeres - 15 Añ... |
| Q45 | - |  |  | SI | Ecografía Gineco-Obstétrica - Hombres - Menores De... |
| Q46 | - |  |  | SI | Ecografía Gineco-Obstétrica - Mujeres - Menores De... |
| Q47 | - |  |  | SI | Ecografía Gineco-Obstétrica - Hombres - 15 Años Y ... |
| Q48 | - |  |  | SI | Ecografía Gineco-Obstétrica - Mujeres - 15 Años Y ... |
| Q49 | - |  |  | SI | Ecografía Gineco-Obstétrica - Institucional - Moda... |
| Q50 | - |  |  | SI | Ecografía Gineco-Obstétrica - Sistema - Compra De ... |
| Q51 | - |  |  | SI | Ecografía Gineco-Obstétrica - Extrasistema - Compr... |
| Q52 | - |  |  | SI | Ecografía Gineco-Obstétrica - Hombres - Menores De... |
| Q53 | - |  |  | SI | Ecografía Gineco-Obstétrica - Mujeres - Menores De... |
| Q54 | - |  |  | SI | Ecografía Gineco-Obstétrica - Hombres - 15 Años Y ... |
| Q55 | - |  |  | SI | Ecografía Gineco-Obstétrica - Mujeres - 15 Años Y ... |
| QA | - |  |  | SI | Año |
| QHR | - |  |  | SI | Establecimiento |
| QM | - |  |  | SI | Mes |
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