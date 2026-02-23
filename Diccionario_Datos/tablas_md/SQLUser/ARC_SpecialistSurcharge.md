# SQLUser.ARC_SpecialistSurcharge

**Schema:** SQLUser
**Columnas:** 88
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SPSUR_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Condición |
| Q02 | - |  |  | SI | Criterios |
| Q03 | - |  |  | SI | Trastorno del Equilibrio |
| Q04 | - |  |  | SI | Observación |
| Q05 | - |  |  | SI | Caídas frecuentes |
| Q06 | - |  |  | SI | Observación |
| Q07 | - |  |  | SI | Enfermedad de Parkinson |
| Q08 | - |  |  | SI | Observación |
| Q09 | - |  |  | SI | Artrosis de cadera y rodilla avanzada sin alcance ... |
| Q10 | - |  |  | SI | Observación |
| Q11 | - |  |  | SI | Disnea de esfuerzo que requiera descansos frecuent... |
| Q12 | - |  |  | SI | Observación |
| Q13 | - |  |  | SI | Desviación severa de columna |
| Q14 | - |  |  | SI | Observación |
| Q15 | - |  |  | SI | Indemnidad de extremidades superiores |
| Q16 | - |  |  | SI | Observación |
| Q17 | - |  |  | SI | Adultos mayores con demencia en etapa inicial requ... |
| Q18 | - |  |  | SI | Observación |
| Q19 | - |  |  | SI | Cuadros de demencia en etapa inicial requerirán su... |
| Q20 | - |  |  | SI | Observación |
| Q21 | - |  |  | SI | Compromiso moderado a severo del equilibrio |
| Q22 | - |  |  | SI | Observación |
| Q23 | - |  |  | SI | Residencia en lugar que permita los desplazamiento... |
| Q24 | - |  |  | SI | Observación |
| Q25 | - |  |  | SI | Su entorno (patio y barrio) debe permitir libertad... |
| Q26 | - |  |  | SI | Observación |
| Q27 | - |  |  | SI | No indicar en |
| Q28 | - |  |  | SI | Problemas de: conciencia |
| Q29 | - |  |  | SI | Observación |
| Q30 | - |  |  | SI | Problemas cognitivos |
| Q31 | - |  |  | SI | Observación |
| Q32 | - |  |  | SI | Amputados |
| Q33 | - |  |  | SI | Observación |
| Q34 | - |  |  | SI | Hemipléjicos |
| Q35 | - |  |  | SI | Observación |
| Q36 | - |  |  | SI | Otras Observaciones |
| Q37 | - |  |  | SI | Consideraciones |
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
| SPSUR_CTCPTyp_DR | bigint |  | FK | SI | Des Ref to CTCPType |
| SPSUR_CreatedDate | date |  |  | SI | Created Date |
| SPSUR_CreatedTime | time |  |  | SI | Created Time |
| SPSUR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SPSUR_DateFrom | date |  |  | SI | Date From |
| SPSUR_DateTo | date |  |  | SI | Date To |
| SPSUR_Perc | double |  |  | SI | Percentage |
| SPSUR_UpdatedDate | date |  |  | SI | Updated Date |
| SPSUR_UpdatedTime | time |  |  | SI | Updated Time |
| SPSUR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*