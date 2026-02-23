# SQLUser.PA_ORAnOpSecondPrcSnapshot

**Schema:** SQLUser
**Columnas:** 79
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PASEC_ParRef | bigint | PK |  | NO | PA_ORAnaestOper Parent Reference |
| PASEC_BodySite_DR | bigint |  | FK | SI | Des Ref OECBodySite |
| PASEC_Childsub | double |  |  | NO | Childsub |
| PASEC_Laterality_DR | bigint |  | FK | SI | Des Ref Laterality |
| PASEC_Operation_DR | bigint |  | FK | SI | Des Ref ORCOperation |
| PASEC_Procedure_DR | bigint |  | FK | SI | Des Ref PACStatePPP |
| PASEC_Qualifier_DR | varchar |  | FK | SI | Des Ref ORCProcedureQualifier |
| PASEC_RowId | varchar |  |  | NO | - |
| Q01 | - |  |  | SI | DATOS DE IDENTIFICACIÓN |
| Q02 | - |  |  | SI | Establecimiento |
| Q03 | - |  |  | SI | Tipo de Enseñanza |
| Q04 | - |  |  | SI | Curso |
| Q05 | - |  |  | SI | Letra Curso |
| Q06 | - |  |  | SI | PREGUNTAS ANTECEDENTES FAMILIARES |
| Q07 | - |  |  | SI | a. Actualmente, ¿vives con tu mamá y papá? |
| Q08 | - |  |  | SI | b. Tienes una enfermedad que te hace faltar al col... |
| Q09 | - |  |  | SI | c. Vives en el mismo hogar con algún familiar que ... |
| Q10 | - |  |  | SI | d. En tu tiempo libre fuera de la escuela ¿partici... |
| Q11 | - |  |  | SI | CUESTIONARIO PSC Y 17 |
| Q12 | - |  |  | SI | 1.&nbsp |
| Q13 | - |  |  | SI | 2.&nbsp |
| Q14 | - |  |  | SI | 3. Eres muy soñador (a) |
| Q15 | - |  |  | SI | 4. Te niegas a compartir |
| Q16 | - |  |  | SI | 5. No comprendes los sentimientos de otros |
| Q17 | - |  |  | SI | 6.&nbsp |
| Q18 | - |  |  | SI | 7.&nbsp |
| Q19 | - |  |  | SI | 8.&nbsp |
| Q20 | - |  |  | SI | 9.&nbsp |
| Q21 | - |  |  | SI | 10.&nbsp |
| Q22 | - |  |  | SI | 11.&nbsp |
| Q23 | - |  |  | SI | 12.&nbsp |
| Q24 | - |  |  | SI | 13.&nbsp |
| Q25 | - |  |  | SI | 14.&nbsp |
| Q26 | - |  |  | SI | 15.&nbsp |
| Q27 | - |  |  | SI | 16.&nbsp |
| Q28 | - |  |  | SI | 17.&nbsp |
| Q29 | - |  |  | SI | Subescala Problemas de Atención (PA) |
| Q30 | - |  |  | SI | Subescala Problemas Internalizantes (PI) |
| Q31 | - |  |  | SI | Subescala Problemas Externalizantes (PE) |
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