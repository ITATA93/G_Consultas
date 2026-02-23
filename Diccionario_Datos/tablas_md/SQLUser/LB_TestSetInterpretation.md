# SQLUser.LB_TestSetInterpretation

**Schema:** SQLUser
**Columnas:** 90
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Exámenes de Laboratorio**. Solicitudes y resultados.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBTSINT_ParRef | bigint | PK |  | NO | Parent TestSet DR |
| LBTSINT_AppEventRule_DR | bigint |  | FK | SI | Interpretation App Event Rule |
| LBTSINT_Document_DR | bigint |  | FK | SI | Link to a websys.Document that stores the formated... |
| LBTSINT_Index | varchar |  |  | SI | Index of Interpretation within app event rule list... |
| LBTSINT_Interpretation_DR | bigint |  | FK | SI | Link to the interpretation |
| LBTSINT_Reportable | varchar |  |  | SI | Reportable flag |
| LBTSINT_RowID | varchar |  |  | NO | - |
| LBTSINT_SourceType | varchar |  |  | SI | Interpetation Source |
| Q01 | - |  |  | SI | FECHA ENVIO |
| Q02 | - |  |  | SI | APELLIDO PATERNO |
| Q03 | - |  |  | SI | APELLIDO MATERNO |
| Q04 | - |  |  | SI | NOMBRE |
| Q05 | - |  |  | SI | RUT |
| Q06 | - |  |  | SI | FECHA DE NACIMIENTO |
| Q07 | - |  |  | SI | SEXO |
| Q08 | - |  |  | SI | PREVISIÓN |
| Q09 | - |  |  | SI | DIRECCIÓN |
| Q10 | - |  |  | SI | TELÉFONO |
| Q11 | - |  |  | SI | PROFESIONAL RESPONSABLE |
| Q12 | - |  |  | SI | ESTABLECIMIENTO |
| Q13 | - |  |  | SI | DIRECCIÓN |
| Q14 | - |  |  | SI | TELEFONO |
| Q15 | - |  |  | SI | FAX |
| Q16 | - |  |  | SI | MAIL |
| Q17 | - |  |  | SI | Con Eosinofilia |
| Q18 | - |  |  | SI | Sin Eosinofilia |
| Q19 | - |  |  | SI | Observación Microscópica |
| Q20 | - |  |  | SI | Tipo de Muestra |
| Q21 | - |  |  | SI | Fecha Toma Muestra |
| Q22 | - |  |  | SI | Hora Toma Muestra |
| Q23 | - |  |  | SI | Fecha de Eliminación |
| Q24 | - |  |  | SI | Via de Eliminación |
| Q25 | - |  |  | SI | Viaje Reciente Extranjero |
| Q26 | - |  |  | SI | Lugar |
| Q27 | - |  |  | SI | Tiene Macotas |
| Q28 | - |  |  | SI | Especificar |
| Q29 | - |  |  | SI | Presenta Eosinofilia |
| Q30 | - |  |  | SI | N° |
| Q31 | - |  |  | SI | % de Eosinofilia |
| Q32 | - |  |  | SI | Consumo Carne Cruda |
| Q33 | - |  |  | SI | Tipo de Preparación |
| Q34 | - |  |  | SI | Lugar de Consumo |
| Q35 | - |  |  | SI | Servicio |
| Q36 | - |  |  | SI | Especificar |
| Q37 | - |  |  | SI | OTROS ANTECEDENTES |
| Q38 | - |  |  | SI | Hora Toma de Muestra |
| Q39 | - |  |  | SI | Edad |
| Q40 | - |  |  | SI | Ciudad |
| Q41 | - |  |  | SI | Otro |
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