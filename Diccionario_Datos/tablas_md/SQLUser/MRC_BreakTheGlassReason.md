# SQLUser.MRC_BreakTheGlassReason

**Schema:** SQLUser
**Columnas:** 114
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BTGR_RowId | bigint | PK |  | NO | - |
| BTGR_Code | varchar |  |  | NO | Code |
| BTGR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| BTGR_CreatedDate | date |  |  | SI | Created Date |
| BTGR_CreatedTime | time |  |  | SI | Created Time |
| BTGR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| BTGR_DateFrom | date |  |  | SI | Date From |
| BTGR_DateTo | date |  |  | SI | Date To |
| BTGR_Desc | varchar |  |  | NO | Description |
| BTGR_Owner | varchar |  |  | SI | Owner |
| BTGR_UpdatedDate | date |  |  | SI | Updated Date |
| BTGR_UpdatedTime | time |  |  | SI | Updated Time |
| BTGR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Diagnóstico |
| Q02 | - |  |  | SI | Diagnóstico Maxilar Superior |
| Q03 | - |  |  | SI | Diagnóstico Maxilar Inferioir |
| Q04 | - |  |  | SI | Observaciones |
| Q05 | - |  |  | SI | Kennedy Maxilar Superior |
| Q06 | - |  |  | SI | Kennedy Maxilar Inferior |
| Q08 | - |  |  | SI | Fecha |
| Q09 | - |  |  | SI | Impresion Preliminar |
| Q10 | - |  |  | SI | Impresion Definitiva |
| Q11 | - |  |  | SI | Cubeta |
| Q12 | - |  |  | SI | Altura y/o Prueba de Base + Prueba de Color |
| Q13 | - |  |  | SI | Prueba de Cera |
| Q14 | - |  |  | SI | Instalación/Alta |
| Q15 | - |  |  | SI | Entrego Protesis y Cito a Control |
| Q16 | - |  |  | SI | Acta de Recepción |
| Q17 | - |  |  | SI | Comprobante de Recepción de Protesis |
| Q18 | - |  |  | SI | Controles |
| Q19 | - |  |  | SI | Pronostico |
| Q20 | - |  |  | SI | Superior 1 |
| Q21 | - |  |  | SI | Superior Parcial Acrílica |
| Q22 | - |  |  | SI | Superior Total Acrílica |
| Q23 | - |  |  | SI | Inferior1 |
| Q24 | - |  |  | SI | Inferior Parcial Acrílica |
| Q25 | - |  |  | SI | Inferior Total Acrílica |
| Q26 | - |  |  | SI | Color |
| Q28 | - |  |  | SI | Desea Agregar Nuevo Tratamiento [1] |
| Q29 | - |  |  | SI | Desea Agregar Nuevo Tratamiento [2] |
| Q30 | - |  |  | SI | Desea Agregar Nuevo Tratamiento [3] |
| Q31 | - |  |  | SI | Impresion Preliminar 1 |
| Q32 | - |  |  | SI | Impresion Preliminar 2 |
| Q33 | - |  |  | SI | Impresion Preliminar 3 |
| Q34 | - |  |  | SI | Impresion Definitiva 1 |
| Q35b | - |  |  | SI | Impresion Definitiva 2 |
| Q36 | - |  |  | SI | Impresion Definitiva 3 |
| Q36b | - |  |  | SI | Cubeta 1 |
| Q37 | - |  |  | SI | Cubeta 2 |
| Q38 | - |  |  | SI | Cubeta 3 |
| Q39 | - |  |  | SI | Altura y/o Prueba de Base + Prueba de Color 1 |
| Q40 | - |  |  | SI | Altura y/o Prueba de Base + Prueba de Color 2 |
| Q41 | - |  |  | SI | Altura y/o Prueba de Base + Prueba de Color 3 |
| Q42 | - |  |  | SI | Prueba de cera 1 |
| Q43 | - |  |  | SI | prueba de cera 2 |
| Q44 | - |  |  | SI | prueba de cera 3 |
| Q45b | - |  |  | SI | Instalacion Alta 1 |
| Q46 | - |  |  | SI | Instalacion? Alta 2 |
| Q47 | - |  |  | SI | Instalacion Alta 3 |
| Q49 | - |  |  | SI | Tratamiento |
| Q50 | - |  |  | SI | Fecha Control |
| Q51 | - |  |  | SI | Comentario |
| Q52 | - |  |  | SI | Contenido 2 |
| Q54 | - |  |  | SI | Color 1 |
| Q55 | - |  |  | SI | Color 2 |
| Q56 | - |  |  | SI | Color 3 |
| Q57 | - |  |  | SI | Color 4 |
| Q59 | - |  |  | SI | Digitado Por |
| Q60 | - |  |  | SI | Cera |
| Q61 | - |  |  | SI | Cera 1 |
| Q62 | - |  |  | SI | Cera 2 |
| Q63 | - |  |  | SI | Cera 3 |
| Q66 | - |  |  | SI | Pronóstico Observación |
| QRem1 | - |  |  | SI | Instalación/Alta |
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