# SQLUser.LB_EpisodePaymentContact

**Schema:** SQLUser
**Columnas:** 92
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBEPPC_RowID | bigint | PK |  | NO | - |
| LBEPPC_AddressOne | varchar |  |  | SI | Address line one |
| LBEPPC_AddressTwo | varchar |  |  | SI | Address line two |
| LBEPPC_City_DR | bigint |  | FK | SI | City |
| LBEPPC_DOB | date |  |  | SI | Date Of Birth |
| LBEPPC_FirstName | varchar |  |  | SI | Contact Firstname |
| LBEPPC_LabEpisode_DR | bigint |  | FK | SI | Lab Episode |
| LBEPPC_MedicareCardNo | varchar |  |  | SI | Medicare Card No |
| LBEPPC_Province_DR | bigint |  | FK | SI | Province |
| LBEPPC_ReferenceNo | varchar |  |  | SI | Reference No |
| LBEPPC_Surname | varchar |  |  | SI | Contact Surname  |
| LBEPPC_Zip_DR | bigint |  | FK | SI | Zip Code |
| Q01 | - |  |  | SI | Postura General |
| Q02 | - |  |  | SI | Posterior |
| Q03 | - |  |  | SI | Anterior |
| Q04 | - |  |  | SI | Lateral |
| Q05 | - |  |  | SI | Ubicación e Intensidad |
| Q06 | - |  |  | SI | Palpitación |
| Q07 | - |  |  | SI | Factores que lo inducen |
| Q08 | - |  |  | SI | Factores que lo aminoran |
| Q09 | - |  |  | SI | Flexión cabeza 35-45 al Ingreso |
| Q10 | - |  |  | SI | Extensión cabeza 35-45 al Ingreso |
| Q11 | - |  |  | SI | Inclinación Lateral cabeza 60-80 al Ingreso |
| Q12 | - |  |  | SI | Rotación en Flexión 45-0-45 al Ingreso |
| Q13 | - |  |  | SI | Rotación en Extensión 60-0-60 al Ingreso |
| Q14 | - |  |  | SI | Extensión Columna 0-30 al Ingreso |
| Q15 | - |  |  | SI | Flexión Columna 75 al Ingreso |
| Q16 | - |  |  | SI | Inclinación Lateral al Ingreso |
| Q17 | - |  |  | SI | Rotación Tronco al Ingreso |
| Q18 | - |  |  | SI | Ingreso A/P |
| Q19 | - |  |  | SI | Flexión cabeza 35-45 al Alta |
| Q20 | - |  |  | SI | Pruebas Funcionales |
| Q21 | - |  |  | SI | Examen Radiológico |
| Q22 | - |  |  | SI | Medición |
| Q23 | - |  |  | SI | Miembro Inferior Derecho |
| Q24 | - |  |  | SI | Miembro Inferior Izquierdo |
| Q25 | - |  |  | SI | Anteversión |
| Q26 | - |  |  | SI | Retroversión |
| Q27 | - |  |  | SI | Extensión cabeza 35-45 al Alta |
| Q28 | - |  |  | SI | Inclinación Lateral cabeza 60-80 al Alta |
| Q29 | - |  |  | SI | Rotación en Flexión 45-0-45 al Alta |
| Q30 | - |  |  | SI | Rotación en Extensión 60-0-60 al Alta |
| Q31 | - |  |  | SI | Extensión Columna 0-30 al Alta |
| Q32 | - |  |  | SI | Flexión Columna 75 al Alta |
| Q33 | - |  |  | SI | Inclinación Lateral al Alta |
| Q34 | - |  |  | SI | Rotación Tronco al Alta |
| Q35 | - |  |  | SI | Observación |
| Q36 | - |  |  | SI | Dolor (EVA) |
| Q37 | - |  |  | SI | Rangos Articulares |
| Q38 | - |  |  | SI | Medición |
| Q39 | - |  |  | SI | A/P |
| Q40 | - |  |  | SI | A/P |
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