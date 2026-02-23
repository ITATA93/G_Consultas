# SQLUser.CT_CareProvKeywords

**Schema:** SQLUser
**Columnas:** 88
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de Profesionales**. Médicos y personal de salud.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| KEYW_ParRef | varchar | PK |  | NO | CT_CareProv Parent Reference |
| ChildQ22DR | - |  |  | SI | Child Reference: TABLA REGISTRO DE AUTOMONITOREO |
| KEYW_Anaestetist | varchar |  |  | SI | Anaestetist |
| KEYW_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC |
| KEYW_Childsub | double |  |  | NO | Childsub |
| KEYW_Name | varchar |  |  | SI | Name |
| KEYW_RowId | varchar |  |  | NO | - |
| KEYW_Specialist | varchar |  |  | SI | Specialist |
| KEYW_Surgeon | varchar |  |  | SI | Surgeon |
| Q01 | - |  |  | SI | Tipo de Atención |
| Q02 | - |  |  | SI | ANAMNESIS |
| Q03 | - |  |  | SI | Motivo de Inicio de Insulina |
| Q04 | - |  |  | SI | Acude con Acompañado |
| Q05 | - |  |  | SI | Relación del Acompañante |
| Q06 | - |  |  | SI | Nombre del Acompañante |
| Q07 | - |  |  | SI | Principal red de apoyo |
| Q08 | - |  |  | SI | Trabaja |
| Q09 | - |  |  | SI | Tipo de trabajo |
| Q10 | - |  |  | SI | Turnos |
| Q11 | - |  |  | SI | Comidas al día |
| Q12 | - |  |  | SI | TIPO INSULINA INDICADA |
| Q13 | - |  |  | SI | Insulina Lentas |
| Q14 | - |  |  | SI | Insulina Rápidas |
| Q15 | - |  |  | SI | Otra Insulina |
| Q16 | - |  |  | SI | Dosis y Esquema Indicado |
| Q17 | - |  |  | SI | Horario Insulina |
| Q18 | - |  |  | SI | Tipo de Administración |
| Q19 | - |  |  | SI | Nombre de un Tercero |
| Q20 | - |  |  | SI | Signos de Lipodistrofia |
| Q21 | - |  |  | SI | Sitio Lipodistrofia |
| Q23 | - |  |  | SI | Presencia de Hipoglicemias sobre todo nocturna y c... |
| Q24 | - |  |  | SI | Necesidad de ajuste |
| Q25 | - |  |  | SI | Descripción del Ajuste |
| Q26 | - |  |  | SI | INDICACIONES |
| Q27 | - |  |  | SI | Automonitoreo de glicemias en ayunas-precena y con... |
| Q28 | - |  |  | SI | Mantener controles de salud cardiovascular |
| Q29 | - |  |  | SI | Mantener el tratamiento farmacológico y reforzar e... |
| Q30 | - |  |  | SI | Médico/Urgencia SOS |
| Q31 | - |  |  | SI | Educación |
| Q32 | - |  |  | SI | Agregar imagen con sitio de punción |
| Q33 | - |  |  | SI | Ajuste Insulina |
| Q34 | - |  |  | SI | Otra red de Apoyo |
| Q35 | - |  |  | SI | Con quien Vive |
| Q36 | - |  |  | SI | Horarios y otros de Comida |
| Q37 | - |  |  | SI | Colación al día |
| Q38 | - |  |  | SI | Horarios y otros de Colación |
| Q39 | - |  |  | SI | Educación en particular |
| Q40 | - |  |  | SI | Opciones Ajuste insulina |
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