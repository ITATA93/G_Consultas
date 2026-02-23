# SQLUser.ARC_ServiceCharge

**Schema:** SQLUser
**Columnas:** 85
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SERCH_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Fecha Evalaución |
| Q02 | - |  |  | SI | Hora Evaluación |
| Q03 | - |  |  | SI | A. ANAMNESIS |
| Q04 | - |  |  | SI | 1. PESO |
| Q05 | - |  |  | SI | Peso Habitual |
| Q06 | - |  |  | SI | Pérdida de peso en los últimos 6 meses |
| Q07 | - |  |  | SI | Cantidad perdida |
| Q08 | - |  |  | SI | % de Pérdida en relación a su peso Habitual |
| Q09 | - |  |  | SI | Las últimas dos semana |
| Q10 | - |  |  | SI | 2. INGESTA ALIMENTARIA CON RELACIÓN A LA HABITUAL |
| Q11 | - |  |  | SI | Ingesta Alimentaria |
| Q12 | - |  |  | SI | Hace cuanto Tiempo (días) |
| Q13 | - |  |  | SI | Tipo de Dieta |
| Q14 | - |  |  | SI | 3. SÍNTOMAS GASTROINTESTINALES |
| Q15 | - |  |  | SI | Presente hace más de 15 días |
| Q16 | - |  |  | SI | Vómitos |
| Q17 | - |  |  | SI | Náuseas |
| Q18 | - |  |  | SI | Diarrea (+ de 3 Evacuaciones liquidas/día) |
| Q19 | - |  |  | SI | Falta de Apetito |
| Q20 | - |  |  | SI | 4. CAPACIDAD FUNCIONAL |
| Q21 | - |  |  | SI | Disfunción |
| Q22 | - |  |  | SI | Hace cuanto tiempo (días) |
| Q23 | - |  |  | SI | Que tipo |
| Q24 | - |  |  | SI | 5. DIAGNÓSTICO PRINCIPAL Y SU RELACIÓN CON LAS NEC... |
| Q25 | - |  |  | SI | Diagnostico Principal |
| Q26 | - |  |  | SI | Demanda Metabólica |
| Q27 | - |  |  | SI | B. EXAMEN FÍSICO |
| Q28 | - |  |  | SI | Pérdida de Grasa Subcutánea |
| Q29 | - |  |  | SI | Pérdida Muscular ( Cuadriceps o Deltoides) |
| Q30 | - |  |  | SI | Edema de Tobillos |
| Q31 | - |  |  | SI | Edema Sacro |
| Q32 | - |  |  | SI | Ascitis |
| Q33 | - |  |  | SI | C. EVALUCIÓN SUBJETIVA |
| Q34 | - |  |  | SI | Resultado Evaluación Subjetiva |
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
| SERCH_Code | varchar |  |  | NO | Code |
| SERCH_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SERCH_CreatedDate | date |  |  | SI | Created Date |
| SERCH_CreatedTime | time |  |  | SI | Created Time |
| SERCH_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SERCH_Desc | varchar |  |  | NO | Description |
| SERCH_Owner | varchar |  |  | SI | Owner |
| SERCH_UpdatedDate | date |  |  | SI | Updated Date |
| SERCH_UpdatedTime | time |  |  | SI | Updated Time |
| SERCH_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*