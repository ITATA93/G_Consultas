# SQLUser.PA_Notification

**Schema:** SQLUser
**Columnas:** 126
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| NOT_RowId | bigint | PK |  | NO | - |
| NOT_AdmType | varchar |  |  | SI | Admission Type |
| NOT_CTCP_DR | varchar |  | FK | SI | Des REf CTCP |
| NOT_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC |
| NOT_Diagnosis_DR | bigint |  | FK | SI | Des Ref MRCIDx |
| NOT_ExpAdmDate | date |  |  | SI | Expected Adm Date |
| NOT_ExpLOS | double |  |  | SI | Expected Length Of Stay |
| NOT_ExpOperDate | date |  |  | SI | Expected Operation Date |
| NOT_MRC_DiagType_DR | bigint |  | FK | SI | Des REf DiagType |
| NOT_Operation_DR | bigint |  | FK | SI | Des Ref to Operation |
| NOT_OrderSubcat_DR | bigint |  | FK | SI | Des Ref OrderSubCat |
| NOT_PAADM_DR | bigint |  | FK | NO | Des Ref to PAADM |
| NOT_RoomType_DR | bigint |  | FK | SI | Des Ref RoomType |
| NOT_Urgent | varchar |  |  | SI | Urgent |
| Q01 | - |  |  | SI | Establecimiento |
| Q02 | - |  |  | SI | Fecha Entrevista |
| Q03 | - |  |  | SI | Hospitalizado |
| Q04L | - |  |  | SI | DATOS DE IDENTIFICACIÓN DEL PACIENTE |
| Q04N | - |  |  | SI | Nombres |
| Q04NS | - |  |  | SI | Nombre Social |
| Q04PA | - |  |  | SI | Primer Apellido |
| Q04SA | - |  |  | SI | Segundo Apellido |
| Q05 | - |  |  | SI | R.U.N./ FC / HC / Pasaporte |
| Q06 | - |  |  | SI | Sexo Biológico |
| Q07 | - |  |  | SI | Fecha de nacimiento |
| Q08 | - |  |  | SI | Edad |
| Q09 | - |  |  | SI | Pueblo Originario - Declarado |
| Q10 | - |  |  | SI | Nacionalidad |
| Q10TA | - |  |  | SI | Tiempo en Chile (Años) |
| Q10TM | - |  |  | SI | Tiempo en Chile (Meses) |
| Q11 | - |  |  | SI | Pueblo Tribal |
| Q12 | - |  |  | SI | Domicilio |
| Q12B | - |  |  | SI | Block |
| Q12D | - |  |  | SI | Departamento |
| Q12N | - |  |  | SI | Número |
| Q12P | - |  |  | SI | Población |
| Q13 | - |  |  | SI | Comuna de Residencia |
| Q13C | - |  |  | SI | Código Comuna |
| Q14 | - |  |  | SI | Teléfono |
| Q15 | - |  |  | SI | Condición de Actividad |
| Q16 | - |  |  | SI | Ocupación |
| Q17 | - |  |  | SI | Orientación Sexual |
| Q18 | - |  |  | SI | Identidad de Género |
| Q19 | - |  |  | SI | Estado Civil |
| Q20 | - |  |  | SI | Nivel Educacional |
| Q21 | - |  |  | SI | Completó el Nivel educaciona |
| Q22 | - |  |  | SI | Método Utilizado |
| Q22C | - |  |  | SI | CIE-10 Método Utilizado |
| Q22L | - |  |  | SI | ANTECEDENTES DEL INTENTO DE SUICIDIO |
| Q23 | - |  |  | SI | Comorbilidad |
| Q23C | - |  |  | SI | CIE-10 Comorbilidad |
| Q24 | - |  |  | SI | Diagnósticos Previos Salud Mental |
| Q24C | - |  |  | SI | CIE-10 Diagnósticos&nbsp |
| Q25 | - |  |  | SI | Fecha del intento suicida |
| Q26 | - |  |  | SI | Intentos Previos |
| Q27 | - |  |  | SI | Número de intentos previos |
| Q28 | - |  |  | SI | Fecha Intento Previo |
| Q29 | - |  |  | SI | Tratamiento Salud Mental |
| Q30 | - |  |  | SI | Adherencia al tratamiento |
| Q31 | - |  |  | SI | Lugar de atención |
| Q32 | - |  |  | SI | Embarazo |
| Q33 | - |  |  | SI | Abuso de alcohol o drogas |
| Q33C | - |  |  | SI | ¿CUÁL? |
| Q34 | - |  |  | SI | VIF |
| Q35 | - |  |  | SI | Desencadenante del Evento |
| Q36 | - |  |  | SI | IS (Intento de Suicidio) o Suicidio en su entorno |
| Q36B | - |  |  | SI | OBSERVACIONES |
| Q37 | - |  |  | SI | Red de Apoyo Efectivo |
| Q37Q | - |  |  | SI | ¿QUIÉN / QUIENES? |
| Q38 | - |  |  | SI | Persistencia de Ideación suicida |
| Q39 | - |  |  | SI | Derivación Red Asistencial |
| Q40L | - |  |  | SI | DATOS PERSONA RESPONSABLE DEL PACIENTE |
| Q40N | - |  |  | SI | Nombre |
| Q40R | - |  |  | SI | Relación /Parentesco |
| Q40T | - |  |  | SI | Teléfono |
| Q41C | - |  |  | SI | Correo del Profesional |
| Q41L | - |  |  | SI | DATOS DEL PROFESIONAL QUE NOTIFICA |
| Q41N | - |  |  | SI | Nombres del Profesional |
| Q41P | - |  |  | SI | Apellidos del Profesional |
| Q41R | - |  |  | SI | R.U.N. del Profesional |
| Q41T | - |  |  | SI | Teléfono del Profesional |
| Q42 | - |  |  | SI | Observaciones |
| Q43 | - |  |  | SI | Fecha de Notificación |
| Q43C | - |  |  | SI | NOTIFICACIÓN: Enviar a |
| Q44 | - |  |  | SI | ¿Fallece? |
| Q45 | - |  |  | SI | Vía de Entrada del Equipo Piscología de Enlace |
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