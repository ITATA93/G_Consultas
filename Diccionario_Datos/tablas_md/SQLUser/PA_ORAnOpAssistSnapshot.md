# SQLUser.PA_ORAnOpAssistSnapshot

**Schema:** SQLUser
**Columnas:** 86
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PAOAS_ParRef | bigint | PK |  | NO | PA_ORAnaestOper Parent Reference |
| PAOAS_Assist_DR | varchar |  | FK | NO | Assistant Des Ref to CTCP |
| PAOAS_Childsub | numeric |  |  | NO | Childsub |
| PAOAS_RowId | varchar |  |  | NO | - |
| Q01 | - |  |  | SI | Fecha de Registro |
| Q02 | - |  |  | SI | Antecedentes del Tutor |
| Q03 | - |  |  | SI | Nombre Completo Tutor |
| Q04 | - |  |  | SI | RUT del Tutor |
| Q05 | - |  |  | SI | Parentesco del Tutor |
| Q06 | - |  |  | SI | Teléfono del Tutor |
| Q07 | - |  |  | SI | Dirección del Tutor |
| Q08 | - |  |  | SI | Comuna del Tutor |
| Q09 | - |  |  | SI | Fecha de Ingreso HD |
| Q10 | - |  |  | SI | Unidad de Procedencia |
| Q11 | - |  |  | SI | CESFAM o Centro Médico de Atención Habitual |
| Q12 | - |  |  | SI | Anamnesis |
| Q14 | - |  |  | SI | Exámenes de Laboratorio Imágenes u Otros |
| Q34 | - |  |  | SI | libre eliminar al final |
| Q35 | - |  |  | SI | EXAMEN FÍSICO |
| Q36 | - |  |  | SI | Cabeza |
| Q36ObsDR | - |  |  | SI | Cabeza DR |
| Q37 | - |  |  | SI | Comentarios Cabeza |
| Q38 | - |  |  | SI | Tórax |
| Q38ObsDR | - |  |  | SI | Tórax DR |
| Q39 | - |  |  | SI | Comentarios Tórax |
| Q40 | - |  |  | SI | Mamas |
| Q40ObsDR | - |  |  | SI | Mamas DR |
| Q41 | - |  |  | SI | Comentarios Mamas |
| Q42 | - |  |  | SI | Abdomen |
| Q42ObsDR | - |  |  | SI | Abdomen DR |
| Q43 | - |  |  | SI | Comentarios Abdomen |
| Q44 | - |  |  | SI | Extremidades Superior |
| Q44ObsDR | - |  |  | SI | Extremidades Superior DR |
| Q45 | - |  |  | SI | Comentarios Extremidades Superior |
| Q46 | - |  |  | SI | Extremidades Inferior |
| Q46ObsDR | - |  |  | SI | Extremidades Inferior DR |
| Q47 | - |  |  | SI | Comentarios Extremidades Inferior |
| Q48 | - |  |  | SI | Genitales |
| Q48ObsDR | - |  |  | SI | Genitales DR |
| Q49 | - |  |  | SI | Comentarios Genitales |
| Q50 | - |  |  | SI | Otros |
| Q51 | - |  |  | SI | TRATAMIENTO HABITUAL |
| Q53 | - |  |  | SI | Resultados de Categorización |
| Q54 | - |  |  | SI | Prestaciones de salud especificas |
| Q57 | - |  |  | SI | PLAN TERAPÉUTICO |
| Q59 | - |  |  | SI | Nombre Profesional que registra |
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