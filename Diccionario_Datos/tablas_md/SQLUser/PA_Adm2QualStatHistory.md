# SQLUser.PA_Adm2QualStatHistory

**Schema:** SQLUser
**Columnas:** 79
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Admisión de Pacientes**. Registra episodios de atención hospitalaria. Histórico de cambios.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUAL_ParRef | bigint | PK |  | NO | PA_Adm2 Parent Reference |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Bundle Compliance Percentage |
| Q04 | - |  |  | SI | % |
| Q05 | - |  |  | SI | The Quick Sepsis Organ Failure Assessment must be ... |
| Q06 | - |  |  | SI | Within 1 hour of recognizing sepsis or septic shoc... |
| Q07 | - |  |  | SI | Determination of the lactate level |
| Q08 | - |  |  | SI | If initial lactate is> 2 mmol / L new determinatio... |
| Q09 | - |  |  | SI | Collection of blood cultures samples before antibi... |
| Q10 | - |  |  | SI | Administration of empirical broad spectrum  antimi... |
| Q11 | - |  |  | SI | If patient has hypotension or lactates> 4mmol / L,... |
| Q12 | - |  |  | SI | If patient has hypotension during or after restora... |
| Q13 | - |  |  | SI | After having carried out the above interventions, ... |
| Q14 | - |  |  | SI | Periodic monitoring of clinical conditions, Acid-B... |
| Q15 | - |  |  | SI | Blood chemistry test: Glucose |
| Q16 | - |  |  | SI | Complete blood count: Hemoglobin |
| Q17 | - |  |  | SI | Lymphocytes |
| Q18 | - |  |  | SI | Differential Count of Leukocytes: Neutrophil Granu... |
| Q19 | - |  |  | SI | Coagulation test: Prothrombin time (PT) |
| Q20 | - |  |  | SI | Radiology exams to assess of the source of the inf... |
| Q21 | - |  |  | SI | Comments |
| Q22 | - |  |  | SI | * The diagnosis of sepsis/septic shock coincides w... |
| Q23 | - |  |  | SI | that highlights all the elements of sepsis or sept... |
| Q24 | - |  |  | SI | Score |
| Q25 | - |  |  | SI | Classifiaction |
| Q26 | - |  |  | SI | 0 - 100 |
| Q27 | - |  |  | SI | Higher percetage indicates higher compliance |
| Q28 | - |  |  | SI | 0 - 100: Higher percetage indicates higher complia... |
| Q29 | - |  |  | SI | The SEPSIS prevention bundle is used for decision ... |
| QUAL_Childsub | double |  |  | NO | Childsub |
| QUAL_Date | date |  |  | SI | Date |
| QUAL_DateUpdated | date |  |  | SI | DateUpdated |
| QUAL_HospitalUpdated_DR | bigint |  | FK | SI | Des Ref HospitalUpdated |
| QUAL_QualifStatus_DR | bigint |  | FK | SI | Des Ref QualifStatus |
| QUAL_RowId | varchar |  |  | NO | - |
| QUAL_Time | time |  |  | SI | Time |
| QUAL_TimeUpdated | time |  |  | SI | TimeUpdated |
| QUAL_UserUpdated_DR | bigint |  | FK | SI | Des Ref UserUpdated |
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