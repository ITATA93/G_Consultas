# SQLUser.AR_HICInHospitalClaimRepElement

**Schema:** SQLUser
**Columnas:** 105
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuentas por Cobrar (AR)**. Facturación y cobranza de pacientes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| IHCRE_ParRef | bigint | PK |  | NO | - |
| ChildQ28DR | - |  |  | SI | Child Reference: Actividades Importantes |
| IHCRE_ElementName | varchar |  |  | NO | Name of the element |
| IHCRE_ElementValue | varchar |  |  | SI | Value of the element |
| IHCRE_RowID | varchar |  |  | NO | - |
| Q01 | - |  |  | SI | Fecha de Ingreso |
| Q02 | - |  |  | SI | Hora de Ingreso |
| Q03 | - |  |  | SI | Contextualización |
| Q04 | - |  |  | SI | Higiene |
| Q05 | - |  |  | SI | Vestuario |
| Q06 | - |  |  | SI | Arreglo Personal |
| Q07 | - |  |  | SI | Uso de Medicamento |
| Q08 | - |  |  | SI | Observación (Autocuidado) |
| Q09 | - |  |  | SI | Preparación de Alimento |
| Q10 | - |  |  | SI | Uso Medios de Comunicación |
| Q11 | - |  |  | SI | Cuidado de Hijos |
| Q12 | - |  |  | SI | Gestión y Movilidad en la Comunidad |
| Q13 | - |  |  | SI | Administración del Dinero |
| Q14 | - |  |  | SI | Gestión y Mantenimiento de Salud |
| Q15 | - |  |  | SI | Observación (Actividades Instrumentales) |
| Q16 | - |  |  | SI | Recreación |
| Q17 | - |  |  | SI | Observaciones (Recreación) |
| Q18 | - |  |  | SI | Trabajo |
| Q19 | - |  |  | SI | Observaciones (Trabajo) |
| Q20 | - |  |  | SI | Educación |
| Q21 | - |  |  | SI | Educación (Finalización) |
| Q22 | - |  |  | SI | Capacitaciones |
| Q23 | - |  |  | SI | Observaciones (Educaciones) |
| Q24 | - |  |  | SI | Participación Social |
| Q25 | - |  |  | SI | Observaciones (Participación Social) |
| Q26 | - |  |  | SI | Roles |
| Q27 | - |  |  | SI | Rutina |
| Q29 | - |  |  | SI | Rutina Diaria  Mañana (Lunes a Viernes) |
| Q30 | - |  |  | SI | Rutina Diaria Tarde (Lunes a Viernes) |
| Q31 | - |  |  | SI | Rutina Diaria Manaña (Sábado y Domingo) |
| Q32 | - |  |  | SI | Rutina Diaria Tarde (Sábado y Domingo) |
| Q33 | - |  |  | SI | Movilidad Global |
| Q34 | - |  |  | SI | Tolerancia al Esfuerzo |
| Q35 | - |  |  | SI | Destreza Fina |
| Q36 | - |  |  | SI | Ritmo y Fluidez de Movimiento |
| Q37 | - |  |  | SI | Visoperceptuales |
| Q38 | - |  |  | SI | Equilibrio |
| Q39 | - |  |  | SI | Orientación |
| Q40 | - |  |  | SI | Memoria |
| Q41 | - |  |  | SI | Atención y Concentración |
| Q42 | - |  |  | SI | Resolución de Problemas |
| Q43 | - |  |  | SI | Contacto Social |
| Q44 | - |  |  | SI | Participación Grupal |
| Q45 | - |  |  | SI | Comunicación |
| Q46 | - |  |  | SI | Tolerancia Frustración |
| Q47 | - |  |  | SI | Respuesta a Crítica |
| Q48 | - |  |  | SI | Autocontrol |
| Q49 | - |  |  | SI | Motivación de Logro |
| Q50 | - |  |  | SI | Social Comunitario |
| Q51 | - |  |  | SI | Familia |
| Q52 | - |  |  | SI | Amigos |
| Q53 | - |  |  | SI | Trabajo / Estudio |
| Q54 | - |  |  | SI | Comunidad |
| Q55 | - |  |  | SI | Intereses |
| Q56 | - |  |  | SI | Proyecto Vital |
| Q57 | - |  |  | SI | Áreas Ocupacionales Exitosas |
| Q58 | - |  |  | SI | Áreas Ocupacionales en Riesgo |
| Q59 | - |  |  | SI | Objetivos |
| Q60 | - |  |  | SI | Estrategias |
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