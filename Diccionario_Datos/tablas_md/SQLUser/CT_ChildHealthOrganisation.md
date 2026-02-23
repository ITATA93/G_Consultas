# SQLUser.CT_ChildHealthOrganisation

**Schema:** SQLUser
**Columnas:** 91
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema. Registros hijos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CHORG_RowId | bigint | PK |  | NO | - |
| CHORG_Active | varchar |  |  | SI | Active  |
| CHORG_Code | varchar |  |  | NO | Code |
| CHORG_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CHORG_CreatedDate | date |  |  | SI | Created Date |
| CHORG_CreatedTime | time |  |  | SI | Created Time |
| CHORG_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CHORG_DateFrom | date |  |  | SI | Date From |
| CHORG_DateTo | date |  |  | SI | Date To |
| CHORG_Desc | varchar |  |  | NO | Description |
| CHORG_NationalCode | varchar |  |  | SI | National Code |
| CHORG_Owner | varchar |  |  | SI | Owner |
| CHORG_UpdatedDate | date |  |  | SI | Updated Date |
| CHORG_UpdatedTime | time |  |  | SI | Updated Time |
| CHORG_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Delirios ¿Cree el/la paciente en cosas que no son ... |
| Q02 | - |  |  | SI | Gravedad del Síntoma |
| Q03 | - |  |  | SI | Estrés que a usted le provoca la presencia del sín... |
| Q04 | - |  |  | SI | Alucinaciones. ¿El/la paciente ve cosas o personas... |
| Q05 | - |  |  | SI | Gravedad del Síntoma |
| Q06 | - |  |  | SI | Estrés que a usted le provoca la presencia del sín... |
| Q07 | - |  |  | SI | Agresividad. ¿El/la paciente insulta o se molesta ... |
| Q08 | - |  |  | SI | Gravedad del Síntoma |
| Q09 | - |  |  | SI | Estrés que a usted le provoca la presencia del sín... |
| Q10 | - |  |  | SI | Depresión. ¿El/la paciente está triste o desanimad... |
| Q11 | - |  |  | SI | Gravedad del Síntoma |
| Q12 | - |  |  | SI | Estrés que a usted le provoca la presencia del sín... |
| Q13 | - |  |  | SI | Ansiedad ¿El/la paciente está nervioso, inquieto, ... |
| Q14 | - |  |  | SI | Gravedad del Síntoma |
| Q15 | - |  |  | SI | Estrés que a usted le provoca la presencia del sín... |
| Q16 | - |  |  | SI | Euforia. ¿Parece el/la paciente estar demasiado al... |
| Q17 | - |  |  | SI | Gravedad del Síntoma |
| Q18 | - |  |  | SI | Estrés que a usted le provoca la presencia del sín... |
| Q19 | - |  |  | SI | Apatía. ¿El/la paciente parece poco interesado, po... |
| Q20 | - |  |  | SI | Gravedad del Síntoma |
| Q21 | - |  |  | SI | Estrés que a usted le provoca la presencia del sín... |
| Q22 | - |  |  | SI | Desinhibición. ¿El/la paciente actúa impulsivament... |
| Q23 | - |  |  | SI | Gravedad del Síntoma |
| Q24 | - |  |  | SI | Estrés que a usted le provoca la presencia del sín... |
| Q25 | - |  |  | SI | Irritabilidad. ¿Está el/la paciente irritable o se... |
| Q26 | - |  |  | SI | Gravedad del Síntoma |
| Q27 | - |  |  | SI | Estrés que a usted le provoca la presencia del sín... |
| Q28 | - |  |  | SI | Conducta Motora Anómala. ¿El/la paciente se dedica... |
| Q29 | - |  |  | SI | Gravedad del Síntoma |
| Q30 | - |  |  | SI | Estrés que a usted le provoca la presencia del sín... |
| Q31 | - |  |  | SI | Problema de Sueño. ¿El/la paciente tiene dificulta... |
| Q32 | - |  |  | SI | Gravedad del Síntoma |
| Q33 | - |  |  | SI | Estrés que a usted le provoca la presencia del sín... |
| Q34 | - |  |  | SI | Problemas de Apetito. ¿El/la paciente ha perdido o... |
| Q35 | - |  |  | SI | Gravedad del Síntoma |
| Q36 | - |  |  | SI | Estrés que a usted le provoca la presencia del sín... |
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