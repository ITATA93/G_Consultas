# SQLUser.CT_BarcodeData

**Schema:** SQLUser
**Columnas:** 106
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTBD_RowID | bigint | PK |  | NO | - |
| CTBD_AssociatedProperties | varchar |  |  | SI | Associated Properties |
| CTBD_BarcodeDataType | varchar |  |  | NO | Barcode Data Type |
| CTBD_Code | varchar |  |  | NO | Code |
| CTBD_CodeTableClass_DR | varchar |  | FK | SI | Code Table Class |
| CTBD_CodeTableTags | varchar |  |  | SI | List of code table tags |
| CTBD_CreatedDate | date |  |  | SI | Created Date |
| CTBD_CreatedTime | time |  |  | SI | Created Time |
| CTBD_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CTBD_Desc | varchar |  |  | NO | Description |
| CTBD_UpdatedDate | date |  |  | SI | Updated Date |
| CTBD_UpdatedTime | time |  |  | SI | Updated Time |
| CTBD_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Nombre |
| Q02 | - |  |  | SI | Apellido Paterno |
| Q03 | - |  |  | SI | Apellido Materno |
| Q04 | - |  |  | SI | N° Ced. Identidad |
| Q05 | - |  |  | SI | Fecha de Nacimiento |
| Q06 | - |  |  | SI | Domicilio |
| Q07 | - |  |  | SI | Nombre Cuidador |
| Q08 | - |  |  | SI | Teléfono |
| Q09 | - |  |  | SI | Motivo de Hospitalización |
| Q10 | - |  |  | SI | Otras Lesiones |
| Q11 | - |  |  | SI | Tratamiento U.P.P. u Otras Lesiones |
| Q12 | - |  |  | SI | Otros Antecedentes |
| Q13 | - |  |  | SI | Fármacos |
| Q14 | - |  |  | SI | Número de la Dirección |
| Q15 | - |  |  | SI | Etnia |
| Q16 | - |  |  | SI | Edad |
| Q17 | - |  |  | SI | Categorización (Riesgo/Dependencia) |
| Q18 | - |  |  | SI | Fecha Próximo Control 1era. |
| Q19 | - |  |  | SI | Especialidad 1era. |
| Q20 | - |  |  | SI | Zona |
| Q21 | - |  |  | SI | Especialidad 2da. |
| Q22 | - |  |  | SI | Teléfono Contacto |
| Q23 | - |  |  | SI | Estado Conyugal |
| Q24 | - |  |  | SI | Fecha Próximo Control 2da. |
| Q25 | - |  |  | SI | Estado Ocupacional |
| Q26 | - |  |  | SI | Otros cuidados a realizar en el hogar |
| Q27 | - |  |  | SI | Diagnóstico de Egreso |
| Q28 | - |  |  | SI | Sala |
| Q29 | - |  |  | SI | Servicio que Deriva |
| Q30 | - |  |  | SI | Fecha Solicitud |
| Q31 | - |  |  | SI | Médico Solicitante |
| Q32 | - |  |  | SI | Teléfono Celular |
| Q33 | - |  |  | SI | Licencia Médica Entregada |
| Q34 | - |  |  | SI | Cuidados de Enfermería |
| Q35 | - |  |  | SI | Régimren |
| Q36 | - |  |  | SI | Reposo |
| Q37 | - |  |  | SI | Oxigeno |
| Q38 | - |  |  | SI | Resultado Escala  Braden |
| Q38ObsDR | - |  |  | SI | Resultado Escala  Braden DR |
| Q39 | - |  |  | SI | Cama |
| Q40 | - |  |  | SI | Requisitos Necesarios para la Hospitalización Domi... |
| Q41 | - |  |  | SI | 1. Fácil acceso a domicilio |
| Q42 | - |  |  | SI | 2. Inscrito(a) en CESFAM |
| Q43 | - |  |  | SI | 3. Presencia del Cuidador en Domicilio |
| Q44 | - |  |  | SI | 4. Cond.Higiénicas adecuadas en el Hogar |
| Q45 | - |  |  | SI | 5. Paciente no crítico |
| Q46 | - |  |  | SI | 6. Acceso Telefónico |
| Q47 | - |  |  | SI | 7. Educación a familia y/o Cuidador |
| Q48 | - |  |  | SI | 8. Previsón FONASA |
| Q49 | - |  |  | SI | Cual |
| Q50 | - |  |  | SI | INFORMACIÓN PREVIA |
| Q51 | - |  |  | SI | Tipo de Hospitalización Domiciliaria |
| Q52 | - |  |  | SI | ¿Paciente ingresa a Hospitalización Domiciliaria c... |
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