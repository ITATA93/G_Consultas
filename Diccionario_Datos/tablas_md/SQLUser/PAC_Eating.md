# SQLUser.PAC_Eating

**Schema:** SQLUser
**Columnas:** 69
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EAT_RowId | bigint | PK |  | NO | - |
| EAT_Code | varchar |  |  | NO | Code |
| EAT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| EAT_CreatedDate | date |  |  | SI | Created Date |
| EAT_CreatedTime | time |  |  | SI | Created Time |
| EAT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| EAT_DateFrom | date |  |  | SI | Date From |
| EAT_DateTo | date |  |  | SI | Date To |
| EAT_Desc | varchar |  |  | NO | Description |
| EAT_NationCode | varchar |  |  | SI | National Code |
| EAT_NumericVal | double |  |  | SI | Numeric Value |
| EAT_Owner | varchar |  |  | SI | Owner |
| EAT_UpdatedDate | date |  |  | SI | Updated Date |
| EAT_UpdatedTime | time |  |  | SI | Updated Time |
| EAT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q1 | - |  |  | SI | Fecha Evaluación |
| Q10 | - |  |  | SI | Pautas |
| Q11 | - |  |  | SI | BOAS 0-5: Realizar una evaluación oral una vez al ... |
| Q12 | - |  |  | SI | BOAS 6-10: Realizar evaluaciones orales dos veces ... |
| Q13 | - |  |  | SI | BOAS 11-15: Realizar una evaluación oral cada turn... |
| Q14 | - |  |  | SI | BOAS 16-20: Realizar una evaluación oral cada 4 ho... |
| Q15 | - |  |  | SI | El cuidado bucal es una actividad básica de atenci... |
| Q2 | - |  |  | SI | Hora Evaluación |
| Q3 | - |  |  | SI | Labios |
| Q4 | - |  |  | SI | Encía y mucosa oral |
| Q5 | - |  |  | SI | Lengua |
| Q6 | - |  |  | SI | Dientes |
| Q7 | - |  |  | SI | Saliva |
| Q8 | - |  |  | SI | Nota: Proporcione humedad con más frecuencia que e... |
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