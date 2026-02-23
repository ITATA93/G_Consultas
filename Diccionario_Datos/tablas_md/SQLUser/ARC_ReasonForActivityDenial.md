# SQLUser.ARC_ReasonForActivityDenial

**Schema:** SQLUser
**Columnas:** 86
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REACTDEN_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Fecha Evaluación |
| Q02 | - |  |  | SI | Hora Evaluación |
| Q03 | - |  |  | SI | Tipo de Familia |
| Q04 | - |  |  | SI | Número de Familia Casa o Sitio |
| Q05 | - |  |  | SI | Número de Personas |
| Q06 | - |  |  | SI | Número de Mujeres |
| Q07 | - |  |  | SI | Número de Hombres |
| Q08 | - |  |  | SI | Número de Adulto Mayor |
| Q09 | - |  |  | SI | Número de Niños |
| Q10 | - |  |  | SI | Número de Adolescentes |
| Q11 | - |  |  | SI | Número de Menores de 1 Año |
| Q12 | - |  |  | SI | Jefatura Hogar |
| Q13 | - |  |  | SI | Autónomo Grupo Familiar ($) |
| Q14 | - |  |  | SI | Aporte Estado ($) |
| Q15 | - |  |  | SI | Total ($) |
| Q16 | - |  |  | SI | Tenencia de la Vivienda |
| Q17 | - |  |  | SI | Tipo de Vivienda |
| Q18 | - |  |  | SI | Número de Dormitorios |
| Q19 | - |  |  | SI | Número de Camas |
| Q20 | - |  |  | SI | Participación Sub-Sistemas |
| Q21 | - |  |  | SI | Factores de Riesgo Otros Integrantes |
| Q22 | - |  |  | SI | Existencia de más de una familia dentro de la Vivi... |
| Q23 | - |  |  | SI | Existencia de más de una familia dentro del sitio |
| Q24 | - |  |  | SI | Comentarios |
| Q25 | - |  |  | SI | Antecedentes de Consumo |
| Q26 | - |  |  | SI | Comentarios - Antecedentes de Consumo |
| Q27 | - |  |  | SI | Antecedentes Judiciales |
| Q28 | - |  |  | SI | Materias |
| Q29 | - |  |  | SI | Vigentes |
| Q30 | - |  |  | SI | Comentarios - Antecedentes Judiciales |
| Q31 | - |  |  | SI | Situación Salud Actual |
| Q32 | - |  |  | SI | Síntesis Diagnóstica |
| Q33 | - |  |  | SI | Profesional Evaluador |
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
| REACTDEN_Code | varchar |  |  | NO | Code |
| REACTDEN_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| REACTDEN_CreatedDate | date |  |  | SI | Created Date |
| REACTDEN_CreatedTime | time |  |  | SI | Created Time |
| REACTDEN_CreatedUser_DR | bigint |  | FK | SI | Created User |
| REACTDEN_DateFrom | date |  |  | SI | Date From |
| REACTDEN_DateTo | date |  |  | SI | Date To |
| REACTDEN_Desc | varchar |  |  | NO | Description |
| REACTDEN_Owner | varchar |  |  | SI | Owner |
| REACTDEN_UpdatedDate | date |  |  | SI | Updated Date |
| REACTDEN_UpdatedTime | time |  |  | SI | Updated Time |
| REACTDEN_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*