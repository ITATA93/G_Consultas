# questionnaire.QCLXXCFVHU

> Valoración Heridas/Úlceras

**Schema:** questionnaire
**Columnas:** 95
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Valoración Heridas/Úlceras

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Diagnóstico |
| Q02 | varchar |  |  | SI | IMC |
| Q02ObsDR | varchar |  | FK | SI | IMC DR |
| Q03 | varchar |  |  | SI | Diabetes |
| Q04 | varchar |  |  | SI | Hipertensión Arterial |
| Q05 | varchar |  |  | SI | Cáncer |
| Q06 | varchar |  |  | SI | Inmunodepresión |
| Q07 | varchar |  |  | SI | Tabaquismo |
| Q08 | varchar |  |  | SI | Drogadicción |
| Q09 | varchar |  |  | SI | Insuficiencia Venosa |
| Q10 | varchar |  |  | SI | Insuficiencia Arterial |
| Q11 | varchar |  |  | SI | Otras |
| Q12 | varchar |  |  | SI | Hematocrito |
| Q13 | varchar |  |  | SI | Hemoglobina |
| Q14 | varchar |  |  | SI | VHS |
| Q15 | varchar |  |  | SI | Albuminemia |
| Q16 | varchar |  |  | SI | Proteinemia |
| Q17 | varchar |  |  | SI | Glicemia |
| Q18 | varchar |  |  | SI | Cultivos |
| Q19 | varchar |  |  | SI | Otros |
| Q20 | varchar |  |  | SI | Antibióticos |
| Q21 | varchar |  |  | SI | Corticoesteroides |
| Q22 | varchar |  |  | SI | Tratamiento anticoagulante |
| Q23 | varchar |  |  | SI | Otros |
| Q24 | varchar |  |  | SI | Aspecto (Obsoleto) |
| Q25 | varchar |  |  | SI | Diámetro (Obsoleto) |
| Q26 | varchar |  |  | SI | Profundidad (Obsoleto) |
| Q27 | varchar |  |  | SI | Cantidad Exudado (Obsoleto) |
| Q28 | varchar |  |  | SI | Calidad Exudado (Obsoleto) |
| Q29 | varchar |  |  | SI | Tejido Esfacelado/Necrótico (Obsoleto) |
| Q30 | varchar |  |  | SI | Tejido Granulatorio (Obsoleto) |
| Q31 | varchar |  |  | SI | Edema (Obsoleto) |
| Q32 | varchar |  |  | SI | Dolor (Obsoleto) |
| Q33 | varchar |  |  | SI | Piel Circundante (Obsoleto) |
| Q34 | varchar |  |  | SI | Agente Utilizado |
| Q35 | varchar |  |  | SI | Apósito o Cobertura |
| Q36 | varchar |  |  | SI | Tipo de Fijación |
| Q37 | varchar |  |  | SI | Describa Antibióticos |
| Q38 | varchar |  |  | SI | Describa Corticoesteroides |
| Q39 | varchar |  |  | SI | Describa Anticoagulantes |
| Q40 | varchar |  |  | SI | Aspecto |
| Q41 | varchar |  |  | SI | Diámetro |
| Q42 | varchar |  |  | SI | Profundidad |
| Q43 | varchar |  |  | SI | Cantidad Exudado |
| Q44 | varchar |  |  | SI | Calidad Exudado |
| Q45 | varchar |  |  | SI | Tejido Esfacelado/Necrótico |
| Q46 | varchar |  |  | SI | Tejido Granulatorio |
| Q47 | varchar |  |  | SI | Edema |
| Q48 | varchar |  |  | SI | Dolor |
| Q49 | varchar |  |  | SI | Piel Circundante |
| Q50 | varchar |  |  | SI | Hemoglobina Glicosilada |
| Q51 | varchar |  |  | SI | mg/dL |
| Q52 | varchar |  |  | SI | mg/dL |
| Q53 | varchar |  |  | SI | % |
| QUESAnaDR | varchar |  | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar |  | FK | SI | Operation |
| QUESConsultDR | varchar |  | FK | SI | Consult |
| QUESCopiedComments | varchar |  |  | SI | Copied Comments |
| QUESCopiedDate | date |  |  | SI | Copied Date |
| QUESCopiedEpDR | bigint |  | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint |  | FK | SI | Copied Source DR |
| QUESCopiedTime | time |  |  | SI | Copied Time |
| QUESCopiedUserDR | bigint |  | FK | SI | Copied User |
| QUESCreateDate | date |  |  | SI | Creation Date |
| QUESCreateTime | time |  |  | SI | Creation Time |
| QUESCreateUserDR | bigint |  | FK | SI | Creation User |
| QUESDate | date |  |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint |  | FK | SI | Error Reason |
| QUESFHResidentDR | bigint |  | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar |  | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar |  | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar |  | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint |  | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar |  | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint |  | FK | SI | Operating Room |
| QUESPAAdmDR | bigint |  | FK | SI | Admission |
| QUESPAAdverseEventDR | varchar |  | FK | SI | Adverse Event |
| QUESPAPatMasDR | bigint |  | FK | SI | Patient |
| QUESPAPregnancyDR | bigint |  | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint |  | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar |  | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar |  | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar |  | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar |  | FK | SI | Appointment Outcome |
| QUESRBApptSlotDR | varchar |  | FK | SI | Appointment Slot |
| QUESReasonForCorrectionDR | bigint |  | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint |  | FK | SI | Questionnaire |
| QUESScore | varchar |  |  | SI | Score |
| QUESSecondUserDR | bigint |  | FK | SI | Second Signature |
| QUESStatusDR | bigint |  | FK | SI | Status |
| QUESTextResultDR | bigint |  | FK | SI | Text Result |
| QUESTime | time |  |  | SI | Last Update Time |
| QUESTransactionDR | varchar |  | FK | SI | Transaction |
| QUESUserDR | bigint |  | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*